# ARCHITECTURAL_BRIEF: sqitch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/sqitch` |
| **Timestamp** | `2026-08-03T19:30:32.773564+00:00` |
| **Scan Duration** | `0.73s` |
| **Git Branch** | `develop` |
| **Git Commit** | `0ab857e3bb5060e6feda0dd3e05ebb04f7aac85b` |
| **Git Remote** | `https://github.com/sqitchers/sqitch.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 26 malicious artifacts.

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
| Total Artifacts | 364 |
| Analyzed Artifacts (Scanned) | 98 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 266 |
| Total LOC | 23292 |
| Volatility Index | 0.031 |
| % Scanned of codebase = | 26.9% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3801 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4347 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6693 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 62 | 23229 | 63.3% |
| SQLITE | 26 | 63 | 26.5% |
| MARKDOWN | 4 | 0 | 4.1% |
| XML | 4 | 0 | 4.1% |
| PLAINTEXT | 2 | 0 | 2.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.149`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 44 | 44.9% |
| file_cluster_8 | 39 | 39.8% |
| file_cluster_13 | 7 | 7.1% |
| file_cluster_9 | 2 | 2.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 6.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 266*

**Composition by Extension & Reason:**
- `.pm`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 30x Excluded (Unsupported Extension: '.tmpl')
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.plan`: 14x Excluded (Unsupported Extension: '.plan'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 12x Excluded (Unsupported Extension: '.conf')
- `.sh`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.po`: 6x Excluded (Unsupported Extension: '.po')
- `.t`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 3x Excluded (Unsupported Extension: '.ini'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mo`: 3x Excluded (Unsupported Extension: '.mo')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.spec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 94.6 | 47.4 | 61.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 83.7 | 25.6 | 23.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 0.2 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 21.4 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.4 | 99.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 68.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.6 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 95.3 | 3.3 | 0.0 | 0.0 |
| Documentation Exposure | 1.2 | 100.0 | 24.3 | 14.8 | 6.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/plan.t` (Hits: 14)
- `t/change.t` (Hits: 12)
- `t/oracle.t` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.t** (`t/config.t`) — 15 inbound connections
2. **options.t** (`t/options.t`) — 8 inbound connections
3. **change.t** (`t/change.t`) — 5 inbound connections
4. **engine.t** (`t/engine.t`) — 3 inbound connections
5. **command.t** (`t/command.t`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **engine.t** (`t/engine.t`) — 47 outbound dependencies
2. **plan.t** (`t/plan.t`) — 37 outbound dependencies
3. **command.t** (`t/command.t`) — 33 outbound dependencies
4. **add.t** (`t/add.t`) — 31 outbound dependencies
5. **base.t** (`t/base.t`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `is_deployed_tag` (@ `t/engine.t`) -> Impact: **1869.9** | LOC: 1421
- `run` (@ `xt/dependency_report`) -> Impact: **173.4** | LOC: 38
- `report_on` (@ `xt/dependency_report`) -> Impact: **127.9** | LOC: 38
- `change` (@ `t/plan.t`) -> Impact: **48.3** | LOC: 31
- `new` (@ `inc/Menlo/Sqitch.pm`) -> Impact: **43.2** | LOC: 16
- `version` (@ `t/plan.t`) -> Impact: **42.2** | LOC: 5
- `dep` (@ `t/add.t`) -> Impact: **36.8** | LOC: 9
- `dep` (@ `t/rework.t`) -> Impact: **36.8** | LOC: 9
- `configure` (@ `inc/Menlo/Sqitch.pm`) -> Impact: **34.6** | LOC: 13
- `prag` (@ `t/plan.t`) -> Impact: **29.2** | LOC: 14

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `is_deployed_tag` (@ `t/engine.t`) -> **O(2^N) [Recursive]**
- `new` (@ `xt/dependency_report`) -> **O(2^N) [Recursive]**
- `new` (@ `inc/Menlo/Sqitch.pm`) -> **O(2^N) [Recursive]**
- `configure` (@ `inc/Menlo/Sqitch.pm`) -> **O(2^N) [Recursive]**
- `dep` (@ `t/add.t`) -> **O(2^N) [Recursive]**
- `version` (@ `t/plan.t`) -> **O(2^N) [Recursive]**
- `dep` (@ `t/rework.t`) -> **O(2^N) [Recursive]**
- `report_on` (@ `xt/dependency_report`) -> **O(2^N) [Recursive]**
- `save_meta` (@ `inc/Menlo/Sqitch.pm`) -> **O(2^N) [Recursive]**
- `find_prereqs` (@ `inc/Menlo/Sqitch.pm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `is_deployed_tag` (@ `t/engine.t`) -> DB Complexity: **159**
- `new` (@ `inc/Menlo/Sqitch.pm`) -> DB Complexity: **8**
- `contents_of` (@ `t/add.t`) -> DB Complexity: **8**
- `change` (@ `t/plan.t`) -> DB Complexity: **7**
- `Declarative_Block` (@ `etc/tools/upgrade-registry-to-mysql-5.5.0.sql`) -> DB Complexity: **7**
- `configure` (@ `inc/Menlo/Sqitch.pm`) -> DB Complexity: **6**
- `tag` (@ `t/plan.t`) -> DB Complexity: **6**
- `Declarative_Block` (@ `etc/tools/upgrade-registry-to-mysql-5.5.0.sql`) -> DB Complexity: **6**
  * *Intent:* -- This script upgrades the Sqitch registry for MySQL 5.5.0 and higher. It -- sets up triggers in the registry to use it to emulate CHECK constraints....
- `new` (@ `xt/dependency_report`) -> DB Complexity: **5**
- `save_meta` (@ `inc/Menlo/Sqitch.pm`) -> DB Complexity: **4**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 55 | 24590.75 | 72.13% | 5.82% |
| `xt` | 3 | 414.02 | 30.29% | 0.0% |
| `inc/Menlo` | 1 | 156.74 | 21.39% | 36.04% |
| `t/click-conf` | 8 | 103.32 | 7.61% | 0.0% |
| `t/sql/deploy` | 8 | 84.16 | 5.0% | 0.0% |
| `t/sql/revert` | 7 | 73.64 | 5.0% | 0.0% |
| `__monolith__` | 3 | 52.28 | 0.0% | 0.0% |
| `bin` | 1 | 12.08 | 5.0% | 0.0% |
| `t/engine/deploy` | 2 | 7.92 | 5.0% | 100.0% |
| `t/engine/revert` | 2 | 6.48 | 5.0% | 100.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `etc/tools/upgrade-registry-to-mysql-5.5.0.sql` -> **100.0%** Exposure
- `etc/tools/upgrade-registry-to-mysql-5.6.4.sql` -> **100.0%** Exposure
- `t/engine/deploy/func/add_user.sql` -> **100.0%** Exposure
- `t/engine/deploy/users.sql` -> **100.0%** Exposure
- `t/engine/deploy/widgets.sql` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `t/add.t` -> **100.0%** Exposure
- `t/base.t` -> **100.0%** Exposure
- `t/blank.t` -> **100.0%** Exposure
- `t/clickhouse.t` -> **100.0%** Exposure
- `t/cockroach.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `etc/tools/upgrade-registry-to-mysql-5.5.0.sql` -> **0** Orphaned Functions | **7** Duplicates
- `etc/tools/upgrade-registry-to-mysql-5.6.4.sql` -> **0** Orphaned Functions | **5** Duplicates
- `t/engine/deploy/func/add_user.sql` -> **1** Orphaned Functions | **3** Duplicates
- `t/engine/revert/func/add_user.sql` -> **1** Orphaned Functions | **2** Duplicates
- `t/engine/deploy/users.sql` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`etc/tools/upgrade-registry-to-mysql-5.5.0.sql`** -> AI Confidence: **99.29%**
2. **`t/sql/verify/users.sql`** -> AI Confidence: **98.85%**
3. **`etc/tools/upgrade-registry-to-mysql-5.6.4.sql`** -> AI Confidence: **98.84%**
4. **`t/engine/deploy/func/add_user.sql`** -> AI Confidence: **98.84%**
5. **`t/engine/deploy/users.sql`** -> AI Confidence: **98.84%**
6. **`t/engine/deploy/widgets.sql`** -> AI Confidence: **98.84%**
7. **`t/engine/revert/func/add_user.sql`** -> AI Confidence: **98.84%**
8. **`t/engine/revert/users.sql`** -> AI Confidence: **98.84%**
9. **`t/engine/revert/widgets.sql`** -> AI Confidence: **98.84%**
10. **`t/engine/reworked/deploy/users@alpha.sql`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `t/change.t` -> **100.0%** Exposure
- `t/command.t` -> **100.0%** Exposure
- `t/engine.t` -> **100.0%** Exposure
- `xt/dependency_report` -> **100.0%** Exposure
- `t/cx_cmd_role.t` -> **99.997%** Exposure
### Algorithmic DoS Exposure
- `inc/Menlo/Sqitch.pm` -> **100.0%** Exposure
- `t/engine.t` -> **100.0%** Exposure
- `etc/tools/upgrade-registry-to-mysql-5.6.4.sql` -> **44.3283%** Exposure
- `xt/dependency_report` -> **27.3101%** Exposure
- `etc/tools/upgrade-registry-to-mysql-5.5.0.sql` -> **23.4629%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `990` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `xt/dependency_report` (PERL) -> Cumulative Risk: **619.04**
- **Archetype:** `file_cluster_0` (Distance: 12.638 IQR)
- **Magnitude:** 408.1 | **LOC:** 184 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Cognitive Load (90.857%)
- **Heaviest Functions:** `run` (Impact: 173.4), `report_on` (Impact: 127.9), `new` (Impact: 17.7)

### 2. `t/cx_cmd_role.t` (PERL) -> Cumulative Risk: **589.25**
- **Archetype:** `file_cluster_13` (Distance: 12.171 IQR)
- **Magnitude:** 58.04 | **LOC:** 110 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.997%), Cognitive Load (91.9589%)
- **Heaviest Functions:** `options` (Impact: 2.3)

### 3. `t/engine.t` (PERL) -> Cumulative Risk: **495.88**
- **Archetype:** `file_cluster_8` (Distance: 12.575 IQR)
- **Magnitude:** 2611.74 | **LOC:** 3749 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.7597%)
- **Heaviest Functions:** `is_deployed_tag` (Impact: 1869.9)

### 4. `inc/Menlo/Sqitch.pm` (PERL) -> Cumulative Risk: **486.77**
- **Archetype:** `file_cluster_8` (Distance: 9.535 IQR)
- **Magnitude:** 156.74 | **LOC:** 314 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (98.3116%), Verification (80.0%)
- **Heaviest Functions:** `new` (Impact: 43.2), `configure` (Impact: 34.6), `save_meta` (Impact: 11.7)

### 5. `etc/tools/upgrade-registry-to-mysql-5.5.0.sql` (SQLITE) -> Cumulative Risk: **484.63**
- **Archetype:** `file_cluster_8` (Distance: 12.461 IQR)
- **Magnitude:** 0.04 | **LOC:** 31 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (91.7284%), Cognitive Load (90.025%)
- **Heaviest Functions:** `Declarative_Block` (Impact: 3.4), `Declarative_Block` (Impact: 3.4), `Declarative_Block` (Impact: 2.0)

### 6. `t/conn_cmd_role.t` (PERL) -> Cumulative Risk: **474.05**
- **Archetype:** `file_cluster_0` (Distance: 11.433 IQR)
- **Magnitude:** 39.14 | **LOC:** 113 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Cognitive Load (85.6019%), Logic Bomb (63.1545%)
- **Heaviest Functions:** `options` (Impact: 2.3)

### 7. `t/base.t` (PERL) -> Cumulative Risk: **466.48**
- **Archetype:** `file_cluster_0` (Distance: 12.35 IQR)
- **Magnitude:** 294.4 | **LOC:** 746 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (93.6528%), Cognitive Load (92.1009%)
- **Heaviest Functions:** `puke` (Impact: 5.0)

### 8. `t/mooseless.t` (PERL) -> Cumulative Risk: **451.74**
- **Archetype:** `file_cluster_13` (Distance: 13.453 IQR)
- **Magnitude:** 36.46 | **LOC:** 32 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (94.6321%), Documentation (91.2761%)

### 9. `t/clickhouse.t` (PERL) -> Cumulative Risk: **444.12**
- **Archetype:** `file_cluster_0` (Distance: 12.471 IQR)
- **Magnitude:** 413.6 | **LOC:** 1023 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (95.34%), Cognitive Load (88.7772%)

### 10. `t/command.t` (PERL) -> Cumulative Risk: **434.37**
- **Archetype:** `file_cluster_0` (Distance: 12.014 IQR)
- **Magnitude:** 222.94 | **LOC:** 784 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9986%), Cognitive Load (85.9772%)
- **Heaviest Functions:** `options` (Impact: 2.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/mysql.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.93 IQR)
- **Top Global Matches:** file_cluster_0: 12.93, file_cluster_13: 13.113, file_cluster_8: 13.205
- **Magnitude:** 13752.85 | **LOC:** 742 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.8836%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 122`, `args: 17`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 373`
* *Architecture:* `io: 3`, `import: 35`
* *Defense:* `safety: 6`, `test: 37`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Test::File::Contents, query, Locale::TextDomain, warning, TestConfig, database, column...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/engine.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.575 IQR)
- **Top Global Matches:** file_cluster_8: 12.575, file_cluster_0: 12.582, file_cluster_13: 12.745
- **Magnitude:** 2611.74 | **LOC:** 3749 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 159
- **Risk Profile:** Cognitive Load (39.7581%), Tech Debt (12.5031%)
**Top Internal Functions/Classes:**
  * `is_deployed_tag` (Impact: 1869.9 | O(2^N) | DB: 159)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 743`, `structural_boundaries: 339`, `args: 15`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 669`, `planned_debt: 1`, `fragile_debt: 11`
