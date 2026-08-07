# ARCHITECTURAL_BRIEF: yii2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/yii2` |
| **Timestamp** | `2026-08-07T03:55:33.061677+00:00` |
| **Scan Duration** | `2.79s` |
| **Git Branch** | `master` |
| **Git Commit** | `9265980e089733f657609a37a95ab86176cb6c00` |
| **Git Remote** | `https://github.com/yiisoft/yii2.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 654 malicious artifacts.

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
| Modularity | 0.517 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `5.149`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 332 | 48.9% |
| file_cluster_8 | 248 | 36.5% |
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
| Cognitive Load Exposure | 0.0 | 58.4 | 18.9 | 10.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 55.3 | 70.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.7 | 4.8 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 52.2 | 85.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 59.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.6 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 12.7 | 11.9 | 0.0 |
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

- `bindActionParams` (@ `framework/console/Controller.php`) -> Impact: **160.0** | LOC: 325
- `bindActionParams` (@ `framework/web/Controller.php`) -> Impact: **146.4** | LOC: 296
  * *Intent:* /** * Renders a view in response to an AJAX request. *
- `saveMessagesToDb` (@ `framework/console/controllers/MessageController.php`) -> Impact: **106.0** | LOC: 141
- `sendContent` (@ `framework/web/Response.php`) -> Impact: **101.6** | LOC: 266
- `parseToken` (@ `framework/i18n/MessageFormatter.php`) -> Impact: **98.5** | LOC: 91
- `saveMessagesToPO` (@ `framework/console/controllers/MessageController.php`) -> Impact: **77.7** | LOC: 84
- `createUrl` (@ `framework/web/UrlRule.php`) -> Impact: **76.2** | LOC: 85
- `resolveCallableDependencies` (@ `framework/di/Container.php`) -> Impact: **75.2** | LOC: 83
  * *Intent:* * * ``` * // register a class name as is. This can be skipped. * $container->set('yii\db\Connection'); * * // register an interface * // When a class ...
