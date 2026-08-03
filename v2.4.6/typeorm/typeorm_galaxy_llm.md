# ARCHITECTURAL_BRIEF: typeorm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/typeorm` |
| **Timestamp** | `2026-08-03T19:59:42.300454+00:00` |
| **Scan Duration** | `3.55s` |
| **Git Branch** | `master` |
| **Git Commit** | `5b5058c4a2aacffd4e3f7c72833803df3707cf1c` |
| **Git Remote** | `https://github.com/typeorm/typeorm.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 685 malicious artifacts.

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
| Total Artifacts | 3629 |
| Analyzed Artifacts (Scanned) | 711 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2918 |
| Total LOC | 64408 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 19.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5205 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1914 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 30.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6351 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 34 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 680 | 63348 | 95.6% |
| JSON | 12 | 362 | 1.7% |
| MARKDOWN | 7 | 0 | 1.0% |
| PLAINTEXT | 5 | 0 | 0.7% |
| JAVASCRIPT | 4 | 541 | 0.6% |
| YAML | 2 | 146 | 0.3% |
| SQLITE | 1 | 11 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.608`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 300 | 42.2% |
| file_cluster_13 | 250 | 35.2% |
| file_cluster_4 | 74 | 10.4% |
| file_cluster_16 | 49 | 6.9% |
| file_cluster_17 | 18 | 2.5% |
| file_cluster_0 | 2 | 0.3% |
| file_cluster_6 | 2 | 0.3% |
| file_cluster_9 | 1 | 0.1% |
| file_cluster_1 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_2 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 1.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2918*

