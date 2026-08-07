# ARCHITECTURAL_BRIEF: sqitch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/sqitch` |
| **Timestamp** | `2026-08-07T03:52:33.222132+00:00` |
| **Scan Duration** | `0.73s` |
| **Git Branch** | `develop` |
| **Git Commit** | `0ab857e3bb5060e6feda0dd3e05ebb04f7aac85b` |
| **Git Remote** | `https://github.com/sqitchers/sqitch.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 26 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.039`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 43 | 43.9% |
| file_cluster_0 | 39 | 39.8% |
| file_cluster_13 | 8 | 8.2% |
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
| Cognitive Load Exposure | 0.0 | 90.0 | 29.9 | 18.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.0 | 52.8 | 68.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 0.2 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 17.7 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 55.8 | 95.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 68.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.6 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 95.3 | 3.3 | 0.0 | 0.0 |
| Documentation Exposure | 1.2 | 95.6 | 20.3 | 14.5 | 6.2 |
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

- `mock_check_deploy` (@ `t/engine.t`) -> Impact: **174.8** | LOC: 1431
- `mock_check_revert` (@ `t/engine.t`) -> Impact: **174.8** | LOC: 1432
- `mock_lock` (@ `t/engine.t`) -> Impact: **174.8** | LOC: 1431
- `load_change` (@ `t/engine.t`) -> Impact: **174.7** | LOC: 1429
- `deployed_changes_since` (@ `t/engine.t`) -> Impact: **174.7** | LOC: 1429
- `deployed_changes` (@ `t/engine.t`) -> Impact: **174.6** | LOC: 1428
- `changes_requiring_change` (@ `t/engine.t`) -> Impact: **174.5** | LOC: 1425
- `earliest_change_id` (@ `t/engine.t`) -> Impact: **174.5** | LOC: 1425
- `latest_change_id` (@ `t/engine.t`) -> Impact: **174.5** | LOC: 1426
- `current_state` (@ `t/engine.t`) -> Impact: **174.5** | LOC: 1425

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 55 | 16950.16 | 43.02% | 5.82% |
| `xt` | 3 | 160.12 | 29.31% | 0.0% |
| `t/click-conf` | 8 | 103.32 | 7.61% | 0.0% |
| `t/sql/deploy` | 8 | 84.16 | 5.0% | 0.0% |
| `inc/Menlo` | 1 | 78.74 | 17.94% | 36.04% |
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
- `t/blank.t` -> **100.0%** Exposure
- `t/cockroach.t` -> **100.0%** Exposure
- `t/cx_cmd_role.t` -> **100.0%** Exposure
- `t/firebird.t` -> **100.0%** Exposure
- `t/mooseless.t` -> **100.0%** Exposure
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `990` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/clickhouse.t` (PERL) -> Cumulative Risk: **477.77**
- **Archetype:** `file_cluster_0` (Distance: 12.198 IQR)
- **Magnitude:** 371.6 | **LOC:** 1023 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Churn (95.34%), Safety Score (82.621%)

### 2. `xt/dependency_report` (PERL) -> Cumulative Risk: **464.79**
- **Archetype:** `file_cluster_0` (Distance: 12.499 IQR)
- **Magnitude:** 154.2 | **LOC:** 184 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (87.9233%), Safety Score (84.9454%)
- **Heaviest Functions:** `report_on` (Impact: 43.9), `run` (Impact: 31.3), `is_build` (Impact: 8.9)

### 3. `t/cx_cmd_role.t` (PERL) -> Cumulative Risk: **454.25**
- **Archetype:** `file_cluster_13` (Distance: 11.568 IQR)
- **Magnitude:** 47.04 | **LOC:** 110 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (86.6144%), Tech Debt (77.4803%)
- **Heaviest Functions:** `options` (Impact: 1.3)

### 4. `etc/tools/upgrade-registry-to-mysql-5.5.0.sql` (SQLITE) -> Cumulative Risk: **441.39**
- **Archetype:** `file_cluster_8` (Distance: 12.461 IQR)
- **Magnitude:** 0.03 | **LOC:** 31 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Safety Score (96.312%), Cognitive Load (90.025%)
- **Heaviest Functions:** `Declarative_Block` (Impact: 2.4), `Declarative_Block` (Impact: 2.4), `Declarative_Block` (Impact: 2.0)

### 5. `t/mooseless.t` (PERL) -> Cumulative Risk: **436.05**
- **Archetype:** `file_cluster_13` (Distance: 13.37 IQR)
- **Magnitude:** 36.46 | **LOC:** 32 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.9197%), Cognitive Load (85.0577%)

### 6. `t/oracle.t` (PERL) -> Cumulative Risk: **417.78**
- **Archetype:** `file_cluster_0` (Distance: 11.756 IQR)
- **Magnitude:** 219.82 | **LOC:** 727 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (83.5086%), Cognitive Load (80.8757%)

### 7. `t/firebird.t` (PERL) -> Cumulative Risk: **409.88**
- **Archetype:** `file_cluster_0` (Distance: 11.968 IQR)
- **Magnitude:** 198.06 | **LOC:** 516 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.6849%), Cognitive Load (83.8572%)

### 8. `t/vertica.t` (PERL) -> Cumulative Risk: **400.79**
- **Archetype:** `file_cluster_0` (Distance: 12.121 IQR)
- **Magnitude:** 182.36 | **LOC:** 402 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.389%), Cognitive Load (80.9466%)

### 9. `t/sqlite.t` (PERL) -> Cumulative Risk: **397.82**
- **Archetype:** `file_cluster_0` (Distance: 11.686 IQR)
- **Magnitude:** 149.66 | **LOC:** 411 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Safety Score (83.0029%), Cognitive Load (82.1351%)

### 10. `t/mysql.t` (PERL) -> Cumulative Risk: **396.79**
- **Archetype:** `file_cluster_0` (Distance: 12.518 IQR)
- **Magnitude:** 6480.36 | **LOC:** 742 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (88.6605%), Cognitive Load (77.0531%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/mysql.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.518 IQR)
- **Top Global Matches:** file_cluster_0: 12.518, file_cluster_13: 12.703, file_cluster_8: 12.761
- **Magnitude:** 6480.36 | **LOC:** 742 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.0531%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 143`, `args: 17`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 313`
* *Architecture:* `io: 3`, `import: 35`
* *Defense:* `safety: 6`, `test: 37`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, database, limit, Locale::TextDomain, App::Sqitch::Target, File::Temp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/engine.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.664 IQR)
- **Top Global Matches:** file_cluster_8: 11.664, file_cluster_0: 11.77, file_cluster_13: 11.95
- **Magnitude:** 3889.74 | **LOC:** 3749 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.8562%), Tech Debt (12.5031%)
**Top Internal Functions/Classes:**
  * `mock_check_deploy` (Impact: 174.8)
  * `mock_check_revert` (Impact: 174.8)
  * `mock_lock` (Impact: 174.8)
  * `load_change` (Impact: 174.7)
  * `deployed_changes_since` (Impact: 174.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 404`, `args: 15`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 501`, `planned_debt: 1`, `fragile_debt: 11`
* *Architecture:* `io: 3`, `concurrency: 7`, `import: 82`
* *Defense:* `safety: 2`, `test: 376`, `sync_locks: 3`, `cleanup: 180`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.609
  * `Choke Point (Betweenness):` 0.007571 | `Ripple Effect (Closeness):` 0.053019
  * `Imports (Out-Degree: 5):` Test::More, App::Sqitch::DateTime, deploy, strict, variables, warnings, script, Locale::TextDomain...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/plan.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.953 IQR)
- **Top Global Matches:** file_cluster_0: 11.953, file_cluster_8: 12.091, file_cluster_13: 12.391
- **Magnitude:** 561.54 | **LOC:** 2062 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.7711%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `change` (Impact: 22.3)
  * `prag` (Impact: 13.7)
  * `tag` (Impact: 7.7)
  * `ts` (Impact: 5.8)
  * `dep` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 181`, `args: 13`, `func_start: 10`
