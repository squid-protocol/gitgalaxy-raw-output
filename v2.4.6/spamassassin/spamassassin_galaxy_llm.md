# ARCHITECTURAL_BRIEF: spamassassin
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/spamassassin` |
| **Timestamp** | `2026-08-03T19:30:29.824059+00:00` |
| **Scan Duration** | `2.13s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `cd27d984b5eed731d8b4aae0dc654267fc7b9917` |
| **Git Remote** | `https://github.com/apache/spamassassin.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 104 malicious artifacts.

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
| Total Artifacts | 1882 |
| Analyzed Artifacts (Scanned) | 515 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1367 |
| Total LOC | 38852 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 27.4% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7483 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3685 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 335 | 33207 | 65.0% |
| SHELL | 57 | 1965 | 11.1% |
| PLAINTEXT | 45 | 4 | 8.7% |
| MARKDOWN | 25 | 0 | 4.9% |
| SQLITE | 22 | 354 | 4.3% |
| C | 15 | 2643 | 2.9% |
| MAKEFILE | 5 | 205 | 1.0% |
| YAML | 3 | 37 | 0.6% |
| PHP | 2 | 5 | 0.4% |
| M4 | 2 | 144 | 0.4% |
| CSS | 1 | 123 | 0.2% |
| JAVASCRIPT | 1 | 162 | 0.2% |
| XML | 1 | 0 | 0.2% |
| CSV | 1 | 3 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.142`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 225 | 43.7% |
| file_cluster_0 | 102 | 19.8% |
| file_cluster_13 | 93 | 18.1% |
| file_cluster_17 | 13 | 2.5% |
| file_cluster_9 | 5 | 1.0% |
| Unknown | 4 | 0.8% |
| file_cluster_12 | 3 | 0.6% |
| file_cluster_4 | 2 | 0.4% |
| file_cluster_11 | 2 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 66 | 12.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1367*

