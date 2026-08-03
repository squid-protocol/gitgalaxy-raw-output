# ARCHITECTURAL_BRIEF: db-tutorial
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/db-tutorial` |
| **Timestamp** | `2026-08-03T20:10:06.262541+00:00` |
| **Scan Duration** | `0.88s` |
| **Git Branch** | `master` |
| **Git Commit** | `47d7d1552f1be6cde030d44b19d976553965886a` |
| **Git Remote** | `https://github.com/dunwu/db-tutorial.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 232 malicious artifacts.

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
| Total Artifacts | 472 |
| Analyzed Artifacts (Scanned) | 279 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 193 |
| Total LOC | 17393 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 59.1% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7827 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1764 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7835 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 176 | 12727 | 63.1% |
| XML | 22 | 0 | 7.9% |
| SHELL | 18 | 207 | 6.5% |
| PLAINTEXT | 16 | 0 | 5.7% |
| BATCH | 16 | 98 | 5.7% |
| PYTHON | 12 | 3799 | 4.3% |
| SQLITE | 6 | 33 | 2.2% |
| MARKDOWN | 5 | 0 | 1.8% |
| JAVASCRIPT | 4 | 136 | 1.4% |
| JSON | 3 | 389 | 1.1% |
| YAML | 1 | 4 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.958`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 129 | 46.2% |
| file_cluster_8 | 101 | 36.2% |
| file_cluster_4 | 8 | 2.9% |
| file_cluster_0 | 7 | 2.5% |
| file_cluster_16 | 7 | 2.5% |
| file_cluster_9 | 4 | 1.4% |
| file_cluster_17 | 1 | 0.4% |
| file_cluster_7 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 21 | 7.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 193*

**Composition by Extension & Reason:**
- `no_extension`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded (Unsupported Extension: '.sql"'), 2x Excluded (Unsupported Extension: '.md"')
- `.conf`: 30x Excluded (Unsupported Extension: '.conf')
- `.rdb`: 12x Excluded (Unsupported Extension: '.rdb')
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 7607 LOC), 1x Excluded (Massive Static Asset Blob: 3601 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.styl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.1 | 31.8 | 28.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.3 | 1.1 | 0.0 |
| API Exposure | 0.0 | 12.1 | 3.9 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 72.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.5 | 15.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 32.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` (Hits: 18)
- `codes/javadb/sqlite/src/main/java/io/github/dunwu/javadb/sqlite/springboot/SqliteDemo.java` (Hits: 16)
- `utils/editFrontmatter.js` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **redis.xml** (`codes/javadb/redis/src/test/resources/redis.xml`) — 12 inbound connections
2. **BaseHbaseEntity.java** (`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/BaseHbaseEntity.java`) — 7 inbound connections
3. **PageData.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/common/PageData.java`) — 6 inbound connections
4. **ScrollData.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/common/ScrollData.java`) — 6 inbound connections
5. **BaseEsEntity.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/BaseEsEntity.java`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ElasticsearchTemplate.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java`) — 72 outbound dependencies
2. **HbaseTemplate.java** (`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java`) — 51 outbound dependencies
3. **BaseEsMapper.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java`) — 28 outbound dependencies
4. **RestHighLevelClientDocumentApiTest.java** (`codes/javadb/elasticsearch/elasticsearch7/src/test/java/io/github/dunwu/javadb/elasticsearch/springboot/RestHighLevelClientDocumentApiTest.java`) — 27 outbound dependencies
5. **UserEsMapperTest.java** (`codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper/UserEsMapperTest.java`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `syndicate_status` (@ `codes/redis/redis-in-action-py/ch08_listing_source.py`) -> Impact: **302.7** | LOC: 241
  * *Intent:* # 以上次被更新的最后一个关注者为起点，获取接下来的一千个关注者。 followers = conn.zrangebyscore('followers:%s' % uid, start, 'inf', start=0, num=POSTS_PER_PASS, withscores=True) pip...
- `testMultiRecipientMessaging` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`) -> Impact: **281.1** | LOC: 31
- `createIndex` (@ `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java`) -> Impact: **265.6** | LOC: 21
- `testFileDistribution` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`) -> Impact: **226.8** | LOC: 64
- `testAddUpdateContact` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`) -> Impact: **226.2** | LOC: 52
- `testUserLocation` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java`) -> Impact: **189.8** | LOC: 39
- `cleanTimelines` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter08.java`) -> Impact: **185.3** | LOC: 31
- `updateCpms` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java`) -> Impact: **181.3** | LOC: 75
- `refillTimeline` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter08.java`) -> Impact: **176.5** | LOC: 42
- `run` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`) -> Impact: **164.6** | LOC: 71

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `matchPhraseQuery` (@ `codes/javadb/elasticsearch/elasticsearch7/src/test/java/io/github/dunwu/javadb/elasticsearch/springboot/RestHighLevelClientDocumentSearchApiTest.java`) -> **O(2^N) [Recursive]**
- `batchDelete` (@ `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java`) -> **O(2^N) [Recursive]**
- `toScan` (@ `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/scan/MultiFamilyScan.java`) -> **O(2^N) [Recursive]**
- `batchSave` (@ `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/HbaseMapperTest.java`) -> **O(2^N) [Recursive]**
- `update` (@ `codes/javadb/mysql/src/main/java/io/github/dunwu/javadb/mysql/springboot/UserDaoImpl.java`) -> **O(2^N) [Recursive]**
- `createIndex` (@ `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java`) -> **O(2^N) [Recursive]**
- `deleteIndex` (@ `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java`) -> **O(2^N) [Recursive]**
- `pojoPageByLastId` (@ `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper/UserEsMapperTest.java`) -> **O(2^N) [Recursive]**
- `pojoPageByLastIdInDay` (@ `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper/UserEsMapperTest.java`) -> **O(2^N) [Recursive]**
- `pojoScroll` (@ `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper/UserEsMapperTest.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `testFileDistribution` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`) -> DB Complexity: **24**
- `main` (@ `utils/editFrontmatter.js`) -> DB Complexity: **22**
- `readFileList` (@ `utils/modules/readFileList.js`) -> DB Complexity: **21**
- `copy_logs_to_redis` (@ `codes/redis/redis-in-action-py/ch06_listing_source.py`) -> DB Complexity: **14**
  * *Intent:* # <end id="_1314_15044_3669"/> # 代码清单 6-30 # <start id="_1314_14473_9209"/>
- `run` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`) -> DB Complexity: **13**
- `testIpLookup` (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java`) -> DB Complexity: **12**
- `getRestClientBuilder` (@ `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchFactory.java`) -> DB Complexity: **10**
- `select` (@ `codes/javadb/sqlite/src/main/java/io/github/dunwu/javadb/sqlite/springboot/SqliteDemo.java`) -> DB Complexity: **10**
- `printDataSourceInfo` (@ `codes/javadb/h2/src/main/java/io/github/dunwu/javadb/h2/springboot/SpringBootDataJpaApplication.java`) -> DB Complexity: **9**
- `redisTemplate` (@ `codes/javadb/redis/src/main/java/io/github/dunwu/javadb/redis/springboot/RedisAutoConfiguration.java`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis` | 10 | 9619.66 | 31.9% | 57.43% |
| `codes/redis/redis-in-action-py` | 13 | 3320.1 | 9.56% | 51.03% |
| `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper` | 4 | 2132.56 | 9.73% | 89.28% |
| `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase` | 3 | 1914.32 | 6.8% | 66.66% |
| `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch` | 2 | 1257.56 | 21.45% | 93.02% |
| `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank` | 5 | 1021.12 | 7.95% | 0.0% |
| `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper` | 1 | 707.96 | 8.59% | 0.0% |
| `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch` | 4 | 611.66 | 8.1% | 0.0% |
| `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper` | 7 | 573.96 | 7.2% | 66.57% |
| `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase` | 7 | 507.4 | 16.12% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchFactory.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/exception/CodeMsgException.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/exception/DefaultException.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities/Article.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities/Product.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/common/ColumnDo.java` -> **100.0%** Exposure
- `scripts/deploy.sh` -> **100.0%** Exposure
- `utils/modules/fn.js` -> **100.0%** Exposure
- `utils/modules/readFileList.js` -> **100.0%** Exposure
- `codes/redis/redis-config/sentinel3/linux/server-6380/start.sh` -> **99.9987%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` -> **0** Orphaned Functions | **47** Duplicates
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseDynamicEsMapper.java` -> **15** Orphaned Functions | **4** Duplicates
- `codes/redis/redis-in-action-py/ch11_listing_source.py` -> **11** Orphaned Functions | **8** Duplicates
- `codes/redis/redis-in-action-py/ch06_listing_source.py` -> **17** Orphaned Functions | **0** Duplicates
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` -> **4** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseDynamicEsMapper.java`** -> AI Confidence: **99.31%**
2. **`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java`** -> AI Confidence: **99.31%**
3. **`codes/javadb/mysql/src/test/java/io/github/dunwu/javadb/mysql/springboot/MysqlDemoTest.java`** -> AI Confidence: **99.31%**
4. **`codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank/RankDemo.java`** -> AI Confidence: **99.31%**
5. **`codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter04.java`** -> AI Confidence: **99.31%**
6. **`codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java`** -> AI Confidence: **99.31%**
7. **`codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java`** -> AI Confidence: **99.31%**
8. **`codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java`** -> AI Confidence: **99.31%**
9. **`codes/redis/redis-in-action-py/ch06_listing_source.py`** -> AI Confidence: **99.31%**
10. **`codes/redis/redis-in-action-py/ch09_listing_source.py`** -> AI Confidence: **99.31%**
11. **`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchFactory.java`** -> AI Confidence: **99.24%**
12. **`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/util/JsonUtil.java`** -> AI Confidence: **99.24%**
13. **`codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java`** -> AI Confidence: **99.24%**
14. **`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/util/JsonUtil.java`** -> AI Confidence: **99.24%**
15. **`codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/HbaseTemplateScanTest.java`** -> AI Confidence: **99.24%**
16. **`codes/redis/redis-in-action-py/ch05_listing_source.py`** -> AI Confidence: **99.24%**
17. **`codes/redis/redis-in-action-py/ch08_listing_source.py`** -> AI Confidence: **99.24%**
18. **`codes/redis/redis-in-action-py/ch10_listing_source.py`** -> AI Confidence: **99.24%**
19. **`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/annotation/RowKeyUtil.java`** -> AI Confidence: **99.23%**
20. **`utils/editFrontmatter.js`** -> AI Confidence: **99.23%**
21. **`codes/javadb/h2/src/main/java/io/github/dunwu/javadb/h2/springboot/SpringBootDataJpaApplication.java`** -> AI Confidence: **99.18%**
22. **`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseAdmin.java`** -> AI Confidence: **99.18%**
23. **`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/common/ColumnDo.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchFactory.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/constant/ResultCode.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/exception/CodeMsgException.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseDynamicEsMapper.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseDynamicEsMapper.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch7/src/test/java/io/github/dunwu/javadb/elasticsearch/springboot/RestHighLevelClientDocumentSearchApiTest.java` -> **100.0%** Exposure
- `codes/javadb/h2/src/test/java/io/github/dunwu/javadb/h2/H2JdbcTest.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchFactory.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/exception/CodeMsgException.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1407` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` (JAVA) -> Cumulative Risk: **948.95**
- **Archetype:** `file_cluster_13` (Distance: 10.882 IQR)
- **Magnitude:** 963.18 | **LOC:** 702 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `pojoListByIds` (Impact: 68.7), `updateById` (Impact: 65.6), `save` (Impact: 65.5)

### 2. `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter02.java` (JAVA) -> Cumulative Risk: **862.4**
- **Archetype:** `file_cluster_8` (Distance: 11.604 IQR)
- **Magnitude:** 1037.18 | **LOC:** 503 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `testShopppingCartCookies` (Impact: 126.9), `run` (Impact: 120.8), `testCacheRows` (Impact: 118.5)

### 3. `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter01.java` (JAVA) -> Cumulative Risk: **797.04**
- **Archetype:** `file_cluster_16` (Distance: 11.736 IQR)
- **Magnitude:** 283.16 | **LOC:** 186 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9921%)
- **Heaviest Functions:** `run` (Impact: 57.5), `printArticles` (Impact: 47.3), `addRemoveGroups` (Impact: 36.4)

