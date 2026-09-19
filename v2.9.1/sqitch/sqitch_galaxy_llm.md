# ARCHITECTURAL_BRIEF: sqitch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sqitchers/sqitch.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 139 analyzed artifact(s), 26754 LOC.
- **Load-bearing artifact:** `t/config.t` -- 15 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `t/engine.t` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `t/engine.t` at magnitude 444.26 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 364 |
| Analyzed Artifacts (Scanned) | 139 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 225 |
| Total LOC | 26754 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 38.2% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3943 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3936 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8556 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 63 | 23862 | 45.3% |
| SQLITE | 45 | 2541 | 32.4% |
| DB2_SQL | 21 | 351 | 15.1% |
| MARKDOWN | 4 | 0 | 2.9% |
| XML | 4 | 0 | 2.9% |
| PLAINTEXT | 2 | 0 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `5.528`
> **Composition Archetype:** `Small Flat Repo (2)` (z +5.53; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 42%, Data / Markup / Trivial 32%, Large Core Modules (3) 17%, Interface Declarations Files 5%, Parameter Forwarders Files 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 133 | 95.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 225*

**Composition by Extension & Reason:**
- `.pm`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 30x Excluded (Unsupported Extension: '.tmpl')
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.plan`: 14x Excluded (Unsupported Extension: '.plan'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 12x Excluded (Unsupported Extension: '.conf')
- `.sh`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.po`: 6x Excluded (Unsupported Extension: '.po')
- `.ini`: 3x Excluded (Unsupported Extension: '.ini'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.t`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mo`: 3x Excluded (Unsupported Extension: '.mo')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.spec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pot`: 1x Excluded (Unsupported Extension: '.pot')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 71.4 | 11.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.3 | 31.3 | 31.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 77.3 | 2.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 52.3 | 1.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 12.6 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 2.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.4 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 65.9 | 1.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 623 | 47 | 11 | `t/engine.t` |
| cleanup | 59 | 29 | 1 | `t/rework.t` |
| guards | 606 | 93 | 15 | `lib/App/Sqitch/Engine/Upgrade/sqlite-1.0.sql` |
| danger | 294 | 58 | 7 | `t/engine.t` |
| concurrency | 28 | 8 | 0 | `t/rebase.t` |
| connectivity | 59 | 13 | 0 | `t/engine.t` |
| io | 84 | 23 | 2 | `t/plan.t` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 2 | 0 | `t/engine.t` |
| time | 115 | 26 | 3 | `lib/App/Sqitch/Engine/sqlite.sql` |
| serialization | 0 | 0 | 0 | - |
| regex | 306 | 36 | 9 | `t/config.t` |
| events | 240 | 46 | 3 | `t/config.t` |
| tests | 1536 | 52 | 33 | `t/engine.t` |
| docs | 0 | 0 | 0 | - |
| debt | 141 | 42 | 3 | `t/engine.t` |
| mutation | 6431 | 89 | 135 | `t/engine.t` |
| dead_code | 19 | 11 | 0 | `inc/Menlo/Sqitch.pm` |
| credential | 1 | 1 | 0 | `t/clickhouse.t` |
| threat | 90 | 38 | 2 | `t/mysql.t` |
| ml_ai | 238 | 16 | 1 | `t/log.t` |
| ui | 15 | 2 | 0 | `t/add.t` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.625**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/plan.t` (Hits: 12)
- `t/change.t` (Hits: 8)
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

- `report_on` **(Compute Cores)** (@ `xt/dependency_report`) -> Impact: **43.9** | LOC: 38
- `run` **(Compute Cores)** (@ `xt/dependency_report`) -> Impact: **39.3** | LOC: 59
- `change` **(Compute Cores)** (@ `t/plan.t`) -> Impact: **18.5** | LOC: 31
- `prag` **(Compute Cores)** (@ `t/plan.t`) -> Impact: **13.7** | LOC: 14
- `new` **(Compute Cores)** (@ `inc/Menlo/Sqitch.pm`) -> Impact: **12.1** | LOC: 16
- `is_build` **(Compute Cores)** (@ `xt/dependency_report`) -> Impact: **8.9** | LOC: 9
- `tag` **(Compute Cores)** (@ `t/plan.t`) -> Impact: **6.4** | LOC: 15
- `configure` **(Type Conversions)** (@ `inc/Menlo/Sqitch.pm`) -> Impact: **6.3** | LOC: 13
- `exp_prompt` **(I/O & Config Routines)** (@ `t/change.t`) -> Impact: **5.8** | LOC: 17
- `_get` **(Compute Cores)** (@ `xt/dependency_report`) -> Impact: **5.5** | LOC: 6

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t` | 56 | 4659.28 | 23.8% | 5.01% |
| `t/lib/upgradable_registries` | 10 | 786.04 | 7.14% | 0.0% |
| `lib/App/Sqitch/Engine` | 10 | 530.48 | 0.0% | 0.0% |
| `lib/App/Sqitch/Engine/Upgrade` | 20 | 231.18 | 2.3% | 0.0% |
| `xt` | 3 | 140.12 | 18.82% | 0.0% |
| `t/click-conf` | 8 | 103.32 | 2.02% | 0.0% |
| `t/sql/deploy` | 8 | 84.16 | 0.0% | 0.0% |
| `t/sql/revert` | 7 | 73.64 | 0.0% | 0.0% |
| `inc/Menlo` | 1 | 58.94 | 9.1% | 77.28% |
| `__monolith__` | 3 | 52.28 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `inc/Menlo/Sqitch.pm` -> **77.2822%** Exposure
- `t/cx_cmd_role.t` -> **65.9467%** Exposure
- `t/item_formatter.t` -> **52.402%** Exposure
- `t/conn_cmd_role.t` -> **24.2081%** Exposure
- `t/plan_cmd.t` -> **19.8283%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/cx_cmd_role.t` -> **99.9998%** Exposure
- `t/base.t` -> **99.991%** Exposure
- `t/options.t` -> **99.9891%** Exposure
- `t/target.t` -> **99.9677%** Exposure
- `t/conn_cmd_role.t` -> **99.95%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `inc/Menlo/Sqitch.pm` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1018` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `t/engine.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 444.26 | **LOC:** 3749 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **47**; blast radius 18.849; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (78.7%), Connectivity (formerly Api Exposure) (52.3%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (17.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `current_state` **(Compute Cores)** (Impact: 3.0)
  * `begin_work` **(Compute Cores)** (Impact: 2.0)
  * `finish_work` **(Compute Cores)** (Impact: 2.0)
  * `are_deployed_changes` **(Parameter Forwarders)** (Impact: 1.5)
  * `change_id_for` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 170
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 406`, `args: 11`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 207`, `planned_debt: 1`, `fragile_debt: 11`
* *Architecture:* `io: 2`, `api: 28`, `concurrency: 2`, `import: 82`
* *Defense:* `safety: 2`, `test: 376`, `sync_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.849
  * `Choke Point (Betweenness):` 0.003729 | `Ripple Effect (Closeness):` 0.037267
  * `Imports (Out-Degree: 5):` App::Sqitch, App::Sqitch::DateTime, App::Sqitch::Plan, App::Sqitch::Target, App::Sqitch::X, Clone, ID, List::Util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/plan.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 401.12 | **LOC:** 2062 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 14.73; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (70.9%), Connectivity (formerly Api Exposure) (35.8%), Complexity Load (formerly Cognitive Load) (26.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `change` **(Compute Cores)** (Impact: 18.5)
  * `prag` **(Compute Cores)** (Impact: 13.7)
  * `tag` **(Compute Cores)** (Impact: 6.4)
  * `ts` **(Annotated & Test Methods)** (Impact: 4.9)
  * `dep` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 80 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 181`, `args: 16`, `func_start: 10`
* *Risk/State:* `state_mutation: 139`
* *Architecture:* `io: 12`, `api: 10`, `import: 31`
* *Defense:* `safety: 3`, `test: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.73
  * `Choke Point (Betweenness):` 0.001613 | `Ripple Effect (Closeness):` 0.029158
  * `Imports (Out-Degree: 3):` App::Sqitch, App::Sqitch::DateTime, App::Sqitch::Target, Encode, File::Path, Locale::TextDomain, MockOutput, Path::Class...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/lib/upgradable_registries/firebird.sql` (SQLITE | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 340.02 | **LOC:** 328 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UPDATE_Statement` **(Unclassified)** (Impact: 3.0)
  * `UPDATE_Statement` **(Unclassified)** (Impact: 3.0)
  * `UPDATE_Statement` **(Unclassified)** (Impact: 3.0)
  * `UPDATE_Statement` **(Unclassified)** (Impact: 3.0)
  * `UPDATE_Statement` **(Unclassified)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `args: 211`, `class_start: 6`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* None
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 201.82 | **LOC:** 1162 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **22**; blast radius 76.393; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (15.7%), Debt Markers (formerly Tech Debt) (14.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 112`, `args: 6`
* *Risk/State:* `state_mutation: 124`, `fragile_debt: 4`
* *Architecture:* `import: 25`
* *Defense:* `safety: 2`, `test: 106`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 76.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.103154
  * `Imports (Out-Degree: 0):` App::Sqitch, File::Path, File::Spec, Locale::TextDomain, Path::Class, Test::Exception, Test::MockModule, Test::More...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `t/target.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 182.0 | **LOC:** 735 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 11.179; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (64.6%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_load` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 75`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `api: 1`, `import: 32`
* *Defense:* `safety: 3`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.179
  * `Choke Point (Betweenness):` 0.001177 | `Ripple Effect (Closeness):` 0.028202
  * `Imports (Out-Degree: 3):` App::Sqitch, List::Util, Locale::TextDomain, Path::Class, Test::Exception, Test::More, TestConfig, config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/base.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 180.5 | **LOC:** 746 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 10.354; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.3%), Complexity Load (formerly Cognitive Load) (53.9%), Connectivity (formerly Api Exposure) (11.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `puke` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* # Now make it die.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 160`, `args: 7`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 79`
* *Architecture:* `io: 5`, `api: 1`, `import: 41`
* *Defense:* `safety: 2`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.354
  * `Choke Point (Betweenness):` 0.000688 | `Ripple Effect (Closeness):` 0.007246
  * `Imports (Out-Degree: 1):` App::Sqitch::X, Capture::Tiny, IO::Pager, Locale::TextDomain, Path::Class, String::ShellQuote, Sys::Hostname, TTY...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/rebase.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 157.98 | **LOC:** 738 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (67.4%), Complexity Load (formerly Cognitive Load) (27.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 79`, `args: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 50`
* *Architecture:* `import: 28`
* *Defense:* `safety: 2`, `test: 72`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App::Sqitch, App::Sqitch::Target, App::Sqitch::X, Locale::TextDomain, MockOutput, Path::Class, Test::Exception, Test::MockModule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/clickhouse.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 157.62 | **LOC:** 1023 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.9%), Guard Balance (formerly Safety Score) (63.5%), Complexity Load (formerly Cognitive Load) (33.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 156`, `args: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `io: 3`, `import: 36`
* *Defense:* `safety: 5`, `test: 44`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::Target, Cwd, DBD::Mem, DBD::ODBC, DBIEngineTest, False, File::Temp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/command.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 146.94 | **LOC:** 784 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 42.967; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (37.9%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `options` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 108`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 62`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 39`
* *Defense:* `safety: 2`, `test: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.967
  * `Choke Point (Betweenness):` 0.005078 | `Ripple Effect (Closeness):` 0.035982
  * `Imports (Out-Degree: 4):` App::Sqitch, App::Sqitch::Target, Capture::Tiny, File::Path, List::Util, Locale::TextDomain, MockOutput, Moo...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/add.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 140.0 | **LOC:** 1039 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.2%), Guard Balance (formerly Safety Score) (60.1%), Complexity Load (formerly Cognitive Load) (18.6%), Debt Markers (formerly Tech Debt) (11.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `contents_of` **(Annotated & Test Methods)** (Impact: 4.5)
  * `dep` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 154`, `args: 8`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `api: 2`, `import: 30`
* *Defense:* `safety: 2`, `test: 60`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` App::Sqitch, App::Sqitch::Target, File::Path, File::Temp, Locale::TextDomain, MockOutput, Path::Class, Template...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/checkout.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 137.16 | **LOC:** 706 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (64.8%), Complexity Load (formerly Cognitive Load) (24.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 66`, `args: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`
* *Architecture:* `import: 24`
* *Defense:* `safety: 2`, `test: 57`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::Target, App::Sqitch::X, Locale::TextDomain, MockOutput, Path::Class, Test::Exception, Test::MockModule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/dependency_report` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 134.2 | **LOC:** 184 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%), Complexity Load (formerly Cognitive Load) (56.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report_on` **(Compute Cores)** (Impact: 43.9)
  * `run` **(Compute Cores)** (Impact: 39.3)
  * `is_build` **(Compute Cores)** (Impact: 8.9)
  * `_get` **(Compute Cores)** (Impact: 5.5)
  * `_fetch` **(Parameter Forwarders)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 51`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 5`, `api: 4`, `import: 7`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Long, HTTP::Tiny, JSON::PP, strict, utf8, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/log.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 134.04 | **LOC:** 756 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Guard Balance (formerly Safety Score) (72.2%), Complexity Load (formerly Cognitive Load) (29.4%), Debt Markers (formerly Tech Debt) (18.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 104`, `args: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 52`, `fragile_debt: 4`
* *Architecture:* `import: 22`
* *Defense:* `safety: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App::Sqitch, Encode, LC, Locale::TextDomain, MockOutput, Path::Class, Term::ANSIColor, Test::Exception...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mysql.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 123.72 | **LOC:** 742 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Guard Balance (formerly Safety Score) (65.0%), Complexity Load (formerly Cognitive Load) (45.7%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 144`, `args: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `io: 3`, `api: 1`, `import: 35`
* *Defense:* `safety: 6`, `test: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::Target, DBD::Mem, DBIEngineTest, File::Temp, List::MoreUtils, Locale::TextDomain, MariaDB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rework.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 120.8 | **LOC:** 1089 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 9.769; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.8%), Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (19.7%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dep` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 160`, `args: 4`, `func_start: 1`
* *Risk/State:* `state_mutation: 54`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 20`
* *Defense:* `safety: 3`, `test: 41`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.769
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.025362
  * `Imports (Out-Degree: 1):` App::Sqitch, App::Sqitch::Command::add, Data::Dump, File::Path, Locale::TextDomain, MockOutput, Path::Class, Test::Exception...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/oracle.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 119.84 | **LOC:** 727 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (70.7%), Complexity Load (formerly Cognitive Load) (48.8%), Debt Markers (formerly Tech Debt) (15.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 96`, `args: 5`
* *Risk/State:* `state_mutation: 39`, `dead_code: 2`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `import: 21`
* *Defense:* `safety: 5`, `test: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::Plan, App::Sqitch::Target, Capture::Tiny, DBIEngineTest, File::Temp, Locale::TextDomain, ORACLE_HOME...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/pg.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 116.94 | **LOC:** 566 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (66.4%), Complexity Load (formerly Cognitive Load) (42.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 126`, `args: 13`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `io: 3`, `import: 30`
* *Defense:* `safety: 7`, `test: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::Plan, App::Sqitch::Target, Capture::Tiny, DBD::Mem, DBIEngineTest, Locale::TextDomain, ORDER...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/plan_cmd.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 105.24 | **LOC:** 714 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Guard Balance (formerly Safety Score) (68.3%), Complexity Load (formerly Cognitive Load) (22.6%), Debt Markers (formerly Tech Debt) (19.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 82`, `args: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 44`, `fragile_debt: 4`
* *Architecture:* `import: 22`
* *Defense:* `safety: 2`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App::Sqitch, Encode, LC, Locale::TextDomain, MockOutput, Path::Class, Term::ANSIColor, Test::Exception...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/snowflake.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 105.14 | **LOC:** 650 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Guard Balance (formerly Safety Score) (62.5%), Complexity Load (formerly Cognitive Load) (32.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 144`, `args: 7`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `io: 4`, `import: 31`
* *Defense:* `safety: 8`, `test: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::DateTime, App::Sqitch::Plan, App::Sqitch::Target, COMMENT, CREATE, Capture::Tiny, DBD::Mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/bundle.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 103.48 | **LOC:** 555 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Guard Balance (formerly Safety Score) (68.0%), Complexity Load (formerly Cognitive Load) (23.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 61`, `args: 2`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `import: 18`
* *Defense:* `safety: 2`, `test: 19`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, File::Path, Locale::TextDomain, MockOutput, Path::Class, Test::Exception, Test::File, Test::File::Contents...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/status.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 97.32 | **LOC:** 618 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (23.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 86`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`
* *Architecture:* `import: 21`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` App::Sqitch, Locale::TextDomain, MockOutput, Path::Class, Test::Exception, Test::MockModule, Test::More, Test::NoWarnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/target_cmd.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 91.52 | **LOC:** 794 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (79.0%), Guard Balance (formerly Safety Score) (57.3%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 84`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `import: 26`
* *Defense:* `safety: 2`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, Data::Dump, File::Copy, File::Temp, List::Util, Locale::TextDomain, MockOutput, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/engine_cmd.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 87.26 | **LOC:** 611 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Guard Balance (formerly Safety Score) (61.1%), Complexity Load (formerly Cognitive Load) (21.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 69`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `import: 23`
* *Defense:* `safety: 3`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, File::Copy, File::Temp, List::Util, Locale::TextDomain, MockOutput, Path::Class, Test::Dir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/pg.sql` (SQLITE | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 81.4 | **LOC:** 146 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CREATE_Statement` **(Unclassified)** (Impact: 3.2)
  * `CREATE_Statement` **(Unclassified)** (Impact: 2.1)
  * `CREATE_Statement` **(Unclassified)** (Impact: 2.1)
  * `CREATE_Statement` **(Unclassified)** (Impact: 1.9)
  * `CREATE_Statement` **(Unclassified)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 7`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/vertica.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 80.36 | **LOC:** 402 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (64.2%), Complexity Load (formerly Cognitive Load) (45.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 18 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 75`, `args: 7`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `io: 1`, `import: 21`
* *Defense:* `safety: 7`, `test: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App::Sqitch, App::Sqitch::Plan, App::Sqitch::Target, Capture::Tiny, DBIEngineTest, Locale::TextDomain, Test::Exception, Test::MockModule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/clickhouse.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 157.62
- `t/firebird.t` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 79.06
- `inc/Menlo/Sqitch.pm` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 58.94

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/command.t` -> **Severity: 0.507** (Bridge: 0.0051 * Flux: 99.7579%)
- `t/options.t` -> **Severity: 0.45** (Bridge: 0.0045 * Flux: 99.9891%)
- `t/engine.t` -> **Severity: 0.293** (Bridge: 0.0037 * Flux: 78.6646%)
- `t/plan.t` -> **Severity: 0.159** (Bridge: 0.0016 * Flux: 98.7058%)
- `t/target.t` -> **Severity: 0.118** (Bridge: 0.0012 * Flux: 99.9677%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/config.t` -> **Severity: 6.175** (Embedded: 0.1032 * Error Risk: 59.8588%)
- `t/options.t` -> **Severity: 3.92** (Embedded: 0.0549 * Error Risk: 71.3758%)
- `t/command.t` -> **Severity: 2.537** (Embedded: 0.036 * Error Risk: 70.5103%)
- `t/change.t` -> **Severity: 2.414** (Embedded: 0.0431 * Error Risk: 55.9566%)
- `t/target.t` -> **Severity: 2.154** (Embedded: 0.0282 * Error Risk: 76.3638%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/command.t` -> **Severity: 4296.7** (Blast Radius: 42.967 * Doc Risk: 100.0%)
- `t/change.t` -> **Severity: 2343.8** (Blast Radius: 23.438 * Doc Risk: 100.0%)
- `t/engine.t` -> **Severity: 1884.9** (Blast Radius: 18.849 * Doc Risk: 100.0%)
- `t/plan.t` -> **Severity: 1473.0** (Blast Radius: 14.73 * Doc Risk: 100.0%)
- `t/target.t` -> **Severity: 1117.9** (Blast Radius: 11.179 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
