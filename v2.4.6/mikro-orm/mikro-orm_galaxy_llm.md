# ARCHITECTURAL_BRIEF: mikro-orm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/mikro-orm` |
| **Timestamp** | `2026-08-03T19:54:43.632784+00:00` |
| **Scan Duration** | `2.68s` |
| **Git Branch** | `master` |
| **Git Commit** | `cb44ba007a75171878bfc59eb899ab395e1119ed` |
| **Git Remote** | `https://github.com/mikro-orm/mikro-orm.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 468 malicious artifacts.

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
| Total Artifacts | 2384 |
| Analyzed Artifacts (Scanned) | 572 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1812 |
| Total LOC | 46829 |
| Volatility Index | 0.063 |
| % Scanned of codebase = | 24.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4414 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0687 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7464 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 450 | 45430 | 78.7% |
| JSON | 43 | 433 | 7.5% |
| MARKDOWN | 38 | 0 | 6.6% |
| PLAINTEXT | 22 | 0 | 3.8% |
| JAVASCRIPT | 14 | 522 | 2.4% |
| SQLITE | 4 | 324 | 0.7% |
| YAML | 1 | 120 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.654`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 213 | 37.2% |
| file_cluster_8 | 100 | 17.5% |
| file_cluster_4 | 66 | 11.5% |
| file_cluster_0 | 46 | 8.0% |
| file_cluster_17 | 32 | 5.6% |
| file_cluster_16 | 31 | 5.4% |
| file_cluster_2 | 19 | 3.3% |
| file_cluster_11 | 5 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 60 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1812*

