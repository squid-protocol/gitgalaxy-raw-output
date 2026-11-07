# ARCHITECTURAL_BRIEF: sqitch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sqitchers/sqitch.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 285 analyzed artifact(s), 63178 LOC.
- **Load-bearing artifact:** `lib/App/Sqitch/X.pm` -- 49 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `t/engine.t` -- pulls in 43 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/App/Sqitch/Plan.pm` at magnitude 1030.66 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 285 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 79 |
| Total LOC | 63178 |
| Volatility Index | 0.018 |
| % Scanned of codebase = | 78.3% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4098 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.307 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4087 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 183 | 59337 | 64.2% |
| POSTGRESQL | 40 | 2802 | 14.0% |
| SQLITE | 25 | 55 | 8.8% |
| YAML | 16 | 755 | 5.6% |
| SHELL | 10 | 194 | 3.5% |
| MARKDOWN | 4 | 0 | 1.4% |
| XML | 4 | 0 | 1.4% |
| PLAINTEXT | 2 | 0 | 0.7% |
| DB2_SQL | 1 | 35 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 285 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 47%, Data / Markup / Trivial 23%, Large Core Modules (3) 18%, Parameter Forwarders Files 5%, Compute Cores Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 279 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 79*

**Composition by Extension & Reason:**
- `.tmpl`: 30x Excluded (Unsupported Extension: '.tmpl')
- `.plan`: 15x Excluded (Unsupported Extension: '.plan')
- `.conf`: 12x Excluded (Unsupported Extension: '.conf')
- `.po`: 6x Excluded (Unsupported Extension: '.po')
- `.ini`: 4x Excluded (Unsupported Extension: '.ini')
- `.mo`: 3x Excluded (Unsupported Extension: '.mo')
- `.t`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.spec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pm`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pot`: 1x Excluded (Unsupported Extension: '.pot')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.1 | 16.5 | 10.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.7 | 38.9 | 51.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 86.5 | 4.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.0 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 66.5 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 14.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 29.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1000 | 85 | 9 | `t/engine.t` |
| cleanup | 72 | 40 | 1 | `t/rework.t` |
| guards | 2066 | 175 | 15 | `lib/App/Sqitch/Engine/firebird.sql` |
| danger | 555 | 114 | 6 | `t/engine.t` |
| concurrency | 116 | 41 | 1 | `t/lib/DBIEngineTest.pm` |
| connectivity | 625 | 83 | 7 | `lib/App/Sqitch/Engine.pm` |
| io | 502 | 96 | 5 | `lib/sqitch-environment.pod` |
| crypto | 0 | 0 | 0 | - |
| ipc | 52 | 21 | 0 | `lib/sqitch-configuration.pod` |
| time | 198 | 62 | 3 | `lib/App/Sqitch/Engine.pm` |
| serialization | 0 | 0 | 0 | - |
| regex | 693 | 101 | 9 | `lib/App/Sqitch/Plan.pm` |
| events | 469 | 76 | 4 | `t/config.t` |
| tests | 1688 | 68 | 18 | `t/engine.t` |
| docs | 148 | 130 | 1 | `.github/workflows/os.yml` |
| debt | 276 | 98 | 3 | `lib/App/Sqitch.pm` |
| mutation | 11351 | 224 | 103 | `t/engine.t` |
| dead_code | 304 | 41 | 1 | `lib/App/Sqitch/Engine/exasol.pm` |
| credential | 6 | 5 | 0 | `.github/ubuntu/clickhouse.sh` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 394 | 58 | 3 | `t/log.t` |
| ui | 72 | 11 | 0 | `lib/sqitch-add.pod` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/sqitch-environment.pod` (Hits: 77)
- `.github/ubuntu/sqlite.sh` (Hits: 25)
- `lib/App/Sqitch.pm` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **X.pm** (`lib/App/Sqitch/X.pm`) — 49 inbound connections
2. **TestConfig.pm** (`t/lib/TestConfig.pm`) — 48 inbound connections
3. **Sqitch.pm** (`lib/App/Sqitch.pm`) — 46 inbound connections
4. **Types.pm** (`lib/App/Sqitch/Types.pm`) — 33 inbound connections
5. **Target.pm** (`lib/App/Sqitch/Target.pm`) — 32 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **engine.t** (`t/engine.t`) — 43 outbound dependencies
2. **Sqitch.pm** (`lib/App/Sqitch.pm`) — 34 outbound dependencies
3. **clickhouse.t** (`t/clickhouse.t`) — 31 outbound dependencies
4. **command.t** (`t/command.t`) — 31 outbound dependencies
5. **base.t** (`t/base.t`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run` **(Many-Argument Workhorses)** (@ `t/lib/DBIEngineTest.pm`) -> Impact: **469.8** | LOC: 1830
- `_parse` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Plan.pm`) -> Impact: **432.2** | LOC: 325
- `check_changes` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Plan.pm`) -> Impact: **71.2** | LOC: 103
- `revert` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Engine.pm`) -> Impact: **64.5** | LOC: 128
- `parse_args` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Command.pm`) -> Impact: **61.9** | LOC: 95
- `execute` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Command/show.pm`) -> Impact: **59.6** | LOC: 73
- `log_deploy_change` **(Compute Cores)** (@ `lib/App/Sqitch/Engine/firebird.pm`) -> Impact: **58.5** | LOC: 97
- `BUILDARGS` **(Compute Cores)** (@ `lib/App/Sqitch/Target.pm`) -> Impact: **57.1** | LOC: 102
- `search_events` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Engine/firebird.pm`) -> Impact: **52.8** | LOC: 121
- `deploy` **(Many-Argument Workhorses)** (@ `lib/App/Sqitch/Engine.pm`) -> Impact: **52.4** | LOC: 87

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t` | 56 | 4659.28 | 23.8% | 4.02% |
| `lib/App/Sqitch/Engine` | 20 | 3441.54 | 18.77% | 48.92% |
| `lib` | 58 | 3130.48 | 24.43% | 0.88% |
| `lib/App/Sqitch` | 9 | 2616.74 | 29.49% | 4.83% |
| `lib/App/Sqitch/Command` | 20 | 1930.26 | 19.44% | 12.11% |
| `lib/App/Sqitch/Role` | 5 | 976.84 | 30.04% | 20.7% |
| `t/lib` | 4 | 771.84 | 26.55% | 0.0% |
| `t/lib/upgradable_registries` | 10 | 736.74 | 9.6% | 0.0% |
| `lib/App/Sqitch/Plan` | 8 | 626.4 | 20.4% | 13.0% |
| `lib/App` | 1 | 357.28 | 29.39% | 11.23% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/App/Sqitch/Engine/cockroach.pm` -> **99.9874%** Exposure
- `lib/App/Sqitch/Engine/snowflake.pm` -> **99.8388%** Exposure
- `lib/App/Sqitch/Engine/sqlite.pm` -> **99.7725%** Exposure
- `lib/App/Sqitch/Engine/oracle.pm` -> **99.3157%** Exposure
- `lib/App/Sqitch/Engine/pg.pm` -> **99.0137%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/sqitch-log-usage.pod` -> **100.0%** Exposure
- `t/cx_cmd_role.t` -> **99.9998%** Exposure
- `lib/sqitch-configuration.pod` -> **99.9992%** Exposure
- `lib/sqitch-plan-usage.pod` -> **99.997%** Exposure
- `lib/sqitch-init.pod` -> **99.9918%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/App/Sqitch/Engine/oracle.pm` -> **32** Orphaned Functions | **0** Duplicates
- `lib/App/Sqitch/Engine/exasol.pm` -> **31** Orphaned Functions | **0** Duplicates
- `lib/App/Sqitch/Engine/pg.pm` -> **30** Orphaned Functions | **0** Duplicates
- `lib/App/Sqitch/Engine/vertica.pm` -> **30** Orphaned Functions | **0** Duplicates
- `lib/App/Sqitch/Engine/firebird.pm` -> **26** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1658` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/App/Sqitch/Plan.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.359)
- **Top Global Matches:** file_cluster_4: 7.359, file_cluster_6: 8.722, file_cluster_15: 13.748
- **Magnitude:** 1030.66 | **LOC:** 1631 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **20**; blast radius 13.861; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(Many-Argument Workhorses)** (Impact: 432.2)
  * `check_changes` **(Many-Argument Workhorses)** (Impact: 71.2)
  * `search_changes` **(Compute Cores)** (Impact: 51.5)
  * `write_to` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `_is_valid` **(Compute Cores)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 492`, `structural_boundaries: 320`, `args: 47`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`, `fragile_debt: 3`
