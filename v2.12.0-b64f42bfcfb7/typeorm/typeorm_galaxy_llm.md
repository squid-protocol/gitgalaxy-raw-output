# ARCHITECTURAL_BRIEF: typeorm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/typeorm/typeorm.git` |
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
- **Scope:** 3456 analyzed artifact(s), 220462 LOC.
- **Load-bearing artifact:** `src/index.ts` -- 1440 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/index.ts` -- pulls in 173 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/driver/postgres/PostgresQueryRunner.ts` at magnitude 2738.76 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 3456 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 173 |
| Total LOC | 220462 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 95.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5513 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2132 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 24.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7507 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 58 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 3396 | 217963 | 98.3% |
| JSON | 21 | 543 | 0.6% |
| YAML | 19 | 1404 | 0.5% |
| MARKDOWN | 10 | 0 | 0.3% |
| PLAINTEXT | 5 | 0 | 0.1% |
| JAVASCRIPT | 4 | 541 | 0.1% |
| DB2_SQL | 1 | 11 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 3456 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 71%, Data / Markup / Trivial 11%, Callbacks & Closures Files 3%, Parameter Forwarders Files 3%, State Mutators Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3441 | 99.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 173*

**Composition by Extension & Reason:**
- `.md`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 10x Excluded (Machine-Generated Source Code Signature: 15 LOC), 7x Excluded (Machine-Generated Source Code Signature: 25 LOC), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.0 | 24.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.0 | 23.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 32.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.5 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.1 | 0.3 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 13.7 | 12.1 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 583 | 219 | 0 | `src/entity-manager/EntityManager.ts` |
| cleanup | 60 | 43 | 0 | `test/functional/data-source/data-source.test.ts` |
| guards | 3395 | 638 | 2 | `src/driver/mongodb/typings.ts` |
| danger | 8943 | 829 | 5 | `test/functional/database-schema/column-types/postgres/column-types-postgres.test.ts` |
| concurrency | 21598 | 1177 | 16 | `test/functional/tree-tables/update-remove/update-remove.test.ts` |
| connectivity | 6031 | 2383 | 3 | `src/driver/mongodb/typings.ts` |
| io | 2466 | 422 | 1 | `src/driver/sqlserver/SqlServerQueryRunner.ts` |
| crypto | 6 | 5 | 0 | `src/util/StringUtils.ts` |
| ipc | 13 | 9 | 0 | `src/cache/RedisQueryResultCache.ts` |
| time | 211 | 82 | 0 | `test/functional/query-builder/insert-on-conflict/query-builder-insert-on-conflict.test.ts` |
| serialization | 76 | 37 | 0 | `src/commands/InitCommand.ts` |
| regex | 349 | 83 | 0 | `src/driver/postgres/PostgresQueryRunner.ts` |
| events | 440 | 180 | 0 | `src/driver/postgres/PostgresDriver.ts` |
| tests | 10515 | 942 | 8 | `test/functional/query-builder/join/query-builder-joins.test.ts` |
| docs | 6594 | 514 | 1 | `src/driver/mongodb/typings.ts` |
| debt | 1056 | 250 | 0 | `src/driver/mongodb/typings.ts` |
| mutation | 34958 | 1637 | 22 | `test/functional/tree-tables/update-remove/update-remove.test.ts` |
| dead_code | 449 | 162 | 0 | `src/query-builder/InsertQueryBuilder.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
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

1. **index.ts** (`src/index.ts`) — 1440 inbound connections
2. **test-utils.ts** (`test/utils/test-utils.ts`) — 888 inbound connections
3. **Column.ts** (`src/decorator/columns/Column.ts`) — 706 inbound connections
4. **Entity.ts** (`src/decorator/entity/Entity.ts`) — 672 inbound connections
5. **DataSource.ts** (`src/data-source/DataSource.ts`) — 616 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/index.ts`) — 173 outbound dependencies
2. **index.ts** (`src/error/index.ts`) — 58 outbound dependencies
3. **SelectQueryBuilder.ts** (`src/query-builder/SelectQueryBuilder.ts`) — 48 outbound dependencies
4. **DataSource.ts** (`src/data-source/DataSource.ts`) — 37 outbound dependencies
5. **PostgresDriver.ts** (`src/driver/postgres/PostgresDriver.ts`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createOrderByExpression` **(I/O & Config Routines)** (@ `src/query-builder/SelectQueryBuilder.ts`) -> Impact: **500.6** | LOC: 2073
  * *Intent:* /** * Creates "ORDER BY" part of SQL query. */
- `changeColumn` **(Many-Argument Workhorses)** (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> Impact: **260.2** | LOC: 1164
  * *Intent:* /** * Changes a column in the table. * */
- `changeColumn` **(Many-Argument Workhorses)** (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> Impact: **203.7** | LOC: 794
  * *Intent:* /** * Changes a column in the table. * */
- `buildWhere` **(Many-Argument Workhorses)** (@ `src/query-builder/SelectQueryBuilder.ts`) -> Impact: **182.6** | LOC: 342
- `prepareHydratedValue` **(Many-Argument Workhorses)** (@ `src/driver/cockroachdb/CockroachDriver.ts`) -> Impact: **182.4** | LOC: 807
  * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
- `loadTables` **(Compute Cores)** (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> Impact: **165.0** | LOC: 726
  * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
- `loadTables` **(Compute Cores)** (@ `src/driver/sqlserver/SqlServerQueryRunner.ts`) -> Impact: **158.9** | LOC: 717
  * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
- `prepareHydratedValue` **(Many-Argument Workhorses)** (@ `src/driver/postgres/PostgresDriver.ts`) -> Impact: **148.3** | LOC: 1026
  * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
- `changeColumn` **(Many-Argument Workhorses)** (@ `src/driver/sqlserver/SqlServerQueryRunner.ts`) -> Impact: **140.5** | LOC: 650
  * *Intent:* /** * Changes a column in the table. * */
- `loadTables` **(Compute Cores)** (@ `src/driver/mysql/MysqlQueryRunner.ts`) -> Impact: **140.1** | LOC: 596
  * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/query-builder` | 28 | 6315.58 | 17.71% | 6.96% |
| `src/driver/postgres` | 4 | 3410.14 | 21.78% | 5.07% |
| `src/driver/mongodb` | 5 | 3401.08 | 18.82% | 41.76% |
| `src/driver/sqlserver` | 5 | 3158.34 | 27.39% | 3.67% |
| `src/driver/cockroachdb` | 4 | 2816.88 | 22.03% | 5.54% |
| `test/functional/query-runner` | 29 | 2735.64 | 27.19% | 0.0% |
| `src/driver/mysql` | 4 | 2723.02 | 27.73% | 2.58% |
| `src/driver/sap` | 4 | 2631.32 | 27.86% | 2.38% |
| `test/functional/tree-tables/update-remove` | 1 | 2537.14 | 48.26% | 0.0% |
| `src/driver/oracle` | 4 | 2492.88 | 25.4% | 4.26% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/driver/mongodb/typings.ts` -> **100.0%** Exposure
- `src/driver/mongodb/bson.typings.ts` -> **99.9999%** Exposure
- `.github/ISSUE_TEMPLATE/bug-report.yml` -> **99.5741%** Exposure
- `src/metadata-builder/EntityMetadataValidator.ts` -> **96.5913%** Exposure
- `sample/sample32-migrations/migrations/1481283582-first-release-changes.ts` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/codemod/src/cli/parse-args.ts` -> **100.0%** Exposure
- `src/metadata/ColumnMetadata.ts` -> **100.0%** Exposure
- `src/metadata/ForeignKeyMetadata.ts` -> **100.0%** Exposure
- `src/metadata/RelationMetadata.ts` -> **100.0%** Exposure
- `src/schema-builder/table/TableColumn.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/driver/mongodb/typings.ts` -> **0** Orphaned Functions | **164** Duplicates
- `src/driver/mongodb/bson.typings.ts` -> **0** Orphaned Functions | **37** Duplicates
- `test/functional/repository/find-options-locking/find-options-locking.test.ts` -> **0** Orphaned Functions | **7** Duplicates
- `test/github-issues/8398/subscriber/PostSubscriber.ts` -> **7** Orphaned Functions | **0** Duplicates
- `src/driver/cockroachdb/CockroachQueryRunner.ts` -> **0** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `1079` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/driver/postgres/PostgresQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.306)
- **Top Global Matches:** file_cluster_4: 6.306, file_cluster_12: 9.001, file_cluster_16: 9.176
- **Magnitude:** 2738.76 | **LOC:** 5280 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **31**; blast radius 0.137; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 8.6331% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 260.2)
    * *Intent:* /** * Changes a column in the table. * */
  * `loadTables` **(Compute Cores)** (Impact: 165.0)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `buildCreateColumnSql` **(Compute Cores)** (Impact: 59.7)
    * *Intent:* /** * Builds a query for create column. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* /** * Drops column in the table. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /** * Builds create table sql. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 172 instances
* *Concurrency (weighted view):* 564
* *State Mutation (weighted view):* 686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 548`, `structural_boundaries: 613`, `args: 251`, `func_start: 103`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 342`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 64`, `api: 37`, `concurrency: 304`, `import: 31`
* *Defense:* `safety: 15`, `doc: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.137
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.190116
  * `Imports (Out-Degree: 32):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `test/functional/tree-tables/update-remove/update-remove.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.076)
- **Top Global Matches:** file_cluster_10: 8.076, file_cluster_15: 8.395, file_cluster_9: 9.184
- **Magnitude:** 2537.14 | **LOC:** 2241 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 0.2; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (62.4%), Complexity Load (formerly Cognitive Load) (48.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNestedSetIds` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* /** * HELPER FUNCTIONS */
  * `escape` **(Compute Cores)** (Impact: 12.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.2
  * `Choke Point (Betweenness):` 0.007159 | `Ripple Effect (Closeness):` 0.221696
  * `Imports (Out-Degree: 7):` src, NestedSetMultipleRootError, test-utils, RelationEntities, RemainingTreeEntities, SqlServerTreeEntities, chai
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/query-builder/SelectQueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.836)
- **Top Global Matches:** file_cluster_6: 9.836, file_cluster_4: 10.777, file_cluster_12: 16.076
- **Magnitude:** 2491.14 | **LOC:** 4677 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 54.2%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **48**; blast radius 5.035; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (94.4%), Concurrency Surface (formerly Concurrency) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 16.0714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createOrderByExpression` **(I/O & Config Routines)** (Impact: 500.6)
    * *Intent:* /** * Creates "ORDER BY" part of SQL query. */
  * `buildWhere` **(Many-Argument Workhorses)** (Impact: 182.6)
  * `join` **(Many-Argument Workhorses)** (Impact: 76.5)
    * *Intent:* // ------------------------------------------------------------------------- // Protected Methods //...
  * `executeEntitiesAndRawResults` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* /** * Executes sql generated by query builder and returns object with raw results and entities creat...
  * `applyFindOptions` **(I/O & Config Routines)** (Impact: 61.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 132 instances
* *Concurrency (weighted view):* 174
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 710`, `structural_boundaries: 460`, `args: 217`, `func_start: 95`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 154`, `state_mutation: 179`, `dead_code: 21`, `planned_debt: 9`
* *Architecture:* `io: 23`, `api: 19`, `concurrency: 74`, `import: 46`
* *Defense:* `safety: 60`, `doc: 127`, `sync_locks: 18`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.035
  * `Choke Point (Betweenness):` 0.019373 | `Ripple Effect (Closeness):` 0.367807
  * `Imports (Out-Degree: 47):` &&
                    (alias.tablePath || alias.subQuery), )
            .map((alias) => 
                if (alias.subQuery)
                    return alias.subQuery +, QueryResultCacheOptions, EntityTarget, ObjectLiteral, DriverUtils, AuroraMysqlDriver, MysqlDriver...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `src/driver/sqlserver/SqlServerQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.696)
