# ARCHITECTURAL_BRIEF: typeorm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/typeorm/typeorm.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3458 analyzed artifact(s), 217706 LOC.
- **Load-bearing artifact:** `test/utils/test-utils.ts` -- 881 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/error/index.ts` -- pulls in 58 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/driver/postgres/PostgresQueryRunner.ts` at magnitude 3037.56 (structural weight, not risk).
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
| Total Artifacts | 3629 |
| Analyzed Artifacts (Scanned) | 3458 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 171 |
| Total LOC | 217706 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 95.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6297 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2744 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.963 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 241 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 3418 | 216465 | 98.8% |
| JSON | 21 | 543 | 0.6% |
| MARKDOWN | 7 | 0 | 0.2% |
| PLAINTEXT | 5 | 0 | 0.1% |
| JAVASCRIPT | 4 | 541 | 0.1% |
| YAML | 2 | 146 | 0.1% |
| DB2_SQL | 1 | 11 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `8.35`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +8.35; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 72%, Data / Markup / Trivial 10%, State Mutators Files 3%, Callbacks & Closures Files 3%, Parameter Forwarders Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3446 | 99.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 171*

**Composition by Extension & Reason:**
- `.md`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2570 LOC)
- `.ts`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 1682 LOC)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.template`: 5x Unsupported Format (.template)
- `.tsx`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2439 LOC), 1x Excluded (Massive Static Asset Blob: 8971 LOC)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 27.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.2 | 23.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 85.1 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.1 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 13.5 | 11.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 578 | 218 | 0 | `src/entity-manager/EntityManager.ts` |
| cleanup | 60 | 43 | 0 | `test/functional/data-source/data-source.test.ts` |
| guards | 3355 | 637 | 2 | `src/driver/mongodb/typings.ts` |
| danger | 8858 | 821 | 5 | `test/functional/database-schema/column-types/postgres/column-types-postgres.test.ts` |
| concurrency | 21452 | 1161 | 16 | `test/functional/tree-tables/update-remove/update-remove.test.ts` |
| connectivity | 5897 | 2404 | 3 | `src/driver/mongodb/typings.ts` |
| io | 2452 | 417 | 1 | `src/driver/sqlserver/SqlServerQueryRunner.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 9 | 0 | `src/cache/RedisQueryResultCache.ts` |
| time | 207 | 80 | 0 | `test/functional/query-builder/insert-on-conflict/query-builder-insert-on-conflict.test.ts` |
| serialization | 76 | 37 | 0 | `src/commands/InitCommand.ts` |
| regex | 348 | 82 | 0 | `src/driver/postgres/PostgresQueryRunner.ts` |
| events | 428 | 172 | 0 | `src/driver/postgres/PostgresDriver.ts` |
| tests | 10427 | 935 | 8 | `test/functional/query-builder/join/query-builder-joins.test.ts` |
| docs | 6521 | 497 | 1 | `src/driver/mongodb/typings.ts` |
| debt | 1010 | 243 | 0 | `src/driver/mongodb/typings.ts` |
| mutation | 34556 | 1626 | 22 | `test/functional/tree-tables/update-remove/update-remove.test.ts` |
| dead_code | 596 | 192 | 0 | `src/driver/mysql/MysqlQueryRunner.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 202 | 78 | 0 | `src/driver/sap/SapQueryRunner.ts` |
| ml_ai | 48 | 19 | 0 | `src/driver/cockroachdb/CockroachDriver.ts` |
| ui | 43 | 30 | 0 | `src/util/OrmUtils.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/driver/sqlserver/SqlServerQueryRunner.ts` (Hits: 88)
- `test/functional/query-builder/select/query-builder-select.test.ts` (Hits: 68)
- `src/driver/postgres/PostgresQueryRunner.ts` (Hits: 64)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **test-utils.ts** (`test/utils/test-utils.ts`) — 881 inbound connections
2. **Column.ts** (`src/decorator/columns/Column.ts`) — 729 inbound connections
3. **Entity.ts** (`src/decorator/entity/Entity.ts`) — 696 inbound connections
4. **DataSource.ts** (`src/data-source/DataSource.ts`) — 607 inbound connections
5. **PrimaryGeneratedColumn.ts** (`src/decorator/columns/PrimaryGeneratedColumn.ts`) — 464 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/error/index.ts`) — 58 outbound dependencies
2. **SelectQueryBuilder.ts** (`src/query-builder/SelectQueryBuilder.ts`) — 46 outbound dependencies
3. **DataSource.ts** (`src/data-source/DataSource.ts`) — 37 outbound dependencies
4. **PostgresDriver.ts** (`src/driver/postgres/PostgresDriver.ts`) — 35 outbound dependencies
5. **EntityManager.ts** (`src/entity-manager/EntityManager.ts`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `prepareHydratedValue` **(Many-Argument Workhorses)** (@ `src/driver/postgres/PostgresDriver.ts`) -> Impact: **615.9** | LOC: 1026
  * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
- `prepareHydratedValue` **(Many-Argument Workhorses)** (@ `src/driver/cockroachdb/CockroachDriver.ts`) -> Impact: **482.0** | LOC: 807
  * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
- `unescapeString` **(Compute Cores)** (@ `src/driver/postgres/PostgresDriver.ts`) -> Impact: **470.0** | LOC: 972
- `getSchemaFromKey` **(Many-Argument Workhorses)** (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> Impact: **351.4** | LOC: 1243
- `createOrderByExpression` **(I/O & Config Routines)** (@ `src/query-builder/SelectQueryBuilder.ts`) -> Impact: **346.1** | LOC: 1381
  * *Intent:* /** * Creates "ORDER BY" part of SQL query. */
- `changeColumn` **(Many-Argument Workhorses)** (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> Impact: **272.2** | LOC: 1164
  * *Intent:* /** * Changes a column in the table. * */
- `loadTables` **(Many-Argument Workhorses)** (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> Impact: **246.1** | LOC: 1160
  * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
- `changeColumn` **(Many-Argument Workhorses)** (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> Impact: **213.7** | LOC: 794
  * *Intent:* /** * Changes a column in the table. * */
- `loadTables` **(Compute Cores)** (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> Impact: **204.6** | LOC: 726
  * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
- `getSchemaFromKey` **(Many-Argument Workhorses)** (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> Impact: **201.1** | LOC: 592

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/query-builder` | 27 | 5192.64 | 15.91% | 8.64% |
| `src/driver/postgres` | 4 | 4729.04 | 31.37% | 4.7% |
| `src/driver/cockroachdb` | 4 | 3725.18 | 30.47% | 5.13% |
| `src/driver/mongodb` | 5 | 3416.88 | 19.16% | 41.89% |
| `src/driver/sqlserver` | 5 | 3342.84 | 27.48% | 3.74% |
| `test/functional/query-runner` | 29 | 2817.34 | 31.45% | 0.0% |
| `src/driver/sap` | 4 | 2797.92 | 30.19% | 2.47% |
| `src/driver/mysql` | 4 | 2745.82 | 27.77% | 2.64% |
| `test/functional/tree-tables/update-remove` | 1 | 2537.24 | 48.26% | 0.0% |
| `src/driver/oracle` | 4 | 2508.08 | 25.46% | 4.35% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/driver/mongodb/typings.ts` -> **100.0%** Exposure
- `src/driver/mongodb/bson.typings.ts` -> **99.9999%** Exposure
- `src/metadata-builder/EntityMetadataValidator.ts` -> **96.9302%** Exposure
- `sample/sample32-migrations/migrations/1481283582-first-release-changes.ts` -> **88.0797%** Exposure
- `sample/sample32-migrations/migrations/1481521933-second-release-changes.ts` -> **88.0797%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/codemod/src/cli/parse-args.ts` -> **100.0%** Exposure
- `sample/sample13-everywhere-abstraction/app.ts` -> **100.0%** Exposure
- `sample/sample6-abstract-table/app.ts` -> **100.0%** Exposure
- `src/metadata/ColumnMetadata.ts` -> **100.0%** Exposure
- `src/metadata/ForeignKeyMetadata.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/driver/mongodb/typings.ts` -> **0** Orphaned Functions | **164** Duplicates
- `src/driver/mongodb/bson.typings.ts` -> **0** Orphaned Functions | **37** Duplicates
- `test/github-issues/8398/subscriber/PostSubscriber.ts` -> **7** Orphaned Functions | **0** Duplicates
- `test/functional/null-undefined-handling/find-options.test.ts` -> **0** Orphaned Functions | **4** Duplicates
- `packages/codemod/test/transforms/transformer.test.ts` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1053` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/driver/postgres/PostgresQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3037.56 | **LOC:** 5280 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **31**; blast radius 0.202; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 9.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 272.2)
    * *Intent:* /** * Changes a column in the table. * */
  * `loadTables` **(Compute Cores)** (Impact: 204.6)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `getSchemaFromKey` **(Many-Argument Workhorses)** (Impact: 201.1)
  * `buildCreateColumnSql` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* /** * Builds a query for create column. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* /** * Drops column in the table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 180 instances
* *Concurrency (weighted view):* 564
* *State Mutation (weighted view):* 702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 613`, `args: 251`, `func_start: 103`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 342`, `dead_code: 19`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 64`, `api: 38`, `concurrency: 304`, `import: 31`
* *Defense:* `safety: 15`, `doc: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.202
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.112481
  * `Imports (Out-Degree: 31):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/driver/cockroachdb/CockroachQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2759.44 | **LOC:** 4559 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 58.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **30**; blast radius 0.117; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 9.901% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSchemaFromKey` **(Many-Argument Workhorses)** (Impact: 351.4)
  * `loadTables` **(Many-Argument Workhorses)** (Impact: 246.1)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 213.7)
    * *Intent:* /** * Changes a column in the table. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 60.7)
    * *Intent:* /** * Drops column in the table. * */
  * `query` **(Many-Argument Workhorses)** (Impact: 50.8)
    * *Intent:* /** * Executes a given SQL query. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 59 instances
* *Amplified Cascading Flux:* 160 instances
* *Concurrency (weighted view):* 577
* *State Mutation (weighted view):* 630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 504`, `structural_boundaries: 559`, `args: 239`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 310`, `dead_code: 17`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 50`, `api: 37`, `concurrency: 282`, `import: 30`
* *Defense:* `safety: 13`, `doc: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.117
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.094063
  * `Imports (Out-Degree: 30):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/sqlserver/SqlServerQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2612.0 | **LOC:** 4492 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 0.154; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.5%)
- **Documentation Coverage:** 9.7561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 158.9)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `getSchemaFromKey` **(Many-Argument Workhorses)** (Impact: 157.5)
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 148.5)
    * *Intent:* /** * Changes a column in the table. * */
  * `mssqlParameterToNativeParameter` **(Compute Cores)** (Impact: 60.9)
    * *Intent:* /** * Converts MssqlParameter into real mssql parameter type. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 60.5)
    * *Intent:* /** * Drops column in the table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 64 instances
* *Amplified Cascading Flux:* 137 instances
* *Concurrency (weighted view):* 595
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 488`, `structural_boundaries: 546`, `args: 245`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 277`, `dead_code: 20`, `planned_debt: 1`
* *Architecture:* `io: 88`, `api: 39`, `concurrency: 275`, `import: 31`
* *Defense:* `safety: 18`, `doc: 79`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.000421 | `Ripple Effect (Closeness):` 0.121376
  * `Imports (Out-Degree: 31):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryLock...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/functional/tree-tables/update-remove/update-remove.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2537.24 | **LOC:** 2241 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (82.2%), Complexity Load (formerly Cognitive Load) (48.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNestedSetIds` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* /** * HELPER FUNCTIONS */
  * `escape` **(Compute Cores)** (Impact: 12.7)
  * `isResultExpected` **(Callbacks & Closures)** (Impact: 4.2)
  * `getEntity` **(Parameter Forwarders)** (Impact: 3.8)
  * `generateConnections` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 304 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 1965
* *State Mutation (weighted view):* 499
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 497`, `args: 126`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 489`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 445`, `import: 7`
* *Defense:* `safety: 8`, `doc: 6`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` src, NestedSetMultipleRootError, test-utils, RelationEntities, RemainingTreeEntities, SqlServerTreeEntities, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/query-builder/SelectQueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2356.64 | **LOC:** 4677 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 54.2%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **46**; blast radius 4.327; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (94.4%), Concurrency Surface (formerly Concurrency) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 16.8142% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createOrderByExpression` **(I/O & Config Routines)** (Impact: 346.1)
    * *Intent:* /** * Creates "ORDER BY" part of SQL query. */
  * `buildWhere` **(Many-Argument Workhorses)** (Impact: 184.8)
  * `join` **(Many-Argument Workhorses)** (Impact: 76.5)
    * *Intent:* // ------------------------------------------------------------------------- // Protected Methods //...
  * `executeEntitiesAndRawResults` **(Compute Cores)** (Impact: 72.9)
    * *Intent:* /** * Executes sql generated by query builder and returns object with raw results and entities creat...
  * `buildOrder` **(Many-Argument Workhorses)** (Impact: 63.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 132 instances
* *Concurrency (weighted view):* 174
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 730`, `structural_boundaries: 460`, `args: 217`, `func_start: 95`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 154`, `state_mutation: 179`, `dead_code: 16`, `planned_debt: 9`
* *Architecture:* `io: 23`, `api: 20`, `concurrency: 74`, `import: 46`
* *Defense:* `safety: 60`, `doc: 127`, `sync_locks: 18`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.327
  * `Choke Point (Betweenness):` 0.03022 | `Ripple Effect (Closeness):` 0.198819
  * `Imports (Out-Degree: 45):` QueryResultCacheOptions, EntityTarget, ObjectLiteral, DriverUtils, AuroraMysqlDriver, MysqlDriver, ReactNativeDriver, AbstractSqliteDriver...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `src/driver/sap/SapQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2264.74 | **LOC:** 3714 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%)
- **Documentation Coverage:** 11.0294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSchemaFromKey` **(Many-Argument Workhorses)** (Impact: 122.6)
  * `loadTables` **(Compute Cores)** (Impact: 118.7)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 80.8)
    * *Intent:* /** * Changes a column in the table. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 54.2)
    * *Intent:* /** * Drops column in the table. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 43.5)
    * *Intent:* /** * Builds and returns SQL for create table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 627
* *State Mutation (weighted view):* 503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 480`, `args: 245`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 263`, `dead_code: 12`
* *Architecture:* `io: 34`, `api: 39`, `concurrency: 267`, `import: 31`
* *Defense:* `safety: 21`, `doc: 79`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.000225 | `Ripple Effect (Closeness):` 0.094097
  * `Imports (Out-Degree: 30):` ObjectLiteral, error, QueryRunnerAlreadyReleasedError, TransactionAlreadyStartedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryLock...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/mysql/MysqlQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2008.02 | **LOC:** 3635 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 58.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **30**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 5.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 140.1)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* /** * Changes a column in the table. * */
  * `buildCreateColumnSql` **(Many-Argument Workhorses)** (Impact: 58.7)
    * *Intent:* /** * Builds a part of query to create/change a column. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* /** * Drops column in the table. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 48.1)
    * *Intent:* /** * Builds create table sql * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 145 instances
* *Concurrency (weighted view):* 428
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 425`, `args: 189`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 261`, `dead_code: 24`
* *Architecture:* `io: 55`, `api: 45`, `concurrency: 243`, `import: 30`
* *Defense:* `safety: 16`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.000249 | `Ripple Effect (Closeness):` 0.121331
  * `Imports (Out-Degree: 30):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/mongodb/typings.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1893.26 | **LOC:** 9024 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **6**; blast radius 1.776; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (87.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 18.0142% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /** * Create a TopologyDescription */
  * `resolveExplainTimeoutOptions` **(Stateful Encapsulated Methods)** (Impact: 14.4)
  * `constructor` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /** * Constructs a WriteConcern from the write concern properties. */
  * `explain` **(Generic / Templated Code)** (Impact: 8.9)
  * `updateOne` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* /** * Update a single document in a collection * * The value of `update` can be either: * - UpdateFi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 912`, `structural_boundaries: 1681`, `args: 572`, `func_start: 564`, `class_start: 264`
* *Risk/State:* `safety_bypasses: 66`, `planned_debt: 1`, `duplicate_logic: 164`
* *Architecture:* `api: 565`, `concurrency: 140`, `import: 6`
* *Defense:* `doc: 1359`, `immutability_locks: 154`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.776
  * `Choke Point (Betweenness):` 0.000185 | `Ripple Effect (Closeness):` 0.14116
  * `Imports (Out-Degree: 2):` PlatformTools, bson.typings, dns, mongodb, net, tls
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/driver/oracle/OracleQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1831.14 | **LOC:** 3441 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.5%)
- **Documentation Coverage:** 5.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 130.7)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 124.4)
    * *Intent:* /** * Changes a column in the table. * */
  * `query` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* /** * Executes a given SQL query. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* /** * Drops column in the table. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 31.7)
    * *Intent:* /** * Builds and returns SQL for create table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 104 instances
* *Concurrency (weighted view):* 435
* *State Mutation (weighted view):* 415
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 420`, `args: 202`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 207`, `dead_code: 13`, `planned_debt: 1`
* *Architecture:* `io: 28`, `api: 38`, `concurrency: 240`, `import: 28`
* *Defense:* `safety: 22`, `doc: 77`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.109679
  * `Imports (Out-Degree: 28):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/aurora-mysql/AuroraMysqlQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1717.84 | **LOC:** 3016 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%)
- **Documentation Coverage:** 4.2373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 107.4)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* /** * Changes a column in the table. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /** * Drops column in the table. * */
  * `buildCreateColumnSql` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* /** * Builds a part of query to create/change a column. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 42.4)
    * *Intent:* /** * Builds create table sql * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 129 instances
* *Concurrency (weighted view):* 365
* *State Mutation (weighted view):* 484
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 361`, `args: 180`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 226`, `dead_code: 19`
* *Architecture:* `io: 54`, `api: 44`, `concurrency: 220`, `import: 25`
* *Defense:* `safety: 13`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.121232
  * `Imports (Out-Degree: 25):` ObjectLiteral, error, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult, QueryRunner...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/postgres/PostgresDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1657.8 | **LOC:** 1901 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **35**; blast radius 0.436; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.7%), Mutation Surface (formerly State Flux) (90.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareHydratedValue` **(Many-Argument Workhorses)** (Impact: 615.9)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
  * `unescapeString` **(Compute Cores)** (Impact: 470.0)
  * `preparePersistentValue` **(Compute Cores)** (Impact: 100.7)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type and metadata. * */
  * `quoteString` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* // https://www.postgresql.org/docs/9.0/hstore.html
  * `enableExtensions` **(Defensive Guards)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 126
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 414`, `args: 91`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 65`, `dead_code: 4`, `planned_debt: 7`
* *Architecture:* `io: 36`, `api: 9`, `concurrency: 51`, `import: 35`
* *Defense:* `safety: 42`, `doc: 61`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.436
  * `Choke Point (Betweenness):` 0.000345 | `Ripple Effect (Closeness):` 0.111631
  * `Imports (Out-Degree: 35):` ObjectLiteral, DataSource, error, ConnectionIsNotSetError, DriverPackageNotInstalledError, ColumnMetadata, EntityMetadata, IndexMetadata...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/driver/sqlite-abstract/AbstractSqliteQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1641.92 | **LOC:** 2495 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **22**; blast radius 0.219; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 9.5652% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 101.6)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `queryPromises` **(Compute Cores)** (Impact: 91.6)
  * `recreateTable` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* /** * Builds create table sql. * */
  * `buildCreateColumnSql` **(Stateful Encapsulated Methods)** (Impact: 36.5)
    * *Intent:* /** * Builds a query for create column. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 91 instances
* *Concurrency (weighted view):* 431
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 402`, `args: 193`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 139`, `dead_code: 5`
* *Architecture:* `io: 46`, `api: 42`, `concurrency: 241`, `import: 22`
* *Defense:* `safety: 11`, `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.219
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.101847
  * `Imports (Out-Degree: 22):` ObjectLiteral, error, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryRunner, TableIndexOptions, Table...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/driver/spanner/SpannerQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1442.74 | **LOC:** 2501 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 4.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 50.7)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 49.2)
    * *Intent:* /** * Changes a column in the table. * */
  * `query` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* /** * Executes a given SQL query. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* /** * Builds create table sql. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* /** * Drops column in the table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 49 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 486
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 329`, `args: 144`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 121`, `dead_code: 13`
* *Architecture:* `io: 24`, `api: 42`, `concurrency: 241`, `import: 28`
* *Defense:* `safety: 18`, `doc: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.094097
  * `Imports (Out-Degree: 28):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/functional/query-builder/join/query-builder-joins.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1418.62 | **LOC:** 1727 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 191 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 1163
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 254`, `args: 83`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 200`
* *Architecture:* `concurrency: 208`, `import: 10`
* *Defense:* `safety: 2`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DataSource, test-utils, Category, CategoryWithCompositePK, Image, Photo, Post, Tag...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/relations/lazy-relations/basic-lazy-relation/basic-lazy-relations.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1288.61 | **LOC:** 432 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 56 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 375
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 106`, `args: 28`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 83`
* *Architecture:* `concurrency: 95`, `import: 8`
* *Defense:* `safety: 5`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` src, DataSource, test-utils, Category, Post, profile.json, user.json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/data-source/data-source.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1244.68 | **LOC:** 458 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Complexity Load (formerly Cognitive Load) (46.9%), Guard Balance (formerly Safety Score) (33.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 170
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 149`, `args: 72`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`
* *Architecture:* `io: 4`, `concurrency: 80`, `import: 21`
* *Defense:* `safety: 10`, `test: 56`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` src, DataSource, PostgresDataSourceOptions, EntityManager, CannotGetEntityManagerNotConnectedError, NoConnectionForRepositoryError, Repository, TreeRepository...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/repository/find-options-operators/repository-find-operators.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1197.76 | **LOC:** 1328 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPost` **(Callbacks & Closures)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 158 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 991
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 261`, `args: 108`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 159`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 201`, `import: 9`
* *Defense:* `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` src, DriverUtils, Raw, test-utils, Comment, PersonAR, Post, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/driver/cockroachdb/CockroachDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 933.16 | **LOC:** 1262 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **32**; blast radius 0.16; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 7.3171% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareHydratedValue` **(Many-Argument Workhorses)** (Impact: 482.0)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
  * `findChangedColumns` **(Compute Cores)** (Impact: 52.4)
    * *Intent:* /** * Differentiate columns of this table and columns from the given column metadatas columns * and ...
  * `preparePersistentValue` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type and metadata. * */
  * `createPool` **(Stateful Encapsulated Methods)** (Impact: 12.8)
    * *Intent:* /** * Creates a new connection pool for a given database credentials. * */
  * `connect` **(I/O & Config Routines)** (Impact: 9.7)
    * *Intent:* // ------------------------------------------------------------------------- // Public Implemented M...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 103
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 288`, `args: 60`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 49`, `dead_code: 3`, `planned_debt: 7`
* *Architecture:* `io: 35`, `api: 14`, `concurrency: 33`, `import: 32`
* *Defense:* `safety: 17`, `doc: 57`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.16
  * `Choke Point (Betweenness):` 0.000272 | `Ripple Effect (Closeness):` 0.110877
  * `Imports (Out-Degree: 32):` ObjectLiteral, DataSource, error, ConnectionIsNotSetError, DriverPackageNotInstalledError, ColumnMetadata, EntityMetadata, PlatformTools...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/subscriber/Broadcaster.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 857.38 | **LOC:** 1014 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **8**; blast radius 0.962; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 6.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `broadcastBeforeUpdateEvent` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* * Broadcasts "BEFORE_UPDATE" event. * Before update event is executed before entity is being updated...
  * `broadcastAfterUpdateEvent` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* * Broadcasts "AFTER_UPDATE" event. * After update event is executed after entity is being updated in...
  * `broadcastBeforeRemoveEvent` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* /** * Broadcasts "BEFORE_REMOVE" event. * Before remove event is executed before entity is being rem...
  * `broadcastBeforeSoftRemoveEvent` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* /** * Broadcasts "BEFORE_SOFT_REMOVE" event. * Before soft remove event is executed before entity is...
  * `broadcastBeforeRecoverEvent` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* /** * Broadcasts "BEFORE_RECOVER" event. * Before recover event is executed before entity is being r...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 60 instances
* *Concurrency (weighted view):* 184
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 115`, `args: 77`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 60`, `planned_debt: 2`
* *Architecture:* `api: 22`, `concurrency: 34`, `import: 8`
* *Defense:* `safety: 6`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.962
  * `Choke Point (Betweenness):` 0.000888 | `Ripple Effect (Closeness):` 0.146238
  * `Imports (Out-Degree: 8):` ObjectLiteral, ColumnMetadata, EntityMetadata, RelationMetadata, QueryRunner, ObjectUtils, BroadcasterResult, EntitySubscriberInterface
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/metadata/ColumnMetadata.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 853.28 | **LOC:** 1027 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **14**; blast radius 3.049; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 123.5)
    * *Intent:* // --------------------------------------------------------------------- // Constructor // ---------...
  * `getEntityValue` **(Compute Cores)** (Impact: 87.3)
    * *Intent:* /** * Extracts column value from the given entity. * If column is in embedded (or recursive embedded...
  * `extractEmbeddedColumnValue` **(Compute Cores)** (Impact: 81.2)
    * *Intent:* // next we need to access post[data][information][counters][this.propertyName] to get column value f...
  * `getEntityValueMap` **(Many-Argument Workhorses)** (Impact: 58.8)
    * *Intent:* /** * Extracts column value and returns its column name with this value in a literal object. * If co...
  * `extractEmbeddedColumnValue` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* // now need to access post[data][information][counters] to get column value from the counters // and...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 97`, `args: 24`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 99`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 7`, `import: 14`
* *Defense:* `safety: 2`, `doc: 63`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.049
  * `Choke Point (Betweenness):` 0.002355 | `Ripple Effect (Closeness):` 0.163748
  * `Imports (Out-Degree: 14):` ObjectLiteral, DataSource, ValueTransformer, VirtualColumnOptions, ColumnTypes, ColumnMetadataArgs, ApplyValueTransformers, InstanceChecker...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `test/functional/relations/multiple-primary-keys/multiple-primary-keys-many-to-many/implicit-join-entity.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 798.62 | **LOC:** 1041 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (76.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 88 instances
* *Concurrency (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 169`, `args: 30`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 215`
* *Architecture:* `concurrency: 110`, `import: 6`
* *Defense:* `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DataSource, test-utils, Category, Post, Tag, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/query-builder/QueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 764.26 | **LOC:** 1722 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **29**; blast radius 0.368; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Guard Balance (formerly Safety Score) (85.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 26.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createWhereConditionExpression` **(Compute Cores)** (Impact: 60.0)
    * *Intent:* /** * Computes given where argument - transforms to a where string all forms it can take. * */
  * `getWherePredicateCondition` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `replacePropertyNamesForTheWholeQuery` **(Compute Cores)** (Impact: 33.7)
    * *Intent:* /** * Replaces all entity's propertyName to name in the given SQL string. * */
  * `createPropertyPath` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* /** * Creates a property paths for a given ObjectLiteral. * */
  * `createReturningExpression` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* /** * Creates "RETURNING" / "OUTPUT" expression. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 236`, `args: 90`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 81`, `dead_code: 2`, `planned_debt: 20`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `api: 18`, `concurrency: 4`, `import: 29`
* *Defense:* `safety: 9`, `doc: 58`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.368
  * `Choke Point (Betweenness):` 0.002583 | `Ripple Effect (Closeness):` 0.150989
  * `Imports (Out-Degree: 28):` EntityTarget, ObjectLiteral, DataSource, OracleDriver, ReturningType, error, EntityPropertyNotFoundError, FindOperator...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `test/functional/query-builder/relation-id/many-to-many/multiple-pk/multiple-pk.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 752.34 | **LOC:** 1074 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (72.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 85 instances
* *Concurrency (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 124`, `args: 32`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 190`
* *Architecture:* `concurrency: 103`, `import: 6`
* *Defense:* `test: 150`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DataSource, test-utils, Category, Image, Post, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/driver/mysql/MysqlDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 704.96 | **LOC:** 1347 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **31**; blast radius 0.306; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.4%), Mutation Surface (formerly State Flux) (96.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.3%)
- **Documentation Coverage:** 5.3571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeType` **(Compute Cores)** (Impact: 66.9)
    * *Intent:* /** * Creates a database type from a given column metadata. * */
  * `prepareHydratedValue` **(Compute Cores)** (Impact: 62.3)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
  * `preparePersistentValue` **(Compute Cores)** (Impact: 50.6)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type and metadata. * */
  * `findChangedColumns` **(Compute Cores)** (Impact: 42.1)
    * *Intent:* /** * Differentiate columns of this table and columns from the given column metadatas columns * and ...
  * `parseTableName` **(Compute Cores)** (Impact: 30.7)
    * *Intent:* /** * Parse a target table name or other types and return a normalized table definition. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 70
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 265`, `args: 57`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 47`, `dead_code: 3`, `planned_debt: 6`
* *Architecture:* `io: 26`, `api: 19`, `concurrency: 20`, `import: 31`
* *Defense:* `safety: 6`, `doc: 57`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 0.001891 | `Ripple Effect (Closeness):` 0.150835
  * `Imports (Out-Degree: 31):` ObjectLiteral, DataSource, error, ConnectionIsNotSetError, DriverPackageNotInstalledError, ColumnMetadata, EntityMetadata, PlatformTools...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `test/functional/relations/multiple-primary-keys/multiple-primary-keys-one-to-one/multiple-primary-keys-one-to-one.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 703.7 | **LOC:** 883 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.113; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (77.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 78 instances
* *Concurrency (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 150`, `args: 30`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 185`
* *Architecture:* `concurrency: 98`, `import: 6`
* *Defense:* `safety: 3`, `test: 123`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DataSource, test-utils, Category, Post, Tag, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/driver/cockroachdb/CockroachQueryRunner.ts` -> Churn: **79.68%** | Cog Load: 68.746% | Debt: 9.7894%
- `src/driver/mysql/MysqlQueryRunner.ts` -> Churn: **79.68%** | Cog Load: 67.3738% | Debt: 0.0%
- `src/driver/postgres/PostgresQueryRunner.ts` -> Churn: **79.68%** | Cog Load: 66.6337% | Debt: 9.3774%
- `src/driver/aurora-mysql/AuroraMysqlQueryRunner.ts` -> Churn: **77.2%** | Cog Load: 51.8961% | Debt: 0.0%
- `src/driver/sap/SapQueryRunner.ts` -> Churn: **77.2%** | Cog Load: 69.4223% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/functional/tree-tables/update-remove/update-remove.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 2537.24
- `src/driver/mongodb/typings.ts` -> **Naor Peled** (100.0% isolated ownership) | Magnitude: 1893.26
- `test/functional/relations/multiple-primary-keys/multiple-primary-keys-many-to-many/implicit-join-entity.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 798.62
- `test/functional/repository/find-options-locking/find-options-locking.test.ts` -> **Piotr Kuczynski** (85.7% isolated ownership) | Magnitude: 342.88
- `test/functional/tree-tables/closure-table/custom-join-column/custom-join-column.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 313.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/data-source/DataSource.ts` -> **Severity: 2.909** (Bridge: 0.033 * Flux: 88.2844%)
- `src/query-builder/SelectQueryBuilder.ts` -> **Severity: 2.854** (Bridge: 0.0302 * Flux: 94.4464%)
- `src/decorator/entity/Entity.ts` -> **Severity: 0.939** (Bridge: 0.0188 * Flux: 50.0%)
- `test/utils/test-utils.ts` -> **Severity: 0.891** (Bridge: 0.0089 * Flux: 100.0%)
- `src/metadata/EntityMetadata.ts` -> **Severity: 0.496** (Bridge: 0.005 * Flux: 99.9293%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util/ObjectUtils.ts` -> **Severity: 18.633** (Embedded: 0.2662 * Error Risk: 70.0%)
- `test/utils/test-utils.ts` -> **Severity: 18.588** (Embedded: 0.2548 * Error Risk: 72.9574%)
- `src/decorator/columns/Column.ts` -> **Severity: 18.037** (Embedded: 0.2111 * Error Risk: 85.4312%)
- `src/query-builder/SelectQueryBuilder.ts` -> **Severity: 15.767** (Embedded: 0.1988 * Error Risk: 79.3017%)
- `src/metadata/ColumnMetadata.ts` -> **Severity: 15.496** (Embedded: 0.1637 * Error Risk: 94.6304%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/utils/test-utils.ts` -> **Severity: 1741.591** (Blast Radius: 47.023 * Doc Risk: 37.037%)
- `src/error/TypeORMError.ts` -> **Severity: 938.4** (Blast Radius: 9.384 * Doc Risk: 100.0%)
- `src/metadata-args/MetadataArgsStorage.ts` -> **Severity: 588.185** (Blast Radius: 6.362 * Doc Risk: 92.4528%)
- `packages/codemod/src/lib/colors.ts` -> **Severity: 380.3** (Blast Radius: 3.803 * Doc Risk: 100.0%)
- `src/platform/PlatformTools.ts` -> **Severity: 323.383** (Blast Radius: 9.204 * Doc Risk: 35.1351%)

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