**Composition by Extension & Reason:**
- `no_extension`: 239x Unsupported Format (.undeterminable), 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.cf`: 234x Excluded (Unsupported Extension: '.cf'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lm`: 172x Excluded (Unsupported Extension: '.lm')
- `.pm`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.eml`: 44x Excluded (Unsupported Extension: '.eml')
- `.msg`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.8`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.1`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC)
- `.3`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pre`: 16x Excluded (Unsupported Extension: '.pre'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.2`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.5`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC), 1x Excluded (Saturation: Line 23 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 55.8 | 69.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 41.8 | 32.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 14.3 | 0.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 68.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 37.9 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 53.9 | 51.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `masses/mass-check` (Hits: 118)
- `masses/rule-dev/sought/mkzone_remote_svn/run` (Hits: 55)
- `masses/rule-dev/sought/mkzone/run_part2` (Hits: 52)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rules** (`debian/rules`) — 7 inbound connections
2. **utils.h** (`spamc/utils.h`) — 3 inbound connections
3. **date.t** (`t/date.t`) — 2 inbound connections
4. **utf8.t** (`t/utf8.t`) — 2 inbound connections
5. **spamassassin.install** (`debian/spamassassin.install`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mass-check** (`masses/mass-check`) — 45 outbound dependencies
2. **spamc.c** (`spamc/spamc.c`) — 28 outbound dependencies
3. **ruleqa.cgi** (`masses/rule-qa/automc/ruleqa.cgi`) — 24 outbound dependencies
4. **libspamc.c** (`spamc/libspamc.c`) — 24 outbound dependencies
5. **SIQ.pm** (`rulesrc/sandbox/dos/SIQ.pm`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `usage` (@ `masses/mass-check`) -> Impact: **4819.6** | LOC: 1782
- `show_default_view` (@ `masses/rule-qa/automc/ruleqa.cgi`) -> Impact: **3559.6** | LOC: 1852
- `main` (@ `masses/garescorer.c`) -> Impact: **1172.0** | LOC: 767
- `tryone` (@ `t/cidrs.t`) -> Impact: **1128.5** | LOC: 130
- `init` (@ `masses/rule-qa/corpus-hourly`) -> Impact: **1096.1** | LOC: 442
- `parse_arg` (@ `Makefile.PL`) -> Impact: **884.7** | LOC: 385
- `init` (@ `masses/rule-qa/reports-from-logs`) -> Impact: **867.9** | LOC: 319
  * *Intent:* # ---------------------------------------------------------------------------
- `_message_read_bsmtp` (@ `spamc/libspamc.c`) -> Impact: **631.9** | LOC: 479
- `set_all_confs` (@ `t/cross_user_config_leak.t`) -> Impact: **608.0** | LOC: 86
  * *Intent:* # ---------------------------------------------------------------------------
- `compute_overlaps_for_rule` (@ `masses/hit-frequencies`) -> Impact: **574.7** | LOC: 225

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `usage` (@ `masses/log-grep-recent`) -> **O(2^N) [Recursive]**
  * *Intent:* #!/usr/bin/perl # # log-grep-recent - select only recent messages from a mass-check log # [optionally only select messages with set=x]...
- `usage` (@ `masses/rule-qa/rule-hits-over-time`) -> **O(2^N) [Recursive]**
- `_evaluate_at_all_thresholds` (@ `masses/mk-roc-graphs`) -> **O(2^N) [Recursive]**
- `usage` (@ `masses/corpora/mk-corpus-link-farm`) -> **O(2^N) [Recursive]**
- `usage` (@ `masses/mass-check`) -> **O(2^N) [Recursive]**
- `start_hit_frequencies_at_rev` (@ `masses/rule-qa/reports-from-logs`) -> **O(2^N) [Recursive]**
  * *Intent:* # ---------------------------------------------------------------------------
- `usage` (@ `t.rules/run`) -> **O(2^N) [Recursive]**
- `reload` (@ `debian/spamassassin-maint.sh`) -> **O(2^N) [Recursive]**
  * *Intent:* # Tell a running spamd to reload its configs and rules.
- `finish` (@ `masses/plugins/HitFreqsRuleTiming.pm`) -> **O(2^N) [Recursive]**
- `new_score_line` (@ `masses/rewrite-cf-with-new-scores`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `usage` (@ `masses/mass-check`) -> DB Complexity: **620**
- `show_default_view` (@ `masses/rule-qa/automc/ruleqa.cgi`) -> DB Complexity: **489**
- `main` (@ `masses/garescorer.c`) -> DB Complexity: **225**
- `init` (@ `masses/rule-qa/corpus-hourly`) -> DB Complexity: **207**
- `make_tarball_for_version_[Truncated]` (@ `masses/rule-dev/sought/mkzone/run_part2`) -> DB Complexity: **165**
  * *Intent:* # ---------------------------------------------------------------------------
- `Anonymous_Block_[Truncated]` (@ `masses/bayes-testing/bayes-10pcv-driver`) -> DB Complexity: **143**
- `setup_masscheck_[Truncated]` (@ `masses/contrib/automasscheck-minimal/automasscheck-minimal.sh`) -> DB Complexity: **139**
  * *Intent:* # to you under the Apache License, Version 2.0 (the # "License"); you may not use this file except in compliance # with the License. You may obtain a ...
- `make_tarball_for_version` (@ `masses/rule-dev/sought/mkzone_remote_svn/run`) -> DB Complexity: **132**
  * *Intent:* # ---------------------------------------------------------------------------
- `Anonymous_Block_[Truncated]` (@ `spamd/suse-ancient-rc-script.sh`) -> DB Complexity: **132**
  * *Intent:* # Note: The SuSE {start,kill,check}proc utils can't handle perl scripts # which change there $0 -- like spamd. So I implemented my own # routines whic...
- `_message_read_bsmtp` (@ `spamc/libspamc.c`) -> DB Complexity: **123**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 227 | 24110.52 | 53.88% | 17.47% |
| `masses` | 36 | 15227.78 | 72.57% | 16.73% |
| `spamd-apache2/t/certs` | 3 | 10062.04 | 1.97% | 0.0% |
| `xt` | 3 | 6311.64 | 56.19% | 39.53% |
| `masses/rule-qa/automc` | 6 | 5693.63 | 42.34% | 18.41% |
| `debian` | 10 | 5249.6 | 7.34% | 9.01% |
| `t/data/etc` | 2 | 5001.0 | 0.0% | 0.0% |
| `masses/rule-qa` | 14 | 4810.52 | 68.44% | 50.15% |
| `spamd-apache2/bin` | 3 | 4348.3 | 58.81% | 94.65% |
| `spamc` | 16 | 3794.18 | 35.56% | 26.06% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/perlcritic.t` -> **100.0%** Exposure
- `t/spamc_bug6176.t` -> **100.0%** Exposure
- `t/spamc_x_e.t` -> **100.0%** Exposure
- `t/spamc_y.t` -> **100.0%** Exposure
- `t/spamd_maxsize.t` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Makefile.PL` -> **100.0%** Exposure
- `contrib/mbox-to-check` -> **100.0%** Exposure
- `contrib/samailoffset` -> **100.0%** Exposure
- `debian/bin/genorig.pl` -> **100.0%** Exposure
- `masses/bayes-testing/bayes-static-thresholds` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contrib/run-corpora` -> **1** Orphaned Functions | **14** Duplicates
- `sql/bayes_pg.sql` -> **2** Orphaned Functions | **11** Duplicates
- `masses/rule-qa/automc/sorttable.js` -> **6** Orphaned Functions | **4** Duplicates
- `sql/neural_pg.sql` -> **0** Orphaned Functions | **9** Duplicates
- `spamd/netbsd-rc-script.sh` -> **1** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`spamc/spamc.c`** -> AI Confidence: **99.48%**
2. **`masses/evolve_metarule/evolve_metarule.c`** -> AI Confidence: **99.39%**
3. **`spamc/libspamc.c`** -> AI Confidence: **99.39%**
4. **`masses/garescorer.c`** -> AI Confidence: **99.34%**
5. **`spamc/qmail-spamc.c`** -> AI Confidence: **99.32%**
6. **`masses/perceptron.c`** -> AI Confidence: **99.31%**
7. **`spamc/utils.c`** -> AI Confidence: **99.31%**
8. **`contrib/kill-spamd.sh`** -> AI Confidence: **99.29%**
9. **`masses/bayes-testing/benchmark/helper/mysql/dbsize`** -> AI Confidence: **99.29%**
10. **`masses/bayes-testing/benchmark/helper/pgsql/dbsize`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Makefile.PL` -> **100.0%** Exposure
- `debian/bin/genorig.pl` -> **100.0%** Exposure
- `masses/bayes-testing/bayes-static-thresholds` -> **100.0%** Exposure
- `masses/bayes-testing/map-s-space/bayes-analyse-from-raw-counts` -> **100.0%** Exposure
- `masses/corpora/mass-find-nonspam` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `contrib/mbox-to-check` -> **100.0%** Exposure
- `masses/bayes-testing/graph-accuracy-curve` -> **100.0%** Exposure
- `masses/bayes-testing/graph-bayes-histogram` -> **100.0%** Exposure
- `masses/bayes-testing/map-s-space/run-search` -> **100.0%** Exposure
- `masses/compare-models` -> **100.0%** Exposure
### Raw Memory Manipulation
- `spamc/libspamc.c` -> **9.9998%** Exposure
- `spamc/libspamc.h` -> **0.0072%** Exposure
- `masses/evolve_metarule/evolve_metarule.c` -> **0.0002%** Exposure
- `spamc/getopt.c` -> **0.0002%** Exposure
### Algorithmic DoS Exposure
- `Makefile.PL` -> **100.0%** Exposure
- `masses/bayes-testing/map-s-space/bayes-analyse-from-raw-counts` -> **100.0%** Exposure
- `masses/hit-frequencies` -> **100.0%** Exposure
- `masses/lint-rules-from-freqs` -> **100.0%** Exposure
- `masses/log-grep-recent` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `91` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1734` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `masses/plugins/HitFreqsRuleTiming.pm` (PERL) -> Cumulative Risk: **960.36**
- **Archetype:** `file_cluster_0` (Distance: 13.613 IQR)
- **Magnitude:** 193.82 | **LOC:** 122 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `finish` (Impact: 70.0), `ran_rule` (Impact: 19.4), `new` (Impact: 12.0)

### 2. `backend/nitemc/extract_to_rsync_dir` (SHELL) -> Cumulative Risk: **933.53**
- **Archetype:** `file_cluster_4` (Distance: 14.6 IQR)
- **Magnitude:** 66.28 | **LOC:** 63 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 31.3), `Anonymous_Block` (Impact: 3.2), `Anonymous_Block` (Impact: 3.2)

### 3. `masses/mass-check` (PERL) -> Cumulative Risk: **902.84**
- **Archetype:** `file_cluster_0` (Distance: 14.949 IQR)
- **Magnitude:** 7284.92 | **LOC:** 2679 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `usage` (Impact: 4819.6), `client_mode` (Impact: 554.4), `server_mode` (Impact: 104.0)

### 4. `masses/rule-qa/import-logs` (PERL) -> Cumulative Risk: **864.9**
- **Archetype:** `file_cluster_0` (Distance: 11.86 IQR)
- **Magnitude:** 240.38 | **LOC:** 158 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `init` (Impact: 172.2), `configure` (Impact: 10.9)

### 5. `masses/runGA` (SHELL) -> Cumulative Risk: **825.0**
- **Archetype:** `file_cluster_8` (Distance: 11.357 IQR)
- **Magnitude:** 108.48 | **LOC:** 184 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), State Flux (99.999%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 63.1), `Anonymous_Block` (Impact: 3.1), `__global_context__` (Impact: 3.1)

### 6. `masses/rule-qa/get-rulemetadata-for-revision` (PERL) -> Cumulative Risk: **824.05**
- **Archetype:** `file_cluster_13` (Distance: 12.462 IQR)
- **Magnitude:** 119.92 | **LOC:** 137 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `svn_and_build` (Impact: 33.7), `usage` (Impact: 9.3), `configure` (Impact: 8.8)

### 7. `masses/rule-qa/corpus-nightly` (SHELL) -> Cumulative Risk: **821.33**
- **Archetype:** `file_cluster_11` (Distance: 13.082 IQR)
- **Magnitude:** 97.02 | **LOC:** 100 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.9991%), Tech Debt (98.6106%)
- **Heaviest Functions:** `__global_context__` (Impact: 72.8)

### 8. `masses/rule-qa/reports-from-logs` (PERL) -> Cumulative Risk: **811.59**
- **Archetype:** `file_cluster_17` (Distance: 13.436 IQR)
- **Magnitude:** 1685.4 | **LOC:** 714 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `init` (Impact: 867.9), `start_hit_frequencies_at_rev` (Impact: 383.2), `configure` (Impact: 23.1)

### 9. `masses/rule-qa/automc/sorttable.js` (JAVASCRIPT) -> Cumulative Risk: **811.25**
- **Archetype:** `file_cluster_17` (Distance: 15.104 IQR)
- **Magnitude:** 267.34 | **LOC:** 496 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9998%), Tech Debt (99.9541%)
- **Heaviest Functions:** `forEach` (Impact: 37.0), `shaker_sort` (Impact: 36.1), `dean_addEvent` (Impact: 29.1)

### 10. `masses/rule-qa/corpus-hourly` (PERL) -> Cumulative Risk: **805.44**
- **Archetype:** `file_cluster_17` (Distance: 13.789 IQR)
- **Magnitude:** 1442.44 | **LOC:** 524 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `init` (Impact: 1096.1), `configure` (Impact: 12.9), `clean_up` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `masses/mass-check` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.949 IQR)
- **Top Global Matches:** file_cluster_0: 14.949, file_cluster_11: 15.204, file_cluster_13: 15.322
- **Magnitude:** 7284.92 | **LOC:** 2679 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 620
- **Risk Profile:** Cognitive Load (99.1449%), Tech Debt (10.5525%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 4819.6 | O(2^N) | DB: 620)
  * `client_mode` (Impact: 554.4 | O(N^5) | DB: 111)
    * *Intent:* # this is the function that implements client mode. generally, in a loop: # make a request of the se...
  * `server_mode` (Impact: 104.0 | O(N^3) | DB: 73)
    * *Intent:* ############################################################################ # this is the function ...
  * `scan_client_cache` (Impact: 50.5 | O(N^1) | DB: 17)
    * *Intent:* # scan the client's cache and return a path to a gzip archive of AI output
  * `generate_queue` (Impact: 44.6 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1032`, `structural_boundaries: 389`, `args: 27`, `func_start: 39`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 1529`, `dead_code: 26`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 118`, `concurrency: 36`, `import: 39`
* *Defense:* `safety: 7`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Getopt::Long, POSIX, other, message, FindBin, for, cached, SSL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dnsbl_subtests.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.04 IQR)
- **Top Global Matches:** file_cluster_0: 12.04, file_cluster_4: 12.466, file_cluster_13: 12.48
- **Magnitude:** 6333.18 | **LOC:** 390 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.8838%), Tech Debt (71.4362%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 49`, `args: 11`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 103`, `dead_code: 3`, `fragile_debt: 6`
* *Architecture:* `io: 5`, `concurrency: 12`, `import: 14`
* *Defense:* `safety: 5`, `test: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vars, lib, re, warnings, strict, Net::DNS::Nameserver, SATest, longer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/20_saw_ampersand.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.821 IQR)
- **Top Global Matches:** file_cluster_0: 10.821, file_cluster_13: 11.722, file_cluster_8: 11.744
- **Magnitude:** 6274.7 | **LOC:** 230 | **CtrlFlow:** 94.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (72.4104%), Tech Debt (18.594%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 21`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 37`, `planned_debt: 1`
* *Architecture:* `io: 11`, `import: 7`
* *Defense:* `safety: 3`, `test: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lib, Carp, strict, debug, SATest, longer, of, Devel::SawAmpersand...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/automc/ruleqa.cgi` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.175 IQR)
- **Top Global Matches:** file_cluster_0: 14.175, file_cluster_17: 14.178, file_cluster_8: 14.197
- **Magnitude:** 5241.44 | **LOC:** 2189 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 489
- **Risk Profile:** Cognitive Load (80.3307%), Tech Debt (10.5063%)
**Top Internal Functions/Classes:**
  * `show_default_view` (Impact: 3559.6 | O(N^6) | DB: 489)
  * `read_automc_global_conf` (Impact: 460.2 | O(N^5) | DB: 18)
    * *Intent:* # ---------------------------------------------------------------------------
  * `new` (Impact: 21.5 | O(2^N) | DB: 4)
  * `hide_header` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 421`, `args: 64`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 1165`, `dead_code: 6`, `fragile_debt: 3`
* *Architecture:* `io: 34`, `api: 1`, `import: 18`
* *Defense:* `safety: 12`, `doc: 1`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` POSIX, date, Time::Local, CGI, need, Compress::LZ4, info, parms...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `debian/GPG.KEY` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamd-apache2/t/certs/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamd-apache2/t/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/data/etc/testhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamd-apache2/bin/apache-spamd.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.697 IQR)
- **Top Global Matches:** file_cluster_0: 13.697, file_cluster_13: 13.994, file_cluster_8: 14.023
- **Magnitude:** 4058.4 | **LOC:** 368 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.2924%), Tech Debt (99.5369%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 36`, `args: 3`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 258`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `io: 7`, `import: 7`
* *Defense:* `safety: 1`, `doc: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` point, strict, Mail::SpamAssassin::Spamd::Config, Mail::SpamAssassin::Util, File::Spec, Cwd, DESTROY, Sys::Hostname...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mkrules.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.88 IQR)
- **Top Global Matches:** file_cluster_8: 11.88, file_cluster_0: 11.907, file_cluster_13: 12.212
- **Magnitude:** 3015.51 | **LOC:** 476 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.731%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 41`, `args: 10`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 146`
* *Architecture:* `io: 2`, `import: 8`
* *Defense:* `test: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, File::Path, SATest, this, Test::More, Mail::SpamAssassin::Plugin, File::Copy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/bayessql.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.08 IQR)
- **Top Global Matches:** file_cluster_0: 13.08, file_cluster_13: 13.171, file_cluster_8: 13.249
- **Magnitude:** 2545.1 | **LOC:** 559 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.5571%), Tech Debt (14.429%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 89`, `args: 2`, `func_start: 4`
* *Risk/State:* `state_mutation: 268`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `import: 13`
* *Defense:* `safety: 3`, `test: 54`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Find, lib, SATest, this, constant, Test::More, Redis, DBD::SQLite...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/garescorer.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.858 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.047 IQR)
- **Top Global Matches:** file_cluster_8: 13.858, file_cluster_13: 14.031, file_cluster_7: 14.117
- **Magnitude:** 2045.56 | **LOC:** 1314 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (86.2567%), Tech Debt (26.0257%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 1172.0 | O(N^6) | DB: 225)
  * `usage` (Impact: 15.1 | O(2^N) | DB: 7)
    * *Intent:* #endif
  * `init_data` (Impact: 3.5 | O(N^1) | DB: 2)
  * `load_scores_into_lookup` (Impact: 2.5 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 35`, `args: 5`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 717`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 120`, `import: 6`
* *Defense:* `doc: 6`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time.h, pgapack.h, tests.h, math.h, scores.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/libspamc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.719 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.189 IQR)
- **Top Global Matches:** file_cluster_13: 13.719, file_cluster_8: 13.84, file_cluster_0: 13.992
- **Magnitude:** 1983.22 | **LOC:** 2465 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 123
- **Risk Profile:** Cognitive Load (92.6598%), Tech Debt (47.6978%)
**Top Internal Functions/Classes:**
  * `_message_read_bsmtp` (Impact: 631.9 | O(N^5) | DB: 123)
  * `_opensocket` (Impact: 391.1 | O(2^N) | DB: 30)
    * *Intent:* #include <syslog.h> #include <unistd.h> #include <sys/types.h> #include <sys/socket.h> #include <net...
  * `_try_to_connect_unix` (Impact: 170.5 | O(N^6) | DB: 27)
  * `_try_ssl_connect` (Impact: 33.2 | O(N^3) | DB: 4)
    * *Intent:* #ifdef SPAMC_HAS_ADDRINFO
  * `_try_ssl_ctx_init` (Impact: 22.0 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 87`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 522`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 7`
* *Architecture:* `io: 12`, `api: 157`, `import: 24`
* *Defense:* `safety: 17`, `test: 7`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` tcp.h, time.h, unistd.h, utils.h, stdio.h, in.h, types.h, un.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.421 IQR)
- **Top Global Matches:** file_cluster_0: 12.421, file_cluster_8: 12.732, file_cluster_13: 12.87
- **Magnitude:** 1858.72 | **LOC:** 1141 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (68.6144%), Tech Debt (79.0084%)
**Top Internal Functions/Classes:**
  * `parse_arg` (Impact: 884.7 | O(2^N) | DB: 29)
  * `MY` (Impact: 511.7 | O(N^5) | DB: 46)
    * *Intent:* # Now override the constants routine to add our own macros.
  * `float_to_version` (Impact: 68.0 | O(N^1) | DB: 31)
    * *Intent:* # Converts a version represented as a float to a real three-part version, # eg.: # 5.006001 -> 5.6.1...
  * `MY` (Impact: 17.6 | O(N^1) | DB: 4)
    * *Intent:* # Override the install routine to add our additional install dirs and # hack DESTDIR support into ol...
  * `MY` (Impact: 14.8 | O(N^4) | DB: 3)
    * *Intent:* # Override the libscan routine so it skips SVN/CVS stuff and some common # patch/backup extensions.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 136`, `args: 8`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 332`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `import: 11`
* *Defense:* `safety: 8`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, warnings, for, parameters, strict, Config, TEST_REQUIRES, this...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/reports-from-logs` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.436 IQR)
- **Top Global Matches:** file_cluster_17: 13.436, file_cluster_0: 13.463, file_cluster_13: 13.505
- **Magnitude:** 1685.4 | **LOC:** 714 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 109
- **Risk Profile:** Cognitive Load (96.7628%), Tech Debt (17.5937%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 867.9 | O(N^5) | DB: 109)
    * *Intent:* # ---------------------------------------------------------------------------
  * `start_hit_frequencies_at_rev` (Impact: 383.2 | O(2^N) | DB: 74)
    * *Intent:* # ---------------------------------------------------------------------------
  * `configure` (Impact: 23.1 | O(N^3) | DB: 17)
    * *Intent:* # ---------------------------------------------------------------------------
  * `get_rulemetadata_for_revision` (Impact: 21.8 | O(N^5) | DB: 4)
    * *Intent:* # ---------------------------------------------------------------------------
  * `create_outputdir` (Impact: 7.5 | O(N^1) | DB: 5)
    * *Intent:* # ---------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 152`, `args: 14`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 361`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 32`, `import: 14`
