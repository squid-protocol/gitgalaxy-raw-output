# ARCHITECTURAL_BRIEF: Dancer2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/Dancer2` |
| **Timestamp** | `2026-08-03T19:29:23.554135+00:00` |
| **Scan Duration** | `0.61s` |
| **Git Branch** | `main` |
| **Git Commit** | `25176c5b860493b4a6dcda5bc12ecbefa67df716` |
| **Git Remote** | `https://github.com/PerlDancer/Dancer2.git` |
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
| Total Artifacts | 438 |
| Analyzed Artifacts (Scanned) | 226 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 212 |
| Total LOC | 10813 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 51.6% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.375 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 179 | 10365 | 79.2% |
| YAML | 23 | 100 | 10.2% |
| HTML | 7 | 84 | 3.1% |
| MARKDOWN | 5 | 0 | 2.2% |
| PLAINTEXT | 4 | 0 | 1.8% |
| CSS | 4 | 239 | 1.8% |
| SQLITE | 2 | 14 | 0.9% |
| DOCKERFILE | 1 | 6 | 0.4% |
| JSON | 1 | 5 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.949`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 85 | 37.6% |
| file_cluster_13 | 85 | 37.6% |
| file_cluster_8 | 47 | 20.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 212*

**Composition by Extension & Reason:**
- `.pm`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tt`: 25x Excluded (Unsupported Extension: '.tt')
- `.t`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.pod`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.psgi`: 2x Excluded (Unsupported Extension: '.psgi')
- `.fcgi`: 2x Excluded (Unsupported Extension: '.fcgi')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.db`: 1x Excluded (Unsupported Extension: '.db'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 2x Excluded (Unsupported Extension: '.rc')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.1 | 57.5 | 73.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 20.8 | 18.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.3 | 0.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 9.3 | 1.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 42.3 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 70.6 | 100.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.6 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.4 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 38.0 | 3.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 67.0 | 80.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.4 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 97.9 | 0.5 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/request_upload.t` (Hits: 5)
- `t/file_utils.t` (Hits: 3)
- `share/skel/default/public/404.html` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **content.t** (`t/dsl/content.t`) — 3 inbound connections
2. **TestPlugin.pm** (`t/issues/gh-1449/TestPlugin.pm`) — 1 inbound connections
3. **AUTHORS** (`AUTHORS`) — 0 inbound connections
4. **Changes** (`Changes`) — 0 inbound connections
5. **file.txt** (`t/public/file.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **error.t** (`t/error.t`) — 17 outbound dependencies
2. **plugin_syntax.t** (`t/plugin_syntax.t`) — 14 outbound dependencies
3. **hooks.t** (`t/hooks.t`) — 13 outbound dependencies
4. **serializer_mutable_custom.t** (`t/serializer_mutable_custom.t`) — 12 outbound dependencies
5. **perf.pl** (`tools/perf.pl`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_app` (@ `t/dsl/uri_for_route.t`) -> Impact: **527.7** | LOC: 128
- `run_test` (@ `t/request_upload.t`) -> Impact: **215.3** | LOC: 167
- `MyApp` (@ `t/error.t`) -> Impact: **212.3** | LOC: 46
- `run_test` (@ `t/request.t`) -> Impact: **163.1** | LOC: 111
- `all_tests` (@ `t/cookie.t`) -> Impact: **155.6** | LOC: 171
- `hexe` (@ `t/file_utils.t`) -> Impact: **117.2** | LOC: 52
- `generate_id` (@ `t/session_bad_client_cookie.t`) -> Impact: **45.1** | LOC: 102
- `BUILD` (@ `t/plugin2/hooks.t`) -> Impact: **30.3** | LOC: 12
- `_read_config_with_warnings` (@ `t/strict_config.t`) -> Impact: **24.6** | LOC: 23
- `config_any` (@ `t/config_reader.t`) -> Impact: **18.5** | LOC: 7

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `test_app` (@ `t/dsl/uri_for_route.t`) -> **O(2^N) [Recursive]**
- `MyApp` (@ `t/error.t`) -> **O(2^N) [Recursive]**
- `hexe` (@ `t/file_utils.t`) -> **O(2^N) [Recursive]**
- `config_location` (@ `t/issues/gh-634.t`) -> **O(2^N) [Recursive]**
- `BUILD` (@ `t/plugin2/hooks.t`) -> **O(N^6)**
- `run_test` (@ `t/request.t`) -> **O(N^6)**
- `all_tests` (@ `t/cookie.t`) -> **O(N^5)**
- `run_test` (@ `t/request_upload.t`) -> **O(N^5)**
- `run_tests` (@ `t/auto_page.t`) -> **O(N^3)**
- `_build_config` (@ `t/config_reader.t`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `run_test` (@ `t/request_upload.t`) -> DB Complexity: **58**
- `hexe` (@ `t/file_utils.t`) -> DB Complexity: **17**
- `test_app` (@ `t/dsl/uri_for_route.t`) -> DB Complexity: **16**
- `generate_id` (@ `t/session_bad_client_cookie.t`) -> DB Complexity: **15**
- `all_tests` (@ `t/cookie.t`) -> DB Complexity: **14**
- `run_tests` (@ `t/auto_page.t`) -> DB Complexity: **8**
- `run_test` (@ `t/request.t`) -> DB Complexity: **8**
- `MyApp` (@ `t/error.t`) -> DB Complexity: **6**
- `write_file` (@ `t/file_utils.t`) -> DB Complexity: **6**
- `_read_config_with_warnings` (@ `t/strict_config.t`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 83 | 4442.1 | 71.62% | 2.98% |
| `t/dsl` | 24 | 1503.92 | 74.65% | 7.01% |
| `t/issues` | 19 | 555.32 | 72.19% | 4.94% |
| `t/plugin2` | 13 | 358.18 | 74.38% | 0.0% |
| `t/scope_problems` | 5 | 148.12 | 72.81% | 0.0% |
| `share/skel/tutorial/t` | 4 | 82.84 | 36.16% | 0.0% |
| `__monolith__` | 7 | 59.94 | 0.0% | 0.0% |
| `share/skel/default/public` | 3 | 54.92 | 7.51% | 0.0% |
| `share/skel/tutorial/public` | 3 | 54.92 | 7.51% | 0.0% |
| `t/examples` | 2 | 53.86 | 48.04% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `share/skel/tutorial/db/entries.sql` -> **100.0%** Exposure
- `share/skel/tutorial/db/users.sql` -> **100.0%** Exposure
- `t/dsl/extend.t` -> **98.6851%** Exposure
- `t/roles/hook.t` -> **96.7987%** Exposure
- `t/issues/gh-797.t` -> **93.8921%** Exposure
### Highest State Flux (Mutation/Volatility)
- `share/skel/default/t/002_index_route.t` -> **100.0%** Exposure
- `share/skel/tutorial/t/002_index_route.t` -> **100.0%** Exposure
- `t/caller.t` -> **100.0%** Exposure
- `t/deserialize.t` -> **100.0%** Exposure
- `t/disp_named_capture.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/roles/hook.t` -> **2** Orphaned Functions | **0** Duplicates
- `share/skel/tutorial/db/users.sql` -> **2** Orphaned Functions | **0** Duplicates
- `t/config_reader.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/dsl/extend.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/dsl/send_as.t` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`share/docker/Dockerfile`** -> AI Confidence: **98.84%**
2. **`share/skel/tutorial/db/entries.sql`** -> AI Confidence: **98.84%**
3. **`share/skel/tutorial/db/users.sql`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `t/cookie.t` -> **100.0%** Exposure
- `t/dsl/uri_for_route.t` -> **100.0%** Exposure
- `t/error.t` -> **100.0%** Exposure
- `t/plugin2/hooks.t` -> **100.0%** Exposure
- `t/request.t` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `script/dancer2` -> **0.4065%** Exposure
### Hardcoded Payload Artifacts
- `t/error.t` -> **97.8667%** Exposure
### Algorithmic DoS Exposure
- `t/cookie.t` -> **100.0%** Exposure
- `t/dsl/uri_for_route.t` -> **100.0%** Exposure
- `t/error.t` -> **100.0%** Exposure
- `t/plugin2/hooks.t` -> **100.0%** Exposure
- `t/request_upload.t` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1255` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/request_upload.t` (PERL) -> Cumulative Risk: **728.29**
- **Archetype:** `file_cluster_0` (Distance: 12.757 IQR)
- **Magnitude:** 343.54 | **LOC:** 210 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run_test` (Impact: 215.3), `test_path` (Impact: 1.9)

### 2. `t/error.t` (PERL) -> Cumulative Risk: **725.16**
- **Archetype:** `file_cluster_0` (Distance: 12.235 IQR)
- **Magnitude:** 318.96 | **LOC:** 320 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `MyApp` (Impact: 212.3), `throw` (Impact: 8.1), `new` (Impact: 1.6)

### 3. `t/plugin2/hooks.t` (PERL) -> Cumulative Risk: **624.51**
- **Archetype:** `file_cluster_0` (Distance: 11.793 IQR)
- **Magnitude:** 61.5 | **LOC:** 83 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `BUILD` (Impact: 30.3)

### 4. `t/session_bad_client_cookie.t` (PERL) -> Cumulative Risk: **620.64**
- **Archetype:** `file_cluster_0` (Distance: 11.9 IQR)
- **Magnitude:** 87.8 | **LOC:** 121 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `generate_id` (Impact: 45.1)

### 5. `t/cookie.t` (PERL) -> Cumulative Risk: **598.23**
- **Archetype:** `file_cluster_0` (Distance: 10.973 IQR)
- **Magnitude:** 201.06 | **LOC:** 211 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9505%)
- **Heaviest Functions:** `all_tests` (Impact: 155.6)

### 6. `t/dsl/uri_for_route.t` (PERL) -> Cumulative Risk: **581.99**
- **Archetype:** `file_cluster_0` (Distance: 11.474 IQR)
- **Magnitude:** 598.5 | **LOC:** 247 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9986%)
- **Heaviest Functions:** `test_app` (Impact: 527.7)

### 7. `t/request.t` (PERL) -> Cumulative Risk: **578.54**
- **Archetype:** `file_cluster_0` (Distance: 11.267 IQR)
- **Magnitude:** 239.7 | **LOC:** 274 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.997%), Algorithmic Dos (86.9295%)
- **Heaviest Functions:** `run_test` (Impact: 163.1)

### 8. `t/file_utils.t` (PERL) -> Cumulative Risk: **536.24**
- **Archetype:** `file_cluster_0` (Distance: 12.804 IQR)
- **Magnitude:** 163.92 | **LOC:** 73 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (91.35%)
- **Heaviest Functions:** `hexe` (Impact: 117.2), `write_file` (Impact: 5.6)

### 9. `tools/cookie_perf.pl` (PERL) -> Cumulative Risk: **504.02**
- **Archetype:** `file_cluster_0` (Distance: 11.731 IQR)
- **Magnitude:** 0.1 | **LOC:** 184 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.8194%), Cognitive Load (90.5062%)
- **Heaviest Functions:** `xscookies_bake` (Impact: 14.8), `cookiebaker_bake` (Impact: 14.8)

### 10. `t/issues/gh-797.t` (PERL) -> Cumulative Risk: **486.17**
- **Archetype:** `file_cluster_13` (Distance: 12.006 IQR)
- **Magnitude:** 36.86 | **LOC:** 57 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (93.8921%), Cognitive Load (86.5351%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/dsl/uri_for_route.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.474 IQR)
- **Top Global Matches:** file_cluster_0: 11.474, file_cluster_13: 11.778, file_cluster_8: 11.827
- **Magnitude:** 598.5 | **LOC:** 247 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (78.1373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_app` (Impact: 527.7 | O(2^N) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 30`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 6`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Plack::Builder, warnings, HTTP::Request::Common, Test::More, JSON::MaybeXS, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/request_upload.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.757 IQR)
- **Top Global Matches:** file_cluster_0: 12.757, file_cluster_13: 13.113, file_cluster_11: 13.333
- **Magnitude:** 343.54 | **LOC:** 210 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (89.2809%), Tech Debt (23.9997%)
**Top Internal Functions/Classes:**
  * `run_test` (Impact: 215.3 | O(N^5) | DB: 58)
  * `test_path` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 40`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 123`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `import: 13`
* *Defense:* `safety: 3`, `test: 8`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Path::Tiny, Test::More, Dancer2::Core::Request, Encode, Carp, strict, File::Temp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/error.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.235 IQR)
- **Top Global Matches:** file_cluster_0: 12.235, file_cluster_13: 12.422, file_cluster_11: 12.565
- **Magnitude:** 318.96 | **LOC:** 320 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (98.0391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MyApp` (Impact: 212.3 | O(2^N) | DB: 6)
  * `throw` (Impact: 8.1 | O(N^2) | DB: 1)
  * `new` (Impact: 1.6 | O(N^2))
  * `as_str` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 77`, `args: 4`, `func_start: 4`, `class_start: 6`
* *Risk/State:* `state_mutation: 86`
* *Architecture:* `api: 5`, `import: 21`
* *Defense:* `safety: 5`, `test: 36`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ref::Util, lib, Module::Runtime, errors, warnings, Dancer2::Core::Response, HTTP::Request::Common, Dancer2::Core::App...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.267 IQR)
- **Top Global Matches:** file_cluster_0: 11.267, file_cluster_8: 11.656, file_cluster_13: 11.79
- **Magnitude:** 239.7 | **LOC:** 274 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (83.08%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_test` (Impact: 163.1 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 28`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 25`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Dancer2::Core::App, Test::More, Dancer2::Core::Request, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cookie.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.973 IQR)
- **Top Global Matches:** file_cluster_0: 10.973, file_cluster_13: 11.148, file_cluster_8: 11.167
- **Magnitude:** 201.06 | **LOC:** 211 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (76.3761%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `all_tests` (Impact: 155.6 | O(N^5) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 23`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Test::More, Dancer2::Core::Request, Dancer2::Core::Cookie, strict, cookie, domain, Test::Fatal
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file_utils.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.804 IQR)
- **Top Global Matches:** file_cluster_0: 12.804, file_cluster_13: 12.949, file_cluster_11: 13.376
- **Magnitude:** 163.92 | **LOC:** 73 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (91.35%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hexe` (Impact: 117.2 | O(2^N) | DB: 17)
  * `write_file` (Impact: 5.6 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 24`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `io: 3`, `import: 8`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utf8, warnings, Dancer2::FileUtils, Path::Tiny, Test::More, File::Temp, strict, Test::Fatal
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/deserialize.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.52 IQR)
- **Top Global Matches:** file_cluster_0: 12.52, file_cluster_13: 12.713, file_cluster_11: 12.875
- **Magnitude:** 132.3 | **LOC:** 229 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (87.6926%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 52`, `args: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 111`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utf8, Module::Runtime, warnings, HTTP::Request::Common, Test::More, Dancer2::Logger::Capture, JSON::MaybeXS, Dancer2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/parameters.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.318 IQR)
- **Top Global Matches:** file_cluster_0: 11.318, file_cluster_8: 11.636, file_cluster_13: 11.717
- **Magnitude:** 125.62 | **LOC:** 393 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.519%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 55`, `class_start: 7`
* *Risk/State:* `state_mutation: 95`
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `safety: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utf8, critic, warnings, HTTP::Request::Common, Test::More, Dancer2, Encode, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.391 IQR)
- **Top Global Matches:** file_cluster_0: 12.391, file_cluster_13: 12.575, file_cluster_11: 12.725
- **Magnitude:** 124.36 | **LOC:** 352 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (88.8412%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `my_after` (Impact: 3.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 72`, `args: 8`, `func_start: 1`, `class_start: 9`
* *Risk/State:* `state_mutation: 103`
* *Architecture:* `api: 13`, `import: 21`
* *Defense:* `safety: 3`, `test: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ref::Util, Template, Sub::Util, Capture::Tiny, warnings, Path::Tiny, HTTP::Request::Common, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dispatcher.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.019 IQR)
- **Top Global Matches:** file_cluster_0: 12.019, file_cluster_8: 12.104, file_cluster_13: 12.124
- **Magnitude:** 114.98 | **LOC:** 247 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.3141%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 42`, `args: 5`
* *Risk/State:* `state_mutation: 96`
* *Architecture:* `import: 11`
* *Defense:* `safety: 3`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ref::Util, warnings, Dancer2::Core::Hook, Dancer2::Core::App, Dancer2::Core::Response, Test::More, Dancer2::Core::Dispatcher, Dancer2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.44 IQR)
- **Top Global Matches:** file_cluster_0: 12.44, file_cluster_13: 12.577, file_cluster_11: 12.775
- **Magnitude:** 105.24 | **LOC:** 221 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.3365%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 39`, `args: 5`, `class_start: 4`
* *Risk/State:* `state_mutation: 76`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 3`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Template, lib, warnings, Dancer2::Core::Hook, HTTP::Request::Common, Path::Tiny, Test::More, Dancer2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/multiapp_template_hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.22 IQR)
- **Top Global Matches:** file_cluster_0: 12.22, file_cluster_13: 12.305, file_cluster_8: 12.392
- **Magnitude:** 100.9 | **LOC:** 206 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.9869%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 32`, `args: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 80`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `test: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hooks, warnings, Path::Tiny, HTTP::Request::Common, Test::More, routes, Dancer2, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/delayed.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.959 IQR)
- **Top Global Matches:** file_cluster_0: 11.959, file_cluster_11: 12.089, file_cluster_13: 12.182
- **Magnitude:** 93.22 | **LOC:** 189 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.2761%), Tech Debt (38.193%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 42`, `args: 3`, `class_start: 6`
* *Risk/State:* `state_mutation: 65`, `planned_debt: 4`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 13`
* *Defense:* `safety: 3`, `test: 30`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` critic, AnyEvent, warnings, HTTP::Request::Common, Test::More, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_bad_client_cookie.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.9 IQR)
- **Top Global Matches:** file_cluster_0: 11.9, file_cluster_13: 11.992, file_cluster_11: 12.291
- **Magnitude:** 87.8 | **LOC:** 121 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (88.8011%), Tech Debt (53.6699%)
**Top Internal Functions/Classes:**
  * `generate_id` (Impact: 45.1 | O(N^3) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 29`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `state_mutation: 40`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Moo, warnings, HTTP::Request::Common, HTTP::Cookies, Test::More, Path::Tiny, Dancer2, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.521 IQR)