**Composition by Extension & Reason:**
- `.ts`: 2753x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 1682 LOC)
- `.md`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2570 LOC)
- `.json`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 38.2 | 44.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.1 | 2.3 | 80.0 |
| API Exposure | 0.0 | 19.9 | 5.3 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 1.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 79.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.1 | 0.3 | 0.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 21.5 | 12.1 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.8 | 40.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 36.4 | 1.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/driver/sqlserver/SqlServerQueryRunner.ts` (Hits: 85)
- `src/driver/postgres/PostgresQueryRunner.ts` (Hits: 61)
- `src/driver/cockroachdb/CockroachQueryRunner.ts` (Hits: 50)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ObjectLiteral.ts** (`src/common/ObjectLiteral.ts`) — 84 inbound connections
2. **TypeORMError.ts** (`src/error/TypeORMError.ts`) — 69 inbound connections
3. **EntityMetadata.ts** (`src/metadata/EntityMetadata.ts`) — 69 inbound connections
4. **QueryRunner.ts** (`src/query-runner/QueryRunner.ts`) — 64 inbound connections
5. **error.ts** (`packages/codemod/src/lib/error.ts`) — 62 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/index.ts`) — 173 outbound dependencies
2. **index.ts** (`src/error/index.ts`) — 58 outbound dependencies
3. **SelectQueryBuilder.ts** (`src/query-builder/SelectQueryBuilder.ts`) — 46 outbound dependencies
4. **DataSource.ts** (`src/data-source/DataSource.ts`) — 37 outbound dependencies
5. **PostgresDriver.ts** (`src/driver/postgres/PostgresDriver.ts`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `prepareHydratedValue` (@ `src/driver/cockroachdb/CockroachDriver.ts`) -> Impact: **3241.2** | LOC: 807
- `createTable` (@ `src/driver/oracle/OracleQueryRunner.ts`) -> Impact: **1404.0** | LOC: 989
  * *Intent:* /** * Checks if column with the given name exist in the given table. *
- `transaction` (@ `src/entity-manager/EntityManager.ts`) -> Impact: **1384.2** | LOC: 1013
- `createTable` (@ `src/driver/sqlserver/SqlServerQueryRunner.ts`) -> Impact: **1261.9** | LOC: 1062
- `where` (@ `src/query-builder/UpdateQueryBuilder.ts`) -> Impact: **1141.1** | LOC: 252
  * *Intent:* // ------------------------------------------------------------------------- // Public Methods // ----------------------------------------------------...
- `registerQueryBuilders` (@ `src/data-source/DataSource.ts`) -> Impact: **1127.3** | LOC: 570
- `createIndex` (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> Impact: **1093.1** | LOC: 1142
- `Load` (@ `src/subscriber/Broadcaster.ts`) -> Impact: **1049.4** | LOC: 741
- `execute` (@ `src/persistence/SubjectExecutor.ts`) -> Impact: **972.0** | LOC: 527
- `clearDatabase` (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> Impact: **924.9** | LOC: 797

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `connect` (@ `src/cache/RedisQueryResultCache.ts`) -> **O(2^N) [Recursive]**
- `load` (@ `src/connection/ConnectionOptionsReader.ts`) -> **O(2^N) [Recursive]**
- `registerQueryBuilders` (@ `src/data-source/DataSource.ts`) -> **O(2^N) [Recursive]**
- `prepareHydratedValue` (@ `src/driver/cockroachdb/CockroachDriver.ts`) -> **O(2^N) [Recursive]**
- `query` (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> **O(2^N) [Recursive]**
- `query` (@ `src/driver/mysql/MysqlQueryRunner.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `query` (@ `src/driver/nativescript/NativescriptQueryRunner.ts`) -> **O(2^N) [Recursive]**
- `query` (@ `src/driver/postgres/PostgresQueryRunner.ts`) -> **O(2^N) [Recursive]**
- `query` (@ `src/driver/react-native/ReactNativeQueryRunner.ts`) -> **O(2^N) [Recursive]**
- `query` (@ `src/driver/spanner/SpannerQueryRunner.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `changeColumn` (@ `src/driver/sap/SapQueryRunner.ts`) -> DB Complexity: **191**
- `createIndex` (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> DB Complexity: **172**
- `createTable` (@ `src/driver/sqlserver/SqlServerQueryRunner.ts`) -> DB Complexity: **167**
- `Load` (@ `src/subscriber/Broadcaster.ts`) -> DB Complexity: **155**
- `changeColumn` (@ `src/driver/cockroachdb/CockroachQueryRunner.ts`) -> DB Complexity: **150**
- `createTable` (@ `src/driver/oracle/OracleQueryRunner.ts`) -> DB Complexity: **142**
  * *Intent:* /** * Checks if column with the given name exist in the given table. *
- `prepareHydratedValue` (@ `src/driver/cockroachdb/CockroachDriver.ts`) -> DB Complexity: **136**
- `registerQueryBuilders` (@ `src/data-source/DataSource.ts`) -> DB Complexity: **120**
- `transaction` (@ `src/entity-manager/EntityManager.ts`) -> DB Complexity: **117**
- `startTransaction` (@ `src/driver/sap/SapQueryRunner.ts`) -> DB Complexity: **102**
  * *Intent:* // return the connection back to the pool

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/query-builder` | 27 | 1346.2 | 25.5% | 14.19% |
| `src/driver/cockroachdb` | 4 | 969.65 | 28.7% | 4.5% |
| `src/driver/postgres` | 4 | 524.09 | 28.96% | 4.72% |
| `src/driver/sqlserver` | 5 | 445.37 | 27.49% | 3.66% |
| `src/driver/oracle` | 4 | 440.3 | 28.79% | 4.31% |
| `src/driver/sqlite-abstract` | 2 | 430.49 | 42.0% | 4.33% |
| `src/driver/spanner` | 4 | 428.01 | 24.54% | 18.66% |
| `src/metadata` | 11 | 421.86 | 33.8% | 7.08% |
| `src/driver/mysql` | 4 | 411.78 | 28.0% | 2.62% |
| `src/driver/aurora-mysql` | 4 | 368.58 | 23.59% | 2.57% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docker/oracle/startup/01_init.sql` -> **100.0%** Exposure
- `packages/codemod/src/transforms/stats.ts` -> **100.0%** Exposure
- `src/query-builder/Alias.ts` -> **100.0%** Exposure
- `src/repository/BaseEntity.ts` -> **99.9982%** Exposure
- `src/decorator/Index.ts` -> **99.95%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/data-source/DataSource.ts` -> **100.0%** Exposure
- `src/driver/aurora-postgres/AuroraPostgresDriver.ts` -> **100.0%** Exposure
- `src/driver/aurora-postgres/AuroraPostgresQueryRunner.ts` -> **100.0%** Exposure
- `src/driver/better-sqlite3/BetterSqlite3Driver.ts` -> **100.0%** Exposure
- `src/driver/better-sqlite3/BetterSqlite3QueryRunner.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/driver/mongodb/typings.ts` -> **0** Orphaned Functions | **38** Duplicates
- `src/repository/BaseEntity.ts` -> **0** Orphaned Functions | **18** Duplicates
- `src/repository/Repository.ts` -> **0** Orphaned Functions | **9** Duplicates
- `test/utils/test-utils.ts` -> **8** Orphaned Functions | **0** Duplicates
- `docker/oracle/startup/01_init.sql` -> **2** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/subscriber/Broadcaster.ts`** -> AI Confidence: **99.39%**
2. **`src/metadata/ColumnMetadata.ts`** -> AI Confidence: **99.35%**
3. **`src/decorator/options/ColumnOptions.ts`** -> AI Confidence: **99.32%**
4. **`src/driver/mongodb/MongoDataSourceOptions.ts`** -> AI Confidence: **99.32%**
5. **`src/commands/InitCommand.ts`** -> AI Confidence: **99.31%**
6. **`src/connection/ConnectionOptionsReader.ts`** -> AI Confidence: **99.31%**
7. **`src/data-source/BaseDataSourceOptions.ts`** -> AI Confidence: **99.31%**
8. **`src/driver/aurora-mysql/AuroraMysqlQueryRunner.ts`** -> AI Confidence: **99.31%**
9. **`src/driver/cockroachdb/CockroachDriver.ts`** -> AI Confidence: **99.31%**
10. **`src/driver/cockroachdb/CockroachQueryRunner.ts`** -> AI Confidence: **99.31%**
11. **`src/driver/mysql/MysqlQueryRunner.ts`** -> AI Confidence: **99.31%**
12. **`src/driver/oracle/OracleDriver.ts`** -> AI Confidence: **99.31%**
13. **`src/driver/oracle/OracleQueryRunner.ts`** -> AI Confidence: **99.31%**
14. **`src/driver/postgres/PostgresQueryRunner.ts`** -> AI Confidence: **99.31%**
15. **`src/driver/react-native/ReactNativeDriver.ts`** -> AI Confidence: **99.31%**
16. **`src/driver/sap/SapDriver.ts`** -> AI Confidence: **99.31%**
17. **`src/driver/spanner/SpannerQueryRunner.ts`** -> AI Confidence: **99.31%**
18. **`src/driver/sqlite-abstract/AbstractSqliteDriver.ts`** -> AI Confidence: **99.31%**
19. **`src/driver/sqljs/SqljsDriver.ts`** -> AI Confidence: **99.31%**
20. **`src/driver/sqlserver/SqlServerQueryRunner.ts`** -> AI Confidence: **99.31%**
21. **`src/entity-schema/EntitySchemaRelationOptions.ts`** -> AI Confidence: **99.31%**
22. **`src/entity-schema/EntitySchemaTransformer.ts`** -> AI Confidence: **99.31%**
23. **`src/find-options/FindOptionsUtils.ts`** -> AI Confidence: **99.31%**
24. **`src/metadata-builder/EntityMetadataValidator.ts`** -> AI Confidence: **99.31%**
25. **`src/metadata-builder/JunctionEntityMetadataBuilder.ts`** -> AI Confidence: **99.31%**
26. **`src/metadata/RelationMetadata.ts`** -> AI Confidence: **99.31%**
27. **`src/persistence/Subject.ts`** -> AI Confidence: **99.31%**
28. **`src/persistence/SubjectChangedColumnsComputer.ts`** -> AI Confidence: **99.31%**
29. **`src/persistence/SubjectExecutor.ts`** -> AI Confidence: **99.31%**
30. **`src/query-builder/QueryBuilder.ts`** -> AI Confidence: **99.31%**
31. **`src/query-builder/QueryExpressionMap.ts`** -> AI Confidence: **99.31%**
32. **`src/query-builder/SelectQueryBuilder.ts`** -> AI Confidence: **99.31%**
33. **`src/query-builder/SoftDeleteQueryBuilder.ts`** -> AI Confidence: **99.31%**
34. **`src/query-builder/UpdateQueryBuilder.ts`** -> AI Confidence: **99.31%**
35. **`src/query-builder/transformer/RawSqlResultsToEntityTransformer.ts`** -> AI Confidence: **99.31%**
36. **`src/subscriber/EntitySubscriberInterface.ts`** -> AI Confidence: **99.31%**
37. **`packages/codemod/src/cli/parse-args.ts`** -> AI Confidence: **99.29%**
38. **`src/driver/mysql/MysqlConnectionCredentialsOptions.ts`** -> AI Confidence: **99.29%**
39. **`src/driver/oracle/OracleConnectionCredentialsOptions.ts`** -> AI Confidence: **99.29%**
40. **`src/driver/sap/SapConnectionCredentialsOptions.ts`** -> AI Confidence: **99.29%**
41. **`src/entity-schema/EntitySchemaIndexOptions.ts`** -> AI Confidence: **99.29%**
42. **`src/metadata-args/TransactionRepositoryMetadataArgs.ts`** -> AI Confidence: **99.29%**
43. **`src/schema-builder/options/TableColumnOptions.ts`** -> AI Confidence: **99.29%**
44. **`src/cache/DbQueryResultCache.ts`** -> AI Confidence: **99.24%**
45. **`src/data-source/DataSource.ts`** -> AI Confidence: **99.24%**
46. **`src/driver/aurora-mysql/AuroraMysqlDriver.ts`** -> AI Confidence: **99.24%**
47. **`src/driver/mongodb/MongoQueryRunner.ts`** -> AI Confidence: **99.24%**
48. **`src/driver/mysql/MysqlDriver.ts`** -> AI Confidence: **99.24%**
49. **`src/driver/react-native/ReactNativeQueryRunner.ts`** -> AI Confidence: **99.24%**
50. **`src/driver/spanner/SpannerDriver.ts`** -> AI Confidence: **99.24%**
51. **`src/driver/sqlite-abstract/AbstractSqliteQueryRunner.ts`** -> AI Confidence: **99.24%**
52. **`src/driver/sqljs/SqljsQueryRunner.ts`** -> AI Confidence: **99.24%**
53. **`src/driver/sqlserver/SqlServerDriver.ts`** -> AI Confidence: **99.24%**
54. **`src/entity-manager/EntityManager.ts`** -> AI Confidence: **99.24%**
55. **`src/entity-manager/MongoEntityManager.ts`** -> AI Confidence: **99.24%**
56. **`src/entity-schema/EntitySchemaOptions.ts`** -> AI Confidence: **99.24%**
57. **`src/metadata/EntityMetadata.ts`** -> AI Confidence: **99.24%**
58. **`src/migration/MigrationExecutor.ts`** -> AI Confidence: **99.24%**
59. **`src/platform/PlatformTools.ts`** -> AI Confidence: **99.24%**
60. **`src/query-builder/RelationIdLoader.ts`** -> AI Confidence: **99.24%**
61. **`src/query-runner/BaseQueryRunner.ts`** -> AI Confidence: **99.24%**
62. **`src/schema-builder/RdbmsSchemaBuilder.ts`** -> AI Confidence: **99.24%**
63. **`src/schema-builder/table/Table.ts`** -> AI Confidence: **99.24%**
64. **`src/decorator/columns/PrimaryColumn.ts`** -> AI Confidence: **99.23%**
65. **`src/decorator/columns/PrimaryGeneratedColumn.ts`** -> AI Confidence: **99.23%**
66. **`src/driver/better-sqlite3/BetterSqlite3QueryRunner.ts`** -> AI Confidence: **99.23%**
67. **`src/driver/capacitor/CapacitorQueryRunner.ts`** -> AI Confidence: **99.23%**
68. **`src/query-builder/JoinAttribute.ts`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/codemod/src/cli/run-dependencies.ts` -> **100.0%** Exposure
- `packages/codemod/src/cli/run-transforms.ts` -> **100.0%** Exposure
- `packages/codemod/src/dependencies/find-package-json.ts` -> **100.0%** Exposure
- `packages/codemod/src/dependencies/upgrade.ts` -> **100.0%** Exposure
- `packages/codemod/src/transforms/ast-helpers.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `sample/sample32-migrations/migrations/1481283582-first-release-changes.ts` -> **100.0%** Exposure
- `sample/sample32-migrations/migrations/1481521933-second-release-changes.ts` -> **100.0%** Exposure
- `src/commands/MigrationGenerateCommand.ts` -> **100.0%** Exposure
- `src/find-options/operator/Raw.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `gulpfile.ts` -> **100.0%** Exposure
- `packages/codemod/src/cli/run-dependencies.ts` -> **100.0%** Exposure
- `packages/codemod/src/cli/run-transforms.ts` -> **100.0%** Exposure
- `packages/codemod/src/dependencies/find-package-json.ts` -> **100.0%** Exposure
- `packages/codemod/src/dependencies/upgrade.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `229` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/query-builder/transformer/PlainObjectToDatabaseEntityTransformer.ts` (TYPESCRIPT) -> Cumulative Risk: **969.95**
- **Archetype:** `file_cluster_4` (Distance: 11.567 IQR)
- **Magnitude:** 37.15 | **LOC:** 194 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `transform` (Impact: 228.8), `fillEntities` (Impact: 18.9), `addLoadMap` (Impact: 13.3)

### 2. `src/driver/aurora-postgres/AuroraPostgresQueryRunner.ts` (TYPESCRIPT) -> Cumulative Risk: **960.83**
- **Archetype:** `file_cluster_4` (Distance: 14.164 IQR)
- **Magnitude:** 52.96 | **LOC:** 215 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `query` (Impact: 81.8), `startTransaction` (Impact: 71.2), `commitTransaction` (Impact: 35.5)

### 3. `src/persistence/tree/MaterializedPathSubjectExecutor.ts` (TYPESCRIPT) -> Cumulative Risk: **952.9**
- **Archetype:** `file_cluster_4` (Distance: 14.894 IQR)
- **Magnitude:** 34.12 | **LOC:** 184 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `update` (Impact: 143.4), `insert` (Impact: 37.8), `getEntityPath` (Impact: 29.4)

### 4. `src/query-builder/RelationQueryBuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **931.93**
- **Archetype:** `file_cluster_4` (Distance: 14.907 IQR)
- **Magnitude:** 48.13 | **LOC:** 204 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `set` (Impact: 121.5), `remove` (Impact: 103.9), `add` (Impact: 89.8)

### 5. `src/repository/Repository.ts` (TYPESCRIPT) -> Cumulative Risk: **914.63**
- **Archetype:** `file_cluster_4` (Distance: 14.058 IQR)
- **Magnitude:** 84.8 | **LOC:** 838 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createQueryBuilder` (Impact: 40.5), `update` (Impact: 19.0), `extend` (Impact: 17.9)

### 6. `src/schema-builder/RdbmsSchemaBuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **914.09**
- **Archetype:** `file_cluster_4` (Distance: 13.711 IQR)
- **Magnitude:** 326.84 | **LOC:** 1445 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `renameColumns` (Impact: 136.2), `dropOldViews` (Impact: 131.0), `createNewViewIndices` (Impact: 108.0)

### 7. `src/query-builder/SoftDeleteQueryBuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **912.99**
- **Archetype:** `file_cluster_4` (Distance: 13.881 IQR)
- **Magnitude:** 91.15 | **LOC:** 611 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `execute` (Impact: 168.7), `createUpdateExpression` (Impact: 107.3), `orderBy` (Impact: 71.6)

### 8. `src/persistence/tree/NestedSetSubjectExecutor.ts` (TYPESCRIPT) -> Cumulative Risk: **908.27**
- **Archetype:** `file_cluster_4` (Distance: 12.889 IQR)
- **Magnitude:** 54.24 | **LOC:** 394 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `update` (Impact: 146.5), `insert` (Impact: 80.5), `remove` (Impact: 38.8)

### 9. `src/driver/spanner/SpannerQueryRunner.ts` (TYPESCRIPT) -> Cumulative Risk: **903.24**
- **Archetype:** `file_cluster_4` (Distance: 14.265 IQR)
- **Magnitude:** 361.12 | **LOC:** 2501 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `query` (Impact: 413.1), `stream` (Impact: 173.5), `changeColumn` (Impact: 171.6)

### 10. `src/persistence/SubjectTopologicalSorter.ts` (TYPESCRIPT) -> Cumulative Risk: **900.17**
- **Archetype:** `file_cluster_4` (Distance: 14.65 IQR)
- **Magnitude:** 30.97 | **LOC:** 241 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `toposort` (Impact: 86.8), `sort` (Impact: 57.7), `getDependencies` (Impact: 11.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/driver/cockroachdb/CockroachQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.771 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_4: 13.771, file_cluster_17: 14.21, file_cluster_13: 14.346
- **Magnitude:** 576.1 | **LOC:** 4559 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 58.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 172
- **Risk Profile:** Cognitive Load (49.9897%), Tech Debt (7.8141%)
**Top Internal Functions/Classes:**
  * `createIndex` (Impact: 1093.1 | O(N^6) | DB: 172)
  * `changeColumn` (Impact: 720.6 | O(N^6) | DB: 150)
  * `query` (Impact: 413.7 | O(2^N) | DB: 26)
  * `dropColumn` (Impact: 206.4 | O(N^6) | DB: 52)
  * `createTable` (Impact: 99.1 | O(N^6) | DB: 29)
    * *Intent:* /** * Checks if column with the given name exist in the given table. * * @param tableOrName * @param...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 457`, `structural_boundaries: 448`, `args: 221`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 1181`, `dead_code: 14`, `planned_debt: 2`
* *Architecture:* `io: 50`, `api: 28`, `concurrency: 1198`, `import: 30`
* *Defense:* `safety: 52`, `doc: 230`, `immutability_locks: 273`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.629
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.078182
  * `Imports (Out-Degree: 30):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, CockroachDriver, ColumnTypes, TableIndex...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/query-builder/SelectQueryBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.279 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.134 IQR)
- **Top Global Matches:** file_cluster_4: 14.279, file_cluster_13: 14.446, file_cluster_17: 14.494
- **Magnitude:** 553.98 | **LOC:** 4677 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 54.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (46.5197%), Tech Debt (8.5811%)
**Top Internal Functions/Classes:**
  * `buildWhere` (Impact: 832.3 | O(2^N) | DB: 35)
  * `buildOrder` (Impact: 468.2 | O(2^N) | DB: 12)
    * *Intent:* // if real entity relation is involved
  * `join` (Impact: 295.4 | O(2^N) | DB: 12)
    * *Intent:* /** * Adds new AND WHERE with conditions for the given ids. * * Ids are mixed. * It means if you hav...
  * `createOrderByExpression` (Impact: 291.5 | O(N^6) | DB: 15)
  * `createLockExpression` (Impact: 265.5 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 517`, `structural_boundaries: 357`, `args: 178`, `func_start: 119`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `state_mutation: 1035`, `dead_code: 7`, `planned_debt: 6`
* *Architecture:* `io: 20`, `api: 21`, `concurrency: 311`, `import: 47`
* *Defense:* `safety: 52`, `doc: 169`, `sync_locks: 4`, `immutability_locks: 125`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.852
  * `Choke Point (Betweenness):` 0.089865 | `Ripple Effect (Closeness):` 0.169505
  * `Imports (Out-Degree: 44):` SqlServerDriver, OptimisticLockCanNotBeUsedError, EntityNotFoundError, QueryRunner, NoVersionOrUpdateDateColumnError, FindOptionsRelations, EntityMetadata, EntityTarget...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `src/driver/postgres/PostgresQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.635 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.859 IQR)
- **Top Global Matches:** file_cluster_4: 13.635, file_cluster_17: 14.036, file_cluster_13: 14.137
- **Magnitude:** 470.79 | **LOC:** 5280 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 85
- **Risk Profile:** Cognitive Load (49.9683%), Tech Debt (7.7258%)
**Top Internal Functions/Classes:**
  * `clearDatabase` (Impact: 924.9 | O(N^6) | DB: 85)
  * `buildSequenceName` (Impact: 308.5 | O(N^5) | DB: 20)
  * `query` (Impact: 270.7 | O(2^N) | DB: 9)
  * `createTableSql` (Impact: 128.6 | O(N^6) | DB: 45)
  * `renameTable` (Impact: 124.5 | O(N^6) | DB: 45)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 439`, `structural_boundaries: 402`, `args: 174`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 981`, `dead_code: 13`, `planned_debt: 1`
* *Architecture:* `io: 61`, `api: 31`, `concurrency: 829`, `import: 31`
* *Defense:* `safety: 34`, `doc: 157`, `immutability_locks: 257`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.732
  * `Choke Point (Betweenness):` 0.001548 | `Ripple Effect (Closeness):` 0.099892
  * `Imports (Out-Degree: 31):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, TableIndex, TableUnique...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/driver/cockroachdb/CockroachDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.741 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.72 IQR)
- **Top Global Matches:** file_cluster_4: 12.741, file_cluster_13: 12.969, file_cluster_0: 13.022
- **Magnitude:** 390.29 | **LOC:** 1262 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 136
- **Risk Profile:** Cognitive Load (49.23%), Tech Debt (10.1715%)
**Top Internal Functions/Classes:**
  * `prepareHydratedValue` (Impact: 3241.2 | O(2^N) | DB: 136)
  * `preparePersistentValue` (Impact: 101.6 | O(N^4) | DB: 3)
  * `connect` (Impact: 43.2 | O(N^5) | DB: 32)
  * `constructor` (Impact: 31.6 | O(N^4) | DB: 27)
    * *Intent:* /** * The prefix used for the parameters */
  * `afterConnect` (Impact: 9.4 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 288`, `args: 68`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 249`, `dead_code: 3`, `planned_debt: 7`
* *Architecture:* `io: 43`, `api: 7`, `concurrency: 183`, `import: 33`
* *Defense:* `safety: 27`, `doc: 97`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.664
  * `Choke Point (Betweenness):` 0.000968 | `Ripple Effect (Closeness):` 0.092529
  * `Imports (Out-Degree: 32):` CteCapabilities, Driver, IsolationLevel, DateUtils, ColumnMetadata, QueryRunner, TableForeignKey, EntityMetadata...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/driver/spanner/SpannerQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.265 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_4: 14.265, file_cluster_13: 14.888, file_cluster_17: 14.923
- **Magnitude:** 361.12 | **LOC:** 2501 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (49.992%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `query` (Impact: 413.1 | O(2^N) | DB: 22)
  * `stream` (Impact: 173.5 | O(2^N) | DB: 7)
    * *Intent:* /** * Update database schema. * Used for creating/altering/dropping tables, columns, indexes, etc. *...
  * `changeColumn` (Impact: 171.6 | O(N^6) | DB: 33)
  * `addColumn` (Impact: 100.0 | O(2^N) | DB: 24)
  * `dropColumn` (Impact: 91.8 | O(N^5) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 209`, `args: 103`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 630`, `dead_code: 10`
* *Architecture:* `io: 35`, `api: 40`, `concurrency: 953`, `import: 28`
* *Defense:* `safety: 68`, `doc: 214`, `immutability_locks: 140`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.634
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.078216
  * `Imports (Out-Degree: 28):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, TableIndex, TableUnique...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/sqlserver/SqlServerQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.454 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.054 IQR)
- **Top Global Matches:** file_cluster_4: 13.454, file_cluster_17: 13.833, file_cluster_0: 13.959
- **Magnitude:** 350.93 | **LOC:** 4492 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 167
- **Risk Profile:** Cognitive Load (49.9732%), Tech Debt (7.7706%)
**Top Internal Functions/Classes:**
  * `createTable` (Impact: 1261.9 | O(N^6) | DB: 167)
  * `query` (Impact: 429.1 | O(2^N) | DB: 16)
  * `stream` (Impact: 114.5 | O(N^6) | DB: 11)
  * `startTransaction` (Impact: 79.5 | O(N^6) | DB: 19)
  * `rollbackTransaction` (Impact: 32.6 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 333`, `args: 163`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 699`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `io: 85`, `api: 17`, `concurrency: 624`, `import: 32`
* *Defense:* `safety: 36`, `doc: 115`, `sync_locks: 3`, `immutability_locks: 175`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.633
  * `Choke Point (Betweenness):` 0.001393 | `Ripple Effect (Closeness):` 0.101761
  * `Imports (Out-Degree: 31):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, MssqlParameter, TableIndex...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/schema-builder/RdbmsSchemaBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.711 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.268 IQR)
- **Top Global Matches:** file_cluster_4: 13.711, file_cluster_17: 14.019, file_cluster_13: 14.362
- **Magnitude:** 326.84 | **LOC:** 1445 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (65.8165%), Tech Debt (7.9071%)
**Top Internal Functions/Classes:**
  * `renameColumns` (Impact: 136.2 | O(N^6) | DB: 10)
    * *Intent:* // find foreign keys that exist in the schemas but does not exist in the entity metadata
  * `dropOldViews` (Impact: 131.0 | O(N^6) | DB: 16)
  * `createNewViewIndices` (Impact: 108.0 | O(N^6) | DB: 14)
  * `updateExistColumns` (Impact: 102.0 | O(N^6) | DB: 17)
  * `createForeignKeys` (Impact: 99.7 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 291`, `args: 151`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 709`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 3`, `concurrency: 736`, `import: 22`
* *Defense:* `safety: 33`, `doc: 38`, `immutability_locks: 120`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.11
  * `Choke Point (Betweenness):` 0.005379 | `Ripple Effect (Closeness):` 0.123968
  * `Imports (Out-Degree: 21):` View, ViewUtils, DataSource, QueryRunner, TableColumn, EntityMetadata, TableColumnOptions, SchemaBuilder...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/driver/oracle/OracleQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.501 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.102 IQR)
- **Top Global Matches:** file_cluster_4: 13.501, file_cluster_17: 13.895, file_cluster_13: 14.005
- **Magnitude:** 307.08 | **LOC:** 3441 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 142
- **Risk Profile:** Cognitive Load (49.9981%), Tech Debt (7.892%)
**Top Internal Functions/Classes:**
  * `createTable` (Impact: 1404.0 | O(N^6) | DB: 142)
    * *Intent:* /** * Checks if column with the given name exist in the given table. *
  * `query` (Impact: 341.0 | O(2^N) | DB: 11)
    * *Intent:* /**
  * `stream` (Impact: 112.4 | O(2^N) | DB: 6)
  * `createDatabase` (Impact: 43.2 | O(N^5) | DB: 16)
  * `startTransaction` (Impact: 27.4 | O(N^4) | DB: 10)
    * *Intent:* /** * Releases used database connection. * You cannot use query runner methods once its released.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 237`, `args: 110`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 432`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 27`, `api: 13`, `concurrency: 538`, `import: 28`
* *Defense:* `safety: 33`, `doc: 101`, `immutability_locks: 116`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.63
  * `Choke Point (Betweenness):` 0.000164 | `Ripple Effect (Closeness):` 0.089843
  * `Imports (Out-Degree: 28):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, OracleDriver, TableIndex...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/mysql/MysqlQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.305 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.096 IQR)
- **Top Global Matches:** file_cluster_4: 14.305, file_cluster_17: 14.779, file_cluster_13: 14.855
- **Magnitude:** 281.72 | **LOC:** 3635 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 58.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (49.9082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `query` (Impact: 271.4 | O(2^N) | DB: 14)
    * *Intent:* /**
  * `dropColumn` (Impact: 167.8 | O(N^6) | DB: 46)
  * `buildCreateColumnSql` (Impact: 159.2 | O(N^4) | DB: 5)
  * `stream` (Impact: 133.5 | O(2^N) | DB: 3)
  * `dropTable` (Impact: 110.2 | O(N^6) | DB: 31)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 194`, `args: 107`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 576`, `dead_code: 17`
* *Architecture:* `io: 23`, `api: 37`, `concurrency: 690`, `import: 31`
* *Defense:* `safety: 46`, `doc: 151`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.634
  * `Choke Point (Betweenness):` 0.000952 | `Ripple Effect (Closeness):` 0.101761
  * `Imports (Out-Degree: 30):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, TableIndex, TableUnique...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/sqlite-abstract/AbstractSqliteQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.814 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.085 IQR)
- **Top Global Matches:** file_cluster_4: 13.814, file_cluster_17: 14.278, file_cluster_13: 14.416
- **Magnitude:** 276.77 | **LOC:** 2495 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (49.9799%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildCreateColumnSql` (Impact: 228.8 | O(N^6) | DB: 51)
  * `createTableSql` (Impact: 187.4 | O(N^6) | DB: 44)
  * `startTransaction` (Impact: 74.0 | O(N^5) | DB: 15)
    * *Intent:* /**
  * `createTable` (Impact: 62.8 | O(N^6) | DB: 15)
    * *Intent:* /** * Checks if table with the given name exist in the database. * * @param tableOrName
  * `dropTable` (Impact: 51.7 | O(N^4) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 245`, `args: 145`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 503`, `dead_code: 3`
* *Architecture:* `io: 21`, `api: 40`, `concurrency: 768`, `import: 22`
* *Defense:* `safety: 48`, `doc: 193`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.165
  * `Choke Point (Betweenness):` 0.003282 | `Ripple Effect (Closeness):` 0.08697
  * `Imports (Out-Degree: 22):` IsolationLevel, QueryRunner, TableForeignKey, TableUnique, TableIndex, BaseQueryRunner, validate-isolation-level, MetadataTableType...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/driver/aurora-mysql/AuroraMysqlQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.972 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.263 IQR)
- **Top Global Matches:** file_cluster_4: 13.972, file_cluster_17: 14.379, file_cluster_13: 14.517
- **Magnitude:** 251.73 | **LOC:** 3016 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 63.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (49.8845%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dropColumn` (Impact: 151.2 | O(N^6) | DB: 41)
  * `createTableSql` (Impact: 133.3 | O(N^6) | DB: 30)
  * `stream` (Impact: 111.2 | O(2^N) | DB: 2)
  * `query` (Impact: 81.8 | O(2^N) | DB: 2)
    * *Intent:* /**
  * `dropTable` (Impact: 77.6 | O(N^6) | DB: 27)
    * *Intent:* /** * Creates a new database.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 181`, `args: 125`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 505`, `dead_code: 12`
* *Architecture:* `io: 27`, `api: 38`, `concurrency: 645`, `import: 25`
* *Defense:* `safety: 44`, `doc: 175`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.638
  * `Choke Point (Betweenness):` 0.000564 | `Ripple Effect (Closeness):` 0.101761
  * `Imports (Out-Degree: 25):` AuroraMysqlDriver, IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, TableIndex...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/driver/sap/SapQueryRunner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.47 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.235 IQR)
- **Top Global Matches:** file_cluster_4: 13.47, file_cluster_17: 13.868, file_cluster_13: 13.986
- **Magnitude:** 215.15 | **LOC:** 3714 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 54.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 191
- **Risk Profile:** Cognitive Load (49.997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeColumn` (Impact: 714.5 | O(N^6) | DB: 191)
  * `startTransaction` (Impact: 223.3 | O(N^6) | DB: 102)
    * *Intent:* // return the connection back to the pool
  * `renameColumn` (Impact: 34.8 | O(N^4) | DB: 3)
  * `release` (Impact: 21.5 | O(N^5) | DB: 5)
    * *Intent:* // ------------------------------------------------------------------------- // Public Methods // --...
  * `addColumns` (Impact: 8.4 | O(N^3) | DB: 1)
    * *Intent:* /** * Checks if table with the given name exist in the database.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 192`, `args: 119`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 467`, `dead_code: 4`
* *Architecture:* `io: 10`, `api: 7`, `concurrency: 641`, `import: 31`
* *Defense:* `safety: 34`, `doc: 122`, `sync_locks: 1`, `immutability_locks: 125`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.631
  * `Choke Point (Betweenness):` 0.001166 | `Ripple Effect (Closeness):` 0.078216
  * `Imports (Out-Degree: 30):` IsolationLevel, Broadcaster, QueryResult, QueryRunner, TableForeignKey, ColumnTypes, SapDriver, TableIndex...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/entity-manager/EntityManager.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.323 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.049 IQR)
- **Top Global Matches:** file_cluster_4: 14.323, file_cluster_13: 14.402, file_cluster_2: 14.46
- **Magnitude:** 200.04 | **LOC:** 1630 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 117
- **Risk Profile:** Cognitive Load (49.4491%), Tech Debt (7.9924%)
**Top Internal Functions/Classes:**
  * `transaction` (Impact: 1384.2 | O(N^6) | DB: 117)
  * `constructor` (Impact: 10.8 | O(N^3) | DB: 3)
    * *Intent:* // ------------------------------------------------------------------------- // Protected Properties...
  * `connection` (Impact: 2.7 | O(N^2) | DB: 1)
    * *Intent:* // ------------------------------------------------------------------------- // Public Properties //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 195`, `args: 30`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 259`, `dead_code: 9`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 324`, `import: 35`
* *Defense:* `safety: 11`, `doc: 159`, `immutability_locks: 64`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.785
  * `Choke Point (Betweenness):` 0.022623 | `Ripple Effect (Closeness):` 0.131602
  * `Imports (Out-Degree: 34):` InsertResult, IsolationLevel, DataSource, EntityPersistExecutor, FindOneOptions, QueryPartialEntity, EntityNotFoundError, QueryRunner...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/metadata/ColumnMetadata.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.102 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.344 IQR)
- **Top Global Matches:** file_cluster_13: 14.102, file_cluster_0: 14.222, file_cluster_8: 14.237
- **Magnitude:** 192.67 | **LOC:** 1027 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (41.784%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getEntityValue` (Impact: 677.9 | O(2^N) | DB: 43)
  * `default` (Impact: 174.4 | O(2^N) | DB: 11)
    * *Intent:* /** * Indicates if this column is nested set's left column. * Used only in tree entities with nested...
  * `extractEmbeddedColumnValue` (Impact: 156.8 | O(2^N) | DB: 6)
  * `createValueMap` (Impact: 106.0 | O(N^6) | DB: 15)
  * `setEntityValue` (Impact: 105.6 | O(N^6) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 105`, `args: 28`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 567`, `dead_code: 1`
* *Architecture:* `io: 14`, `api: 6`, `concurrency: 12`, `import: 14`
* *Defense:* `safety: 23`, `doc: 67`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.020815 | `Ripple Effect (Closeness):` 0.156228
  * `Imports (Out-Degree: 14):` ColumnTypes, VirtualColumnOptions, DataSource, ObjectLiteral, EntityMetadata, ApplyValueTransformers, ColumnMetadataArgs, Uint8ArrayUtils...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `src/query-builder/UpdateQueryBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.162 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.081 IQR)
- **Top Global Matches:** file_cluster_4: 13.162, file_cluster_13: 13.238, file_cluster_11: 13.42
- **Magnitude:** 169.56 | **LOC:** 822 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (73.159%), Tech Debt (12.8938%)
**Top Internal Functions/Classes:**
  * `where` (Impact: 1141.1 | O(2^N) | DB: 53)
    * *Intent:* // ------------------------------------------------------------------------- // Public Methods // --...
  * `execute` (Impact: 164.3 | O(N^6) | DB: 39)
  * `createOrderByExpression` (Impact: 25.4 | O(N^6) | DB: 1)
    * *Intent:* /** * Sets LIMIT - maximum number of rows to be selected. *
  * `createLimitExpression` (Impact: 22.5 | O(N^4) | DB: 3)
  * `getValueSet` (Impact: 7.2 | O(N^3) | DB: 2)
    * *Intent:* /** * Indicates if entity must be updated after update operation. * This may produce extra query or ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 88`, `args: 17`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 255`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `io: 8`, `api: 5`, `concurrency: 55`, `import: 23`
* *Defense:* `safety: 5`, `doc: 11`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.004
  * `Choke Point (Betweenness):` 0.005191 | `Ripple Effect (Closeness):` 0.122865
  * `Imports (Out-Degree: 23):` SqlServerDriver, ReturningStatementNotSupportedError, DataSource, QueryRunner, AbstractSqliteDriver, EntityPropertyNotFoundError, Brackets, AuroraMysqlDriver...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/data-source/DataSource.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.407 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.159 IQR)
- **Top Global Matches:** file_cluster_4: 14.407, file_cluster_13: 14.622, file_cluster_11: 14.894
- **Magnitude:** 163.73 | **LOC:** 783 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 120
- **Risk Profile:** Cognitive Load (49.9858%), Tech Debt (10.2921%)
**Top Internal Functions/Classes:**
  * `registerQueryBuilders` (Impact: 1127.3 | O(2^N) | DB: 120)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 127`, `args: 29`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 235`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `io: 11`, `api: 1`, `concurrency: 265`, `import: 38`
* *Defense:* `safety: 17`, `doc: 71`, `immutability_locks: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.934
  * `Choke Point (Betweenness):` 0.109038 | `Ripple Effect (Closeness):` 0.145703
  * `Imports (Out-Degree: 35):` DriverFactory, IsolationLevel, SqljsEntityManager, EntityMetadataValidator, QueryRunner, EntityTarget, EntityMetadata, LoggerFactory...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `extra/typeorm-model-shim.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.422 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 1.751 IQR)
- **Top Global Matches:** file_cluster_8: 8.422, file_cluster_7: 9.258, file_cluster_1: 9.519
- **Magnitude:** 160.8 | **LOC:** 294 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Column` (Impact: 1.9 | O(N^1))
  * `CreateDateColumn` (Impact: 1.9 | O(N^1))
  * `DeleteDateColumn` (Impact: 1.9 | O(N^1))
  * `PrimaryGeneratedColumn` (Impact: 1.9 | O(N^1))
  * `PrimaryColumn` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 54`, `args: 54`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `api: 54`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.611
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/subscriber/Broadcaster.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.098 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.814 IQR)
- **Top Global Matches:** file_cluster_4: 14.098, file_cluster_17: 14.314, file_cluster_8: 14.421
- **Magnitude:** 159.12 | **LOC:** 1014 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 155
- **Risk Profile:** Cognitive Load (49.1196%), Tech Debt (8.5906%)
**Top Internal Functions/Classes:**
  * `Load` (Impact: 1049.4 | O(N^6) | DB: 155)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 76`, `args: 77`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 341`, `planned_debt: 2`
* *Architecture:* `api: 2`, `concurrency: 184`, `import: 8`
* *Defense:* `safety: 45`, `doc: 91`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.135
  * `Choke Point (Betweenness):` 0.00343 | `Ripple Effect (Closeness):` 0.123882
  * `Imports (Out-Degree: 8):` RelationMetadata, ObjectLiteral, QueryRunner, EntityMetadata, EntitySubscriberInterface, ColumnMetadata, BroadcasterResult, ObjectUtils
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/driver/sqlite-abstract/AbstractSqliteDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.659 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.004 IQR)
- **Top Global Matches:** file_cluster_13: 11.659, file_cluster_4: 11.792, file_cluster_8: 11.825
- **Magnitude:** 153.72 | **LOC:** 1039 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (34.0135%), Tech Debt (8.6532%)
**Top Internal Functions/Classes:**
  * `compareJsonDefaults` (Impact: 793.8 | O(2^N) | DB: 11)
  * `prepareHydratedValue` (Impact: 197.4 | O(N^6))
  * `preparePersistentValue` (Impact: 97.3 | O(N^4))
  * `escapeQueryWithParameters` (Impact: 80.1 | O(N^6) | DB: 23)
    * *Intent:* /** * Prepares given value to a value to be hydrated, based on its column type or metadata.
  * `normalizeDefault` (Impact: 58.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 192`, `args: 44`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 73`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `io: 26`, `api: 17`, `concurrency: 42`, `import: 25`
* *Defense:* `safety: 13`, `doc: 87`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.309
  * `Choke Point (Betweenness):` 0.00418 | `Ripple Effect (Closeness):` 0.129982
  * `Imports (Out-Degree: 25):` BaseDataSourceOptions, CteCapabilities, Driver, IsolationLevel, DateUtils, ColumnMetadata, QueryRunner, TableForeignKey...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/persistence/SubjectExecutor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.659 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.684 IQR)
- **Top Global Matches:** file_cluster_4: 14.659, file_cluster_17: 14.894, file_cluster_13: 15.073
- **Magnitude:** 135.51 | **LOC:** 1183 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (56.4869%), Tech Debt (9.3363%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 972.0 | O(2^N) | DB: 78)
  * `constructor` (Impact: 7.3 | O(N^2) | DB: 5)
    * *Intent:* /** * Subjects that must be updated. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 74`, `args: 35`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 212`, `dead_code: 11`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 153`, `import: 19`
* *Defense:* `safety: 8`, `doc: 19`, `immutability_locks: 24`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.006446 | `Ripple Effect (Closeness):` 0.086592
  * `Imports (Out-Degree: 18):` SubjectTopologicalSorter, ClosureSubjectExecutor, SaveOptions, MaterializedPathSubjectExecutor, ObjectLiteral, SubjectWithoutIdentifierError, NestedSetSubjectExecutor, QueryRunner...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `extra/typeorm-class-transformer-shim.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.966 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.014 IQR)
- **Top Global Matches:** file_cluster_8: 11.966, file_cluster_0: 12.232, file_cluster_9: 12.279
- **Magnitude:** 134.2 | **LOC:** 267 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.4228%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDesignTypeFunction` (Impact: 11.0 | O(N^2))
    * *Intent:* /**
  * `makePropertyDecorator` (Impact: 5.7 | O(N^1))
  * `ManyToMany` (Impact: 2.1 | O(N^1))
  * `ManyToOne` (Impact: 2.1 | O(N^1))
  * `OneToMany` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 43`, `args: 72`, `func_start: 41`
* *Risk/State:* `dead_code: 4`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.611
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` class-transformer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/driver/oracle/OracleDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.031 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.841 IQR)
- **Top Global Matches:** file_cluster_4: 13.031, file_cluster_13: 13.189, file_cluster_11: 13.446
- **Magnitude:** 129.86 | **LOC:** 1148 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (47.6287%), Tech Debt (9.3349%)
**Top Internal Functions/Classes:**
  * `prepareHydratedValue` (Impact: 116.4 | O(N^5))
  * `preparePersistentValue` (Impact: 105.6 | O(N^5))
  * `createFullType` (Impact: 95.5 | O(N^5) | DB: 3)
  * `findChangedColumns` (Impact: 95.5 | O(N^5) | DB: 4)
  * `columnTypeToNativeParameter` (Impact: 92.4 | O(N^4) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 211`, `args: 47`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 220`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `io: 24`, `api: 18`, `concurrency: 109`, `import: 32`
* *Defense:* `safety: 9`, `doc: 84`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.002002 | `Ripple Effect (Closeness):` 0.109321
  * `Imports (Out-Degree: 32):` CteCapabilities, Driver, IsolationLevel, DateUtils, OnDeleteType, ColumnMetadata, TableForeignKey, EntityMetadata...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/metadata-builder/EntityMetadataBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.365 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.976 IQR)
- **Top Global Matches:** file_cluster_17: 12.365, file_cluster_13: 12.628, file_cluster_8: 12.732
- **Magnitude:** 128.78 | **LOC:** 1282 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (30.7668%), Tech Debt (9.2877%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 363.4 | O(2^N) | DB: 33)
  * `computeEntityMetadataStep1` (Impact: 331.2 | O(N^6) | DB: 35)
  * `createForeignKeys` (Impact: 166.6 | O(N^6) | DB: 9)
  * `computeInverseProperties` (Impact: 57.7 | O(N^6))
  * `createKeysForTableInheritance` (Impact: 37.4 | O(N^5) | DB: 1)
    * *Intent:* /** * Computes all entity metadata's computed properties, and all its sub-metadatas (relations, colu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 193`, `args: 100`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 225`, `dead_code: 9`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 2`, `import: 23`
* *Defense:* `safety: 4`, `doc: 19`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.003909 | `Ripple Effect (Closeness):` 0.092386
  * `Imports (Out-Degree: 23):` MetadataArgsStorage, EmbeddedMetadata, DataSource, ForeignKeyMetadata, EntityListenerMetadata, EntityMetadata, JunctionEntityMetadataBuilder, CheckMetadata...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/entity-manager/MongoEntityManager.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.597 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.792 IQR)
- **Top Global Matches:** file_cluster_2: 13.597, file_cluster_4: 13.671, file_cluster_16: 13.734
- **Magnitude:** 127.85 | **LOC:** 1462 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 58.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (49.5353%), Tech Debt (8.0169%)
**Top Internal Functions/Classes:**
  * `findByIds` (Impact: 75.4 | O(N^6) | DB: 6)
  * `executeFindOne` (Impact: 62.1 | O(N^6) | DB: 10)
    * *Intent:* /** * Initiate an In order bulk write operation, operations will be serially executed in the order t...
  * `update` (Impact: 61.0 | O(2^N) | DB: 4)
  * `delete` (Impact: 60.8 | O(2^N) | DB: 4)
  * `find` (Impact: 40.6 | O(N^6) | DB: 9)
    * *Intent:* // -------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 117`, `args: 19`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 302`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 11`, `concurrency: 300`, `import: 21`
* *Defense:* `safety: 1`, `doc: 160`, `immutability_locks: 75`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.502
  * `Choke Point (Betweenness):` 0.007267 | `Ripple Effect (Closeness):` 0.131796
  * `Imports (Out-Degree: 21):` InsertResult, MongoFindManyOptions, DataSource, QueryPartialEntity, EntityTarget, EntityMetadata, MongoFindOneOptions, PlatformTools...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/driver/mysql/MysqlDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.845 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.968 IQR)
- **Top Global Matches:** file_cluster_4: 12.845, file_cluster_13: 12.89, file_cluster_11: 13.157
- **Magnitude:** 126.78 | **LOC:** 1347 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (43.6434%), Tech Debt (10.4622%)
**Top Internal Functions/Classes:**
  * `getColumnLength` (Impact: 316.8 | O(N^6) | DB: 24)
  * `prepareHydratedValue` (Impact: 216.4 | O(N^5) | DB: 5)
  * `preparePersistentValue` (Impact: 123.4 | O(N^4) | DB: 2)
  * `connect` (Impact: 65.1 | O(N^5) | DB: 42)
    * *Intent:* /** * Max length allowed by MySQL for aliases. * * @see https://dev.mysql.com/doc/refman/5.5/en/iden...
  * `normalizeDefault` (Impact: 62.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 195`, `args: 53`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 207`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `io: 27`, `api: 14`, `concurrency: 93`, `import: 31`
* *Defense:* `safety: 15`, `doc: 81`, `immutability_locks: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.006264 | `Ripple Effect (Closeness):` 0.12749
  * `Imports (Out-Degree: 31):` CteCapabilities, Driver, IsolationLevel, DateUtils, ColumnMetadata, TableForeignKey, EntityMetadata, ColumnTypes...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `sample/sample16-indexes/entity/Post.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, decorators: 7, import: 3
- `sample/sample30-default-order-by/entity/Category.ts` (TYPESCRIPT) | Magnitude: 0.59 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, decorators: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 17.14 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 99, doc: 34, decorators: 27, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/codemod/src/transforms/stats.ts` (TYPESCRIPT) | Magnitude: 9.09 | Delta: **0.352 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, immutability_locks: 12, structural_boundaries: 9, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/codemod/src/transforms/todo.ts` (TYPESCRIPT) | Magnitude: 1.01 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, state_mutation: 3, api: 2
- `packages/codemod/src/transforms/v1/column-unsigned-numeric.ts` (TYPESCRIPT) | Magnitude: 7.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 29, branch: 16, immutability_locks: 16
- `src/error/CircularRelationsError.ts` (TYPESCRIPT) | Magnitude: 0.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, args: 2, func_start: 2
- `src/query-builder/index.ts` (TYPESCRIPT) | Magnitude: 0.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 14, args: 7, import: 7
- `src/commands/MigrationCreateCommand.ts` (TYPESCRIPT) | Magnitude: 5.72 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 29, doc: 16, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/repository/BaseEntity.ts` (TYPESCRIPT) | Magnitude: 41.67 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 314, concurrency: 187, generics: 126, structural_boundaries: 118
- `src/error/LockNotSupportedOnGivenDriverError.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, args: 2, func_start: 2
- `src/subscriber/event/RecoverEvent.ts` (TYPESCRIPT) | Magnitude: 1.2 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, generics: 3, ui_framework: 2, class_start: 1
- `src/subscriber/event/SoftRemoveEvent.ts` (TYPESCRIPT) | Magnitude: 1.2 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, generics: 3, ui_framework: 2, class_start: 1
- `src/error/ConnectionNotFoundError.ts` (TYPESCRIPT) | Magnitude: 0.48 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/codemod/src/transforms/v1/find-options-string-select.ts` (TYPESCRIPT) | Magnitude: 2.86 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 18, immutability_locks: 10, io: 7
- `packages/codemod/src/transforms/v1/datasource-sqlite-options.ts` (TYPESCRIPT) | Magnitude: 1.81 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 15, io: 9, immutability_locks: 6
- `packages/codemod/src/transforms/v1/find-options-string-relations.ts` (TYPESCRIPT) | Magnitude: 10.17 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 23, branch: 15, immutability_locks: 14
- `src/query-builder/transformer/PlainObjectToNewEntityTransformer.ts` (TYPESCRIPT) | Magnitude: 24.29 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 17, branch: 12, state_mutation: 8
- `src/query-builder/RelationLoader.ts` (TYPESCRIPT) | Magnitude: 54.93 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 379, structural_boundaries: 65, branch: 54, doc: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/entity-manager/MongoEntityManager.ts` (TYPESCRIPT) | Magnitude: 127.85 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 810, state_mutation: 302, concurrency: 300, generics: 164

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/driver/sap/SapDriver.ts` (TYPESCRIPT) | Magnitude: 83.89 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 506, structural_boundaries: 182, branch: 172, state_mutation: 129
- `src/commands/SchemaLogCommand.ts` (TYPESCRIPT) | Magnitude: 7.8 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, concurrency: 15, branch: 8
- `src/query-builder/transformer/PlainObjectToDatabaseEntityTransformer.ts` (TYPESCRIPT) | Magnitude: 37.15 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 151, state_mutation: 48, structural_boundaries: 37, concurrency: 28
- `src/commands/QueryCommand.ts` (TYPESCRIPT) | Magnitude: 8.26 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 23, concurrency: 18, branch: 8
- `src/schema-builder/MongoSchemaBuilder.ts` (TYPESCRIPT) | Magnitude: 5.06 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, concurrency: 22, structural_boundaries: 17, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/metadata-builder/EntityMetadataValidator.ts` (TYPESCRIPT) | Magnitude: 47.49 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 218, branch: 55, structural_boundaries: 51, planned_debt: 27
- `src/query-builder/QueryBuilderUtils.ts` (TYPESCRIPT) | Magnitude: 2.41 | Delta: **0.354 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 7, branch: 6, structural_boundaries: 6, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/codemod/src/cli/print-usage.ts` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, doc: 6, decorators: 6, structural_boundaries: 5
- `src/metadata-args/EntityListenerMetadataArgs.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 4, immutability_locks: 3, indent_spaces: 3
- `src/error/OptimisticLockVersionMismatchError.ts` (TYPESCRIPT) | Magnitude: 0.71 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, args: 2, func_start: 2
- `src/entity-schema/EntitySchemaEmbeddedColumnOptions.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 3, indent_spaces: 3, branch: 2
- `src/entity-schema/EntitySchemaExclusionOptions.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 3, indent_spaces: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `docker/oracle/startup/01_init.sql` (SQLITE) | Magnitude: 6.92 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, duplicate_logic: 2, orphaned_logic: 2, state_mutation: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/query-builder/UpdateQueryBuilder.ts` -> Churn: **71.53%** | Cog Load: 73.159% | Debt: 12.8938%
- `src/repository/Repository.ts` -> Churn: **68.26%** | Cog Load: 49.9845% | Debt: 95.3834%
- `src/metadata/IndexMetadata.ts` -> Churn: **60.45%** | Cog Load: 50.1131% | Debt: 12.0278%
- `src/repository/BaseEntity.ts` -> Churn: **60.45%** | Cog Load: 49.9972% | Debt: 99.9982%
- `src/metadata-builder/EntityMetadataValidator.ts` -> Churn: **55.66%** | Cog Load: 6.262% | Debt: 96.5913%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `extra/typeorm-model-shim.js` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 160.8
- `extra/typeorm-class-transformer-shim.js` -> **Piotr Kuczynski** (100.0% isolated ownership) | Magnitude: 134.2
- `src/driver/mongodb/typings.ts` -> **Naor Peled** (100.0% isolated ownership) | Magnitude: 79.45

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/data-source/DataSource.ts` -> **Severity: 10.904** (Bridge: 0.109 * Flux: 100.0%)
- `src/query-builder/SelectQueryBuilder.ts` -> **Severity: 8.986** (Bridge: 0.0899 * Flux: 100.0%)
- `src/metadata-args/MetadataArgsStorage.ts` -> **Severity: 5.738** (Bridge: 0.0608 * Flux: 94.4132%)
- `src/util/InstanceChecker.ts` -> **Severity: 5.279** (Bridge: 0.0528 * Flux: 100.0%)
- `src/metadata/EntityMetadata.ts` -> **Severity: 4.245** (Bridge: 0.0424 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/metadata/EntityMetadata.ts` -> **Severity: 16.544** (Embedded: 0.1665 * Error Risk: 99.3554%)
- `src/query-builder/SelectQueryBuilder.ts` -> **Severity: 16.249** (Embedded: 0.1695 * Error Risk: 95.8622%)
- `src/metadata/ColumnMetadata.ts` -> **Severity: 15.46** (Embedded: 0.1562 * Error Risk: 98.9598%)
- `src/metadata/RelationMetadata.ts` -> **Severity: 14.681** (Embedded: 0.1469 * Error Risk: 99.9415%)
- `src/common/ObjectLiteral.ts` -> **Severity: 14.226** (Embedded: 0.1778 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/error/TypeORMError.ts` -> **Severity: 2610.398** (Blast Radius: 30.12 * Doc Risk: 86.6666%)
- `src/platform/PlatformTools.ts` -> **Severity: 1585.2** (Blast Radius: 15.852 * Doc Risk: 100.0%)
- `src/find-options/FindOperator.ts` -> **Severity: 1257.8** (Blast Radius: 12.578 * Doc Risk: 100.0%)
- `packages/codemod/src/transforms/ast-helpers.ts` -> **Severity: 879.2** (Blast Radius: 8.792 * Doc Risk: 100.0%)
- `src/util/InstanceChecker.ts` -> **Severity: 843.5** (Blast Radius: 8.435 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