* *Risk/State:* `state_mutation: 462`
* *Architecture:* `io: 14`, `import: 31`
* *Defense:* `safety: 3`, `test: 32`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.231
  * `Choke Point (Betweenness):` 0.003275 | `Ripple Effect (Closeness):` 0.041483
  * `Imports (Out-Degree: 3):` Test::More, App::Sqitch::DateTime, strict, Test::File, warnings, the, project, Locale::TextDomain...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/clickhouse.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.198 IQR)
- **Top Global Matches:** file_cluster_0: 12.198, file_cluster_8: 12.512, file_cluster_13: 12.527
- **Magnitude:** 371.6 | **LOC:** 1023 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.9511%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 156`, `args: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 339`, `dead_code: 2`
* *Architecture:* `io: 3`, `import: 36`
* *Defense:* `safety: 5`, `test: 44`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, False, warnings, database, limit, Locale::TextDomain, _limit_default...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/add.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.968 IQR)
- **Top Global Matches:** file_cluster_0: 11.968, file_cluster_8: 12.108, file_cluster_13: 12.166
- **Magnitude:** 345.56 | **LOC:** 1039 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.402%), Tech Debt (11.9018%)
**Top Internal Functions/Classes:**
  * `contents_of` (Impact: 6.3)
  * `dep` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 152`, `args: 9`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 320`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `import: 29`
* *Defense:* `safety: 2`, `test: 60`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Test::More, strict, Test::File, warnings, the, Test::Dir, Locale::TextDomain, change...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rework.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.838 IQR)
- **Top Global Matches:** file_cluster_8: 11.838, file_cluster_0: 11.893, file_cluster_17: 12.11
- **Magnitude:** 336.04 | **LOC:** 1089 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.7614%), Tech Debt (10.0498%)
**Top Internal Functions/Classes:**
  * `dep` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 160`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 316`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `import: 20`
* *Defense:* `safety: 3`, `test: 41`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.758
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.036082
  * `Imports (Out-Degree: 1):` Test::More, strict, Test::File, warnings, the, Locale::TextDomain, utf8, Path::Class...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/snowflake.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.1 IQR)
- **Top Global Matches:** file_cluster_0: 12.1, file_cluster_13: 12.351, file_cluster_8: 12.438
- **Magnitude:** 265.14 | **LOC:** 650 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.9631%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 140`, `args: 7`
* *Risk/State:* `state_mutation: 240`
* *Architecture:* `io: 6`, `import: 31`
* *Defense:* `safety: 8`, `test: 25`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, schema, App::Sqitch::DateTime, strict, warnings, limit, Locale::TextDomain, COMMENT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/pg.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.403 IQR)
- **Top Global Matches:** file_cluster_0: 12.403, file_cluster_13: 12.587, file_cluster_8: 12.722
- **Magnitude:** 257.94 | **LOC:** 566 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.703%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 126`, `args: 14`
* *Risk/State:* `state_mutation: 234`
* *Architecture:* `io: 3`, `import: 30`
* *Defense:* `safety: 7`, `test: 32`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, XC, the, Locale::TextDomain, App::Sqitch::Target, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/target.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.813 IQR)
- **Top Global Matches:** file_cluster_0: 11.813, file_cluster_8: 12.187, file_cluster_13: 12.223
- **Magnitude:** 241.8 | **LOC:** 735 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_load` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 75`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 226`
* *Architecture:* `api: 1`, `import: 32`
* *Defense:* `safety: 3`, `test: 38`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.599
  * `Choke Point (Betweenness):` 0.002389 | `Ripple Effect (Closeness):` 0.040123
  * `Imports (Out-Degree: 3):` Test::More, params, strict, variables, warnings, Locale::TextDomain, utf8, name...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/log.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.773 IQR)
