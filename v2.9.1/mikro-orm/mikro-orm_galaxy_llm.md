# ARCHITECTURAL_BRIEF: mikro-orm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mikro-orm/mikro-orm.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1694 analyzed artifact(s), 202719 LOC.
- **Load-bearing artifact:** `tests/features/reflection/entities-compiled/index.js` -- 100 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/core/src/EntityManager.ts` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/features/entity-manager/EntityManager.mssql.test.ts` at magnitude 12128.1 (structural weight, not risk).
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
| Total Artifacts | 2384 |
| Analyzed Artifacts (Scanned) | 1694 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 690 |
| Total LOC | 202719 |
| Volatility Index | 0.021 |
| % Scanned of codebase = | 71.1% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5848 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.527 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8837 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1551 | 201042 | 91.6% |
| JSON | 63 | 605 | 3.7% |
| MARKDOWN | 38 | 0 | 2.2% |
| PLAINTEXT | 22 | 0 | 1.3% |
| JAVASCRIPT | 15 | 628 | 0.9% |
| SQLITE | 3 | 284 | 0.2% |
| YAML | 1 | 120 | 0.1% |
| DB2_SQL | 1 | 40 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.808`
> **Composition Archetype:** `Mid Flat Project` (z +2.81; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 42%, State Mutators Files 14%, Data / Markup / Trivial 10%, Large Core Modules (3) 7%, Callbacks & Closures Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1634 | 96.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 60 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 690*

**Composition by Extension & Reason:**
- `.md`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4853 LOC), 1x Excluded (Machine-Generated Source Code Signature: 106 LOC)
- `.snap`: 175x Excluded (Unsupported Extension: '.snap')
- `.html`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 15x Unsupported Format (.undeterminable), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 191 LOC)
- `.js`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 19x Excluded (Explicitly Denied Extension: '.jpg')
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.css`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.lock')
- `.patch`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.9 | 24.1 | 17.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 46.6 | 52.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 73.0 | 100.0 | 100.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.9 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.0 | 0.5 | 0.4 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 83.4 | 11.3 | 11.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1920 | 265 | 2 | `packages/sql/src/AbstractSqlDriver.ts` |
| cleanup | 1470 | 1085 | 1 | `tests/features/table-per-type-inheritance/table-per-type-inheritance.test.ts` |
| guards | 5347 | 579 | 6 | `packages/sql/src/query/QueryBuilder.ts` |
| danger | 4942 | 531 | 6 | `packages/sql/src/AbstractSqlDriver.ts` |
| concurrency | 24377 | 1227 | 28 | `tests/features/entity-manager/EntityManager.postgre.test.ts` |
| connectivity | 3221 | 626 | 5 | `packages/core/src/typings.ts` |
| io | 2836 | 372 | 3 | `packages/sql/src/query/QueryBuilder.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 5 | 0 | `tests/features/table-per-type-inheritance/table-per-type-inheritance.test.ts` |
| time | 709 | 193 | 1 | `tests/features/mikro-kysely-plugin.test.ts` |
| serialization | 92 | 49 | 0 | `packages/core/src/utils/DataloaderUtils.ts` |
| regex | 459 | 117 | 0 | `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` |
| events | 2045 | 265 | 2 | `tests/features/entity-manager/EntityManager.mysql.test.ts` |
| tests | 29255 | 1101 | 39 | `tests/features/entity-manager/EntityManager.postgre.test.ts` |
| docs | 2415 | 284 | 1 | `packages/core/src/typings.ts` |
| debt | 242 | 87 | 0 | `tests/defineEntity.test.ts` |
| mutation | 39154 | 1441 | 47 | `tests/features/entity-manager/EntityManager.mysql.test.ts` |
| dead_code | 729 | 342 | 1 | `packages/core/src/utils/Utils.ts` |
| credential | 3 | 3 | 0 | `tests/Connection.test.ts` |
| threat | 641 | 150 | 0 | `tests/features/migrations/Migrator.test.ts` |
| ml_ai | 191 | 49 | 0 | `tests/features/query-builder/query-builder-select.test.ts` |
| ui | 173 | 49 | 0 | `packages/core/src/EntityManager.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **1.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/sql/src/query/QueryBuilder.ts` (Hits: 102)
- `packages/sql/src/query/QueryBuilderHelper.ts` (Hits: 87)
- `packages/sql/src/AbstractSqlDriver.ts` (Hits: 75)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`tests/features/reflection/entities-compiled/index.js`) — 100 inbound connections
2. **Book.js** (`tests/features/reflection/entities-compiled/Book.js`) — 25 inbound connections
3. **fs-utils.ts** (`packages/core/src/utils/fs-utils.ts`) — 24 inbound connections
4. **seeder.ts** (`tests/perf/serializing-nested-entities/seeder.ts`) — 19 inbound connections
5. **BaseEntity.js** (`tests/features/reflection/entities-compiled/BaseEntity.js`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **EntityManager.ts** (`packages/core/src/EntityManager.ts`) — 29 outbound dependencies
2. **Configuration.ts** (`packages/core/src/utils/Configuration.ts`) — 28 outbound dependencies
3. **typings.ts** (`packages/core/src/typings.ts`) — 26 outbound dependencies
4. **index.ts** (`packages/core/src/types/index.ts`) — 25 outbound dependencies
5. **bootstrap.ts** (`tests/bootstrap.ts`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `diffForeignKey` **(Many-Argument Workhorses)** (@ `packages/sql/src/schema/SchemaComparator.ts`) -> Impact: **404.9** | LOC: 417
- `isSimpleRegExp` **(Many-Argument Workhorses)** (@ `packages/sql/src/query/QueryBuilderHelper.ts`) -> Impact: **395.6** | LOC: 983
  * *Intent:* /** * Checks whether the RE can be rewritten to simple LIKE query */
- `getTableKey` **(Compute Cores)** (@ `packages/sql/src/schema/SchemaHelper.ts`) -> Impact: **357.4** | LOC: 841
- `unquote` **(Compute Cores)** (@ `packages/sql/src/schema/SchemaHelper.ts`) -> Impact: **357.4** | LOC: 841
- `getEntityHydrator` **(Many-Argument Workhorses)** (@ `packages/core/src/hydration/ObjectHydrator.ts`) -> Impact: **354.1** | LOC: 482
  * *Intent:* /** */
- `rule` **(Many-Argument Workhorses)** (@ `packages/sql/src/schema/SchemaComparator.ts`) -> Impact: **336.3** | LOC: 387
- `getAllIndexes` **(Many-Argument Workhorses)** (@ `packages/oracledb/src/OracleSchemaHelper.ts`) -> Impact: **326.6** | LOC: 533
- `initCustomType` **(Many-Argument Workhorses)** (@ `packages/core/src/metadata/MetadataDiscovery.ts`) -> Impact: **220.9** | LOC: 169
- `nativeInsertMany` **(Many-Argument Workhorses)** (@ `packages/sql/src/AbstractSqlDriver.ts`) -> Impact: **213.4** | LOC: 199
- `nativeUpdateMany` **(Many-Argument Workhorses)** (@ `packages/sql/src/AbstractSqlDriver.ts`) -> Impact: **189.3** | LOC: 209

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/issues` | 400 | 52552.36 | 27.34% | 0.0% |
| `tests/features/entity-manager` | 7 | 33121.99 | 49.93% | 0.0% |
| `tests/features/schema-generator` | 89 | 16260.41 | 25.37% | 0.0% |
| `tests/features/embeddables` | 89 | 10131.27 | 25.99% | 0.0% |
| `tests/features` | 21 | 6877.6 | 28.89% | 0.0% |
| `tests/features/query-builder` | 13 | 6564.82 | 18.64% | 0.0% |
| `tests` | 33 | 6524.38 | 16.56% | 0.0% |
| `packages/sql/src/query` | 11 | 5619.06 | 30.41% | 0.0% |
| `tests/features/composite-keys` | 22 | 5100.83 | 35.07% | 0.0% |
| `tests/features/multiple-schemas` | 15 | 5092.42 | 25.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/core/src/types/Type.ts` -> **99.9999%** Exposure
- `packages/core/src/entity/BaseEntity.ts` -> **99.974%** Exposure
- `packages/core/src/cache/FileCacheAdapter.ts` -> **99.5554%** Exposure
- `packages/core/src/utils/AbstractSchemaGenerator.ts` -> **97.807%** Exposure
- `packages/sql/src/plugin/index.ts` -> **93.9456%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/core/src/hydration/ObjectHydrator.ts` -> **100.0%** Exposure
- `packages/core/src/logging/DefaultLogger.ts` -> **100.0%** Exposure
- `packages/core/src/metadata/MetadataDiscovery.ts` -> **100.0%** Exposure
- `packages/core/src/utils/AbstractMigrator.ts` -> **100.0%** Exposure
- `packages/core/src/utils/AbstractSchemaGenerator.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/core/src/utils/Utils.ts` -> **41** Orphaned Functions | **0** Duplicates
- `tests/defineEntity.test.ts` -> **8** Orphaned Functions | **25** Duplicates
- `tests/features/decorators/legacy/decorators.test.ts` -> **4** Orphaned Functions | **16** Duplicates
- `tests/features/decorators/es/decorators.sqlite.test.ts` -> **3** Orphaned Functions | **16** Duplicates
- `packages/core/src/types/Type.ts` -> **13** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/database/seeder/user.seeder.ts` -> **99.9995%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3224` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/features/entity-manager/EntityManager.mssql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 12128.1 | **LOC:** 1608 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (33.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 162 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 1119
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 335`, `args: 82`, `func_start: 56`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 143`
* *Architecture:* `io: 5`, `concurrency: 309`, `import: 5`
* *Defense:* `safety: 37`, `test: 435`, `sync_locks: 15`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, index.js, mssql, node:perf_hooks, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.sqlite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 11705.58 | **LOC:** 1813 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (26.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 178 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 1277
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 423`, `args: 98`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 148`
* *Architecture:* `io: 4`, `concurrency: 387`, `import: 8`
* *Defense:* `safety: 32`, `test: 497`, `sync_locks: 15`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, Author4.js, index.js, core, libsql, sql, sqlite, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/query-builder/query-builder.postgres.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3744.87 | **LOC:** 605 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Guard Balance (formerly Safety Score) (27.7%), Complexity Load (formerly Cognitive Load) (12.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 52`, `args: 31`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `io: 11`, `concurrency: 41`, `import: 7`
* *Defense:* `safety: 4`, `test: 109`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BaseEntity2.js, BaseEntity22.js, index.js, core, legacy, postgresql, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/issues/GH234.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3629.2 | **LOC:** 223 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (4.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 109
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 43`, `args: 21`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 2`, `concurrency: 19`, `import: 3`
* *Defense:* `test: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.js, legacy, sqlite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/AbstractSqlDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3330.58 | **LOC:** 3023 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (98.4%), Guard Balance (formerly Safety Score) (92.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 69.5122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nativeInsertMany` **(Many-Argument Workhorses)** (Impact: 213.4)
  * `nativeUpdateMany` **(Many-Argument Workhorses)** (Impact: 189.3)
  * `mapJoinedProps` **(Many-Argument Workhorses)** (Impact: 160.2)
  * `getFieldsForJoinedLoad` **(Many-Argument Workhorses)** (Impact: 156.6)
  * `addParams` **(Many-Argument Workhorses)** (Impact: 127.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 191 instances
* *Concurrency (weighted view):* 186
* *State Mutation (weighted view):* 586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 833`, `structural_boundaries: 497`, `args: 195`, `func_start: 68`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 222`, `state_mutation: 204`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 75`, `api: 13`, `concurrency: 81`, `import: 9`
* *Defense:* `safety: 112`, `doc: 22`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlConnection.js, AbstractSqlPlatform.js, PivotCollectionPersister.js, SqlEntityManager.js, NativeQueryBuilder.js, QueryBuilder.js, enums.js, typings.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/issues/GHx10.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2988.71 | **LOC:** 335 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.5%), Complexity Load (formerly Cognitive Load) (42.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 44`, `args: 18`, `func_start: 3`, `class_start: 5`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `concurrency: 22`, `import: 5`
* *Defense:* `test: 36`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.js, core, legacy, sqlite, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/MetadataDiscovery.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2581.7 | **LOC:** 2429 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.2%)
- **Documentation Coverage:** 78.1609% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initCustomType` **(Many-Argument Workhorses)** (Impact: 220.9)
  * `initColumnType` **(Stateful Encapsulated Methods)** (Impact: 102.5)
  * `initEmbeddables` **(Many-Argument Workhorses)** (Impact: 88.3)
  * `initSingleTableInheritance` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `initPolymorphicRelation` **(Many-Argument Workhorses)** (Impact: 55.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 301 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 956
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 705`, `structural_boundaries: 507`, `args: 205`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 354`, `dead_code: 5`
* *Architecture:* `io: 21`, `api: 10`, `concurrency: 10`, `import: 18`
* *Defense:* `safety: 115`, `doc: 16`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BaseEntity.js, enums.js, errors.js, Logger.js, colors.js, NamingStrategy.js, Platform.js, index.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.mysql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2432.4 | **LOC:** 3205 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (35.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveBook` **(Callbacks & Closures)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 298 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 2029
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 612`, `args: 169`, `func_start: 104`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 301`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `concurrency: 539`, `import: 9`
* *Defense:* `safety: 54`, `test: 879`, `sync_locks: 25`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, index.js, Author2Subscriber.js, EverythingSubscriber.js, FlushSubscriber.js, Test2Subscriber.js, mysql, node:util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2407.0 | **LOC:** 4266 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.3%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.5%)
- **Documentation Coverage:** 45.098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `joinReference` **(Many-Argument Workhorses)** (Impact: 107.5)
  * `prepareFields` **(Many-Argument Workhorses)** (Impact: 101.7)
  * `execute` **(Defensive Guards)** (Impact: 62.0)
    * *Intent:* /** * Executes this QB and returns the raw results, mapped to the property names (unless disabled vi...
  * `resolveNestedPath` **(Defensive Guards)** (Impact: 51.3)
    * *Intent:* /** * Resolves nested paths like `a.books.title` to their actual field references. * Auto-joins rela...
  * `getFieldName` **(Defensive Guards)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 118 instances
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 937`, `structural_boundaries: 963`, `args: 265`, `func_start: 177`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 208`, `state_mutation: 140`
* *Architecture:* `io: 102`, `api: 46`, `concurrency: 43`, `import: 10`
* *Defense:* `safety: 135`, `doc: 99`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlConnection.js, AbstractSqlDriver.js, AbstractSqlPlatform.js, SqlEntityManager.js, typings.js, CriteriaNodeFactory.js, NativeQueryBuilder.js, QueryBuilderHelper.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.postgre.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2345.4 | **LOC:** 3100 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (29.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveUser` **(Generic / Templated Code)** (Impact: 3.4)
  * `createBooksWithTags` **(I/O & Config Routines)** (Impact: 2.0)
  * `afterFlush` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 276 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 1947
* *State Mutation (weighted view):* 338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 651`, `args: 192`, `func_start: 110`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 252`
* *Architecture:* `io: 13`, `concurrency: 567`, `import: 8`
* *Defense:* `safety: 67`, `test: 819`, `sync_locks: 17`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, index.js, Test2Subscriber.js, knex-compat, postgresql, knex, node:perf_hooks, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.mongo.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2257.04 | **LOC:** 2598 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (43.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `failHandler` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 287 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 1893
* *State Mutation (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 511`, `args: 127`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 120`, `state_mutation: 294`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `concurrency: 458`, `import: 7`
* *Defense:* `safety: 19`, `test: 742`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, FooBar.js, FooBaz.js, index.js, AuthorRepository.js, legacy, mongodb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/EntityManager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2219.64 | **LOC:** 2902 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (86.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 11.4754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upsertMany` **(Many-Argument Workhorses)** (Impact: 146.8)
    * *Intent:* * * ```ts * const author = await em.upsertMany(Author, [ * ]); * ``` * * Depending on the driver sup...
  * `upsert` **(Many-Argument Workhorses)** (Impact: 84.9)
    * *Intent:* * ``` * * The entity data needs to contain either the primary key, or any other unique property. Let...
  * `autoJoinRefsForFilters` **(Many-Argument Workhorses)** (Impact: 84.2)
    * *Intent:* /** * When filters are active on M:1 or 1:1 relations, we need to ref join them eagerly as they migh...
  * `preparePopulate` **(Many-Argument Workhorses)** (Impact: 68.6)
  * `pruneToOneRelations` **(Many-Argument Workhorses)** (Impact: 54.2)
    * *Intent:* // we need to prune the `populate` hint from to-one relations, as partially loading them does not re...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 57 instances
* *Amplified Cascading Flux:* 139 instances
* *Concurrency (weighted view):* 455
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 576`, `args: 145`, `func_start: 94`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 114`, `state_mutation: 170`
* *Architecture:* `api: 30`, `concurrency: 170`, `import: 29`
* *Defense:* `safety: 79`, `doc: 105`, `sync_locks: 3`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CacheAdapter.js, Connection.js, IDatabaseDriver.js, EntityAssigner.js, EntityFactory.js, EntityLoader.js, EntityRepository.js, Reference.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/multiple-schemas-entity-manager/multiple-schemas-entity-manager.postgres.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1983.63 | **LOC:** 592 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.6%), Guard Balance (formerly Safety Score) (29.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 249
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 85`, `args: 14`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `state_mutation: 80`, `dead_code: 2`
* *Architecture:* `concurrency: 69`, `import: 4`
* *Defense:* `test: 159`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.js, core, legacy, postgresql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/joined-strategy.postgre.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1873.99 | **LOC:** 622 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (43.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 54 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 340
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 84`, `args: 25`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 72`
* *Architecture:* `io: 1`, `concurrency: 70`, `import: 5`
* *Defense:* `safety: 25`, `test: 156`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, index.js, core, postgresql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/composite-keys/composite-keys.mysql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1858.72 | **LOC:** 497 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 63 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 419
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 112`, `args: 20`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 69`
* *Architecture:* `io: 1`, `concurrency: 104`, `import: 5`
* *Defense:* `safety: 3`, `test: 112`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, index.js, core, mysql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/read-replicas.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1834.19 | **LOC:** 310 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (24.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 271
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 87`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`
* *Architecture:* `io: 1`, `concurrency: 66`, `import: 8`
* *Defense:* `safety: 16`, `test: 76`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, index.js, Author2Subscriber.js, EverythingSubscriber.js, FlushSubscriber.js, Test2Subscriber.js, core, mysql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilderHelper.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1721.86 | **LOC:** 1525 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isSimpleRegExp` **(Many-Argument Workhorses)** (Impact: 395.6)
    * *Intent:* /** * Checks whether the RE can be rewritten to simple LIKE query */
  * `mapper` **(Many-Argument Workhorses)** (Impact: 151.1)
  * `isPrefixed` **(Stateful Encapsulated Methods)** (Impact: 144.9)
  * `createJoinExpression` **(Many-Argument Workhorses)** (Impact: 95.1)
  * `processObjectSubCondition` **(Many-Argument Workhorses)** (Impact: 84.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 323`, `args: 107`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 113`
* *Architecture:* `io: 87`, `api: 17`, `import: 6`
* *Defense:* `safety: 65`, `doc: 5`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlDriver.js, AbstractSqlPlatform.js, typings.js, NativeQueryBuilder.js, enums.js, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/multiple-schemas/multiple-schemas.postgres.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1714.11 | **LOC:** 444 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.6%), Guard Balance (formerly Safety Score) (26.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 202
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 77`, `args: 17`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `state_mutation: 42`, `dead_code: 2`
* *Architecture:* `api: 3`, `concurrency: 57`, `import: 5`
* *Defense:* `test: 115`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.js, core, legacy, entity-generator, postgresql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/polymorphic-relations/polymorphic-loading-strategies.sqlite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1640.02 | **LOC:** 748 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (46.9%), Guard Balance (formerly Safety Score) (25.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 247
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 139`, `args: 68`, `func_start: 25`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`
* *Architecture:* `io: 7`, `concurrency: 82`, `import: 2`
* *Defense:* `safety: 3`, `test: 143`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` legacy, sqlite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/table-per-type-inheritance/table-per-type-inheritance.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1518.36 | **LOC:** 3455 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.0%), Complexity Load (formerly Cognitive Load) (48.6%), Guard Balance (formerly Safety Score) (31.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formula` **(Compute Cores)** (Impact: 9.1)
  * `onFlush` **(Compute Cores)** (Impact: 6.6)
  * `onFlush` **(Compute Cores)** (Impact: 5.0)
  * `onFlush` **(Type Conversions)** (Impact: 4.8)
  * `onFlush` **(Type Conversions)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 171 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 1302
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 820`, `args: 222`, `func_start: 88`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 99`, `unreferenced_by_name: 3`
* *Architecture:* `io: 10`, `concurrency: 447`, `import: 7`
* *Defense:* `safety: 43`, `test: 426`, `immutability_locks: 1`, `cleanup: 58`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootstrap.js, core, legacy, mongodb, sqlite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.mongo2.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1496.68 | **LOC:** 409 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (36.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 473
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 133`, `args: 31`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 45`
* *Architecture:* `io: 1`, `concurrency: 118`, `import: 5`
* *Defense:* `safety: 13`, `test: 103`, `sync_locks: 10`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, FooBar.js, index.js, legacy, mongodb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/unit-of-work/UnitOfWork.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1381.06 | **LOC:** 1677 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.5%), Guard Balance (formerly Safety Score) (85.9%), Complexity Load (formerly Cognitive Load) (62.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remove` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* /** Marks an entity for removal, cascading to related entities. */
  * `getById` **(Many-Argument Workhorses)** (Impact: 37.7)
    * *Intent:* /** * Returns entity from the identity map. For composite keys, you need to pass an array of PKs in ...
  * `register` **(Defensive Guards)** (Impact: 35.7)
    * *Intent:* /** */
  * `persistToDatabase` **(Defensive Guards)** (Impact: 35.5)
  * `createTPTChangeSets` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /** * For TPT inheritance, creates separate changesets for each table in the hierarchy. * Uses the s...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 104 instances
* *Concurrency (weighted view):* 102
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 416`, `structural_boundaries: 334`, `args: 102`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 123`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 22`, `concurrency: 62`, `import: 23`
* *Defense:* `safety: 42`, `doc: 29`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityManager.js, Connection.js, IDatabaseDriver.js, Collection.js, EntityHelper.js, EntityIdentifier.js, Reference.js, wrap.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/multiple-schemas/multiple-schemas.mssql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1379.38 | **LOC:** 483 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (31.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 249
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 86`, `args: 18`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `state_mutation: 52`, `dead_code: 2`
* *Architecture:* `api: 3`, `concurrency: 64`, `import: 4`
* *Defense:* `test: 113`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.js, legacy, entity-generator, mssql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/native-query-builder/NativeQueryBuilder.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1370.97 | **LOC:** 311 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.0%), Guard Balance (formerly Safety Score) (26.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%), Complexity Load (formerly Cognitive Load) (9.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 34`, `args: 27`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 20`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 4`, `test: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` legacy, postgresql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/utils/EntityComparator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1362.1 | **LOC:** 1067 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.504; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 43.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPropertySnapshot` **(Many-Argument Workhorses)** (Impact: 170.7)
  * `getResultMapper` **(Compute Cores)** (Impact: 118.4)
    * *Intent:* /** */
  * `mapEntityProperties` **(Compute Cores)** (Impact: 111.9)
  * `getEmbeddedPropertySnapshot` **(Many-Argument Workhorses)** (Impact: 73.3)
  * `getPropertyComparator` **(Many-Argument Workhorses)** (Impact: 40.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 513
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 206`, `args: 85`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 177`
* *Architecture:* `io: 16`, `api: 11`, `import: 10`
* *Defense:* `safety: 26`, `doc: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityIdentifier.js, PolymorphicRef.js, enums.js, Platform.js, JsonType.js, typings.js, Configuration.js, RawQueryFragment.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/sql/src/AbstractSqlDriver.ts` -> Churn: **78.14%** | Cog Load: 71.103% | Debt: 7.8074%
- `packages/core/src/metadata/MetadataDiscovery.ts` -> Churn: **74.01%** | Cog Load: 77.2433% | Debt: 0.0%
- `packages/sql/src/query/QueryBuilderHelper.ts` -> Churn: **71.7%** | Cog Load: 81.7368% | Debt: 0.0%
- `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` -> Churn: **66.44%** | Cog Load: 85.1704% | Debt: 0.0%
- `packages/core/src/entity/EntityLoader.ts` -> Churn: **63.4%** | Cog Load: 57.0586% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/features/entity-manager/EntityManager.mssql.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 12128.1
- `tests/features/entity-manager/EntityManager.sqlite.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 11705.58
- `packages/sql/src/AbstractSqlDriver.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 3330.58
- `packages/core/src/metadata/MetadataDiscovery.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 2581.7
- `tests/features/entity-manager/EntityManager.mysql.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 2432.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/features/reflection/entities-compiled/Book.js` -> **Severity: 4.047** (Embedded: 0.0429 * Error Risk: 94.42%)
- `tests/features/reflection/entities-compiled/BaseEntity.js` -> **Severity: 3.616** (Embedded: 0.0392 * Error Risk: 92.3134%)
- `tests/features/reflection/entities-compiled/Author.js` -> **Severity: 3.444** (Embedded: 0.0351 * Error Risk: 98.244%)
- `tests/features/reflection/entities-compiled/Publisher.js` -> **Severity: 3.4** (Embedded: 0.0346 * Error Risk: 98.2473%)
- `tests/features/reflection/entities-compiled/BaseEntity3.js` -> **Severity: 3.051** (Embedded: 0.0397 * Error Risk: 76.8525%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/features/reflection/entities-compiled/Book.js` -> **Severity: 1973.2** (Blast Radius: 19.732 * Doc Risk: 100.0%)
- `packages/core/src/utils/fs-utils.ts` -> **Severity: 1003.4** (Blast Radius: 10.034 * Doc Risk: 100.0%)
- `tests/perf/serializing-nested-entities/seeder.ts` -> **Severity: 767.8** (Blast Radius: 7.678 * Doc Risk: 100.0%)
- `tests/features/reflection/entities-compiled/Author.js` -> **Severity: 720.0** (Blast Radius: 7.2 * Doc Risk: 100.0%)
- `tests/features/reflection/entities-compiled/Publisher.js` -> **Severity: 698.5** (Blast Radius: 6.985 * Doc Risk: 100.0%)

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