* *Architecture:* `io: 10`, `api: 29`, `import: 28`
* *Defense:* `safety: 11`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.861
  * `Choke Point (Betweenness):` 0.006335 | `Ripple Effect (Closeness):` 0.112902
  * `Imports (Out-Degree: 10):` App::Sqitch::DateTime, App::Sqitch::Plan::Blank, App::Sqitch::Plan::Change, App::Sqitch::Plan::ChangeList, App::Sqitch::Plan::Depend, App::Sqitch::Plan::LineList, App::Sqitch::Plan::Pragma, App::Sqitch::Plan::Tag...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `lib/App/Sqitch/Engine.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.133)
- **Top Global Matches:** file_cluster_4: 7.133, file_cluster_15: 7.659, file_cluster_11: 9.426
- **Magnitude:** 883.96 | **LOC:** 2795 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 7.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (59.2%), Guard Balance (formerly Safety Score) (51.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `revert` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `deploy` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `_verify_changes` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `check_deploy_dependencies` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `_load_changes` **(Compute Cores)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 597`, `args: 65`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 46`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 69`, `import: 37`
* *Defense:* `safety: 47`, `doc: 1`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.072387
  * `Imports (Out-Degree: 2):` Algorithm::Backoff::Exponential, App::Sqitch::Types, App::Sqitch::X, List::MoreUtils, List::Util, Locale::TextDomain, Moo, Path::Class...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/lib/DBIEngineTest.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.088)
