# ARCHITECTURAL_BRIEF: catalyst-runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/catalyst-runtime` |
| **Timestamp** | `2026-08-03T19:29:35.902118+00:00` |
| **Scan Duration** | `0.56s` |
| **Git Branch** | `master` |
| **Git Commit** | `1d40b8ea5a7f4a4ae99af921b914f04e7c9a21c3` |
| **Git Remote** | `https://github.com/perl-catalyst/catalyst-runtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
| Total Artifacts | 493 |
| Analyzed Artifacts (Scanned) | 213 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 280 |
| Total LOC | 13088 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 43.2% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 209 | 12935 | 98.1% |
| PLAINTEXT | 2 | 0 | 0.9% |
| M4 | 1 | 27 | 0.5% |
| JSON | 1 | 126 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.972`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 111 | 52.1% |
| file_cluster_13 | 85 | 39.9% |
| file_cluster_8 | 13 | 6.1% |
| file_cluster_4 | 2 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 280*

**Composition by Extension & Reason:**
- `.pm`: 254x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.t`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mkdn`: 1x Excluded (Unsupported Extension: '.mkdn')
- `.include`: 1x Excluded (Unsupported Extension: '.include')
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')
- `.pl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 69.1 | 83.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 25.4 | 19.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 3.0 | 0.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 7.1 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 79.7 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 20.9 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 66.4 | 70.2 | 86.4 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/optional_lighttpd-fastcgi-non-root.t` (Hits: 9)
- `t/optional_lighttpd-fastcgi.t` (Hits: 9)
- `t/optional_http-server-restart.t` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utf8.txt** (`t/utf8.txt`) — 11 inbound connections
2. **Changes** (`Changes`) — 0 inbound connections
3. **Makefile.PL** (`Makefile.PL`) — 0 inbound connections
4. **catalyst.pl** (`script/catalyst.pl`) — 0 inbound connections
5. **01use.t** (`t/01use.t`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **arg_constraints.t** (`t/arg_constraints.t`) — 18 outbound dependencies
2. **utf_incoming.t** (`t/utf_incoming.t`) — 17 outbound dependencies
3. **live_engine_request_uploads.t** (`t/aggregate/live_engine_request_uploads.t`) — 15 outbound dependencies
4. **live_component_controller_action_chained.t** (`t/aggregate/live_component_controller_action_chained.t`) — 14 outbound dependencies
5. **psgi-log.t** (`t/psgi-log.t`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_tests` (@ `t/aggregate/live_component_controller_action_chained.t`) -> Impact: **8548.9** | LOC: 1149
- `make_component_file` (@ `t/aggregate/unit_core_component_loading.t`) -> Impact: **1224.4** | LOC: 189
- `uri_for` (@ `t/utf_incoming.t`) -> Impact: **1076.0** | LOC: 527
- `run_tests` (@ `t/aggregate/live_component_controller_action_visit.t`) -> Impact: **865.5** | LOC: 259
- `run_tests` (@ `t/aggregate/live_component_controller_action_forward.t`) -> Impact: **739.2** | LOC: 234
- `run_tests` (@ `t/aggregate/live_component_controller_action_go.t`) -> Impact: **709.6** | LOC: 242
- `run_tests` (@ `t/aggregate/live_component_controller_action_auto.t`) -> Impact: **636.0** | LOC: 160
- `streaming_body_with_charset` (@ `t/psgi_utils.t`) -> Impact: **392.8** | LOC: 374
- `run_tests` (@ `t/aggregate/live_component_controller_action_inheritance.t`) -> Impact: **370.7** | LOC: 94
- `run_tests` (@ `t/aggregate/live_component_controller_action_action.t`) -> Impact: **246.2** | LOC: 244

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `make_component_file` (@ `t/aggregate/unit_core_component_loading.t`) -> **O(2^N) [Recursive]**
- `root` (@ `t/abort-chain-1.t`) -> **O(2^N) [Recursive]**
- `main` (@ `t/abort-chain-1.t`) -> **O(2^N) [Recursive]**
- `hits` (@ `t/abort-chain-1.t`) -> **O(2^N) [Recursive]**
- `root` (@ `t/abort-chain-2.t`) -> **O(2^N) [Recursive]**
- `main` (@ `t/abort-chain-2.t`) -> **O(2^N) [Recursive]**
- `hits` (@ `t/abort-chain-2.t`) -> **O(2^N) [Recursive]**
- `root` (@ `t/abort-chain-3.t`) -> **O(2^N) [Recursive]**
- `main` (@ `t/abort-chain-3.t`) -> **O(2^N) [Recursive]**
- `hits` (@ `t/abort-chain-3.t`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `run_tests` (@ `t/aggregate/live_component_controller_action_chained.t`) -> DB Complexity: **164**
- `uri_for` (@ `t/utf_incoming.t`) -> DB Complexity: **69**
- `run_tests` (@ `t/aggregate/live_component_controller_action_auto.t`) -> DB Complexity: **27**
- `run_tests` (@ `t/aggregate/live_component_controller_action_go.t`) -> DB Complexity: **27**
- `run_tests` (@ `t/aggregate/live_component_controller_action_visit.t`) -> DB Complexity: **27**
- `make_component_file` (@ `t/aggregate/unit_core_component_loading.t`) -> DB Complexity: **26**
- `run_tests` (@ `t/aggregate/live_component_controller_action_forward.t`) -> DB Complexity: **20**
- `run_tests` (@ `t/aggregate/live_component_controller_action_index.t`) -> DB Complexity: **15**
- `streaming_body_with_charset` (@ `t/psgi_utils.t`) -> DB Complexity: **15**
- `run_tests` (@ `t/aggregate/live_component_controller_action_action.t`) -> DB Complexity: **11**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t/aggregate` | 118 | 19521.82 | 70.3% | 9.0% |
| `t` | 85 | 15379.85 | 70.32% | 23.7% |
| `xt/author` | 5 | 202.08 | 42.38% | 4.25% |
| `__monolith__` | 2 | 115.52 | 21.43% | 0.0% |
| `script` | 1 | 32.36 | 36.55% | 0.0% |
| `t/conf` | 1 | 15.54 | 9.46% | 0.0% |
| `t/something` | 1 | 10.52 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/aggregate/unit_controller_namespace.t` -> **100.0%** Exposure
- `t/aggregate/unit_metaclass_compat_non_moose_controller.t` -> **100.0%** Exposure
- `t/class_traits.t` -> **100.0%** Exposure
- `t/dead_load_bad_args.t` -> **100.0%** Exposure
- `t/dead_load_multiple_chained_attributes.t` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `t/aggregate/deprecated_test_import.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_auto.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_chained.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_default.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_index.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/next-action.t` -> **0** Orphaned Functions | **7** Duplicates
- `t/class_traits.t` -> **1** Orphaned Functions | **4** Duplicates
- `t/http_exceptions.t` -> **3** Orphaned Functions | **2** Duplicates
- `t/http_exceptions_backcompat.t` -> **3** Orphaned Functions | **2** Duplicates
- `t/dead_recursive_chained_attributes.t` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`t/conf/extra.conf.in`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `t/aggregate/unit_core_uri_for.t` -> **0.001%** Exposure
### Exploit Generation Surface
- `t/aggregate/live_component_controller_action_chained.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_forward.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_go.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_visit.t` -> **100.0%** Exposure
- `t/aggregate/unit_core_component_loading.t` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `t/aggregate/live_component_controller_action_auto.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_chained.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_forward.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_go.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_visit.t` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1510` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/next-action.t` (PERL) -> Cumulative Risk: **721.39**
- **Archetype:** `file_cluster_0` (Distance: 12.272 IQR)
- **Magnitude:** 179.56 | **LOC:** 172 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `d` (Impact: 18.6), `root` (Impact: 12.5), `b` (Impact: 12.3)

### 2. `xt/author/http-server.t` (PERL) -> Cumulative Risk: **679.71**
- **Archetype:** `file_cluster_4` (Distance: 12.576 IQR)
- **Magnitude:** 109.04 | **LOC:** 101 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `prove` (Impact: 45.6), `wait_port_timeout` (Impact: 2.1)

### 3. `t/aggregate/live_component_controller_action_auto.t` (PERL) -> Cumulative Risk: **633.95**
- **Archetype:** `file_cluster_0` (Distance: 12.076 IQR)
- **Magnitude:** 722.86 | **LOC:** 192 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9992%)
- **Heaviest Functions:** `run_tests` (Impact: 636.0)

### 4. `t/aggregate/unit_core_component_loading.t` (PERL) -> Cumulative Risk: **624.14**
- **Archetype:** `file_cluster_0` (Distance: 12.255 IQR)
- **Magnitude:** 1345.72 | **LOC:** 246 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `make_component_file` (Impact: 1224.4), `write_component_file` (Impact: 14.6)

### 5. `t/aggregate/live_component_controller_action_index.t` (PERL) -> Cumulative Risk: **604.74**
- **Archetype:** `file_cluster_0` (Distance: 12.451 IQR)
- **Magnitude:** 193.3 | **LOC:** 99 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9993%), Documentation (92.7655%)
- **Heaviest Functions:** `run_tests` (Impact: 143.8)

### 6. `t/aggregate/live_component_controller_action_detach.t` (PERL) -> Cumulative Risk: **576.1**
- **Archetype:** `file_cluster_0` (Distance: 11.124 IQR)
- **Magnitude:** 224.86 | **LOC:** 99 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9982%), Algorithmic Dos (99.1594%), Documentation (94.8267%)
- **Heaviest Functions:** `run_tests` (Impact: 196.2)

### 7. `t/aggregate/live_component_controller_action_chained.t` (PERL) -> Cumulative Risk: **566.19**
- **Archetype:** `file_cluster_0` (Distance: 13.027 IQR)
- **Magnitude:** 9060.1 | **LOC:** 1176 | **CtrlFlow:** 89.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `run_tests` (Impact: 8548.9)

### 8. `t/aggregate/live_component_controller_action_local.t` (PERL) -> Cumulative Risk: **563.42**
- **Archetype:** `file_cluster_0` (Distance: 10.739 IQR)
- **Magnitude:** 206.5 | **LOC:** 150 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.947%), State Flux (99.8875%), Logic Bomb (96.8242%)
- **Heaviest Functions:** `run_tests` (Impact: 173.8)

### 9. `t/aggregate/live_component_controller_action_go.t` (PERL) -> Cumulative Risk: **553.93**
- **Archetype:** `file_cluster_0` (Distance: 11.688 IQR)
- **Magnitude:** 803.12 | **LOC:** 276 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `run_tests` (Impact: 709.6), `_begin` (Impact: 1.7)

### 10. `t/http_method.t` (PERL) -> Cumulative Risk: **553.91**
- **Archetype:** `file_cluster_0` (Distance: 11.772 IQR)
- **Magnitude:** 71.26 | **LOC:** 94 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (91.0313%)
- **Heaviest Functions:** `Catalyst` (Impact: 28.7), `show` (Impact: 5.6), `post_user` (Impact: 5.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/arg_constraints.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.602 IQR)
- **Top Global Matches:** file_cluster_0: 12.602, file_cluster_13: 12.861, file_cluster_8: 13.078
- **Magnitude:** 9724.13 | **LOC:** 597 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.382%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 128`, `args: 17`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`
* *Architecture:* `api: 1`, `import: 33`
* *Defense:* `safety: 27`, `doc: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst::Test, MyApp::Types, Catalyst, Type::Library, strict, MooseX::MethodAttributes::Role, Test::More, Type::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_chained.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.027 IQR)
- **Top Global Matches:** file_cluster_0: 13.027, file_cluster_8: 13.751, file_cluster_11: 13.761
- **Magnitude:** 9060.1 | **LOC:** 1176 | **CtrlFlow:** 89.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 164
- **Risk Profile:** Cognitive Load (88.5885%), Tech Debt (16.7293%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 8548.9 | O(N^4) | DB: 164)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1532`, `structural_boundaries: 182`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 495`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `import: 10`
* *Defense:* `safety: 4`, `test: 174`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, concurrent, Test::More, FindBin, arguments, URI::QueryParam, Benchmark...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_component_loading.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.255 IQR)
- **Top Global Matches:** file_cluster_0: 12.255, file_cluster_13: 12.643, file_cluster_11: 12.817
- **Magnitude:** 1345.72 | **LOC:** 246 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (90.1593%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_component_file` (Impact: 1224.4 | O(2^N) | DB: 26)
  * `write_component_file` (Impact: 14.6 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 50`, `args: 4`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 99`
* *Architecture:* `io: 3`, `api: 4`, `import: 14`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, MRO::Compat, strict, Test::More, File::Spec, base, warnings, File::Path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/utf_incoming.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.821 IQR)
- **Top Global Matches:** file_cluster_0: 11.821, file_cluster_13: 12.215, file_cluster_8: 12.301
- **Magnitude:** 1236.02 | **LOC:** 567 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 69
- **Risk Profile:** Cognitive Load (82.7893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `uri_for` (Impact: 1076.0 | O(2^N) | DB: 69)
  * `heart` (Impact: 7.2 | O(2^N))
  * `hat` (Impact: 7.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 116`, `args: 23`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 136`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 17`
* *Defense:* `safety: 3`, `test: 30`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst::Test, Catalyst, gunzip, HTTP::Message::PSGI, strict, Test::More, Encode, File::Spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_visit.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.588 IQR)
- **Top Global Matches:** file_cluster_0: 11.588, file_cluster_8: 12.224, file_cluster_13: 12.231
- **Magnitude:** 959.36 | **LOC:** 292 | **CtrlFlow:** 91.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (88.9463%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 865.5 | O(N^4) | DB: 27)
  * `_begin` (Impact: 1.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 34`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 87`
* *Architecture:* `import: 8`
* *Defense:* `safety: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, namespace, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.223 IQR)
- **Top Global Matches:** file_cluster_0: 11.223, file_cluster_8: 11.769, file_cluster_13: 11.863
- **Magnitude:** 806.68 | **LOC:** 258 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (85.6401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 739.2 | O(N^4) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 27`, `func_start: 1`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_go.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.688 IQR)
- **Top Global Matches:** file_cluster_0: 11.688, file_cluster_13: 12.243, file_cluster_8: 12.287
- **Magnitude:** 803.12 | **LOC:** 276 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (90.9117%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 709.6 | O(N^4) | DB: 27)
  * `_begin` (Impact: 1.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 34`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 87`
* *Architecture:* `import: 9`
* *Defense:* `safety: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, FindBin, namespace, Benchmark, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_auto.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.076 IQR)
- **Top Global Matches:** file_cluster_0: 12.076, file_cluster_13: 12.723, file_cluster_8: 12.905
- **Magnitude:** 722.86 | **LOC:** 192 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (90.7183%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 636.0 | O(N^3) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 38`, `func_start: 1`
* *Risk/State:* `state_mutation: 84`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_args.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.705 IQR)
- **Top Global Matches:** file_cluster_13: 12.705, file_cluster_0: 12.861, file_cluster_8: 13.077
- **Magnitude:** 553.51 | **LOC:** 97 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.5714%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 15`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings, URI::Escape
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/psgi_utils.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.742 IQR)
- **Top Global Matches:** file_cluster_0: 10.742, file_cluster_8: 10.802, file_cluster_13: 10.941
- **Magnitude:** 532.34 | **LOC:** 442 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (70.4445%), Tech Debt (32.0974%)
**Top Internal Functions/Classes:**
  * `streaming_body_with_charset` (Impact: 392.8 | O(2^N) | DB: 15)
  * `as_psgi` (Impact: 14.1 | O(2^N) | DB: 1)
  * `name_args` (Impact: 12.3 | O(N^1) | DB: 1)
  * `filehandle` (Impact: 12.3 | O(N^1) | DB: 4)
  * `name` (Impact: 10.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 99`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `state_mutation: 69`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 2`, `import: 13`
* *Defense:* `safety: 2`, `test: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst::Test, Catalyst::Utils, Catalyst, strict, Plack::Request, Test::More, Encode, base...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_inheritance.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.253 IQR)
- **Top Global Matches:** file_cluster_0: 11.253, file_cluster_13: 11.815, file_cluster_8: 11.989
- **Magnitude:** 402.76 | **LOC:** 118 | **CtrlFlow:** 91.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (90.8957%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 370.7 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 17`, `func_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/args0_bug.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.221 IQR)
- **Top Global Matches:** file_cluster_0: 17.221, file_cluster_13: 17.267, file_cluster_11: 17.536
- **Magnitude:** 345.94 | **LOC:** 66 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (68.4178%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `chained_one_args_0` (Impact: 4.0 | O(2^N))
  * `chained_one_args_1` (Impact: 4.0 | O(2^N))
  * `chained_one_args_2` (Impact: 4.0 | O(2^N))
  * `chained_zero_args_0` (Impact: 4.0 | O(2^N))
  * `chained_zero_args_1` (Impact: 4.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 11`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 319`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `doc: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, Moose, MooseX::MethodAttributes, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_action.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.684 IQR)
- **Top Global Matches:** file_cluster_0: 10.684, file_cluster_8: 10.815, file_cluster_13: 11.005
- **Magnitude:** 287.1 | **LOC:** 269 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (74.5256%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 246.2 | O(N^3) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 26`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 67`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst::Test, strict, Test::More, FindBin, Catalyst::Action, Benchmark, lib, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_detach.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.124 IQR)
- **Top Global Matches:** file_cluster_0: 11.124, file_cluster_13: 11.475, file_cluster_8: 11.703
- **Magnitude:** 224.86 | **LOC:** 99 | **CtrlFlow:** 84.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (88.9372%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 196.2 | O(N^4) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 16`, `func_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_local.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.739 IQR)
- **Top Global Matches:** file_cluster_0: 10.739, file_cluster_8: 10.954, file_cluster_13: 10.97
- **Magnitude:** 206.5 | **LOC:** 150 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (84.1131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 173.8 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 30`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_path.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.65 IQR)
- **Top Global Matches:** file_cluster_0: 10.65, file_cluster_8: 10.85, file_cluster_13: 10.973
- **Magnitude:** 199.88 | **LOC:** 162 | **CtrlFlow:** 86.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (81.7073%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 172.9 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 15`, `func_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_index.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.451 IQR)
- **Top Global Matches:** file_cluster_0: 12.451, file_cluster_13: 12.522, file_cluster_17: 12.834
- **Magnitude:** 193.3 | **LOC:** 99 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (92.6446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 143.8 | O(N^3) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 20`, `func_start: 1`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `import: 13`
* *Defense:* `safety: 2`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, slash, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/next-action.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.272 IQR)
- **Top Global Matches:** file_cluster_0: 12.272, file_cluster_13: 12.446, file_cluster_8: 12.842
- **Magnitude:** 179.56 | **LOC:** 172 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (84.2682%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `d` (Impact: 18.6 | O(N^2) | DB: 3)
  * `root` (Impact: 12.5 | O(N^1) | DB: 3)
  * `b` (Impact: 12.3 | O(N^3) | DB: 3)
  * `c` (Impact: 10.2 | O(N^4) | DB: 1)
  * `a` (Impact: 9.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 69`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 72`, `duplicate_logic: 7`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, base, Data::Dumper, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_script_server.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.082 IQR)
- **Top Global Matches:** file_cluster_0: 13.082, file_cluster_4: 13.171, file_cluster_13: 13.181
- **Magnitude:** 174.08 | **LOC:** 215 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (96.6966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBackgroundOptionWithFork` (Impact: 40.8 | O(N^2) | DB: 9)
  * `testOption` (Impact: 40.2 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 59`, `args: 5`, `func_start: 6`
* *Risk/State:* `state_mutation: 71`
* *Architecture:* `concurrency: 19`, `import: 13`
* *Defense:* `safety: 12`, `test: 9`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MooseX::Daemonize, strict, Test::More, FindBin, Plack::Handler::Starman, File::Temp, Cwd, opts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/state.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.663 IQR)
- **Top Global Matches:** file_cluster_0: 10.663, file_cluster_13: 11.113, file_cluster_8: 11.349
- **Magnitude:** 173.58 | **LOC:** 91 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (58.257%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `two` (Impact: 42.4 | O(N^2) | DB: 1)
  * `end` (Impact: 24.6 | O(N^1) | DB: 1)
  * `auto` (Impact: 21.2 | O(2^N))
  * `begin` (Impact: 21.0 | O(2^N))
  * `base` (Impact: 10.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 39`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 2`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, base, HTTP::Request::Common, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_default.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.772 IQR)
- **Top Global Matches:** file_cluster_0: 11.772, file_cluster_13: 12.014, file_cluster_8: 12.321
- **Magnitude:** 171.12 | **LOC:** 95 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (94.2104%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 133.6 | O(N^3) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 17`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, strict, Test::More, FindBin, Benchmark, lib, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/relative_root_action_for_bug.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.363 IQR)
- **Top Global Matches:** file_cluster_0: 9.363, file_cluster_13: 9.69, file_cluster_8: 9.704
- **Magnitude:** 153.18 | **LOC:** 94 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (33.4589%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `author` (Impact: 56.3 | O(2^N))
  * `top` (Impact: 34.9 | O(2^N))
  * `story` (Impact: 34.9 | O(2^N))
  * `default` (Impact: 8.0 | O(N^2))
  * `root` (Impact: 7.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `duplicate_logic: 3`, `orphaned_logic: 1`
* *Architecture:* `import: 11`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, Moose, MooseX::MethodAttributes, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/configured_comps.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.327 IQR)
- **Top Global Matches:** file_cluster_0: 11.327, file_cluster_13: 11.655, file_cluster_8: 12.021
- **Magnitude:** 151.5 | **LOC:** 127 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (70.4052%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `user` (Impact: 96.5 | O(2^N) | DB: 1)
  * `default` (Impact: 16.2 | O(2^N))
  * `find` (Impact: 14.1 | O(N^1) | DB: 1)
  * `foo` (Impact: 2.9 | O(2^N) | DB: 1)
  * `role` (Impact: 2.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 37`, `args: 5`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `import: 13`
* *Defense:* `safety: 3`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, Moose, MooseX::MethodAttributes, Moose::Role, HTTP::Request::Common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dispatch_on_scheme.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.976 IQR)
- **Top Global Matches:** file_cluster_0: 10.976, file_cluster_13: 11.357, file_cluster_8: 11.476
- **Magnitude:** 143.74 | **LOC:** 124 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.5947%), Tech Debt (70.0675%)
**Top Internal Functions/Classes:**
  * `is_http` (Impact: 21.0 | O(2^N))
  * `is_https` (Impact: 21.0 | O(2^N))
  * `endpoint` (Impact: 15.8 | O(N^2))
  * `is_http_chain` (Impact: 10.6 | O(N^1))
  * `is_https_chain` (Impact: 10.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 25`, `args: 8`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 2`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Catalyst, strict, Test::More, base, HTTP::Request::Common, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_engine_request_uploads.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.624 IQR)
- **Top Global Matches:** file_cluster_0: 11.624, file_cluster_13: 11.875, file_cluster_8: 11.886
- **Magnitude:** 133.5 | **LOC:** 412 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.3419%), Tech Debt (23.2846%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 61`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 112`, `fragile_debt: 2`
* *Architecture:* `import: 20`
* *Defense:* `safety: 2`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, HTTP::Headers::Util, strict, Test::More, FindBin, way, HTTP::Body::OctetStream, Path::Class::Dir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/aggregate/live_component_controller_attributes.t` (PERL) | Magnitude: 61.08 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 31, state_mutation: 30, indent_spaces: 12, test: 11
- `t/aggregate/custom_live_component_controller_action_auto_doublebug.t` (PERL) | Magnitude: 61.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 30, indent_spaces: 23, structural_boundaries: 12, state_mutation: 12
- `t/no_test_stash_bug.t` (PERL) | Magnitude: 6.46 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 11, structural_boundaries: 9, indent_spaces: 9, decorators: 6
- `t/optional_apache-cgi-rewrite.pl` (PERL) | Magnitude: 25.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 31, indent_spaces: 15, structural_boundaries: 14, decorators: 12
- `t/optional_apache-cgi.pl` (PERL) | Magnitude: 25.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 31, indent_spaces: 15, structural_boundaries: 14, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/content_negotiation.t` (PERL) | Magnitude: 47.82 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 37, state_mutation: 31, encapsulation: 29
- `t/query_keywords_and_parameters.t` (PERL) | Magnitude: 20.54 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 36, indent_spaces: 29, structural_boundaries: 22, state_mutation: 15
- `t/aggregate/c3_mro.t` (PERL) | Magnitude: 21.42 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 18, structural_boundaries: 11, indent_spaces: 9, decorators: 7
- `t/live_redirect_body.t` (PERL) | Magnitude: 42.8 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 33, state_mutation: 27, indent_spaces: 26, test: 19
- `t/aggregate/live_component_controller_action_index_or_default.t` (PERL) | Magnitude: 22.28 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 24, indent_spaces: 13, structural_boundaries: 8, decorators: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `xt/author/http-server.t` (PERL) | Magnitude: 109.04 | Delta: **0.24 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 47, state_mutation: 36, structural_boundaries: 33, indent_spaces: 32
- `t/live_fork.t` (PERL) | Magnitude: 80.54 | Delta: **0.467 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 55, indent_spaces: 26, state_mutation: 22, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/aggregate/unit_controller_config.t` (PERL) | Magnitude: 18.7 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 17, pointers: 11, branch: 9, structural_boundaries: 9
- `t/aggregate/unit_core_engine-prepare_path.t` (PERL) | Magnitude: 51.5 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 42, branch: 40, structural_boundaries: 22
- `t/aggregate/unit_core_classdata.t` (PERL) | Magnitude: 45.68 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 37, state_mutation: 29, structural_boundaries: 25, indent_spaces: 21
- `t/aggregate/live_component_controller_httpmethods.t` (PERL) | Magnitude: 6.94 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 28, branch: 16, structural_boundaries: 7, import: 7
- `t/aggregate/unit_core_merge_config_hashes.t` (PERL) | Magnitude: 18.76 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, branch: 15, structural_boundaries: 6, import: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/aggregate/unit_metaclass_compat_extend_non_moose_controller.t` -> **Severity: 449.549** (Blast Radius: 4.497 * Doc Risk: 99.9665%)
- `t/aggregate/custom_live_component_controller_action_auto_doublebug.t` -> **Severity: 449.481** (Blast Radius: 4.497 * Doc Risk: 99.9513%)
- `t/aggregate/custom_live_path_bug.t` -> **Severity: 449.339** (Blast Radius: 4.497 * Doc Risk: 99.9197%)
- `t/aggregate/live_component_view_single.t` -> **Severity: 449.282** (Blast Radius: 4.497 * Doc Risk: 99.9071%)
- `t/aggregate/live_component_controller_action_begin.t` -> **Severity: 448.42** (Blast Radius: 4.497 * Doc Risk: 99.7154%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