* *Defense:* `safety: 3`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, POSIX, revision, File::Path, rtype, scoreset, time, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/corpus-hourly` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.789 IQR)
- **Top Global Matches:** file_cluster_17: 13.789, file_cluster_0: 13.869, file_cluster_13: 14.014
- **Magnitude:** 1442.44 | **LOC:** 524 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 207
- **Risk Profile:** Cognitive Load (91.8134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 1096.1 | O(N^5) | DB: 207)
  * `configure` (Impact: 12.9 | O(N^2) | DB: 17)
  * `clean_up` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 112`, `args: 3`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 324`, `dead_code: 4`
* *Architecture:* `io: 40`, `import: 11`
* *Defense:* `safety: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, POSIX, File::Path, new, svn, strict, longer, constant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cross_user_config_leak.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.091 IQR)
- **Top Global Matches:** file_cluster_0: 12.091, file_cluster_13: 12.663, file_cluster_17: 12.691
- **Magnitude:** 1193.74 | **LOC:** 263 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (90.0523%), Tech Debt (47.7806%)
**Top Internal Functions/Classes:**
  * `set_all_confs` (Impact: 608.0 | O(N^4) | DB: 4)
    * *Intent:* # ---------------------------------------------------------------------------
  * `validate_all_confs` (Impact: 468.2 | O(N^4) | DB: 10)
  * `assert_validation` (Impact: 34.6 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 44`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 79`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, warnings, strict, SATest, the, Test::More, Mail::SpamAssassin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rulesrc/sandbox/dos/SIQ.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.932 IQR)
