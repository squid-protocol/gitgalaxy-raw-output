# ARCHITECTURAL_BRIEF: redis
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/redis/redis` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1648 analyzed artifact(s), 339795 LOC.
- **Load-bearing artifact:** `deps/jemalloc/test/include/test/jemalloc_test.h.in` -- 132 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/server.h` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/redis-cli.c` at magnitude 12117.2 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1648 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 106 |
| Total LOC | 339795 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 94.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.699 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3206 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2673 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 52 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 748 | 239665 | 45.4% |
| JSON | 423 | 27047 | 25.7% |
| TCL | 222 | 60640 | 13.5% |
| SHELL | 76 | 1096 | 4.6% |
| PYTHON | 43 | 3564 | 2.6% |
| MARKDOWN | 29 | 0 | 1.8% |
| PLAINTEXT | 23 | 1 | 1.4% |
| MAKEFILE | 22 | 2616 | 1.3% |
| LUA | 19 | 363 | 1.2% |
| CPP | 12 | 458 | 0.7% |
| M4 | 8 | 2888 | 0.5% |
| RUBY | 8 | 464 | 0.5% |
| XML | 5 | 1 | 0.3% |
| HTML | 4 | 811 | 0.2% |
| YAML | 2 | 34 | 0.1% |
| CSS | 2 | 91 | 0.1% |
| BATCH | 1 | 26 | 0.1% |
| JAVASCRIPT | 1 | 30 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.037`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.04; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Declarative / Non-Code 21%, Large Core Modules (3) 11%, Encapsulated Accessors Files 8%, Parameter Forwarders Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1595 | 96.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 51 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 106*