### 4. `codes/redis/redis-in-action-py/ch11_listing_source.py` (PYTHON) -> Cumulative Risk: **793.59**
- **Archetype:** `file_cluster_8` (Distance: 10.249 IQR)
- **Magnitude:** 292.56 | **LOC:** 799 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Tech Debt (99.9992%)
- **Heaviest Functions:** `sharded_bpop_helper` (Impact: 41.1), `create_status` (Impact: 15.9), `autocomplete_on_prefix` (Impact: 15.6)

### 5. `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java` (JAVA) -> Cumulative Risk: **791.41**
- **Archetype:** `file_cluster_8` (Distance: 11.059 IQR)
- **Magnitude:** 1529.24 | **LOC:** 732 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9998%)
- **Heaviest Functions:** `testIpLookup` (Impact: 163.1), `run` (Impact: 135.7), `testCounters` (Impact: 109.2)

### 6. `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter08.java` (JAVA) -> Cumulative Risk: **777.29**
- **Archetype:** `file_cluster_8` (Distance: 12.373 IQR)
- **Magnitude:** 1285.12 | **LOC:** 537 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9966%)
- **Heaviest Functions:** `cleanTimelines` (Impact: 185.3), `refillTimeline` (Impact: 176.5), `syndicateStatus` (Impact: 148.2)

