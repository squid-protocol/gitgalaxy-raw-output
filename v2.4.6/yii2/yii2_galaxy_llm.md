# ARCHITECTURAL_BRIEF: yii2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/yii2` |
| **Timestamp** | `2026-08-03T19:33:56.748551+00:00` |
| **Scan Duration** | `3.0s` |
| **Git Branch** | `master` |
| **Git Commit** | `9265980e089733f657609a37a95ab86176cb6c00` |
| **Git Remote** | `https://github.com/yiisoft/yii2.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 654 malicious artifacts.

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
| Total Artifacts | 2426 |
| Analyzed Artifacts (Scanned) | 679 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1747 |
| Total LOC | 51904 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 28.0% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5201 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1119 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3666 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 58 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 623 | 48650 | 91.8% |
| SQLITE | 28 | 2440 | 4.1% |
| MARKDOWN | 9 | 0 | 1.3% |
| YAML | 6 | 118 | 0.9% |
| PLAINTEXT | 3 | 0 | 0.4% |
| HTML | 3 | 375 | 0.4% |
| JSON | 2 | 220 | 0.3% |
| DOCKERFILE | 1 | 7 | 0.1% |
| JAVASCRIPT | 1 | 80 | 0.1% |
| BATCH | 1 | 14 | 0.1% |
| XML | 1 | 0 | 0.1% |
| CSS | 1 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.154`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 333 | 49.0% |
| file_cluster_8 | 247 | 36.4% |
| file_cluster_9 | 47 | 6.9% |
| file_cluster_2 | 20 | 2.9% |
| file_cluster_0 | 9 | 1.3% |
| file_cluster_7 | 7 | 1.0% |
| file_cluster_6 | 2 | 0.3% |
| file_cluster_17 | 1 | 0.1% |
| file_cluster_4 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1747*

