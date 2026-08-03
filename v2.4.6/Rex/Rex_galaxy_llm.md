# ARCHITECTURAL_BRIEF: Rex
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/Rex` |
| **Timestamp** | `2026-08-03T19:29:30.877135+00:00` |
| **Scan Duration** | `0.43s` |
| **Git Branch** | `master` |
| **Git Commit** | `3159b71860d2f75850c75965462f0d7cd791dd57` |
| **Git Remote** | `https://github.com/RexOps/Rex.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Total Artifacts | 515 |
| Analyzed Artifacts (Scanned) | 108 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 407 |
| Total LOC | 6845 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 21.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 90 | 6601 | 83.3% |
| PLAINTEXT | 7 | 0 | 6.5% |
| YAML | 5 | 36 | 4.6% |
| SHELL | 3 | 208 | 2.8% |
| MARKDOWN | 2 | 0 | 1.9% |
| XML | 1 | 0 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.129`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 54 | 50.0% |
| file_cluster_13 | 28 | 25.9% |
| file_cluster_8 | 14 | 13.0% |
| file_cluster_4 | 2 | 1.9% |
| file_cluster_17 | 1 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 8.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 407*

**Composition by Extension & Reason:**
- `.pm`: 347x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2047 LOC)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out1`: 3x Excluded (Unsupported Extension: '.out1')
- `.out2`: 3x Excluded (Unsupported Extension: '.out2')
- `.out`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ex`: 2x Excluded (Unsupported Extension: '.ex')
- `.out3`: 2x Excluded (Unsupported Extension: '.out3')
- `.rex`: 2x Excluded (Unsupported Extension: '.rex')
- `.stderr`: 2x Excluded (Unsupported Extension: '.stderr')
- `.stdout`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 99.8 | 69.8 | 84.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.9 | 35.7 | 28.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.0 | 4.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 91.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 6.0 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 99.6 | 57.2 | 59.4 | 81.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `misc/create_pod.sh` (Hits: 166)
- `share/rex-tab-completion.zsh` (Hits: 28)
- `share/rex-tab-completion.bash` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **rex** (`bin/rex`) — 0 inbound connections
4. **rexify** (`bin/rexify`) — 0 inbound connections
5. **check_supported_OS.pl** (`misc/check_supported_OS.pl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rexify** (`bin/rexify`) — 29 outbound dependencies
2. **file.t** (`t/file.t`) — 15 outbound dependencies
3. **load_rexfile.t** (`t/load_rexfile.t`) — 14 outbound dependencies
4. **git.t** (`t/scm/git.t`) — 14 outbound dependencies
5. **rsync.t** (`t/rsync.t`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `upload_rexfile` (@ `bin/rexify`) -> Impact: **373.3** | LOC: 222
  * *Intent:* # upload rexfile to rex-jobcontrol (the complete directory)
- `get_image_format` (@ `t/issue/948.t`) -> Impact: **137.7** | LOC: 71
- `Anonymous_Block` (@ `share/rex-tab-completion.bash`) -> Impact: **62.4** | LOC: 46
- `Anonymous_Block` (@ `misc/create_pod.sh`) -> Impact: **29.6** | LOC: 98
- `test_summary` (@ `t/summary.t`) -> Impact: **24.6** | LOC: 32
- `expected_params` (@ `t/file_hooks.t`) -> Impact: **20.9** | LOC: 22
- `_hostgroups_[Truncated]` (@ `share/rex-tab-completion.zsh`) -> Impact: **18.4** | LOC: 68
- `download_recipe_local_tar_gz` (@ `bin/rexify`) -> Impact: **14.0** | LOC: 12
- `git_last_commit_message_ok` (@ `t/scm/git.t`) -> Impact: **8.6** | LOC: 34
- `create_tasks` (@ `t/summary.t`) -> Impact: **6.2** | LOC: 25

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `expected_params` (@ `t/file_hooks.t`) -> **O(2^N) [Recursive]**
- `get_image_format` (@ `t/issue/948.t`) -> **O(2^N) [Recursive]**
- `git_last_commit_message_ok` (@ `t/scm/git.t`) -> **O(2^N) [Recursive]**
- `Anonymous_Block` (@ `misc/create_pod.sh`) -> **O(N^4)**
- `Anonymous_Block` (@ `share/rex-tab-completion.bash`) -> **O(N^4)**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block` (@ `misc/create_pod.sh`) -> DB Complexity: **503**
- `_hostgroups_[Truncated]` (@ `share/rex-tab-completion.zsh`) -> DB Complexity: **90**
- `Anonymous_Block` (@ `share/rex-tab-completion.bash`) -> DB Complexity: **76**
- `upload_rexfile` (@ `bin/rexify`) -> DB Complexity: **41**
  * *Intent:* # upload rexfile to rex-jobcontrol (the complete directory)
- `get_image_format` (@ `t/issue/948.t`) -> DB Complexity: **10**
- `_get_log` (@ `t/logger.t`) -> DB Complexity: **7**
- `git_last_commit_message_ok` (@ `t/scm/git.t`) -> DB Complexity: **6**
- `test_summary` (@ `t/summary.t`) -> DB Complexity: **5**
- `expected_params` (@ `t/file_hooks.t`) -> DB Complexity: **4**
- `after_change_hook` (@ `t/file_hooks.t`) -> DB Complexity: **4**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 75 | 5525.12 | 74.66% | 1.58% |
| `bin` | 2 | 870.78 | 61.75% | 4.76% |
| `t/issue` | 8 | 402.72 | 70.49% | 8.39% |
| `share` | 2 | 150.86 | 80.06% | 96.46% |
| `misc` | 3 | 134.56 | 47.11% | 14.59% |
| `t/scm` | 1 | 108.66 | 56.02% | 0.0% |
| `xt/author` | 2 | 49.86 | 89.74% | 0.0% |
| `t/cmdb/default` | 2 | 29.42 | 5.0% | 0.0% |
| `t/cmdb` | 2 | 25.76 | 5.0% | 0.0% |
| `t/commands` | 1 | 22.6 | 16.8% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `share/rex-tab-completion.bash` -> **98.97%** Exposure
- `share/rex-tab-completion.zsh` -> **93.9456%** Exposure
- `t/augeas.t` -> **87.3855%** Exposure
- `t/issue/948.t` -> **67.1347%** Exposure
- `misc/create_pod.sh` -> **43.7823%** Exposure
### Highest State Flux (Mutation/Volatility)
- `misc/sanitize_pod.pl` -> **100.0%** Exposure
- `t/0.31.t` -> **100.0%** Exposure
- `t/args.t` -> **100.0%** Exposure
- `t/augeas.t` -> **100.0%** Exposure
- `t/base_virt.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `share/rex-tab-completion.bash` -> **2** Orphaned Functions | **0** Duplicates
- `share/rex-tab-completion.zsh` -> **2** Orphaned Functions | **0** Duplicates
- `misc/create_pod.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`share/rex-tab-completion.bash`** -> AI Confidence: **99.06%**
2. **`share/rex-tab-completion.zsh`** -> AI Confidence: **99.06%**
3. **`misc/create_pod.sh`** -> AI Confidence: **98.83%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `bin/rexify` -> **100.0%** Exposure
- `t/virtualization.t` -> **100.0%** Exposure
- `t/load_rexfile.t` -> **91.9291%** Exposure
### Weaponizable Injection Vectors
- `bin/rexify` -> **100.0%** Exposure
- `t/load_rexfile.t` -> **100.0%** Exposure
- `t/virtualization.t` -> **100.0%** Exposure
- `misc/create_pod.sh` -> **100.0%** Exposure
- `share/rex-tab-completion.zsh` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `misc/create_pod.sh` -> **100.0%** Exposure
- `share/rex-tab-completion.bash` -> **100.0%** Exposure
- `bin/rexify` -> **48.1752%** Exposure
- `t/scm/git.t` -> **1.2015%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `651` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `share/rex-tab-completion.bash` (SHELL) -> Cumulative Risk: **877.2**
- **Archetype:** `file_cluster_4` (Distance: 12.383 IQR)
- **Magnitude:** 117.82 | **LOC:** 67 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 62.4), `Anonymous_Block_[Truncated]` (Impact: 5.2), `__global_context__` (Impact: 1.3)

### 2. `misc/create_pod.sh` (SHELL) -> Cumulative Risk: **754.42**
- **Archetype:** `file_cluster_8` (Distance: 9.245 IQR)
- **Magnitude:** 50.1 | **LOC:** 120 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Concurrency (99.9823%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 29.6), `__global_context__` (Impact: 1.5)

### 3. `bin/rexify` (PERL) -> Cumulative Risk: **727.75**
- **Archetype:** `file_cluster_0` (Distance: 12.874 IQR)
- **Magnitude:** 833.36 | **LOC:** 1402 | **CtrlFlow:** 91.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `upload_rexfile` (Impact: 373.3), `download_recipe_local_tar_gz` (Impact: 14.0)

### 4. `t/virtualization.t` (PERL) -> Cumulative Risk: **654.65**
- **Archetype:** `file_cluster_0` (Distance: 11.499 IQR)
- **Magnitude:** 18.32 | **LOC:** 23 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (99.5504%)

### 5. `t/load_rexfile.t` (PERL) -> Cumulative Risk: **621.89**
- **Archetype:** `file_cluster_0` (Distance: 12.968 IQR)
- **Magnitude:** 911.64 | **LOC:** 100 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Cognitive Load (97.6207%)

### 6. `share/rex-tab-completion.zsh` (SHELL) -> Cumulative Risk: **581.58**
- **Archetype:** `file_cluster_8` (Distance: 9.377 IQR)
- **Magnitude:** 33.04 | **LOC:** 77 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.6467%), Tech Debt (93.9456%)
- **Heaviest Functions:** `_hostgroups_[Truncated]` (Impact: 18.4), `__global_context__` (Impact: 1.4)

### 7. `t/shared.t` (PERL) -> Cumulative Risk: **498.53**
- **Archetype:** `file_cluster_4` (Distance: 12.966 IQR)
- **Magnitude:** 69.18 | **LOC:** 87 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9946%), Cognitive Load (99.1946%)

### 8. `t/issue/948.t` (PERL) -> Cumulative Risk: **482.55**
- **Archetype:** `file_cluster_0` (Distance: 12.273 IQR)
- **Magnitude:** 173.1 | **LOC:** 96 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (90.7687%), Documentation (82.2514%)
- **Heaviest Functions:** `get_image_format` (Impact: 137.7)

### 9. `t/read_buffers.t` (PERL) -> Cumulative Risk: **460.62**
- **Archetype:** `file_cluster_0` (Distance: 12.386 IQR)
- **Magnitude:** 33.62 | **LOC:** 45 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (98.0838%), Safety Score (85.2323%)

### 10. `t/augeas.t` (PERL) -> Cumulative Risk: **459.29**
- **Archetype:** `file_cluster_0` (Distance: 12.067 IQR)
- **Magnitude:** 51.24 | **LOC:** 103 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (91.073%), Tech Debt (87.3855%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/load_rexfile.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.968 IQR)
- **Top Global Matches:** file_cluster_0: 12.968, file_cluster_13: 13.131, file_cluster_11: 13.458
- **Magnitude:** 911.64 | **LOC:** 100 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (97.6207%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 29`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 55`
* *Architecture:* `io: 4`, `import: 13`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Commands::File, constant, Test::More, autodie, File::Temp, Rex::CLI, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/rexify` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.874 IQR)
- **Top Global Matches:** file_cluster_0: 12.874, file_cluster_11: 13.622, file_cluster_13: 13.635
- **Magnitude:** 833.36 | **LOC:** 1402 | **CtrlFlow:** 91.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (90.4234%), Tech Debt (9.5291%)
**Top Internal Functions/Classes:**
  * `upload_rexfile` (Impact: 373.3 | O(N^2) | DB: 41)
    * *Intent:* # upload rexfile to rex-jobcontrol (the complete directory)
  * `download_recipe_local_tar_gz` (Impact: 14.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1851`, `structural_boundaries: 164`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 51`, `state_mutation: 424`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `import: 33`
* *Defense:* `safety: 5`, `doc: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Logger, LWP::UserAgent, Rex::Helper::URI, File::Basename, Rex::Commands::File, Rexfile, Rex::Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/write_utf8_files.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.471 IQR)
- **Top Global Matches:** file_cluster_13: 12.471, file_cluster_0: 12.632, file_cluster_11: 12.941
- **Magnitude:** 647.82 | **LOC:** 100 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.3675%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 29`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 53`
* *Architecture:* `io: 2`, `import: 19`
* *Defense:* `safety: 3`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::LibMagic, utf8, v5, magic, command, Test::More, warnings, Carp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rsync.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.293 IQR)
- **Top Global Matches:** file_cluster_13: 11.293, file_cluster_0: 11.344, file_cluster_8: 11.729
- **Magnitude:** 583.2 | **LOC:** 108 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.7079%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 25`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 33`
* *Architecture:* `io: 2`, `import: 13`
* *Defense:* `safety: 2`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands::Rsync, v5, File::Basename, Rex::Commands::Run, Test::More, autodie, File::Temp, Rex::Task...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/db.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.61 IQR)
- **Top Global Matches:** file_cluster_13: 10.61, file_cluster_0: 10.615, file_cluster_8: 10.875
- **Magnitude:** 405.04 | **LOC:** 121 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.2075%), Tech Debt (31.3391%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 24`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 22`, `planned_debt: 1`
* *Architecture:* `io: 1`, `import: 11`
* *Defense:* `safety: 2`, `test: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, DBI, warnings, Test::mysqld, TCP, Data::Dumper, Rex::Commands::DB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/issue/948.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.273 IQR)
- **Top Global Matches:** file_cluster_0: 12.273, file_cluster_13: 12.415, file_cluster_11: 12.734
- **Magnitude:** 173.1 | **LOC:** 96 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (90.7687%), Tech Debt (67.1347%)
**Top Internal Functions/Classes:**
  * `get_image_format` (Impact: 137.7 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 26`, `args: 2`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `planned_debt: 2`
* *Architecture:* `import: 12`
* *Defense:* `safety: 4`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Commands::File, Rex::Commands::Run, Rex::Commands::Fs, Test::More, warnings, Data::Dumper, Rex::Virtualization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.105 IQR)
- **Top Global Matches:** file_cluster_0: 12.105, file_cluster_8: 12.105, file_cluster_13: 12.146
- **Magnitude:** 137.06 | **LOC:** 393 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.1644%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 34`
* *Risk/State:* `state_mutation: 116`
* *Architecture:* `import: 19`
* *Defense:* `safety: 2`, `test: 67`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Commands::File, Rex::Commands::Run, Rex::Commands::Fs, change, Test::More, longer, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `share/rex-tab-completion.bash` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.383 IQR)
- **Top Global Matches:** file_cluster_4: 12.383, file_cluster_8: 12.615, file_cluster_12: 12.76
- **Magnitude:** 117.82 | **LOC:** 67 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (99.7921%), Tech Debt (98.97%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 62.4 | O(N^4) | DB: 76)
  * `Anonymous_Block_[Truncated]` (Impact: 5.2 | O(N^2) | DB: 4)
  * `__global_context__` (Impact: 1.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 9`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 42`, `orphaned_logic: 2`
* *Architecture:* `io: 22`, `concurrency: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dmi.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.041 IQR)
- **Top Global Matches:** file_cluster_0: 12.041, file_cluster_8: 12.229, file_cluster_13: 12.299
- **Magnitude:** 117.34 | **LOC:** 196 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.5331%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 99`
* *Architecture:* `import: 5`
* *Defense:* `safety: 5`, `test: 29`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, warnings, Rex::Inventory::DMIDecode, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/scm/git.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.938 IQR)
- **Top Global Matches:** file_cluster_8: 10.938, file_cluster_13: 11.08, file_cluster_0: 11.112
- **Magnitude:** 108.66 | **LOC:** 353 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (56.0191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `git_last_commit_message_ok` (Impact: 8.6 | O(2^N) | DB: 6)
  * `git_repo_ok` (Impact: 5.0 | O(N^1) | DB: 3)
  * `create_commit` (Impact: 4.0 | O(N^1) | DB: 4)
  * `init_test` (Impact: 3.9 | O(N^2) | DB: 1)
  * `prepare_test_repo` (Impact: 3.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 59`, `args: 5`, `func_start: 8`
* *Risk/State:* `state_mutation: 77`
* *Architecture:* `import: 13`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` critic, v5, Rex::Commands::File, Rex::Commands::Run, Test::More, File::Temp, warnings, File::Spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cron.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.37 IQR)
- **Top Global Matches:** file_cluster_8: 11.37, file_cluster_17: 11.784, file_cluster_0: 12.033
- **Magnitude:** 92.86 | **LOC:** 539 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.3747%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 25`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `import: 5`
* *Defense:* `safety: 4`, `test: 287`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Cron::Base, Test::More, warnings, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file_hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.115 IQR)
- **Top Global Matches:** file_cluster_13: 12.115, file_cluster_0: 12.178, file_cluster_8: 12.308
- **Magnitude:** 90.0 | **LOC:** 141 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (94.8175%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expected_params` (Impact: 20.9 | O(2^N) | DB: 4)
  * `before_hook` (Impact: 2.6 | O(N^1) | DB: 2)
  * `after_change_hook` (Impact: 2.5 | O(N^1) | DB: 4)
  * `after_hook` (Impact: 2.5 | O(N^1) | DB: 4)
  * `before_change_hook` (Impact: 2.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 36`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Commands::File, Test::More, File::Temp, Test::Deep, warnings, Test::Output, Rex::Hook...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/fs_files.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.433 IQR)
- **Top Global Matches:** file_cluster_0: 12.433, file_cluster_13: 12.916, file_cluster_17: 13.201
- **Magnitude:** 82.44 | **LOC:** 107 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.702%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 28`
* *Risk/State:* `state_mutation: 66`
* *Architecture:* `io: 7`, `import: 6`
* *Defense:* `safety: 2`, `test: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Commands::File, Test::More, warnings, Rex::Helper::Path, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/0.31.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.676 IQR)
- **Top Global Matches:** file_cluster_0: 12.676, file_cluster_13: 12.701, file_cluster_8: 12.728
- **Magnitude:** 80.46 | **LOC:** 156 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.9103%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 63`
* *Architecture:* `import: 7`
* *Defense:* `safety: 5`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, warnings, Rex, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/helper_path.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.642 IQR)
- **Top Global Matches:** file_cluster_0: 13.642, file_cluster_13: 14.092, file_cluster_11: 14.437
- **Magnitude:** 78.86 | **LOC:** 60 | **CtrlFlow:** 89.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.166%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 15`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Basename, v5, Test::More, warnings, Cwd, Rex::Helper::Path, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cmdb_path.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.08 IQR)
- **Top Global Matches:** file_cluster_0: 12.08, file_cluster_13: 12.272, file_cluster_8: 12.58
- **Magnitude:** 74.12 | **LOC:** 121 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (90.0072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_host_filename` (Impact: 3.1 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 46`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, Test::Deep, warnings, Cwd, File::Spec, Rex::Hardware, Rex::CMDB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/network_linux.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.23 IQR)
- **Top Global Matches:** file_cluster_0: 14.23, file_cluster_13: 14.754, file_cluster_11: 14.993
- **Magnitude:** 73.48 | **LOC:** 93 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.6385%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `import: 6`
* *Defense:* `safety: 9`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, warnings, Rex::Hardware::Network::Linux, Test::Warnings, Rex::Helper::Hash
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template_ng.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.777 IQR)
- **Top Global Matches:** file_cluster_13: 11.777, file_cluster_0: 11.786, file_cluster_8: 11.98
- **Magnitude:** 73.22 | **LOC:** 149 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.9581%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 19`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Config, Test::More, warnings, spaces, Rex::Commands, Rex::Template::NG, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks_in_rexfile_tasks_in_pkg.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.791 IQR)
- **Top Global Matches:** file_cluster_0: 13.791, file_cluster_13: 13.988, file_cluster_11: 14.098
- **Magnitude:** 72.86 | **LOC:** 58 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (94.9321%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::RunList, Test::More, lib, File::Temp, warnings, t::tasks::alien, Rex::Commands...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/summary.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.593 IQR)
- **Top Global Matches:** file_cluster_0: 11.593, file_cluster_13: 11.681, file_cluster_4: 11.9
- **Magnitude:** 71.5 | **LOC:** 115 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (95.6159%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_summary` (Impact: 24.6 | O(N^1) | DB: 5)
  * `create_tasks` (Impact: 6.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 32`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 33`
* *Architecture:* `concurrency: 6`, `import: 12`
* *Defense:* `safety: 2`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Commands::Run, Rex::Config, Rex::Transaction, Test::More, if, Test::Deep, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/sanitize_pod.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.395 IQR)
- **Top Global Matches:** file_cluster_13: 13.395, file_cluster_8: 13.491, file_cluster_17: 13.763
- **Magnitude:** 69.78 | **LOC:** 51 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.3241%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 11`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/shared.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.966 IQR)
- **Top Global Matches:** file_cluster_4: 12.966, file_cluster_0: 13.076, file_cluster_13: 13.128
- **Magnitude:** 69.18 | **LOC:** 87 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (99.1946%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 13`, `args: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 41`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `safety: 2`, `test: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, Test::Deep, warnings, Time::HiRes, Rex::Shared::Var, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/auth.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.663 IQR)
- **Top Global Matches:** file_cluster_8: 11.663, file_cluster_0: 11.732, file_cluster_13: 11.786
- **Magnitude:** 68.92 | **LOC:** 181 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (68.5857%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Test::More, warnings, Rex::Group, Rex::Commands, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.637 IQR)
- **Top Global Matches:** file_cluster_13: 11.637, file_cluster_0: 11.684, file_cluster_8: 11.869
- **Magnitude:** 65.04 | **LOC:** 139 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (80.4044%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 21`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::Config, Test::More, Rex::Template, warnings, Rex::Commands, Symbol, Test::Warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks_in_rexfile.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.429 IQR)
- **Top Global Matches:** file_cluster_0: 13.429, file_cluster_13: 13.462, file_cluster_11: 13.609
- **Magnitude:** 60.82 | **LOC:** 58 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (95.146%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v5, Rex::RunList, Test::More, warnings, Test::Warnings, Rex::Commands, Rex::Shared::Var, File::Temp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/file.t` (PERL) | Magnitude: 137.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 116, indent_spaces: 111, branch: 83, test: 67
- `t/no_tty.t` (PERL) | Magnitude: 27.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 20, state_mutation: 12, indent_spaces: 10, decorators: 9
- `t/interface_fs_local.t` (PERL) | Magnitude: 24.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 13, structural_boundaries: 12, state_mutation: 9, test: 8
- `t/issue/949.t` (PERL) | Magnitude: 24.5 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 19, structural_boundaries: 12, indent_spaces: 10, state_mutation: 9
- `t/hooks.t` (PERL) | Magnitude: 60.8 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 45, branch: 19, structural_boundaries: 11, decorators: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/db.t` (PERL) | Magnitude: 405.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, branch: 32, structural_boundaries: 24, state_mutation: 22
- `t/waitpid_blocking_sleep_time.t` (PERL) | Magnitude: 19.22 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 11, structural_boundaries: 6, decorators: 5, import: 5
- `t/template_ng.t` (PERL) | Magnitude: 73.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 56, branch: 37, indent_spaces: 37, structural_boundaries: 19
- `t/helper_hash.t` (PERL) | Magnitude: 19.84 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, branch: 8, structural_boundaries: 8, test: 7
- `t/symlinks.t` (PERL) | Magnitude: 21.38 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, test: 25, branch: 21, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/ini.t` (PERL) | Magnitude: 29.64 | Delta: **0.156 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, branch: 46, test: 35, globals: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/shared.t` (PERL) | Magnitude: 69.18 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 26, branch: 20, test: 18
- `share/rex-tab-completion.bash` (SHELL) | Magnitude: 117.82 | Delta: **0.232 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_spaces: 39, io: 22, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/auth.t` (PERL) | Magnitude: 68.92 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 51, pointers: 42, test: 37
- `t/scm/git.t` (PERL) | Magnitude: 108.66 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 178, state_mutation: 77, structural_boundaries: 59, branch: 42
- `t/package.t` (PERL) | Magnitude: 38.54 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 26, branch: 24, state_mutation: 21
- `t/cmdb/foo.yml` (YAML) | Magnitude: 10.52 | Delta: **0.322 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 1
- `misc/create_pod.sh` (SHELL) | Magnitude: 50.1 | Delta: **0.381 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: io: 166, indent_spaces: 92, structural_boundaries: 42, serialization_parsing: 16

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `share/rex-tab-completion.bash` -> **Severity: 922.066** (Blast Radius: 9.259 * Doc Risk: 99.5859%)
- `t/os_dependencies.t` -> **Severity: 912.878** (Blast Radius: 9.259 * Doc Risk: 98.5936%)
- `t/path.t` -> **Severity: 912.878** (Blast Radius: 9.259 * Doc Risk: 98.5936%)
- `t/virtualization.t` -> **Severity: 912.878** (Blast Radius: 9.259 * Doc Risk: 98.5936%)
- `t/proc.t` -> **Severity: 907.21** (Blast Radius: 9.259 * Doc Risk: 97.9814%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