### 7. `codes/javadb/mysql/src/main/java/io/github/dunwu/javadb/mysql/springboot/UserDaoImpl.java` (JAVA) -> Cumulative Risk: **769.96**
- **Archetype:** `file_cluster_0` (Distance: 10.172 IQR)
- **Magnitude:** 246.0 | **LOC:** 111 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `update` (Impact: 94.1), `insert` (Impact: 39.3), `queryByName` (Impact: 31.7)

### 8. `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` (JAVA) -> Cumulative Risk: **766.21**
- **Archetype:** `file_cluster_13` (Distance: 11.692 IQR)
- **Magnitude:** 1556.6 | **LOC:** 1012 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `newPut` (Impact: 121.8), `getFamilyMap` (Impact: 121.6), `getScrollData` (Impact: 95.9)

### 9. `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/common/ColumnDo.java` (JAVA) -> Cumulative Risk: **764.11**
- **Archetype:** `file_cluster_13` (Distance: 10.103 IQR)
- **Magnitude:** 75.72 | **LOC:** 83 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `toKvMap` (Impact: 35.4), `toColumnMap` (Impact: 13.7), `check` (Impact: 6.2)

### 10. `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/exception/CodeMsgException.java` (JAVA) -> Cumulative Risk: **755.92**
- **Archetype:** `file_cluster_8` (Distance: 10.082 IQR)
- **Magnitude:** 114.4 | **LOC:** 129 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getMessage` (Impact: 16.3), `CodeMsgException` (Impact: 3.7), `CodeMsgException` (Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.834 IQR)
- **Top Global Matches:** file_cluster_8: 11.834, file_cluster_16: 11.915, file_cluster_0: 11.922
- **Magnitude:** 2162.1 | **LOC:** 951 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (31.9392%), Tech Debt (67.8095%)
**Top Internal Functions/Classes:**
  * `testMultiRecipientMessaging` (Impact: 281.1 | O(2^N) | DB: 2)
  * `testFileDistribution` (Impact: 226.8 | O(2^N) | DB: 24)
  * `testAddUpdateContact` (Impact: 226.2 | O(2^N) | DB: 1)
  * `run` (Impact: 164.6 | O(N^6) | DB: 13)
  * `testDelayedTasks` (Impact: 117.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 133`, `args: 57`, `func_start: 74`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 74`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `io: 18`, `api: 51`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 46`, `doc: 7`, `sync_locks: 10`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` redis.clients.jedis.ZParams, java.util.zip.GZIPOutputStream, com.google.gson.Gson, java.util.*, redis.clients.jedis.Transaction, java.util.zip.GZIPInputStream, java.io.*, redis.clients.jedis.Tuple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.526 IQR)
- **Top Global Matches:** file_cluster_8: 12.526, file_cluster_16: 12.54, file_cluster_0: 12.638
- **Magnitude:** 1888.52 | **LOC:** 959 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (55.4577%), Tech Debt (15.0363%)
**Top Internal Functions/Classes:**
  * `updateCpms` (Impact: 181.3 | O(N^4) | DB: 3)
  * `testStringToScore` (Impact: 127.5 | O(2^N) | DB: 6)
  * `testIndexAndTargetAds` (Impact: 109.1 | O(2^N))
  * `recordClick` (Impact: 102.1 | O(N^4) | DB: 1)
  * `indexAd` (Impact: 101.8 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 145`, `args: 56`, `func_start: 85`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 166`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `safety: 55`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` redis.clients.jedis.*, java.util.regex.Matcher, java.util.*, org.javatuples.Pair, java.util.regex.Pattern
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.18 IQR)
- **Top Global Matches:** file_cluster_0: 11.18, file_cluster_13: 11.327, file_cluster_8: 11.394
- **Magnitude:** 1600.4 | **LOC:** 503 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (18.8925%), Tech Debt (99.4661%)
**Top Internal Functions/Classes:**
  * `createIndex` (Impact: 265.6 | O(2^N) | DB: 1)
  * `save` (Impact: 63.4 | O(2^N))
  * `saveBatch` (Impact: 63.4 | O(2^N))
  * `updateBatchIds` (Impact: 63.3 | O(2^N))
  * `deleteById` (Impact: 63.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 113`, `args: 44`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 3`, `duplicate_logic: 12`, `orphaned_logic: 4`
* *Architecture:* `api: 45`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 50`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.elasticsearch.action.search.SearchResponse, java.util.Map, java.lang.reflect.Method, org.elasticsearch.action.get.GetResponse, org.elasticsearch.search.builder.SearchSourceBuilder, cn.hutool.core.util.ReflectUtil, java.util.HashSet, org.elasticsearch.action.ActionListener...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.692 IQR)
- **Top Global Matches:** file_cluster_13: 11.692, file_cluster_16: 11.801, file_cluster_8: 12.036
- **Magnitude:** 1556.6 | **LOC:** 1012 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (10.7883%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `newPut` (Impact: 121.8 | O(N^6))
  * `getFamilyMap` (Impact: 121.6 | O(2^N))
  * `getScrollData` (Impact: 95.9 | O(N^6) | DB: 1)
  * `getPageData` (Impact: 94.6 | O(N^6) | DB: 1)
    * *Intent:* // ===================================================================================== // scan 操作封...
  * `toEntity` (Impact: 67.5 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 289`, `args: 92`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 72`, `duplicate_logic: 47`
* *Architecture:* `io: 5`, `api: 59`, `concurrency: 4`, `import: 51`
* *Defense:* `safety: 22`, `doc: 67`, `sync_locks: 4`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.479
  * `Choke Point (Betweenness):` 0.000467 | `Ripple Effect (Closeness):` 0.011511
  * `Imports (Out-Degree: 9):` io.github.dunwu.javadb.hbase.entity.common.FamilyDo, org.apache.hadoop.hbase.client.Result, org.apache.hadoop.hbase.client.Durability, cn.hutool.core.date.DateUtil, java.util.Date, org.apache.hadoop.hbase.client.ConnectionFactory, java.util.Map, io.github.dunwu.javadb.hbase.entity.common.RowDo...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.059 IQR)
- **Top Global Matches:** file_cluster_8: 11.059, file_cluster_13: 11.241, file_cluster_16: 11.252
- **Magnitude:** 1529.24 | **LOC:** 732 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (24.0449%), Tech Debt (73.4502%)
**Top Internal Functions/Classes:**
  * `testIpLookup` (Impact: 163.1 | O(2^N) | DB: 12)
  * `run` (Impact: 135.7 | O(N^6))
  * `testCounters` (Impact: 109.2 | O(2^N))
  * `testLogCommon` (Impact: 101.4 | O(2^N))
  * `importIpsToRedis` (Impact: 99.1 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 118`, `args: 45`, `func_start: 66`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 43`, `duplicate_logic: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 55`, `concurrency: 6`, `import: 10`
* *Defense:* `safety: 24`, `doc: 4`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` redis.clients.jedis.*, com.google.gson.Gson, java.util.*, java.io.File, org.apache.commons.csv.CSVParser, java.io.FileReader, java.text.SimpleDateFormat, org.apache.commons.csv.CSVFormat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter08.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.373 IQR)
- **Top Global Matches:** file_cluster_8: 12.373, file_cluster_0: 12.464, file_cluster_13: 12.553
- **Magnitude:** 1285.12 | **LOC:** 537 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (37.68%), Tech Debt (99.092%)
**Top Internal Functions/Classes:**
  * `cleanTimelines` (Impact: 185.3 | O(2^N))
  * `refillTimeline` (Impact: 176.5 | O(2^N) | DB: 2)
  * `syndicateStatus` (Impact: 148.2 | O(2^N) | DB: 1)
  * `testFollowUnfollowUser` (Impact: 115.4 | O(2^N))
  * `testRefillTimeline` (Impact: 73.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 70`, `args: 57`, `func_start: 71`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 50`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 28`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 65`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.*, java.lang.reflect.Method, redis.clients.jedis.Transaction, redis.clients.jedis.Pipeline, redis.clients.jedis.Tuple, redis.clients.jedis.Jedis
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter02.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.604 IQR)
- **Top Global Matches:** file_cluster_8: 11.604, file_cluster_4: 11.758, file_cluster_13: 11.793
- **Magnitude:** 1037.18 | **LOC:** 503 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (37.1426%), Tech Debt (94.2722%)
**Top Internal Functions/Classes:**
  * `testShopppingCartCookies` (Impact: 126.9 | O(2^N))
  * `run` (Impact: 120.8 | O(N^6) | DB: 1)
    * *Intent:* /** * 代码清单 2-8 数据行缓存-定时更新数据行缓存 */
  * `testCacheRows` (Impact: 118.5 | O(2^N))
  * `testLoginCookies` (Impact: 117.8 | O(2^N))
  * `run` (Impact: 99.4 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 73`, `args: 35`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 31`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 37`, `concurrency: 24`, `import: 5`
* *Defense:* `safety: 21`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.net.URL, com.google.gson.Gson, java.util.*, redis.clients.jedis.Tuple, redis.clients.jedis.Jedis, java.net.MalformedURLException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.882 IQR)
- **Top Global Matches:** file_cluster_13: 10.882, file_cluster_16: 11.231, file_cluster_8: 11.269
- **Magnitude:** 963.18 | **LOC:** 702 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (19.5481%), Tech Debt (86.0301%)
**Top Internal Functions/Classes:**
  * `pojoListByIds` (Impact: 68.7 | O(N^5) | DB: 2)
  * `updateById` (Impact: 65.6 | O(2^N))
  * `save` (Impact: 65.5 | O(2^N))
  * `deleteBatchIds` (Impact: 65.2 | O(2^N) | DB: 2)
  * `saveBatch` (Impact: 49.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 235`, `args: 53`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 57`, `duplicate_logic: 10`
* *Architecture:* `api: 58`, `concurrency: 7`, `import: 72`
* *Defense:* `safety: 2`, `doc: 6`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.191
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 4):` org.elasticsearch.client.GetAliasesResponse, io.github.dunwu.javadb.elasticsearch.util.JsonUtil, org.elasticsearch.action.search.SearchResponse, java.util.Map, org.elasticsearch.action.search.SearchScrollRequest, org.elasticsearch.ElasticsearchException, org.elasticsearch.action.index.IndexResponse, org.elasticsearch.search.SearchHits...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank/RankDemo.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.515 IQR)
- **Top Global Matches:** file_cluster_16: 11.515, file_cluster_8: 11.531, file_cluster_13: 11.622
- **Magnitude:** 860.46 | **LOC:** 668 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.7031%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRankByMemberWithRegions` (Impact: 158.5 | O(2^N) | DB: 3)
  * `parseZsetTuples` (Impact: 80.1 | O(N^6) | DB: 3)
  * `deleteWithAutoAdjust` (Impact: 67.2 | O(N^4) | DB: 3)
  * `saveRankWithRegions` (Impact: 65.1 | O(N^5) | DB: 3)
  * `getRankElementListWithRegions` (Impact: 62.2 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 72`, `args: 29`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 56`, `orphaned_logic: 5`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `doc: 65`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.*, cn.hutool.core.bean.BeanUtil, cn.hutool.core.collection.CollectionUtil, redis.clients.jedis.Pipeline, lombok.extern.slf4j.Slf4j, redis.clients.jedis.Response, redis.clients.jedis.Tuple, redis.clients.jedis.Jedis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.379 IQR)
- **Top Global Matches:** file_cluster_8: 11.379, file_cluster_13: 11.502, file_cluster_0: 11.576
- **Magnitude:** 834.7 | **LOC:** 458 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (28.8874%), Tech Debt (67.7705%)
**Top Internal Functions/Classes:**
  * `testUserLocation` (Impact: 189.8 | O(2^N) | DB: 2)
  * `testShardKey` (Impact: 56.9 | O(2^N))
  * `getExpected` (Impact: 55.3 | O(N^5) | DB: 2)
  * `testUniqueVisitors` (Impact: 54.6 | O(2^N) | DB: 1)
  * `isDigit` (Impact: 45.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 70`, `args: 28`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 50`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 28`, `import: 8`