- **Top Global Matches:** file_cluster_4: 7.088, file_cluster_15: 9.511, file_cluster_11: 10.544
- **Magnitude:** 661.96 | **LOC:** 2125 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **24**; blast radius 5.805; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (52.3%), Guard Balance (formerly Safety Score) (48.5%), Mutation Surface (formerly State Flux) (46.7%), Complexity Load (formerly Cognitive Load) (14.6%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 469.8)
  * `dt_for_event` **(Compute Cores)** (Impact: 8.0)
  * `all_events` **(Type Conversions)** (Impact: 6.5)
  * `dt_for_change` **(Parameter Forwarders)** (Impact: 3.9)
  * `dt_for_tag` **(Parameter Forwarders)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 309`, `args: 21`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `io: 4`, `api: 14`, `import: 49`
* *Defense:* `safety: 12`, `doc: 1`, `test: 132`, `sync_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.805
  * `Choke Point (Betweenness):` 0.000308 | `Ripple Effect (Closeness):` 0.035211
  * `Imports (Out-Degree: 3):` Carp, Digest::SHA, File::Temp, Locale::TextDomain, Path::Class, Test::Exception, Test::File, Test::More...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `lib/App/Sqitch/Role/DBIEngine.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.565)
- **Top Global Matches:** file_cluster_4: 5.565, file_cluster_15: 8.819, file_cluster_11: 10.123
- **Magnitude:** 618.9 | **LOC:** 1178 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.9%), Guard Balance (formerly Safety Score) (54.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%), Complexity Load (formerly Cognitive Load) (33.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_log_event` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `change_id_for` **(Compute Cores)** (Impact: 39.9)
  * `search_events` **(Compute Cores)** (Impact: 38.9)
  * `register_project` **(Compute Cores)** (Impact: 35.8)
  * `log_deploy_change` **(Many-Argument Workhorses)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 330`, `args: 48`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 38`, `unreferenced_by_name: 4`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 10`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` App::Sqitch::DateTime, App::Sqitch::X, DBI, Locale::TextDomain, Moo::Role, Try::Tiny, namespace::autoclean, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/firebird.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.516)