- **Top Global Matches:** file_cluster_0: 12.932, file_cluster_13: 13.207, file_cluster_8: 13.351
- **Magnitude:** 1158.08 | **LOC:** 1162 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (62.8079%), Tech Debt (13.4463%)
**Top Internal Functions/Classes:**
  * `set_config` (Impact: 384.8 | O(N^2) | DB: 41)
  * `siq_score` (Impact: 82.2 | O(2^N) | DB: 2)
  * `siq_ip_score` (Impact: 82.2 | O(2^N) | DB: 2)
  * `siq_domain_score` (Impact: 82.2 | O(2^N) | DB: 2)
  * `siq_relative_score` (Impact: 82.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 186`, `args: 25`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 327`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 22`, `api: 1`, `import: 23`
* *Defense:* `safety: 2`, `doc: 39`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Outbound, suitable, port, warnings, strict, Mail::SpamAssassin::Logger, this, first...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/hit-frequencies` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.304 IQR)
- **Top Global Matches:** file_cluster_8: 13.304, file_cluster_17: 13.406, file_cluster_13: 13.422
- **Magnitude:** 1152.48 | **LOC:** 1036 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (71.8257%), Tech Debt (11.3024%)
**Top Internal Functions/Classes:**
  * `compute_overlaps_for_rule` (Impact: 574.7 | O(N^6) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 187`, `args: 8`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 563`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `import: 6`
* *Defense:* `safety: 5`, `doc: 18`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Getopt::Long, warnings, hits, FindBin, strict, this, less, results...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cidrs.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.135 IQR)
- **Top Global Matches:** file_cluster_0: 10.135, file_cluster_13: 10.486, file_cluster_8: 10.548
- **Magnitude:** 1148.92 | **LOC:** 152 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (58.792%), Tech Debt (73.3489%)
**Top Internal Functions/Classes:**
  * `tryone` (Impact: 1128.5 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 17`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 18`, `fragile_debt: 2`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, strict, SATest, constant, Test::More, Net::CIDR::Lite, Mail::SpamAssassin::NetSet, Mail::SpamAssassin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/header_utf8.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.113 IQR)