* *Architecture:* `io: 3`, `concurrency: 7`, `import: 82`
* *Defense:* `safety: 2`, `test: 376`, `sync_locks: 3`, `cleanup: 180`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.609
  * `Choke Point (Betweenness):` 0.007571 | `Ripple Effect (Closeness):` 0.053019
  * `Imports (Out-Degree: 5):` lib, Test::MockObject::Extends, info, deploys, arg, List::Util, following, ID...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/plan.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.388 IQR)
- **Top Global Matches:** file_cluster_0: 12.388, file_cluster_8: 12.578, file_cluster_13: 12.814
- **Magnitude:** 809.64 | **LOC:** 2062 | **CtrlFlow:** 82.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (79.6683%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `change` (Impact: 48.3 | O(N^2) | DB: 7)
  * `version` (Impact: 42.2 | O(2^N))
  * `prag` (Impact: 29.2 | O(N^2))
  * `tag` (Impact: 26.7 | O(N^2) | DB: 6)
  * `dep` (Impact: 23.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 782`, `structural_boundaries: 162`, `args: 13`, `func_start: 10`
* *Risk/State:* `state_mutation: 566`
* *Architecture:* `io: 14`, `import: 31`
* *Defense:* `safety: 3`, `test: 32`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.231
  * `Choke Point (Betweenness):` 0.003275 | `Ripple Effect (Closeness):` 0.041483
  * `Imports (Out-Degree: 3):` lib, Test::File::Contents, Locale::TextDomain, more, sorting, TestConfig, rework, tags...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/rework.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.404 IQR)
- **Top Global Matches:** file_cluster_0: 12.404, file_cluster_8: 12.431, file_cluster_17: 12.607
- **Magnitude:** 458.64 | **LOC:** 1089 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (81.3867%), Tech Debt (10.0498%)
**Top Internal Functions/Classes:**
  * `dep` (Impact: 36.8 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 156`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 404`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `import: 20`
* *Defense:* `safety: 3`, `test: 41`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.758
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.036082
  * `Imports (Out-Degree: 1):` lib, App::Sqitch::Command::add, Test::File::Contents, config, Locale::TextDomain, TestConfig, Data::Dump, File::Path...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/add.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.541 IQR)
- **Top Global Matches:** file_cluster_0: 12.541, file_cluster_13: 12.73, file_cluster_8: 12.747
- **Magnitude:** 446.16 | **LOC:** 1039 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (80.694%), Tech Debt (11.9018%)
**Top Internal Functions/Classes:**
  * `dep` (Impact: 36.8 | O(2^N) | DB: 1)
  * `contents_of` (Impact: 6.3 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 138`, `args: 9`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 386`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `import: 29`
* *Defense:* `safety: 2`, `test: 60`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` lib, Test::File::Contents, Test::Dir, config, Locale::TextDomain, TestConfig, Template, App::Sqitch::Target...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/clickhouse.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.471 IQR)
- **Top Global Matches:** file_cluster_0: 12.471, file_cluster_13: 12.796, file_cluster_8: 12.809
- **Magnitude:** 413.6 | **LOC:** 1023 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.7772%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 480`, `structural_boundaries: 144`, `args: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 381`, `dead_code: 2`
* *Architecture:* `io: 3`, `import: 36`
* *Defense:* `safety: 5`, `test: 44`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Test::File::Contents, DBD::ODBC, override, False, Locale::TextDomain, client, TestConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/dependency_report` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.638 IQR)
- **Top Global Matches:** file_cluster_0: 12.638, file_cluster_13: 12.845, file_cluster_17: 12.963
- **Magnitude:** 408.1 | **LOC:** 184 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (90.857%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 173.4 | O(N^5) | DB: 1)
  * `report_on` (Impact: 127.9 | O(2^N) | DB: 4)
  * `new` (Impact: 17.7 | O(2^N) | DB: 5)
  * `is_build` (Impact: 17.4 | O(N^2) | DB: 2)
  * `_fetch` (Impact: 5.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 45`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* `io: 6`, `import: 7`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Tiny, Getopt::Long, warnings, JSON::PP, utf8, v5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.234 IQR)
- **Top Global Matches:** file_cluster_0: 12.234, file_cluster_8: 12.387, file_cluster_13: 12.511
- **Magnitude:** 325.82 | **LOC:** 1162 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.7697%), Tech Debt (15.0646%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 95`, `args: 6`
* *Risk/State:* `high_risk_execution: 47`, `state_mutation: 292`, `fragile_debt: 4`
* *Architecture:* `import: 25`
* *Defense:* `safety: 2`, `test: 106`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 99.743
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.146756
  * `Imports (Out-Degree: 0):` lib, config, Locale::TextDomain, File::Spec, TestConfig, system, File::Path, strict...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `t/snowflake.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.491 IQR)
- **Top Global Matches:** file_cluster_0: 12.491, file_cluster_13: 12.738, file_cluster_8: 12.861
- **Magnitude:** 307.14 | **LOC:** 650 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.2673%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 131`, `args: 7`
* *Risk/State:* `state_mutation: 282`
* *Architecture:* `io: 6`, `import: 31`
* *Defense:* `safety: 8`, `test: 25`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Test::File::Contents, Locale::TextDomain, TestConfig, COMMENT, column, App::Sqitch::Target, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/target.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.152 IQR)
- **Top Global Matches:** file_cluster_0: 12.152, file_cluster_13: 12.543, file_cluster_8: 12.577
- **Magnitude:** 298.7 | **LOC:** 735 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (88.7205%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_load` (Impact: 8.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 72`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 276`
* *Architecture:* `api: 1`, `import: 32`
* *Defense:* `safety: 3`, `test: 38`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.599
  * `Choke Point (Betweenness):` 0.002389 | `Ripple Effect (Closeness):` 0.040123
  * `Imports (Out-Degree: 3):` lib, config, List::Util, Locale::TextDomain, TestConfig, configuration, section, target...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/pg.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.783 IQR)
- **Top Global Matches:** file_cluster_0: 12.783, file_cluster_13: 12.965, file_cluster_8: 13.13
- **Magnitude:** 295.94 | **LOC:** 566 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.2359%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 110`, `args: 14`
* *Risk/State:* `state_mutation: 272`
* *Architecture:* `io: 3`, `import: 30`
* *Defense:* `safety: 7`, `test: 32`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Test::File::Contents, Locale::TextDomain, ORDER, TestConfig, column, App::Sqitch::Target, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.35 IQR)
- **Top Global Matches:** file_cluster_0: 12.35, file_cluster_13: 12.49, file_cluster_8: 12.677
- **Magnitude:** 294.4 | **LOC:** 746 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.1009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `puke` (Impact: 5.0 | O(N^1))
    * *Intent:* # Now make it die.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 144`, `args: 7`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 278`