- **Top Global Matches:** file_cluster_4: 6.516, file_cluster_6: 9.437, file_cluster_15: 12.031
- **Magnitude:** 537.5 | **LOC:** 1024 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Debt Markers (formerly Tech Debt) (92.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `log_deploy_change` **(Compute Cores)** (Impact: 58.5)
  * `search_events` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `change_id_for` **(Compute Cores)** (Impact: 36.4)
  * `default_client` **(Defensive Guards)** (Impact: 28.0)
  * `_ts2char_format` **(Compute Cores)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 309`, `args: 38`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `io: 5`, `api: 24`, `import: 16`
* *Defense:* `safety: 20`, `doc: 1`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App::Sqitch::DateTime, App::Sqitch::Plan::Change, App::Sqitch::Types, App::Sqitch::X, File::Basename, File::Temp, Locale::TextDomain, Moo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/oracle.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.513)
- **Top Global Matches:** file_cluster_4: 6.513, file_cluster_15: 8.341, file_cluster_11: 9.299
- **Magnitude:** 522.44 | **LOC:** 840 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_log_event` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `search_events` **(Compute Cores)** (Impact: 42.6)
    * *Intent:* # Override for special handling of regular the expression operator and # LIMIT/OFFSET.
  * `_script` **(Compute Cores)** (Impact: 26.4)
  * `_file_for_script` **(Compute Cores)** (Impact: 19.6)
  * `change_offset_from_id` **(Many-Argument Workhorses)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 234`, `args: 37`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 48`, `fragile_debt: 1`, `unreferenced_by_name: 32`
* *Architecture:* `io: 4`, `api: 21`, `import: 14`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App::Sqitch::DateTime, App::Sqitch::Plan::Change, App::Sqitch::Types, App::Sqitch::X, DBI, File::Temp, IPC::Run3, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/clickhouse.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.952)
- **Top Global Matches:** file_cluster_4: 5.952, file_cluster_15: 10.655, file_cluster_6: 10.698
- **Magnitude:** 492.08 | **LOC:** 927 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.3%), Mutation Surface (formerly State Flux) (95.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_log_event` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* # Override to query for existing tags separately.
  * `_setup_uri` **(Compute Cores)** (Impact: 43.2)
  * `_conn_cfg` **(Compute Cores)** (Impact: 29.1)
    * *Intent:* # Connection name defaults to host name from url, or else hostname from config # or else localhost. ...
  * `_load_cli` **(Compute Cores)** (Impact: 27.0)
  * `log_new_tags` **(Compute Cores)** (Impact: 25.4)
    * *Intent:* # Override to query for existing tags in a separate query. The LEFT JOIN/UNION # dance simply didn't...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 269`, `args: 36`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `fragile_debt: 3`, `unreferenced_by_name: 23`
* *Architecture:* `io: 6`, `api: 16`, `import: 18`
* *Defense:* `safety: 15`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App::Sqitch::Plan::Change, App::Sqitch::Types, App::Sqitch::X, List::MoreUtils, Locale::TextDomain, Moo, Path::Class, Scalar::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/engine.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.51)
- **Top Global Matches:** file_cluster_11: 6.51, file_cluster_15: 6.837, file_cluster_2: 8.088
- **Magnitude:** 444.26 | **LOC:** 3749 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (78.7%), Connectivity (formerly Api Exposure) (49.9%), Guard Balance (formerly Safety Score) (49.2%), Complexity Load (formerly Cognitive Load) (17.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` App::Sqitch, App::Sqitch::DateTime, App::Sqitch::Plan, App::Sqitch::Target, App::Sqitch::X, Clone, ID, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/plan.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.427)
- **Top Global Matches:** file_cluster_11: 7.427, file_cluster_15: 7.546, file_cluster_13: 7.991
- **Magnitude:** 401.12 | **LOC:** 2062 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (57.2%), Connectivity (formerly Api Exposure) (35.8%), Complexity Load (formerly Cognitive Load) (26.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` App::Sqitch, App::Sqitch::DateTime, App::Sqitch::Target, Encode, File::Path, Locale::TextDomain, MockOutput, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.265)
- **Top Global Matches:** file_cluster_15: 6.265, file_cluster_12: 7.584, file_cluster_10: 8.037
- **Magnitude:** 357.28 | **LOC:** 929 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **34**; blast radius 27.482; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prompt` **(Compute Cores)** (Impact: 27.6)
  * `_find_cmd` **(Compute Cores)** (Impact: 26.9)
  * `spool` **(Compute Cores)** (Impact: 26.2)
  * `_parse_core_opts` **(Compute Cores)** (Impact: 25.0)
  * `ask_y_n` **(Compute Cores)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 245`, `args: 49`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 28`, `fragile_debt: 2`
* *Architecture:* `io: 16`, `api: 26`, `import: 46`
* *Defense:* `safety: 18`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.482
  * `Choke Point (Betweenness):` 0.007504 | `Ripple Effect (Closeness):` 0.140652
  * `Imports (Out-Degree: 6):` App::Sqitch::Command, App::Sqitch::Command::help, App::Sqitch::Config, App::Sqitch::Plan, App::Sqitch::Types, App::Sqitch::X, Config, Encode...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `lib/App/Sqitch/Engine/vertica.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.166)
