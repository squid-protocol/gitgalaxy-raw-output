# ARCHITECTURAL_BRIEF: redis
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/redis/redis` |
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
- **Scope:** 1025 analyzed artifact(s), 240899 LOC.
- **Load-bearing artifact:** `src/server.h` -- 76 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/server.h` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/redis-cli.c` at magnitude 11848.0 (structural weight, not risk).
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
| Total Artifacts | 1754 |
| Analyzed Artifacts (Scanned) | 1025 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 729 |
| Total LOC | 240899 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 58.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4236 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2469 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6299 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 423 | 27047 | 41.3% |
| C | 263 | 143453 | 25.7% |
| TCL | 224 | 63393 | 21.9% |
| PYTHON | 40 | 3295 | 3.9% |
| MARKDOWN | 20 | 0 | 2.0% |
| SHELL | 14 | 560 | 1.4% |
| YAML | 12 | 1810 | 1.2% |
| MAKEFILE | 11 | 745 | 1.1% |
| PLAINTEXT | 8 | 1 | 0.8% |
| RUBY | 8 | 487 | 0.8% |
| CPP | 1 | 78 | 0.1% |
| JAVASCRIPT | 1 | 30 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1024 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Declarative / Non-Code 19%, Large Core Modules (3) 11%, Parameter Forwarders Files 7%, Compute Cores Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 997 | 97.3% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 2.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 729*

**Composition by Extension & Reason:**
- `.c`: 267x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 215x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 16385 commas in 837 LOC), 1x Excluded (Saturation: Line 47 exceeds 500 chars)
- `.sh`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.in`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lua`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rdb`: 8x Excluded (Unsupported Extension: '.rdb')
- `.conf`: 6x Excluded (Unsupported Extension: '.conf')
- `.html`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vcxproj`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.filters`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 18.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 19.9 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 32.1 | 2.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1319 | 157 | 2 | `src/server.c` |
| cleanup | 910 | 154 | 2 | `tests/unit/type/list.tcl` |
| guards | 11523 | 443 | 28 | `src/redis-cli.c` |
| danger | 3570 | 315 | 8 | `src/redis-cli.c` |
| concurrency | 1285 | 168 | 2 | `tests/unit/type/stream-cgroups.tcl` |
| connectivity | 8736 | 318 | 18 | `src/server.h` |
| io | 846 | 163 | 2 | `.github/workflows/daily.yml` |
| crypto | 0 | 0 | 0 | - |
| ipc | 173 | 38 | 0 | `src/server.c` |
| time | 150 | 45 | 0 | `src/server.h` |
| serialization | 1 | 1 | 0 | `modules/Makefile` |
| regex | 48 | 7 | 0 | `utils/generate-module-api-doc.rb` |
| events | 448 | 58 | 0 | `src/t_zset.c` |
| tests | 865 | 114 | 1 | `.github/workflows/daily.yml` |
| docs | 182 | 60 | 0 | `src/ebuckets.c` |
| debt | 2699 | 223 | 4 | `.github/workflows/daily.yml` |
| mutation | 56734 | 498 | 123 | `src/redis-cli.c` |
| dead_code | 1821 | 227 | 2 | `src/module.c` |
| credential | 2 | 2 | 0 | `tests/unit/cluster/hostnames.tcl` |
| threat | 82 | 9 | 0 | `tests/integration/corrupt-dump.tcl` |
| ml_ai | 1246 | 165 | 3 | `tests/unit/type/hash-field-expire.tcl` |
| ui | 47 | 8 | 0 | `tests/unit/geo.tcl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/workflows/daily.yml` (Hits: 59)
- `utils/install_server.sh` (Hits: 44)
- `src/mkreleasehdr.sh` (Hits: 33)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **server.h** (`src/server.h`) — 76 inbound connections
2. **zmalloc.c** (`src/zmalloc.c`) — 74 inbound connections
3. **sds.h** (`src/sds.h`) — 63 inbound connections
4. **redismodule.h** (`src/redismodule.h`) — 58 inbound connections
5. **sds.c** (`src/sds.c`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **server.h** (`src/server.h`) — 51 outbound dependencies
2. **server.c** (`src/server.c`) — 46 outbound dependencies
3. **redis-cli.c** (`src/redis-cli.c`) — 34 outbound dependencies
4. **redis-benchmark.c** (`src/redis-benchmark.c`) — 27 outbound dependencies
5. **debug.c** (`src/debug.c`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `rdbLoadObject` **(Many-Argument Workhorses)** (@ `src/rdb.c`) -> Impact: **785.8** | LOC: 1313
  * *Intent:* /* Load a Redis object of the specified type from the specified file. * On success a newly allocated object is returned, otherwise NULL. * * error - W...
- `parseOptions` **(Many-Argument Workhorses)** (@ `src/redis-cli.c`) -> Impact: **576.9** | LOC: 418
  * *Intent:* /*------------------------------------------------------------------------------ * User interface *---------------------------------------------------...
- `debugCommand` **(Many-Argument Workhorses)** (@ `src/debug.c`) -> Impact: **461.4** | LOC: 772
  * *Intent:* #endif
- `quicklistTest` **(Many-Argument Workhorses)** (@ `src/quicklist.c`) -> Impact: **461.3** | LOC: 1506
  * *Intent:* /* main test, but callable from other files */
- `clientCommand` **(Compute Cores)** (@ `src/networking.c`) -> Impact: **332.1** | LOC: 560
- `genRedisInfoString` **(Many-Argument Workhorses)** (@ `src/server.c`) -> Impact: **324.9** | LOC: 739
  * *Intent:* /* Create the string returned by the INFO command. This is decoupled * by the INFO command itself as we need to report the same information * on memor...
- `crashlog_from_file` **(Compute Cores)** (@ `tests/support/util.tcl`) -> Impact: **306.7** | LOC: 1241
  * *Intent:* # Return all log lines starting with the first line that contains a warning. # Generally, this will be an assertion error with a stack trace.
- `rdbLoadRioWithLoadingCtx` **(Many-Argument Workhorses)** (@ `src/rdb.c`) -> Impact: **292.7** | LOC: 397
  * *Intent:* /* Load an RDB file from the rio stream 'rdb'. On success C_OK is returned, * otherwise C_ERR is returned. * The rdb_loading_ctx argument holds object...
- `ziplistTest` **(Many-Argument Workhorses)** (@ `src/ziplist.c`) -> Impact: **282.9** | LOC: 817
  * *Intent:* /* ./redis-server test ziplist <randomseed> */
- `parseExtendedStringArgumentsOrReply` **(Many-Argument Workhorses)** (@ `src/t_string.c`) -> Impact: **281.5** | LOC: 129
  * *Intent:* * * Get specific commands - PERSIST/DEL * Set specific commands - XX/NX/GET/IFEQ/IFNE/IFDEQ/IFDNE * Common commands - EX/EXAT/PX/PXAT/KEEPTTL * * Func...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 201 | 141508.94 | 44.43% | 24.98% |
| `src/commands` | 424 | 11856.52 | 0.0% | 0.0% |
| `tests/unit` | 47 | 10424.48 | 28.18% | 0.0% |
| `tests/modules` | 46 | 8474.66 | 18.7% | 0.0% |
| `modules/vector-sets` | 14 | 6694.72 | 41.63% | 14.28% |
| `tests/unit/type` | 11 | 5948.84 | 29.67% | 0.0% |
| `tests/support` | 11 | 4416.54 | 35.46% | 0.0% |
| `tests/integration` | 28 | 4224.26 | 30.08% | 0.0% |
| `modules/vector-sets/tests` | 31 | 3113.48 | 26.16% | 0.0% |
| `tests/unit/moduleapi` | 46 | 3091.0 | 16.6% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/daily.yml` -> **100.0%** Exposure
- `src/connection.c` -> **99.995%** Exposure
- `.github/workflows/external.yml` -> **99.8841%** Exposure
- `src/eventnotifier.c` -> **99.593%** Exposure
- `src/module.c` -> **99.5389%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/Makefile` -> **100.0%** Exposure
- `modules/vector-sets/test.py` -> **100.0%** Exposure
- `utils/generate-command-code.py` -> **100.0%** Exposure
- `utils/generate-commands-json.py` -> **100.0%** Exposure
- `utils/req-res-log-validator.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/module.c` -> **414** Orphaned Functions | **0** Duplicates
- `.github/workflows/daily.yml` -> **0** Orphaned Functions | **148** Duplicates
- `src/db.c` -> **57** Orphaned Functions | **0** Duplicates
- `src/cluster_legacy.c` -> **52** Orphaned Functions | **0** Duplicates
- `src/networking.c` -> **51** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1536` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/redis-cli.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.3)
- **Top Global Matches:** file_cluster_6: 8.3, file_cluster_8: 12.284, file_cluster_4: 14.811
- **Magnitude:** 11848.0 | **LOC:** 11143 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.595; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseOptions` **(Many-Argument Workhorses)** (Impact: 576.9)
    * *Intent:* /*------------------------------------------------------------------------------ * User interface *-...
  * `cliSendCommand` **(Many-Argument Workhorses)** (Impact: 238.2)
  * `clusterManagerCommandCreate` **(Many-Argument Workhorses)** (Impact: 146.4)
    * *Intent:* /* Cluster Manager Commands */
  * `clusterManagerFixOpenSlot` **(Many-Argument Workhorses)** (Impact: 138.2)
    * *Intent:* /* Slot 'slot' was found to be in importing or migrating state in one or * more nodes. This function...
  * `clusterManagerNodeLoadInfo` **(Many-Argument Workhorses)** (Impact: 130.6)
    * *Intent:* /* Load node's cluster configuration by calling "CLUSTER NODES" command. * Node's configuration (nam...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 14 instances
* *Amplified Cascading Flux:* 1963 instances
* *High Risk Execution (weighted view):* 112
* *State Mutation (weighted view):* 6247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2687`, `structural_boundaries: 807`, `args: 386`, `func_start: 233`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 126`, `state_mutation: 2321`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 48`, `import: 34`
* *Defense:* `safety: 158`, `immutability_locks: 56`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` adlist.h, ae.h, anet.h, assert.h, cli_commands.h, cli_common.h, connection.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/module.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.301)
- **Top Global Matches:** file_cluster_4: 7.301, file_cluster_15: 9.682, file_cluster_12: 10.185
- **Magnitude:** 9479.02 | **LOC:** 15586 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **15**; blast radius 1.514; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.4496% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RM_Call` **(Many-Argument Workhorses)** (Impact: 201.7)
    * *Intent:* * * EACCES: Command cannot be executed, according to ACL rules * * ENOSPC: Write or deny-oom command...
  * `moduleCreateArgvFromUserFormat` **(Many-Argument Workhorses)** (Impact: 134.2)
    * *Intent:* * The integer pointed by 'flags' is populated with flags according * to special modifiers in "fmt". ...
  * `RM_SetCommandInfo` **(Many-Argument Workhorses)** (Impact: 72.7)
    * *Intent:* * * Explanation of the command argument flags: * * * `REDISMODULE_CMD_ARG_OPTIONAL`: The argument is...
  * `RM_ScanKey` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* * RedisModule_CloseKey(key); * RedisModule_ScanCursorDestroy(c); * * The function will return 1 if t...
  * `commandFlagsFromString` **(Compute Cores)** (Impact: 68.2)
    * *Intent:* /* Helper for RM_CreateCommand(). Turns a string representing command * flags into the command flags...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1105 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 3525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1988`, `structural_boundaries: 1620`, `args: 1097`, `func_start: 576`, `class_start: 90`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 3`, `state_mutation: 1315`, `dead_code: 4`, `planned_debt: 12`, `fragile_debt: 3`, `unreferenced_by_name: 414`
* *Architecture:* `io: 5`, `api: 620`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 118`, `doc: 10`, `sync_locks: 8`, `immutability_locks: 226`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.514
  * `Choke Point (Betweenness):` 0.000758 | `Ripple Effect (Closeness):` 0.036627
  * `Imports (Out-Degree: 53):` call_reply.h, cluster.h, cluster_asm.h, crc16_slottable.h, dlfcn.h, fcntl.h, hdr_histogram.h, monotonic.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/server.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.077)
- **Top Global Matches:** file_cluster_4: 5.077, file_cluster_6: 10.811, file_cluster_15: 11.25
- **Magnitude:** 6009.38 | **LOC:** 8171 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 24.1%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **46**; blast radius 3.316; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genRedisInfoString` **(Many-Argument Workhorses)** (Impact: 324.9)
    * *Intent:* /* Create the string returned by the INFO command. This is decoupled * by the INFO command itself as...
  * `processCommand` **(Compute Cores)** (Impact: 210.0)
    * *Intent:* /* If this function gets called we already read a whole * command, arguments are in the client argv/...
  * `main` **(Many-Argument Workhorses)** (Impact: 178.5)
    * *Intent:* #endif
  * `serverCron` **(Many-Argument Workhorses)** (Impact: 140.6)
    * *Intent:* * lookup). * - Software watchdog. * - Update some statistic. * - Incremental rehashing of the DBs ha...
  * `call` **(Many-Argument Workhorses)** (Impact: 124.8)
    * *Intent:* * * Note that regardless of the client flags, if CMD_CALL_PROPAGATE_AOF * or CMD_CALL_PROPAGATE_REPL...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 774 instances
* *State Mutation (weighted view):* 2752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1415`, `structural_boundaries: 657`, `args: 491`, `func_start: 233`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 27`, `state_mutation: 1204`, `fragile_debt: 2`, `unreferenced_by_name: 44`
* *Architecture:* `io: 16`, `api: 222`, `import: 46`
* *Defense:* `safety: 58`, `doc: 3`, `immutability_locks: 78`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.316
  * `Choke Point (Betweenness):` 0.004454 | `Ripple Effect (Closeness):` 0.043468
  * `Imports (Out-Degree: 83):` inet.h, asciilogo.h, atomicvar.h, bio.h, chk.h, cluster.h, cluster_asm.h, cluster_slot_stats.h...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `src/t_zset.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.232)
- **Top Global Matches:** file_cluster_6: 6.232, file_cluster_4: 7.528, file_cluster_16: 15.75
- **Magnitude:** 5004.12 | **LOC:** 5021 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **6**; blast radius 0.877; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%)
- **Documentation Coverage:** 98.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zunionInterDiffGenericCommand` **(Many-Argument Workhorses)** (Impact: 243.0)
    * *Intent:* /* The zunionInterDiffGenericCommand() function is called in order to implement the * following comm...
  * `genericZpopCommand` **(Many-Argument Workhorses)** (Impact: 140.1)
    * *Intent:* * * 'count' is the number of elements requested to pop, or -1 for plain single pop. * * 'use_nested_...
  * `zrangeGenericCommand` **(Many-Argument Workhorses)** (Impact: 137.4)
    * *Intent:* /** * This function handles ZRANGE and ZRANGESTORE, and also the deprecated * Z[REV]RANGE[BYSCORE|BY...
  * `zrandmemberWithCountCommand` **(Many-Argument Workhorses)** (Impact: 114.7)
    * *Intent:* /* How many times bigger should be the zset compared to the requested size * for us to not use the "...
  * `genericZrangebylexCommand` **(Many-Argument Workhorses)** (Impact: 107.1)
    * *Intent:* /* This command implements ZRANGEBYLEX, ZREVRANGEBYLEX. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 672 instances
* *State Mutation (weighted view):* 2058
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1091`, `structural_boundaries: 437`, `args: 182`, `func_start: 159`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 714`, `planned_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `api: 123`, `import: 6`
* *Defense:* `safety: 58`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.877
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.029694
  * `Imports (Out-Degree: 19):` assert.h, fast_float_strtod.h, intset.h, math.h, server.h, testhelp.h
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/commands/auth.json` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/networking.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.38)
- **Top Global Matches:** file_cluster_4: 6.38, file_cluster_15: 11.776, file_cluster_16: 11.777
- **Magnitude:** 4724.54 | **LOC:** 5784 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **14**; blast radius 3.202; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clientCommand` **(Compute Cores)** (Impact: 332.1)
  * `processMultibulkBuffer` **(Many-Argument Workhorses)** (Impact: 84.9)
    * *Intent:* /* Process the query buffer for client 'c', setting up the client argument * vector for command exec...
  * `catClientInfoString` **(Many-Argument Workhorses)** (Impact: 79.8)
    * *Intent:* /* Concatenate a string representing the state of a client in a human * readable format, into the sd...
  * `processInputBuffer` **(Compute Cores)** (Impact: 79.4)
    * *Intent:* /* This function is called every time, in the client structure 'c', there is * more query buffer to ...
  * `afterErrorReply` **(Many-Argument Workhorses)** (Impact: 78.6)
    * *Intent:* /* Do some actions after an error reply was sent (Log if needed, updates stats, etc.) * Possible fla...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 629 instances
* *State Mutation (weighted view):* 2053
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1171`, `structural_boundaries: 480`, `args: 254`, `func_start: 189`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 795`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 51`
* *Architecture:* `api: 154`, `import: 14`
* *Defense:* `safety: 95`, `immutability_locks: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.202
  * `Choke Point (Betweenness):` 0.001172 | `Ripple Effect (Closeness):` 0.039003
  * `Imports (Out-Degree: 36):` atomicvar.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, connection.h, ctype.h, fmtargs.h, fpconv_dtoa.h...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `src/t_stream.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.044)
- **Top Global Matches:** file_cluster_6: 5.044, file_cluster_8: 11.844, file_cluster_4: 12.356
- **Magnitude:** 4625.8 | **LOC:** 5934 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **5**; blast radius 0.907; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `streamReplyWithRange` **(Many-Argument Workhorses)** (Impact: 214.9)
    * *Intent:* * will always pass 'spi' and propagate when a group is passed. * * Note that this function is recurs...
  * `streamParseAddOrTrimArgsOrReply` **(Many-Argument Workhorses)** (Impact: 171.4)
    * *Intent:* /* Parse the arguments of XADD/XTRIM. * * See streamAddTrimArgs for more details about the arguments...
  * `xreadCommand` **(Many-Argument Workhorses)** (Impact: 155.5)
    * *Intent:* /* XREAD [BLOCK <milliseconds>] [COUNT <count>] STREAMS key_1 key_2 ... key_N * ID_1 ID_2 ... ID_N *...
  * `streamAppendItem` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* * but instead the passed ID is used to add the new entry. In this case * adding the entry may fail a...
  * `streamIteratorGetID` **(Many-Argument Workhorses)** (Impact: 111.3)
    * *Intent:* /* Return 1 and store the current item ID at 'id' if there are still * elements within the iteration...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 611 instances
* *State Mutation (weighted view):* 1989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1103`, `structural_boundaries: 434`, `args: 159`, `func_start: 116`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 767`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 109`, `import: 5`
* *Defense:* `safety: 71`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.907
  * `Choke Point (Betweenness):` 9.8e-05 | `Ripple Effect (Closeness):` 0.031509
  * `Imports (Out-Degree: 19):` endianconv.h, server.h, stream.h, string.h, xxhash.h
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/cluster_legacy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.171)
- **Top Global Matches:** file_cluster_4: 5.171, file_cluster_15: 10.627, file_cluster_12: 10.79
- **Magnitude:** 4609.84 | **LOC:** 6582 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **15**; blast radius 1.185; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clusterCommandSpecial` **(Compute Cores)** (Impact: 238.4)
  * `clusterProcessPacket` **(Compute Cores)** (Impact: 227.0)
    * *Intent:* /* When this function is called, there is a packet to process starting * at link->rcvbuf. Releasing ...
  * `clusterLoadConfig` **(Many-Argument Workhorses)** (Impact: 160.8)
    * *Intent:* /* ----------------------------------------------------------------------------- * Initialization * ...
  * `clusterUpdateSlotsConfigWith` **(Many-Argument Workhorses)** (Impact: 80.3)
    * *Intent:* /* This function is called when we receive a master configuration via a * PING, PONG or UPDATE packe...
  * `clusterGenNodeDescription` **(Many-Argument Workhorses)** (Impact: 72.8)
    * *Intent:* /* Generate a csv-alike representation of the specified cluster node. * See clusterGenNodesDescripti...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 597 instances
* *State Mutation (weighted view):* 1943
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1174`, `structural_boundaries: 582`, `args: 448`, `func_start: 204`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 9`, `state_mutation: 749`, `planned_debt: 1`, `unreferenced_by_name: 52`
* *Architecture:* `io: 5`, `api: 246`, `import: 15`
* *Defense:* `safety: 20`, `immutability_locks: 25`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.185
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.032503
  * `Imports (Out-Degree: 29):` inet.h, cluster.h, cluster_asm.h, cluster_legacy.h, cluster_slot_stats.h, connection.h, endianconv.h, fcntl.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/rdb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.827)
- **Top Global Matches:** file_cluster_6: 5.827, file_cluster_4: 9.068, file_cluster_8: 16.255
- **Magnitude:** 4502.56 | **LOC:** 4540 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **20**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rdbLoadObject` **(Many-Argument Workhorses)** (Impact: 785.8)
    * *Intent:* /* Load a Redis object of the specified type from the specified file. * On success a newly allocated...
  * `rdbLoadRioWithLoadingCtx` **(Many-Argument Workhorses)** (Impact: 292.7)
    * *Intent:* /* Load an RDB file from the rio stream 'rdb'. On success C_OK is returned, * otherwise C_ERR is ret...
  * `rdbSaveObject` **(Many-Argument Workhorses)** (Impact: 242.1)
    * *Intent:* /* Save a Redis object. * Returns -1 on error, number of bytes written on success. */
  * `rdbSaveToSlavesSockets` **(Many-Argument Workhorses)** (Impact: 73.9)
    * *Intent:* /* Spawn an RDB child that writes the RDB to the sockets of the slaves * that are currently in SLAVE...
  * `rdbGenericLoadStringObjectUsable` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* /* Load a string object from an RDB file according to flags: * * RDB_LOAD_NONE (no flags): load an R...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 571 instances
* *State Mutation (weighted view):* 1760
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1028`, `structural_boundaries: 459`, `args: 183`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 5`, `state_mutation: 618`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `io: 7`, `api: 83`, `import: 20`
* *Defense:* `safety: 57`, `immutability_locks: 6`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.000735 | `Ripple Effect (Closeness):` 0.034858
  * `Imports (Out-Degree: 54):` inet.h, bio.h, cluster_asm.h, endianconv.h, fcntl.h, fpconv_dtoa.h, functions.h, intset.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/sentinel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.001)
- **Top Global Matches:** file_cluster_4: 5.001, file_cluster_6: 8.309, file_cluster_16: 12.819
- **Magnitude:** 4470.1 | **LOC:** 5475 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 0.736; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sentinelHandleConfiguration` **(Compute Cores)** (Impact: 190.2)
  * `sentinelCommand` **(Compute Cores)** (Impact: 188.7)
  * `sentinelRefreshInstanceInfo` **(Many-Argument Workhorses)** (Impact: 158.3)
    * *Intent:* /* Process the INFO output from masters. */
  * `sentinelSetDebugConfigParameters` **(Compute Cores)** (Impact: 102.0)
  * `sentinelSetCommand` **(Compute Cores)** (Impact: 99.2)
    * *Intent:* /* SENTINEL SET <mastername> [<option> <value> ...] */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 646 instances
* *State Mutation (weighted view):* 2100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1101`, `structural_boundaries: 413`, `args: 238`, `func_start: 125`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 6`, `state_mutation: 808`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 152`, `import: 10`
* *Defense:* `safety: 4`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.736
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.029213
  * `Imports (Out-Degree: 15):` inet.h, async.h, ctype.h, fcntl.h, hiredis.h, hiredis_ssl.h, ssl.h, server.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/t_hash.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.596)
- **Top Global Matches:** file_cluster_6: 4.596, file_cluster_4: 11.626, file_cluster_8: 12.634
- **Magnitude:** 3355.78 | **LOC:** 4094 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **6**; blast radius 0.964; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseHashFieldExpireArgs` **(Many-Argument Workhorses)** (Impact: 142.9)
    * *Intent:* #define HFE_KEEPTTL (1<<5) /* Do not discard field ttl on set op */ #define HFE_FXX (1<<6) /* Set fi...
  * `hrandfieldWithCountCommand` **(Many-Argument Workhorses)** (Impact: 121.4)
    * *Intent:* /* How many times bigger should be the hash compared to the requested size * for us to not use the "...
  * `hashTypeGetValue` **(Many-Argument Workhorses)** (Impact: 103.4)
    * *Intent:* * Arguments: * hfeFlags - Lookup for HFE_LAZY_* flags * * Returned: * GetFieldRes - Result of get op...
  * `hashTypeSet` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `httlGenericCommand` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* /* HTTL key <FIELDS count field [field ...]> */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 431 instances
* *State Mutation (weighted view):* 1352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 772`, `structural_boundaries: 319`, `args: 154`, `func_start: 96`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 490`, `unreferenced_by_name: 35`
* *Architecture:* `api: 84`, `import: 6`
* *Defense:* `safety: 50`, `doc: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.964
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.02994
  * `Imports (Out-Degree: 21):` cluster_asm.h, ebuckets.h, entry.h, math.h, redisassert.h, server.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/replication.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.838)
- **Top Global Matches:** file_cluster_6: 4.838, file_cluster_4: 8.982, file_cluster_8: 15.441
- **Magnitude:** 3320.42 | **LOC:** 5410 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **13**; blast radius 1.181; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.4%), Guard Balance (formerly Safety Score) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSyncBulkPayload` **(Many-Argument Workhorses)** (Impact: 128.4)
    * *Intent:* /* Asynchronously read the SYNC payload we receive from a master */ #define REPL_MAX_WRITTEN_BEFORE_...
  * `syncWithMaster` **(Many-Argument Workhorses)** (Impact: 115.6)
    * *Intent:* /* This handler fires when the non blocking connect was able to * establish a connection with the ma...
  * `replconfCommand` **(Compute Cores)** (Impact: 112.2)
    * *Intent:* * Unlike other subcommands, this is used by master to get the replication * offset from a replica. *...
  * `syncCommand` **(Compute Cores)** (Impact: 77.4)
    * *Intent:* /* SYNC and PSYNC command implementation. */
  * `slaveTryPartialResynchronization` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* * 1) As a side effect of the function call the function removes the readable * event handler from "f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 457 instances
* *State Mutation (weighted view):* 1493
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 873`, `structural_boundaries: 421`, `args: 316`, `func_start: 113`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 579`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 23`
* *Architecture:* `io: 8`, `api: 101`, `import: 13`
* *Defense:* `safety: 35`, `doc: 1`, `immutability_locks: 5`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.181
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.032798
  * `Imports (Out-Degree: 38):` bio.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, connection.h, fcntl.h, functions.h, memory.h...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/db.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.806)
- **Top Global Matches:** file_cluster_4: 4.806, file_cluster_6: 10.515, file_cluster_15: 10.773
- **Magnitude:** 3176.36 | **LOC:** 3915 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 22.7%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **12**; blast radius 2.006; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.6241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scanGenericCommand` **(Many-Argument Workhorses)** (Impact: 185.1)
    * *Intent:* /* This command implements SCAN, HSCAN and SSCAN commands. * If object 'o' is passed, then it must b...
  * `getKeysUsingKeySpecs` **(Many-Argument Workhorses)** (Impact: 103.7)
    * *Intent:* /* Fetch the keys based of the provided key specs. Returns the number of keys found, or -1 on error....
  * `dbSetValue` **(Many-Argument Workhorses)** (Impact: 100.2)
    * *Intent:* * transferred to this function. The value may be reallocated, potentially * invalidating any externa...
  * `lookupKey` **(Many-Argument Workhorses)** (Impact: 58.9)
    * *Intent:* * LOOKUP_NONE (or zero): No special flags are passed. * LOOKUP_NOTOUCH: Don't alter the last access ...
  * `copyCommand` **(Compute Cores)** (Impact: 58.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 378 instances
* *State Mutation (weighted view):* 1194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 708`, `structural_boundaries: 333`, `args: 169`, `func_start: 135`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 438`, `planned_debt: 5`, `unreferenced_by_name: 57`
* *Architecture:* `api: 128`, `import: 12`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 0.00072 | `Ripple Effect (Closeness):` 0.039003
  * `Imports (Out-Degree: 51):` atomicvar.h, bio.h, cluster.h, cluster_asm.h, ctype.h, functions.h, keymeta.h, latency.h...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `src/config.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.489)
- **Top Global Matches:** file_cluster_4: 6.489, file_cluster_16: 7.438, file_cluster_15: 8.473
- **Magnitude:** 2838.76 | **LOC:** 3777 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 0.723; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (52.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadServerConfigFromString` **(Compute Cores)** (Impact: 87.9)
  * `configSetCommand` **(Compute Cores)** (Impact: 55.2)
    * *Intent:* /*----------------------------------------------------------------------------- * CONFIG SET impleme...
  * `numericParseString` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `setNumericType` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* /* Gets a 'long long val' and sets it into the union, using a macro to get * compile time type check...
  * `rewriteConfigReadOldFile` **(Compute Cores)** (Impact: 43.5)
    * *Intent:* /* Read the old file, split it into lines to populate a newly created * config rewrite state, and re...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 375 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 1180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 406`, `args: 194`, `func_start: 151`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 430`, `planned_debt: 1`, `unreferenced_by_name: 27`
* *Architecture:* `io: 7`, `api: 87`, `import: 10`
* *Defense:* `safety: 24`, `immutability_locks: 121`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.723
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.029694
  * `Imports (Out-Degree: 29):` bio.h, cluster.h, connection.h, ctype.h, fcntl.h, glob.h, locale.h, server.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/listpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.43)
- **Top Global Matches:** file_cluster_4: 5.43, file_cluster_6: 9.419, file_cluster_16: 12.072
- **Magnitude:** 2785.98 | **LOC:** 3335 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **14**; blast radius 1.096; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.5%), Guard Balance (formerly Safety Score) (68.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listpackTest` **(Many-Argument Workhorses)** (Impact: 248.0)
  * `lpInsert` **(Many-Argument Workhorses)** (Impact: 97.9)
    * *Intent:* * or replace with a string, which is stored in the 'elestr' buffer. * * Returns NULL on out of memor...
  * `lpGetWithSize` **(Many-Argument Workhorses)** (Impact: 76.0)
    * *Intent:* * * If 'entry_size' is not NULL, *entry_size is set to the entry length of the * listpack element po...
  * `lpEncodeIntegerGetType` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* /* Stores the integer encoded representation of 'v' in the 'intenc' buffer. */
  * `lpBatchInsert` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* * and 'sval' and 'slen' will be used. Otherwise, 'lval' will be used to append * the integer entry. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 412 instances
* *State Mutation (weighted view):* 1437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 470`, `structural_boundaries: 219`, `args: 94`, `func_start: 73`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 613`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 11`
* *Architecture:* `io: 3`, `api: 49`, `import: 14`
* *Defense:* `safety: 220`, `test: 64`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.096
  * `Choke Point (Betweenness):` 0.000125 | `Ripple Effect (Closeness):` 0.031091
  * `Imports (Out-Degree: 11):` adlist.h, limits.h, listpack.h, listpack_malloc.h, redisassert.h, sds.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/quicklist.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.837)
- **Top Global Matches:** file_cluster_4: 5.837, file_cluster_12: 11.197, file_cluster_6: 11.211
- **Magnitude:** 2601.24 | **LOC:** 3659 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **14**; blast radius 0.797; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quicklistTest` **(Many-Argument Workhorses)** (Impact: 461.3)
    * *Intent:* /* main test, but callable from other files */
  * `_quicklistInsert` **(Many-Argument Workhorses)** (Impact: 119.9)
    * *Intent:* /* Insert a new entry before or after existing entry 'entry'. * * If after==1, the new value is inse...
  * `quicklistPopCustom` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* /* pop from quicklist and return result in 'data' ptr. Value of 'data' * is the return value of 'sav...
  * `quicklistDelRange` **(Many-Argument Workhorses)** (Impact: 48.3)
    * *Intent:* /* Delete a range of elements from the quicklist. * * elements may span across multiple quicklistNod...
  * `quicklistReplaceEntry` **(Many-Argument Workhorses)** (Impact: 39.1)
    * *Intent:* /* Replace quicklist entry by 'data' with length 'sz'. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 343 instances
* *State Mutation (weighted view):* 1137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 518`, `structural_boundaries: 157`, `args: 92`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 451`, `unreferenced_by_name: 10`
* *Architecture:* `api: 64`, `import: 14`
* *Defense:* `safety: 161`, `test: 42`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.797
  * `Choke Point (Betweenness):` 7.9e-05 | `Ripple Effect (Closeness):` 0.02942
  * `Imports (Out-Degree: 13):` config.h, limits.h, listpack.h, lzf.h, quicklist.h, redisassert.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/cluster_asm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.073)
- **Top Global Matches:** file_cluster_4: 5.073, file_cluster_6: 9.663, file_cluster_16: 12.104
- **Magnitude:** 2558.52 | **LOC:** 3810 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 1.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.6%)
- **Documentation Coverage:** 99.2157% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clusterSyncSlotsCommand` **(Compute Cores)** (Impact: 164.5)
  * `slotSnapshotSaveRio` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* /* Save the slot ranges snapshot to the file. It generates the DUMP encoded * representation of each...
  * `asmSyncWithSource` **(Compute Cores)** (Impact: 47.6)
  * `asmTaskStateToString` **(Compute Cores)** (Impact: 43.0)
  * `asmReplicaHandleMasterTask` **(Compute Cores)** (Impact: 40.2)
    * *Intent:* /* The replicas handle the master import ASM task information. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 740`, `structural_boundaries: 426`, `args: 228`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 398`, `planned_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 111`, `import: 6`
* *Defense:* `safety: 16`, `doc: 2`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.032
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.032213
  * `Imports (Out-Degree: 35):` bio.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, functions.h, server.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `modules/vector-sets/hnsw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.42)
- **Top Global Matches:** file_cluster_6: 6.42, file_cluster_4: 6.523, file_cluster_16: 14.699
- **Magnitude:** 2537.6 | **LOC:** 3300 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.933; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.2%), Complexity Load (formerly Cognitive Load) (75.0%)
- **Documentation Coverage:** 49.2958% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hnsw_reconnect_nodes` **(Many-Argument Workhorses)** (Impact: 117.9)
    * *Intent:* * * So the score is directly proportional to the SIMILARITY of the two nodes * and also directly pro...
  * `select_neighbors` **(Many-Argument Workhorses)** (Impact: 100.3)
    * *Intent:* * that already has the max number of links, inevitably some other node loses * a connection (to make...
  * `search_layer_with_filter` **(Many-Argument Workhorses)** (Impact: 80.1)
    * *Intent:* /* Search the specified layer starting from the specified entry point * to collect 'ef' nodes that a...
  * `hnsw_node_new` **(Many-Argument Workhorses)** (Impact: 60.8)
    * *Intent:* * * Only vector or qvector should be non-NULL. The reason why passing * a quantized vector is useful...
  * `hnsw_insert_serialized` **(Many-Argument Workhorses)** (Impact: 59.9)
    * *Intent:* /* Load a serialized node. See the top comment in this section of code * for the documentation about...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 360 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 460`, `structural_boundaries: 264`, `args: 97`, `func_start: 71`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 419`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 23`
* *Architecture:* `api: 71`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001951
  * `Imports (Out-Degree: 2):` assert.h, float.h, hnsw.h, immintrin.h, math.h, mixer.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/acl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.169)
- **Top Global Matches:** file_cluster_4: 5.169, file_cluster_12: 10.326, file_cluster_15: 10.906
- **Magnitude:** 2449.94 | **LOC:** 3314 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **5**; blast radius 0.894; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.3%), Guard Balance (formerly Safety Score) (71.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aclCommand` **(Compute Cores)** (Impact: 163.5)
    * *Intent:* /* ACL -- show and modify the configuration of ACL users. * ACL HELP * ACL LOAD * ACL SAVE * ACL LIS...
  * `ACLSetSelector` **(Many-Argument Workhorses)** (Impact: 138.8)
    * *Intent:* * It is possible to specify multiple patterns. * %R~<pattern> Add key read pattern that specifies wh...
  * `ACLSetUser` **(Many-Argument Workhorses)** (Impact: 90.8)
    * *Intent:* * When an error is returned, errno is set to the following values: * * EINVAL: The specified opcode ...
  * `ACLSelectorCheckCmd` **(Many-Argument Workhorses)** (Impact: 64.3)
    * *Intent:* /* Check if the command is ready to be executed according to the * ACLs associated with the specifie...
  * `ACLLoadFromFile` **(Compute Cores)** (Impact: 56.3)
    * *Intent:* * also allowed. * * One important part of implementing ACL LOAD, that uses this function, is * to av...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 312 instances
* *State Mutation (weighted view):* 975
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 586`, `structural_boundaries: 315`, `args: 161`, `func_start: 96`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 3`, `state_mutation: 351`, `dead_code: 1`, `unreferenced_by_name: 16`
* *Architecture:* `io: 4`, `api: 102`, `import: 5`
* *Defense:* `safety: 20`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.894
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.031647
  * `Imports (Out-Degree: 18):` cluster.h, ctype.h, fcntl.h, server.h, sha256.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/bitops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.797)
- **Top Global Matches:** file_cluster_8: 6.797, file_cluster_6: 13.189, file_cluster_4: 21.861
- **Magnitude:** 2445.4 | **LOC:** 2196 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.636; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bitopCommand` **(Compute Cores)** (Impact: 180.2)
  * `bitfieldGeneric` **(Many-Argument Workhorses)** (Impact: 122.8)
    * *Intent:* /* This implements both the BITFIELD command and the BITFIELD_RO command * when flags is set to BITF...
  * `bitposCommand` **(Compute Cores)** (Impact: 86.1)
    * *Intent:* /* BITPOS key bit [start [end [BIT|BYTE]]] */
  * `bitopCommandAVX` **(Many-Argument Workhorses)** (Impact: 80.9)
    * *Intent:* #ifdef HAVE_AVX2 /* Compute the given bitop operation using AVX2 intrinsics. * Return how many bytes...
  * `bitopCommandAVX512` **(Many-Argument Workhorses)** (Impact: 80.9)
    * *Intent:* #endif /* HAVE_AVX2 */ #ifdef HAVE_AVX512 /* Compute the given bitop operation using AVX512 intrinsi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 435 instances
* *State Mutation (weighted view):* 1410
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 138`, `args: 39`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 540`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 12`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023053
  * `Imports (Out-Degree: 10):` arm_neon.h, ctype.h, immintrin.h, server.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/redis-benchmark.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.592)
- **Top Global Matches:** file_cluster_8: 8.592, file_cluster_6: 8.922, file_cluster_4: 17.071
- **Magnitude:** 2264.56 | **LOC:** 2044 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.595; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.8%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseOptions` **(Many-Argument Workhorses)** (Impact: 217.6)
    * *Intent:* /* Returns number of consumed options. */
  * `main` **(Many-Argument Workhorses)** (Impact: 136.2)
  * `createClient` **(Many-Argument Workhorses)** (Impact: 103.3)
    * *Intent:* * Also an initial SELECT command is prepended in order to make sure the right * database is selected...
  * `readHandler` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `fetchClusterConfiguration` **(I/O & Config Routines)** (Impact: 58.2)
    * *Intent:* /* TODO: This should be refactored to use CLUSTER SLOTS, the migrating/importing * information is an...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 24 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 390 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 24
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 472`, `structural_boundaries: 141`, `args: 68`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 20`, `state_mutation: 474`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 4`, `import: 27`
* *Defense:* `safety: 28`, `sync_locks: 3`, `immutability_locks: 48`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` adlist.h, ae.h, assert.h, atomicvar.h, cli_common.h, crc16_slottable.h, dict.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/aof.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.816)
- **Top Global Matches:** file_cluster_6: 5.816, file_cluster_4: 7.43, file_cluster_12: 15.643
- **Magnitude:** 2139.36 | **LOC:** 2970 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **13**; blast radius 0.821; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rewriteStreamObject` **(Many-Argument Workhorses)** (Impact: 120.7)
    * *Intent:* /* Emit the commands needed to rebuild a stream object. * The function returns 0 on error, 1 on succ...
  * `loadSingleAppendOnlyFile` **(Compute Cores)** (Impact: 92.5)
    * *Intent:* /* Replay an append log file. On success AOF_OK or AOF_TRUNCATED is returned, * otherwise, one of th...
  * `flushAppendOnlyFile` **(Compute Cores)** (Impact: 75.5)
    * *Intent:* * buffer and write it on disk using this function just before entering * the event loop again. * * A...
  * `rewriteObject` **(Stateful Encapsulated Methods)** (Impact: 75.4)
  * `aofLoadManifestFromFile` **(Compute Cores)** (Impact: 61.7)
    * *Intent:* /* Generic manifest loading function, used in `aofLoadManifestFromDisk` and redis-check-aof tool. */...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 270 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 874
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 224`, `args: 180`, `func_start: 72`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 13`, `state_mutation: 334`, `unreferenced_by_name: 9`
* *Architecture:* `io: 18`, `api: 78`, `import: 13`
* *Defense:* `safety: 18`, `immutability_locks: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.821
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.030065
  * `Imports (Out-Degree: 34):` bio.h, cluster_asm.h, fcntl.h, functions.h, rio.h, server.h, signal.h, param.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/ebuckets.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.999)
- **Top Global Matches:** file_cluster_4: 5.999, file_cluster_12: 10.449, file_cluster_16: 11.28
- **Magnitude:** 2106.86 | **LOC:** 2726 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 0.756; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%), Complexity Load (formerly Cognitive Load) (62.9%)
- **Documentation Coverage:** 77.0115% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ebucketsTest` **(Many-Argument Workhorses)** (Impact: 130.3)
  * `ebRemoveFromRax` **(Many-Argument Workhorses)** (Impact: 85.1)
    * *Intent:* /* * Remove item from rax * * Return 1 if removed. Otherwise, return 0 * * Note: The function is opt...
  * `ebExpireDryRun` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* /* Performs active expiration dry-run to evaluate number of expired items * * It is faster than actu...
  * `distributeTest` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /* expireRanges - is given as bucket-key to be agnostic to the different configuration * of EB_BUCKE...
  * `ebSegExpire` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /* return 1 if managed to expire the entire segment. Returns 0 otherwise. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 181`, `args: 66`, `func_start: 54`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 448`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 42`, `import: 14`
* *Defense:* `safety: 83`, `doc: 19`, `test: 18`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.756
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.026373
  * `Imports (Out-Degree: 7):` config.h, ebuckets.h, inttypes.h, redisassert.h, stddef.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/ziplist.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.616)
- **Top Global Matches:** file_cluster_4: 5.616, file_cluster_16: 10.945, file_cluster_6: 11.166
- **Magnitude:** 1984.78 | **LOC:** 2666 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.612; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.3%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ziplistTest` **(Many-Argument Workhorses)** (Impact: 282.9)
    * *Intent:* /* ./redis-server test ziplist <randomseed> */
  * `zipTryEncoding` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* /* Check if string pointed to by 'entry' can be encoded as an integer. * Stores the integer value in...
  * `__ziplistInsert` **(Many-Argument Workhorses)** (Impact: 42.9)
    * *Intent:* /* Insert item at "p". */
  * `ziplistValidateIntegrity` **(Many-Argument Workhorses)** (Impact: 42.3)
    * *Intent:* /* Validate the integrity of the data structure. * when `deep` is 0, only the integrity of the heade...
  * `zipEntrySafe` **(Many-Argument Workhorses)** (Impact: 37.3)
    * *Intent:* /* Fills a struct with all information about an entry. * This function is safe to use on untrusted p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 298 instances
* *State Mutation (weighted view):* 974
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 160`, `args: 109`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 378`, `unreferenced_by_name: 5`
* *Architecture:* `io: 12`, `api: 35`, `import: 15`
* *Defense:* `safety: 137`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.612
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.025117
  * `Imports (Out-Degree: 13):` adlist.h, config.h, endianconv.h, limits.h, redisassert.h, sds.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cluster.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.866)
- **Top Global Matches:** file_cluster_6: 5.866, file_cluster_4: 6.929, file_cluster_15: 15.091
- **Magnitude:** 1957.88 | **LOC:** 2348 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 18.8%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **6**; blast radius 1.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNodeByQuery` **(Many-Argument Workhorses)** (Impact: 268.8)
    * *Intent:* * * CLUSTER_REDIR_UNSTABLE if the request contains multiple keys * belonging to the same slot, but t...
  * `migrateCommand` **(Compute Cores)** (Impact: 123.0)
    * *Intent:* /* MIGRATE host port key dbid timeout [COPY | REPLACE | AUTH password | * AUTH2 username password] *...
  * `clusterCommand` **(Compute Cores)** (Impact: 86.7)
  * `restoreCommand` **(Compute Cores)** (Impact: 67.0)
    * *Intent:* /* RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME seconds] [FREQ frequency] */
  * `sflushCommand` **(Compute Cores)** (Impact: 41.0)
    * *Intent:* /* Partially flush destination DB in a cluster node, based on the slot range. * * Usage: SFLUSH <sta...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 243 instances
* *State Mutation (weighted view):* 755
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 505`, `structural_boundaries: 213`, `args: 75`, `func_start: 66`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 269`, `dead_code: 1`, `unreferenced_by_name: 25`
* *Architecture:* `api: 63`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.195
  * `Choke Point (Betweenness):` 0.000191 | `Ripple Effect (Closeness):` 0.031647
  * `Imports (Out-Degree: 36):` bio.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, ctype.h, server.h
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `modules/vector-sets/tests/concurrent_vsim_and_del.py` (PYTHON) | Magnitude: 56.32 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, state_mutation: 9, branch: 7
- `modules/Makefile` (MAKEFILE) | Magnitude: 39.38 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 52, branch: 15, structural_boundaries: 13, func_start: 12
- `tests/support/response_transformers.tcl` (TCL) | Magnitude: 60.88 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 18, state_mutation: 10, branch: 9
- `tests/integration/rdb.tcl` (TCL) | Magnitude: 255.92 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 402, state_mutation: 85, branch: 46, safety: 16
- `modules/vector-sets/tests/memory_usage.py` (PYTHON) | Magnitude: 13.82 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, state_mutation: 6, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `utils/releasetools/03_test_release.sh` (SHELL) | Magnitude: 14.3 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 12, safety_bypasses: 4, io: 3, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/unit/info.tcl` (TCL) | Magnitude: 237.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 562, state_mutation: 128, safety: 30, branch: 21
- `modules/vector-sets/tests/vrandmember.py` (PYTHON) | Magnitude: 52.9 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 34, indent_spaces: 32, safety: 17, state_mutation: 14
- `modules/vector-sets/tests/vemb.py` (PYTHON) | Magnitude: 44.52 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, state_mutation: 10, core_var_decl: 10
- `tests/unit/type/string.tcl` (TCL) | Magnitude: 561.1 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1291, state_mutation: 392, scientific: 31, branch: 28
- `tests/unit/sort.tcl` (TCL) | Magnitude: 170.14 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 355, state_mutation: 58, branch: 28, scientific: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/modules/timer.c` (C) | Magnitude: 53.84 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 18, pointers: 16, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/sentinel/tests/12-master-reboot.tcl` (TCL) | Magnitude: 40.28 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 16, branch: 10, structural_boundaries: 3
- `tests/unit/replybufsize.tcl` (TCL) | Magnitude: 28.94 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, state_mutation: 5, branch: 3, structural_boundaries: 3
- `tests/integration/failover.tcl` (TCL) | Magnitude: 46.44 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 206, state_mutation: 30, branch: 13, scientific: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tests/modules/list.c` (C) | Magnitude: 220.84 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 182, branch: 60, structural_boundaries: 28, pointers: 28
- `src/syscheck.c` (C) | Magnitude: 213.84 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 202, branch: 52, core_var_decl: 41, design_snake_case: 41
- `modules/vector-sets/hnsw.c` (C) | Magnitude: 2537.6 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1598, pointers: 890, branch: 460, state_mutation: 419

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `modules/vector-sets/tests/vrand-ping-pong.py` (PYTHON) | Magnitude: 27.12 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 10, core_var_decl: 9, design_snake_case: 9
- `tests/support/aofmanifest.tcl` (TCL) | Magnitude: 163.58 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 103, state_mutation: 45, structural_boundaries: 33, args: 18
- `modules/vector-sets/tests/replication.py` (PYTHON) | Magnitude: 76.34 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 22, structural_boundaries: 20, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/sds.h` (C) | Magnitude: 195.32 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 164, pointers: 107, structural_boundaries: 100, api: 66
- `tests/modules/keymeta_notify.c` (C) | Magnitude: 83.82 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 81, branch: 20, state_mutation: 16, structural_boundaries: 15

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/server.c` -> Churn: **89.88%** | Cog Load: 91.9421% | Debt: 22.0842%
- `src/db.c` -> Churn: **82.86%** | Cog Load: 93.4922% | Debt: 77.6482%
- `src/module.c` -> Churn: **80.45%** | Cog Load: 74.6284% | Debt: 99.5389%
- `src/rdb.c` -> Churn: **80.45%** | Cog Load: 97.233% | Debt: 15.3312%
- `src/t_stream.c` -> Churn: **77.81%** | Cog Load: 94.5196% | Debt: 21.9389%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/quicklist.c` -> **Slavomir Kaslev** (100.0% isolated ownership) | Magnitude: 2601.24
- `src/redis-benchmark.c` -> **h.o.t. neglected** (100.0% isolated ownership) | Magnitude: 2264.56
- `src/ebuckets.c` -> **cui** (100.0% isolated ownership) | Magnitude: 2106.86
- `src/ziplist.c` -> **zzj** (100.0% isolated ownership) | Magnitude: 1984.78
- `src/rax.c` -> **Sergei Georgiev** (100.0% isolated ownership) | Magnitude: 1812.52

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/server.c` -> **Severity: 0.445** (Bridge: 0.0045 * Flux: 100.0%)
- `src/keymeta.c` -> **Severity: 0.126** (Bridge: 0.0013 * Flux: 100.0%)
- `src/connection.c` -> **Severity: 0.124** (Bridge: 0.0012 * Flux: 100.0%)
- `src/object.c` -> **Severity: 0.122** (Bridge: 0.0012 * Flux: 99.9996%)
- `src/networking.c` -> **Severity: 0.117** (Bridge: 0.0012 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/support/test.tcl` -> **Severity: 5.165** (Embedded: 0.066 * Error Risk: 78.2714%)
- `tests/test_helper.tcl` -> **Severity: 4.832** (Embedded: 0.0554 * Error Risk: 87.1426%)
- `tests/support/util.tcl` -> **Severity: 4.354** (Embedded: 0.0517 * Error Risk: 84.1966%)
- `src/sds.c` -> **Severity: 4.21** (Embedded: 0.0539 * Error Risk: 78.1329%)
- `tests/support/server.tcl` -> **Severity: 4.027** (Embedded: 0.0466 * Error Risk: 86.4825%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/support/test.tcl` -> **Severity: 3040.6** (Blast Radius: 30.406 * Doc Risk: 100.0%)
- `src/redismodule.h` -> **Severity: 2913.3** (Blast Radius: 29.133 * Doc Risk: 100.0%)
- `tests/support/redis.tcl` -> **Severity: 2847.9** (Blast Radius: 28.479 * Doc Risk: 100.0%)
- `tests/support/server.tcl` -> **Severity: 2044.0** (Blast Radius: 20.44 * Doc Risk: 100.0%)
- `tests/support/util.tcl` -> **Severity: 1742.6** (Blast Radius: 17.426 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2347 literal sites + 20 sites through wrappers = 2367
- **`memory_alloc`:** 108 literal sites + 104 sites through wrappers = 212
- **`panics_and_aborts`:** 1180 literal sites + 4 sites through wrappers = 1184

- `listDelNode` (function, memory_alloc, primitive): 76 call sites in 25 files -- `src/adlist.c`
- `ok` (function, debug_prints, primitive): 7 call sites in 1 files -- `src/intset.c`
- `memtest_progress_end` (function, debug_prints, primitive): 5 call sites in 1 files -- `src/memtest.c`
- `cache_exist` (function, memory_alloc, primitive): 4 call sites in 1 files -- `src/util.c`
- `clusterManagerRemoveNodeFromList` (function, memory_alloc, via listDelNode): 4 call sites in 1 files -- `src/redis-cli.c`
- `all` (function, debug_prints, primitive): 3 call sites in 2 files -- `src/Makefile`
- `removeClientFromMemUsageBucket` (function, memory_alloc, via listDelNode): 3 call sites in 3 files -- `src/server.c`
- `checkOldStyleAof` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/redis-check-aof.c`
- `ldbEnable` (function, memory_alloc, via ldbFlushLog): 2 call sites in 1 files -- `src/eval.c`
- `moduleUnregisterCleanup` (function, memory_alloc, via moduleUnregisterAuthCBs): 2 call sites in 1 files -- `src/module.c`
- `rdbShowGenericInfo` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/redis-check-rdb.c`
- `sentinelSimFailureCrash` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/sentinel.c`
*(+14 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 35414 call pairs -- scoped 22.0%, unique 33.4%, ambiguous 3.1%, external 41.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 31390 | 23.0% | 36.2% | 3.1% | 37.7% |
| tcl | 2902 | 13.3% | 16.8% | 3.9% | 66.1% |
| python | 897 | 19.4% | 0.0% | 1.2% | 79.4% |
| ruby | 140 | 9.3% | 0.0% | 0.0% | 90.7% |
| shell | 74 | 4.1% | 0.0% | 0.0% | 95.9% |
| makefile | 7 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