* *Defense:* `safety: 19`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` redis.clients.jedis.ZParams, java.util.zip.CRC32, java.util.*, java.io.InputStream, redis.clients.jedis.Pipeline, java.text.SimpleDateFormat, java.io.IOException, redis.clients.jedis.Jedis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch08_listing_source.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.392 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.732 IQR)
- **Top Global Matches:** file_cluster_8: 9.392, file_cluster_13: 9.807, file_cluster_7: 9.937
- **Magnitude:** 727.7 | **LOC:** 1052 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.3617%), Tech Debt (36.3468%)
**Top Internal Functions/Classes:**
  * `syndicate_status` (Impact: 302.7 | O(2^N) | DB: 3)
    * *Intent:* # 以上次被更新的最后一个关注者为起点，获取接下来的一千个关注者。 followers = conn.zrangebyscore('followers:%s' % uid, start, 'inf',...
  * `create_status` (Impact: 151.6 | O(2^N) | DB: 6)
    * *Intent:* # 代码清单 8-13 # <start id="create-message-streaming"/>
  * `refill_timeline` (Impact: 74.5 | O(2^N) | DB: 1)
  * `get_config` (Impact: 40.2 | O(2^N))
  * `create_status` (Impact: 21.2 | O(N^2) | DB: 1)
    * *Intent:* # <end id="create-twitter-user"/> # 代码清单 8-2 # <start id="create-twitter-status"/>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 126`, `args: 45`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 24`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 47`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 5`, `doc: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` threading, urlparse, redis, math, time, json, SocketServer, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper/UserEsMapperTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.525 IQR)
- **Top Global Matches:** file_cluster_8: 9.525, file_cluster_0: 9.653, file_cluster_13: 9.779
- **Magnitude:** 707.96 | **LOC:** 473 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.5936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pojoPageByLastId` (Impact: 109.8 | O(2^N))
  * `pojoPageByLastIdInDay` (Impact: 109.8 | O(2^N))
  * `pojoScroll` (Impact: 85.9 | O(2^N))
  * `pojoScrollInDay` (Impact: 43.9 | O(N^5))
  * `query` (Impact: 30.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 80`, `args: 30`, `func_start: 22`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 23`, `import: 24`
* *Defense:* `doc: 1`, `test: 52`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.assertj.core.api.Assertions, org.springframework.beans.factory.annotation.Autowired, io.github.dunwu.javadb.elasticsearch.BaseApplicationTests, io.github.dunwu.javadb.elasticsearch.util.JsonUtil, org.elasticsearch.action.search.SearchResponse, java.util.Map, org.elasticsearch.search.builder.SearchSourceBuilder, org.elasticsearch.index.query.BoolQueryBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.463 IQR)
- **Top Global Matches:** file_cluster_13: 9.463, file_cluster_8: 9.464, file_cluster_16: 9.753
- **Magnitude:** 518.18 | **LOC:** 296 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.8717%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteIndex` (Impact: 96.8 | O(2^N))
  * `pojoScroll` (Impact: 92.0 | O(2^N))
  * `pojoPageByLastId` (Impact: 46.9 | O(N^4))
  * `onResponse` (Impact: 39.5 | O(N^4))
  * `saveBatch` (Impact: 32.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 70`, `args: 29`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 28`, `import: 23`
* *Defense:* `safety: 2`, `doc: 1`, `test: 23`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.assertj.core.api.Assertions, io.github.dunwu.javadb.elasticsearch.util.JsonUtil, org.elasticsearch.action.search.SearchResponse, java.util.Map, org.elasticsearch.ElasticsearchException, org.elasticsearch.action.get.GetResponse, org.elasticsearch.search.builder.SearchSourceBuilder, org.elasticsearch.index.query.BoolQueryBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch10_listing_source.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.786 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.805 IQR)
- **Top Global Matches:** file_cluster_8: 9.786, file_cluster_13: 10.176, file_cluster_0: 10.414
- **Magnitude:** 506.14 | **LOC:** 839 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (13.9245%), Tech Debt (24.0224%)
**Top Internal Functions/Classes:**
  * `search_shards_zset` (Impact: 160.5 | O(N^4) | DB: 8)
    * *Intent:* # <end id="zset-search-with-values"/> # 代码清单 10-9 # <start id="search-shards-zset"/> # 函数需要接受所有分片参数以...
  * `shard_key` (Impact: 54.1 | O(2^N))
  * `get_config` (Impact: 38.3 | O(2^N))
  * `test_sharded_search` (Impact: 28.4 | O(N^1))
  * `get_shard_results_thread` (Impact: 24.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 107`, `args: 49`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 29`, `orphaned_logic: 6`
* *Architecture:* `api: 45`, `concurrency: 3`, `import: 12`
* *Defense:* `safety: 7`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` threading, collections, Queue, time, binascii, decimal, datetime, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter04.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.306 IQR)
- **Top Global Matches:** file_cluster_13: 11.306, file_cluster_8: 11.336, file_cluster_0: 11.641
- **Magnitude:** 499.34 | **LOC:** 211 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (40.0075%), Tech Debt (12.6195%)
**Top Internal Functions/Classes:**
  * `testPurchaseItem` (Impact: 162.8 | O(2^N))
  * `testListItem` (Impact: 84.6 | O(2^N) | DB: 1)
  * `purchaseItem` (Impact: 69.1 | O(N^4) | DB: 1)
  * `listItem` (Impact: 40.4 | O(N^4) | DB: 1)
  * `benchmarkUpdateToken` (Impact: 32.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`, `args: 11`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 21`, `orphaned_logic: 1`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Map, java.util.List, java.lang.reflect.Method, redis.clients.jedis.Transaction, redis.clients.jedis.Pipeline, redis.clients.jedis.Tuple, redis.clients.jedis.Jedis, java.util.Set
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseDynamicEsMapper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.381 IQR)
- **Top Global Matches:** file_cluster_13: 11.381, file_cluster_8: 11.431, file_cluster_16: 11.72
- **Magnitude:** 486.7 | **LOC:** 332 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.7963%), Tech Debt (99.8841%)
**Top Internal Functions/Classes:**
  * `updateAliasInDay` (Impact: 31.8 | O(N^3))
  * `getIndex` (Impact: 29.0 | O(N^4))
  * `asyncSaveBatchInDay` (Impact: 28.7 | O(N^3))
  * `asyncUpdateBatchIdsInDay` (Impact: 28.6 | O(N^3))
  * `saveInDay` (Impact: 25.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 75`, `args: 26`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `duplicate_logic: 4`, `orphaned_logic: 15`
* *Architecture:* `api: 25`, `import: 23`
* *Defense:* `safety: 36`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.elasticsearch.action.search.SearchResponse, cn.hutool.core.date.DateUtil, org.elasticsearch.action.get.GetResponse, org.elasticsearch.search.builder.SearchSourceBuilder, cn.hutool.core.date.DateTime, org.elasticsearch.action.ActionListener, java.util.ArrayList, cn.hutool.core.date.DatePattern...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch06_listing_source.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.669 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.669 IQR)
- **Top Global Matches:** file_cluster_8: 9.669, file_cluster_13: 10.108, file_cluster_7: 10.263
- **Magnitude:** 469.28 | **LOC:** 1128 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (12.7704%), Tech Debt (54.8957%)
**Top Internal Functions/Classes:**
  * `test_add_update_contact` (Impact: 44.1 | O(N^1) | DB: 1)
  * `test_file_distribution` (Impact: 33.9 | O(N^2) | DB: 9)
  * `copy_logs_to_redis` (Impact: 31.4 | O(N^1) | DB: 14)
    * *Intent:* # <end id="_1314_15044_3669"/> # 代码清单 6-30 # <start id="_1314_14473_9209"/>
  * `readblocks_gz` (Impact: 24.7 | O(N^1))
    * *Intent:* # <end id="_1314_14473_9225"/> # 代码清单 6-34 # <start id="_1314_14473_9229"/>
  * `process_logs_from_redis` (Impact: 19.6 | O(N^1))
    * *Intent:* # <end id="_1314_14473_9209"/> # 代码清单 6-31 # <start id="_1314_14473_9213"/>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 122`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `orphaned_logic: 17`
* *Architecture:* `io: 7`, `api: 47`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 18`, `test: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` threading, collections, pprint, math, gzip, time, zlib, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch07_listing_source.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.0 IQR)
- **Top Global Matches:** file_cluster_8: 9.841, file_cluster_7: 10.433, file_cluster_13: 10.448
- **Magnitude:** 419.18 | **LOC:** 922 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.1099%), Tech Debt (12.2113%)
**Top Internal Functions/Classes:**
  * `record_click` (Impact: 66.9 | O(N^1) | DB: 1)
    * *Intent:* # <end id="record_targeting"/> # 代码清单 7-15 # <start id="record_click"/> def record_click(conn, targe...
  * `search_job_years` (Impact: 46.9 | O(N^3) | DB: 2)
  * `parse` (Impact: 22.9 | O(N^1) | DB: 2)
    * *Intent:* # <end id="_1314_14473_9158"/> # 代码清单 7-3 # <start id="parse-query"/> # 查找需要的单词、不需要的单词以及同义词的正则表达式。 Q...
  * `search_and_zsort` (Impact: 20.8 | O(N^1))
    * *Intent:* # 代码清单 7-6 # <start id="zset_scored_composite"/> # 和之前一样，函数接受一个已有搜索结果的 ID 作为可选参数， # 以便在结果仍然可用的情况下，对其...
  * `search_and_sort` (Impact: 18.6 | O(N^2))
    * *Intent:* # <end id="search-query"/> # 代码清单 7-5 # <start id="sorted-searches"/> # 用户可以通过可选的参数来传入已有的搜索结果、指定搜索结果...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 108`, `args: 49`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 37`, `orphaned_logic: 2`
* *Architecture:* `api: 45`, `import: 5`
* *Defense:* `safety: 2`, `doc: 2`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math, re, unittest, redis, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseAdmin.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.74 IQR)
- **Top Global Matches:** file_cluster_13: 10.74, file_cluster_8: 11.174, file_cluster_7: 11.371
- **Magnitude:** 340.38 | **LOC:** 295 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (6.7579%), Tech Debt (99.9876%)
**Top Internal Functions/Classes:**
  * `createTable` (Impact: 41.0 | O(2^N) | DB: 2)
  * `dropNamespace` (Impact: 32.0 | O(N^5))
    * *Intent:* /** * 创建命名空间 *
  * `createNamespace` (Impact: 27.3 | O(2^N))
  * `listTableNamesByNamespace` (Impact: 27.3 | O(2^N))
  * `listNamespaces` (Impact: 24.4 | O(2^N))
    * *Intent:* /** * 删除命名空间 * * @param namespace 命名空间 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 67`, `args: 24`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 6`, `duplicate_logic: 8`
* *Architecture:* `io: 5`, `api: 23`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 10`, `doc: 36`, `sync_locks: 3`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003597
  * `Imports (Out-Degree: 0):` org.apache.hadoop.hbase.client.ColumnFamilyDescriptorBuilder, org.apache.hadoop.hbase.client.Table, org.apache.hadoop.hbase.NamespaceDescriptor, java.util.List, org.apache.hadoop.hbase.client.Admin, org.apache.hadoop.hbase.client.ConnectionFactory, org.apache.hadoop.security.UserGroupInformation, org.apache.hadoop.hbase.client.TableDescriptorBuilder...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/HbaseTemplateScanTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.083 IQR)