- **Top Global Matches:** file_cluster_15: 5.166, file_cluster_11: 6.378, file_cluster_16: 7.808
- **Magnitude:** 300.54 | **LOC:** 581 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.2%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.5%), Guard Balance (formerly Safety Score) (53.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cid` **(Defensive Guards)** (Impact: 16.5)
  * `_tag_placeholders` **(Compute Cores)** (Impact: 16.4)
  * `_tag_subselect_columns` **(Compute Cores)** (Impact: 16.4)
  * `_ts2char_format` **(Compute Cores)** (Impact: 14.2)
  * `_select_state` **(Compute Cores)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 213`, `args: 39`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 30`
* *Architecture:* `io: 1`, `api: 19`, `import: 10`
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App::Sqitch::DateTime, App::Sqitch::Types, App::Sqitch::X, DBI, File::Temp, Locale::TextDomain, Moo, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/exasol.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.7)
- **Top Global Matches:** file_cluster_15: 6.7, file_cluster_11: 7.504, file_cluster_13: 8.636
- **Magnitude:** 292.22 | **LOC:** 590 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.9%), Mutation Surface (formerly State Flux) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ts2char_format` **(Compute Cores)** (Impact: 26.4)
  * `_file_for_script` **(Compute Cores)** (Impact: 19.6)
  * `change_offset_from_id` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* # LIMIT / OFFSET in Exasol doesn't seem to play nice in the original query with # JOIN and GROUP BY;...
  * `_cid` **(Defensive Guards)** (Impact: 16.5)
  * `_capture` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 187`, `args: 32`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 22`, `dead_code: 1`, `unreferenced_by_name: 31`
* *Architecture:* `io: 3`, `api: 17`, `import: 15`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App::Sqitch::DateTime, App::Sqitch::Plan::Change, App::Sqitch::Types, App::Sqitch::X, DBI, File::Temp, IPC::Run3, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/sqitch-configuration.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.513)
- **Top Global Matches:** file_cluster_2: 5.513, file_cluster_13: 5.554, file_cluster_17: 7.021
- **Magnitude:** 291.88 | **LOC:** 1038 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.1%), Guard Balance (formerly Safety Score) (68.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 31`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 142`
* *Architecture:* `io: 3`, `import: 15`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/lib/upgradable_registries/firebird.sql` (POSTGRESQL | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.242)
- **Top Global Matches:** file_cluster_2: 4.242, file_cluster_17: 6.042, file_cluster_15: 6.914
- **Magnitude:** 289.92 | **LOC:** 328 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `class_start: 6`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* None
* *Defense:* `safety: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Command/add.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.501)
- **Top Global Matches:** file_cluster_6: 7.501, file_cluster_8: 9.749, file_cluster_4: 15.429
- **Magnitude:** 280.86 | **LOC:** 567 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 2.477; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `execute` **(Compute Cores)** (Impact: 31.7)
  * `_add` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `all_templates` **(Compute Cores)** (Impact: 27.5)
  * `_parse_opts` **(Many-Argument Workhorses)** (Impact: 26.2)
    * *Intent:* # Override to convert multiple vars to an array.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 115`, `args: 13`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 4`, `import: 16`