**Composition by Extension & Reason:**
- `.ts`: 1110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Unsupported Format (.undeterminable)
- `.md`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4853 LOC), 1x Excluded (Machine-Generated Source Code Signature: 106 LOC)
- `.snap`: 175x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 19x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.css`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.lock')
- `.patch`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 23.3 | 7.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 40.7 | 49.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.4 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.7 | 5.9 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 16.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.0 | 0.5 | 0.7 | 0.7 |
| Volatility Exposure | 0.0 | 83.4 | 21.7 | 19.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.9 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/sql/src/query/QueryBuilder.ts` (Hits: 79)
- `packages/sql/src/query/QueryBuilderHelper.ts` (Hits: 66)
- `tests/mysql-schema.sql` (Hits: 52)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fs-utils.ts** (`packages/core/src/utils/fs-utils.ts`) — 14 inbound connections
2. **seeder.ts** (`tests/perf/serializing-nested-entities/seeder.ts`) — 9 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections
5. **CHANGELOG.md** (`packages/cli/CHANGELOG.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **EntityManager.ts** (`packages/core/src/EntityManager.ts`) — 29 outbound dependencies
2. **Configuration.ts** (`packages/core/src/utils/Configuration.ts`) — 28 outbound dependencies
3. **typings.ts** (`packages/core/src/typings.ts`) — 26 outbound dependencies
4. **index.ts** (`packages/core/src/types/index.ts`) — 25 outbound dependencies
5. **bootstrap.ts** (`tests/bootstrap.ts`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createDatabase` (@ `packages/oracledb/src/OracleSchemaGenerator.ts`) -> Impact: **1589.5** | LOC: 485
  * *Intent:* /**
- `isSimpleRegExp` (@ `packages/sql/src/query/QueryBuilderHelper.ts`) -> Impact: **1372.3** | LOC: 599
- `getAllIndexes` (@ `packages/oracledb/src/OracleSchemaHelper.ts`) -> Impact: **1266.5** | LOC: 444
- `applyJoinedFilters` (@ `packages/sql/src/query/QueryBuilder.ts`) -> Impact: **1121.7** | LOC: 956
- `getTableKey` (@ `packages/sql/src/schema/SchemaHelper.ts`) -> Impact: **962.0** | LOC: 841
- `initCustomType` (@ `packages/core/src/metadata/MetadataDiscovery.ts`) -> Impact: **940.6** | LOC: 208
- `recomputeSingleChangeSet` (@ `packages/core/src/unit-of-work/UnitOfWork.ts`) -> Impact: **903.0** | LOC: 740
- `convertException` (@ `packages/oracledb/src/OracleExceptionConverter.ts`) -> Impact: **881.4** | LOC: 138
  * *Intent:* /**
- `quote` (@ `packages/entity-generator/src/SourceFile.ts`) -> Impact: **869.5** | LOC: 189
- `dynamicImportProvider` (@ `packages/core/src/utils/Configuration.ts`) -> Impact: **649.8** | LOC: 395

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `liftGroupOperators` (@ `packages/core/src/utils/QueryHelper.ts`) -> **O(2^N) [Recursive]**
- `inlinePrimaryKeyObjects` (@ `packages/core/src/utils/QueryHelper.ts`) -> **O(2^N) [Recursive]**
- `quote` (@ `packages/entity-generator/src/SourceFile.ts`) -> **O(2^N) [Recursive]**
- `createDatabase` (@ `packages/oracledb/src/OracleSchemaGenerator.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `isSimpleRegExp` (@ `packages/sql/src/query/QueryBuilderHelper.ts`) -> **O(2^N) [Recursive]**
- `expand` (@ `packages/sql/src/schema/DatabaseTable.ts`) -> **O(2^N) [Recursive]**
- `mapDataToFieldNames` (@ `packages/core/src/drivers/DatabaseDriver.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** @internal */
- `createCursorCondition` (@ `packages/core/src/drivers/DatabaseDriver.ts`) -> **O(2^N) [Recursive]**
- `inlineEmbeddables` (@ `packages/core/src/drivers/DatabaseDriver.ts`) -> **O(2^N) [Recursive]**
- `helper` (@ `packages/core/src/entity/EntityHelper.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // oxfmt-ignore

### Highest Data Gravity (Database Complexity)
- `applyJoinedFilters` (@ `packages/sql/src/query/QueryBuilder.ts`) -> DB Complexity: **336**
- `getTableKey` (@ `packages/sql/src/schema/SchemaHelper.ts`) -> DB Complexity: **315**
- `isSimpleRegExp` (@ `packages/sql/src/query/QueryBuilderHelper.ts`) -> DB Complexity: **221**
- `createDatabase` (@ `packages/oracledb/src/OracleSchemaGenerator.ts`) -> DB Complexity: **175**
  * *Intent:* /**
- `dynamicImport` (@ `packages/core/src/utils/fs-utils.ts`) -> DB Complexity: **148**
- `getAllIndexes` (@ `packages/oracledb/src/OracleSchemaHelper.ts`) -> DB Complexity: **118**
- `generateImports` (@ `packages/entity-generator/src/SourceFile.ts`) -> DB Complexity: **93**
- `compileSelect` (@ `packages/sql/src/dialects/mssql/MsSqlNativeQueryBuilder.ts`) -> DB Complexity: **80**
- `compileSelect` (@ `packages/sql/src/dialects/oracledb/OracleNativeQueryBuilder.ts`) -> DB Complexity: **71**
- `compileSelect` (@ `packages/sql/src/query/NativeQueryBuilder.ts`) -> DB Complexity: **68**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/sql/src/query` | 11 | 756.66 | 50.67% | 0.0% |
| `packages/core/src/utils` | 20 | 661.33 | 36.31% | 22.84% |
| `packages/oracledb/src` | 9 | 650.9 | 57.99% | 0.0% |
| `tests` | 10 | 577.15 | 9.32% | 0.0% |
| `tests/features/reflection/entities-compiled` | 20 | 455.19 | 21.16% | 0.0% |
| `packages/core/src/entity` | 16 | 452.43 | 27.76% | 28.62% |
| `packages/core/src/metadata` | 8 | 427.27 | 40.85% | 4.2% |
| `packages/entity-generator/src` | 7 | 349.22 | 53.64% | 1.22% |
| `packages/core/src` | 8 | 320.0 | 22.72% | 20.19% |
| `packages/sql/src/schema` | 6 | 312.4 | 64.8% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docker/oracle-init.sql` -> **100.0%** Exposure
- `packages/core/src/entity/Reference.ts` -> **99.999%** Exposure
- `packages/decorators/src/es/CreateRequestContext.ts` -> **99.9891%** Exposure
- `packages/mssql/src/UnicodeStringType.ts` -> **99.9891%** Exposure
- `packages/core/src/types/Type.ts` -> **99.9572%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/core/src/connections/Connection.ts` -> **100.0%** Exposure
- `packages/core/src/entity/Collection.ts` -> **100.0%** Exposure
- `packages/core/src/entity/EntityRepository.ts` -> **100.0%** Exposure
- `packages/core/src/entity/WrappedEntity.ts` -> **100.0%** Exposure
- `packages/core/src/events/TransactionEventBroadcaster.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/mysql-schema.sql` -> **0** Orphaned Functions | **149** Duplicates
- `tests/postgre-schema.sql` -> **0** Orphaned Functions | **94** Duplicates
- `docker/oracle-init.sql` -> **0** Orphaned Functions | **40** Duplicates
- `packages/core/src/utils/Utils.ts` -> **30** Orphaned Functions | **2** Duplicates
- `tests/sqlite-schema.sql` -> **0** Orphaned Functions | **27** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/cli/src/CLIHelper.ts`** -> AI Confidence: **99.31%**
2. **`packages/core/src/EntityManager.ts`** -> AI Confidence: **99.31%**
3. **`packages/core/src/drivers/DatabaseDriver.ts`** -> AI Confidence: **99.31%**
4. **`packages/core/src/drivers/IDatabaseDriver.ts`** -> AI Confidence: **99.31%**
5. **`packages/core/src/entity/EntityAssigner.ts`** -> AI Confidence: **99.31%**
6. **`packages/core/src/entity/EntityFactory.ts`** -> AI Confidence: **99.31%**
7. **`packages/core/src/entity/EntityHelper.ts`** -> AI Confidence: **99.31%**
8. **`packages/core/src/entity/EntityLoader.ts`** -> AI Confidence: **99.31%**
9. **`packages/core/src/metadata/EntitySchema.ts`** -> AI Confidence: **99.31%**
10. **`packages/core/src/metadata/MetadataDiscovery.ts`** -> AI Confidence: **99.31%**
11. **`packages/core/src/platforms/Platform.ts`** -> AI Confidence: **99.31%**
12. **`packages/core/src/unit-of-work/ChangeSetComputer.ts`** -> AI Confidence: **99.31%**
13. **`packages/core/src/unit-of-work/UnitOfWork.ts`** -> AI Confidence: **99.31%**
14. **`packages/core/src/utils/Configuration.ts`** -> AI Confidence: **99.31%**
15. **`packages/core/src/utils/EntityComparator.ts`** -> AI Confidence: **99.31%**
16. **`packages/core/src/utils/QueryHelper.ts`** -> AI Confidence: **99.31%**
17. **`packages/core/src/utils/Utils.ts`** -> AI Confidence: **99.31%**
18. **`packages/core/src/utils/fs-utils.ts`** -> AI Confidence: **99.31%**
19. **`packages/entity-generator/src/EntityGenerator.ts`** -> AI Confidence: **99.31%**
20. **`packages/sql/src/AbstractSqlDriver.ts`** -> AI Confidence: **99.31%**
21. **`packages/sql/src/query/QueryBuilder.ts`** -> AI Confidence: **99.31%**
22. **`packages/sql/src/schema/SqlSchemaGenerator.ts`** -> AI Confidence: **99.31%**
23. **`packages/sql/src/typings.ts`** -> AI Confidence: **99.31%**
24. **`tests/entities-mssql/Book2.ts`** -> AI Confidence: **99.31%**
25. **`tests/entities-sql/Book2.ts`** -> AI Confidence: **99.31%**
26. **`scripts/copy.mjs`** -> AI Confidence: **99.31%**
27. **`packages/oracledb/src/OracleExceptionConverter.ts`** -> AI Confidence: **99.29%**
28. **`packages/core/src/entity/Collection.ts`** -> AI Confidence: **99.24%**
29. **`packages/core/src/typings.ts`** -> AI Confidence: **99.24%**
30. **`packages/core/src/unit-of-work/ChangeSetPersister.ts`** -> AI Confidence: **99.24%**
31. **`packages/core/src/utils/Cursor.ts`** -> AI Confidence: **99.24%**
32. **`packages/cli/src/commands/CompileCommand.ts`** -> AI Confidence: **99.23%**
33. **`packages/migrations/src/Migrator.ts`** -> AI Confidence: **99.23%**
34. **`packages/mssql/src/MsSqlPlatform.ts`** -> AI Confidence: **99.23%**
35. **`packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts`** -> AI Confidence: **99.23%**
36. **`packages/sql/src/schema/SchemaComparator.ts`** -> AI Confidence: **99.22%**
37. **`scripts/publish-jsr.mjs`** -> AI Confidence: **99.2%**
38. **`packages/cli/src/CLIConfigurator.ts`** -> AI Confidence: **99.18%**
39. **`packages/core/src/entity/EntityRepository.ts`** -> AI Confidence: **99.18%**
40. **`packages/core/src/entity/Reference.ts`** -> AI Confidence: **99.18%**
41. **`packages/core/src/hydration/ObjectHydrator.ts`** -> AI Confidence: **99.18%**
42. **`packages/core/src/serialization/EntityTransformer.ts`** -> AI Confidence: **99.18%**
43. **`packages/sql/src/SqlEntityManager.ts`** -> AI Confidence: **99.18%**
44. **`tests/features/reflection/entities/Book.ts`** -> AI Confidence: **99.18%**
45. **`packages/core/src/naming-strategy/NamingStrategy.ts`** -> AI Confidence: **99.17%**
46. **`packages/core/src/utils/clone.ts`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/core/src/EntityManager.ts` -> **100.0%** Exposure
- `packages/core/src/drivers/DatabaseDriver.ts` -> **100.0%** Exposure
- `packages/core/src/entity/EntityFactory.ts` -> **100.0%** Exposure
- `packages/core/src/entity/EntityLoader.ts` -> **100.0%** Exposure
- `packages/core/src/metadata/EntitySchema.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `packages/cli/src/commands/CompileCommand.ts` -> **100.0%** Exposure
- `packages/core/src/connections/Connection.ts` -> **100.0%** Exposure
- `packages/core/src/utils/RawQueryFragment.ts` -> **100.0%** Exposure
- `packages/knex-compat/src/raw.ts` -> **100.0%** Exposure
- `packages/migrations/src/Migration.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `tests/database/seeder/user.seeder.ts` -> **99.9995%** Exposure
### Algorithmic DoS Exposure
- `packages/cli/src/commands/DebugCommand.ts` -> **100.0%** Exposure
- `packages/core/src/connections/Connection.ts` -> **100.0%** Exposure
- `packages/core/src/drivers/DatabaseDriver.ts` -> **100.0%** Exposure
- `packages/core/src/entity/Collection.ts` -> **100.0%** Exposure
- `packages/core/src/entity/EntityLoader.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `544` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **952.06**
- **Archetype:** `file_cluster_4` (Distance: 13.216 IQR)
- **Magnitude:** 154.42 | **LOC:** 1073 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 127.2), `getEnumDefinitions` (Impact: 89.6), `createTableColumn` (Impact: 69.9)

### 2. `packages/mssql/src/MsSqlSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **920.42**
- **Archetype:** `file_cluster_4` (Distance: 13.254 IQR)
- **Magnitude:** 150.72 | **LOC:** 805 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 551.2), `getAllColumns` (Impact: 88.7), `createTableColumn` (Impact: 64.7)

### 3. `packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **918.75**
- **Archetype:** `file_cluster_4` (Distance: 12.41 IQR)
- **Magnitude:** 71.42 | **LOC:** 502 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 79.1), `getAllColumns` (Impact: 65.9), `loadViews` (Impact: 53.1)

