# ARCHITECTURAL_BRIEF: mikro-orm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/mikro-orm` |
| **Timestamp** | `2026-08-07T04:15:29.692602+00:00` |
| **Scan Duration** | `2.47s` |
| **Git Branch** | `master` |
| **Git Commit** | `cb44ba007a75171878bfc59eb899ab395e1119ed` |
| **Git Remote** | `https://github.com/mikro-orm/mikro-orm.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 468 malicious artifacts.

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
> **Architectural Drift Z-Score:** `3.663`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 215 | 37.6% |
| file_cluster_8 | 100 | 17.5% |
| file_cluster_4 | 63 | 11.0% |
| file_cluster_0 | 46 | 8.0% |
| file_cluster_17 | 34 | 5.9% |
| file_cluster_16 | 30 | 5.2% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 23.2 | 7.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 41.3 | 52.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.0 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.7 | 6.0 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 16.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.0 | 0.5 | 0.7 | 0.7 |
| Volatility Exposure | 0.0 | 83.4 | 21.7 | 19.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 30.8 | 17.9 | 0.0 |
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

- `getTableKey` (@ `packages/sql/src/schema/SchemaHelper.ts`) -> Impact: **502.1** | LOC: 841
- `recomputeSingleChangeSet` (@ `packages/core/src/unit-of-work/UnitOfWork.ts`) -> Impact: **484.2** | LOC: 740
- `applyJoinedFilters` (@ `packages/sql/src/query/QueryBuilder.ts`) -> Impact: **477.3** | LOC: 956
- `diffForeignKey` (@ `packages/sql/src/schema/SchemaComparator.ts`) -> Impact: **406.9** | LOC: 417
- `createDatabase` (@ `packages/oracledb/src/OracleSchemaGenerator.ts`) -> Impact: **337.3** | LOC: 485
  * *Intent:* /**
- `populatePolymorphic` (@ `packages/core/src/entity/EntityLoader.ts`) -> Impact: **326.0** | LOC: 446
- `rule` (@ `packages/sql/src/schema/SchemaComparator.ts`) -> Impact: **314.9** | LOC: 375
- `getAllIndexes` (@ `packages/oracledb/src/OracleSchemaHelper.ts`) -> Impact: **306.2** | LOC: 444
- `convertException` (@ `packages/oracledb/src/OracleExceptionConverter.ts`) -> Impact: **298.4** | LOC: 138
  * *Intent:* /**
- `isSimpleRegExp` (@ `packages/sql/src/query/QueryBuilderHelper.ts`) -> Impact: **298.4** | LOC: 599

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests` | 10 | 576.99 | 9.32% | 0.0% |
| `packages/sql/src/query` | 11 | 572.01 | 50.68% | 1.15% |
| `packages/core/src/utils` | 20 | 482.33 | 36.06% | 32.29% |
| `tests/features/reflection/entities-compiled` | 20 | 453.19 | 21.16% | 0.0% |
| `packages/core/src/entity` | 16 | 401.63 | 27.87% | 43.59% |
| `packages/oracledb/src` | 9 | 346.2 | 57.87% | 1.77% |
| `packages/core/src` | 8 | 303.24 | 22.65% | 22.85% |
| `packages/core/src/metadata` | 8 | 279.54 | 39.82% | 5.91% |
| `packages/sql/src/schema` | 6 | 255.0 | 64.42% | 0.0% |
| `packages/core/src/unit-of-work` | 7 | 254.86 | 43.62% | 6.54% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docker/oracle-init.sql` -> **100.0%** Exposure
- `packages/core/src/entity/Reference.ts` -> **100.0%** Exposure
- `packages/core/src/logging/colors.ts` -> **100.0%** Exposure
- `packages/decorators/src/es/CreateRequestContext.ts` -> **100.0%** Exposure
- `packages/mssql/src/UnicodeStringType.ts` -> **99.9891%** Exposure
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
- `packages/core/src/utils/Utils.ts` -> **30** Orphaned Functions | **5** Duplicates
- `packages/core/src/entity/defineEntity.ts` -> **0** Orphaned Functions | **34** Duplicates

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

### Hardcoded Payload Artifacts
- `tests/database/seeder/user.seeder.ts` -> **99.9995%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `544` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/mssql/src/MsSqlSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **710.78**
- **Archetype:** `file_cluster_4` (Distance: 13.254 IQR)
- **Magnitude:** 100.98 | **LOC:** 805 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9924%), Safety Score (95.0235%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 135.3), `createTableColumn` (Impact: 64.7), `getAllColumns` (Impact: 55.6)

### 2. `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **703.39**
- **Archetype:** `file_cluster_4` (Distance: 13.209 IQR)
- **Magnitude:** 126.86 | **LOC:** 1073 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.983%), Cognitive Load (99.0567%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 86.9), `createTableColumn` (Impact: 47.4), `getEnumDefinitions` (Impact: 45.6)