- **Top Global Matches:** file_cluster_8: 11.773, file_cluster_0: 11.798, file_cluster_13: 11.992
- **Magnitude:** 233.04 | **LOC:** 756 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.452%), Tech Debt (19.9721%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 104`, `args: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 205`, `fragile_debt: 4`
* *Architecture:* `import: 22`
* *Defense:* `safety: 2`, `test: 17`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, LC, strict, warnings, Locale::TextDomain, utf8, Path::Class, Test::Warn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.823 IQR)
- **Top Global Matches:** file_cluster_0: 11.823, file_cluster_13: 11.978, file_cluster_8: 12.088
- **Magnitude:** 232.5 | **LOC:** 746 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0383%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `puke` (Impact: 1.1)
    * *Intent:* # Now make it die.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 159`, `args: 7`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 220`
* *Architecture:* `io: 5`, `import: 40`
* *Defense:* `safety: 2`, `test: 28`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.521
  * `Choke Point (Betweenness):` 0.001396 | `Ripple Effect (Closeness):` 0.010309
  * `Imports (Out-Degree: 1):` Test::More, default, Sys::Hostname, strict, warnings, Locale::TextDomain, TTY, prompt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.384 IQR)
- **Top Global Matches:** file_cluster_0: 11.384, file_cluster_8: 11.446, file_cluster_13: 11.674
- **Magnitude:** 221.82 | **LOC:** 1162 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.1036%), Tech Debt (15.0646%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 108`, `args: 6`
* *Risk/State:* `high_risk_execution: 47`, `state_mutation: 188`, `fragile_debt: 4`
* *Architecture:* `import: 25`
* *Defense:* `safety: 2`, `test: 106`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 99.743
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.146756
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, Locale::TextDomain, File::Spec, name, Path::Class, new...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `t/oracle.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.756 IQR)
- **Top Global Matches:** file_cluster_0: 11.756, file_cluster_13: 12.236, file_cluster_8: 12.327
- **Magnitude:** 219.82 | **LOC:** 727 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.8757%), Tech Debt (16.3226%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 96`, `args: 7`
* *Risk/State:* `state_mutation: 195`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `import: 21`
* *Defense:* `safety: 5`, `test: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, as, strict, warnings, the, Locale::TextDomain, App::Sqitch::Target, File::Temp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/firebird.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.968 IQR)
- **Top Global Matches:** file_cluster_0: 11.968, file_cluster_13: 12.283, file_cluster_8: 12.459
- **Magnitude:** 198.06 | **LOC:** 516 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.8572%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 106`, `args: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 175`
* *Architecture:* `io: 5`, `import: 30`
* *Defense:* `safety: 7`, `test: 17`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, db, File::Spec::Functions, Locale::TextDomain, useful, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/command.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.556 IQR)
- **Top Global Matches:** file_cluster_0: 11.556, file_cluster_13: 11.853, file_cluster_8: 11.862
- **Magnitude:** 185.94 | **LOC:** 784 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.917%), Tech Debt (10.5161%)
**Top Internal Functions/Classes:**
  * `options` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 106`, `args: 2`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 172`, `planned_debt: 2`