* *Defense:* `safety: 13`, `doc: 1`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.477
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.003521
  * `Imports (Out-Degree: 2):` App::Sqitch::Types, App::Sqitch::X, Clone, List::Util, Locale::TextDomain, Moo, Path::Class, Template...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/App/Sqitch/Command.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.024)
- **Top Global Matches:** file_cluster_4: 6.024, file_cluster_15: 9.27, file_cluster_11: 10.587
- **Magnitude:** 253.74 | **LOC:** 798 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 5.38; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.6%), Complexity Load (formerly Cognitive Load) (55.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_args` **(Many-Argument Workhorses)** (Impact: 61.9)
  * `_pod2usage` **(Compute Cores)** (Impact: 21.1)
  * `_parse_opts` **(Compute Cores)** (Impact: 11.2)
  * `_mkpath` **(Compute Cores)** (Impact: 7.7)
  * `command` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 177`, `args: 14`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 14`, `api: 11`, `import: 27`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.38
  * `Choke Point (Betweenness):` 0.000498 | `Ripple Effect (Closeness):` 0.083214
  * `Imports (Out-Degree: 3):` App::Sqitch::Target, App::Sqitch::Types, App::Sqitch::X, File::Basename, File::Path, Hash::Merge, Locale::TextDomain, Moo...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/App/Sqitch/Role/TargetConfigCommand.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.334)
- **Top Global Matches:** file_cluster_8: 6.334, file_cluster_6: 13.14, file_cluster_4: 21.742
- **Magnitude:** 249.04 | **LOC:** 554 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.8%), Complexity Load (formerly Cognitive Load) (46.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `config_target` **(Compute Cores)** (Impact: 42.7)
  * `write_plan` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `directories_for` **(Compute Cores)** (Impact: 17.2)
  * `mkdirs` **(Compute Cores)** (Impact: 12.5)
  * `BUILD` **(Defensive Guards)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 112`, `args: 9`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 7`, `import: 17`
* *Defense:* `safety: 8`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App::Sqitch::Plan, App::Sqitch::Target, App::Sqitch::Types, App::Sqitch::X, File::Path, List::Util, Locale::TextDomain, Moo::Role...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Target.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.652)
- **Top Global Matches:** file_cluster_3: 6.652, file_cluster_8: 20.459, file_cluster_6: 33.32
- **Magnitude:** 234.94 | **LOC:** 869 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **10**; blast radius 18.08; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BUILDARGS` **(Compute Cores)** (Impact: 57.1)
  * `all_targets` **(Compute Cores)** (Impact: 47.3)
  * `_fetch` **(Compute Cores)** (Impact: 9.1)
  * `target` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 145`, `args: 18`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 35`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 22`
* *Defense:* `safety: 19`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.08
  * `Choke Point (Betweenness):` 0.001084 | `Ripple Effect (Closeness):` 0.105634
  * `Imports (Out-Degree: 3):` App::Sqitch::Engine, App::Sqitch::Types, App::Sqitch::X, Locale::TextDomain, Moo, Path::Class, URI::db, namespace::autoclean...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `lib/sqitchtutorial-snowflake.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.688)