### 3. `packages/core/src/utils/AbstractSchemaGenerator.ts` (TYPESCRIPT) -> Cumulative Risk: **694.95**
- **Archetype:** `file_cluster_4` (Distance: 14.637 IQR)
- **Magnitude:** 43.88 | **LOC:** 168 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.0504%)
- **Heaviest Functions:** `getOrderedMetadata` (Impact: 35.9), `clear` (Impact: 16.4), `refresh` (Impact: 14.7)

### 4. `packages/sql/src/PivotCollectionPersister.ts` (TYPESCRIPT) -> Cumulative Risk: **686.31**
- **Archetype:** `file_cluster_2` (Distance: 11.474 IQR)
- **Magnitude:** 18.33 | **LOC:** 240 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9819%), State Flux (99.3058%), Tech Debt (97.6314%)
- **Heaviest Functions:** `enqueueUpdate` (Impact: 19.5), `execute` (Impact: 16.5), `constructor` (Impact: 11.3)

### 5. `packages/core/src/entity/Collection.ts` (TYPESCRIPT) -> Cumulative Risk: **684.49**
- **Archetype:** `file_cluster_4` (Distance: 14.404 IQR)
- **Magnitude:** 65.67 | **LOC:** 1034 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Safety Score (97.971%)
- **Heaviest Functions:** `propagateToOwningSide` (Impact: 27.6), `slice` (Impact: 16.6), `shouldPropagateToCollection` (Impact: 14.8)

### 6. `packages/core/src/EntityManager.ts` (TYPESCRIPT) -> Cumulative Risk: **672.78**
- **Archetype:** `file_cluster_17` (Distance: 14.339 IQR)
- **Magnitude:** 173.63 | **LOC:** 2902 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8948%), Safety Score (85.9623%)
- **Heaviest Functions:** `preparePopulate` (Impact: 84.9), `applyFilters` (Impact: 42.8), `getJoinedFilters` (Impact: 40.9)

### 7. `packages/core/src/utils/AbstractMigrator.ts` (TYPESCRIPT) -> Cumulative Risk: **671.68**
- **Archetype:** `file_cluster_4` (Distance: 13.468 IQR)
- **Magnitude:** 62.7 | **LOC:** 449 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.9634%)
- **Heaviest Functions:** `filterDown` (Impact: 24.7), `filterUp` (Impact: 17.3), `runMigrations` (Impact: 12.8)

### 8. `packages/oracledb/src/OracleSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **669.85**
- **Archetype:** `file_cluster_4` (Distance: 13.026 IQR)
- **Magnitude:** 90.46 | **LOC:** 794 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.999%), Cognitive Load (98.0956%)
- **Heaviest Functions:** `getAllIndexes` (Impact: 306.2), `getAllColumns` (Impact: 76.0), `loadViews` (Impact: 18.3)