* *Architecture:* `io: 5`, `import: 40`
* *Defense:* `safety: 2`, `test: 28`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.521
  * `Choke Point (Betweenness):` 0.001396 | `Ripple Effect (Closeness):` 0.010309
  * `Imports (Out-Degree: 1):` lib, info, Locale::TextDomain, Sys::Hostname, TTY, default, emitted, TestConfig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/log.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.187 IQR)
- **Top Global Matches:** file_cluster_0: 12.187, file_cluster_8: 12.209, file_cluster_13: 12.379
- **Magnitude:** 273.04 | **LOC:** 756 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.9018%), Tech Debt (19.9721%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 100`, `args: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 245`, `fragile_debt: 4`
* *Architecture:* `import: 22`
* *Defense:* `safety: 2`, `test: 17`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lib, config, Locale::TextDomain, TestConfig, strict, Path::Class, headers, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/oracle.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.179 IQR)
- **Top Global Matches:** file_cluster_0: 12.179, file_cluster_13: 12.646, file_cluster_11: 12.749
- **Magnitude:** 265.82 | **LOC:** 727 | **CtrlFlow:** 81.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.3042%), Tech Debt (16.3226%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 85`, `args: 7`
* *Risk/State:* `state_mutation: 241`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `import: 21`
* *Defense:* `safety: 5`, `test: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Locale::TextDomain, as, TestConfig, ORACLE_HOME, column, App::Sqitch::Target, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/command.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.014 IQR)
- **Top Global Matches:** file_cluster_0: 12.014, file_cluster_13: 12.307, file_cluster_8: 12.364
- **Magnitude:** 222.94 | **LOC:** 784 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (85.9772%), Tech Debt (10.5161%)
**Top Internal Functions/Classes:**
  * `options` (Impact: 2.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 90`, `args: 2`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 208`, `planned_debt: 2`
* *Architecture:* `import: 39`
* *Defense:* `safety: 2`, `test: 48`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.115
  * `Choke Point (Betweenness):` 0.010309 | `Ripple Effect (Closeness):` 0.051191
  * `Imports (Out-Degree: 4):` lib, class, info, Test::Dir, List::Util, config, Locale::TextDomain, path...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/plan_cmd.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.541 IQR)
- **Top Global Matches:** file_cluster_8: 11.541, file_cluster_0: 11.615, file_cluster_13: 11.744
- **Magnitude:** 214.24 | **LOC:** 714 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (66.9491%), Tech Debt (21.1591%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 79`, `args: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 187`, `fragile_debt: 4`
* *Architecture:* `import: 22`
* *Defense:* `safety: 2`, `test: 15`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lib, config, Locale::TextDomain, changes, TestConfig, strict, Path::Class, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/firebird.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.149 IQR)
- **Top Global Matches:** file_cluster_0: 12.149, file_cluster_13: 12.463, file_cluster_8: 12.656
- **Magnitude:** 206.06 | **LOC:** 516 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.0116%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 94`, `args: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 183`
* *Architecture:* `io: 5`, `import: 30`
* *Defense:* `safety: 7`, `test: 17`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Locale::TextDomain, useful, client, TestConfig, File::Spec::Functions, column, App::Sqitch::Target...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rebase.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.592 IQR)
- **Top Global Matches:** file_cluster_0: 11.592, file_cluster_8: 11.703, file_cluster_13: 11.806
- **Magnitude:** 198.9 | **LOC:** 738 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (62.1913%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 72`, `args: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 171`
* *Architecture:* `import: 28`
* *Defense:* `safety: 2`, `test: 72`, `sync_locks: 8`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lib, variables, App::Sqitch::Target, MockOutput, strict, App::Sqitch::X, config, Test::Exception...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/init.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.54 IQR)
- **Top Global Matches:** file_cluster_0: 11.54, file_cluster_8: 11.708, file_cluster_13: 11.853
- **Magnitude:** 198.86 | **LOC:** 682 | **CtrlFlow:** 75.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (81.3278%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 70`, `args: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 173`
* *Architecture:* `io: 3`, `import: 19`
* *Defense:* `safety: 2`, `test: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` lib, Test::File::Contents, Test::Dir, config, Locale::TextDomain, TestConfig, command, File::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/vertica.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.318 IQR)
- **Top Global Matches:** file_cluster_0: 12.318, file_cluster_13: 12.567, file_cluster_8: 12.704
- **Magnitude:** 192.36 | **LOC:** 402 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.9228%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 66`, `args: 7`
* *Risk/State:* `state_mutation: 171`
* *Architecture:* `io: 1`, `import: 21`
* *Defense:* `safety: 7`, `test: 18`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, column, App::Sqitch::Target, listagg, strict, Test::Exception, Locale::TextDomain, table...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/bundle.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.588 IQR)
- **Top Global Matches:** file_cluster_0: 11.588, file_cluster_8: 11.646, file_cluster_13: 11.802
- **Magnitude:** 183.48 | **LOC:** 555 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.5053%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 50`, `args: 2`
* *Risk/State:* `state_mutation: 159`
* *Architecture:* `import: 18`
* *Defense:* `safety: 2`, `test: 19`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Test::File::Contents, File::Path, strict, MockOutput, arg, Test::Exception, Locale::TextDomain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/status.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.326 IQR)
- **Top Global Matches:** file_cluster_0: 11.326, file_cluster_8: 11.427, file_cluster_13: 11.564
- **Magnitude:** 160.32 | **LOC:** 618 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (72.9532%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 75`, `args: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 135`
* *Architecture:* `import: 21`
* *Defense:* `safety: 2`, `test: 29`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lib, config, Locale::TextDomain, changes, registered, TestConfig, tags, target...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/exasol.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.806 IQR)
- **Top Global Matches:** file_cluster_0: 11.806, file_cluster_13: 12.044, file_cluster_8: 12.076
- **Magnitude:** 158.5 | **LOC:** 470 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.7088%), Tech Debt (14.5957%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 63`, `args: 8`
* *Risk/State:* `state_mutation: 136`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `import: 23`
* *Defense:* `safety: 4`, `test: 23`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Locale::TextDomain, TestConfig, column, App::Sqitch::Target, strict, table, limit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `inc/Menlo/Sqitch.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.535 IQR)
- **Top Global Matches:** file_cluster_8: 9.535, file_cluster_0: 10.157, file_cluster_13: 10.225
- **Magnitude:** 156.74 | **LOC:** 314 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (21.3935%), Tech Debt (36.04%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 43.2 | O(2^N) | DB: 8)
  * `configure` (Impact: 34.6 | O(2^N) | DB: 6)
  * `save_meta` (Impact: 11.7 | O(2^N) | DB: 4)
  * `find_prereqs` (Impact: 10.7 | O(2^N))
  * `remove_build_dependencies` (Impact: 4.7 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 20`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, base, strict, vendor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/sqlite.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.829 IQR)
- **Top Global Matches:** file_cluster_0: 11.829, file_cluster_13: 12.008, file_cluster_8: 12.098
- **Magnitude:** 155.66 | **LOC:** 411 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.8456%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 53`, `args: 6`
* *Risk/State:* `state_mutation: 134`
* *Architecture:* `io: 1`, `import: 25`
* *Defense:* `safety: 3`, `test: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib, Locale::TextDomain, TestConfig, database, column, App::Sqitch::Target, strict, table...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/conn_cmd_role.t` (PERL) | Magnitude: 39.14 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 35, branch: 31, structural_boundaries: 23
- `t/target_cmd.t` (PERL) | Magnitude: 123.48 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 435, branch: 252, decorators: 120, state_mutation: 95
- `t/log.t` (PERL) | Magnitude: 273.04 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 439, state_mutation: 245, branch: 200, structural_boundaries: 100
- `t/rework.t` (PERL) | Magnitude: 458.64 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 737, state_mutation: 404, branch: 289, structural_boundaries: 156
- `t/bundle.t` (PERL) | Magnitude: 183.48 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 246, branch: 166, state_mutation: 159, decorators: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/cx_cmd_role.t` (PERL) | Magnitude: 58.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 54, branch: 43, indent_spaces: 37, structural_boundaries: 25
- `bin/sqitch` (PERL) | Magnitude: 12.08 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 4, structural_boundaries: 2, decorators: 2, import: 2
- `t/options.t` (PERL) | Magnitude: 153.54 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 135, indent_spaces: 122, branch: 73, structural_boundaries: 44
- `t/datetime.t` (PERL) | Magnitude: 46.7 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 32, state_mutation: 30, branch: 29
- `t/mooseless.t` (PERL) | Magnitude: 36.46 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 21, branch: 17, structural_boundaries: 11, indent_spaces: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/engine.t` (PERL) | Magnitude: 2611.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1966, branch: 743, state_mutation: 669, test: 376
- `t/plan_cmd.t` (PERL) | Magnitude: 214.24 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 419, state_mutation: 187, branch: 178, structural_boundaries: 79
- `t/dbiengine_role.t` (PERL) | Magnitude: 31.22 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 30, branch: 24, state_mutation: 14
- `etc/tools/upgrade-registry-to-mysql-5.5.0.sql` (SQLITE) | Magnitude: 0.04 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 10, duplicate_logic: 7, branch: 6
- `t/item_formatter.t` (PERL) | Magnitude: 56.2 | Delta: **0.259 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 187, branch: 43, state_mutation: 36, structural_boundaries: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `t/sql/deploy/users.sql` (SQLITE) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `t/sql/deploy/widgets.sql` (SQLITE) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `t/clickhouse.t` -> Churn: **95.34%** | Cog Load: 88.7772% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/mysql.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 13752.85
- `t/clickhouse.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 413.6
- `t/snowflake.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 307.14
- `t/pg.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 295.94
- `t/oracle.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 265.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/command.t` -> **Severity: 1.031** (Bridge: 0.0103 * Flux: 99.9986%)
- `t/options.t` -> **Severity: 0.913** (Bridge: 0.0091 * Flux: 100.0%)
- `t/engine.t` -> **Severity: 0.755** (Bridge: 0.0076 * Flux: 99.7597%)
- `t/plan.t` -> **Severity: 0.327** (Bridge: 0.0033 * Flux: 99.9977%)
- `t/target.t` -> **Severity: 0.239** (Bridge: 0.0024 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/config.t` -> **Severity: 10.192** (Embedded: 0.1468 * Error Risk: 69.4453%)
- `t/options.t` -> **Severity: 5.591** (Embedded: 0.0781 * Error Risk: 71.5621%)
- `t/rework.t` -> **Severity: 1.395** (Embedded: 0.0361 * Error Risk: 38.6549%)
- `t/target.t` -> **Severity: 1.385** (Embedded: 0.0401 * Error Risk: 34.5247%)
- `t/change.t` -> **Severity: 1.199** (Embedded: 0.0614 * Error Risk: 19.5289%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/config.t` -> **Severity: 1188.966** (Blast Radius: 99.743 * Doc Risk: 11.9203%)
- `t/options.t` -> **Severity: 871.043** (Blast Radius: 54.979 * Doc Risk: 15.8432%)
- `t/command.t` -> **Severity: 756.34** (Blast Radius: 56.115 * Doc Risk: 13.4784%)
- `t/click-conf/client.pl` -> **Severity: 730.8** (Blast Radius: 7.308 * Doc Risk: 100.0%)
- `t/click-conf/multi-creds.pl` -> **Severity: 730.8** (Blast Radius: 7.308 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