### 4. `packages/mysql/src/MySqlConnection.ts` (TYPESCRIPT) -> Cumulative Risk: **886.95**
- **Archetype:** `file_cluster_4` (Distance: 13.484 IQR)
- **Magnitude:** 15.06 | **LOC:** 73 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `commit` (Impact: 48.0), `createKyselyDialect` (Impact: 25.0), `mapOptions` (Impact: 11.5)

### 5. `packages/sql/src/schema/SqlSchemaGenerator.ts` (TYPESCRIPT) -> Cumulative Risk: **883.73**
- **Archetype:** `file_cluster_4` (Distance: 14.394 IQR)
- **Magnitude:** 65.93 | **LOC:** 694 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `clear` (Impact: 129.3), `ensureDatabase` (Impact: 38.6), `sortViewsByDependencies` (Impact: 29.9)

### 6. `packages/sql/src/dialects/sqlite/SqliteSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **876.33**
- **Archetype:** `file_cluster_4` (Distance: 12.695 IQR)
- **Magnitude:** 100.82 | **LOC:** 745 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getEnumDefinitions` (Impact: 199.5), `alterTable` (Impact: 52.2), `createTable` (Impact: 36.4)

### 7. `packages/sql/src/dialects/oracledb/OracleNativeQueryBuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **873.81**
- **Archetype:** `file_cluster_17` (Distance: 14.34 IQR)
- **Magnitude:** 66.39 | **LOC:** 310 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `compileUpsert` (Impact: 66.0), `compileSelect` (Impact: 50.8), `markOutBindings` (Impact: 20.6)

### 8. `packages/mariadb/src/MariaDbSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **865.21**
- **Archetype:** `file_cluster_4` (Distance: 11.696 IQR)
- **Magnitude:** 20.11 | **LOC:** 232 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.8047%)
- **Heaviest Functions:** `getAllColumns` (Impact: 56.9), `getAllChecks` (Impact: 45.8), `getChecksSQL` (Impact: 14.0)