- `saveMessagesCategoryToPHP` (@ `framework/console/controllers/MessageController.php`) -> Impact: **71.1** | LOC: 64
- `safeUp` (@ `framework/views/createJunctionMigration.php`) -> Impact: **69.4** | LOC: 38
  * *Intent:* /** * This view is used by console/controllers/MigrateController.php. * * The following variables are available in this view: * @since 2.0.7 * @deprec...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `framework/web` | 58 | 6772.87 | 22.74% | 42.11% |
| `framework/db` | 46 | 5686.12 | 21.92% | 48.62% |
| `framework/helpers` | 31 | 4302.28 | 17.97% | 36.08% |
| `framework/console/controllers` | 8 | 3275.76 | 37.02% | 44.23% |
| `framework/base` | 49 | 3040.86 | 18.8% | 60.18% |
| `framework/validators` | 24 | 2780.5 | 33.57% | 61.44% |
| `framework/i18n` | 12 | 2216.86 | 23.81% | 55.9% |
| `framework/rbac` | 10 | 1671.37 | 12.6% | 25.23% |
| `framework/widgets` | 19 | 1381.1 | 28.17% | 16.55% |
| `framework/data` | 9 | 1339.41 | 30.87% | 62.49% |

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
4. **`framework/BaseYii.php`** -> AI Confidence: **99.31%**
5. **`framework/base/Controller.php`** -> AI Confidence: **99.31%**
6. **`framework/behaviors/AttributeTypecastBehavior.php`** -> AI Confidence: **99.31%**
7. **`framework/console/Controller.php`** -> AI Confidence: **99.31%**
8. **`framework/console/ExitCode.php`** -> AI Confidence: **99.31%**
9. **`framework/console/controllers/AssetController.php`** -> AI Confidence: **99.31%**
10. **`framework/console/controllers/BaseMigrateController.php`** -> AI Confidence: **99.31%**
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
39. **`framework/web/UrlRule.php`** -> AI Confidence: **99.31%**
40. **`framework/web/User.php`** -> AI Confidence: **99.31%**
41. **`framework/web/View.php`** -> AI Confidence: **99.31%**
42. **`framework/widgets/Breadcrumbs.php`** -> AI Confidence: **99.31%**
43. **`framework/widgets/DetailView.php`** -> AI Confidence: **99.31%**
44. **`framework/widgets/Pjax.php`** -> AI Confidence: **99.31%**
45. **`framework/requirements/views/web/css.php`** -> AI Confidence: **99.29%**
46. **`framework/views/_addColumns.php`** -> AI Confidence: **99.29%**
47. **`framework/views/_addComments.php`** -> AI Confidence: **99.29%**
48. **`framework/views/_addForeignKeys.php`** -> AI Confidence: **99.29%**
49. **`framework/views/_createTable.php`** -> AI Confidence: **99.29%**
50. **`framework/views/_dropColumns.php`** -> AI Confidence: **99.29%**
51. **`framework/views/_dropForeignKeys.php`** -> AI Confidence: **99.29%**
52. **`framework/views/_dropTable.php`** -> AI Confidence: **99.29%**
53. **`framework/views/_foreignTables.php`** -> AI Confidence: **99.29%**
54. **`framework/views/createJunctionMigration.php`** -> AI Confidence: **99.29%**
55. **`framework/views/errorHandler/callStackItem.php`** -> AI Confidence: **99.29%**
56. **`framework/views/errorHandler/error.php`** -> AI Confidence: **99.29%**
57. **`framework/views/errorHandler/previousException.php`** -> AI Confidence: **99.29%**
58. **`tests/data/views/error.php`** -> AI Confidence: **99.29%**
59. **`tests/data/views/errorHandler.php`** -> AI Confidence: **99.29%**
60. **`tests/data/views/errorHandlerForAssetFiles.php`** -> AI Confidence: **99.29%**
61. **`tests/framework/console/controllers/stub/index.php`** -> AI Confidence: **99.29%**
62. **`tests/data/oci/optimize_for_tests.sql`** -> AI Confidence: **99.29%**
63. **`framework/base/ArrayableTrait.php`** -> AI Confidence: **99.24%**
64. **`framework/base/Model.php`** -> AI Confidence: **99.24%**
65. **`framework/caching/Cache.php`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2580` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `framework/base/Module.php` (PHP) -> Cumulative Risk: **608.85**
- **Archetype:** `file_cluster_13` (Distance: 14.058 IQR)
- **Magnitude:** 275.06 | **LOC:** 795 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.8398%), Safety Score (87.9267%)
- **Heaviest Functions:** `getModule` (Impact: 11.5), `getModules` (Impact: 9.7), `setBasePath` (Impact: 9.2)

### 2. `framework/base/Application.php` (PHP) -> Cumulative Risk: **607.09**
- **Archetype:** `file_cluster_8` (Distance: 12.97 IQR)
- **Magnitude:** 139.28 | **LOC:** 679 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 90.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9952%), Tech Debt (99.9742%), Churn (87.0%)
- **Heaviest Functions:** `end` (Impact: 13.1), `run` (Impact: 8.1), `registerErrorHandler` (Impact: 5.8)

### 3. `framework/web/Request.php` (PHP) -> Cumulative Risk: **599.02**
- **Archetype:** `file_cluster_8` (Distance: 13.956 IQR)
- **Magnitude:** 951.56 | **LOC:** 2041 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.772%), Tech Debt (87.434%)
- **Heaviest Functions:** `getUserIpFromIpHeaders` (Impact: 39.5), `getHostInfo` (Impact: 23.8), `getScriptUrl` (Impact: 23.6)

### 4. `framework/db/BaseActiveRecord.php` (PHP) -> Cumulative Risk: **598.75**
- **Archetype:** `file_cluster_13` (Distance: 13.911 IQR)
- **Magnitude:** 347.7 | **LOC:** 1860 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.2337%), Verification (80.0%)
- **Heaviest Functions:** `link` (Impact: 57.9), `getRelation` (Impact: 19.1), `getOldPrimaryKey` (Impact: 18.7)

### 5. `framework/db/oci/Schema.php` (PHP) -> Cumulative Risk: **593.8**
- **Archetype:** `file_cluster_13` (Distance: 13.556 IQR)
- **Magnitude:** 511.14 | **LOC:** 748 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.9826%), Safety Score (92.4099%)
- **Heaviest Functions:** `extractColumnType` (Impact: 30.6), `loadTableConstraints` (Impact: 25.5), `createColumn` (Impact: 24.4)

### 6. `framework/base/Model.php` (PHP) -> Cumulative Risk: **593.28**
- **Archetype:** `file_cluster_13` (Distance: 14.341 IQR)
- **Magnitude:** 451.68 | **LOC:** 1089 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (85.92%), Safety Score (80.9083%)
- **Heaviest Functions:** `scenarios` (Impact: 33.4), `getActiveValidators` (Impact: 19.0), `validate` (Impact: 11.8)

### 7. `framework/db/cubrid/QueryBuilder.php` (PHP) -> Cumulative Risk: **592.25**
- **Archetype:** `file_cluster_13` (Distance: 13.522 IQR)
- **Magnitude:** 257.82 | **LOC:** 294 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.632%), Tech Debt (93.1344%)
- **Heaviest Functions:** `upsert` (Impact: 29.5), `getColumnDefinition` (Impact: 18.5), `resetSequence` (Impact: 11.3)

### 8. `framework/db/mssql/QueryBuilder.php` (PHP) -> Cumulative Risk: **591.85**
- **Archetype:** `file_cluster_13` (Distance: 13.903 IQR)
- **Magnitude:** 585.72 | **LOC:** 692 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 71.4%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.8713%), Tech Debt (80.5219%)
- **Heaviest Functions:** `insert` (Impact: 34.4), `upsert` (Impact: 32.3), `oldBuildOrderByAndLimit` (Impact: 19.1)

### 9. `framework/web/Session.php` (PHP) -> Cumulative Risk: **587.49**
- **Archetype:** `file_cluster_8` (Distance: 13.105 IQR)
- **Magnitude:** 415.82 | **LOC:** 1084 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9788%), Tech Debt (99.9729%), Verification (80.0%)
- **Heaviest Functions:** `updateFlashCounters` (Impact: 25.6), `registerSessionHandler` (Impact: 20.7), `open` (Impact: 17.0)

### 10. `framework/web/Response.php` (PHP) -> Cumulative Risk: **585.52**
- **Archetype:** `file_cluster_13` (Distance: 13.509 IQR)
- **Magnitude:** 537.0 | **LOC:** 1158 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (92.4142%), Safety Score (90.555%)
- **Heaviest Functions:** `sendContent` (Impact: 101.6), `sendCookies` (Impact: 30.0), `redirect` (Impact: 29.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `framework/i18n/Formatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.303 IQR)
- **Top Global Matches:** file_cluster_13: 14.303, file_cluster_8: 14.418, file_cluster_7: 14.473
- **Magnitude:** 1273.3 | **LOC:** 2198 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (29.294%), Tech Debt (27.8743%)
**Top Internal Functions/Classes:**
  * `formatNumber` (Impact: 61.0)
  * `asDecimalStringFallback` (Impact: 55.4)
  * `asShortSize` (Impact: 42.2)
  * `asSize` (Impact: 42.2)
  * `asCurrency` (Impact: 35.6)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 226`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 145`, `high_risk_execution: 8`, `state_mutation: 676`, `orphaned_logic: 16`
* *Architecture:* `api: 48`, `import: 17`
* *Defense:* `safety: 16`, `doc: 247`, `test: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.118
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.003319
  * `Imports (Out-Degree: 9):` 'kilogram' => 1000, IntlDateFormatter, DateInterval, yii\base\InvalidArgumentException, but it is highly recommended to install it to get good formatting results.
     *
     * Since 2.0.16 numbers that are mispresented after normalization are formatted, DateTimeInterface, 'furlong' => 7920, 'meter' => 1000...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `framework/web/Request.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.956 IQR)
- **Top Global Matches:** file_cluster_8: 13.956, file_cluster_13: 13.972, file_cluster_7: 14.017
- **Magnitude:** 951.56 | **LOC:** 2041 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (45.8527%), Tech Debt (87.434%)
**Top Internal Functions/Classes:**
  * `getUserIpFromIpHeaders` (Impact: 39.5)
  * `getHostInfo` (Impact: 23.8)
    * *Intent:* * ``` * [ * '192.168.0.0/24', * ] * ``` * * To trust just the `X-Forwarded-For` header from `10.0.0....
  * `getScriptUrl` (Impact: 23.6)
    * *Intent:* /** * @var array list of headers to check for determining whether the connection is made via HTTPS. ...
  * `resolvePathInfo` (Impact: 23.0)
  * `getHeaders` (Impact: 20.7)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 254`, `args: 78`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 11`, `state_mutation: 559`, `planned_debt: 2`, `fragile_debt: 4`, `orphaned_logic: 25`
* *Architecture:* `io: 32`, `api: 62`, `import: 7`
* *Defense:* `safety: 33`, `doc: 228`, `test: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` to use this feature, unlike this header,  IIS
            $requestUri = $this->headers->get('X-Rewrite-Url', 
    public $enableCsrfCookie = true, s that the user client accepts cookie. Also, s starting a session for every page, the script file name, Yii...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/MessageController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.772 IQR)
- **Top Global Matches:** file_cluster_13: 13.772, file_cluster_8: 13.958, file_cluster_7: 14.067
- **Magnitude:** 828.96 | **LOC:** 1028 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (36.9566%), Tech Debt (34.653%)
**Top Internal Functions/Classes:**
  * `saveMessagesToDb` (Impact: 106.0)
  * `saveMessagesToPO` (Impact: 77.7)
  * `saveMessagesCategoryToPHP` (Impact: 71.1)
  * `extractMessagesFromTokens` (Impact: 41.5)
  * `actionExtract` (Impact: 31.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 106`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 355`, `planned_debt: 6`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 24`, `import: 14`
* *Defense:* `safety: 29`, `doc: 119`, `test: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` d, 
    public $sourcePath = '@yii', 
    public $languages = [], yii\db\Query, yii\i18n\GettextPoFile, yii\console\Controller, Yii, $fileName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/helpers/BaseArrayHelper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.501 IQR)
- **Top Global Matches:** file_cluster_13: 14.501, file_cluster_8: 14.56, file_cluster_11: 14.57
- **Magnitude:** 746.3 | **LOC:** 1104 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.5294%), Tech Debt (75.5169%)
**Top Internal Functions/Classes:**
  * `toArray` (Impact: 38.2)
  * `filter` (Impact: 37.4)
    * *Intent:* * ] * ], * '345' => [ * 'tablet' => [ * 'def' => ['id' => '345', 'data' => 'def', 'device' => 'table...
  * `getValue` (Impact: 30.2)
  * `merge` (Impact: 22.1)
  * `multisort` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 111`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 359`, `planned_debt: 7`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 22`, `doc: 101`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` $sortFlag = SORT_REGULAR)
    
        $keys = is_array($key) ? $key : [$key], Traversable, yii\base\Arrayable, ArrayAccess, `SORT_STRING`, * `SORT_REGULAR`, yii\base\InvalidArgumentException, function.sort.php)
     * for more details. When sorting by multiple keys with different sort flags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/BaseMigrateController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.038 IQR)
- **Top Global Matches:** file_cluster_13: 14.038, file_cluster_8: 14.235, file_cluster_7: 14.357
- **Magnitude:** 726.94 | **LOC:** 1020 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (38.6367%), Tech Debt (56.7602%)
**Top Internal Functions/Classes:**
  * `actionUp` (Impact: 40.5)
    * *Intent:* /** * @var string the template file for generating new migrations. * This can be either a [path alia...
  * `actionRedo` (Impact: 36.0)
  * `getNewMigrations` (Impact: 35.3)
  * `actionDown` (Impact: 33.6)
  * `actionMark` (Impact: 28.3)
    * *Intent:* * For example, * * ``` * yii migrate/down # revert the last migration * yii migrate/down 3 # revert ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 131`, `args: 28`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 344`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 18`, `import: 15`
* *Defense:* `safety: 22`, `doc: 96`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001475
  * `Imports (Out-Degree: 9):` yii\base\Action, yii\console\Controller, yii\db\MigrationInterface, yii\helpers\Inflector, 
    protected function includeMigrationFile($class)
    
        $class = trim($class, Yii, s the migration file for a given migration class name.
     *
     * This function will do nothing on namespaced migrations, yii\console\Application...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `framework/db/Connection.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.103 IQR)
- **Top Global Matches:** file_cluster_13: 14.103, file_cluster_0: 14.269, file_cluster_11: 14.274
- **Magnitude:** 699.36 | **LOC:** 1289 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (37.835%), Tech Debt (22.9595%)
**Top Internal Functions/Classes:**
  * `openFromPoolSequentially` (Impact: 39.6)
  * `createPdoInstance` (Impact: 24.1)
  * `open` (Impact: 21.3)
    * *Intent:* /** * @var int number of seconds that table metadata can remain valid in cache. * Use 0 to indicate ...
  * `getQueryCacheInfo` (Impact: 20.5)
    * *Intent:* /**
  * `initConnection` (Impact: 18.4)
    * *Intent:* /** * @var array mapping between PDO driver names and [[Command]] classes. * The keys of the array a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 143`, `args: 38`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 6`, `state_mutation: 321`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 20`, `api: 64`, `import: 9`
* *Defense:* `safety: 56`, `doc: 203`, `test: 7`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.854
  * `Choke Point (Betweenness):` 0.000485 | `Ripple Effect (Closeness):` 0.045349
  * `Imports (Out-Degree: 5):` PDO, d PHP version is >= 5.5
            $this->enableSlaves = true, yii\base\InvalidConfigException, yii\caching\CacheInterface, yii\base\NotSupportedException, Yii, ref.pdo-sqlite.connection.php) you may use a [path alias](guide:concept-aliases)
     * for specifying the database path, yii\base\Component...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `framework/db/ActiveQuery.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.492 IQR)
- **Top Global Matches:** file_cluster_13: 14.492, file_cluster_8: 14.583, file_cluster_11: 14.642
- **Magnitude:** 676.9 | **LOC:** 867 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (38.5836%), Tech Debt (25.816%)
**Top Internal Functions/Classes:**
  * `joinWithRelation` (Impact: 41.3)
    * *Intent:* * } * ])->all(); * // find all orders that contain books of the category 'Science fiction', using th...
  * `prepare` (Impact: 38.1)
    * *Intent:* * - [[max()]]: returns the max over the specified column. * - [[scalar()]]: returns the value of the...
  * `removeDuplicatedModels` (Impact: 28.3)
  * `buildJoinWith` (Impact: 25.2)
  * `joinWithRelations` (Impact: 24.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 76`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 362`, `dead_code: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 35`, `doc: 97`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.94
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.013728
  * `Imports (Out-Degree: 3):` ActiveQueryTrait, ActiveRelationTrait, yii\base\InvalidConfigException
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseConsole.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.484 IQR)
- **Top Global Matches:** file_cluster_13: 14.484, file_cluster_8: 14.528, file_cluster_7: 14.581
- **Magnitude:** 660.3 | **LOC:** 1208 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.8245%), Tech Debt (99.9943%)
**Top Internal Functions/Classes:**
  * `getScreenSize` (Impact: 42.8)
  * `ansiToHtml` (Impact: 34.4)
    * *Intent:* /** * Resets any ANSI format set by previous method [[beginAnsiFormat()]] * Any output after this wi...
  * `ansiColorizedSubstr` (Impact: 30.3)
  * `getProgressbarWidth` (Impact: 13.3)
  * `wrapText` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 96`, `args: 48`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 325`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 35`
* *Architecture:* `io: 2`, `api: 69`, `import: 3`
* *Defense:* `safety: 7`, `doc: 115`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` $options = [])
    
        $options = ArrayHelper::merge(
            [
                'required' => false, array_keys($options)) . ', ?)'
            . ($default !== null ? '[' . $default . ']' : '') . ': ', yii\base\Model, 'pattern' => null, $default = null)
    
        top:
        static::stdout("$prompt (" . implode(', 'error' => 'Invalid input.', '...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/rbac/DbManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.411 IQR)
- **Top Global Matches:** file_cluster_8: 12.411, file_cluster_13: 12.48, file_cluster_7: 12.616
- **Magnitude:** 659.58 | **LOC:** 1138 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.2391%), Tech Debt (55.8426%)
**Top Internal Functions/Classes:**
  * `checkAccessFromCache` (Impact: 21.5)
    * *Intent:* /** * Performs access check for the specified user based on the data loaded from cache. * This metho...
  * `loadFromCache` (Impact: 21.1)
  * `checkAccessRecursive` (Impact: 19.3)
    * *Intent:* /** * Performs access check for the specified user. * This method is internally called by [[checkAcc...
  * `getRolesByUser` (Impact: 12.0)
  * `getRule` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 199`, `args: 50`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 4`, `state_mutation: 297`, `orphaned_logic: 26`
* *Architecture:* `api: 35`, `import: 11`
* *Defense:* `safety: 24`, `doc: 109`, `test: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.948
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.007375
  * `Imports (Out-Degree: 7):` extra memory and, 
    public $cache, yii\base\InvalidCallException, 
    public function getRolesByUser($userId)
    
        if ($this->isEmptyUserId($userId)) 
            return [], yii\base\InvalidArgumentException, yii\di\Instance, yii\caching\CacheInterface, yii\db\Expression...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `framework/console/Controller.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.235 IQR)
- **Top Global Matches:** file_cluster_13: 15.235, file_cluster_11: 15.42, file_cluster_0: 15.471
- **Magnitude:** 658.26 | **LOC:** 809 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 91.7%
- **Risk Profile:** Cognitive Load (48.4791%), Tech Debt (67.0907%)
**Top Internal Functions/Classes:**
  * `bindActionParams` (Impact: 160.0)
  * `getActionArgsHelp` (Impact: 47.8)
  * `runAction` (Impact: 43.3)
    * *Intent:* /** * @deprecated since 2.0.13. Use [[ExitCode::OK]] instead.
  * `getActionOptionsHelp` (Impact: 26.6)
    * *Intent:* /** * Prints a string to STDERR. * * You may optionally format the string with ANSI codes by * passi...
  * `parseDocCommentTags` (Impact: 13.2)
    * *Intent:* /** * Asks user to confirm by typing y or n. * * A typical usage looks like the following: * * ``` *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 80`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 283`, `dead_code: 3`, `orphaned_logic: 11`
* *Architecture:* `api: 22`, `import: 8`
* *Defense:* `safety: 29`, `doc: 81`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` &$error) 
     *     if (strlen($input) !== 4) 
     *         $error = 'The Pin must be exactly 4 chars!', yii\base\InvalidRouteException, yii\base\Action, $options, yii\base\Module, the default value of this argument
     * - comment: string, yii\helpers\Inflector,  $actionId might be used in subclasses to provide options specific to action id
        return ['color'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Command.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.411 IQR)
- **Top Global Matches:** file_cluster_8: 14.411, file_cluster_7: 14.447, file_cluster_13: 14.455
- **Magnitude:** 616.66 | **LOC:** 1348 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.411%), Tech Debt (45.4279%)
**Top Internal Functions/Classes:**
  * `getRawSql` (Impact: 31.1)
  * `prepare` (Impact: 28.5)
    * *Intent:* /** * Enables query cache for this command. * @param int|null $duration the number of seconds that q...
  * `internalExecute` (Impact: 22.1)
    * *Intent:* /** * Creates a SQL command for dropping a DB table. * @param string $table the table to be dropped....
  * `queryInternal` (Impact: 21.5)
    * *Intent:* * * ``` * $minAge = 30; * $connection->createCommand()->update('user', ['status' => 1], 'age > :minA...
  * `bindValues` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 145`, `args: 64`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 268`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 57`, `import: 3`
* *Defense:* `safety: 29`, `doc: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` TableSchemaRefresh($viewName, 
    protected function refreshTableSchema()
    
        if ($this->_refreshTableName !== null) 
            $this->db->getSchema()->refreshTableSchema($this->_refreshTableName, Transaction($isolationLevel = null)
    
        $this->_isolationLevel = $isolationLevel, TableSchemaRefresh($name)
    
        $this->_refreshTableName = $name, $value[1], 
    public function createIndex($name, TableSchemaRefresh($table, $value[0]...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/AssetController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.243 IQR)
- **Top Global Matches:** file_cluster_13: 14.243, file_cluster_8: 14.411, file_cluster_7: 14.529
- **Magnitude:** 600.38 | **LOC:** 847 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.6595%), Tech Debt (14.4691%)
**Top Internal Functions/Classes:**
  * `adjustCssUrl` (Impact: 51.5)
  * `loadTargets` (Impact: 35.7)
    * *Intent:* /** * Returns the asset manager instance.
  * `buildTarget` (Impact: 25.9)
  * `adjustDependency` (Impact: 17.6)
  * `getAssetManager` (Impact: 15.0)
    * *Intent:* * Usage: * * 1. Create a configuration file using the `template` action: * * yii asset/template /pat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 111`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 293`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 12`, `import: 10`
* *Defense:* `safety: 44`, `doc: 105`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` yii\web\AssetBundle, all-hash.js', yii\console\Controller,  Include only 'backend' assets:
     *         'app\assets\AdminAsset'
     *     ], * ], all-hash.js', Yii, yii\console\Application...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/mssql/Schema.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.603 IQR)
- **Top Global Matches:** file_cluster_13: 13.603, file_cluster_8: 13.692, file_cluster_7: 13.871
- **Magnitude:** 588.6 | **LOC:** 832 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.3771%), Tech Debt (78.6566%)
**Top Internal Functions/Classes:**
  * `loadColumnSchema` (Impact: 39.3)
    * *Intent:* /** * {@inheritdoc}
  * `loadTableConstraints` (Impact: 29.3)
  * `findColumns` (Impact: 22.7)
  * `insert` (Impact: 15.3)
  * `resolveTableName` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 94`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 356`, `orphaned_logic: 17`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 12`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` yii\db\DefaultValueConstraint, yii\db\ConstraintFinderTrait, yii\db\CheckConstraint, ConstraintFinderTrait, yii\db\ForeignKeyConstraint, yii\db\ViewFinderTrait, ViewFinderTrait, yii\db\ConstraintFinderInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/mssql/QueryBuilder.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.903 IQR)
- **Top Global Matches:** file_cluster_13: 13.903, file_cluster_8: 13.91, file_cluster_7: 14.013
- **Magnitude:** 585.72 | **LOC:** 692 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (33.9654%), Tech Debt (80.5219%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 34.4)
  * `upsert` (Impact: 32.3)
  * `oldBuildOrderByAndLimit` (Impact: 19.1)
    * *Intent:* /** * Builds the ORDER BY/LIMIT/OFFSET clauses for SQL SERVER 2012 or newer. * @param string $sql th...
  * `alterColumn` (Impact: 15.9)
  * `normalizeTableRowData` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 87`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 327`, `orphaned_logic: 16`
* *Architecture:* `api: 19`, `import: 5`
* *Defense:* `safety: 10`, `doc: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` yii\db\TableSchema, s an ORDER BY clause
            $orderBy = 'ORDER BY (SELECT NULL)', yii\base\InvalidArgumentException, d when FETCH and OFFSET are in the SQL
            $orderBy = 'ORDER BY (SELECT NULL)', yii\base\NotSupportedException, yii\db\Expression, yii\db\Query
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/web/UrlRule.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.698 IQR)
- **Top Global Matches:** file_cluster_13: 14.698, file_cluster_0: 14.827, file_cluster_11: 14.858
- **Magnitude:** 570.12 | **LOC:** 605 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (40.8897%), Tech Debt (35.5754%)
**Top Internal Functions/Classes:**
  * `createUrl` (Impact: 76.2)
  * `translatePattern` (Impact: 68.0)
    * *Intent:* /**
  * `parseRequest` (Impact: 43.2)
  * `preparePattern` (Impact: 24.4)
    * *Intent:* /** * @var int|null a value indicating if this rule should be used for both request parsing and URL ...
  * `init` (Impact: 24.0)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 57`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 277`, `dead_code: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 21`, `import: 3`
* *Defense:* `safety: 22`, `doc: 72`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` dPatternPart = $this->pattern, yii\base\BaseObject, ', yii\base\InvalidConfigException, $requiredPatternPart, dPatternPart, ') === '') 
            $this->translatePattern(false, "...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/rbac/PhpManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.717 IQR)
- **Top Global Matches:** file_cluster_13: 13.717, file_cluster_8: 13.724, file_cluster_7: 13.873
- **Magnitude:** 565.02 | **LOC:** 897 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (34.4829%), Tech Debt (96.5194%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 25.0)
    * *Intent:* /** * {@inheritdoc} */
  * `removeAllItems` (Impact: 22.5)
  * `checkAccessRecursive` (Impact: 21.4)
    * *Intent:* /**
  * `updateItem` (Impact: 15.6)
    * *Intent:* /** * Returns all permissions that the user inherits from the roles assigned to him. * @param string...
  * `addChild` (Impact: 13.3)
    * *Intent:* /** * {@inheritdoc} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 158`, `args: 50`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 225`, `orphaned_logic: 31`
* *Architecture:* `io: 1`, `api: 32`, `import: 5`
* *Defense:* `safety: 44`, `doc: 99`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.831
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.00295
  * `Imports (Out-Degree: 4):` 
    public function getRolesByUser($userId)
    
        $roles = $this->getDefaultRoleInstances(, yii\helpers\VarDumper, yii\base\InvalidCallException, yii\base\InvalidArgumentException, Yii, $file
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseFileHelper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.46 IQR)
- **Top Global Matches:** file_cluster_13: 14.46, file_cluster_8: 14.691, file_cluster_11: 14.776
- **Magnitude:** 561.84 | **LOC:** 1032 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (43.6989%), Tech Debt (30.6179%)
**Top Internal Functions/Classes:**
  * `changeOwnership` (Impact: 58.9)
    * *Intent:* /** * Copies a whole directory as another one. * The files and sub-directories will also be copied o...
  * `copyDirectory` (Impact: 52.8)
  * `normalizePath` (Impact: 32.7)
  * `removeDirectory` (Impact: 23.9)
  * `unlink` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 66`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 273`, `orphaned_logic: 5`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 25`, `doc: 60`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pattern must be a string.', yii\base\InvalidArgumentException, 
    public static function findFiles($dir, $aliasesFile, flags and firstWildcard keys.', en#_pattern_format).
     * - `only`: array, $options = [])
    
        $dir = self::clearDir($dir, Yii...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/HelpController.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.955 IQR)
- **Top Global Matches:** file_cluster_13: 13.955, file_cluster_8: 14.027, file_cluster_7: 14.205
- **Magnitude:** 557.06 | **LOC:** 570 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.7729%), Tech Debt (20.9977%)
**Top Internal Functions/Classes:**
  * `formatOptionHelp` (Impact: 33.6)
  * `getSubCommandHelp` (Impact: 32.9)
  * `getDefaultHelp` (Impact: 23.6)
  * `actionIndex` (Impact: 21.3)
  * `getModuleCommands` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 79`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 315`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 13`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004425
  * `Imports (Out-Degree: 4):` Console::FG_CYAN, 
    protected function formatOptionHelp($name, d ? "$name (required)" : $name, $defaultValue, yii\base\Module, yii\console\Controller, yii\helpers\Inflector, yii\base\Application...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `framework/web/Response.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.509 IQR)
- **Top Global Matches:** file_cluster_13: 13.509, file_cluster_8: 13.661, file_cluster_7: 13.708
- **Magnitude:** 537.0 | **LOC:** 1158 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (45.3291%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `sendContent` (Impact: 101.6)
  * `sendCookies` (Impact: 30.0)
    * *Intent:* /** * @var HeaderCollection|null
  * `redirect` (Impact: 29.9)
    * *Intent:* /** * Sends the response headers to the client. */
  * `prepare` (Impact: 26.3)
    * *Intent:* /** * Sends a file to the browser. * * Note that this method only prepares the response for file sen...
  * `setStatusCode` (Impact: 11.2)
    * *Intent:* /** * @var string the HTTP status description that comes together with the status code.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 88`, `args: 28`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 206`, `planned_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 5`, `api: 40`, `import: 8`
* *Defense:* `safety: 11`, `doc: 109`, `test: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` 504 => 'Gateway Time-out', yii\base\InvalidRouteException, 417 => 'Expectation failed', 424 => 'Method failure', 408 => 'Request Time-out', 415 => 'Unsupported Media Type', yii\base\InvalidArgumentException, 421 => 'Misdirected Request'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/helpers/BaseHtml.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.757 IQR)
- **Top Global Matches:** file_cluster_13: 14.757, file_cluster_8: 14.896, file_cluster_7: 14.955
- **Magnitude:** 519.42 | **LOC:** 2412 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.5653%), Tech Debt (94.4163%)
**Top Internal Functions/Classes:**
  * `beginForm` (Impact: 30.2)
  * `normalizeMaxLength` (Impact: 16.6)
    * *Intent:* * * If you want to use an absolute url you can call [[Url::to()]] yourself, before passing the URL t...
  * `errorSummary` (Impact: 13.3)
    * *Intent:* // query parameters in the action are ignored for GET method // we use hidden fields to add them bac...
  * `cssFile` (Impact: 9.6)
    * *Intent:* /** * Generates a complete HTML tag. * @param string|bool|null $name the tag name. If $name is `null...
  * `img` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 91`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 261`, `orphaned_logic: 19`
* *Architecture:* `io: 5`, `api: 38`, `import: 6`
* *Defense:* `safety: 27`, `doc: 164`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` yii\web\Request, yii\base\Model, yii\base\InvalidArgumentException, Yii, yii\validators\StringValidator, yii\db\ActiveRecordInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/i18n/MessageFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.225 IQR)
- **Top Global Matches:** file_cluster_13: 14.225, file_cluster_8: 14.505, file_cluster_11: 14.523
- **Magnitude:** 514.76 | **LOC:** 443 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.6907%), Tech Debt (15.7499%)
**Top Internal Functions/Classes:**
  * `parseToken` (Impact: 98.5)
  * `replaceNamedArguments` (Impact: 38.1)
    * *Intent:* /** * Formats a message via [ICU message format](https://unicode-org.github.io/icu/userguide/format_...
  * `tokenizePattern` (Impact: 29.8)
  * `parse` (Impact: 20.6)
    * *Intent:* * * This class enhances the message formatter class provided by the PHP intl extension. * * The foll...
  * `fallbackFormat` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 51`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 305`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 9`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` conforming to the pattern.
     * @param string $language The locale to use for formatting locale-dependent parts
     * @return array|bool An array containing items extracted, $language)
    
        $this->_errorCode = 0, yii\base\NotSupportedException, $message, 
    public function parse($pattern, Yii, yii\base\Component, s PHP intl extension to be installed.
     *
     * @param string $pattern The pattern to use for parsing the message.
     * @param string $message The message to parse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/oci/Schema.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.556 IQR)
- **Top Global Matches:** file_cluster_13: 13.556, file_cluster_8: 13.756, file_cluster_7: 13.922
- **Magnitude:** 511.14 | **LOC:** 748 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (34.8792%), Tech Debt (96.9826%)
**Top Internal Functions/Classes:**
  * `extractColumnType` (Impact: 30.6)
  * `loadTableConstraints` (Impact: 25.5)
  * `createColumn` (Impact: 24.4)
    * *Intent:* // does nothing as Oracle does not support this
  * `insert` (Impact: 19.6)
  * `findConstraints` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 95`, `args: 27`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 273`, `fragile_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 8`, `api: 9`, `import: 16`
* *Defense:* `safety: 13`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` yii\db\TableSchema, yii\db\ConstraintFinderTrait, yii\db\CheckConstraint, yii\db\ColumnSchema, ConstraintFinderTrait, yii\base\InvalidCallException, yii\db\ForeignKeyConstraint, yii\base\NotSupportedException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Query.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.903 IQR)
- **Top Global Matches:** file_cluster_13: 12.903, file_cluster_8: 13.02, file_cluster_7: 13.136
- **Magnitude:** 487.8 | **LOC:** 1403 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.7305%), Tech Debt (16.8577%)
**Top Internal Functions/Classes:**
  * `column` (Impact: 35.5)
    * *Intent:* /** * @var int|bool|null the default number of seconds that query results can remain valid in cache....
  * `setCommandCache` (Impact: 7.4)
  * `populate` (Impact: 5.8)
  * `createCommand` (Impact: 5.1)
    * *Intent:* * $query->select('id, name') * ->from('user') * ->limit(10); * // build and execute the query * $row...
  * `all` (Impact: 5.0)
    * *Intent:* /** * @var array|null how to join with other tables. Each array element represents the specification...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 224`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 118`, `high_risk_execution: 29`, `state_mutation: 305`, `orphaned_logic: 8`
* *Architecture:* `api: 60`, `import: 20`
* *Defense:* `safety: 23`, `doc: 206`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.379
  * `Choke Point (Betweenness):` 0.000351 | `Ripple Effect (Closeness):` 0.03401
  * `Imports (Out-Degree: 6):` 
    public function populate($rows)
    
        if ($this->indexBy === null) 
            return $rows, `*` explicitly
     * if you want to select all remaining columns too:
     *
     * ```
     * $query->addSelect(["*", "CONCAT(first_name, last_name) AS full_name"])->one(, 
    public function where($condition, QueryTrait, yii\base\InvalidArgumentException, yii\base\InvalidConfigException...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `framework/db/mysql/Schema.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.592 IQR)
- **Top Global Matches:** file_cluster_13: 13.592, file_cluster_8: 13.801, file_cluster_17: 13.944
- **Magnitude:** 486.3 | **LOC:** 668 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.7118%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `loadColumnSchema` (Impact: 56.9)
  * `loadTableConstraints` (Impact: 21.9)
  * `findConstraints` (Impact: 19.5)
    * *Intent:* /** * When displayed in the INFORMATION_SCHEMA.COLUMNS table, a default CURRENT TIMESTAMP is display...
  * `findColumns` (Impact: 19.3)
    * *Intent:* /** * Loads the column information into a [[ColumnSchema]] object. * @param array $info column infor...
  * `loadTableChecks` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 85`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 281`, `orphaned_logic: 12`
* *Architecture:* `io: 3`, `api: 5`, `import: 15`
* *Defense:* `safety: 19`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` yii\db\TableSchema, yii\db\ConstraintFinderTrait, yii\db\CheckConstraint, ConstraintFinderTrait, yii\db\ForeignKeyConstraint, yii\helpers\ArrayHelper, yii\base\InvalidConfigException, yii\base\NotSupportedException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/sqlite/SqlTokenizer.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.118 IQR)
- **Top Global Matches:** file_cluster_8: 10.118, file_cluster_7: 10.704, file_cluster_1: 10.937
- **Magnitude:** 464.55 | **LOC:** 292 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.546%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 57`
* *Architecture:* None
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.858
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `framework/db/DataReader.php` (PHP) | Magnitude: 78.52 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, doc: 45, structural_boundaries: 32, state_mutation: 23
- `tests/js/data/yii.html` (HTML) | Magnitude: 47.22 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 156, args: 136, io: 70, decorators: 65
- `framework/web/HeaderCollection.php` (PHP) | Magnitude: 95.92 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 105, doc: 55, structural_boundaries: 41, state_mutation: 30
- `framework/db/mssql/SqlsrvPDO.php` (PHP) | Magnitude: 8.9 | Delta: **0.265 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 5, indent_spaces: 5, state_mutation: 3
- `framework/db/mssql/DBLibPDO.php` (PHP) | Magnitude: 17.26 | Delta: **0.274 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 10, doc: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `framework/db/conditions/LikeCondition.php` (PHP) | Magnitude: 23.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 15, doc: 14, branch: 10
- `framework/db/mssql/QueryBuilder.php` (PHP) | Magnitude: 585.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 408, state_mutation: 327, doc: 89, structural_boundaries: 87
- `framework/rbac/PhpManager.php` (PHP) | Magnitude: 565.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 532, state_mutation: 225, structural_boundaries: 158, branch: 106
- `tests/data/ar/CustomerWithConstructor.php` (PHP) | Magnitude: 0.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 15, doc: 8, args: 5
- `framework/web/UploadedFile.php` (PHP) | Magnitude: 147.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 224, doc: 66, structural_boundaries: 57, state_mutation: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/framework/db/AnyCaseValue.php` (PHP) | Magnitude: 16.9 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 9, structural_boundaries: 4, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `framework/views/migration.php` (PHP) | Magnitude: 9.76 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, branch: 8, structural_boundaries: 6, doc: 5
- `framework/base/ViewRenderer.php` (PHP) | Magnitude: 32.4 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 4, ownership: 2, branch: 1
- `framework/i18n/migrations/m150207_210500_i18n_init.php` (PHP) | Magnitude: 29.42 | Delta: **0.263 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 18, ui_framework: 10, structural_boundaries: 5
- `framework/views/createTableMigration.php` (PHP) | Magnitude: 19.48 | Delta: **0.27 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, branch: 13, doc: 11, ui_framework: 7
- `framework/views/addColumnMigration.php` (PHP) | Magnitude: 13.76 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 10, doc: 10, ui_framework: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/framework/db/testBatchInsertWithYield.php` (PHP) | Magnitude: 27.28 | Delta: **0.366 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 6, concurrency: 6, indent_spaces: 6, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `framework/base/DynamicContentAwareInterface.php` (PHP) | Magnitude: 47.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 5, args: 3, func_start: 3
- `framework/web/IdentityInterface.php` (PHP) | Magnitude: 60.19 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 7, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `framework/base/Security.php` (PHP) | Magnitude: 309.78 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 208, state_mutation: 156, doc: 120, structural_boundaries: 64
- `framework/db/QueryInterface.php` (PHP) | Magnitude: 119.38 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 51, structural_boundaries: 18, args: 16, func_start: 16
- `framework/web/Cookie.php` (PHP) | Magnitude: 21.3 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 23, indent_spaces: 15, api: 12, state_mutation: 7
- `framework/db/ConstraintFinderInterface.php` (PHP) | Magnitude: 112.95 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 50, state_mutation: 20, structural_boundaries: 14, args: 12
- `framework/rbac/ManagerInterface.php` (PHP) | Magnitude: 166.13 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 98, structural_boundaries: 35, args: 32, func_start: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `framework/web/MultipartFormDataParser.php` (PHP) | Magnitude: 316.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 218, state_mutation: 168, branch: 62, structural_boundaries: 39
- `framework/base/Event.php` (PHP) | Magnitude: 209.56 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 142, state_mutation: 103, branch: 43, structural_boundaries: 29
- `framework/base/ActionFilter.php` (PHP) | Magnitude: 102.04 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 45, doc: 25, structural_boundaries: 19
- `framework/web/Request.php` (PHP) | Magnitude: 951.56 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1090, state_mutation: 559, branch: 271, structural_boundaries: 254
- `framework/db/ExpressionBuilderTrait.php` (PHP) | Magnitude: 5.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 6, indent_spaces: 5, structural_boundaries: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `framework/base/ActionEvent.php` (PHP) | Magnitude: 11.26 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_spaces: 8, state_mutation: 5, structural_boundaries: 4
- `framework/caching/ExpressionDependency.php` (PHP) | Magnitude: 7.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 6, indent_spaces: 6, state_mutation: 3
- `framework/data/DataProviderInterface.php` (PHP) | Magnitude: 72.81 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 9, args: 7, func_start: 7
- `framework/caching/MemCacheServer.php` (PHP) | Magnitude: 31.26 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 18, api: 8, state_mutation: 8, indent_spaces: 8
- `framework/rbac/migrations/schema-oci.sql` (SQLITE) | Magnitude: 0.71 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, safety: 11, duplicate_logic: 10, class_start: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `framework/console/Controller.php` -> Churn: **100.0%** | Cog Load: 48.4791% | Debt: 67.0907%
- `framework/base/Application.php` -> Churn: **87.0%** | Cog Load: 37.8405% | Debt: 99.9742%
- `framework/base/Model.php` -> Churn: **85.92%** | Cog Load: 39.1537% | Debt: 79.7088%
- `framework/base/Module.php` -> Churn: **78.59%** | Cog Load: 36.652% | Debt: 97.8398%
- `framework/console/controllers/BaseMigrateController.php` -> Churn: **78.59%** | Cog Load: 38.6367% | Debt: 56.7602%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `framework/web/Request.php` -> **Maksim Spirkov** (83.3% isolated ownership) | Magnitude: 951.56
- `framework/helpers/BaseArrayHelper.php` -> **Maksim Spirkov** (100.0% isolated ownership) | Magnitude: 746.3
- `framework/console/controllers/BaseMigrateController.php` -> **Maksim Spirkov** (88.9% isolated ownership) | Magnitude: 726.94
- `framework/db/Connection.php` -> **Maksim Spirkov** (83.3% isolated ownership) | Magnitude: 699.36
- `framework/db/ActiveQuery.php` -> **Maksim Spirkov** (87.5% isolated ownership) | Magnitude: 676.9

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

- `framework/Yii.php` -> **Severity: 21.7** (Embedded: 0.2815 * Error Risk: 77.0804%)
- `framework/base/Component.php` -> **Severity: 9.308** (Embedded: 0.121 * Error Risk: 76.9336%)
- `framework/base/BaseObject.php` -> **Severity: 5.983** (Embedded: 0.0888 * Error Risk: 67.3415%)
- `framework/db/Connection.php` -> **Severity: 4.067** (Embedded: 0.0453 * Error Risk: 89.6878%)
- `framework/base/Model.php` -> **Severity: 3.858** (Embedded: 0.0477 * Error Risk: 80.9083%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `framework/Yii.php` -> **Severity: 840.597** (Blast Radius: 88.148 * Doc Risk: 9.5362%)
- `framework/base/BaseObject.php` -> **Severity: 580.147** (Blast Radius: 32.446 * Doc Risk: 17.8804%)
- `framework/db/SchemaBuilderTrait.php` -> **Severity: 510.9** (Blast Radius: 5.109 * Doc Risk: 100.0%)
- `framework/base/Component.php` -> **Severity: 397.839** (Blast Radius: 22.25 * Doc Risk: 17.8804%)
- `framework/db/Migration.php` -> **Severity: 357.733** (Blast Radius: 20.007 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