**Composition by Extension & Reason:**
- `.md`: 857x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3209 LOC)
- `.php`: 363x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 53x Excluded (Machine-Generated Source Code Signature: 149 LOC), 1x Excluded (Machine-Generated Source Code Signature: 339 LOC)
- `.png`: 261x Excluded (Explicitly Denied Extension: '.png')
- `.graphml`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC)
- `.neon`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.neon')
- `.vsd`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xlsx`: 3x Excluded (Explicitly Denied Extension: '.xlsx')
- `.dist`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 58.4 | 19.1 | 10.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.8 | 24.9 | 14.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.7 | 4.8 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 52.2 | 85.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 59.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.6 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.4 | 14.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 55.0 | 93.1 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 36.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/data/postgres.sql` (Hits: 90)
- `tests/data/oci.sql` (Hits: 83)
- `tests/data/mysql.sql` (Hits: 76)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Yii.php** (`framework/Yii.php`) — 151 inbound connections
2. **InvalidConfigException.php** (`framework/base/InvalidConfigException.php`) — 91 inbound connections
3. **BaseObject.php** (`framework/base/BaseObject.php`) — 47 inbound connections
4. **Component.php** (`framework/base/Component.php`) — 47 inbound connections
5. **InvalidArgumentException.php** (`framework/base/InvalidArgumentException.php`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **messageConfig.php** (`framework/views/messageConfig.php`) — 95 outbound dependencies
2. **Formatter.php** (`framework/i18n/Formatter.php`) — 75 outbound dependencies
3. **config.php** (`framework/messages/config.php`) — 75 outbound dependencies
4. **YiiRequirementChecker.php** (`framework/requirements/YiiRequirementChecker.php`) — 61 outbound dependencies
5. **requirements.php** (`framework/requirements/requirements.php`) — 61 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `bindActionParams` (@ `framework/console/Controller.php`) -> Impact: **543.7** | LOC: 325
- `translatePattern` (@ `framework/web/UrlRule.php`) -> Impact: **537.4** | LOC: 79
  * *Intent:* /**
- `bindActionParams` (@ `framework/web/Controller.php`) -> Impact: **475.5** | LOC: 296
  * *Intent:* /** * Renders a view in response to an AJAX request. *
- `dumpInternal` (@ `framework/helpers/BaseVarDumper.php`) -> Impact: **403.6** | LOC: 70
- `link` (@ `framework/db/BaseActiveRecord.php`) -> Impact: **381.9** | LOC: 78
- `saveMessagesToDb` (@ `framework/console/controllers/MessageController.php`) -> Impact: **353.5** | LOC: 141
- `copyDirectory` (@ `framework/helpers/BaseFileHelper.php`) -> Impact: **352.8** | LOC: 56
- `parseToken` (@ `framework/i18n/MessageFormatter.php`) -> Impact: **333.6** | LOC: 91
- `runAction` (@ `framework/console/Controller.php`) -> Impact: **330.8** | LOC: 69
  * *Intent:* /** * @deprecated since 2.0.13. Use [[ExitCode::OK]] instead.
- `authenticate` (@ `framework/filters/auth/CompositeAuth.php`) -> Impact: **296.7** | LOC: 54
  * *Intent:* /** * CompositeAuth is an action filter that supports multiple authentication methods at the same time. * * The authentication methods contained by Co...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `toArray` (@ `framework/base/ArrayableTrait.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Returns the list of fields that should be returned by default by [[toArray()]] when no specific fields are specified.
- `scenarios` (@ `framework/base/Model.php`) -> **O(2^N) [Recursive]**
  * *Intent:* * - scenario-based validation * * Model also raises the following events when performing data validation: * * - [[EVENT_BEFORE_VALIDATE]]: an event ra...
- `gcRecursive` (@ `framework/caching/FileCache.php`) -> **O(2^N) [Recursive]**
- `runAction` (@ `framework/console/Controller.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @deprecated since 2.0.13. Use [[ExitCode::OK]] instead.
- `beforeAction` (@ `framework/console/controllers/BaseMigrateController.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @var string|array|null the directory containing the migration classes. This can be either * a [path alias](guide:concept-aliases) or a directory...
- `getModuleCommands` (@ `framework/console/controllers/HelpController.php`) -> **O(2^N) [Recursive]**
- `extractMessagesFromTokens` (@ `framework/console/controllers/MessageController.php`) -> **O(2^N) [Recursive]**
- `setSort` (@ `framework/data/ActiveDataProvider.php`) -> **O(2^N) [Recursive]**
- `joinWith` (@ `framework/db/ActiveQuery.php`) -> **O(2^N) [Recursive]**
- `link` (@ `framework/db/BaseActiveRecord.php`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `DROP_Statement` (@ `tests/data/mssql.sql`) -> DB Complexity: **173**
- `bindActionParams` (@ `framework/console/Controller.php`) -> DB Complexity: **66**
- `ansiToHtml` (@ `framework/helpers/BaseConsole.php`) -> DB Complexity: **50**
  * *Intent:* /** * Resets any ANSI format set by previous method [[beginAnsiFormat()]] * Any output after this will have default text format. * This is equal to ca...
- `asDecimalStringFallback` (@ `framework/i18n/Formatter.php`) -> DB Complexity: **47**
- `parseToken` (@ `framework/i18n/MessageFormatter.php`) -> DB Complexity: **39**
- `bindActionParams` (@ `framework/web/Controller.php`) -> DB Complexity: **37**
  * *Intent:* /** * Renders a view in response to an AJAX request. *
- `sendContent` (@ `framework/web/Response.php`) -> DB Complexity: **37**
- `loadColumnSchema` (@ `framework/db/cubrid/Schema.php`) -> DB Complexity: **35**
- `loadColumnSchema` (@ `framework/db/mssql/Schema.php`) -> DB Complexity: **31**
  * *Intent:* /** * {@inheritdoc}
- `parse` (@ `framework/web/MultipartFormDataParser.php`) -> DB Complexity: **31**
  * *Intent:* * * Usage example: * * ``` * use yii\web\UploadedFile; * * $restRequestData = Yii::$app->request->getBodyParams(); * $uploadedFile = UploadedFile::get...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `framework/web` | 58 | 11764.37 | 22.92% | 41.04% |
| `framework/db` | 46 | 9627.72 | 22.12% | 48.33% |
| `framework/helpers` | 31 | 8343.28 | 18.07% | 35.72% |
| `framework/console/controllers` | 8 | 6341.36 | 37.35% | 44.23% |
| `framework/validators` | 24 | 5013.2 | 33.88% | 61.44% |
| `framework/base` | 49 | 4984.26 | 18.8% | 60.18% |
| `framework/i18n` | 12 | 3923.36 | 23.9% | 55.9% |
| `framework/rbac` | 10 | 2715.17 | 12.7% | 25.23% |
| `framework/data` | 9 | 2282.31 | 30.87% | 62.49% |
| `framework/console` | 9 | 2109.72 | 25.99% | 41.13% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `framework/base/Action.php` -> **100.0%** Exposure
- `framework/base/DynamicContentAwareInterface.php` -> **100.0%** Exposure
- `framework/caching/DummyCache.php` -> **100.0%** Exposure
- `framework/caching/WinCache.php` -> **100.0%** Exposure
- `framework/db/ExpressionInterface.php` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `framework/BaseYii.php` -> **100.0%** Exposure
- `framework/Yii.php` -> **100.0%** Exposure
- `framework/base/ActionFilter.php` -> **100.0%** Exposure
- `framework/base/ArrayableTrait.php` -> **100.0%** Exposure
- `framework/base/Behavior.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/data/oci.sql` -> **0** Orphaned Functions | **173** Duplicates
- `tests/data/postgres.sql` -> **0** Orphaned Functions | **158** Duplicates
- `tests/data/mysql.sql` -> **0** Orphaned Functions | **135** Duplicates
- `tests/data/sqlite.sql` -> **0** Orphaned Functions | **130** Duplicates
- `tests/data/cubrid.sql` -> **0** Orphaned Functions | **95** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`framework/requirements/views/console/index.php`** -> AI Confidence: **99.48%**
2. **`framework/views/errorHandler/exception.php`** -> AI Confidence: **99.48%**
3. **`framework/requirements/views/web/index.php`** -> AI Confidence: **99.34%**
4. **`framework/web/UrlRule.php`** -> AI Confidence: **99.34%**
5. **`framework/BaseYii.php`** -> AI Confidence: **99.31%**
6. **`framework/base/Controller.php`** -> AI Confidence: **99.31%**
7. **`framework/behaviors/AttributeTypecastBehavior.php`** -> AI Confidence: **99.31%**
8. **`framework/console/Controller.php`** -> AI Confidence: **99.31%**
9. **`framework/console/ExitCode.php`** -> AI Confidence: **99.31%**
10. **`framework/console/controllers/AssetController.php`** -> AI Confidence: **99.31%**
11. **`framework/console/controllers/HelpController.php`** -> AI Confidence: **99.31%**
12. **`framework/console/controllers/MessageController.php`** -> AI Confidence: **99.31%**
13. **`framework/db/ColumnSchema.php`** -> AI Confidence: **99.31%**
14. **`framework/db/Connection.php`** -> AI Confidence: **99.31%**
15. **`framework/db/mssql/QueryBuilder.php`** -> AI Confidence: **99.31%**
16. **`framework/db/mysql/Schema.php`** -> AI Confidence: **99.31%**
17. **`framework/db/pgsql/QueryBuilder.php`** -> AI Confidence: **99.31%**
18. **`framework/di/Container.php`** -> AI Confidence: **99.31%**
19. **`framework/filters/AccessRule.php`** -> AI Confidence: **99.31%**
20. **`framework/grid/GridView.php`** -> AI Confidence: **99.31%**
21. **`framework/helpers/BaseArrayHelper.php`** -> AI Confidence: **99.31%**
22. **`framework/helpers/BaseFileHelper.php`** -> AI Confidence: **99.31%**
23. **`framework/helpers/BaseStringHelper.php`** -> AI Confidence: **99.31%**
24. **`framework/i18n/Formatter.php`** -> AI Confidence: **99.31%**
25. **`framework/i18n/MessageFormatter.php`** -> AI Confidence: **99.31%**
26. **`framework/messages/config.php`** -> AI Confidence: **99.31%**
27. **`framework/requirements/YiiRequirementChecker.php`** -> AI Confidence: **99.31%**
28. **`framework/requirements/requirements.php`** -> AI Confidence: **99.31%**
29. **`framework/rest/UrlRule.php`** -> AI Confidence: **99.31%**
30. **`framework/validators/DateValidator.php`** -> AI Confidence: **99.31%**
31. **`framework/validators/FileValidator.php`** -> AI Confidence: **99.31%**
32. **`framework/validators/RequiredValidator.php`** -> AI Confidence: **99.31%**
33. **`framework/validators/UniqueValidator.php`** -> AI Confidence: **99.31%**
34. **`framework/views/messageConfig.php`** -> AI Confidence: **99.31%**
35. **`framework/web/AssetManager.php`** -> AI Confidence: **99.31%**
36. **`framework/web/Controller.php`** -> AI Confidence: **99.31%**
37. **`framework/web/Request.php`** -> AI Confidence: **99.31%**
38. **`framework/web/Response.php`** -> AI Confidence: **99.31%**
39. **`framework/web/User.php`** -> AI Confidence: **99.31%**
40. **`framework/web/View.php`** -> AI Confidence: **99.31%**
41. **`framework/widgets/Breadcrumbs.php`** -> AI Confidence: **99.31%**
42. **`framework/widgets/DetailView.php`** -> AI Confidence: **99.31%**
43. **`framework/widgets/Pjax.php`** -> AI Confidence: **99.31%**
44. **`framework/requirements/views/web/css.php`** -> AI Confidence: **99.29%**
45. **`framework/views/_addColumns.php`** -> AI Confidence: **99.29%**
46. **`framework/views/_addComments.php`** -> AI Confidence: **99.29%**
47. **`framework/views/_addForeignKeys.php`** -> AI Confidence: **99.29%**
48. **`framework/views/_createTable.php`** -> AI Confidence: **99.29%**
49. **`framework/views/_dropColumns.php`** -> AI Confidence: **99.29%**
50. **`framework/views/_dropForeignKeys.php`** -> AI Confidence: **99.29%**
51. **`framework/views/_dropTable.php`** -> AI Confidence: **99.29%**
52. **`framework/views/_foreignTables.php`** -> AI Confidence: **99.29%**
53. **`framework/views/createJunctionMigration.php`** -> AI Confidence: **99.29%**
54. **`framework/views/errorHandler/callStackItem.php`** -> AI Confidence: **99.29%**
55. **`framework/views/errorHandler/error.php`** -> AI Confidence: **99.29%**
56. **`framework/views/errorHandler/previousException.php`** -> AI Confidence: **99.29%**
57. **`tests/data/views/error.php`** -> AI Confidence: **99.29%**
58. **`tests/data/views/errorHandler.php`** -> AI Confidence: **99.29%**
59. **`tests/data/views/errorHandlerForAssetFiles.php`** -> AI Confidence: **99.29%**
60. **`tests/framework/console/controllers/stub/index.php`** -> AI Confidence: **99.29%**
61. **`tests/data/oci/optimize_for_tests.sql`** -> AI Confidence: **99.29%**
62. **`framework/base/ArrayableTrait.php`** -> AI Confidence: **99.24%**
63. **`framework/base/Model.php`** -> AI Confidence: **99.24%**
64. **`framework/caching/Cache.php`** -> AI Confidence: **99.24%**
65. **`framework/captcha/CaptchaAction.php`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `framework/BaseYii.php` -> **100.0%** Exposure
- `framework/base/ActionFilter.php` -> **100.0%** Exposure
- `framework/base/Application.php` -> **100.0%** Exposure
- `framework/base/ArrayableTrait.php` -> **100.0%** Exposure
- `framework/base/Behavior.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `framework/db/Command.php` -> **100.0%** Exposure
- `framework/db/Connection.php` -> **100.0%** Exposure
- `framework/db/DataReader.php` -> **100.0%** Exposure
- `framework/db/Migration.php` -> **100.0%** Exposure
- `framework/db/Transaction.php` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `framework/BaseYii.php` -> **100.0%** Exposure
- `framework/base/ActionFilter.php` -> **100.0%** Exposure
- `framework/base/Application.php` -> **100.0%** Exposure
- `framework/base/ArrayableTrait.php` -> **100.0%** Exposure
- `framework/base/BaseObject.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2580` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `framework/web/Request.php` (PHP) -> Cumulative Risk: **885.06**
- **Archetype:** `file_cluster_8` (Distance: 13.956 IQR)
- **Magnitude:** 1383.36 | **LOC:** 2041 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getUserIpFromIpHeaders` (Impact: 115.7), `getHostInfo` (Impact: 68.8), `getHeaders` (Impact: 68.3)

### 2. `framework/db/mssql/QueryBuilder.php` (PHP) -> Cumulative Risk: **868.27**
- **Archetype:** `file_cluster_13` (Distance: 13.903 IQR)
- **Magnitude:** 946.42 | **LOC:** 692 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 71.4%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `insert` (Impact: 98.4), `upsert` (Impact: 90.5), `oldBuildOrderByAndLimit` (Impact: 45.9)

### 3. `framework/db/Connection.php` (PHP) -> Cumulative Risk: **868.04**
- **Archetype:** `file_cluster_13` (Distance: 14.103 IQR)
- **Magnitude:** 1165.86 | **LOC:** 1289 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `openFromPoolSequentially` (Impact: 112.3), `createPdoInstance` (Impact: 69.1), `transaction` (Impact: 53.0)

### 4. `framework/filters/RateLimiter.php` (PHP) -> Cumulative Risk: **863.44**
- **Archetype:** `file_cluster_13` (Distance: 11.911 IQR)
- **Magnitude:** 105.42 | **LOC:** 166 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9904%)
- **Heaviest Functions:** `beforeAction` (Impact: 25.3), `checkRateLimit` (Impact: 14.5), `addRateLimitHeaders` (Impact: 11.6)

### 5. `framework/db/cubrid/QueryBuilder.php` (PHP) -> Cumulative Risk: **852.41**
- **Archetype:** `file_cluster_13` (Distance: 13.522 IQR)
- **Magnitude:** 393.82 | **LOC:** 294 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `upsert` (Impact: 83.2), `getColumnDefinition` (Impact: 53.2), `resetSequence` (Impact: 26.9)

### 6. `framework/web/DbSession.php` (PHP) -> Cumulative Risk: **852.29**
- **Archetype:** `file_cluster_13` (Distance: 13.87 IQR)
- **Magnitude:** 288.2 | **LOC:** 290 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `regenerateID` (Impact: 95.8), `writeSession` (Impact: 40.7), `openSession` (Impact: 26.6)

### 7. `framework/helpers/BaseConsole.php` (PHP) -> Cumulative Risk: **849.63**
- **Archetype:** `file_cluster_13` (Distance: 14.476 IQR)
- **Magnitude:** 997.8 | **LOC:** 1208 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getScreenSize` (Impact: 123.3), `ansiToHtml` (Impact: 108.1), `ansiColorizedSubstr` (Impact: 100.3)

### 8. `framework/db/oci/Schema.php` (PHP) -> Cumulative Risk: **846.57**
- **Archetype:** `file_cluster_13` (Distance: 13.556 IQR)
- **Magnitude:** 898.14 | **LOC:** 748 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `insert` (Impact: 106.2), `loadTableConstraints` (Impact: 81.8), `createColumn` (Impact: 80.7)

### 9. `framework/db/pgsql/QueryBuilder.php` (PHP) -> Cumulative Risk: **842.62**
- **Archetype:** `file_cluster_13` (Distance: 13.961 IQR)
- **Magnitude:** 655.92 | **LOC:** 541 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `batchInsert` (Impact: 103.1), `alterColumn` (Impact: 80.5), `dropIndex` (Impact: 42.5)

### 10. `framework/db/Schema.php` (PHP) -> Cumulative Risk: **832.22**
- **Archetype:** `file_cluster_13` (Distance: 13.029 IQR)
- **Magnitude:** 484.3 | **LOC:** 870 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `insert` (Impact: 52.9), `getTableMetadata` (Impact: 41.0), `getSchemaMetadata` (Impact: 20.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `framework/i18n/Formatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.303 IQR)
- **Top Global Matches:** file_cluster_13: 14.303, file_cluster_8: 14.418, file_cluster_7: 14.473
- **Magnitude:** 2118.2 | **LOC:** 2198 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (30.4301%), Tech Debt (27.8743%)
**Top Internal Functions/Classes:**
  * `asDecimalStringFallback` (Impact: 181.0 | O(N^6) | DB: 47)
  * `formatNumber` (Impact: 177.4 | O(N^5) | DB: 13)
  * `asShortSize` (Impact: 122.7 | O(N^5) | DB: 5)
  * `asSize` (Impact: 122.7 | O(N^5) | DB: 5)
  * `asCurrency` (Impact: 85.9 | O(N^4) | DB: 14)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 226`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 145`, `high_risk_execution: 8`, `state_mutation: 676`, `orphaned_logic: 16`
* *Architecture:* `api: 48`, `import: 17`
* *Defense:* `safety: 16`, `doc: 247`, `test: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.118
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.003319
  * `Imports (Out-Degree: 9):` 'foot' => 12, $textOptions = [])
    
        if ($value === null) 
            return $this->nullDisplay, 'ton' => 1000000, 
    public function asShortLength($value, 'stone' => 98000, 
    public $timeZone, yii\base\InvalidConfigException, d in the input date value.
     * If you store your data in a different time zone in the database...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseArrayHelper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.506 IQR)
- **Top Global Matches:** file_cluster_13: 14.506, file_cluster_8: 14.566, file_cluster_11: 14.573
- **Magnitude:** 1930.5 | **LOC:** 1104 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (43.0169%), Tech Debt (75.5169%)
**Top Internal Functions/Classes:**
  * `toArray` (Impact: 254.2 | O(2^N) | DB: 9)
  * `getValue` (Impact: 230.2 | O(2^N) | DB: 8)
  * `filter` (Impact: 210.6 | O(2^N) | DB: 17)
    * *Intent:* * ] * ], * '345' => [ * 'tablet' => [ * 'def' => ['id' => '345', 'data' => 'def', 'device' => 'table...
  * `merge` (Impact: 146.8 | O(2^N) | DB: 5)
  * `htmlEncode` (Impact: 91.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 111`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 359`, `planned_debt: 7`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 22`, `doc: 101`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ArrayAccess, yii\base\Arrayable, Yii, $sortFlag = SORT_REGULAR)
    
        $keys = is_array($key) ? $key : [$key], * `SORT_REGULAR`, `SORT_NUMERIC`, `SORT_LOCALE_STRING`, function.sort.php)
     * for more details. When sorting by multiple keys with different sort flags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/MessageController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.767 IQR)
- **Top Global Matches:** file_cluster_13: 13.767, file_cluster_8: 13.954, file_cluster_7: 14.063
- **Magnitude:** 1863.06 | **LOC:** 1028 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (36.9566%), Tech Debt (34.653%)
**Top Internal Functions/Classes:**
  * `saveMessagesToDb` (Impact: 353.5 | O(N^6) | DB: 27)
  * `extractMessagesFromTokens` (Impact: 269.5 | O(2^N) | DB: 24)
  * `saveMessagesToPO` (Impact: 261.6 | O(N^6) | DB: 14)
  * `saveMessagesCategoryToPHP` (Impact: 240.8 | O(N^6) | DB: 14)
  * `actionExtract` (Impact: 89.4 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 110`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 355`, `planned_debt: 6`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 24`, `import: 14`
* *Defense:* `safety: 29`, `doc: 119`, `test: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` yii\helpers\Console, $fileName, list of language codes that the extracted messages
     * should be translated to. For example, ['zh-CN', 
    public $languages = [], yii\i18n\GettextPoFile, yii\console\Exception, d...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/ActiveQuery.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.488 IQR)
- **Top Global Matches:** file_cluster_13: 14.488, file_cluster_8: 14.58, file_cluster_11: 14.637
- **Magnitude:** 1439.6 | **LOC:** 867 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (38.5836%), Tech Debt (25.816%)
**Top Internal Functions/Classes:**
  * `joinWithRelation` (Impact: 193.3 | O(2^N) | DB: 9)
    * *Intent:* * } * ])->all(); * // find all orders that contain books of the category 'Science fiction', using th...
  * `joinWith` (Impact: 127.5 | O(2^N) | DB: 9)
  * `prepare` (Impact: 124.7 | O(N^6) | DB: 17)
    * *Intent:* * - [[max()]]: returns the max over the specified column. * - [[scalar()]]: returns the value of the...
  * `removeDuplicatedModels` (Impact: 93.2 | O(N^6) | DB: 11)
  * `buildJoinWith` (Impact: 81.5 | O(N^6) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 79`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 362`, `dead_code: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 35`, `doc: 97`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.94
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.013728
  * `Imports (Out-Degree: 3):` ActiveRelationTrait, ActiveQueryTrait, yii\base\InvalidConfigException
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `framework/web/UrlRule.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.708 IQR)
- **Top Global Matches:** file_cluster_13: 14.708, file_cluster_0: 14.838, file_cluster_11: 14.866
- **Magnitude:** 1405.22 | **LOC:** 605 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (41.4855%), Tech Debt (35.5754%)
**Top Internal Functions/Classes:**
  * `translatePattern` (Impact: 537.4 | O(2^N) | DB: 21)
    * *Intent:* /**
  * `createUrl` (Impact: 256.2 | O(N^6) | DB: 21)
  * `parseRequest` (Impact: 122.9 | O(N^5) | DB: 18)
  * `init` (Impact: 69.0 | O(N^5) | DB: 8)
    * *Intent:* /**
  * `preparePattern` (Impact: 58.1 | O(N^4) | DB: 15)
    * *Intent:* /** * @var int|null a value indicating if this rule should be used for both request parsing and URL ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 57`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 277`, `dead_code: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 21`, `import: 3`
* *Defense:* `safety: 22`, `doc: 72`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ', dPatternPart = $this->pattern, Yii, ') === '') 
            $this->translatePattern(false, $requiredPatternPart, ", yii\base\InvalidConfigException, yii\base\BaseObject...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/BaseMigrateController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.995 IQR)
- **Top Global Matches:** file_cluster_13: 13.995, file_cluster_8: 14.198, file_cluster_7: 14.323
- **Magnitude:** 1392.04 | **LOC:** 1020 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 88.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (38.6367%), Tech Debt (56.7602%)
**Top Internal Functions/Classes:**
  * `beforeAction` (Impact: 123.0 | O(2^N) | DB: 6)
    * *Intent:* /** * @var string|array|null the directory containing the migration classes. This can be either * a ...
  * `getNewMigrations` (Impact: 117.6 | O(N^6) | DB: 12)
  * `actionUp` (Impact: 116.5 | O(N^5) | DB: 15)
    * *Intent:* /** * @var string the template file for generating new migrations. * This can be either a [path alia...
  * `actionRedo` (Impact: 103.1 | O(N^5) | DB: 10)
  * `actionDown` (Impact: 96.2 | O(N^5) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 175`, `args: 28`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 344`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 18`, `import: 15`
* *Defense:* `safety: 22`, `doc: 96`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001475
  * `Imports (Out-Degree: 9):` yii\helpers\Console, yii\base\InvalidConfigException, yii\helpers\Inflector, yii\console\Exception, '\\', _once $file, Yii, s the migration file for a given migration class name.
     *
     * This function will do nothing on namespaced migrations...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `framework/web/Request.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.956 IQR)
- **Top Global Matches:** file_cluster_8: 13.956, file_cluster_13: 13.972, file_cluster_7: 14.017
- **Magnitude:** 1383.36 | **LOC:** 2041 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (46.7737%), Tech Debt (87.434%)
**Top Internal Functions/Classes:**
  * `getUserIpFromIpHeaders` (Impact: 115.7 | O(N^5) | DB: 3)
  * `getHostInfo` (Impact: 68.8 | O(N^5) | DB: 9)
    * *Intent:* * ``` * [ * '192.168.0.0/24', * ] * ``` * * To trust just the `X-Forwarded-For` header from `10.0.0....
  * `getHeaders` (Impact: 68.3 | O(N^6) | DB: 10)
    * *Intent:* /**
  * `getScriptUrl` (Impact: 57.4 | O(N^4) | DB: 9)
    * *Intent:* /** * @var array list of headers to check for determining whether the connection is made via HTTPS. ...
  * `getIsSecureConnection` (Impact: 55.7 | O(N^6) | DB: 9)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 254`, `args: 78`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 11`, `state_mutation: 559`, `planned_debt: 2`, `fragile_debt: 4`, `orphaned_logic: 25`
* *Architecture:* `io: 32`, `api: 62`, `import: 7`
* *Defense:* `safety: 33`, `doc: 228`, `test: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` 
    public function getBaseUrl()
    
        if ($this->_baseUrl === null) 
            $this->_baseUrl = rtrim(dirname($this->getScriptUrl()), * forms submitted via POST method must contain a hidden input whose name is specified by [[csrfParam]].
     * You may use [[\yii\helpers\Html::beginForm()]] to generate his hidden input.
     *
     * In JavaScript, yii\base\InvalidConfigException, you may get the values of [[csrfParam]] and [[csrfToken]] via `yii.getCsrfParam()` and
     * `yii.getCsrfToken()`, 
    public function getOrigin()
    
        return $this->getHeaders()->get('origin', yii\validators\IpValidator, 
    public $enableCsrfValidation = true, 
    public function getUrl()
    
        if ($this->_url === null) 
            $this->_url = $this->resolveRequestUri(...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/helpers/BaseFileHelper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.46 IQR)
- **Top Global Matches:** file_cluster_13: 14.46, file_cluster_8: 14.691, file_cluster_11: 14.776
- **Magnitude:** 1307.34 | **LOC:** 1032 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (43.6989%), Tech Debt (30.6179%)
**Top Internal Functions/Classes:**
  * `copyDirectory` (Impact: 352.8 | O(2^N) | DB: 15)
  * `changeOwnership` (Impact: 170.9 | O(N^5) | DB: 15)
    * *Intent:* /** * Copies a whole directory as another one. * The files and sub-directories will also be copied o...
  * `removeDirectory` (Impact: 136.5 | O(2^N) | DB: 6)
  * `unlink` (Impact: 88.0 | O(2^N) | DB: 1)
  * `normalizePath` (Impact: 79.4 | O(N^4) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 66`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 273`, `orphaned_logic: 5`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 25`, `doc: 60`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` yii\base\InvalidConfigException, 
    public static function findFiles($dir, whether the files under the subdirectories should also be looked for. Defaults to `true`.
     * @return array files found under the directory, pattern is an array it must contain the pattern, flags and firstWildcard keys.', $magicFile, $aliasesFile, $options = [])
    
        $dir = self::clearDir($dir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/Controller.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.198 IQR)
- **Top Global Matches:** file_cluster_13: 15.198, file_cluster_11: 15.381, file_cluster_0: 15.442
- **Magnitude:** 1204.26 | **LOC:** 809 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 91.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (42.2658%), Tech Debt (14.1647%)
**Top Internal Functions/Classes:**
  * `bindActionParams` (Impact: 543.7 | O(N^6) | DB: 66)
  * `runAction` (Impact: 330.8 | O(2^N) | DB: 24)
    * *Intent:* /** * @deprecated since 2.0.13. Use [[ExitCode::OK]] instead.
  * `beforeAction` (Impact: 10.7 | O(2^N) | DB: 2)
    * *Intent:* * A console controller consists of one or several actions known as sub-commands. * Users call a cons...
  * `isColorEnabled` (Impact: 6.9 | O(N^2) | DB: 2)
    * *Intent:* * See [[options()]] for details. * * @property Request $request The request object. * @property Resp...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 82`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 283`, `dead_code: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 22`, `import: 8`
* *Defense:* `safety: 29`, `doc: 81`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` yii\base\InvalidRouteException, yii\helpers\Console, 'type' => $type, $default, 'interactive', 'silentExitOnException'], ', 
    public function select($prompt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Command.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.411 IQR)
- **Top Global Matches:** file_cluster_8: 14.411, file_cluster_7: 14.447, file_cluster_13: 14.455
- **Magnitude:** 1172.26 | **LOC:** 1348 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (45.411%), Tech Debt (45.4279%)
**Top Internal Functions/Classes:**
  * `internalExecute` (Impact: 146.8 | O(2^N) | DB: 6)
    * *Intent:* /** * Creates a SQL command for dropping a DB table. * @param string $table the table to be dropped....
  * `prepare` (Impact: 109.0 | O(2^N) | DB: 11)
    * *Intent:* /** * Enables query cache for this command. * @param int|null $duration the number of seconds that q...
  * `getRawSql` (Impact: 75.3 | O(N^4) | DB: 8)
  * `queryInternal` (Impact: 59.6 | O(N^5) | DB: 10)
    * *Intent:* * * ``` * $minAge = 30; * $connection->createCommand()->update('user', ['status' => 1], 'age > :minA...
  * `bindValues` (Impact: 56.1 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 145`, `args: 64`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 268`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 57`, `import: 3`
* *Defense:* `safety: 29`, `doc: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` $table, d in the index. If there are multiple columns, $unique = false)
    
        $sql = $this->db->getQueryBuilder()->createIndex($name, Yii, $value[1], yii\base\NotSupportedException, yii\base\Component, TableSchemaRefresh($name)
    
        $this->_refreshTableName = $name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Connection.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.103 IQR)
- **Top Global Matches:** file_cluster_13: 14.103, file_cluster_0: 14.269, file_cluster_11: 14.274
- **Magnitude:** 1165.86 | **LOC:** 1289 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (39.3471%), Tech Debt (22.9595%)
**Top Internal Functions/Classes:**
  * `openFromPoolSequentially` (Impact: 112.3 | O(N^5) | DB: 6)
  * `createPdoInstance` (Impact: 69.1 | O(N^5) | DB: 18)
  * `transaction` (Impact: 53.0 | O(2^N) | DB: 5)
    * *Intent:* * @var array the configuration that should be merged with every slave configuration listed in [[slav...
  * `open` (Impact: 49.9 | O(N^4) | DB: 5)
    * *Intent:* /** * @var int number of seconds that table metadata can remain valid in cache. * Use 0 to indicate ...
  * `getQueryCacheInfo` (Impact: 49.1 | O(N^4) | DB: 8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 143`, `args: 38`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 6`, `state_mutation: 321`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 20`, `api: 64`, `import: 9`
* *Defense:* `safety: 56`, `doc: 203`, `test: 7`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.854
  * `Choke Point (Betweenness):` 0.000485 | `Ripple Effect (Closeness):` 0.045349
  * `Imports (Out-Degree: 5):` 
    public function getLastInsertID($sequenceName = '')
    
        return $this->getSchema()->getLastInsertID($sequenceName, Yii, ref.pdo-sqlite.connection.php) you may use a [path alias](guide:concept-aliases)
     * for specifying the database path, PDO, yii\base\NotSupportedException, yii\caching\CacheInterface, yii\base\InvalidConfigException, d PHP version is >= 5.5
            $this->enableSlaves = true...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `framework/console/controllers/AssetController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.243 IQR)
- **Top Global Matches:** file_cluster_13: 14.243, file_cluster_8: 14.411, file_cluster_7: 14.529
- **Magnitude:** 1158.28 | **LOC:** 847 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (38.0396%), Tech Debt (14.4691%)
**Top Internal Functions/Classes:**
  * `adjustCssUrl` (Impact: 171.6 | O(N^6) | DB: 29)
  * `loadTargets` (Impact: 118.0 | O(N^6) | DB: 7)
    * *Intent:* /** * Returns the asset manager instance.
  * `buildTarget` (Impact: 85.8 | O(N^6) | DB: 7)
  * `registerBundle` (Impact: 50.7 | O(2^N) | DB: 2)
    * *Intent:* /** * Creates full list of output asset bundles. * @param array $targets output asset bundles config...
  * `adjustDependency` (Impact: 48.8 | O(N^5) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 111`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 293`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 12`, `import: 10`
* *Defense:* `safety: 44`, `doc: 105`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` yii\helpers\Console, all-hash.js', *     'depends' => [], *         'app\assets\SharedAsset', yii\console\Exception, yii\helpers\VarDumper, 
    public $targets = [], Yii...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/rbac/DbManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.409 IQR)
- **Top Global Matches:** file_cluster_8: 12.409, file_cluster_13: 12.478, file_cluster_7: 12.614
- **Magnitude:** 1150.08 | **LOC:** 1138 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (25.2709%), Tech Debt (55.8426%)
**Top Internal Functions/Classes:**
  * `checkAccessFromCache` (Impact: 122.1 | O(2^N) | DB: 1)
    * *Intent:* /** * Performs access check for the specified user based on the data loaded from cache. * This metho...
  * `checkAccessRecursive` (Impact: 90.9 | O(2^N) | DB: 3)
    * *Intent:* /** * Performs access check for the specified user. * This method is internally called by [[checkAcc...
  * `loadFromCache` (Impact: 49.6 | O(N^4) | DB: 11)
  * `detectLoop` (Impact: 35.3 | O(2^N) | DB: 1)
    * *Intent:* /** * Checks whether there is a loop in the authorization item hierarchy.
  * `getChildrenRecursive` (Impact: 30.4 | O(2^N) | DB: 1)
    * *Intent:* /** * Recursively finds all children and grand children of the specified item.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 201`, `args: 50`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 4`, `state_mutation: 297`, `orphaned_logic: 26`
* *Architecture:* `api: 35`, `import: 11`
* *Defense:* `safety: 24`, `doc: 109`, `test: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.948
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.007375
  * `Imports (Out-Degree: 7):` 
    public function getRolesByUser($userId)
    
        if ($this->isEmptyUserId($userId)) 
            return [], extra memory and, Yii, yii\db\Connection, rules or parent-child relationships from outside of this component, 
    public $cache, yii\caching\CacheInterface, yii\db\Query...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `framework/i18n/MessageFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.225 IQR)
- **Top Global Matches:** file_cluster_13: 14.225, file_cluster_8: 14.505, file_cluster_11: 14.523
- **Magnitude:** 1117.86 | **LOC:** 443 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (32.6907%), Tech Debt (15.7499%)
**Top Internal Functions/Classes:**
  * `parseToken` (Impact: 333.6 | O(N^6) | DB: 39)
  * `replaceNamedArguments` (Impact: 252.8 | O(2^N) | DB: 16)
    * *Intent:* /** * Formats a message via [ICU message format](https://unicode-org.github.io/icu/userguide/format_...
  * `parse` (Impact: 110.6 | O(2^N) | DB: 20)
    * *Intent:* * * This class enhances the message formatter class provided by the PHP intl extension. * * The foll...
  * `tokenizePattern` (Impact: 71.3 | O(N^4) | DB: 20)
  * `fallbackFormat` (Impact: 31.1 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 51`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 305`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 9`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` s PHP intl extension to be installed.
     *
     * @param string $pattern The pattern to use for parsing the message.
     * @param string $message The message to parse, $language)
    
        $this->_errorCode = 0, $message, Yii, conforming to the pattern.
     * @param string $language The locale to use for formatting locale-dependent parts
     * @return array|bool An array containing items extracted, yii\base\NotSupportedException, yii\base\Component, 
    public function parse($pattern
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/rbac/PhpManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.714 IQR)
- **Top Global Matches:** file_cluster_13: 13.714, file_cluster_8: 13.721, file_cluster_7: 13.871
- **Magnitude:** 1047.72 | **LOC:** 897 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (34.4829%), Tech Debt (96.5194%)
**Top Internal Functions/Classes:**
  * `checkAccessRecursive` (Impact: 101.9 | O(2^N) | DB: 2)
    * *Intent:* /**
  * `load` (Impact: 81.3 | O(N^6) | DB: 16)
    * *Intent:* /** * {@inheritdoc} */
  * `removeAllItems` (Impact: 74.5 | O(N^6) | DB: 7)
  * `detectLoop` (Impact: 44.2 | O(2^N) | DB: 1)
    * *Intent:* /** * Performs access check for the specified user.
  * `updateItem` (Impact: 43.3 | O(N^5) | DB: 3)
    * *Intent:* /** * Returns all permissions that the user inherits from the roles assigned to him. * @param string...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 160`, `args: 50`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 225`, `orphaned_logic: 31`
* *Architecture:* `io: 1`, `api: 32`, `import: 5`
* *Defense:* `safety: 44`, `doc: 99`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.00295
  * `Imports (Out-Degree: 4):` yii\helpers\VarDumper, Yii, 
    public function getRolesByUser($userId)
    
        $roles = $this->getDefaultRoleInstances(, $file, yii\base\InvalidCallException, yii\base\InvalidArgumentException
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseVarDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.25 IQR)
- **Top Global Matches:** file_cluster_13: 14.25, file_cluster_8: 14.373, file_cluster_11: 14.385
- **Magnitude:** 1037.08 | **LOC:** 274 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (43.1228%), Tech Debt (22.9464%)
**Top Internal Functions/Classes:**
  * `dumpInternal` (Impact: 403.6 | O(2^N) | DB: 29)
  * `exportInternal` (Impact: 281.9 | O(2^N) | DB: 24)
  * `exportClosure` (Impact: 107.0 | O(N^6) | DB: 18)
  * `dumpAsString` (Impact: 16.6 | O(N^3) | DB: 7)
  * `dump` (Impact: 3.2 | O(N^2) | DB: 2)
    * *Intent:* /** * BaseVarDumper provides concrete implementation for [[VarDumper]]. * * Do not use BaseVarDumper...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 25`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 215`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 10`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` 
    public static function export($var)
    
        self::$_output = '', yii\base\Arrayable, yii\base\InvalidValueException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/helpers/BaseConsole.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.476 IQR)
- **Top Global Matches:** file_cluster_13: 14.476, file_cluster_8: 14.522, file_cluster_7: 14.575
- **Magnitude:** 997.8 | **LOC:** 1208 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (48.3453%), Tech Debt (99.9943%)
**Top Internal Functions/Classes:**
  * `getScreenSize` (Impact: 123.3 | O(N^5) | DB: 17)
  * `ansiToHtml` (Impact: 108.1 | O(N^6) | DB: 50)
    * *Intent:* /** * Resets any ANSI format set by previous method [[beginAnsiFormat()]] * Any output after this wi...
  * `ansiColorizedSubstr` (Impact: 100.3 | O(N^6) | DB: 17)
  * `wrapText` (Impact: 30.9 | O(N^4) | DB: 9)
  * `endProgress` (Impact: 26.9 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 100`, `args: 48`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 325`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 35`
* *Architecture:* `io: 2`, `api: 69`, `import: 3`
* *Defense:* `safety: 7`, `doc: 115`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` yii\console\Markdown, 'default' => null, Yii, 'pattern' => null, d']) 
                static::output($options['error'], ', 
    public static function select($prompt, $options = []...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/HelpController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.943 IQR)
- **Top Global Matches:** file_cluster_13: 13.943, file_cluster_8: 14.017, file_cluster_7: 14.196
- **Magnitude:** 971.16 | **LOC:** 570 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (37.7729%), Tech Debt (20.9977%)
**Top Internal Functions/Classes:**
  * `getModuleCommands` (Impact: 135.6 | O(2^N) | DB: 14)
  * `getSubCommandHelp` (Impact: 91.8 | O(N^5) | DB: 12)
  * `formatOptionHelp` (Impact: 81.4 | O(N^4) | DB: 15)
  * `getDefaultHelp` (Impact: 65.2 | O(N^5) | DB: 19)
  * `actionIndex` (Impact: 51.5 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 86`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 315`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 13`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004425
  * `Imports (Out-Degree: 4):` $arg['default'], yii\helpers\Console, d']) ? Console::FG_RED : Console::BOLD
                ), $arg['comment']
                ) . "\n\n", Console::FG_CYAN, d ? "$name (required)" : $name, $defaultValue, yii\helpers\Inflector...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `framework/db/mssql/QueryBuilder.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.903 IQR)
- **Top Global Matches:** file_cluster_13: 13.903, file_cluster_8: 13.91, file_cluster_7: 14.013
- **Magnitude:** 946.42 | **LOC:** 692 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (33.9654%), Tech Debt (80.5219%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 98.4 | O(N^5) | DB: 15)
  * `upsert` (Impact: 90.5 | O(N^5) | DB: 24)
  * `oldBuildOrderByAndLimit` (Impact: 45.9 | O(N^4) | DB: 8)
    * *Intent:* /** * Builds the ORDER BY/LIMIT/OFFSET clauses for SQL SERVER 2012 or newer. * @param string $sql th...
  * `alterColumn` (Impact: 44.0 | O(N^5) | DB: 6)
  * `buildAddCommentSql` (Impact: 43.8 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 87`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 327`, `orphaned_logic: 16`
* *Architecture:* `api: 19`, `import: 5`
* *Defense:* `safety: 10`, `doc: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` s an ORDER BY clause
            $orderBy = 'ORDER BY (SELECT NULL)', d when FETCH and OFFSET are in the SQL
            $orderBy = 'ORDER BY (SELECT NULL)', yii\base\NotSupportedException, yii\db\Query, yii\db\TableSchema, yii\base\InvalidArgumentException, yii\db\Expression
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/mssql/Schema.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.603 IQR)
- **Top Global Matches:** file_cluster_13: 13.603, file_cluster_8: 13.692, file_cluster_7: 13.871
- **Magnitude:** 943.3 | **LOC:** 832 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (44.3771%), Tech Debt (78.6566%)
**Top Internal Functions/Classes:**
  * `loadColumnSchema` (Impact: 130.3 | O(N^6) | DB: 31)
    * *Intent:* /** * {@inheritdoc}
  * `loadTableConstraints` (Impact: 94.2 | O(N^6) | DB: 9)
  * `insert` (Impact: 70.7 | O(2^N) | DB: 5)
  * `findColumns` (Impact: 64.3 | O(N^5) | DB: 11)
  * `findForeignKeys` (Impact: 23.0 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 94`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 356`, `orphaned_logic: 17`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 12`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` yii\db\IndexConstraint, yii\db\Schema, Yii, yii\db\CheckConstraint, yii\db\Constraint, ViewFinderTrait, ConstraintFinderTrait, yii\db\DefaultValueConstraint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/oci/Schema.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.556 IQR)
- **Top Global Matches:** file_cluster_13: 13.556, file_cluster_8: 13.756, file_cluster_7: 13.922
- **Magnitude:** 898.14 | **LOC:** 748 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (34.8792%), Tech Debt (96.9826%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 106.2 | O(2^N) | DB: 19)
  * `loadTableConstraints` (Impact: 81.8 | O(N^6) | DB: 9)
  * `createColumn` (Impact: 80.7 | O(N^6) | DB: 14)
    * *Intent:* // does nothing as Oracle does not support this
  * `extractColumnType` (Impact: 74.7 | O(N^4) | DB: 10)
  * `findConstraints` (Impact: 48.9 | O(N^5) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 95`, `args: 27`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 273`, `fragile_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 8`, `api: 9`, `import: 16`
* *Defense:* `safety: 13`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` yii\db\IndexConstraint, yii\db\Schema, Yii, yii\db\Connection,  get the last insert id from the master connection
            $sequenceName = $this->quoteSimpleTableName($sequenceName, yii\db\CheckConstraint, yii\db\Constraint, yii\base\NotSupportedException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/mysql/Schema.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.618 IQR)
- **Top Global Matches:** file_cluster_13: 13.618, file_cluster_8: 13.831, file_cluster_17: 13.969
- **Magnitude:** 872.1 | **LOC:** 668 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (38.0666%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `loadColumnSchema` (Impact: 191.1 | O(N^6) | DB: 30)
  * `findConstraints` (Impact: 87.0 | O(N^6) | DB: 15)
    * *Intent:* /** * When displayed in the INFORMATION_SCHEMA.COLUMNS table, a default CURRENT TIMESTAMP is display...
  * `loadTableConstraints` (Impact: 69.5 | O(N^6) | DB: 9)
  * `findColumns` (Impact: 53.9 | O(N^5) | DB: 13)
    * *Intent:* /** * Loads the column information into a [[ColumnSchema]] object. * @param array $info column infor...
  * `loadTableChecks` (Impact: 27.7 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 85`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 283`, `orphaned_logic: 12`
* *Architecture:* `io: 3`, `api: 5`, `import: 15`
* *Defense:* `safety: 19`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` yii\db\IndexConstraint, yii\db\Exception, yii\db\Schema, Yii, yii\db\CheckConstraint, yii\db\Constraint, yii\base\NotSupportedException, ConstraintFinderTrait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/helpers/BaseHtml.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.76 IQR)
- **Top Global Matches:** file_cluster_13: 14.76, file_cluster_8: 14.9, file_cluster_7: 14.959
- **Magnitude:** 871.82 | **LOC:** 2412 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (36.8068%), Tech Debt (94.4163%)
**Top Internal Functions/Classes:**
  * `beginForm` (Impact: 100.2 | O(N^6) | DB: 13)
  * `normalizeMaxLength` (Impact: 48.6 | O(N^5) | DB: 2)
    * *Intent:* * * If you want to use an absolute url you can call [[Url::to()]] yourself, before passing the URL t...
  * `img` (Impact: 44.2 | O(2^N) | DB: 3)
  * `error` (Impact: 32.6 | O(2^N) | DB: 7)
    * *Intent:* /** * Generates a form end tag.
  * `errorSummary` (Impact: 31.5 | O(N^4) | DB: 24)
    * *Intent:* // query parameters in the action are ignored for GET method // we use hidden fields to add them bac...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 91`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 261`, `orphaned_logic: 19`
* *Architecture:* `io: 5`, `api: 38`, `import: 6`
* *Defense:* `safety: 27`, `doc: 164`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Yii, yii\web\Request, yii\validators\StringValidator, yii\db\ActiveRecordInterface, yii\base\InvalidArgumentException, yii\base\Model
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/di/Container.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.165 IQR)
- **Top Global Matches:** file_cluster_13: 14.165, file_cluster_8: 14.367, file_cluster_11: 14.452
- **Magnitude:** 866.7 | **LOC:** 833 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (43.8112%), Tech Debt (85.6401%)
**Top Internal Functions/Classes:**
  * `resolveCallableDependencies` (Impact: 252.7 | O(N^6) | DB: 20)
    * *Intent:* * * ``` * // register a class name as is. This can be skipped. * $container->set('yii\db\Connection'...
  * `getDependencies` (Impact: 142.9 | O(N^6) | DB: 14)
    * *Intent:* /** * @var array cached ReflectionClass objects indexed by class/interface names
  * `resolveDependencies` (Impact: 73.6 | O(2^N) | DB: 4)
  * `validateDependencies` (Impact: 53.1 | O(N^5) | DB: 5)
    * *Intent:* * class UserLister extends BaseObject * { * public $finder; * * public function __construct(UserFind...
  * `build` (Impact: 46.4 | O(N^3) | DB: 12)
    * *Intent:* /** * Container implements a [dependency injection](https://en.wikipedia.org/wiki/Dependency_injecti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 93`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 182`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 25`, `doc: 57`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.733
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004425
  * `Imports (Out-Degree: 6):` yii\helpers\ArrayHelper, Yii, yii\db\Connection, d parameter \"$name\" when instantiating \"$class\".", ReflectionException, d to specify the class
     * $container->set('db', [
     *     'class' => 'yii\db\Connection', yii\base\InvalidConfigException...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `framework/base/Model.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.34 IQR)
- **Top Global Matches:** file_cluster_13: 14.34, file_cluster_8: 14.594, file_cluster_7: 14.667
- **Magnitude:** 862.88 | **LOC:** 1089 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (39.1537%), Tech Debt (79.7088%)
**Top Internal Functions/Classes:**
  * `scenarios` (Impact: 220.5 | O(2^N) | DB: 4)
    * *Intent:* * - scenario-based validation * * Model also raises the following events when performing data valida...
  * `getActiveValidators` (Impact: 45.8 | O(N^4) | DB: 8)
    * *Intent:* /** * Returns a list of scenarios and the corresponding active attributes. * * An active attribute i...
  * `setAttributes` (Impact: 31.8 | O(N^5) | DB: 4)
  * `addErrors` (Impact: 30.6 | O(N^5) | DB: 1)
  * `formName` (Impact: 28.1 | O(2^N) | DB: 1)
    * *Intent:* /** * @event Event an event raised at the end of [[validate()]] */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 117`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 184`, `orphaned_logic: 13`
* *Architecture:* `api: 38`, `import: 11`
* *Defense:* `safety: 20`, `doc: 107`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.791
  * `Choke Point (Betweenness):` 0.000672 | `Ripple Effect (Closeness):` 0.04768
  * `Imports (Out-Degree: 5):` ArrayAccess, 'password'], 'compare', mixed> $iterator An iterator for traversing the items in the list.
 * @property string $scenario The scenario that this model is in. Defaults to [[SCENARIO_DEFAULT]].
 * @property-read ArrayObject<int, yii\validators\Validator, Validator>|Validator[] $validators All the validators declared in the
 * model.
 *
 * @author Qiang Xue <qiang.xue@gmail.com>
 * @since 2.0
 *
 * @implements IteratorAggregate<string,  built-in "compare" validator that is used in "register" scenario only
     *     ['password', for single attribute you can pass a string...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `framework/db/DataReader.php` (PHP) | Magnitude: 113.02 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, doc: 45, structural_boundaries: 32, state_mutation: 23
- `tests/js/data/yii.html` (HTML) | Magnitude: 47.22 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 156, args: 136, io: 70, decorators: 65
- `framework/web/HeaderCollection.php` (PHP) | Magnitude: 129.42 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, doc: 55, structural_boundaries: 41, state_mutation: 30
- `framework/db/mssql/SqlsrvPDO.php` (PHP) | Magnitude: 13.4 | Delta: **0.265 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 5, indent_spaces: 5, state_mutation: 3
- `framework/db/mssql/DBLibPDO.php` (PHP) | Magnitude: 58.86 | Delta: **0.274 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 10, doc: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `framework/db/conditions/LikeCondition.php` (PHP) | Magnitude: 34.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 15, doc: 14, branch: 10
- `framework/db/mssql/QueryBuilder.php` (PHP) | Magnitude: 946.42 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 408, state_mutation: 327, doc: 89, structural_boundaries: 87
- `framework/rbac/PhpManager.php` (PHP) | Magnitude: 1047.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 532, state_mutation: 225, structural_boundaries: 160, branch: 106
- `framework/web/UploadedFile.php` (PHP) | Magnitude: 328.46 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 224, doc: 66, structural_boundaries: 57, state_mutation: 48
- `framework/base/Event.php` (PHP) | Magnitude: 409.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, state_mutation: 103, structural_boundaries: 71, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/framework/db/AnyCaseValue.php` (PHP) | Magnitude: 32.5 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 9, structural_boundaries: 4, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `framework/views/migration.php` (PHP) | Magnitude: 12.36 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, branch: 8, structural_boundaries: 8, doc: 5
- `framework/base/ViewRenderer.php` (PHP) | Magnitude: 32.4 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 4, ownership: 2, branch: 1
- `framework/i18n/migrations/m150207_210500_i18n_init.php` (PHP) | Magnitude: 35.52 | Delta: **0.263 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 18, ui_framework: 10, structural_boundaries: 5
- `framework/views/createTableMigration.php` (PHP) | Magnitude: 24.68 | Delta: **0.272 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, branch: 13, doc: 11, structural_boundaries: 7
- `framework/views/addColumnMigration.php` (PHP) | Magnitude: 13.76 | Delta: **0.296 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 10, doc: 10, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/framework/db/testBatchInsertWithYield.php` (PHP) | Magnitude: 27.28 | Delta: **0.366 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 6, concurrency: 6, indent_spaces: 6, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `framework/base/DynamicContentAwareInterface.php` (PHP) | Magnitude: 47.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 5, args: 3, func_start: 3
- `framework/web/IdentityInterface.php` (PHP) | Magnitude: 60.19 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 7, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `framework/base/Security.php` (PHP) | Magnitude: 429.98 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 208, state_mutation: 156, doc: 120, structural_boundaries: 64
- `framework/db/QueryInterface.php` (PHP) | Magnitude: 119.38 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 51, structural_boundaries: 18, args: 16, func_start: 16
- `framework/web/Cookie.php` (PHP) | Magnitude: 22.2 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 23, indent_spaces: 15, api: 12, state_mutation: 7
- `framework/db/ConstraintFinderInterface.php` (PHP) | Magnitude: 112.95 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 50, state_mutation: 20, structural_boundaries: 14, args: 12
- `framework/rbac/ManagerInterface.php` (PHP) | Magnitude: 166.13 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 98, structural_boundaries: 35, args: 32, func_start: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `framework/web/MultipartFormDataParser.php` (PHP) | Magnitude: 588.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 218, state_mutation: 168, branch: 62, structural_boundaries: 39
- `framework/base/ActionFilter.php` (PHP) | Magnitude: 166.04 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 45, doc: 25, structural_boundaries: 19
- `framework/web/Request.php` (PHP) | Magnitude: 1383.36 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1090, state_mutation: 559, branch: 271, structural_boundaries: 254
- `framework/db/ExpressionBuilderTrait.php` (PHP) | Magnitude: 6.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 6, indent_spaces: 5, structural_boundaries: 3, api: 2
- `framework/validators/InlineValidator.php` (PHP) | Magnitude: 83.3 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 36, indent_spaces: 35, doc: 12, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `framework/base/ActionEvent.php` (PHP) | Magnitude: 14.66 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_spaces: 8, state_mutation: 5, structural_boundaries: 4
- `framework/caching/ExpressionDependency.php` (PHP) | Magnitude: 8.02 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 6, indent_spaces: 6, state_mutation: 3
- `framework/data/DataProviderInterface.php` (PHP) | Magnitude: 72.81 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 9, args: 7, func_start: 7
- `framework/caching/MemCacheServer.php` (PHP) | Magnitude: 31.26 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 18, api: 8, state_mutation: 8, indent_spaces: 8
- `framework/rbac/migrations/schema-oci.sql` (SQLITE) | Magnitude: 0.73 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, safety: 11, duplicate_logic: 10, class_start: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `framework/base/Application.php` -> Churn: **87.0%** | Cog Load: 37.8405% | Debt: 99.9742%
- `framework/base/Model.php` -> Churn: **85.92%** | Cog Load: 39.1537% | Debt: 79.7088%
- `framework/base/Module.php` -> Churn: **78.59%** | Cog Load: 36.652% | Debt: 97.8398%
- `framework/console/controllers/BaseMigrateController.php` -> Churn: **78.59%** | Cog Load: 38.6367% | Debt: 56.7602%
- `framework/console/controllers/MigrateController.php` -> Churn: **78.59%** | Cog Load: 29.8982% | Debt: 78.0545%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `framework/helpers/BaseArrayHelper.php` -> **Maksim Spirkov** (100.0% isolated ownership) | Magnitude: 1930.5
- `framework/db/ActiveQuery.php` -> **Maksim Spirkov** (87.5% isolated ownership) | Magnitude: 1439.6
- `framework/console/controllers/BaseMigrateController.php` -> **Maksim Spirkov** (88.9% isolated ownership) | Magnitude: 1392.04
- `framework/web/Request.php` -> **Maksim Spirkov** (83.3% isolated ownership) | Magnitude: 1383.36
- `framework/console/Controller.php` -> **Maksim Spirkov** (91.7% isolated ownership) | Magnitude: 1204.26

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `framework/db/Migration.php` -> **Severity: 0.072** (Bridge: 0.0007 * Flux: 99.9648%)
- `framework/base/Model.php` -> **Severity: 0.067** (Bridge: 0.0007 * Flux: 100.0%)
- `framework/db/Connection.php` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)
- `framework/di/Instance.php` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 100.0%)
- `framework/base/Component.php` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `framework/Yii.php` -> **Severity: 5.756** (Embedded: 0.2815 * Error Risk: 20.4473%)
- `framework/db/Connection.php` -> **Severity: 3.212** (Embedded: 0.0453 * Error Risk: 70.8309%)
- `framework/db/Query.php` -> **Severity: 3.021** (Embedded: 0.034 * Error Risk: 88.8158%)
- `framework/base/Component.php` -> **Severity: 2.853** (Embedded: 0.121 * Error Risk: 23.5796%)
- `framework/db/mssql/PDO.php` -> **Severity: 2.069** (Embedded: 0.0327 * Error Risk: 63.3333%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `framework/Yii.php` -> **Severity: 840.597** (Blast Radius: 88.148 * Doc Risk: 9.5362%)
- `framework/base/InvalidArgumentException.php` -> **Severity: 769.784** (Blast Radius: 14.185 * Doc Risk: 54.2675%)
- `framework/db/Migration.php` -> **Severity: 732.632** (Blast Radius: 20.007 * Doc Risk: 36.6188%)
- `framework/base/Model.php` -> **Severity: 652.095** (Blast Radius: 11.791 * Doc Risk: 55.3045%)
- `framework/db/ActiveQuery.php` -> **Severity: 594.0** (Blast Radius: 5.94 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