- **Top Global Matches:** file_cluster_0: 11.521, file_cluster_13: 11.963, file_cluster_11: 12.039
- **Magnitude:** 82.92 | **LOC:** 196 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.8802%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 40`, `class_start: 3`
* *Risk/State:* `state_mutation: 57`, `dead_code: 1`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, HTTP::Request::Common, HTTP::Cookies, Test::More, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_lifecycle.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.932 IQR)
- **Top Global Matches:** file_cluster_8: 10.932, file_cluster_13: 10.999, file_cluster_0: 11.121
- **Magnitude:** 77.36 | **LOC:** 228 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (54.157%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 45`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 2`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, warnings, HTTP::Request::Common, HTTP::Cookies, Test::More, Dancer2, new, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/path.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.19 IQR)
- **Top Global Matches:** file_cluster_0: 12.19, file_cluster_13: 12.408, file_cluster_11: 12.607
- **Magnitude:** 75.98 | **LOC:** 126 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.1001%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Plack::Builder, warnings, HTTP::Request::Common, Test::More, Dancer2, strict, Plack::Request, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/issues/gh-1564.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.955 IQR)
- **Top Global Matches:** file_cluster_13: 11.955, file_cluster_0: 12.063, file_cluster_8: 12.117
- **Magnitude:** 74.92 | **LOC:** 114 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (73.9171%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 27`, `args: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 2`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Plack::Builder, warnings, HTTP::Request::Common, Test::More, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_engines.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.041 IQR)
- **Top Global Matches:** file_cluster_13: 12.041, file_cluster_0: 12.123, file_cluster_11: 12.331
- **Magnitude:** 73.8 | **LOC:** 117 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (84.4078%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 34`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, YAML, HTTP::Request::Common, HTTP::Cookies, Test::More, Path::Tiny, Dancer2, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config_reader.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.056 IQR)
- **Top Global Matches:** file_cluster_0: 11.056, file_cluster_13: 11.248, file_cluster_8: 11.317
- **Magnitude:** 72.48 | **LOC:** 182 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (61.591%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `config_any` (Impact: 18.5 | O(N^2))
  * `_build_config` (Impact: 8.9 | O(N^3) | DB: 2)
  * `config_reader` (Impact: 8.2 | O(N^2))
  * `config_user` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 39`, `args: 4`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 31`, `orphaned_logic: 1`
* *Architecture:* `import: 11`
* *Defense:* `safety: 5`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2::ConfigReader::Config::Any, Moo, warnings, Path::Tiny, Test::More, Dancer2::Core::Runner, Carp, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/app.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.817 IQR)
- **Top Global Matches:** file_cluster_0: 10.817, file_cluster_13: 11.08, file_cluster_8: 11.105
- **Magnitude:** 64.6 | **LOC:** 285 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.0166%), Tech Debt (14.9423%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 44`
* *Risk/State:* `state_mutation: 45`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `import: 9`
* *Defense:* `safety: 3`, `test: 10`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, Dancer2::Core::Hook, Dancer2::Core::App, Path::Tiny, Test::More, Dancer2::Core::Dispatcher, Dancer2, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/plugin2/hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.793 IQR)
- **Top Global Matches:** file_cluster_0: 11.793, file_cluster_13: 11.876, file_cluster_11: 12.135
- **Magnitude:** 61.5 | **LOC:** 83 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BUILD` (Impact: 30.3 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, HTTP::Request::Common, Dancer2::Plugin, Test::More, Dancer2::Plugin::FooDetector, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_hooks_no_change_id.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.402 IQR)
- **Top Global Matches:** file_cluster_0: 11.402, file_cluster_13: 11.468, file_cluster_8: 11.476
- **Magnitude:** 60.0 | **LOC:** 196 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.6071%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 45`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 2`, `test: 12`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, warnings, HTTP::Request::Common, HTTP::Cookies, Test::More, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.386 IQR)
- **Top Global Matches:** file_cluster_0: 11.386, file_cluster_8: 11.46, file_cluster_13: 11.488
- **Magnitude:** 59.98 | **LOC:** 191 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.1482%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 44`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 2`, `test: 12`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, HTTP::Request::Common, HTTP::Cookies, Test::More, Dancer2, strict, Plack::Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/serializer_mutable.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.773 IQR)
- **Top Global Matches:** file_cluster_0: 11.773, file_cluster_13: 11.843, file_cluster_8: 12.178
- **Magnitude:** 59.8 | **LOC:** 118 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.2227%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ref::Util, Dancer2::Serializer::Mutable, warnings, YAML, HTTP::Request::Common, Test::More, JSON::MaybeXS, Dancer2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/charset_server.t` (PERL) | Magnitude: 29.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, branch: 18, structural_boundaries: 13, state_mutation: 10
- `t/disp_named_capture.t` (PERL) | Magnitude: 35.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, branch: 16, structural_boundaries: 13, indent_spaces: 8
- `t/logger_console.t` (PERL) | Magnitude: 24.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 13, structural_boundaries: 9, state_mutation: 9, decorators: 6
- `t/dsl/any.t` (PERL) | Magnitude: 43.82 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 27, branch: 19, structural_boundaries: 16
- `t/plugin2/no-config.t` (PERL) | Magnitude: 15.48 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, branch: 13, structural_boundaries: 8, decorators: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/dsl/splat.t` (PERL) | Magnitude: 28.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 13, state_mutation: 12, structural_boundaries: 11, indent_spaces: 11
- `t/plugin_register.t` (PERL) | Magnitude: 15.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, branch: 27, structural_boundaries: 15, test: 10
- `t/serializer_mutable_custom.t` (PERL) | Magnitude: 49.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, branch: 51, state_mutation: 43, structural_boundaries: 26
- `t/plugin2/define-keywords.t` (PERL) | Magnitude: 18.38 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 14, structural_boundaries: 9, decorators: 6, import: 6
- `t/issues/gh-1449/gh-1449.t` (PERL) | Magnitude: 36.78 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 28, structural_boundaries: 21, indent_spaces: 20, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/config_settings.t` (PERL) | Magnitude: 15.34 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 10, branch: 7, structural_boundaries: 4, import: 4
- `t/app/t1/bin/app.psgi` (PERL) | Magnitude: 12.08 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, ssr_boundaries: 1
- `t/app/t_config_file_extended/bin/app.psgi` (PERL) | Magnitude: 12.08 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, ssr_boundaries: 1
- `t/session_lifecycle.t` (PERL) | Magnitude: 77.36 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 153, state_mutation: 53, structural_boundaries: 45, test: 33
- `t/psgi_app.t` (PERL) | Magnitude: 33.5 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 25, state_mutation: 19, encapsulation: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/request_upload.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 343.54
- `t/error.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 318.96
- `t/request.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 239.7
- `t/cookie.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 201.06
- `t/file_utils.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 163.92

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/dsl/content.t` -> **Severity: 0.424** (Embedded: 0.0133 * Error Risk: 31.9768%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/dsl/content.t` -> **Severity: 1219.375** (Blast Radius: 15.408 * Doc Risk: 79.1391%)
- `t/issues/gh-1449/TestPlugin.pm` -> **Severity: 588.866** (Blast Radius: 8.03 * Doc Risk: 73.3333%)
- `t/caller.t` -> **Severity: 434.0** (Blast Radius: 4.34 * Doc Risk: 100.0%)
- `t/config_file_extended.t` -> **Severity: 434.0** (Blast Radius: 4.34 * Doc Risk: 100.0%)
- `t/config_many.t` -> **Severity: 434.0** (Blast Radius: 4.34 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