- **Top Global Matches:** file_cluster_13: 12.083, file_cluster_0: 12.197, file_cluster_11: 12.381
- **Magnitude:** 319.52 | **LOC:** 243 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (72.4761%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clear` (Impact: 71.3 | O(N^4) | DB: 7)
  * `test04` (Impact: 31.2 | O(N^4) | DB: 6)
  * `test05` (Impact: 31.2 | O(N^4) | DB: 8)
  * `test06` (Impact: 31.1 | O(N^4) | DB: 6)
  * `test02` (Impact: 17.1 | O(N^3) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 59`, `args: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 79`, `orphaned_logic: 8`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 2`, `doc: 1`, `test: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.assertj.core.api.Assertions, java.util.Map, io.github.dunwu.javadb.hbase.entity.common.RowDo, io.github.dunwu.javadb.hbase.entity.common.ScrollData, cn.hutool.core.util.RandomUtil, java.math.BigDecimal, org.junit.jupiter.api.Test, io.github.dunwu.javadb.hbase.entity.scan.SingleFamilyScan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/BaseHbaseMapper.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.421 IQR)
- **Top Global Matches:** file_cluster_13: 10.421, file_cluster_0: 10.438, file_cluster_8: 10.782
- **Magnitude:** 318.24 | **LOC:** 195 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.7675%), Tech Debt (66.479%)
**Top Internal Functions/Classes:**
  * `getIdStrList` (Impact: 37.3 | O(N^3))
  * `deleteById` (Impact: 36.5 | O(2^N))
  * `batchSave` (Impact: 36.5 | O(2^N))
  * `getOneById` (Impact: 36.5 | O(2^N))
  * `getMapByIds` (Impact: 30.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 63`, `args: 16`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 20`, `import: 17`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.369
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.003597
  * `Imports (Out-Degree: 3):` java.io.Serializable, java.util.List, java.util.Map, lombok.RequiredArgsConstructor, cn.hutool.core.util.StrUtil, cn.hutool.core.collection.CollectionUtil, io.github.dunwu.javadb.hbase.entity.common.ScrollData, lombok.extern.slf4j.Slf4j...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action-py/ch05_listing_source.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.541 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.102 IQR)