- **Top Global Matches:** file_cluster_8: 10.113, file_cluster_0: 10.151, file_cluster_13: 10.325
- **Magnitude:** 1144.72 | **LOC:** 233 | **CtrlFlow:** 90.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (60.2561%), Tech Debt (79.931%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 11`, `func_start: 1`
* *Risk/State:* `state_mutation: 21`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `import: 9`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Net::LibIDN, Email::Address::XS, SATest, constant, Test::More, Net::LibIDN2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-dev/seek-phrases-in-log` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.824 IQR)
- **Top Global Matches:** file_cluster_17: 13.824, file_cluster_0: 13.887, file_cluster_11: 13.997
- **Magnitude:** 1042.94 | **LOC:** 710 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (81.0171%), Tech Debt (15.2667%)
**Top Internal Functions/Classes:**
  * `collapse_pats` (Impact: 221.2 | O(N^3) | DB: 64)
  * `assemble_regexps` (Impact: 96.4 | O(N^3) | DB: 36)
  * `filter_into_message_subsets` (Impact: 87.9 | O(N^6) | DB: 22)
  * `usage` (Impact: 46.8 | O(2^N) | DB: 16)
    * *Intent:* # (the "License"); you may not use this file except in compliance with # the License. You may obtain...
  * `proc_text_spam` (Impact: 29.5 | O(N^2) | DB: 15)
    * *Intent:* # --------------------------------------------------------------------------- # PHASE 1: PARSING, NG...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 115`, `args: 11`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 515`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `io: 12`, `import: 5`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, non, warnings, Data::Dumper, strict, this, longer, N...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spamc/getopt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.046 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.109 IQR)