### 9. `packages/oracledb/src/OracleConnection.ts` (TYPESCRIPT) -> Cumulative Risk: **861.53**
- **Archetype:** `file_cluster_4` (Distance: 12.691 IQR)
- **Magnitude:** 36.49 | **LOC:** 239 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createKyselyDialect` (Impact: 87.9), `execute` (Impact: 31.4), `transformRawResult` (Impact: 29.6)

### 10. `packages/oracledb/src/OracleSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **859.36**
- **Archetype:** `file_cluster_4` (Distance: 13.042 IQR)
- **Magnitude:** 191.44 | **LOC:** 794 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 1266.5), `getAllColumns` (Impact: 122.0), `loadViews` (Impact: 26.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/mysql-schema.sql` (SQLITE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.022 IQR)
- **Top Global Matches:** file_cluster_17: 16.022, file_cluster_8: 16.049, file_cluster_0: 16.144
- **Magnitude:** 320.18 | **LOC:** 201 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CREATE_Statement` (Impact: 1.3 | O(N^1) | DB: 1)
  * `Declarative_Block` (Impact: 1.1 | O(N^1) | DB: 1)
  * `Declarative_Block` (Impact: 1.1 | O(N^1) | DB: 1)
  * `DROP_Statement` (Impact: 1.1 | O(N^1))
  * `DROP_Statement` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `class_start: 24`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 153`, `duplicate_logic: 149`
* *Architecture:* `io: 52`
* *Defense:* `safety: 119`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.966 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.756 IQR)
- **Top Global Matches:** file_cluster_17: 13.966, file_cluster_2: 14.224, file_cluster_16: 14.254
- **Magnitude:** 294.45 | **LOC:** 4266 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 336
- **Risk Profile:** Cognitive Load (72.9173%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyJoinedFilters` (Impact: 1121.7 | O(N^4) | DB: 336)
  * `mergeOnConditions` (Impact: 180.9 | O(2^N) | DB: 5)
  * `wrapPaginateSubQuery` (Impact: 113.2 | O(N^3) | DB: 28)
  * `getQueryBase` (Impact: 108.2 | O(N^2) | DB: 24)
    * *Intent:* /** * Adds an AND WHERE clause to the query using a raw SQL string or fragment.
  * `finalize` (Impact: 107.9 | O(N^4) | DB: 26)
    * *Intent:* // Normalize sql.ref('prop') to string for proper formula resolution
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 546`, `structural_boundaries: 511`, `args: 135`, `func_start: 85`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 790`
* *Architecture:* `io: 79`, `api: 17`, `concurrency: 26`, `import: 10`
* *Defense:* `safety: 151`, `doc: 41`, `immutability_locks: 193`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CriteriaNodeFactory.js, typings.js, QueryBuilderHelper.js, SqlEntityManager.js, AbstractSqlDriver.js, AbstractSqlConnection.js, core, AbstractSqlPlatform.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/MetadataDiscovery.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.242 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.935 IQR)
- **Top Global Matches:** file_cluster_17: 13.242, file_cluster_13: 13.596, file_cluster_4: 13.673
- **Magnitude:** 252.68 | **LOC:** 2429 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (70.2062%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initCustomType` (Impact: 940.6 | O(2^N) | DB: 10)
  * `initManyToManyFields` (Impact: 153.9 | O(2^N) | DB: 3)
  * `discoverReferences` (Impact: 91.1 | O(2^N) | DB: 9)
  * `initOwnColumns` (Impact: 74.4 | O(N^3))
  * `initCheckConstraints` (Impact: 73.9 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 456`, `structural_boundaries: 286`, `args: 126`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 319`, `dead_code: 5`
* *Architecture:* `io: 12`, `api: 9`, `concurrency: 40`, `import: 18`
* *Defense:* `safety: 101`, `doc: 13`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` QueryHelper.js, typings.js, Configuration.js, index.js, Logger.js, errors.js, colors.js, Utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/oracledb/src/OracleSchemaGenerator.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.532 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.865 IQR)
- **Top Global Matches:** file_cluster_4: 14.532, file_cluster_17: 15.238, file_cluster_13: 15.372
- **Magnitude:** 251.16 | **LOC:** 523 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 175
- **Risk Profile:** Cognitive Load (83.7586%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createDatabase` (Impact: 1589.5 | O(2^N) | DB: 175)
    * *Intent:* /**
  * `register` (Impact: 2.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 90`, `args: 22`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 453`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 456`, `import: 3`
* *Defense:* `safety: 57`, `doc: 7`, `immutability_locks: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sql, OracleConnection.js, OracleSchemaHelper.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/reflection/entities-compiled/BaseEntity3.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.078 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.113 IQR)
- **Top Global Matches:** file_cluster_11: 14.078, file_cluster_0: 14.092, file_cluster_13: 14.179
- **Magnitude:** 235.53 | **LOC:** 21 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (49.9959%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 7`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` legacy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/entity-generator/src/SourceFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.319 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.25 IQR)
- **Top Global Matches:** file_cluster_17: 14.319, file_cluster_11: 14.521, file_cluster_13: 14.573
- **Magnitude:** 212.31 | **LOC:** 1232 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (85.0903%), Tech Debt (8.5362%)
**Top Internal Functions/Classes:**
  * `quote` (Impact: 869.5 | O(2^N) | DB: 64)
  * `generateImports` (Impact: 132.6 | O(N^3) | DB: 93)
  * `generate` (Impact: 85.0 | O(N^2) | DB: 48)
  * `getUniqueOptions` (Impact: 33.3 | O(N^2) | DB: 6)
  * `getIndexOptions` (Impact: 26.7 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 162`, `args: 64`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 908`, `planned_debt: 2`
* *Architecture:* `io: 17`, `api: 9`, `import: 8`
* *Defense:* `safety: 53`, `doc: 2`, `immutability_locks: 116`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path, core, CoreImportsHelper.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilderHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.176 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.329 IQR)
- **Top Global Matches:** file_cluster_17: 13.176, file_cluster_8: 13.465, file_cluster_13: 13.525
- **Magnitude:** 211.01 | **LOC:** 1525 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 221
- **Risk Profile:** Cognitive Load (91.116%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isSimpleRegExp` (Impact: 1372.3 | O(2^N) | DB: 221)
  * `getTPTAliasForProperty` (Impact: 232.2 | O(2^N) | DB: 12)
  * `joinManyToManyReference` (Impact: 45.0 | O(N^2) | DB: 22)
  * `processData` (Impact: 32.8 | O(2^N) | DB: 1)
  * `processJoins` (Impact: 13.9 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 185`, `args: 64`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 348`
* *Architecture:* `io: 66`, `api: 9`, `import: 6`
* *Defense:* `safety: 70`, `doc: 4`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typings.js, AbstractSqlDriver.js, enums.js, core, AbstractSqlPlatform.js, NativeQueryBuilder.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/EntityManager.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.27 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.619 IQR)
- **Top Global Matches:** file_cluster_17: 14.27, file_cluster_4: 14.334, file_cluster_2: 14.344
- **Magnitude:** 191.99 | **LOC:** 2902 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (49.9459%), Tech Debt (53.3998%)
**Top Internal Functions/Classes:**
  * `preparePopulate` (Impact: 158.2 | O(N^4) | DB: 12)
  * `getDataLoader` (Impact: 102.8 | O(2^N) | DB: 1)
  * `getJoinedFilters` (Impact: 59.9 | O(2^N) | DB: 4)
  * `unique` (Impact: 48.2 | O(2^N) | DB: 2)
  * `applyFilters` (Impact: 48.1 | O(N^2) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 427`, `args: 104`, `func_start: 107`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 502`, `duplicate_logic: 18`
* *Architecture:* `api: 24`, `concurrency: 528`, `import: 29`
* *Defense:* `safety: 132`, `doc: 102`, `sync_locks: 3`, `immutability_locks: 210`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RawQueryFragment.js, EntityAssigner.js, EventManager.js, utils.js, validators.js, enums.js, EntityFactory.js, EntityRepository.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/oracledb/src/OracleSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.042 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.418 IQR)
- **Top Global Matches:** file_cluster_4: 13.042, file_cluster_17: 13.15, file_cluster_8: 13.404
- **Magnitude:** 191.44 | **LOC:** 794 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 118
- **Risk Profile:** Cognitive Load (98.0663%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllIndexes` (Impact: 1266.5 | O(2^N) | DB: 118)
  * `getAllColumns` (Impact: 122.0 | O(N^2) | DB: 15)
  * `loadViews` (Impact: 26.9 | O(N^2) | DB: 2)
  * `getListTablesSQL` (Impact: 21.9 | O(N^2) | DB: 3)
  * `getAllTables` (Impact: 12.0 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 139`, `args: 71`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 300`
* *Architecture:* `io: 18`, `api: 7`, `concurrency: 105`, `import: 1`
* *Defense:* `safety: 25`, `doc: 1`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/postgre-schema.sql` (SQLITE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.405 IQR)
- **Top Global Matches:** file_cluster_17: 16.405, file_cluster_8: 16.461, file_cluster_0: 16.533
- **Magnitude:** 175.28 | **LOC:** 136 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CREATE_Statement` (Impact: 1.8 | O(N^1))
  * `CREATE_Statement` (Impact: 1.3 | O(N^1))
  * `Declarative_Block` (Impact: 1.1 | O(N^1) | DB: 1)
  * `Declarative_Block` (Impact: 1.1 | O(N^1) | DB: 1)
  * `DROP_Statement` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 4`, `func_start: 6`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 69`, `duplicate_logic: 94`
* *Architecture:* `io: 42`
* *Defense:* `safety: 113`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/unit-of-work/UnitOfWork.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.273 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.574 IQR)
- **Top Global Matches:** file_cluster_4: 13.273, file_cluster_17: 13.285, file_cluster_13: 13.342
- **Magnitude:** 155.96 | **LOC:** 1677 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (70.3114%), Tech Debt (7.9906%)
**Top Internal Functions/Classes:**
  * `recomputeSingleChangeSet` (Impact: 903.0 | O(N^4) | DB: 60)
  * `getById` (Impact: 57.3 | O(N^3) | DB: 2)
  * `normalizeEntityData` (Impact: 30.7 | O(N^2))
    * *Intent:* /**
  * `register` (Impact: 27.2 | O(N^2) | DB: 3)
  * `computeChangeSet` (Impact: 21.5 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 208`, `args: 53`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 214`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 17`, `concurrency: 185`, `import: 23`
* *Defense:* `safety: 68`, `doc: 26`, `immutability_locks: 125`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChangeSet.js, TransactionEventBroadcaster.js, Utils.js, CommitOrderCalculator.js, Collection.js, Connection.js, wrap.js, ChangeSetPersister.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.216 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.158 IQR)
- **Top Global Matches:** file_cluster_4: 13.216, file_cluster_17: 13.292, file_cluster_8: 13.546
- **Magnitude:** 154.42 | **LOC:** 1073 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (99.0567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllIndexes` (Impact: 127.2 | O(N^2) | DB: 17)
  * `getEnumDefinitions` (Impact: 89.6 | O(N^3) | DB: 2)
  * `createTableColumn` (Impact: 69.9 | O(N^2) | DB: 13)
  * `getAllForeignKeys` (Impact: 65.8 | O(N^2) | DB: 11)
  * `getAlterNativeEnumSQL` (Impact: 60.8 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 176`, `args: 96`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 404`, `dead_code: 1`
* *Architecture:* `io: 16`, `api: 29`, `concurrency: 118`, `import: 6`
* *Defense:* `safety: 35`, `doc: 5`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlConnection.js, SchemaHelper.js, typings.js, core, DatabaseSchema.js, DatabaseTable.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mssql/src/MsSqlSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.254 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.555 IQR)
- **Top Global Matches:** file_cluster_4: 13.254, file_cluster_17: 13.389, file_cluster_8: 13.646
- **Magnitude:** 150.72 | **LOC:** 805 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (94.7842%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllIndexes` (Impact: 551.2 | O(2^N) | DB: 50)
  * `getAllColumns` (Impact: 88.7 | O(N^2) | DB: 14)
  * `createTableColumn` (Impact: 64.7 | O(N^1) | DB: 12)
  * `alterTableColumn` (Impact: 40.1 | O(N^2) | DB: 8)
  * `getDropDefaultsSQL` (Impact: 31.4 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 140`, `args: 73`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 358`
* *Architecture:* `io: 28`, `api: 23`, `concurrency: 96`, `import: 2`
* *Defense:* `safety: 29`, `doc: 3`, `immutability_locks: 109`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sql, UnicodeStringType.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/plugin/transformer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.644 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.098 IQR)
- **Top Global Matches:** file_cluster_8: 12.644, file_cluster_17: 12.827, file_cluster_13: 12.862
- **Magnitude:** 150.5 | **LOC:** 1076 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (58.9502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transformInsertQuery` (Impact: 127.9 | O(2^N) | DB: 12)
  * `transformUpdateQuery` (Impact: 112.9 | O(2^N) | DB: 11)
  * `transformIdentifier` (Impact: 98.9 | O(2^N) | DB: 4)
  * `processFromItem` (Impact: 87.6 | O(N^3) | DB: 16)
  * `transformDeleteQuery` (Impact: 84.7 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 124`, `args: 52`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 337`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 31`, `doc: 19`, `immutability_locks: 128`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SqlEntityManager.js, kysely, core, AbstractSqlPlatform.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/drivers/DatabaseDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.313 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.097 IQR)
- **Top Global Matches:** file_cluster_4: 13.313, file_cluster_13: 13.486, file_cluster_16: 13.494
- **Magnitude:** 144.33 | **LOC:** 754 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (69.6508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mapDataToFieldNames` (Impact: 572.6 | O(2^N) | DB: 16)
    * *Intent:* /** @internal */
  * `createCursorCondition` (Impact: 173.6 | O(2^N) | DB: 14)
  * `inlineEmbeddables` (Impact: 133.9 | O(2^N) | DB: 2)
  * `createReplicas` (Impact: 42.3 | O(N^2) | DB: 3)
  * `isPopulated` (Impact: 28.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 157`, `args: 44`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 153`
* *Architecture:* `io: 7`, `api: 20`, `concurrency: 159`, `import: 19`
* *Defense:* `safety: 40`, `doc: 17`, `immutability_locks: 55`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Utils.js, Collection.js, Connection.js, wrap.js, PolymorphicRef.js, Cursor.js, typings.js, Configuration.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/NativeQueryBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.762 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_17: 14.762, file_cluster_8: 14.994, file_cluster_13: 15.019
- **Magnitude:** 139.19 | **LOC:** 706 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (80.8038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compileSelect` (Impact: 44.3 | O(N^2) | DB: 68)
  * `addOnConflictClause` (Impact: 43.9 | O(N^2) | DB: 40)
  * `from` (Impact: 29.5 | O(N^2) | DB: 6)
  * `compileUpdate` (Impact: 27.8 | O(N^2) | DB: 42)
  * `addLockClause` (Impact: 27.7 | O(N^2) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 103`, `args: 68`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 900`
* *Architecture:* `io: 43`, `api: 8`, `import: 3`
* *Defense:* `safety: 29`, `doc: 8`, `immutability_locks: 46`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlPlatform.js, enums.js, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/entity/EntityLoader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.047 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.799 IQR)
- **Top Global Matches:** file_cluster_17: 13.047, file_cluster_2: 13.313, file_cluster_13: 13.437
- **Magnitude:** 126.28 | **LOC:** 1207 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (58.8108%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `populatePolymorphic` (Impact: 518.3 | O(N^3) | DB: 30)
  * `populate` (Impact: 308.6 | O(2^N) | DB: 12)
    * *Intent:* /**
  * `populateMany` (Impact: 73.8 | O(N^2) | DB: 8)
  * `mergeNestedPopulate` (Impact: 48.4 | O(2^N) | DB: 2)
  * `normalizePopulate` (Impact: 15.4 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 146`, `args: 49`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 157`
* *Architecture:* `api: 2`, `concurrency: 112`, `import: 15`
* *Defense:* `safety: 37`, `doc: 23`, `immutability_locks: 117`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` QueryHelper.js, typings.js, MetadataStorage.js, EntityManager.js, errors.js, Collection.js, Utils.js, enums.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/utils/Utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.726 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.633 IQR)
- **Top Global Matches:** file_cluster_16: 12.726, file_cluster_17: 12.761, file_cluster_11: 12.82
- **Magnitude:** 124.23 | **LOC:** 1131 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (31.384%), Tech Debt (85.9404%)
**Top Internal Functions/Classes:**
  * `_merge` (Impact: 121.8 | O(2^N) | DB: 1)
  * `isPrimaryKey` (Impact: 80.4 | O(2^N))
  * `getOrderedPrimaryKeys` (Impact: 79.6 | O(2^N) | DB: 2)
  * `getPrimaryKeyValues` (Impact: 68.5 | O(2^N) | DB: 1)
  * `detectTypeScriptSupport` (Impact: 55.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 224`, `args: 70`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 121`, `duplicate_logic: 2`, `orphaned_logic: 30`
* *Architecture:* `io: 15`, `api: 7`, `concurrency: 22`, `import: 10`
* *Defense:* `safety: 59`, `doc: 37`, `immutability_locks: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typings.js, Reference.js, clone.js, Collection.js, enums.js, RawQueryFragment.js, wrap.js, EntityHelper.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mongodb/src/MongoConnection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.407 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.037 IQR)
- **Top Global Matches:** file_cluster_4: 13.407, file_cluster_17: 13.736, file_cluster_16: 13.855
- **Magnitude:** 110.7 | **LOC:** 688 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (93.1573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `log` (Impact: 188.9 | O(2^N) | DB: 27)
  * `createClient` (Impact: 20.5 | O(N^2) | DB: 9)
  * `commit` (Impact: 14.2 | O(2^N) | DB: 2)
  * `rollback` (Impact: 14.2 | O(2^N) | DB: 2)
  * `close` (Impact: 13.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 159`, `args: 47`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 270`
* *Architecture:* `api: 7`, `concurrency: 420`, `import: 2`
* *Defense:* `safety: 40`, `doc: 4`, `immutability_locks: 49`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mongodb, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/dialects/sqlite/SqliteSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.695 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.521 IQR)
- **Top Global Matches:** file_cluster_4: 12.695, file_cluster_17: 13.19, file_cluster_13: 13.355
- **Magnitude:** 100.82 | **LOC:** 745 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getEnumDefinitions` (Impact: 199.5 | O(N^3) | DB: 58)
    * *Intent:* // Use getIndexColumns to support advanced options like sort order and collation
  * `alterTable` (Impact: 52.2 | O(N^2) | DB: 23)
  * `createTable` (Impact: 36.4 | O(N^2) | DB: 37)
  * `getAllTables` (Impact: 35.1 | O(N^2) | DB: 4)
  * `loadViews` (Impact: 35.0 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 111`, `args: 53`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 272`
* *Architecture:* `io: 37`, `api: 18`, `concurrency: 219`, `import: 6`
* *Defense:* `safety: 10`, `doc: 3`, `immutability_locks: 99`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlConnection.js, SchemaHelper.js, typings.js, core, DatabaseSchema.js, DatabaseTable.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/utils/QueryHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.786 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.119 IQR)
- **Top Global Matches:** file_cluster_17: 11.786, file_cluster_16: 11.848, file_cluster_8: 11.98
- **Magnitude:** 97.22 | **LOC:** 566 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (30.9794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `liftGroupOperators` (Impact: 283.7 | O(2^N) | DB: 1)
  * `inlinePrimaryKeyObjects` (Impact: 184.9 | O(2^N) | DB: 3)
  * `convertCompositeEntityRefs` (Impact: 154.0 | O(2^N) | DB: 4)
  * `processCustomType` (Impact: 84.9 | O(2^N))
  * `processParams` (Impact: 43.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 116`, `args: 37`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 48`
* *Architecture:* `io: 2`, `api: 5`, `import: 10`
* *Defense:* `safety: 32`, `doc: 7`, `immutability_locks: 36`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typings.js, MetadataStorage.js, Reference.js, Utils.js, JsonType.js, enums.js, RawQueryFragment.js, wrap.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/EntitySchema.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.283 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.998 IQR)
- **Top Global Matches:** file_cluster_17: 14.283, file_cluster_2: 14.327, file_cluster_13: 14.393
- **Magnitude:** 95.43 | **LOC:** 616 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (48.4117%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setClass` (Impact: 573.1 | O(2^N) | DB: 67)
    * *Intent:* /** Sets a custom repository class for this entity. */
  * `constructor` (Impact: 21.1 | O(N^1) | DB: 4)
    * *Intent:* /** @internal Type-level marker for fast entity type inference */
  * `REGISTRY` (Impact: 16.2 | O(2^N))
    * *Intent:* /**
  * `formula` (Impact: 14.2 | O(2^N))
  * `addOneToOne` (Impact: 13.4 | O(N^2) | DB: 2)
    * *Intent:* /** Adds a one-to-many relation to the entity schema. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 150`, `args: 37`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 250`
* *Architecture:* `api: 8`, `concurrency: 6`, `import: 9`
* *Defense:* `safety: 43`, `doc: 28`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typings.js, EntityRepository.js, Utils.js, Type.js, types.js, enums.js, BaseEntity.js, EnumArrayType.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/copy.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.722 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 7.228 IQR)
- **Top Global Matches:** file_cluster_13: 11.722, file_cluster_0: 11.753, file_cluster_4: 11.963
- **Magnitude:** 91.7 | **LOC:** 200 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (69.4138%), Tech Debt (99.8771%)
**Top Internal Functions/Classes:**
  * `getRootVersion` (Impact: 45.8 | O(N^2))
  * `getNextVersion` (Impact: 15.3 | O(N^1) | DB: 3)
    * *Intent:* /**
  * `rewrite` (Impact: 5.6 | O(N^1) | DB: 9)
  * `copy` (Impact: 2.4 | O(N^1))
  * `rewrite` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 32`, `args: 13`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `concurrency: 10`, `import: 16`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` migrations, seeder, node:child_process, migrations-mongodb, node:fs, node:path, node:url, entity-generator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/oracledb/src/OracleExceptionConverter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.372 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.103 IQR)
- **Top Global Matches:** file_cluster_8: 7.372, file_cluster_7: 8.13, file_cluster_1: 8.423
- **Magnitude:** 88.56 | **LOC:** 167 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.4898%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertException` (Impact: 881.4 | O(2^N))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 22`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/AbstractSqlDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.831 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.995 IQR)
- **Top Global Matches:** file_cluster_4: 12.831, file_cluster_17: 12.988, file_cluster_16: 13.067
- **Magnitude:** 88.03 | **LOC:** 3023 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (81.375%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadPolymorphicPivotInverseSide` (Impact: 281.7 | O(N^3) | DB: 38)
    * *Intent:* // Copy the value to the unaliased field name and remove the aliased key
  * `loadPolymorphicPivotOwnerSide` (Impact: 57.6 | O(N^2) | DB: 6)
  * `findOne` (Impact: 18.5 | O(N^1) | DB: 6)
  * `hasToManyJoins` (Impact: 18.0 | O(2^N) | DB: 1)
  * `addTPTPolymorphicJoinsForRelation` (Impact: 14.6 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 176`, `args: 27`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 228`
* *Architecture:* `io: 13`, `api: 11`, `concurrency: 144`, `import: 9`
* *Defense:* `safety: 28`, `doc: 12`, `immutability_locks: 92`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` QueryBuilder.js, AbstractSqlPlatform.js, enums.js, NativeQueryBuilder.js, typings.js, PivotCollectionPersister.js, AbstractSqlConnection.js, core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/entities-webpack/AuthorWp.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 10, decorators: 8, import: 3
- `tests/features/createForeignKeyConstraint/entities/BaseEntity.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, decorators: 2, indent_spaces: 2, class_start: 1
- `tests/entities-mssql/Car2.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, decorators: 9, structural_boundaries: 7, args: 3
- `tests/entities-1/dup2.model.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, decorators: 5, import: 3
- `tests/entities-2/dup2.model.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, decorators: 5, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/features/reflection/entities-compiled/Author.js` (JAVASCRIPT) | Magnitude: 32.44 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 38, reflection_metaprogramming: 19, state_mutation: 18, func_start: 17
- `tests/features/reflection/entities-compiled-error/FooBar.js` (JAVASCRIPT) | Magnitude: 15.66 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, branch: 15, state_mutation: 13, reflection_metaprogramming: 10
- `tests/features/reflection/entities-compiled/FooBar.js` (JAVASCRIPT) | Magnitude: 15.66 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, branch: 15, state_mutation: 13, reflection_metaprogramming: 10
- `tests/features/reflection/entities-compiled/BaseEntity3.js` (JAVASCRIPT) | Magnitude: 235.53 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 14, indent_spaces: 14, state_mutation: 12, structural_boundaries: 7
- `tests/features/reflection/entities-compiled/BaseEntity.js` (JAVASCRIPT) | Magnitude: 16.96 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, branch: 14, state_mutation: 12, reflection_metaprogramming: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/core/src/types/BooleanType.ts` (TYPESCRIPT) | Magnitude: 1.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, api: 5, args: 4
- `packages/sql/src/dialects/sqlite/SqlitePlatform.ts` (TYPESCRIPT) | Magnitude: 17.41 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 56, branch: 38, args: 29
- `tests/entities-mssql/FooParam2.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, decorators: 6, import: 4
- `tests/entities-webpack/BookWp.ts` (TYPESCRIPT) | Magnitude: 0.52 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, decorators: 6, import: 4
- `tests/entities-webpack-invalid/AuthorWpI.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, decorators: 8, structural_boundaries: 6, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/core/src/logging/Logger.ts` (TYPESCRIPT) | Magnitude: 3.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, branch: 21, structural_boundaries: 20, doc: 11
- `packages/oracledb/src/OracleMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, generics: 32, structural_boundaries: 28, ui_framework: 24
- `packages/core/src/entity/EntityFactory.ts` (TYPESCRIPT) | Magnitude: 39.43 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 301, branch: 119, state_mutation: 81, structural_boundaries: 79
- `packages/libsql/src/LibSqlMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, generics: 31, structural_boundaries: 28, ui_framework: 23
- `packages/decorators/src/legacy/ManyToMany.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 23, generics: 21, ui_framework: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/mysql-schema.sql` (SQLITE) | Magnitude: 320.18 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 153, duplicate_logic: 149, safety: 119, safety_bypasses: 58
- `packages/oracledb/src/OraclePlatform.ts` (TYPESCRIPT) | Magnitude: 42.74 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 112, branch: 100, state_mutation: 85
- `packages/core/src/metadata/EntitySchema.ts` (TYPESCRIPT) | Magnitude: 95.43 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 421, state_mutation: 250, structural_boundaries: 150, branch: 136
- `tests/repositories/AuthorRepository.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, generics: 6, ui_framework: 5
- `packages/core/src/utils/upsert-utils.ts` (TYPESCRIPT) | Magnitude: 34.12 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 59, branch: 56, generics: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/mariadb/src/MariaDbMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/mssql/src/MsSqlMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/mysql/src/MySqlMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/sqlite/src/SqliteMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/mongodb/src/MongoMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.95 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 30, generics: 22, ui_framework: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/mongodb/src/MongoDriver.ts` (TYPESCRIPT) | Magnitude: 52.99 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 409, state_mutation: 186, concurrency: 148, structural_boundaries: 108
- `packages/core/src/unit-of-work/UnitOfWork.ts` (TYPESCRIPT) | Magnitude: 155.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 858, branch: 296, state_mutation: 214, structural_boundaries: 208
- `packages/oracledb/src/OracleDriver.ts` (TYPESCRIPT) | Magnitude: 9.61 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 112, state_mutation: 47, structural_boundaries: 43, branch: 31
- `tests/bench/basic.bench.ts` (TYPESCRIPT) | Magnitude: 5.94 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, concurrency: 37, structural_boundaries: 31, immutability_locks: 13
- `tests/database/seeder/database.seeder.ts` (TYPESCRIPT) | Magnitude: 1.01 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, concurrency: 6, import: 4, indent_spaces: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/core/src/types/StringType.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, api: 5, args: 4
- `packages/entity-generator/src/DefineEntitySourceFile.ts` (TYPESCRIPT) | Magnitude: 26.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 149, state_mutation: 103, branch: 49, structural_boundaries: 38
- `tests/entities-schema/Author4.ts` (TYPESCRIPT) | Magnitude: 6.73 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 90, concurrency: 24, structural_boundaries: 23, args: 19
- `packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts` (TYPESCRIPT) | Magnitude: 44.78 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 390, structural_boundaries: 142, state_mutation: 130, branch: 104
- `tests/features/reflection/entities/BaseEntity3.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, decorators: 3, import: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/sql/src/AbstractSqlDriver.ts` -> Churn: **78.14%** | Cog Load: 81.375% | Debt: 0.0%
- `packages/core/src/entity/defineEntity.ts` -> Churn: **76.15%** | Cog Load: 13.4917% | Debt: 90.824%
- `packages/core/src/metadata/MetadataDiscovery.ts` -> Churn: **74.01%** | Cog Load: 70.2062% | Debt: 0.0%
- `packages/sql/src/query/QueryBuilderHelper.ts` -> Churn: **71.7%** | Cog Load: 91.116% | Debt: 0.0%
- `packages/core/src/EntityManager.ts` -> Churn: **70.4%** | Cog Load: 49.9459% | Debt: 53.3998%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/sql/src/query/QueryBuilder.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 294.45
- `packages/core/src/metadata/MetadataDiscovery.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 252.68
- `packages/oracledb/src/OracleSchemaGenerator.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 251.16
- `packages/entity-generator/src/SourceFile.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 212.31
- `packages/sql/src/query/QueryBuilderHelper.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 211.01

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/core/src/utils/fs-utils.ts` -> **Severity: 1.935** (Embedded: 0.0245 * Error Risk: 78.9087%)
- `tests/perf/serializing-nested-entities/seeder.ts` -> **Severity: 0.788** (Embedded: 0.0158 * Error Risk: 50.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/core/src/utils/fs-utils.ts` -> **Severity: 1269.965** (Blast Radius: 21.12 * Doc Risk: 60.1309%)
- `packages/core/src/entity/index.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)
- `packages/core/src/entity/validators.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)
- `packages/core/src/entity/wrap.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)
- `packages/core/src/errors.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