* *Architecture:* `import: 39`
* *Defense:* `safety: 2`, `test: 48`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.115
  * `Choke Point (Betweenness):` 0.010309 | `Ripple Effect (Closeness):` 0.051191
  * `Imports (Out-Degree: 4):` Test::More, strict, warnings, Test::Dir, class, Locale::TextDomain, Moo, utf8...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/vertica.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.121 IQR)
- **Top Global Matches:** file_cluster_0: 12.121, file_cluster_13: 12.37, file_cluster_8: 12.487
- **Magnitude:** 182.36 | **LOC:** 402 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.9466%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 75`, `args: 7`
* *Risk/State:* `state_mutation: 161`
* *Architecture:* `io: 1`, `import: 21`
* *Defense:* `safety: 7`, `test: 18`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, App::Sqitch::Target, pw, strict, listagg, warnings, lib, Try::Tiny...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/plan_cmd.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.076 IQR)
- **Top Global Matches:** file_cluster_8: 11.076, file_cluster_0: 11.206, file_cluster_13: 11.336
- **Magnitude:** 180.24 | **LOC:** 714 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0682%), Tech Debt (21.1591%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 82`, `args: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 153`, `fragile_debt: 4`
* *Architecture:* `import: 22`
* *Defense:* `safety: 2`, `test: 15`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, LC, strict, warnings, Locale::TextDomain, utf8, Path::Class, Test::Warn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rebase.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.19 IQR)
- **Top Global Matches:** file_cluster_0: 11.19, file_cluster_8: 11.25, file_cluster_13: 11.405
- **Magnitude:** 174.9 | **LOC:** 738 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.061%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 79`, `args: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 147`
* *Architecture:* `import: 28`
* *Defense:* `safety: 2`, `test: 72`, `sync_locks: 8`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, App::Sqitch::Target, be, Path::Class, MockOutput, strict, variables, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/dependency_report` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.499 IQR)
- **Top Global Matches:** file_cluster_0: 12.499, file_cluster_13: 12.71, file_cluster_17: 12.824
- **Magnitude:** 154.2 | **LOC:** 184 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.9233%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `report_on` (Impact: 43.9)
  * `run` (Impact: 31.3)
  * `is_build` (Impact: 8.9)
  * `_get` (Impact: 5.5)
  * `_fetch` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 51`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `io: 6`, `import: 7`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, strict, warnings, JSON::PP, v5, HTTP::Tiny, utf8
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/bundle.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.005 IQR)
- **Top Global Matches:** file_cluster_8: 11.005, file_cluster_0: 11.016, file_cluster_13: 11.234
- **Magnitude:** 151.48 | **LOC:** 555 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3599%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 61`, `args: 2`
* *Risk/State:* `state_mutation: 127`
* *Architecture:* `import: 18`
* *Defense:* `safety: 2`, `test: 19`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, Path::Class, MockOutput, debugging, strict, Test::File, warnings, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/sqlite.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.686 IQR)
- **Top Global Matches:** file_cluster_0: 11.686, file_cluster_13: 11.864, file_cluster_8: 11.941
- **Magnitude:** 149.66 | **LOC:** 411 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.1351%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 61`, `args: 6`
* *Risk/State:* `state_mutation: 128`
* *Architecture:* `io: 1`, `import: 25`
* *Defense:* `safety: 3`, `test: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, database, Locale::TextDomain, App::Sqitch::Target, File::Temp, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/init.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.802 IQR)
- **Top Global Matches:** file_cluster_0: 10.802, file_cluster_8: 10.884, file_cluster_13: 11.128
- **Magnitude:** 144.86 | **LOC:** 682 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.6296%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 73`, `args: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 119`
* *Architecture:* `io: 3`, `import: 19`
* *Defense:* `safety: 2`, `test: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Test::More, strict, Test::File, warnings, variables, Test::Dir, Locale::TextDomain, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/options.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.186 IQR)
- **Top Global Matches:** file_cluster_13: 12.186, file_cluster_0: 12.251, file_cluster_8: 12.495
- **Magnitude:** 129.54 | **LOC:** 229 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.2867%), Tech Debt (18.0746%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 51`, `args: 3`
* *Risk/State:* `state_mutation: 111`, `planned_debt: 1`
* *Architecture:* `import: 20`
* *Defense:* `safety: 2`, `test: 23`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 54.979
  * `Choke Point (Betweenness):` 0.009128 | `Ripple Effect (Closeness):` 0.078133
  * `Imports (Out-Degree: 1):` Test::More, strict, Test::Exit, warnings, opts, lib, args, Test::MockModule...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `t/exasol.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.349 IQR)