- **Top Global Matches:** file_cluster_4: 5.696, file_cluster_6: 10.911, file_cluster_12: 11.1
- **Magnitude:** 2427.9 | **LOC:** 4492 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.5%)
- **Documentation Coverage:** 8.2645% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 158.9)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 140.5)
    * *Intent:* /** * Changes a column in the table. * */
  * `mssqlParameterToNativeParameter` **(Compute Cores)** (Impact: 60.9)
    * *Intent:* /** * Converts MssqlParameter into real mssql parameter type. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* /** * Drops column in the table. * */
  * `buildCreateColumnSql` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* /** * Builds a query for create column. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 64 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 595
* *State Mutation (weighted view):* 545
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 546`, `args: 245`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 277`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 88`, `api: 37`, `concurrency: 275`, `import: 31`
* *Defense:* `safety: 18`, `doc: 79`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.000389 | `Ripple Effect (Closeness):` 0.199241
  * `Imports (Out-Degree: 32):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryLock...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/driver/cockroachdb/CockroachQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.53)
- **Top Global Matches:** file_cluster_4: 5.53, file_cluster_12: 10.491, file_cluster_15: 10.697
- **Magnitude:** 2195.64 | **LOC:** 4559 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 58.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **30**; blast radius 0.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 9.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 203.7)
    * *Intent:* /** * Changes a column in the table. * */
  * `loadTables` **(Many-Argument Workhorses)** (Impact: 140.0)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 58.7)
    * *Intent:* /** * Drops column in the table. * */
  * `query` **(Many-Argument Workhorses)** (Impact: 48.8)
    * *Intent:* /** * Executes a given SQL query. * */
  * `addColumn` **(Many-Argument Workhorses)** (Impact: 42.3)
    * *Intent:* /** * Creates a new column from the column in the table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 59 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 577
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 559`, `args: 239`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 310`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 50`, `api: 36`, `concurrency: 282`, `import: 30`
* *Defense:* `safety: 13`, `doc: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.16083
  * `Imports (Out-Degree: 31):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/sap/SapQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.686)
- **Top Global Matches:** file_cluster_4: 6.686, file_cluster_12: 10.131, file_cluster_16: 11.66
- **Magnitude:** 2105.84 | **LOC:** 3714 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.09; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.2%)
- **Documentation Coverage:** 8.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 118.7)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 68.8)
    * *Intent:* /** * Changes a column in the table. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 54.2)
    * *Intent:* /** * Drops column in the table. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 43.5)
    * *Intent:* /** * Builds and returns SQL for create table. * */
  * `query` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* /** * Executes a given SQL query. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 119 instances
* *Concurrency (weighted view):* 627
* *State Mutation (weighted view):* 501
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 480`, `args: 245`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 263`, `dead_code: 1`
* *Architecture:* `io: 34`, `api: 37`, `concurrency: 267`, `import: 31`
* *Defense:* `safety: 21`, `doc: 79`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.16088
  * `Imports (Out-Degree: 32):` ObjectLiteral, error, QueryRunnerAlreadyReleasedError, TransactionAlreadyStartedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryLock...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/mysql/MysqlQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.625)
- **Top Global Matches:** file_cluster_4: 5.625, file_cluster_12: 9.887, file_cluster_15: 10.177
- **Magnitude:** 1988.72 | **LOC:** 3635 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 58.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **30**; blast radius 0.093; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%)
- **Documentation Coverage:** 5.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 140.1)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* /** * Changes a column in the table. * */
  * `buildCreateColumnSql` **(Many-Argument Workhorses)** (Impact: 54.7)
    * *Intent:* /** * Builds a part of query to create/change a column. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* /** * Drops column in the table. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* /** * Builds create table sql * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 145 instances
* *Concurrency (weighted view):* 428
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 425`, `args: 189`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 261`, `dead_code: 1`
* *Architecture:* `io: 55`, `api: 45`, `concurrency: 243`, `import: 30`
* *Defense:* `safety: 16`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.000152 | `Ripple Effect (Closeness):` 0.199195
  * `Imports (Out-Degree: 31):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/mongodb/typings.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.328)
- **Top Global Matches:** file_cluster_5: 9.328, file_cluster_0: 10.454, file_cluster_12: 11.131
- **Magnitude:** 1893.26 | **LOC:** 9024 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **5**; blast radius 3.478; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (87.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 18.3644% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.478
  * `Choke Point (Betweenness):` 0.000254 | `Ripple Effect (Closeness):` 0.243106
  * `Imports (Out-Degree: 2):` PlatformTools, bson.typings, dns, net, tls
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/driver/oracle/OracleQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.227)
- **Top Global Matches:** file_cluster_4: 6.227, file_cluster_15: 9.207, file_cluster_12: 9.22
- **Magnitude:** 1815.94 | **LOC:** 3441 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.089; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.5%)
- **Documentation Coverage:** 5.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 129.3)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 118.4)
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
* *Structure:* `branch: 349`, `structural_boundaries: 420`, `args: 202`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 207`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 28`, `api: 38`, `concurrency: 240`, `import: 28`
* *Defense:* `safety: 22`, `doc: 77`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.089
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.186655
  * `Imports (Out-Degree: 29):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/aurora-mysql/AuroraMysqlQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.98)
- **Top Global Matches:** file_cluster_4: 5.98, file_cluster_12: 9.762, file_cluster_15: 10.316
- **Magnitude:** 1692.34 | **LOC:** 3016 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.093; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.2%)
- **Documentation Coverage:** 4.2373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 107.4)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `changeColumn` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* /** * Changes a column in the table. * */
  * `dropColumn` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /** * Drops column in the table. * */
  * `buildCreateColumnSql` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* /** * Builds a part of query to create/change a column. * */
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 40.6)
    * *Intent:* /** * Builds create table sql * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 126 instances
* *Concurrency (weighted view):* 365
* *State Mutation (weighted view):* 478
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 361`, `args: 180`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 226`, `dead_code: 1`
* *Architecture:* `io: 54`, `api: 44`, `concurrency: 220`, `import: 25`
* *Defense:* `safety: 13`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.199088
  * `Imports (Out-Degree: 26):` ObjectLiteral, error, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult, QueryRunner...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/sqlite-abstract/AbstractSqliteQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.408)
- **Top Global Matches:** file_cluster_4: 6.408, file_cluster_15: 9.226, file_cluster_16: 9.58
- **Magnitude:** 1494.62 | **LOC:** 2495 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **22**; blast radius 0.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.5%)
- **Documentation Coverage:** 8.7719% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTables` **(Compute Cores)** (Impact: 83.2)
    * *Intent:* /** * Loads all tables (with given names) from the database and creates a Table from them. * */
  * `recreateTable` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `createTableSql` **(Many-Argument Workhorses)** (Impact: 51.4)
    * *Intent:* /** * Builds create table sql. * */
  * `buildCreateColumnSql` **(Stateful Encapsulated Methods)** (Impact: 34.8)
    * *Intent:* /** * Builds a query for create column. * */
  * `dropTable` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /** * Drops the table. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 431
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 402`, `args: 193`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 139`, `dead_code: 1`
* *Architecture:* `io: 46`, `api: 41`, `concurrency: 241`, `import: 22`
* *Defense:* `safety: 11`, `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.164
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.162472
  * `Imports (Out-Degree: 24):` ObjectLiteral, error, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryRunner, TableIndexOptions, Table...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/driver/spanner/SpannerQueryRunner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.17)
- **Top Global Matches:** file_cluster_4: 7.17, file_cluster_12: 7.69, file_cluster_15: 8.403
- **Magnitude:** 1442.74 | **LOC:** 2501 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.09; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
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
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 121`, `dead_code: 5`
* *Architecture:* `io: 24`, `api: 42`, `concurrency: 241`, `import: 28`
* *Defense:* `safety: 18`, `doc: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.16087
  * `Imports (Out-Degree: 29):` ObjectLiteral, error, QueryFailedError, QueryRunnerAlreadyReleasedError, TransactionNotStartedError, PlatformTools, BaseQueryRunner, QueryResult...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/functional/query-builder/join/query-builder-joins.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.531)
- **Top Global Matches:** file_cluster_7: 5.531, file_cluster_12: 8.076, file_cluster_5: 9.006
- **Magnitude:** 1418.62 | **LOC:** 1727 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (66.6%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 191 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 1163
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 254`, `args: 83`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 200`
* *Architecture:* `concurrency: 208`, `import: 10`
* *Defense:* `safety: 2`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` DataSource, test-utils, Category, CategoryWithCompositePK, Image, Photo, Post, Tag...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/relations/lazy-relations/basic-lazy-relation/basic-lazy-relations.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.636)
- **Top Global Matches:** file_cluster_7: 6.636, file_cluster_12: 6.851, file_cluster_5: 8.93
- **Magnitude:** 1288.61 | **LOC:** 432 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (68.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` src, DataSource, test-utils, Category, Post, profile.json, user.json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/repository/find-options-operators/repository-find-operators.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.78)
- **Top Global Matches:** file_cluster_10: 4.78, file_cluster_2: 7.738, file_cluster_13: 8.452
- **Magnitude:** 1192.66 | **LOC:** 1328 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (56.5%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPost` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 158 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 991
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 261`, `args: 108`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 159`
* *Architecture:* `concurrency: 201`, `import: 9`
* *Defense:* `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` src, DriverUtils, Raw, test-utils, Comment, PersonAR, Post, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/data-source/data-source.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.806)
- **Top Global Matches:** file_cluster_10: 5.806, file_cluster_12: 8.293, file_cluster_2: 8.463
- **Magnitude:** 1157.24 | **LOC:** 458 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Complexity Load (formerly Cognitive Load) (46.7%), Guard Balance (formerly Safety Score) (43.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 170
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 149`, `args: 72`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `dead_code: 6`
* *Architecture:* `io: 4`, `concurrency: 80`, `import: 21`
* *Defense:* `safety: 10`, `test: 56`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` src, DataSource, PostgresDataSourceOptions, EntityManager, CannotGetEntityManagerNotConnectedError, NoConnectionForRepositoryError, Repository, TreeRepository...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/query-builder/InsertQueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.912)
- **Top Global Matches:** file_cluster_8: 7.912, file_cluster_6: 13.326, file_cluster_4: 21.589
- **Magnitude:** 1027.94 | **LOC:** 1682 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **23**; blast radius 0.71; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
- **Documentation Coverage:** 3.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createColumnValueExpression` **(Many-Argument Workhorses)** (Impact: 117.9)
  * `createInsertExpression` **(I/O & Config Routines)** (Impact: 109.8)
    * *Intent:* // ------------------------------------------------------------------------- // Protected Methods //...
  * `createMergeIntoSourceExpression` **(Compute Cores)** (Impact: 63.2)
    * *Intent:* /** * Creates list of values needs to be inserted in the VALUES expression. * */
  * `createMergeExpression` **(I/O & Config Routines)** (Impact: 48.0)
    * *Intent:* /** * Creates MERGE express used to perform insert query. */
  * `createValuesExpression` **(I/O & Config Routines)** (Impact: 46.2)
    * *Intent:* /** * Creates list of values needs to be inserted in the VALUES expression. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 415
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 207`, `args: 71`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 147`, `dead_code: 29`
* *Architecture:* `io: 10`, `api: 5`, `concurrency: 10`, `import: 23`
* *Defense:* `safety: 28`, `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.71
  * `Choke Point (Betweenness):` 0.001798 | `Ripple Effect (Closeness):` 0.281187
  * `Imports (Out-Degree: 24):` EntityTarget, ObjectLiteral, DriverUtils, AuroraMysqlDriver, MysqlDriver, ReactNativeDriver, AbstractSqliteDriver, SqlServerDriver...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/subscriber/Broadcaster.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.315)
- **Top Global Matches:** file_cluster_9: 8.315, file_cluster_12: 8.595, file_cluster_16: 9.457
- **Magnitude:** 842.98 | **LOC:** 1014 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **8**; blast radius 0.736; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 11.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `broadcastBeforeUpdateEvent` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* * Broadcasts "BEFORE_UPDATE" event. * Before update event is executed before entity is being updated...
  * `broadcastAfterUpdateEvent` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* * Broadcasts "AFTER_UPDATE" event. * After update event is executed after entity is being updated in...
  * `broadcastBeforeRemoveEvent` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /** * Broadcasts "BEFORE_REMOVE" event. * Before remove event is executed before entity is being rem...
  * `broadcastBeforeSoftRemoveEvent` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /** * Broadcasts "BEFORE_SOFT_REMOVE" event. * Before soft remove event is executed before entity is...
  * `broadcastBeforeRecoverEvent` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /** * Broadcasts "BEFORE_RECOVER" event. * Before recover event is executed before entity is being r...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 60 instances
* *Concurrency (weighted view):* 184
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 115`, `args: 77`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 60`, `planned_debt: 2`
* *Architecture:* `api: 22`, `concurrency: 34`, `import: 8`
* *Defense:* `safety: 6`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.736
  * `Choke Point (Betweenness):` 0.000163 | `Ripple Effect (Closeness):` 0.24341
  * `Imports (Out-Degree: 8):` ObjectLiteral, ColumnMetadata, EntityMetadata, RelationMetadata, QueryRunner, ObjectUtils, BroadcasterResult, EntitySubscriberInterface
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `test/functional/relations/multiple-primary-keys/multiple-primary-keys-many-to-many/implicit-join-entity.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.835)
- **Top Global Matches:** file_cluster_7: 5.835, file_cluster_12: 6.648, file_cluster_5: 8.753
- **Magnitude:** 798.62 | **LOC:** 1041 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (59.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DataSource, test-utils, Category, Post, Tag, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/functional/query-builder/relation-id/many-to-many/multiple-pk/multiple-pk.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.676)
- **Top Global Matches:** file_cluster_7: 5.676, file_cluster_12: 6.56, file_cluster_5: 8.693
- **Magnitude:** 752.34 | **LOC:** 1074 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DataSource, test-utils, Category, Image, Post, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/query-builder/QueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.27)
- **Top Global Matches:** file_cluster_4: 9.27, file_cluster_6: 11.147, file_cluster_12: 12.678
- **Magnitude:** 741.96 | **LOC:** 1722 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **33**; blast radius 0.931; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 26.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createWhereConditionExpression` **(Compute Cores)** (Impact: 58.2)
    * *Intent:* /** * Computes given where argument - transforms to a where string all forms it can take. * */
  * `getWherePredicateCondition` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `createPropertyPath` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* /** * Creates a property paths for a given ObjectLiteral. * */
  * `replacePropertyNamesForTheWholeQuery` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* /** * Replaces all entity's propertyName to name in the given SQL string. * */
  * `createReturningExpression` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* /** * Creates "RETURNING" / "OUTPUT" expression. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 236`, `args: 90`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 81`, `dead_code: 1`, `planned_debt: 20`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `api: 18`, `concurrency: 4`, `import: 29`
* *Defense:* `safety: 9`, `doc: 58`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 0.002241 | `Ripple Effect (Closeness):` 0.303203
  * `Imports (Out-Degree: 30):` )
         else 
            if (typeof entityTarget ===, EntityTarget, ObjectLiteral, DataSource, OracleDriver, ReturningType, error, EntityPropertyNotFoundError...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/metadata/ColumnMetadata.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.59)
- **Top Global Matches:** file_cluster_6: 6.59, file_cluster_4: 12.872, file_cluster_8: 13.27
- **Magnitude:** 706.08 | **LOC:** 1027 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **48** in-repo importer(s); it depends on **14**; blast radius 3.166; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 123.5)
    * *Intent:* // --------------------------------------------------------------------- // Constructor // ---------...
  * `getEntityValue` **(Compute Cores)** (Impact: 87.3)
    * *Intent:* /** * Extracts column value from the given entity. * If column is in embedded (or recursive embedded...
  * `getEntityValueMap` **(Many-Argument Workhorses)** (Impact: 58.8)
    * *Intent:* /** * Extracts column value and returns its column name with this value in a literal object. * If co...
  * `createValueMap` **(Compute Cores)** (Impact: 27.1)
    * *Intent:* // --------------------------------------------------------------------- // Public Methods // ------...
  * `extractEmbeddedColumnValue` **(Compute Cores)** (Impact: 21.9)
    * *Intent:* // now need to access post[data][information][counters] to get column value from the counters // and...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 97`, `args: 24`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 99`, `dead_code: 2`
* *Architecture:* `io: 10`, `api: 7`, `import: 14`
* *Defense:* `safety: 2`, `doc: 63`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.166
  * `Choke Point (Betweenness):` 0.001136 | `Ripple Effect (Closeness):` 0.268139
  * `Imports (Out-Degree: 14):` ObjectLiteral, DataSource, ValueTransformer, VirtualColumnOptions, ColumnTypes, ColumnMetadataArgs, ApplyValueTransformers, InstanceChecker...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `test/functional/relations/multiple-primary-keys/multiple-primary-keys-one-to-one/multiple-primary-keys-one-to-one.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.689)
- **Top Global Matches:** file_cluster_7: 5.689, file_cluster_12: 6.854, file_cluster_5: 8.72
- **Magnitude:** 703.7 | **LOC:** 883 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.085; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (60.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DataSource, test-utils, Category, Post, Tag, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/driver/mysql/MysqlDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.473)
- **Top Global Matches:** file_cluster_6: 8.473, file_cluster_4: 10.205, file_cluster_12: 15.907
- **Magnitude:** 701.46 | **LOC:** 1347 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **31**; blast radius 0.282; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.4%), Mutation Surface (formerly State Flux) (96.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.5%)
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
* *Structure:* `branch: 252`, `structural_boundaries: 265`, `args: 57`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 47`, `dead_code: 6`, `planned_debt: 6`
* *Architecture:* `io: 26`, `api: 19`, `concurrency: 20`, `import: 31`
* *Defense:* `safety: 6`, `doc: 57`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.282
  * `Choke Point (Betweenness):` 0.001055 | `Ripple Effect (Closeness):` 0.258624
  * `Imports (Out-Degree: 32):` ObjectLiteral, DataSource, error, ConnectionIsNotSetError, DriverPackageNotInstalledError, ColumnMetadata, EntityMetadata, PlatformTools...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/driver/sqlserver/SqlServerDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.12)
- **Top Global Matches:** file_cluster_6: 9.12, file_cluster_4: 9.254, file_cluster_12: 14.296
- **Magnitude:** 683.42 | **LOC:** 1332 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **33**; blast radius 0.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (96.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%)
- **Documentation Coverage:** 12.9032% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareHydratedValue` **(Compute Cores)** (Impact: 52.8)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type or metadata. * */
  * `preparePersistentValue` **(Compute Cores)** (Impact: 48.9)
    * *Intent:* /** * Prepares given value to a value to be persisted, based on its column type and metadata. * */
  * `normalizeType` **(Compute Cores)** (Impact: 45.7)
    * *Intent:* /** * Creates a database type from a given column metadata. * */
  * `findChangedColumns` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* /** * Differentiate columns of this table and columns from the given column metadatas columns * and ...
  * `parseTableName` **(Compute Cores)** (Impact: 35.6)
    * *Intent:* /** * Parse a target table name or other types and return a normalized table definition. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 257`, `args: 56`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 45`, `dead_code: 5`, `planned_debt: 6`
* *Architecture:* `io: 28`, `api: 19`, `concurrency: 26`, `import: 33`
* *Defense:* `safety: 6`, `doc: 56`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.289
  * `Choke Point (Betweenness):` 0.003133 | `Ripple Effect (Closeness):` 0.258649
  * `Imports (Out-Degree: 34):` ObjectLiteral, DataSource, error, ConnectionIsNotSetError, DriverPackageNotInstalledError, FindOperator, ColumnMetadata, EntityMetadata...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/github-issues/5132/entity/foo.entity.ts` (TYPESCRIPT) | Magnitude: 16.3 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, decorators: 4, branch: 2
- `test/github-issues/1123/entity/Post.ts` (TYPESCRIPT) | Magnitude: 17.54 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, api: 2, import: 2
- `test/github-issues/1308/entity/Post.ts` (TYPESCRIPT) | Magnitude: 17.54 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, api: 2, import: 2
- `test/github-issues/4156/entity/Post.ts` (TYPESCRIPT) | Magnitude: 17.54 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, api: 2, import: 2
- `test/github-issues/8346/entity/Customer.ts` (TYPESCRIPT) | Magnitude: 16.34 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, decorators: 4, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/metadata-args/MetadataArgsStorage.ts` (TYPESCRIPT) | Magnitude: 164.04 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 328, structural_boundaries: 112, args: 75, func_start: 45
- `sample/sample34-mongodb/app.ts` (TYPESCRIPT) | Magnitude: 53.14 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 14, concurrency: 7, debug_prints: 7
- `test/functional/cascades/cascade-insert-composite-pk-duplicate/entity/PostAttachment.ts` (TYPESCRIPT) | Magnitude: 6.9 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 10, api: 3, args: 2
- `test/functional/mongodb/basic/mongo-index/entity/Post.ts` (TYPESCRIPT) | Magnitude: 16.44 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 14, indent_spaces: 11, structural_boundaries: 9, args: 5
- `test/github-issues/513/issue-513.test.ts` (TYPESCRIPT) | Magnitude: 83.98 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 36, concurrency: 16, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `test/github-issues/4415/results-templates.ts` (TYPESCRIPT) | Magnitude: 10.28 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 3, api: 3, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/persistence/subject-builder/OneToOneInverseSideSubjectBuilder.ts` (TYPESCRIPT) | Magnitude: 62.88 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 17, branch: 13, core_var_decl: 9
- `test/functional/query-runner/drop-foreign-key.test.ts` (TYPESCRIPT) | Magnitude: 82.72 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 49, concurrency: 26, args: 14
- `src/metadata/RelationMetadata.ts` (TYPESCRIPT) | Magnitude: 334.66 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 311, branch: 86, structural_boundaries: 78, doc: 55
- `src/driver/spanner/SpannerDataSourceOptions.ts` (TYPESCRIPT) | Magnitude: 16.64 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 27, immutability_locks: 25, doc: 23, branch: 22
- `src/query-builder/ReturningResultsEntityUpdator.ts` (TYPESCRIPT) | Magnitude: 100.82 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 47, branch: 27, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/functional/relations/join-strategy/entity/Post.ts` (TYPESCRIPT) | Magnitude: 16.94 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 22, decorators: 16, args: 13
- `test/github-issues/8690/entity/entities.ts` (TYPESCRIPT) | Magnitude: 8.78 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 14, decorators: 9, args: 6
- `test/functional/repository/soft-delete/entity/Post.ts` (TYPESCRIPT) | Magnitude: 16.28 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, import: 5, decorators: 4
- `sample/playground/src/index.ts` (TYPESCRIPT) | Magnitude: 21.62 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, concurrency: 6, debug_prints: 4
- `test/functional/data-source/entity/Subject.ts` (TYPESCRIPT) | Magnitude: 17.36 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, decorators: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `test/functional/query-runner/add-column.test.ts` (TYPESCRIPT) | Magnitude: 124.22 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 52, safety_bypasses: 31, branch: 29
- `packages/codemod/test/transforms/v1/fixtures/query-builder-replace-property-names/query-builder-replace-property-names.output.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, args: 1, func_start: 1
- `src/driver/sap/SapDataSourceOptions.ts` (TYPESCRIPT) | Magnitude: 16.32 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 12, doc: 11, immutability_locks: 10, branch: 9
- `packages/codemod/test/transforms/v1/fixtures/query-builder-replace-property-names/query-builder-replace-property-names.input.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `.github/workflows/tests.yml` (YAML) | Magnitude: 14.44 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 26, import: 16, branch: 10
- `test/functional/columns/value-transformer/entity/PostWithNullTransformer.ts` (TYPESCRIPT) | Magnitude: 6.96 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, decorators: 3, args: 2
- `src/commands/SchemaLogCommand.ts` (TYPESCRIPT) | Magnitude: 39.06 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, core_var_decl: 9, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/metadata/EntityListenerMetadata.ts` (TYPESCRIPT) | Magnitude: 46.76 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 20, branch: 14, doc: 9
- `test/functional/cache/provider/MockQueryResultCache.ts` (TYPESCRIPT) | Magnitude: 150.84 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 221, structural_boundaries: 59, branch: 25, concurrency: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/index.ts` (TYPESCRIPT) | Magnitude: 191.54 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 236, api: 173, import: 173, indent_spaces: 2
- `src/error/index.ts` (TYPESCRIPT) | Magnitude: 74.16 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 58, api: 58, import: 58
- `src/decorator/options/JoinTableMultipleColumnsOptions.ts` (TYPESCRIPT) | Magnitude: 15.68 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 7, branch: 6, indent_spaces: 6, structural_boundaries: 4
- `src/data-source/DataSourceOptions.ts` (TYPESCRIPT) | Magnitude: 16.7 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 36, import: 17, indent_spaces: 17, api: 1
- `packages/codemod/src/transforms/v1/index.ts` (TYPESCRIPT) | Magnitude: 20.38 | Delta: **0.211** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 37, import: 34, indent_spaces: 32, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/github-issues/4147/entity/Post.ts` (TYPESCRIPT) | Magnitude: 18.46 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, api: 3, class_start: 2
- `test/github-issues/5444/entity/Author.ts` (TYPESCRIPT) | Magnitude: 17.62 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, api: 2, import: 2
- `test/functional/cascades/cascade-insert-composite-pk-duplicate/entity/PostTag.ts` (TYPESCRIPT) | Magnitude: 6.96 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 10, api: 3, args: 2
- `test/functional/find-options/basic-usage/find-options-order.test.ts` (TYPESCRIPT) | Magnitude: 84.06 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 642, structural_boundaries: 57, concurrency: 45, test: 23
- `test/functional/metadata-builder/metadata-args-storage/metadata-args-storage.test.ts` (TYPESCRIPT) | Magnitude: 16.56 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 8, import: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/decorator/Index.ts` (TYPESCRIPT) | Magnitude: 123.28 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 78, branch: 43, structural_boundaries: 22, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `test/github-issues/4156/issue-4156.test.ts` (TYPESCRIPT) | Magnitude: 49.56 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 21, concurrency: 15, args: 9
- `src/query-builder/SoftDeleteQueryBuilder.ts` (TYPESCRIPT) | Magnitude: 247.76 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 363, structural_boundaries: 77, branch: 68, args: 31
- `src/driver/mysql/MysqlDataSourceOptions.ts` (TYPESCRIPT) | Magnitude: 16.62 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, doc: 25, immutability_locks: 24, branch: 21
- `test/functional/repository/find-options-locking/find-options-locking.test.ts` (TYPESCRIPT) | Magnitude: 236.58 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 619, structural_boundaries: 176, concurrency: 84, args: 72
- `src/driver/aurora-postgres/AuroraPostgresDriver.ts` (TYPESCRIPT) | Magnitude: 95.12 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 34, args: 12, doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/driver/sqlserver/SqlServerDriver.ts` (TYPESCRIPT) | Magnitude: 683.42 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 771, structural_boundaries: 257, branch: 222, args: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/github-issues/1623/issue-1623.test.ts` (TYPESCRIPT) | Magnitude: 39.94 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 20, concurrency: 7, core_var_decl: 6
- `src/platform/PlatformTools.ts` (TYPESCRIPT) | Magnitude: 103.26 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 47, import: 28, io: 25
- `src/driver/sqljs/SqljsDataSourceOptions.ts` (TYPESCRIPT) | Magnitude: 16.24 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: doc: 9, immutability_locks: 9, indent_spaces: 9, branch: 8
- `src/query-builder/WhereClause.ts` (TYPESCRIPT) | Magnitude: 19.74 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 11, api: 4, class_start: 3
- `test/functional/database-schema/column-length/mysql/column-length-mysql.test.ts` (TYPESCRIPT) | Magnitude: 38.04 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 20, concurrency: 11, safety_bypasses: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/driver/mysql/MysqlQueryRunner.ts` -> Churn: **79.68%** | Cog Load: 67.322% | Debt: 0.0%
- `src/driver/aurora-mysql/AuroraMysqlQueryRunner.ts` -> Churn: **77.2%** | Cog Load: 62.573% | Debt: 0.0%
- `src/driver/sap/SapQueryRunner.ts` -> Churn: **77.2%** | Cog Load: 60.5131% | Debt: 0.0%
- `src/driver/sqlserver/SqlServerQueryRunner.ts` -> Churn: **74.49%** | Cog Load: 69.8219% | Debt: 7.6877%
- `src/driver/sqlite-abstract/AbstractSqliteQueryRunner.ts` -> Churn: **71.53%** | Cog Load: 53.6697% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/functional/tree-tables/update-remove/update-remove.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 2537.14
- `src/driver/mongodb/typings.ts` -> **Naor Peled** (100.0% isolated ownership) | Magnitude: 1893.26
- `test/functional/relations/multiple-primary-keys/multiple-primary-keys-many-to-many/implicit-join-entity.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 798.62
- `test/functional/tree-tables/closure-table/custom-join-column/custom-join-column.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 313.2
- `test/functional/tree-tables/materialized-path/basic/materialized-path.test.ts` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 310.96

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/data-source/DataSource.ts` -> **Severity: 2.991** (Bridge: 0.0339 * Flux: 88.2844%)
- `src/query-builder/SelectQueryBuilder.ts` -> **Severity: 1.83** (Bridge: 0.0194 * Flux: 94.4464%)
- `src/decorator/entity/Entity.ts` -> **Severity: 0.995** (Bridge: 0.0199 * Flux: 50.0%)
- `test/utils/test-utils.ts` -> **Severity: 0.664** (Bridge: 0.0066 * Flux: 100.0%)
- `src/decorator/columns/Column.ts` -> **Severity: 0.461** (Bridge: 0.0046 * Flux: 99.8946%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/driver/sqlserver/MssqlParameter.ts` -> **Severity: 27.007** (Embedded: 0.2815 * Error Risk: 95.9523%)
- `src/subscriber/EntitySubscriberInterface.ts` -> **Severity: 24.843** (Embedded: 0.2989 * Error Risk: 83.1218%)
- `src/util/ObjectUtils.ts` -> **Severity: 24.556** (Embedded: 0.3508 * Error Risk: 70.0%)
- `src/query-builder/WhereExpressionBuilder.ts` -> **Severity: 24.269** (Embedded: 0.3034 * Error Risk: 80.0%)
- `src/logger/Logger.ts` -> **Severity: 23.973** (Embedded: 0.2997 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/error/TypeORMError.ts` -> **Severity: 1312.0** (Blast Radius: 13.12 * Doc Risk: 100.0%)
- `test/utils/test-utils.ts` -> **Severity: 696.147** (Blast Radius: 18.796 * Doc Risk: 37.037%)
- `src/metadata-args/MetadataArgsStorage.ts` -> **Severity: 610.928** (Blast Radius: 6.608 * Doc Risk: 92.4528%)
- `src/util/InstanceChecker.ts` -> **Severity: 473.5** (Blast Radius: 4.735 * Doc Risk: 100.0%)
- `src/platform/PlatformTools.ts` -> **Severity: 354.056** (Blast Radius: 10.077 * Doc Risk: 35.1351%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 11377 call pairs -- scoped 48.2%, unique 0.0%, ambiguous 18.2%, external 33.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 11364 | 48.2% | 0.0% | 18.2% | 33.6% |
| javascript | 13 | 84.6% | 0.0% | 0.0% | 15.4% |

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