### 9. `packages/sql/src/dialects/sqlite/SqliteSchemaHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **666.59**
- **Archetype:** `file_cluster_4` (Distance: 12.691 IQR)
- **Magnitude:** 84.99 | **LOC:** 745 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getEnumDefinitions` (Impact: 104.0), `alterTable` (Impact: 35.8), `createTableColumn` (Impact: 26.3)

### 10. `packages/sql/src/schema/SqlSchemaGenerator.ts` (TYPESCRIPT) -> Cumulative Risk: **665.42**
- **Archetype:** `file_cluster_4` (Distance: 14.394 IQR)
- **Magnitude:** 58.55 | **LOC:** 694 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.8058%)
- **Heaviest Functions:** `clear` (Impact: 44.3), `ensureDatabase` (Impact: 26.3), `prepareSchemaForComparison` (Impact: 16.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/mysql-schema.sql` (SQLITE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.022 IQR)
- **Top Global Matches:** file_cluster_17: 16.022, file_cluster_8: 16.049, file_cluster_0: 16.144
- **Magnitude:** 320.18 | **LOC:** 201 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CREATE_Statement` (Impact: 1.3)
  * `Declarative_Block` (Impact: 1.1)
  * `Declarative_Block` (Impact: 1.1)
  * `DROP_Statement` (Impact: 1.1)
  * `DROP_Statement` (Impact: 1.1)
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
- **Global Archetype:** `file_cluster_17` (Drift: 13.984 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.722 IQR)
- **Top Global Matches:** file_cluster_17: 13.984, file_cluster_2: 14.246, file_cluster_16: 14.263
- **Magnitude:** 241.82 | **LOC:** 4266 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.3736%), Tech Debt (12.6945%)
**Top Internal Functions/Classes:**
  * `applyJoinedFilters` (Impact: 477.3)
  * `prepareFields` (Impact: 113.0)
  * `getQueryBase` (Impact: 73.2)
    * *Intent:* /** * Adds an AND WHERE clause to the query using a raw SQL string or fragment.
  * `wrapPaginateSubQuery` (Impact: 59.1)
  * `processReturningStatement` (Impact: 51.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 546`, `structural_boundaries: 511`, `args: 146`, `func_start: 85`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 784`, `duplicate_logic: 4`
* *Architecture:* `io: 79`, `api: 31`, `concurrency: 26`, `import: 10`
* *Defense:* `safety: 151`, `doc: 41`, `immutability_locks: 193`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlConnection.js, SqlEntityManager.js, core, AbstractSqlDriver.js, typings.js, NativeQueryBuilder.js, QueryBuilderHelper.js, CriteriaNodeFactory.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/reflection/entities-compiled/BaseEntity3.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.078 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.113 IQR)
- **Top Global Matches:** file_cluster_11: 14.078, file_cluster_0: 14.092, file_cluster_13: 14.179
- **Magnitude:** 235.53 | **LOC:** 21 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
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

### `tests/postgre-schema.sql` (SQLITE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.405 IQR)
- **Top Global Matches:** file_cluster_17: 16.405, file_cluster_8: 16.461, file_cluster_0: 16.533
- **Magnitude:** 175.28 | **LOC:** 136 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CREATE_Statement` (Impact: 1.8)
  * `CREATE_Statement` (Impact: 1.3)
  * `Declarative_Block` (Impact: 1.1)
  * `Declarative_Block` (Impact: 1.1)
  * `DROP_Statement` (Impact: 1.1)
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