- **Top Global Matches:** file_cluster_8: 9.541, file_cluster_13: 9.75, file_cluster_7: 10.145
- **Magnitude:** 296.8 | **LOC:** 756 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (12.0729%), Tech Debt (70.5181%)
**Top Internal Functions/Classes:**
  * `update_stats` (Impact: 32.5 | O(N^3))
    * *Intent:* # <end id="clean_counters"/> # 代码清单 5-6 # <start id="update_stats"/> # 设置用于存储统计数据的键。 destination = '...
  * `log_recent` (Impact: 32.3 | O(2^N))
    * *Intent:* # 尝试将日志的级别转换成简单的字符串。 severity = str(SEVERITY.get(severity, severity)).lower() # 创建负责存储消息的键。 destinat...
  * `test_log_recent` (Impact: 25.9 | O(N^1) | DB: 1)
  * `clean_counters` (Impact: 22.7 | O(N^1))
    * *Intent:* # <end id="get_counter"/> # <start id="clean_counters"/>
  * `import_ips_to_redis` (Impact: 16.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 95`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 15`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 6`, `api: 36`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 9`, `doc: 2`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` threading, pprint, csv, time, contextlib, datetime, json, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.81 IQR)
- **Top Global Matches:** file_cluster_13: 9.81, file_cluster_8: 10.161, file_cluster_16: 10.3
- **Magnitude:** 294.38 | **LOC:** 174 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (23.361%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getDefaultEsAddress` (Impact: 111.0 | O(N^4))
  * `toHttpHostList` (Impact: 25.0 | O(N^3))
  * `newRestClient` (Impact: 20.2 | O(N^3) | DB: 3)
  * `newRestHighLevelClient` (Impact: 20.2 | O(N^3))
  * `getRestClientBuilder` (Impact: 10.7 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 46`, `args: 25`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 7`, `duplicate_logic: 12`
* *Architecture:* `io: 5`, `api: 19`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003597
  * `Imports (Out-Degree: 0):` java.util.List, org.elasticsearch.client.RestClientBuilder, org.apache.http.HttpHost, org.elasticsearch.client.RestHighLevelClient, cn.hutool.core.util.StrUtil, cn.hutool.core.collection.CollectionUtil, cn.hutool.core.util.ArrayUtil, org.elasticsearch.client.RestClient...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action-py/ch11_listing_source.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.249 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.982 IQR)
- **Top Global Matches:** file_cluster_8: 10.249, file_cluster_13: 10.571, file_cluster_7: 10.617
- **Magnitude:** 292.56 | **LOC:** 799 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (10.9354%), Tech Debt (99.9992%)
**Top Internal Functions/Classes:**
  * `sharded_bpop_helper` (Impact: 41.1 | O(N^3))
  * `create_status` (Impact: 15.9 | O(2^N) | DB: 3)
    * *Intent:* # <end id="show-script-load"/> # 代码清单 11-2 # <start id="ch08-post-status"/> def create_status(conn, ...
  * `autocomplete_on_prefix` (Impact: 15.6 | O(N^4))
  * `purchase_item_with_lock` (Impact: 14.9 | O(N^1))
  * `autocomplete_on_prefix` (Impact: 11.6 | O(N^1))
    * *Intent:* # 把所有必须的参数传递给 Lua 函数，实际地执行信号量获取操作。
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 87`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 20`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 11`
* *Architecture:* `api: 38`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 9`, `doc: 26`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` threading, math, time, unittest, bisect, redis, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter01.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.736 IQR)
- **Top Global Matches:** file_cluster_16: 11.736, file_cluster_8: 11.895, file_cluster_13: 11.941
- **Magnitude:** 283.16 | **LOC:** 186 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (36.9548%), Tech Debt (99.9279%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 57.5 | O(N^3))
  * `printArticles` (Impact: 47.3 | O(N^5))
  * `addRemoveGroups` (Impact: 36.4 | O(N^3) | DB: 1)
  * `articleVote` (Impact: 29.1 | O(N^3) | DB: 1)
  * `postArticle` (Impact: 21.5 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 27`, `args: 10`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` redis.clients.jedis.ZParams, java.util.*, redis.clients.jedis.Jedis
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `codes/javadb/redis/src/main/java/io/github/dunwu/javadb/redis/springboot/data/UserServiceImpl.java` (JAVA) | Magnitude: 18.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, api: 6, args: 3
- `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/OrderMapper.java` (JAVA) | Magnitude: 17.78 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, func_start: 5, api: 5
- `codes/javadb/mongodb/src/main/java/io/github/dunwu/javadb/mongodb/springboot/SpringBootDataMongodbApplication.java` (JAVA) | Magnitude: 10.68 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 8, import: 6, decorators: 4
- `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank/RankDemoTests.java` (JAVA) | Magnitude: 119.0 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 27, decorators: 17, test: 14
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` (JAVA) | Magnitude: 1600.4 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 408, branch: 146, structural_boundaries: 113, func_start: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java` (JAVA) | Magnitude: 518.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 222, structural_boundaries: 70, branch: 46, args: 29
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/elasticsearch/QueryDocument.java` (JAVA) | Magnitude: 5.92 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, decorators: 7, branch: 5
- `codes/javadb/mysql/src/main/java/io/github/dunwu/javadb/mysql/springboot/UserDao.java` (JAVA) | Magnitude: 43.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 11, args: 11, func_start: 11, indent_spaces: 11
- `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/UserElasticsearchTemplateTest.java` (JAVA) | Magnitude: 68.96 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 35, decorators: 18, api: 14
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/BaseHbaseMapper.java` (JAVA) | Magnitude: 318.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 63, branch: 35, api: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/CommonUkMapper.java` (JAVA) | Magnitude: 29.1 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, doc: 15, args: 9
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/repositories/BookRepository.java` (JAVA) | Magnitude: 26.2 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, generics: 4, import: 4, args: 3
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/repositories/ProductRepository.java` (JAVA) | Magnitude: 26.2 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, generics: 4, import: 4, args: 3
- `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank/RankDemo.java` (JAVA) | Magnitude: 860.46 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 355, branch: 103, structural_boundaries: 72, doc: 65
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/CommonMapper.java` (JAVA) | Magnitude: 36.08 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, doc: 19, structural_boundaries: 14, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/deploy.sh` (SHELL) | Magnitude: 3.18 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 21, reflection_metaprogramming: 10, indent_spaces: 10, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `codes/redis/redis-config/sentinel3/linux/server-6380/start.sh` (SHELL) | Magnitude: 15.52 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, safety_bypasses: 2, state_mutation: 2, orphaned_logic: 1
- `codes/redis/redis-config/sentinel3/linux/server-6381/start.sh` (SHELL) | Magnitude: 15.52 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, safety_bypasses: 2, state_mutation: 2, orphaned_logic: 1
- `codes/redis/redis-config/sentinel3/linux/server-6382/start.sh` (SHELL) | Magnitude: 15.52 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, safety_bypasses: 2, state_mutation: 2, orphaned_logic: 1
- `codes/redis/redis-config/sentinel3/osx/server-6380/start.sh` (SHELL) | Magnitude: 15.52 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, safety_bypasses: 2, state_mutation: 2, orphaned_logic: 1
- `codes/redis/redis-config/sentinel3/osx/server-6381/start.sh` (SHELL) | Magnitude: 15.52 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 12, safety_bypasses: 2, state_mutation: 2, orphaned_logic: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `codes/redis/redis-in-action-py/chA_listing_source.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java` (JAVA) | Magnitude: 1888.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 773, branch: 257, state_mutation: 166, structural_boundaries: 145
- `codes/javadb/h2/src/test/java/io/github/dunwu/javadb/h2/H2JdbcTest.java` (JAVA) | Magnitude: 42.14 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, branch: 13, structural_boundaries: 11, encapsulation: 8
- `codes/javadb/sqlite/src/main/java/io/github/dunwu/javadb/sqlite/springboot/SqliteDemo.java` (JAVA) | Magnitude: 249.6 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 133, branch: 31, sec_high_risk_execution: 18, io: 16
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/aggregation/OrderRepositoryIntegrationTests.java` (JAVA) | Magnitude: 28.48 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 42, func_start: 12, test: 11
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/aggregation/SpringBooksIntegrationTests.java` (JAVA) | Magnitude: 87.94 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 235, func_start: 59, structural_boundaries: 51, test: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `codes/javadb/redis/src/main/java/io/github/dunwu/javadb/redis/springboot/data/UserService.java` (JAVA) | Magnitude: 21.92 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, doc: 2
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, ownership: 1
- `codes/javadb/mongodb/src/main/java/io/github/dunwu/javadb/mongodb/springboot/querybyexample/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, ownership: 1
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/elasticsearch/ElasticSearchUtil.java` (JAVA) | Magnitude: 10.52 | Delta: **0.318 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 84, doc: 6, ownership: 1, sec_high_risk_execution: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` -> **Severity: 0.037** (Bridge: 0.0005 * Flux: 79.197%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 80.7554%)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/BaseHbaseMapper.java` -> **Severity: 0.002** (Bridge: 0.0002 * Flux: 14.6408%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/util/JsonUtil.java` -> **Severity: 1.282** (Embedded: 0.016 * Error Risk: 80.0%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **Severity: 1.252** (Embedded: 0.0144 * Error Risk: 87.0024%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/common/ScrollData.java` -> **Severity: 1.224** (Embedded: 0.023 * Error Risk: 53.1537%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/common/PageData.java` -> **Severity: 1.214** (Embedded: 0.023 * Error Risk: 52.7246%)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/annotation/RowKeyUtil.java` -> **Severity: 1.149** (Embedded: 0.0189 * Error Risk: 60.7392%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/annotation/RowKeyUtil.java` -> **Severity: 2031.68** (Blast Radius: 20.322 * Doc Risk: 99.9744%)
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities/User.java` -> **Severity: 1055.455** (Blast Radius: 11.166 * Doc Risk: 94.524%)
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities/Product.java` -> **Severity: 811.255** (Blast Radius: 9.069 * Doc Risk: 89.4536%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/User.java` -> **Severity: 685.056** (Blast Radius: 7.096 * Doc Risk: 96.5411%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/constant/ResultCode.java` -> **Severity: 654.097** (Blast Radius: 6.541 * Doc Risk: 99.9995%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