**Composition by Extension & Reason:**
- `no_extension`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 16793 LOC)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rdb`: 8x Excluded (Unsupported Extension: '.rdb')
- `.md`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 6x Excluded (Unsupported Extension: '.conf')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 233 LOC), 1x Excluded (Embedded Array/Matrix Payload: 1785 commas in 584 LOC), 1x Excluded (Embedded Array/Matrix Payload: 16385 commas in 837 LOC)
- `.vcxproj`: 4x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 4x Excluded (Unsupported Extension: '.filters')
- `.acl`: 3x Excluded (Unsupported Extension: '.acl')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 1x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 5724 LOC)
- `.sln`: 2x Excluded (Unsupported Extension: '.sln')
- `.sup`: 2x Unsupported Format (.sup)
- `.tcl`: 1x Excluded (Machine-Generated Source Code Signature: 161 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3920 LOC)
- `.service`: 2x Unsupported Format (.service)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 20.7 | 6.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 41.9 | 47.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.0 | 0.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 89.1 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 65.4 | 2.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 98088 | 741 | 120 | `src/module.c` |
| cleanup | 1165 | 230 | 1 | `tests/unit/type/list.tcl` |
| guards | 23557 | 880 | 37 | `deps/jemalloc/src/ctl.c` |
| danger | 4700 | 506 | 7 | `src/redis-cli.c` |
| concurrency | 1298 | 186 | 1 | `tests/unit/type/stream-cgroups.tcl` |
| connectivity | 13662 | 822 | 19 | `src/server.h` |
| io | 1800 | 207 | 1 | `deps/lua/doc/contents.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 239 | 51 | 0 | `src/server.c` |
| time | 169 | 53 | 0 | `src/server.h` |
| serialization | 2 | 2 | 0 | `modules/Makefile` |
| regex | 87 | 21 | 0 | `utils/generate-module-api-doc.rb` |
| events | 605 | 85 | 0 | `src/t_zset.c` |
| tests | 834 | 116 | 0 | `tests/unit/functions.tcl` |
| docs | 822 | 111 | 0 | `deps/xxhash/xxhash.h` |
| debt | 2804 | 316 | 3 | `src/redis-cli.c` |
| mutation | 77759 | 946 | 109 | `src/redis-cli.c` |
| dead_code | 2935 | 522 | 3 | `src/module.c` |
| credential | 5 | 4 | 0 | `deps/lua/doc/contents.html` |
| threat | 2895 | 332 | 3 | `deps/jemalloc/src/ctl.c` |
| ml_ai | 1415 | 210 | 1 | `tests/unit/type/hash-field-expire.tcl` |
| ui | 128 | 13 | 0 | `deps/lua/doc/lua.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4536**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `deps/lua/doc/contents.html` (Hits: 728)
- `utils/install_server.sh` (Hits: 44)
- `deps/xxhash/Makefile` (Hits: 33)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **jemalloc_test.h.in** (`deps/jemalloc/test/include/test/jemalloc_test.h.in`) — 132 inbound connections
2. **assert.h** (`deps/jemalloc/include/jemalloc/internal/assert.h`) — 76 inbound connections
3. **server.h** (`src/server.h`) — 73 inbound connections
4. **jemalloc_preamble.h.in** (`deps/jemalloc/include/jemalloc/internal/jemalloc_preamble.h.in`) — 65 inbound connections
5. **jemalloc_internal_includes.h** (`deps/jemalloc/include/jemalloc/internal/jemalloc_internal_includes.h`) — 61 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **server.h** (`src/server.h`) — 51 outbound dependencies
2. **server.c** (`src/server.c`) — 46 outbound dependencies
3. **jemalloc_test.h.in** (`deps/jemalloc/test/include/test/jemalloc_test.h.in`) — 43 outbound dependencies
4. **redis-cli.c** (`src/redis-cli.c`) — 34 outbound dependencies
5. **jemalloc_internal_decls.h** (`deps/jemalloc/include/jemalloc/internal/jemalloc_internal_decls.h`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `rdbLoadObject` **(Many-Argument Workhorses)** (@ `src/rdb.c`) -> Impact: **795.6** | LOC: 1313
  * *Intent:* /* Load a Redis object of the specified type from the specified file. * On success a newly allocated object is returned, otherwise NULL. * * error - W...
- `parseOptions` **(Many-Argument Workhorses)** (@ `src/redis-cli.c`) -> Impact: **583.8** | LOC: 418
  * *Intent:* /*------------------------------------------------------------------------------ * User interface *---------------------------------------------------...
- `parser_tokenize` **(Compute Cores)** (@ `deps/jemalloc/test/unit/stats_print.c`) -> Impact: **562.4** | LOC: 557
- `debugCommand` **(Many-Argument Workhorses)** (@ `src/debug.c`) -> Impact: **492.6** | LOC: 772
  * *Intent:* #endif
- `quicklistTest` **(Many-Argument Workhorses)** (@ `src/quicklist.c`) -> Impact: **420.0** | LOC: 1240
  * *Intent:* /* main test, but callable from other files */
- `malloc_conf_init_helper` **(Many-Argument Workhorses)** (@ `deps/jemalloc/src/jemalloc.c`) -> Impact: **373.8** | LOC: 666
- `clientCommand` **(Compute Cores)** (@ `src/networking.c`) -> Impact: **343.4** | LOC: 560
- `genRedisInfoString` **(Many-Argument Workhorses)** (@ `src/server.c`) -> Impact: **324.9** | LOC: 739
  * *Intent:* /* Create the string returned by the INFO command. This is decoupled * by the INFO command itself as we need to report the same information * on memor...
- `crashlog_from_file` **(Compute Cores)** (@ `tests/support/util.tcl`) -> Impact: **306.7** | LOC: 1241
  * *Intent:* # Return all log lines starting with the first line that contains a warning. # Generally, this will be an assertion error with a stack trace.
- `rdbLoadRioWithLoadingCtx` **(Many-Argument Workhorses)** (@ `src/rdb.c`) -> Impact: **301.6** | LOC: 397
  * *Intent:* /* Load an RDB file from the rio stream 'rdb'. On success C_OK is returned, * otherwise C_ERR is returned. * The rdb_loading_ctx argument holds object...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 201 | 143265.84 | 47.83% | 26.83% |
| `deps/jemalloc/src` | 65 | 19368.7 | 36.35% | 56.09% |
| `deps/lua/src` | 64 | 14045.76 | 50.93% | 5.34% |
| `src/commands` | 424 | 11856.52 | 0.0% | 0.0% |
| `tests/unit` | 47 | 10424.48 | 28.18% | 0.0% |
| `deps/jemalloc/test/unit` | 134 | 10392.4 | 14.4% | 0.0% |
| `tests/modules` | 46 | 8503.66 | 18.72% | 0.0% |
| `deps/hiredis` | 35 | 8154.76 | 31.02% | 15.39% |
| `deps/jemalloc/include/jemalloc/internal` | 123 | 7892.42 | 15.15% | 1.17% |
| `modules/vector-sets` | 14 | 6738.92 | 42.73% | 16.72% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `deps/hiredis/alloc.c` -> **99.9996%** Exposure
- `deps/jemalloc/src/peak_event.c` -> **99.9989%** Exposure
- `src/connection.c` -> **99.9972%** Exposure
- `deps/jemalloc/src/bin.c` -> **99.9864%** Exposure
- `deps/lua/src/strbuf.c` -> **99.8703%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/Makefile` -> **100.0%** Exposure
- `deps/fpconv/fpconv_dtoa.c` -> **100.0%** Exposure
- `deps/hiredis/adapters/ae.h` -> **100.0%** Exposure
- `deps/hiredis/adapters/poll.h` -> **100.0%** Exposure
- `deps/hiredis/async.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/module.c` -> **414** Orphaned Functions | **0** Duplicates
- `deps/jemalloc/src/ctl.c` -> **77** Orphaned Functions | **0** Duplicates
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
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3241` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/redis-cli.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 12117.2 | **LOC:** 11143 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (81.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseOptions` **(Many-Argument Workhorses)** (Impact: 583.8)
    * *Intent:* /*------------------------------------------------------------------------------ * User interface *-...
  * `cliSendCommand` **(Many-Argument Workhorses)** (Impact: 238.2)
  * `clusterManagerCommandCreate` **(Many-Argument Workhorses)** (Impact: 149.8)
    * *Intent:* /* Cluster Manager Commands */
  * `clusterManagerFixOpenSlot` **(Many-Argument Workhorses)** (Impact: 141.0)
    * *Intent:* /* Slot 'slot' was found to be in importing or migrating state in one or * more nodes. This function...
  * `clusterManagerNodeLoadInfo` **(Many-Argument Workhorses)** (Impact: 130.6)
    * *Intent:* /* Load node's cluster configuration by calling "CLUSTER NODES" command. * Node's configuration (nam...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 14 instances
* *Amplified Cascading Flux:* 2024 instances
* *High Risk Execution (weighted view):* 112
* *State Mutation (weighted view):* 6369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2782`, `structural_boundaries: 807`, `args: 386`, `func_start: 233`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 126`, `state_mutation: 2321`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 48`, `import: 34`
* *Defense:* `safety: 158`, `immutability_locks: 56`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` adlist.h, ae.h, anet.h, assert.h, cli_commands.h, cli_common.h, connection.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/module.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9521.32 | **LOC:** 15586 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 29.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Guard Balance (formerly Safety Score) (92.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.4%)
- **Documentation Coverage:** 98.4496% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RM_Call` **(Many-Argument Workhorses)** (Impact: 208.4)
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
* *Amplified Cascading Flux:* 1110 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 3535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2007`, `structural_boundaries: 1620`, `args: 1097`, `func_start: 576`, `class_start: 90`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 3`, `state_mutation: 1315`, `dead_code: 8`, `planned_debt: 12`, `fragile_debt: 3`, `unreferenced_by_name: 414`
* *Architecture:* `io: 5`, `api: 620`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 118`, `doc: 10`, `sync_locks: 8`, `immutability_locks: 226`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` call_reply.h, cluster.h, cluster_asm.h, crc16_slottable.h, dlfcn.h, fcntl.h, hdr_histogram.h, monotonic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6083.78 | **LOC:** 8171 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 21.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.7%), Complexity Load (formerly Cognitive Load) (92.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genRedisInfoString` **(Many-Argument Workhorses)** (Impact: 324.9)
    * *Intent:* /* Create the string returned by the INFO command. This is decoupled * by the INFO command itself as...
  * `processCommand` **(Compute Cores)** (Impact: 212.8)
    * *Intent:* /* If this function gets called we already read a whole * command, arguments are in the client argv/...
  * `main` **(Many-Argument Workhorses)** (Impact: 187.1)
    * *Intent:* #endif
  * `serverCron` **(Many-Argument Workhorses)** (Impact: 140.6)
    * *Intent:* * lookup). * - Software watchdog. * - Update some statistic. * - Incremental rehashing of the DBs ha...
  * `call` **(Many-Argument Workhorses)** (Impact: 124.8)
    * *Intent:* * * Note that regardless of the client flags, if CMD_CALL_PROPAGATE_AOF * or CMD_CALL_PROPAGATE_REPL...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 781 instances
* *State Mutation (weighted view):* 2766
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1463`, `structural_boundaries: 657`, `args: 491`, `func_start: 233`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 27`, `state_mutation: 1204`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 44`
* *Architecture:* `io: 16`, `api: 222`, `import: 46`
* *Defense:* `safety: 58`, `doc: 3`, `immutability_locks: 78`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` inet.h, asciilogo.h, atomicvar.h, bio.h, chk.h, cluster.h, cluster_asm.h, cluster_slot_stats.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/t_zset.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5006.52 | **LOC:** 5021 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 36.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Complexity Load (formerly Cognitive Load) (94.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zunionInterDiffGenericCommand` **(Many-Argument Workhorses)** (Impact: 245.4)
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
* *Structure:* `branch: 1092`, `structural_boundaries: 437`, `args: 182`, `func_start: 159`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 714`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `api: 123`, `import: 6`
* *Defense:* `safety: 58`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` assert.h, fast_float_strtod.h, intset.h, math.h, server.h, testhelp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/auth.json` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/networking.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4780.04 | **LOC:** 5784 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.3%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clientCommand` **(Compute Cores)** (Impact: 343.4)
  * `processMultibulkBuffer` **(Many-Argument Workhorses)** (Impact: 84.9)
    * *Intent:* /* Process the query buffer for client 'c', setting up the client argument * vector for command exec...
  * `catClientInfoString` **(Many-Argument Workhorses)** (Impact: 79.8)
    * *Intent:* /* Concatenate a string representing the state of a client in a human * readable format, into the sd...
  * `processInputBuffer` **(Compute Cores)** (Impact: 79.4)
    * *Intent:* /* This function is called every time, in the client structure 'c', there is * more query buffer to ...
  * `afterErrorReply` **(Many-Argument Workhorses)** (Impact: 78.6)
    * *Intent:* /* Do some actions after an error reply was sent (Log if needed, updates stats, etc.) * Possible fla...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 636 instances
* *State Mutation (weighted view):* 2067
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1199`, `structural_boundaries: 480`, `args: 254`, `func_start: 189`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 795`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 51`
* *Architecture:* `api: 154`, `import: 14`
* *Defense:* `safety: 95`, `immutability_locks: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` atomicvar.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, connection.h, ctype.h, fmtargs.h, fpconv_dtoa.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cluster_legacy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4657.34 | **LOC:** 6582 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clusterCommandSpecial` **(Compute Cores)** (Impact: 242.6)
  * `clusterProcessPacket` **(Compute Cores)** (Impact: 231.2)
    * *Intent:* /* When this function is called, there is a packet to process starting * at link->rcvbuf. Releasing ...
  * `clusterLoadConfig` **(Many-Argument Workhorses)** (Impact: 162.2)
    * *Intent:* /* ----------------------------------------------------------------------------- * Initialization * ...
  * `clusterUpdateSlotsConfigWith` **(Many-Argument Workhorses)** (Impact: 80.3)
    * *Intent:* /* This function is called when we receive a master configuration via a * PING, PONG or UPDATE packe...
  * `clusterGenNodeDescription` **(Many-Argument Workhorses)** (Impact: 72.8)
    * *Intent:* /* Generate a csv-alike representation of the specified cluster node. * See clusterGenNodesDescripti...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 601 instances
* *State Mutation (weighted view):* 1951
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1204`, `structural_boundaries: 582`, `args: 448`, `func_start: 204`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 9`, `state_mutation: 749`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 52`
* *Architecture:* `io: 5`, `api: 246`, `import: 15`
* *Defense:* `safety: 20`, `immutability_locks: 25`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` inet.h, cluster.h, cluster_asm.h, cluster_legacy.h, cluster_slot_stats.h, connection.h, endianconv.h, fcntl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/t_stream.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4651.9 | **LOC:** 5934 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 29.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `streamReplyWithRange` **(Many-Argument Workhorses)** (Impact: 214.9)
    * *Intent:* * will always pass 'spi' and propagate when a group is passed. * * Note that this function is recurs...
  * `streamParseAddOrTrimArgsOrReply` **(Many-Argument Workhorses)** (Impact: 171.4)
    * *Intent:* /* Parse the arguments of XADD/XTRIM. * * See streamAddTrimArgs for more details about the arguments...
  * `xreadCommand` **(Many-Argument Workhorses)** (Impact: 158.4)
    * *Intent:* /* XREAD [BLOCK <milliseconds>] [COUNT <count>] STREAMS key_1 key_2 ... key_N * ID_1 ID_2 ... ID_N *...
  * `xgroupCommand` **(Compute Cores)** (Impact: 114.3)
    * *Intent:* /* ----------------------------------------------------------------------- * Consumer groups command...
  * `streamAppendItem` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* * but instead the passed ID is used to add the new entry. In this case * adding the entry may fail a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 611 instances
* *State Mutation (weighted view):* 1989
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1121`, `structural_boundaries: 434`, `args: 159`, `func_start: 116`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 767`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 109`, `import: 5`
* *Defense:* `safety: 71`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` endianconv.h, server.h, stream.h, string.h, xxhash.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/rdb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4533.66 | **LOC:** 4540 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.3%), Guard Balance (formerly Safety Score) (95.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rdbLoadObject` **(Many-Argument Workhorses)** (Impact: 795.6)
    * *Intent:* /* Load a Redis object of the specified type from the specified file. * On success a newly allocated...
  * `rdbLoadRioWithLoadingCtx` **(Many-Argument Workhorses)** (Impact: 301.6)
    * *Intent:* /* Load an RDB file from the rio stream 'rdb'. On success C_OK is returned, * otherwise C_ERR is ret...
  * `rdbSaveObject` **(Many-Argument Workhorses)** (Impact: 242.1)
    * *Intent:* /* Save a Redis object. * Returns -1 on error, number of bytes written on success. */
  * `rdbSaveToSlavesSockets` **(Many-Argument Workhorses)** (Impact: 73.9)
    * *Intent:* /* Spawn an RDB child that writes the RDB to the sockets of the slaves * that are currently in SLAVE...
  * `rdbGenericLoadStringObjectUsable` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* /* Load a string object from an RDB file according to flags: * * RDB_LOAD_NONE (no flags): load an R...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 572 instances
* *State Mutation (weighted view):* 1762
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1043`, `structural_boundaries: 459`, `args: 183`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 5`, `state_mutation: 618`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `io: 7`, `api: 83`, `import: 20`
* *Defense:* `safety: 57`, `immutability_locks: 6`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` inet.h, bio.h, cluster_asm.h, endianconv.h, fcntl.h, fpconv_dtoa.h, functions.h, intset.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentinel.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4527.9 | **LOC:** 5475 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sentinelCommand` **(Compute Cores)** (Impact: 200.0)
  * `sentinelHandleConfiguration` **(Compute Cores)** (Impact: 195.4)
  * `sentinelRefreshInstanceInfo` **(Many-Argument Workhorses)** (Impact: 158.3)
    * *Intent:* /* Process the INFO output from masters. */
  * `sentinelSetDebugConfigParameters` **(Compute Cores)** (Impact: 107.6)
  * `sentinelSetCommand` **(Compute Cores)** (Impact: 104.8)
    * *Intent:* /* SENTINEL SET <mastername> [<option> <value> ...] */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 649 instances