### `packages/core/src/EntityManager.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.339 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.617 IQR)
- **Top Global Matches:** file_cluster_17: 14.339, file_cluster_4: 14.402, file_cluster_2: 14.413
- **Magnitude:** 173.63 | **LOC:** 2902 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.9459%), Tech Debt (67.3053%)
**Top Internal Functions/Classes:**
  * `preparePopulate` (Impact: 84.9)
  * `applyFilters` (Impact: 42.8)
  * `getJoinedFilters` (Impact: 40.9)
  * `getDataLoader` (Impact: 34.9)
  * `pruneToOneRelations` (Impact: 26.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 427`, `args: 154`, `func_start: 109`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 500`, `duplicate_logic: 22`
* *Architecture:* `api: 25`, `concurrency: 528`, `import: 29`
* *Defense:* `safety: 132`, `doc: 102`, `sync_locks: 3`, `immutability_locks: 210`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MetadataStorage.js, UnitOfWork.js, Configuration.js, EntityLoader.js, EntityComparator.js, Utils.js, EntityRepository.js, ChangeSet.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/unit-of-work/UnitOfWork.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.35 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.546 IQR)
- **Top Global Matches:** file_cluster_17: 13.35, file_cluster_4: 13.365, file_cluster_13: 13.395
- **Magnitude:** 154.75 | **LOC:** 1677 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.8472%), Tech Debt (17.2231%)
**Top Internal Functions/Classes:**
  * `recomputeSingleChangeSet` (Impact: 484.2)
  * `getById` (Impact: 41.1)
  * `register` (Impact: 35.7)
  * `normalizeEntityData` (Impact: 35.1)
    * *Intent:* /**
  * `findExtraUpdates` (Impact: 33.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 208`, `args: 79`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 212`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 25`, `concurrency: 160`, `import: 23`
* *Defense:* `safety: 68`, `doc: 26`, `immutability_locks: 125`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityComparator.js, MetadataStorage.js, typings.js, ChangeSetPersister.js, IDatabaseDriver.js, CommitOrderCalculator.js, IdentityMap.js, Platform.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/MetadataDiscovery.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.241 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.919 IQR)
- **Top Global Matches:** file_cluster_17: 13.241, file_cluster_13: 13.596, file_cluster_4: 13.672
- **Magnitude:** 142.04 | **LOC:** 2429 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.2062%), Tech Debt (13.7008%)
**Top Internal Functions/Classes:**
  * `initCustomType` (Impact: 243.0)
  * `initManyToManyFields` (Impact: 53.5)
  * `initAccessors` (Impact: 39.9)
  * `initOwnColumns` (Impact: 38.4)
  * `initCheckConstraints` (Impact: 37.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 456`, `structural_boundaries: 286`, `args: 129`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 319`, `dead_code: 5`, `duplicate_logic: 3`
* *Architecture:* `io: 12`, `api: 9`, `concurrency: 40`, `import: 18`
* *Defense:* `safety: 101`, `doc: 13`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Configuration.js, MetadataValidator.js, Platform.js, typings.js, index.js, Utils.js, QueryHelper.js, colors.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/entity-generator/src/SourceFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.319 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.25 IQR)
- **Top Global Matches:** file_cluster_17: 14.319, file_cluster_11: 14.521, file_cluster_13: 14.573
- **Magnitude:** 132.75 | **LOC:** 1232 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.0903%), Tech Debt (8.5362%)
**Top Internal Functions/Classes:**
  * `quote` (Impact: 181.4)
  * `generateImports` (Impact: 68.5)
  * `generate` (Impact: 58.1)
  * `getIndexOptions` (Impact: 26.7)
  * `getUniqueOptions` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 162`, `args: 64`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 908`, `planned_debt: 2`
* *Architecture:* `io: 17`, `api: 9`, `import: 8`
* *Defense:* `safety: 53`, `doc: 2`, `immutability_locks: 116`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CoreImportsHelper.js, node:path, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/NativeQueryBuilder.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.745 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.17 IQR)
- **Top Global Matches:** file_cluster_17: 14.745, file_cluster_8: 14.976, file_cluster_13: 15.003
- **Magnitude:** 127.34 | **LOC:** 706 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.7971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compileSelect` (Impact: 30.4)
  * `addOnConflictClause` (Impact: 30.1)
  * `addCte` (Impact: 23.2)
    * *Intent:* /** * Adds a recursive CTE (`WITH RECURSIVE` on PostgreSQL/MySQL/SQLite, plain `WITH` on MSSQL).
  * `quote` (Impact: 21.3)
  * `from` (Impact: 20.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 103`, `args: 67`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 892`
* *Architecture:* `io: 43`, `api: 8`, `import: 3`
* *Defense:* `safety: 29`, `doc: 8`, `immutability_locks: 46`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlPlatform.js, core, enums.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.209 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.157 IQR)
- **Top Global Matches:** file_cluster_4: 13.209, file_cluster_17: 13.285, file_cluster_8: 13.538
- **Magnitude:** 126.86 | **LOC:** 1073 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.0567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllIndexes` (Impact: 86.9)
  * `createTableColumn` (Impact: 47.4)
  * `getEnumDefinitions` (Impact: 45.6)
  * `getAllForeignKeys` (Impact: 41.3)
  * `getAlterNativeEnumSQL` (Impact: 40.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 176`, `args: 93`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 404`, `dead_code: 1`
* *Architecture:* `io: 16`, `api: 29`, `concurrency: 118`, `import: 6`
* *Defense:* `safety: 35`, `doc: 5`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typings.js, core, SchemaHelper.js, AbstractSqlConnection.js, DatabaseTable.js, DatabaseSchema.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/oracledb/src/OracleSchemaGenerator.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.532 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.865 IQR)
- **Top Global Matches:** file_cluster_4: 14.532, file_cluster_17: 15.238, file_cluster_13: 15.372
- **Magnitude:** 125.94 | **LOC:** 523 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.7586%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createDatabase` (Impact: 337.3)
    * *Intent:* /**
  * `register` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 90`, `args: 22`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 453`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 456`, `import: 3`
* *Defense:* `safety: 57`, `doc: 7`, `immutability_locks: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OracleConnection.js, sql, OracleSchemaHelper.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/entity/EntityLoader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.087 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.764 IQR)
- **Top Global Matches:** file_cluster_17: 13.087, file_cluster_2: 13.356, file_cluster_13: 13.477
- **Magnitude:** 115.86 | **LOC:** 1207 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.4588%), Tech Debt (20.6791%)
**Top Internal Functions/Classes:**
  * `populatePolymorphic` (Impact: 326.0)
  * `populate` (Impact: 87.7)
    * *Intent:* /**
  * `buildFields` (Impact: 84.0)
  * `populateField` (Impact: 71.1)
  * `populateMany` (Impact: 69.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 146`, `args: 63`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 155`, `duplicate_logic: 3`
* *Architecture:* `api: 2`, `concurrency: 107`, `import: 15`
* *Defense:* `safety: 37`, `doc: 23`, `immutability_locks: 117`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Collection.js, MetadataStorage.js, utils.js, EntityManager.js, typings.js, Platform.js, wrap.js, Utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilderHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.203 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.322 IQR)
- **Top Global Matches:** file_cluster_17: 13.203, file_cluster_8: 13.495, file_cluster_13: 13.541
- **Magnitude:** 109.15 | **LOC:** 1525 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.769%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isSimpleRegExp` (Impact: 298.4)
  * `getTPTAliasForProperty` (Impact: 79.8)
  * `getQueryOrderFromObject` (Impact: 49.2)
  * `getValueReplacement` (Impact: 36.4)
  * `joinManyToManyReference` (Impact: 30.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 185`, `args: 67`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 348`
* *Architecture:* `io: 66`, `api: 14`, `import: 6`
* *Defense:* `safety: 70`, `doc: 4`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core, AbstractSqlDriver.js, typings.js, NativeQueryBuilder.js, AbstractSqlPlatform.js, enums.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mssql/src/MsSqlSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.254 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.555 IQR)
- **Top Global Matches:** file_cluster_4: 13.254, file_cluster_17: 13.389, file_cluster_8: 13.646
- **Magnitude:** 100.98 | **LOC:** 805 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.9258%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAllIndexes` (Impact: 135.3)
  * `createTableColumn` (Impact: 64.7)
  * `getAllColumns` (Impact: 55.6)
  * `getCreateIndexSQL` (Impact: 29.9)
  * `alterTableColumn` (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 140`, `args: 73`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 358`
* *Architecture:* `io: 28`, `api: 23`, `concurrency: 96`, `import: 2`
* *Defense:* `safety: 29`, `doc: 3`, `immutability_locks: 109`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UnicodeStringType.js, sql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mongodb/src/MongoConnection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.498 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.027 IQR)
- **Top Global Matches:** file_cluster_4: 13.498, file_cluster_17: 13.827, file_cluster_16: 13.94
- **Magnitude:** 99.4 | **LOC:** 688 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.1568%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `log` (Impact: 51.0)
  * `transformResult` (Impact: 16.4)
  * `case` (Impact: 14.8)
  * `createClient` (Impact: 14.1)
  * `createUpdatePayload` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 159`, `args: 63`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 270`
* *Architecture:* `api: 9`, `concurrency: 415`, `import: 2`
* *Defense:* `safety: 40`, `doc: 4`, `immutability_locks: 49`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core, mongodb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/utils/Utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.816 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.615 IQR)
- **Top Global Matches:** file_cluster_16: 12.816, file_cluster_17: 12.846, file_cluster_11: 12.906
- **Magnitude:** 92.92 | **LOC:** 1131 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.384%), Tech Debt (93.9003%)
**Top Internal Functions/Classes:**
  * `compareObjects` (Impact: 53.1)
    * *Intent:* /** Deeply compares two objects for equality, handling dates, regexes, and raw fragments. */
  * `unwrapProperty` (Impact: 41.8)
  * `getOrderedPrimaryKeys` (Impact: 41.3)
  * `setPayloadProperty` (Impact: 39.4)
  * `detectTypeScriptSupport` (Impact: 37.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 224`, `args: 99`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 121`, `duplicate_logic: 5`, `orphaned_logic: 30`
* *Architecture:* `io: 15`, `api: 7`, `concurrency: 22`, `import: 10`
* *Defense:* `safety: 59`, `doc: 37`, `immutability_locks: 66`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityHelper.js, RawQueryFragment.js, Platform.js, typings.js, Collection.js, wrap.js, Reference.js, clone.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/oracledb/src/OracleSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.026 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.41 IQR)
- **Top Global Matches:** file_cluster_4: 13.026, file_cluster_17: 13.135, file_cluster_8: 13.394
- **Magnitude:** 90.46 | **LOC:** 794 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.0956%), Tech Debt (15.9618%)
**Top Internal Functions/Classes:**
  * `getAllIndexes` (Impact: 306.2)
  * `getAllColumns` (Impact: 76.0)
  * `loadViews` (Impact: 18.3)
  * `getListTablesSQL` (Impact: 14.9)
  * `getAllTables` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 139`, `args: 71`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 300`, `duplicate_logic: 2`