- **Top Global Matches:** file_cluster_13: 13.046, file_cluster_8: 13.119, file_cluster_11: 13.286
- **Magnitude:** 946.34 | **LOC:** 352 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (82.4617%), Tech Debt (14.0027%)
**Top Internal Functions/Classes:**
  * `spamc_getopt_long` (Impact: 365.5 | O(N^5) | DB: 32)
  * `main` (Impact: 106.5 | O(N^5) | DB: 16)
  * `spamc_getopt` (Impact: 87.9 | O(N^3) | DB: 23)
  * `optiserr` (Impact: 70.2 | O(N^3) | DB: 1)
    * *Intent:* * </@LICENSE> */ #include <stdio.h> #include <string.h> #include <assert.h> #include <stdlib.h> #inc...
  * `longoptiserr` (Impact: 59.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 35`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 215`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 6`
* *Defense:* `safety: 4`, `test: 3`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdio.h, errno.h, stdlib.h, assert.h, string.h, getopt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rewrite-cf-with-new-scores` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.133 IQR)
- **Top Global Matches:** file_cluster_0: 13.133, file_cluster_13: 13.236, file_cluster_8: 13.283
- **Magnitude:** 842.06 | **LOC:** 522 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (78.5731%), Tech Debt (11.8035%)
**Top Internal Functions/Classes:**
  * `new_score_line` (Impact: 507.6 | O(2^N) | DB: 25)
  * `read_oldscores` (Impact: 20.0 | O(N^2) | DB: 18)
  * `read_gascores` (Impact: 17.4 | O(N^1) | DB: 11)
  * `read_ranges_data` (Impact: 9.9 | O(N^2) | DB: 9)
  * `readline_gen` (Impact: 7.1 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 69`, `args: 6`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 252`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 11`, `import: 5`
* *Defense:* `safety: 2`, `doc: 6`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, warnings, new, GA, strict, this, options, the...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `masses/rule-qa/rule-hits-over-time` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.333 IQR)
- **Top Global Matches:** file_cluster_13: 13.333, file_cluster_0: 13.363, file_cluster_8: 13.389
- **Magnitude:** 676.08 | **LOC:** 530 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (83.4021%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_gp` (Impact: 143.4 | O(N^4) | DB: 62)
  * `usage` (Impact: 77.8 | O(2^N) | DB: 9)
  * `read_logs` (Impact: 43.3 | O(N^2) | DB: 31)
  * `summarise` (Impact: 29.2 | O(N^2) | DB: 14)
  * `collapse_periods` (Impact: 15.2 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 98`, `args: 4`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 357`, `dead_code: 1`
* *Architecture:* `io: 15`, `import: 10`
* *Defense:* `safety: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.88
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, Statistics::DEA, POSIX, warnings, Fcntl, strict, it, this...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `masses/rule-qa/automc/ruleqa.cgi` (PERL) | Magnitude: 5241.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1427, state_mutation: 1165, branch: 538, structural_boundaries: 421
- `t/db_awl_path_welcome_block.t` (PERL) | Magnitude: 22.66 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 14, structural_boundaries: 8, state_mutation: 7, decorators: 7
- `masses/rule-qa/import-logs` (PERL) | Magnitude: 240.38 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 55, branch: 47, structural_boundaries: 29
- `masses/corpora/mk-corpus-link-farm` (PERL) | Magnitude: 575.52 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 460, state_mutation: 406, branch: 237, structural_boundaries: 174
- `tools/mboxsplit` (PERL) | Magnitude: 0.06 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 42, branch: 22, indent_spaces: 11, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `contrib/run-masses` (SHELL) | Magnitude: 0.53 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 31, safety_bypasses: 14, branch: 9, indent_spaces: 7
- `masses/rule-qa/corpus-nightly` (SHELL) | Magnitude: 97.02 | Delta: **0.285 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 23, io: 21, state_mutation: 21, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/github/apply_pr.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 25, state_mutation: 12, structural_boundaries: 11, branch: 9
- `masses/contrib/automasscheck-minimal/automasscheck-minimal.sh` (SHELL) | Magnitude: 1.55 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 58, io: 39, branch: 30
- `spamd/netbsd-rc-script.sh` (SHELL) | Magnitude: 111.5 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 62, indent_tabs: 50, reflection_metaprogramming: 37, branch: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/askdns.t` (PERL) | Magnitude: 21.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, branch: 20, decorators: 10, bitwise_ops: 10
- `t/idn_dots.t` (PERL) | Magnitude: 97.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 53, indent_spaces: 51, state_mutation: 48, structural_boundaries: 26
- `t/spamc_c_stdout_closed.t` (PERL) | Magnitude: 3.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, bitwise_ops: 4, branch: 3
- `t/spamd_prefork_stress_2.t` (PERL) | Magnitude: 33.76 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, branch: 15, indent_spaces: 9, structural_boundaries: 7
- `contrib/samailoffset` (PERL) | Magnitude: 0.58 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 42, branch: 28, indent_spaces: 22, bitwise_ops: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `masses/freqdiff` (PERL) | Magnitude: 140.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 111, branch: 76, indent_tabs: 46, indent_spaces: 44
- `masses/mboxget` (PERL) | Magnitude: 148.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 66, branch: 60, structural_boundaries: 17
- `masses/evolve_metarule/preproc.pl` (PERL) | Magnitude: 82.46 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 66, branch: 38, indent_tabs: 30, structural_boundaries: 26
- `masses/rule-qa/reports-from-logs` (PERL) | Magnitude: 1685.4 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 424, state_mutation: 361, branch: 195, structural_boundaries: 152
- `masses/cpucount` (PERL) | Magnitude: 31.04 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 34, branch: 33, io: 21, bitwise_ops: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/spamd_prefork_stress_4.t` (PERL) | Magnitude: 46.92 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, state_mutation: 30, branch: 24, structural_boundaries: 16
- `backend/nitemc/extract_to_rsync_dir` (SHELL) | Magnitude: 66.28 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: safety_bypasses: 25, state_mutation: 22, branch: 18, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `masses/bayes-testing/map-s-space/bayes-analyse-from-raw-counts` (PERL) | Magnitude: 71.71 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 387, indent_spaces: 238, structural_boundaries: 103, branch: 87
- `t/spamd_hup.t` (PERL) | Magnitude: 24.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, branch: 13, test: 10, state_mutation: 9
- `t/dmarc.t` (PERL) | Magnitude: 16.52 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 61, decorators: 29, indent_spaces: 12, structural_boundaries: 10
- `masses/lint-rules-from-freqs` (PERL) | Magnitude: 498.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 195, branch: 172, bitwise_ops: 49
- `t/body_str.t` (PERL) | Magnitude: 90.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 58, regex_execution: 34, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sql/neural_pg.sql` (SQLITE) | Magnitude: 10.96 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, duplicate_logic: 9, func_start: 7, class_start: 2
- `sql/decodeshorturl_mysql.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 5, class_start: 1, safety: 1, dead_code: 1
- `sql/decodeshorturl_pg.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, class_start: 1, safety: 1, dead_code: 1
- `sql/redirectors_mysql.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 5, class_start: 1, safety: 1, dead_code: 1
- `sql/redirectors_pg.sql` (SQLITE) | Magnitude: 1.56 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, class_start: 1, safety: 1, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/bayessql.t` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 2545.1
- `masses/rule-qa/reports-from-logs` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 1685.4
- `t/cross_user_config_leak.t` -> **Giovanni Bechis** (100.0% isolated ownership) | Magnitude: 1193.74
- `debian/bin/genorig.pl` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 194.76
- `masses/rule-qa/automc/gen_info_xml` -> **Bill Cole** (100.0% isolated ownership) | Magnitude: 181.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `debian/rules` -> **Severity: 0.208** (Embedded: 0.0136 * Error Risk: 15.2609%)
- `t/debug.t` -> **Severity: 0.066** (Embedded: 0.0019 * Error Risk: 33.7112%)
- `t/utf8.t` -> **Severity: 0.041** (Embedded: 0.0039 * Error Risk: 10.5899%)
- `t/date.t` -> **Severity: 0.003** (Embedded: 0.0039 * Error Risk: 0.883%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `spamc/utils.h` -> **Severity: 389.169** (Blast Radius: 4.276 * Doc Risk: 91.0125%)
- `spamc/getopt.h` -> **Severity: 374.4** (Blast Radius: 3.744 * Doc Risk: 100.0%)
- `t/date.t` -> **Severity: 361.879** (Blast Radius: 5.075 * Doc Risk: 71.3062%)
- `debian/rules` -> **Severity: 353.39** (Blast Radius: 13.064 * Doc Risk: 27.0507%)
- `t/plugin.t` -> **Severity: 315.303** (Blast Radius: 3.477 * Doc Risk: 90.6824%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