- **Top Global Matches:** file_cluster_2: 4.688, file_cluster_13: 5.447, file_cluster_17: 6.254
- **Magnitude:** 230.72 | **LOC:** 1456 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.26; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (56.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 62 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 460`, `structural_boundaries: 87`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 71`
* *Architecture:* `io: 7`, `import: 26`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003521
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/App/Sqitch/Engine/mysql.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.62)
- **Top Global Matches:** file_cluster_15: 6.62, file_cluster_11: 7.389, file_cluster_10: 8.151
- **Magnitude:** 220.64 | **LOC:** 638 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.6%), Mutation Surface (formerly State Flux) (81.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cid` **(Defensive Guards)** (Impact: 18.8)
  * `_ts2char_format` **(Compute Cores)** (Impact: 14.2)
  * `_prepare_registry_file` **(Compute Cores)** (Impact: 11.6)
    * *Intent:* # Prepares $file for execution, editing its contents for various MySQL # configurations.
  * `_prepare_to_log` **(Compute Cores)** (Impact: 9.1)
  * `_create_check_function` **(Defensive Guards)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 211`, `args: 33`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 25`
* *Architecture:* `io: 5`, `api: 14`, `import: 16`
* *Defense:* `safety: 17`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App::Sqitch::Plan::Change, App::Sqitch::Types, App::Sqitch::X, File::Temp, List::MoreUtils, Locale::TextDomain, Moo, MySQL::Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/pg.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.611)
- **Top Global Matches:** file_cluster_15: 5.611, file_cluster_11: 6.276, file_cluster_16: 7.987
- **Magnitude:** 212.54 | **LOC:** 574 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (54.0%), Guard Balance (formerly Safety Score) (52.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `log_new_tags` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* # Override to avoid cast errors, and to use VALUES instead of a UNION query.
  * `_run_registry_file` **(Compute Cores)** (Impact: 21.5)
  * `_ts2char_format` **(Compute Cores)** (Impact: 14.2)
  * `destination` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* # VERSION
  * `log_revert_change` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* # Override to take advantage of the RETURNING expression, and to save tags as # an array rather than...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 189`, `args: 30`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 30`
* *Architecture:* `io: 1`, `api: 15`, `import: 14`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App::Sqitch::DateTime, App::Sqitch::Plan::Change, App::Sqitch::Types, App::Sqitch::X, DBI, File::Temp, List::Util, Locale::TextDomain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Engine/snowflake.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.795)
- **Top Global Matches:** file_cluster_15: 5.795, file_cluster_11: 6.401, file_cluster_10: 8.042
- **Magnitude:** 208.02 | **LOC:** 777 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (55.9%), Guard Balance (formerly Safety Score) (51.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cid` **(Defensive Guards)** (Impact: 16.5)
  * `_ts2char_format` **(Compute Cores)** (Impact: 14.3)
  * `_strip_file` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* # Creates and returns a copy of $file with C<CREATE SCHEMA> and C<COMMENT ON # SCHEMA> commands stri...
  * `_limit_offset` **(Compute Cores)** (Impact: 8.4)
  * `destination` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 228`, `args: 31`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `fragile_debt: 5`, `unreferenced_by_name: 25`
* *Architecture:* `io: 3`, `api: 12`, `import: 16`
* *Defense:* `safety: 11`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App::Sqitch::DateTime, App::Sqitch::Types, App::Sqitch::X, DBI, File::Temp, Locale::TextDomain, Moo, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.776)
- **Top Global Matches:** file_cluster_2: 5.776, file_cluster_10: 6.549, file_cluster_13: 6.764
- **Magnitude:** 201.82 | **LOC:** 1162 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Guard Balance (formerly Safety Score) (53.0%), Complexity Load (formerly Cognitive Load) (15.7%), Debt Markers (formerly Tech Debt) (13.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` App::Sqitch, File::Path, File::Spec, Locale::TextDomain, Path::Class, Test::Exception, Test::MockModule, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Sqitch/Command/config.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.57)
- **Top Global Matches:** file_cluster_15: 5.57, file_cluster_16: 7.958, file_cluster_2: 8.499
- **Magnitude:** 195.26 | **LOC:** 667 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (65.7%), Guard Balance (formerly Safety Score) (49.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%), Mutation Surface (formerly State Flux) (27.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configure` **(Compute Cores)** (Impact: 25.9)
  * `get_regex` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `get` **(Defensive Guards)** (Impact: 13.4)
  * `_set` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `rename_section` **(Defensive Guards)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 107`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `api: 15`, `import: 16`
* *Defense:* `safety: 19`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` App::Sqitch::Types, App::Sqitch::X, File::Basename, File::Path, List::Util, Locale::TextDomain, Moo, Path::Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/sqitchtutorial-mysql.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.491)
- **Top Global Matches:** file_cluster_2: 4.491, file_cluster_13: 5.421, file_cluster_17: 5.903
- **Magnitude:** 193.34 | **LOC:** 1749 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.26; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.5%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (52.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 78`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 66`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `import: 26`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003521
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `t/dbiengine_role.t` (PERL) | Magnitude: 23.22 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 35, import: 7, state_mutation: 6
- `xt/locale/test-cli.t` (PERL) | Magnitude: 0.02 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, branch: 9, high_risk_execution: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `t/plan.t` (PERL) | Magnitude: 401.12 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1079, core_var_decl: 449, design_snake_case: 449, branch: 263

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `lib/sqitch-log.pod` (PERL) | Magnitude: 42.64 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 136, decorators: 73, indent_spaces: 52, scientific: 19
- `t/vertica.t` (PERL) | Magnitude: 80.36 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 183, branch: 95, structural_boundaries: 75, globals: 25
- `t/exasol.t` (PERL) | Magnitude: 60.5 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 208, branch: 103, structural_boundaries: 73, core_var_decl: 48
- `t/clickhouse.t` (PERL) | Magnitude: 157.62 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 691, branch: 247, core_var_decl: 235, design_snake_case: 219

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/App/Sqitch/Command/engine.pm` (PERL) | Magnitude: 141.72 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 73, branch: 43, core_var_decl: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lib/sqitch-configuration.pod` (PERL) | Magnitude: 291.88 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 383, branch: 306, decorators: 157, state_mutation: 142

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `.github/ubuntu/sqlite.sh` (SHELL) | Magnitude: 42.42 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 31, io: 25, branch: 24, indent_spaces: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/ubuntu/sqlite.sh` -> Churn: **100.0%** | Cog Load: 54.9834% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/App/Sqitch/Plan.pm` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 1030.66
- `lib/App/Sqitch/Engine.pm` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 883.96
- `lib/App/Sqitch/Role/DBIEngine.pm` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 618.9
- `lib/App/Sqitch/Engine/firebird.pm` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 537.5
- `lib/App/Sqitch/Engine/oracle.pm` -> **David E. Wheeler** (100.0% isolated ownership) | Magnitude: 522.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/App/Sqitch.pm` -> **Severity: 0.668** (Bridge: 0.0075 * Flux: 89.0482%)
- `lib/App/Sqitch/Plan.pm` -> **Severity: 0.626** (Bridge: 0.0063 * Flux: 98.7907%)
- `t/lib/TestConfig.pm` -> **Severity: 0.226** (Bridge: 0.0023 * Flux: 99.5619%)
- `t/base.t` -> **Severity: 0.223** (Bridge: 0.0022 * Flux: 99.991%)
- `t/options.t` -> **Severity: 0.197** (Bridge: 0.002 * Flux: 99.9891%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/App/Sqitch/X.pm` -> **Severity: 11.461** (Embedded: 0.2336 * Error Risk: 49.0534%)
- `t/lib/TestConfig.pm` -> **Severity: 9.813** (Embedded: 0.1693 * Error Risk: 57.9672%)
- `lib/App/Sqitch.pm` -> **Severity: 7.845** (Embedded: 0.1407 * Error Risk: 55.7725%)
- `lib/App/Sqitch/Config.pm` -> **Severity: 7.503** (Embedded: 0.1448 * Error Risk: 51.8271%)
- `lib/App/Sqitch/Plan.pm` -> **Severity: 6.483** (Embedded: 0.1129 * Error Risk: 57.4187%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/App/Sqitch/X.pm` -> **Severity: 12375.1** (Blast Radius: 123.751 * Doc Risk: 100.0%)
- `t/lib/TestConfig.pm` -> **Severity: 4634.7** (Blast Radius: 46.347 * Doc Risk: 100.0%)
- `t/base.t` -> **Severity: 4454.1** (Blast Radius: 44.541 * Doc Risk: 100.0%)
- `lib/App/Sqitch/Config.pm` -> **Severity: 2750.9** (Blast Radius: 27.509 * Doc Risk: 100.0%)
- `lib/App/Sqitch.pm` -> **Severity: 2748.2** (Blast Radius: 27.482 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4537 call pairs -- scoped 1.4%, unique 0.0%, ambiguous 4.1%, external 94.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 4362 | 1.4% | 0.0% | 3.9% | 94.6% |
| postgresql | 102 | 0.0% | 0.0% | 16.7% | 83.3% |
| shell | 72 | 0.0% | 0.0% | 0.0% | 100.0% |
| db2_sql | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