* *Architecture:* `io: 18`, `api: 7`, `concurrency: 105`, `import: 1`
* *Defense:* `safety: 25`, `doc: 1`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/plugin/transformer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.634 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.098 IQR)
- **Top Global Matches:** file_cluster_8: 12.634, file_cluster_17: 12.817, file_cluster_13: 12.852
- **Magnitude:** 88.64 | **LOC:** 1076 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.9502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processFromItem` (Impact: 40.6)
  * `processJoinNode` (Impact: 37.4)
  * `transformRow` (Impact: 35.7)
  * `transformInsertQuery` (Impact: 34.3)
  * `transformUpdateQuery` (Impact: 29.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 124`, `args: 51`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 337`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 31`, `doc: 19`, `immutability_locks: 128`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SqlEntityManager.js, core, kysely, AbstractSqlPlatform.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/dialects/sqlite/SqliteSchemaHelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.691 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.522 IQR)
- **Top Global Matches:** file_cluster_4: 12.691, file_cluster_17: 13.187, file_cluster_13: 13.352
- **Magnitude:** 84.99 | **LOC:** 745 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getEnumDefinitions` (Impact: 104.0)
    * *Intent:* // Use getIndexColumns to support advanced options like sort order and collation
  * `alterTable` (Impact: 35.8)
  * `createTableColumn` (Impact: 26.3)
  * `createTable` (Impact: 25.1)
  * `getAllTables` (Impact: 24.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 111`, `args: 52`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 272`
* *Architecture:* `io: 37`, `api: 18`, `concurrency: 219`, `import: 6`
* *Defense:* `safety: 10`, `doc: 3`, `immutability_locks: 99`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typings.js, core, SchemaHelper.js, AbstractSqlConnection.js, DatabaseTable.js, DatabaseSchema.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/AbstractSqlDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.95 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.971 IQR)
- **Top Global Matches:** file_cluster_4: 12.95, file_cluster_17: 13.097, file_cluster_16: 13.173
- **Magnitude:** 81.87 | **LOC:** 3023 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (78.7971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadPolymorphicPivotInverseSide` (Impact: 153.6)
    * *Intent:* // Copy the value to the unaliased field name and remove the aliased key
  * `loadPolymorphicPivotOwnerSide` (Impact: 69.4)
  * `mapTPTChildFields` (Impact: 28.7)
  * `findOne` (Impact: 23.6)
  * `wrapVirtualExpressionInSubquery` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 176`, `args: 43`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 228`