* *State Mutation (weighted view):* 2106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1137`, `structural_boundaries: 413`, `args: 238`, `func_start: 125`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 6`, `state_mutation: 808`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 152`, `import: 10`
* *Defense:* `safety: 4`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` inet.h, async.h, ctype.h, fcntl.h, hiredis.h, hiredis_ssl.h, ssl.h, server.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/replication.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3389.12 | **LOC:** 5410 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSyncBulkPayload` **(Many-Argument Workhorses)** (Impact: 132.6)
    * *Intent:* /* Asynchronously read the SYNC payload we receive from a master */ #define REPL_MAX_WRITTEN_BEFORE_...
  * `syncWithMaster` **(Compute Cores)** (Impact: 121.3)
    * *Intent:* /* This handler fires when the non blocking connect was able to * establish a connection with the ma...
  * `replconfCommand` **(Compute Cores)** (Impact: 112.2)
    * *Intent:* * Unlike other subcommands, this is used by master to get the replication * offset from a replica. *...
  * `syncCommand` **(Compute Cores)** (Impact: 97.2)
    * *Intent:* /* SYNC and PSYNC command implementation. */
  * `slaveTryPartialResynchronization` **(Many-Argument Workhorses)** (Impact: 63.1)
    * *Intent:* * 1) As a side effect of the function call the function removes the readable * event handler from "f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 459 instances
* *State Mutation (weighted view):* 1497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 917`, `structural_boundaries: 421`, `args: 316`, `func_start: 113`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 579`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 23`
* *Architecture:* `io: 8`, `api: 101`, `import: 13`
* *Defense:* `safety: 35`, `doc: 1`, `immutability_locks: 5`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` bio.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, connection.h, fcntl.h, functions.h, memory.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/t_hash.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3355.78 | **LOC:** 4094 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 27.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%)
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
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 490`, `dead_code: 6`, `unreferenced_by_name: 35`
* *Architecture:* `api: 84`, `import: 6`
* *Defense:* `safety: 50`, `doc: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` cluster_asm.h, ebuckets.h, entry.h, math.h, redisassert.h, server.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/db.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3182.86 | **LOC:** 3915 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 19.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.3%), Complexity Load (formerly Cognitive Load) (93.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.7%)
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
* *Structure:* `branch: 712`, `structural_boundaries: 333`, `args: 169`, `func_start: 135`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 438`, `dead_code: 6`, `planned_debt: 5`, `unreferenced_by_name: 57`
* *Architecture:* `api: 128`, `import: 12`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` atomicvar.h, bio.h, cluster.h, cluster_asm.h, ctype.h, functions.h, keymeta.h, latency.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/jemalloc/src/jemalloc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2986.9 | **LOC:** 4540 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `malloc_conf_init_helper` **(Many-Argument Workhorses)** (Impact: 373.8)
  * `malloc_conf_next` **(Many-Argument Workhorses)** (Impact: 190.0)
  * `batch_alloc` **(Many-Argument Workhorses)** (Impact: 79.8)
  * `imalloc_body` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `isfree` **(Many-Argument Workhorses)** (Impact: 52.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 320 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 1027
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 734`, `structural_boundaries: 798`, `args: 204`, `func_start: 116`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 12`, `state_mutation: 387`, `fragile_debt: 2`, `unreferenced_by_name: 31`
* *Architecture:* `api: 90`, `import: 26`
* *Defense:* `safety: 299`, `doc: 10`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` features.h, assert.h, atomic.h, buf_writer.h, ctl.h, emap.h, extent_dss.h, extent_mmap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/config.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2881.76 | **LOC:** 3777 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadServerConfigFromString` **(Compute Cores)** (Impact: 90.8)
  * `configSetCommand` **(Compute Cores)** (Impact: 56.6)
    * *Intent:* /*----------------------------------------------------------------------------- * CONFIG SET impleme...
  * `rewriteConfigReadOldFile` **(Compute Cores)** (Impact: 47.7)
    * *Intent:* /* Read the old file, split it into lines to populate a newly created * config rewrite state, and re...
  * `numericParseString` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `setNumericType` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* /* Gets a 'long long val' and sets it into the union, using a macro to get * compile time type check...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 385 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 687`, `structural_boundaries: 406`, `args: 194`, `func_start: 151`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 430`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 27`
* *Architecture:* `io: 7`, `api: 87`, `import: 10`
* *Defense:* `safety: 24`, `immutability_locks: 121`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bio.h, cluster.h, connection.h, ctype.h, fcntl.h, glob.h, locale.h, server.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/listpack.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2801.78 | **LOC:** 3335 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Guard Balance (formerly Safety Score) (91.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listpackTest` **(Many-Argument Workhorses)** (Impact: 253.0)
  * `lpInsert` **(Many-Argument Workhorses)** (Impact: 100.7)
    * *Intent:* * or replace with a string, which is stored in the 'elestr' buffer. * * Returns NULL on out of memor...
  * `lpGetWithSize` **(Many-Argument Workhorses)** (Impact: 76.0)
    * *Intent:* * * If 'entry_size' is not NULL, *entry_size is set to the entry length of the * listpack element po...
  * `lpEncodeIntegerGetType` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* /* Stores the integer encoded representation of 'v' in the 'intenc' buffer. */
  * `lpBatchInsert` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* * and 'sval' and 'slen' will be used. Otherwise, 'lval' will be used to append * the integer entry. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 415 instances
* *State Mutation (weighted view):* 1443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 219`, `args: 94`, `func_start: 73`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 613`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 9`, `unreferenced_by_name: 11`
* *Architecture:* `io: 3`, `api: 49`, `import: 14`
* *Defense:* `safety: 220`, `test: 64`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` adlist.h, limits.h, listpack.h, listpack_malloc.h, redisassert.h, sds.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cluster_asm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2620.92 | **LOC:** 3810 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 29.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.2%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.2157% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clusterSyncSlotsCommand` **(Compute Cores)** (Impact: 171.5)
  * `slotSnapshotSaveRio` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* /* Save the slot ranges snapshot to the file. It generates the DUMP encoded * representation of each...
  * `asmSyncWithSource` **(Compute Cores)** (Impact: 49.0)
  * `asmTaskStateToString` **(Compute Cores)** (Impact: 43.0)
  * `asmReplicaHandleMasterTask` **(Compute Cores)** (Impact: 40.2)
    * *Intent:* /* The replicas handle the master import ASM task information. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 292 instances
* *State Mutation (weighted view):* 982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 772`, `structural_boundaries: 426`, `args: 228`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 398`, `planned_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 111`, `import: 6`
* *Defense:* `safety: 16`, `doc: 2`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bio.h, cluster.h, cluster_asm.h, cluster_slot_stats.h, functions.h, server.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/quicklist.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2572.44 | **LOC:** 3659 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quicklistTest` **(Many-Argument Workhorses)** (Impact: 420.0)
    * *Intent:* /* main test, but callable from other files */
  * `_quicklistInsert` **(Many-Argument Workhorses)** (Impact: 119.9)
    * *Intent:* /* Insert a new entry before or after existing entry 'entry'. * * If after==1, the new value is inse...
  * `quicklistPopCustom` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* /* pop from quicklist and return result in 'data' ptr. Value of 'data' * is the return value of 'sav...
  * `quicklistDelRange` **(Many-Argument Workhorses)** (Impact: 50.3)
    * *Intent:* /* Delete a range of elements from the quicklist. * * elements may span across multiple quicklistNod...
  * `quicklistReplaceEntry` **(Many-Argument Workhorses)** (Impact: 39.1)
    * *Intent:* /* Replace quicklist entry by 'data' with length 'sz'. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 346 instances
* *State Mutation (weighted view):* 1143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 157`, `args: 92`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 451`, `dead_code: 5`, `unreferenced_by_name: 10`
* *Architecture:* `api: 64`, `import: 14`
* *Defense:* `safety: 161`, `test: 42`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` config.h, limits.h, listpack.h, lzf.h, quicklist.h, redisassert.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/vector-sets/hnsw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2558.5 | **LOC:** 3300 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.6%)
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
* *Structure:* `branch: 502`, `structural_boundaries: 264`, `args: 97`, `func_start: 71`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 419`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 23`
* *Architecture:* `api: 71`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` assert.h, float.h, hnsw.h, immintrin.h, math.h, mixer.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/jemalloc/src/ctl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 2485.68 | **LOC:** 4415 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.9%), Guard Balance (formerly Safety Score) (57.2%), Debt Markers (formerly Tech Debt) (42.0%)
- **Documentation Coverage:** 93.5185% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ctl_lookup` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `ctl_arena_stats_sdmerge` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `arena_i_dss_ctl` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `experimental_arenas_i_pactivep_ctl` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `arena_i_decay_ms_ctl_impl` **(Many-Argument Workhorses)** (Impact: 35.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 333 instances
* *State Mutation (weighted view):* 1055
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 424`, `structural_boundaries: 475`, `args: 128`, `func_start: 103`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 389`, `unreferenced_by_name: 77`
* *Architecture:* `api: 14`, `import: 18`
* *Defense:* `safety: 474`, `doc: 16`, `immutability_locks: 213`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` assert.h, ctl.h, extent_dss.h, extent_mmap.h, inspect.h, jemalloc_internal_includes.h, jemalloc_preamble.h, mutex.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/acl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2477.64 | **LOC:** 3314 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aclCommand` **(Compute Cores)** (Impact: 170.6)
    * *Intent:* /* ACL -- show and modify the configuration of ACL users. * ACL HELP * ACL LOAD * ACL SAVE * ACL LIS...
  * `ACLSetSelector` **(Many-Argument Workhorses)** (Impact: 138.8)
    * *Intent:* * It is possible to specify multiple patterns. * %R~<pattern> Add key read pattern that specifies wh...
  * `ACLSetUser` **(Many-Argument Workhorses)** (Impact: 90.8)
    * *Intent:* * When an error is returned, errno is set to the following values: * * EINVAL: The specified opcode ...
  * `ACLSelectorCheckCmd` **(Many-Argument Workhorses)** (Impact: 64.3)
    * *Intent:* /* Check if the command is ready to be executed according to the * ACLs associated with the specifie...
  * `ACLLoadFromFile` **(Compute Cores)** (Impact: 60.6)
    * *Intent:* * also allowed. * * One important part of implementing ACL LOAD, that uses this function, is * to av...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 312 instances
* *State Mutation (weighted view):* 975
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 607`, `structural_boundaries: 315`, `args: 161`, `func_start: 96`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 3`, `state_mutation: 351`, `dead_code: 2`, `unreferenced_by_name: 16`
* *Architecture:* `io: 4`, `api: 102`, `import: 5`
* *Defense:* `safety: 20`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cluster.h, ctype.h, fcntl.h, server.h, sha256.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bitops.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2461.0 | **LOC:** 2196 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bitopCommand` **(Compute Cores)** (Impact: 184.5)
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
* *Structure:* `branch: 476`, `structural_boundaries: 138`, `args: 39`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 540`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 12`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` arm_neon.h, ctype.h, immintrin.h, server.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/redis-benchmark.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2345.76 | **LOC:** 2044 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseOptions` **(Many-Argument Workhorses)** (Impact: 257.4)
    * *Intent:* /* Returns number of consumed options. */
  * `main` **(Many-Argument Workhorses)** (Impact: 139.6)
  * `createClient` **(Many-Argument Workhorses)** (Impact: 103.3)
    * *Intent:* * Also an initial SELECT command is prepended in order to make sure the right * database is selected...
  * `readHandler` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `fetchClusterConfiguration` **(I/O & Config Routines)** (Impact: 58.2)
    * *Intent:* /* TODO: This should be refactored to use CLUSTER SLOTS, the migrating/importing * information is an...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 24 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 409 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 24
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 141`, `args: 68`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 20`, `state_mutation: 474`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 4`, `import: 27`
* *Defense:* `safety: 28`, `sync_locks: 3`, `immutability_locks: 48`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` adlist.h, ae.h, assert.h, atomicvar.h, cli_common.h, crc16_slottable.h, dict.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/aof.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2155.06 | **LOC:** 2970 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.352; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rewriteStreamObject` **(Many-Argument Workhorses)** (Impact: 120.7)
    * *Intent:* /* Emit the commands needed to rebuild a stream object. * The function returns 0 on error, 1 on succ...
  * `loadSingleAppendOnlyFile` **(Compute Cores)** (Impact: 95.3)
    * *Intent:* /* Replay an append log file. On success AOF_OK or AOF_TRUNCATED is returned, * otherwise, one of th...
  * `flushAppendOnlyFile` **(Compute Cores)** (Impact: 81.2)
    * *Intent:* * buffer and write it on disk using this function just before entering * the event loop again. * * A...
  * `rewriteObject` **(Stateful Encapsulated Methods)** (Impact: 75.4)
  * `aofLoadManifestFromFile` **(Compute Cores)** (Impact: 63.1)
    * *Intent:* /* Generic manifest loading function, used in `aofLoadManifestFromDisk` and redis-check-aof tool. */...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 271 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 224`, `args: 180`, `func_start: 72`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 13`, `state_mutation: 334`, `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 18`, `api: 78`, `import: 13`
* *Defense:* `safety: 18`, `immutability_locks: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.352
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bio.h, cluster_asm.h, fcntl.h, functions.h, rio.h, server.h, signal.h, param.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/xxhash/xxhash.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2131.92 | **LOC:** 7489 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **18**; blast radius 1.084; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.4%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 84.8684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `XXH32_finalize` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* * @internal * @brief Processes the last 0-15 bytes of @p ptr. * * There may be up to 15 bytes remain...
  * `XXH3_update` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* #ifndef XXH3_STREAM_USE_STACK # if XXH_SIZE_OPT <= 0 && !defined(__clang__) /* clang doesn't need ad...
  * `XXH3_accumulate_sve` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `XXH3_generateSecret` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* /*! @ingroup XXH3_family */
  * `XXH_mult64to128` **(Many-Argument Workhorses)** (Impact: 25.2)
    * *Intent:* * and perform a full 64x64 multiply -- entirely redundant on 32-bit. */ # define XXH_mult32to64(x, y...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 222 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 627`, `structural_boundaries: 522`, `args: 523`, `func_start: 172`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 342`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 29`
* *Architecture:* `api: 232`, `import: 27`
* *Defense:* `safety: 212`, `doc: 359`, `immutability_locks: 582`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.016921
  * `Imports (Out-Degree: 2):` altivec.h, arm_neon.h, arm_sve.h, assert.h, emmintrin.h, immintrin.h, intrin.h, inttypes.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/server.c` -> Churn: **90.61%** | Cog Load: 92.1671% | Debt: 22.3119%
- `src/db.c` -> Churn: **85.72%** | Cog Load: 93.5421% | Debt: 78.1896%
- `src/module.c` -> Churn: **82.42%** | Cog Load: 74.7994% | Debt: 99.5432%
- `src/rdb.c` -> Churn: **80.59%** | Cog Load: 97.3019% | Debt: 15.6269%
- `src/t_stream.c` -> Churn: **79.62%** | Cog Load: 94.6711% | Debt: 22.27%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/quicklist.c` -> **Slavomir Kaslev** (100.0% isolated ownership) | Magnitude: 2572.44
- `src/redis-benchmark.c` -> **h.o.t. neglected** (100.0% isolated ownership) | Magnitude: 2345.76
- `deps/xxhash/xxhash.h` -> **Mincho Paskalev** (100.0% isolated ownership) | Magnitude: 2131.92
- `src/ziplist.c` -> **zzj** (100.0% isolated ownership) | Magnitude: 2005.28
- `src/eval.c` -> **Ozan Tezcan** (100.0% isolated ownership) | Magnitude: 1430.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `deps/jemalloc/include/jemalloc/internal/mutex.h` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 99.3568%)
- `deps/jemalloc/include/jemalloc/internal/arena_inlines_b.h` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 92.3436%)
- `deps/jemalloc/include/jemalloc/internal/jemalloc_internal_inlines_c.h` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 99.3998%)
- `deps/jemalloc/include/jemalloc/internal/tcache_inlines.h` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 98.9261%)
- `deps/jemalloc/include/jemalloc/internal/rtree.h` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 99.8202%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `deps/jemalloc/test/include/test/math.h` -> **Severity: 8.955** (Embedded: 0.0899 * Error Risk: 99.6599%)
- `deps/jemalloc/include/msvc_compat/C99/stdint.h` -> **Severity: 5.694** (Embedded: 0.1019 * Error Risk: 55.9026%)
- `deps/jemalloc/include/jemalloc/internal/jemalloc_internal_types.h` -> **Severity: 4.656** (Embedded: 0.0701 * Error Risk: 66.3831%)
- `deps/jemalloc/include/jemalloc/internal/util.h` -> **Severity: 4.537** (Embedded: 0.0881 * Error Risk: 51.4702%)
- `deps/jemalloc/test/include/test/jemalloc_test.h.in` -> **Severity: 4.4** (Embedded: 0.08 * Error Risk: 54.9834%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/redismodule.h` -> **Severity: 1285.7** (Blast Radius: 12.857 * Doc Risk: 100.0%)
- `deps/jemalloc/test/include/test/math.h` -> **Severity: 1171.3** (Blast Radius: 11.713 * Doc Risk: 100.0%)
- `deps/jemalloc/include/jemalloc/internal/util.h` -> **Severity: 1035.0** (Blast Radius: 10.35 * Doc Risk: 100.0%)
- `src/server.h` -> **Severity: 1025.7** (Blast Radius: 10.257 * Doc Risk: 100.0%)
- `deps/jemalloc/include/jemalloc/internal/malloc_io.h` -> **Severity: 958.2** (Blast Radius: 9.582 * Doc Risk: 100.0%)

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