- **Top Global Matches:** file_cluster_0: 11.349, file_cluster_8: 11.579, file_cluster_13: 11.593
- **Magnitude:** 128.5 | **LOC:** 470 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.2123%), Tech Debt (14.5957%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 73`, `args: 8`
* *Risk/State:* `state_mutation: 106`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `import: 23`
* *Defense:* `safety: 4`, `test: 23`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, limit, Locale::TextDomain, App::Sqitch::Target, regexp_like, args...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/target_cmd.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.443 IQR)
- **Top Global Matches:** file_cluster_8: 10.443, file_cluster_0: 10.456, file_cluster_13: 10.767
- **Magnitude:** 117.48 | **LOC:** 794 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.2829%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 82`
* *Risk/State:* `state_mutation: 89`
* *Architecture:* `import: 26`
* *Defense:* `safety: 2`, `test: 31`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, Test::File, warnings, variables, Test::Dir, Locale::TextDomain, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/status.t` (PERL) | Magnitude: 106.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 282, branch: 90, structural_boundaries: 86, decorators: 85
- `t/change.t` (PERL) | Magnitude: 90.4 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 194, state_mutation: 77, structural_boundaries: 54, decorators: 49
- `t/pragma.t` (PERL) | Magnitude: 23.08 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, decorators: 18, structural_boundaries: 17, import: 10
- `t/rebase.t` (PERL) | Magnitude: 174.9 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 409, state_mutation: 147, decorators: 99, structural_boundaries: 79
- `t/engine_cmd.t` (PERL) | Magnitude: 104.24 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 333, decorators: 95, branch: 92, state_mutation: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/conn_cmd_role.t` (PERL) | Magnitude: 32.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 29, structural_boundaries: 24, decorators: 14
- `t/cx_cmd_role.t` (PERL) | Magnitude: 47.04 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 44, indent_spaces: 37, structural_boundaries: 27, decorators: 19
- `t/options.t` (PERL) | Magnitude: 129.54 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 111, structural_boundaries: 51, decorators: 26
- `t/mooseless.t` (PERL) | Magnitude: 36.46 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 21, structural_boundaries: 12, indent_spaces: 8, regex_execution: 7
- `t/datetime.t` (PERL) | Magnitude: 42.7 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 32, state_mutation: 26, encapsulation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/bundle.t` (PERL) | Magnitude: 151.48 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, state_mutation: 127, decorators: 63, structural_boundaries: 61
- `t/target_cmd.t` (PERL) | Magnitude: 117.48 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 435, decorators: 120, branch: 112, state_mutation: 89
- `t/log.t` (PERL) | Magnitude: 233.04 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 439, state_mutation: 205, structural_boundaries: 104, branch: 90
- `t/rework.t` (PERL) | Magnitude: 336.04 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 737, state_mutation: 316, structural_boundaries: 160, encapsulation: 132
- `t/engine.t` (PERL) | Magnitude: 3889.74 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1966, state_mutation: 501, structural_boundaries: 404, test: 376

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `t/sql/deploy/users.sql` (SQLITE) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `t/sql/deploy/widgets.sql` (SQLITE) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `t/clickhouse.t` -> Churn: **95.34%** | Cog Load: 75.9511% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/mysql.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 6480.36
- `t/clickhouse.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 371.6
- `t/snowflake.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 265.14
- `t/pg.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 257.94
- `t/oracle.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 219.82

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/command.t` -> **Severity: 1.031** (Bridge: 0.0103 * Flux: 99.986%)
- `t/options.t` -> **Severity: 0.913** (Bridge: 0.0091 * Flux: 100.0%)
- `t/engine.t` -> **Severity: 0.743** (Bridge: 0.0076 * Flux: 98.1791%)
- `t/plan.t` -> **Severity: 0.327** (Bridge: 0.0033 * Flux: 99.9759%)
- `t/target.t` -> **Severity: 0.239** (Bridge: 0.0024 * Flux: 99.9994%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/config.t` -> **Severity: 13.309** (Embedded: 0.1468 * Error Risk: 90.6849%)
- `t/options.t` -> **Severity: 7.082** (Embedded: 0.0781 * Error Risk: 90.6409%)
- `t/change.t` -> **Severity: 4.245** (Embedded: 0.0614 * Error Risk: 69.163%)
- `t/command.t` -> **Severity: 3.774** (Embedded: 0.0512 * Error Risk: 73.7332%)
- `t/target.t` -> **Severity: 3.199** (Embedded: 0.0401 * Error Risk: 79.7233%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/config.t` -> **Severity: 1188.966** (Blast Radius: 99.743 * Doc Risk: 11.9203%)
- `t/options.t` -> **Severity: 846.759** (Blast Radius: 54.979 * Doc Risk: 15.4015%)
- `t/click-conf/client.pl` -> **Severity: 698.719** (Blast Radius: 7.308 * Doc Risk: 95.6102%)
- `t/engine.t` -> **Severity: 695.155** (Blast Radius: 24.609 * Doc Risk: 28.248%)
- `t/command.t` -> **Severity: 668.908** (Blast Radius: 56.115 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