* *Architecture:* `io: 13`, `api: 12`, `concurrency: 139`, `import: 9`
* *Defense:* `safety: 28`, `doc: 12`, `immutability_locks: 92`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbstractSqlConnection.js, core, SqlEntityManager.js, typings.js, NativeQueryBuilder.js, PivotCollectionPersister.js, QueryBuilder.js, AbstractSqlPlatform.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/drivers/DatabaseDriver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.4 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.071 IQR)
- **Top Global Matches:** file_cluster_4: 13.4, file_cluster_13: 13.573, file_cluster_17: 13.582
- **Magnitude:** 79.99 | **LOC:** 754 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.6448%), Tech Debt (16.6544%)
**Top Internal Functions/Classes:**
  * `mapDataToFieldNames` (Impact: 139.2)
    * *Intent:* /** @internal */
  * `createCondition` (Impact: 42.8)
  * `inlineEmbeddables` (Impact: 40.2)
  * `createReplicas` (Impact: 28.9)
  * `createCursorCondition` (Impact: 26.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 157`, `args: 65`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 153`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 21`, `concurrency: 159`, `import: 19`
* *Defense:* `safety: 40`, `doc: 17`, `immutability_locks: 55`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Configuration.js, EntityComparator.js, MetadataStorage.js, typings.js, exceptions.js, Platform.js, MikroORM.js, RawQueryFragment.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/copy.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.713 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 7.293 IQR)
- **Top Global Matches:** file_cluster_13: 11.713, file_cluster_0: 11.744, file_cluster_4: 11.952
- **Magnitude:** 78.1 | **LOC:** 200 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.3771%), Tech Debt (99.9833%)
**Top Internal Functions/Classes:**
  * `getRootVersion` (Impact: 31.1)
  * `getNextVersion` (Impact: 15.3)
    * *Intent:* /**
  * `rewrite` (Impact: 5.6)
  * `copy` (Impact: 2.4)
  * `rewrite` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 32`, `args: 13`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `concurrency: 10`, `import: 16`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` migrations-mongodb, migrations, node:child_process, entity-generator, node:module, node:fs, node:path, node:url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/EntitySchema.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.329 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.987 IQR)
- **Top Global Matches:** file_cluster_17: 14.329, file_cluster_2: 14.372, file_cluster_13: 14.434
- **Magnitude:** 67.25 | **LOC:** 616 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.2824%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setClass` (Impact: 152.2)
    * *Intent:* /** Sets a custom repository class for this entity. */
  * `initProperties` (Impact: 43.4)
  * `normalizeType` (Impact: 23.6)
  * `init` (Impact: 20.0)
    * *Intent:* /** Returns the entity class name. */
  * `addOneToOne` (Impact: 19.3)
    * *Intent:* /** Adds a one-to-many relation to the entity schema. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 150`, `args: 45`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 248`
* *Architecture:* `api: 9`, `concurrency: 6`, `import: 9`
* *Defense:* `safety: 43`, `doc: 28`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Type.js, BaseEntity.js, typings.js, types.js, Utils.js, EventSubscriber.js, EntityRepository.js, enums.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/naming-strategy/NamingStrategy.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.033 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.304 IQR)
- **Top Global Matches:** file_cluster_8: 11.033, file_cluster_7: 11.181, file_cluster_1: 11.366
- **Magnitude:** 67.1 | **LOC:** 131 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.6312%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 5`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` enums.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/platforms/Platform.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.815 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.143 IQR)
- **Top Global Matches:** file_cluster_13: 12.815, file_cluster_8: 12.973, file_cluster_0: 13.034
- **Magnitude:** 65.77 | **LOC:** 882 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.3724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDefaultMappedType` (Impact: 60.2)
  * `shouldHaveColumn` (Impact: 52.1)
  * `formatQuery` (Impact: 35.0)
  * `processJsonCondition` (Impact: 11.0)
  * `isNumericProperty` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 208`, `args: 123`, `func_start: 114`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 109`
* *Architecture:* `io: 30`, `api: 94`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 43`, `doc: 86`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Configuration.js, ExceptionConverter.js, MikroORM.js, Type.js, NamingStrategy.js, typings.js, EntityManager.js, index.js...
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
- `packages/core/src/entity/EntityFactory.ts` (TYPESCRIPT) | Magnitude: 31.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 301, branch: 119, structural_boundaries: 79, state_mutation: 77
- `packages/sql/src/dialects/sqlite/SqlitePlatform.ts` (TYPESCRIPT) | Magnitude: 14.76 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 56, branch: 38, args: 29
- `tests/entities-mssql/FooParam2.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, decorators: 6, import: 4
- `tests/entities-webpack/BookWp.ts` (TYPESCRIPT) | Magnitude: 0.52 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, decorators: 6, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/core/src/logging/Logger.ts` (TYPESCRIPT) | Magnitude: 3.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, branch: 21, structural_boundaries: 20, doc: 11
- `packages/oracledb/src/OracleMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, generics: 32, structural_boundaries: 28, ui_framework: 24
- `packages/libsql/src/LibSqlMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, generics: 31, structural_boundaries: 28, ui_framework: 23
- `packages/decorators/src/legacy/ManyToMany.ts` (TYPESCRIPT) | Magnitude: 1.12 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 23, generics: 21, ui_framework: 17
- `packages/core/src/utils/Utils.ts` (TYPESCRIPT) | Magnitude: 92.92 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 785, branch: 286, structural_boundaries: 224, state_mutation: 121

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/mongodb/src/MongoDriver.ts` (TYPESCRIPT) | Magnitude: 48.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 409, state_mutation: 186, concurrency: 138, structural_boundaries: 108
- `packages/core/src/unit-of-work/UnitOfWork.ts` (TYPESCRIPT) | Magnitude: 154.75 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 858, branch: 296, state_mutation: 212, structural_boundaries: 208
- `packages/oracledb/src/OraclePlatform.ts` (TYPESCRIPT) | Magnitude: 36.01 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 112, branch: 100, state_mutation: 83
- `tests/mysql-schema.sql` (SQLITE) | Magnitude: 320.18 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 153, duplicate_logic: 149, safety: 119, safety_bypasses: 58
- `packages/core/src/metadata/EntitySchema.ts` (TYPESCRIPT) | Magnitude: 67.25 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 421, state_mutation: 248, structural_boundaries: 150, branch: 136

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/mariadb/src/MariaDbMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/mssql/src/MsSqlMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/mysql/src/MySqlMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/sqlite/src/SqliteMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, generics: 33, structural_boundaries: 28, ui_framework: 25
- `packages/mongodb/src/MongoMikroORM.ts` (TYPESCRIPT) | Magnitude: 1.69 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 30, generics: 22, ui_framework: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/oracledb/src/OracleDriver.ts` (TYPESCRIPT) | Magnitude: 11.41 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 112, state_mutation: 47, structural_boundaries: 43, branch: 31
- `tests/bench/basic.bench.ts` (TYPESCRIPT) | Magnitude: 5.94 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, concurrency: 37, structural_boundaries: 31, immutability_locks: 13
- `tests/database/seeder/database.seeder.ts` (TYPESCRIPT) | Magnitude: 1.01 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, concurrency: 6, import: 4, indent_spaces: 3
- `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` (TYPESCRIPT) | Magnitude: 126.86 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 849, state_mutation: 404, branch: 308, structural_boundaries: 176
- `packages/mongodb/src/MongoEntityRepository.ts` (TYPESCRIPT) | Magnitude: 2.73 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 13, concurrency: 12, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/core/src/types/StringType.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, api: 5, args: 4
- `packages/entity-generator/src/DefineEntitySourceFile.ts` (TYPESCRIPT) | Magnitude: 21.43 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 149, state_mutation: 103, branch: 49, structural_boundaries: 38
- `tests/entities-schema/Author4.ts` (TYPESCRIPT) | Magnitude: 6.64 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 90, concurrency: 24, structural_boundaries: 23, args: 19
- `packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts` (TYPESCRIPT) | Magnitude: 37.98 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 390, structural_boundaries: 142, state_mutation: 130, branch: 104
- `tests/features/reflection/entities/BaseEntity3.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, decorators: 3, import: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/sql/src/AbstractSqlDriver.ts` -> Churn: **78.14%** | Cog Load: 78.7971% | Debt: 0.0%
- `packages/core/src/entity/defineEntity.ts` -> Churn: **76.15%** | Cog Load: 13.415% | Debt: 99.8575%
- `packages/core/src/metadata/MetadataDiscovery.ts` -> Churn: **74.01%** | Cog Load: 70.2062% | Debt: 13.7008%
- `packages/sql/src/query/QueryBuilderHelper.ts` -> Churn: **71.7%** | Cog Load: 90.769% | Debt: 0.0%
- `packages/core/src/EntityManager.ts` -> Churn: **70.4%** | Cog Load: 49.9459% | Debt: 67.3053%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/sql/src/query/QueryBuilder.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 241.82
- `packages/core/src/EntityManager.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 173.63
- `packages/core/src/unit-of-work/UnitOfWork.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 154.75
- `packages/core/src/metadata/MetadataDiscovery.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 142.04
- `packages/entity-generator/src/SourceFile.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 132.75

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/core/src/utils/fs-utils.ts` -> **Severity: 1.935** (Embedded: 0.0245 * Error Risk: 78.9087%)
- `tests/perf/serializing-nested-entities/seeder.ts` -> **Severity: 0.788** (Embedded: 0.0158 * Error Risk: 50.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/core/src/utils/fs-utils.ts` -> **Severity: 888.966** (Blast Radius: 21.12 * Doc Risk: 42.0912%)
- `packages/core/src/entity/index.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)
- `packages/core/src/entity/validators.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)
- `packages/core/src/entity/wrap.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)
- `packages/core/src/errors.ts` -> **Severity: 169.3** (Blast Radius: 1.693 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
