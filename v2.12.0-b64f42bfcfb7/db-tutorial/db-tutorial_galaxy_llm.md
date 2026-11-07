# ARCHITECTURAL_BRIEF: db-tutorial
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dunwu/db-tutorial.git` |
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
- **Scope:** 315 analyzed artifact(s), 18605 LOC.
- **Load-bearing artifact:** `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/BaseHbaseEntity.java` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 73 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `codes/redis/redis-in-action-py/ch07_listing_source.py` at magnitude 781.78 (structural weight, not risk).
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
| Total Artifacts | 472 |
| Analyzed Artifacts (Scanned) | 315 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 157 |
| Total LOC | 18605 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.7% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8233 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2056 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.551 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 29 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 176 | 12693 | 55.9% |
| SQLITE | 38 | 1136 | 12.1% |
| XML | 22 | 0 | 7.0% |
| SHELL | 18 | 207 | 5.7% |
| PLAINTEXT | 16 | 0 | 5.1% |
| BATCH | 16 | 126 | 5.1% |
| PYTHON | 12 | 3798 | 3.8% |
| MARKDOWN | 7 | 0 | 2.2% |
| JAVASCRIPT | 4 | 136 | 1.3% |
| JSON | 3 | 389 | 1.0% |
| YAML | 3 | 120 | 1.0% |

## 4.1 SOURCE ENCODINGS
All 315 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Declarative / Non-Code 29%, Large Core Modules (3) 9%, State Mutators Files 9%, Generic / Templated Code Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 292 | 92.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 23 | 7.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 157*

**Composition by Extension & Reason:**
- `.md`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 30x Excluded (Unsupported Extension: '.conf')
- `.rdb`: 12x Excluded (Unsupported Extension: '.rdb')
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 1x Excluded (Massive Static Asset Blob: 7607 LOC), 1x Excluded (Massive Static Asset Blob: 3601 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.styl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pdf`: 1x Excluded (Explicitly Denied Extension: '.pdf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 84.8 | 7.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.2 | 28.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 73.7 | 7.8 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 34.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 254 | 34 | 1 | `codes/redis/redis-in-action-py/ch07_listing_source.py` |
| cleanup | 56 | 23 | 0 | `codes/javadb/sqlite/src/main/java/io/github/dunwu/javadb/sqlite/springboot/SqliteDemo.java` |
| guards | 1239 | 151 | 9 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java` |
| danger | 812 | 100 | 6 | `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` |
| concurrency | 221 | 31 | 0 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` |
| connectivity | 1460 | 181 | 11 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java` |
| io | 136 | 24 | 0 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 197 | 23 | 0 | `codes/redis/redis-in-action-py/ch05_listing_source.py` |
| serialization | 25 | 6 | 0 | `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/util/JsonUtil.java` |
| regex | 20 | 8 | 0 | `codes/mysql/SQL必知必会示例/select.sql` |
| events | 268 | 42 | 1 | `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` |
| tests | 516 | 42 | 4 | `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/HbaseTemplateGetTest.java` |
| docs | 449 | 154 | 4 | `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank/RankDemo.java` |
| debt | 337 | 35 | 1 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` |
| mutation | 5206 | 172 | 33 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java` |
| dead_code | 650 | 102 | 7 | `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/elasticsearch/ElasticSearchUtil.java` |
| credential | 1 | 1 | 0 | `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/constant/ResultCode.java` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 43 | 11 | 0 | `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` (Hits: 22)
- `codes/javadb/sqlite/src/main/java/io/github/dunwu/javadb/sqlite/springboot/SqliteDemo.java` (Hits: 16)
- `utils/modules/readFileList.js` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **BaseHbaseEntity.java** (`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/entity/BaseHbaseEntity.java`) — 9 inbound connections
2. **SortedSetDemo.java** (`codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/SortedSetDemo.java`) — 8 inbound connections
3. **ElasticsearchTemplate.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java`) — 6 inbound connections
4. **PageData.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/common/PageData.java`) — 6 inbound connections
5. **ScrollData.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/entity/common/ScrollData.java`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 73 outbound dependencies
2. **ElasticsearchTemplate.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java`) — 72 outbound dependencies
3. **HbaseTemplate.java** (`codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java`) — 51 outbound dependencies
4. **BaseEsMapper.java** (`codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java`) — 28 outbound dependencies
5. **RestHighLevelClientDocumentApiTest.java** (`codes/javadb/elasticsearch/elasticsearch7/src/test/java/io/github/dunwu/javadb/elasticsearch/springboot/RestHighLevelClientDocumentApiTest.java`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `update_cpms` **(Compute Cores)** (@ `codes/redis/redis-in-action-py/ch07_listing_source.py`) -> Impact: **29.1** | LOC: 62
  * *Intent:* # <end id="record_click"/> # 代码清单 7-16 # <start id="update_cpms"/>
- `copy_logs_to_redis` **(Many-Argument Workhorses)** (@ `codes/redis/redis-in-action-py/ch06_listing_source.py`) -> Impact: **28.7** | LOC: 45
  * *Intent:* # <end id="_1314_15044_3669"/> # 代码清单 6-30 # <start id="_1314_14473_9209"/>
- `updateCpms` **(Type Conversions)** (@ `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java`) -> Impact: **28.0** | LOC: 76
- `newPut` **(Many-Argument Workhorses)** (@ `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java`) -> Impact: **23.8** | LOC: 36
- `readblocks_gz` **(Compute Cores)** (@ `codes/redis/redis-in-action-py/ch06_listing_source.py`) -> Impact: **22.9** | LOC: 43
  * *Intent:* # <end id="_1314_14473_9225"/> # 代码清单 6-34 # <start id="_1314_14473_9229"/>
- `filter_content` **(Many-Argument Workhorses)** (@ `codes/redis/redis-in-action-py/ch08_listing_source.py`) -> Impact: **22.8** | LOC: 32
  * *Intent:* # <end id="delete-message-streaming"/> # 代码清单 8-15 # <start id="message-subscription"/> # 使用第 5 章介绍的自动连接装饰器。 # 创建一个过滤器，让它来判断是否应该将消息发送给客户端。 match = cre...
- `sharded_bpop_helper` **(Many-Argument Workhorses)** (@ `codes/redis/redis-in-action-py/ch11_listing_source.py`) -> Impact: **21.3** | LOC: 31
  * *Intent:* # 定义一个辅助函数， # 这个函数会为左端阻塞弹出操作以及右端阻塞弹出操作执行实际的弹出动作。 # 准备好流水线对象和超时信息。 pipe = conn.pipeline(False) timeout = max(timeout, 0) or 2 ** 64 end = time.time() +...
- `get_shard_results_thread` **(Many-Argument Workhorses)** (@ `codes/redis/redis-in-action-py/ch10_listing_source.py`) -> Impact: **21.2** | LOC: 27
- `search_and_zsort` **(Many-Argument Workhorses)** (@ `codes/redis/redis-in-action-py/ch07_listing_source.py`) -> Impact: **20.8** | LOC: 36
  * *Intent:* # <end id="sorted-searches"/> # 代码清单 7-6 # <start id="zset_scored_composite"/> # 和之前一样，函数接受一个已有搜索结果的 ID 作为可选参数， # 以便在结果仍然可用的情况下，对其进行分页。
- `search_and_zsort` **(Many-Argument Workhorses)** (@ `codes/redis/redis-in-action-py/ch10_listing_source.py`) -> Impact: **20.2** | LOC: 25

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `codes/redis/redis-in-action-py` | 13 | 5160.88 | 49.65% | 60.09% |
| `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis` | 10 | 2556.96 | 32.63% | 33.34% |
| `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase` | 3 | 595.42 | 8.98% | 0.0% |
| `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch` | 2 | 435.96 | 15.36% | 0.0% |
| `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank` | 5 | 370.92 | 7.16% | 0.0% |
| `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper` | 4 | 352.76 | 4.89% | 95.28% |
| `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase` | 7 | 269.1 | 8.35% | 0.0% |
| `codes/mysql/SQL必知必会示例` | 4 | 230.96 | 2.63% | 0.0% |
| `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities` | 13 | 222.48 | 6.03% | 7.69% |
| `codes/mysql/Leetcode之SQL题/easy` | 12 | 186.82 | 4.93% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/EsMapper.java` -> **100.0%** Exposure
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/HbaseMapper.java` -> **100.0%** Exposure
- `codes/javadb/mysql/src/main/java/io/github/dunwu/javadb/mysql/springboot/UserDao.java` -> **100.0%** Exposure
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities/ArticleBuilder.java` -> **99.999%** Exposure
- `codes/javadb/redis/src/main/java/io/github/dunwu/javadb/redis/springboot/SpringBootDataRedisApplication.java` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/textsearch/util/ConsoleResultPrinter.java` -> **100.0%** Exposure
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java` -> **100.0%** Exposure
- `codes/redis/redis-in-action-py/ch01_listing_source.py` -> **100.0%** Exposure
- `codes/redis/redis-in-action-py/ch02_listing_source.py` -> **100.0%** Exposure
- `codes/redis/redis-in-action-py/ch03_listing_source.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/EsMapper.java` -> **27** Orphaned Functions | **0** Duplicates
- `codes/redis/redis-in-action-py/ch06_listing_source.py` -> **23** Orphaned Functions | **0** Duplicates
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` -> **20** Orphaned Functions | **0** Duplicates
- `codes/redis/redis-in-action-py/ch07_listing_source.py` -> **16** Orphaned Functions | **0** Duplicates
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseDynamicEsMapper.java` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1499` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `codes/redis/redis-in-action-py/ch07_listing_source.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.372)
- **Top Global Matches:** file_cluster_12: 6.372, file_cluster_15: 7.857, file_cluster_16: 9.115
- **Magnitude:** 781.78 | **LOC:** 922 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_cpms` **(Compute Cores)** (Impact: 29.1)
    * *Intent:* # <end id="record_click"/> # 代码清单 7-16 # <start id="update_cpms"/>
  * `search_and_zsort` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* # <end id="sorted-searches"/> # 代码清单 7-6 # <start id="zset_scored_composite"/> # 和之前一样，函数接受一个已有搜索结果的...
  * `parse` **(Type Conversions)** (Impact: 19.1)
    * *Intent:* # 这个集合将用于储存不需要的单词。 unwanted = set() # 这个列表将用于储存需要执行交集计算的单词。 all = [] # 这个集合将用于储存目前已发现的同义词。 current =...
  * `parse_and_search` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* # <end id="parse-query"/> # 代码清单 7-4 # <start id="search-query"/> # 对查询语句进行分析。 all, unwanted = parse...
  * `record_click` **(Many-Argument Workhorses)** (Impact: 17.2)
    * *Intent:* # <end id="record_targeting"/> # 代码清单 7-15 # <start id="record_click"/>
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 115`, `args: 49`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 159`, `unreferenced_by_name: 16`
* *Architecture:* `api: 45`, `import: 5`
* *Defense:* `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math, re, redis, unittest, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch10_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.807)
- **Top Global Matches:** file_cluster_12: 5.807, file_cluster_15: 8.299, file_cluster_7: 9.081
- **Magnitude:** 771.14 | **LOC:** 839 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_shard_results_thread` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `search_and_zsort` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `syndicate_status` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* # <end id="sharded-zrangebyscore"/> # 代码清单 10-15 # <start id="sharded-syndicate-posts"/>
  * `search_shards_zset` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* # <end id="zset-search-with-values"/> # 代码清单 10-9 # <start id="search-shards-zset"/> # 函数需要接受所有分片参数以...
  * `test_sharded_follow_user_and_syndicate_status` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 127 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 108`, `args: 50`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 153`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 45`, `concurrency: 3`, `import: 12`
* *Defense:* `safety: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Queue, binascii, collections, datetime, decimal, functools, json, redis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch06_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.76)
- **Top Global Matches:** file_cluster_15: 5.76, file_cluster_12: 7.321, file_cluster_16: 7.871
- **Magnitude:** 769.78 | **LOC:** 1128 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.0%), Guard Balance (formerly Safety Score) (72.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy_logs_to_redis` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* # <end id="_1314_15044_3669"/> # 代码清单 6-30 # <start id="_1314_14473_9209"/>
  * `readblocks_gz` **(Compute Cores)** (Impact: 22.9)
    * *Intent:* # <end id="_1314_14473_9225"/> # 代码清单 6-34 # <start id="_1314_14473_9229"/>
  * `process_logs_from_redis` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* # <end id="_1314_14473_9209"/> # 代码清单 6-31 # <start id="_1314_14473_9213"/>
  * `test_file_distribution` **(Compute Cores)** (Impact: 12.6)
  * `readlines` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* # <end id="_1314_14473_9213"/> # 代码清单 6-32 # <start id="_1314_14473_9221"/>
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 109 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 130`, `args: 48`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 137`, `unreferenced_by_name: 23`
* *Architecture:* `io: 8`, `api: 47`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 17`, `test: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bisect, collections, gzip, json, math, os, pprint, redis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch08_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.259)
- **Top Global Matches:** file_cluster_12: 6.259, file_cluster_15: 7.396, file_cluster_16: 9.089
- **Magnitude:** 717.9 | **LOC:** 1052 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Debt Markers (formerly Tech Debt) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter_content` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* # <end id="delete-message-streaming"/> # 代码清单 8-15 # <start id="message-subscription"/> # 使用第 5 章介绍的...
  * `refill_timeline` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `process_filters` **(Compute Cores)** (Impact: 15.5)
  * `syndicate_status_list` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* # <end id="syndicate-message"/> # <start id="syndicate-message-list"/>
  * `clean_timelines` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* # <end id="delete-message"/> # <start id="exercise-clean-out-timelines"/>
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 110 instances
* *Api Near Db Sink:* 2 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 127`, `args: 45`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 125`, `planned_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `io: 2`, `api: 47`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 5`, `doc: 1`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BaseHTTPServer, SocketServer, cgi, functools, json, math, random, redis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch05_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.081)
- **Top Global Matches:** file_cluster_12: 6.081, file_cluster_15: 7.984, file_cluster_11: 9.454
- **Magnitude:** 618.3 | **LOC:** 756 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clean_counters` **(Compute Cores)** (Impact: 17.7)
    * *Intent:* # <end id="get_counter"/> # <start id="clean_counters"/>
  * `import_ips_to_redis` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* # a faster version with pipelines for actual testing
  * `import_ips_to_redis` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* # <end id="_1314_14473_9188"/> # 代码清单 5-10 # <start id="_1314_14473_9191"/> # 这个函数在执行时需要给定GeoLiteCit...
  * `get_config` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `update_stats` **(Many-Argument Workhorses)** (Impact: 12.0)
    * *Intent:* # <end id="clean_counters"/> # 代码清单 5-6 # <start id="update_stats"/> # 设置用于存储统计数据的键。 destination = '...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 106 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 101`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 138`, `unreferenced_by_name: 10`
* *Architecture:* `io: 6`, `api: 36`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 8`, `doc: 1`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bisect, contextlib, csv, datetime, functools, json, logging, pprint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.214)
- **Top Global Matches:** file_cluster_5: 6.214, file_cluster_12: 8.156, file_cluster_7: 10.141
- **Magnitude:** 610.62 | **LOC:** 959 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 6.428; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (57.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateCpms` **(Type Conversions)** (Impact: 28.0)
  * `parseAndSearch` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `recordClick` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `indexAd` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `testStringToScore` **(Defensive Guards)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 148`, `args: 48`, `func_start: 47`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 135`, `unreferenced_by_name: 2`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `safety: 55`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.428
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008846
  * `Imports (Out-Degree: 2):` java.util.*, java.util.regex.Matcher, java.util.regex.Pattern, org.javatuples.Pair, redis.clients.jedis.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter06.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.703)
- **Top Global Matches:** file_cluster_5: 6.703, file_cluster_12: 8.47, file_cluster_7: 9.712
- **Magnitude:** 489.5 | **LOC:** 951 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.1%), Complexity Load (formerly Cognitive Load) (38.1%)
- **Documentation Coverage:** 83.7209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processLogsFromRedis` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `fetchPendingMessages` **(Generic / Templated Code)** (Impact: 18.7)
  * `run` **(Defensive Guards)** (Impact: 15.6)
  * `testAddUpdateContact` **(Defensive Guards)** (Impact: 12.5)
  * `autocompleteOnPrefix` **(Many-Argument Workhorses)** (Impact: 12.3)
    * *Intent:* /** * 代码清单 6-4 */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 140`, `args: 53`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 81`, `unreferenced_by_name: 2`
* *Architecture:* `io: 22`, `api: 51`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 46`, `doc: 7`, `sync_locks: 10`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.google.gson.Gson, com.google.gson.reflect.TypeToken, java.io.*, java.util.*, java.util.zip.GZIPInputStream, java.util.zip.GZIPOutputStream, redis.clients.jedis.Jedis, redis.clients.jedis.Transaction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.463)
- **Top Global Matches:** file_cluster_5: 6.463, file_cluster_7: 10.158, file_cluster_12: 10.341
- **Magnitude:** 487.8 | **LOC:** 1012 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **51**; blast radius 6.108; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.0%)
- **Documentation Coverage:** 75.4098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newPut` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `getPageData` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `getScrollData` **(Stateful Encapsulated Methods)** (Impact: 15.0)
  * `getRowFromResult` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `toEntity` **(Stateful Encapsulated Methods)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 291`, `args: 70`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 54`, `concurrency: 4`, `import: 51`
* *Defense:* `safety: 22`, `doc: 16`, `sync_locks: 4`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.108
  * `Choke Point (Betweenness):` 0.000555 | `Ripple Effect (Closeness):` 0.016379
  * `Imports (Out-Degree: 11):` cn.hutool.core.collection.CollectionUtil, cn.hutool.core.date.DatePattern, cn.hutool.core.date.DateUtil, cn.hutool.core.io.IoUtil, cn.hutool.core.map.MapUtil, cn.hutool.core.util.ArrayUtil, cn.hutool.core.util.ObjectUtil, cn.hutool.core.util.ReflectUtil...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action-py/ch11_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.055)
- **Top Global Matches:** file_cluster_12: 6.055, file_cluster_15: 6.935, file_cluster_16: 8.923
- **Magnitude:** 423.86 | **LOC:** 799 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (93.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sharded_bpop_helper` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* # 定义一个辅助函数， # 这个函数会为左端阻塞弹出操作以及右端阻塞弹出操作执行实际的弹出动作。 # 准备好流水线对象和超时信息。 pipe = conn.pipeline(False) timeou...
  * `purchase_item_with_lock` **(Many-Argument Workhorses)** (Impact: 10.4)
    * *Intent:* # <end id="autocomplete-on-prefix-lua"/> # 代码清单 11-12 # <start id="ch06-purchase-item-with-lock"/>
  * `call` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* # 在调用已载入脚本的时候， # 用户需要将 Redis 连接、脚本要处理的键以及脚本的其他参数传递给脚本。
  * `acquire_lock_with_timeout` **(Many-Argument Workhorses)** (Impact: 10.0)
    * *Intent:* # <end id="post-status-lua"/> # 代码清单 11-4 # <start id="old-lock"/>
  * `acquire_lock_with_timeout` **(Type Conversions)** (Impact: 9.7)
    * *Intent:* # 代码清单 11-5 # <start id="lock-in-lua"/>
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 87`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 92`, `planned_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 38`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 8`, `doc: 13`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bisect, math, redis, threading, time, unittest, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.877)
- **Top Global Matches:** file_cluster_5: 6.877, file_cluster_12: 7.777, file_cluster_7: 9.66
- **Magnitude:** 398.74 | **LOC:** 732 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 9.328; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Concurrency Surface (formerly Concurrency) (51.4%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(I/O & Config Routines)** (Impact: 12.8)
  * `logCommon` **(Many-Argument Workhorses)** (Impact: 11.3)
  * `updateStats` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `importIpsToRedis` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** * 代码清单 5-10 */
  * `testIpLookup` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 125`, `args: 40`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 68`, `unreferenced_by_name: 3`
* *Architecture:* `io: 9`, `api: 55`, `concurrency: 6`, `import: 10`
* *Defense:* `safety: 24`, `doc: 4`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.328
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.015924
  * `Imports (Out-Degree: 2):` com.google.gson.Gson, com.google.gson.reflect.TypeToken, java.io.File, java.io.FileReader, java.io.Serializable, java.text.Collator, java.text.SimpleDateFormat, java.util.*...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.794)
- **Top Global Matches:** file_cluster_5: 5.794, file_cluster_7: 9.323, file_cluster_12: 9.494
- **Magnitude:** 355.58 | **LOC:** 702 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **72**; blast radius 8.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (73.5%), Connectivity (formerly Api Exposure) (70.2%), Guard Balance (formerly Safety Score) (69.7%)
- **Documentation Coverage:** 87.8049% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pojoListByIds` **(Generic / Templated Code)** (Impact: 19.5)
  * `save` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* // ==================================================================== // CRUD 操作 // ==============...
  * `updateById` **(Many-Argument Workhorses)** (Impact: 15.6)
  * `pojoPageByScrollId` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* /** * search after 分页 */
  * `setMapping` **(Many-Argument Workhorses)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Api Near Db Sink:* 2 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 240`, `args: 47`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 29`
* *Architecture:* `api: 41`, `concurrency: 2`, `import: 72`
* *Defense:* `safety: 2`, `doc: 6`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.553
  * `Choke Point (Betweenness):` 0.000249 | `Ripple Effect (Closeness):` 0.019506
  * `Imports (Out-Degree: 5):` cn.hutool.core.collection.CollectionUtil, cn.hutool.core.io.IoUtil, cn.hutool.core.map.MapUtil, cn.hutool.core.util.ArrayUtil, cn.hutool.core.util.StrUtil, io.github.dunwu.javadb.elasticsearch.entity.BaseEsEntity, io.github.dunwu.javadb.elasticsearch.entity.common.PageData, io.github.dunwu.javadb.elasticsearch.entity.common.ScrollData...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action-py/ch09_listing_source.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.048)
- **Top Global Matches:** file_cluster_15: 6.048, file_cluster_12: 7.752, file_cluster_16: 8.29
- **Magnitude:** 344.04 | **LOC:** 591 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (87.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_aggregates` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* # <end id="aggregate-population"/> # 代码清单 9-17 # <start id="code-to-location"/>
  * `test_user_location` **(Compute Cores)** (Impact: 13.9)
  * `get_code` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* # <end id="location-tables"/> # 代码清单 9-14 # <start id="location-to-code"/> # 寻找国家对应的偏移量。 cindex = bi...
  * `get_expected` **(Many-Argument Workhorses)** (Impact: 11.5)
    * *Intent:* # 如果程序已经计算出或者获取到了当日的预计访客人数， # 那么直接使用已计算出的数字。 if key in EXPECTED: return EXPECTED[key] exkey = key + ...
  * `long_ziplist_performance` **(Many-Argument Workhorses)** (Impact: 10.9)
    * *Intent:* # <start id="rpoplpush-benchmark"/> # 为了以不同的方式进行性能测试，函数需要对所有测试指标进行参数化处理。 # 删除指定的键，确保被测试数据的准确性。 conn....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 52`, `args: 25`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 63`, `unreferenced_by_name: 10`
* *Architecture:* `api: 24`, `import: 9`
* *Defense:* `safety: 1`, `doc: 9`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` binascii, bisect, collections, datetime, math, redis, time, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.807)
- **Top Global Matches:** file_cluster_12: 6.807, file_cluster_5: 6.819, file_cluster_0: 9.77
- **Magnitude:** 341.3 | **LOC:** 458 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testUserLocation` **(Defensive Guards)** (Impact: 16.1)
  * `updateAggregates` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `getExpected` **(Many-Argument Workhorses)** (Impact: 13.3)
  * `longZiplistPerformance` **(Many-Argument Workhorses)** (Impact: 10.6)
  * `getCode` **(Type Conversions)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 70`, `args: 27`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 65`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 26`, `import: 8`
* *Defense:* `safety: 19`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.io.IOException, java.io.InputStream, java.text.SimpleDateFormat, java.util.*, java.util.zip.CRC32, org.javatuples.Pair, redis.clients.jedis.Jedis, redis.clients.jedis.Pipeline...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch02_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.342)
- **Top Global Matches:** file_cluster_15: 6.342, file_cluster_12: 7.223, file_cluster_11: 8.624
- **Magnitude:** 306.04 | **LOC:** 414 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.4%), Complexity Load (formerly Cognitive Load) (84.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cache_rows` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* # <end id="_1311_14471_8287"/> # 代码清单 2-8 # <start id="_1311_14471_8292"/>
  * `can_cache` **(Compute Cores)** (Impact: 7.4)
    * *Intent:* # <end id="_1311_14471_8288"/> # 代码清单 2-11 # <start id="_1311_14471_8289"/> # 尝试从页面里面取出商品ID。 item_id...
  * `add_to_cart` **(Compute Cores)** (Impact: 7.1)
    * *Intent:* # <end id="_1311_14471_8270"/> # 代码清单 2-4 # <start id="_1311_14471_8279"/>
  * `cache_request` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* # <end id="_1311_14471_8271"/> # 代码清单 2-6 # <start id="_1311_14471_8291"/> # 对于不能被缓存的请求，直接调用回调函数。 if...
  * `clean_sessions` **(Compute Cores)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 55`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 66`, `unreferenced_by_name: 8`
* *Architecture:* `api: 25`, `concurrency: 4`, `import: 8`
* *Defense:* `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json, pprint, redis, threading, time, unittest, urlparse, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter08.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.719)
- **Top Global Matches:** file_cluster_5: 6.719, file_cluster_12: 8.064, file_cluster_7: 8.65
- **Magnitude:** 298.72 | **LOC:** 537 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Debt Markers (formerly Tech Debt) (77.1%), Guard Balance (formerly Safety Score) (61.3%), Complexity Load (formerly Cognitive Load) (36.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `refillTimeline` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `cleanTimelines` **(Many-Argument Workhorses)** (Impact: 16.2)
  * `acquireLockWithTimeout` **(Defensive Guards)** (Impact: 12.3)
  * `followUser` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `unfollowUser` **(Many-Argument Workhorses)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 72`, `args: 53`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 47`, `duplicate_logic: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 28`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 65`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` java.lang.reflect.Method, java.util.*, redis.clients.jedis.Jedis, redis.clients.jedis.Pipeline, redis.clients.jedis.Transaction, redis.clients.jedis.Tuple
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/jedis/rank/RankDemo.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.002)
- **Top Global Matches:** file_cluster_5: 8.002, file_cluster_7: 10.133, file_cluster_14: 11.115
- **Magnitude:** 279.76 | **LOC:** 668 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 4.555; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (22.2%), Connectivity (formerly Api Exposure) (2.8%)
- **Documentation Coverage:** 6.4516% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveRankWithRegions` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* /** * 更新【分区】排行榜 * * @param member 榜单成员 * @param score 榜单成员分值 */
  * `getRankElementListWithRegions` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* /** * 根据从总排名的范围获取元素列表 * * @param begin 总排名中的起始位置 * @param end 总排名中的结束位置 * @param isAsc true：从低到高 / f...
  * `deleteWithAutoAdjust` **(Stateful Encapsulated Methods)** (Impact: 16.1)
    * *Intent:* /** * 先将原始排名记录从所属分区中删除，并动态调整之后的分区 */
  * `getRankElementInRegion` **(Stateful Encapsulated Methods)** (Impact: 13.4)
    * *Intent:* /** * 获取指定分区中指定排名的信息 * * @param region 指定榜单分区 * @param rank 分区中的排名 * @param isAsc true：从低到高 / false：...
  * `addWithAutoAdjust` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* /** * 根据 member，score 将成员的记录插入到合适的分区中，如果没有合适的分区，说明在 10W 名以外，则不插入 * <p> * 如果成员在 {@link #TOTAL_RANK_LE...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 88`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 34`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `doc: 32`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.555
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.003185
  * `Imports (Out-Degree: 3):` cn.hutool.core.bean.BeanUtil, cn.hutool.core.collection.CollectionUtil, java.util.*, java.util.stream.Collectors, lombok.extern.slf4j.Slf4j, redis.clients.jedis.Jedis, redis.clients.jedis.Pipeline, redis.clients.jedis.Response...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter02.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.135)
- **Top Global Matches:** file_cluster_5: 7.135, file_cluster_12: 7.497, file_cluster_7: 8.717
- **Magnitude:** 225.98 | **LOC:** 503 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.16; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Mutation Surface (formerly State Flux) (94.0%), Debt Markers (formerly Tech Debt) (84.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canCache` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /** * 代码清单 2-11 */
  * `cacheRequest` **(Many-Argument Workhorses)** (Impact: 9.1)
    * *Intent:* /** * 代码清单 2-6 页面缓存 */
  * `testShopppingCartCookies` **(Defensive Guards)** (Impact: 7.4)
  * `addToCart` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* /** * 代码清单 2-4 */
  * `run` **(I/O & Config Routines)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 77`, `args: 34`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 33`, `duplicate_logic: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 37`, `concurrency: 14`, `import: 5`
* *Defense:* `safety: 21`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003185
  * `Imports (Out-Degree: 2):` com.google.gson.Gson, java.net.MalformedURLException, java.net.URL, java.util.*, redis.clients.jedis.Jedis, redis.clients.jedis.Tuple
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `codes/redis/redis-in-action-py/ch04_listing_source.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.676)
- **Top Global Matches:** file_cluster_12: 6.676, file_cluster_15: 6.959, file_cluster_11: 8.351
- **Magnitude:** 174.68 | **LOC:** 391 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (72.1%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_logs` **(Many-Argument Workhorses)** (Impact: 16.6)
    * *Intent:* # 代码清单 4-2 # <start id="process-logs-progress"/> # 日志处理函数接受的其中一个参数为回调函数， # 这个回调函数接受一个Redis连接和一个日志行作为...
  * `purchase_item` **(Many-Argument Workhorses)** (Impact: 11.5)
    * *Intent:* # <end id="_1313_14472_8342"/> # 代码清单 4-6 # <start id="_1313_14472_8353"/>
  * `wait_for_sync` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* # <end id="process-logs-progress"/> # 代码清单 4-3 # <start id="wait-for-sync"/>
  * `list_item` **(Many-Argument Workhorses)** (Impact: 8.2)
    * *Intent:* # 代码清单 4-5 # <start id="_1313_14472_8342"/>
  * `benchmark_update_token` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* # <end id="update-token-pipeline"/> # 代码清单 4-9 # <start id="simple-pipeline-benchmark-code"/> # 测试会分...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 32`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 38`, `unreferenced_by_name: 6`
* *Architecture:* `io: 3`, `api: 14`, `import: 7`
* *Defense:* `safety: 4`, `doc: 3`, `test: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, pprint, redis, time, unittest, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/mapper/BaseEsMapper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.634)
- **Top Global Matches:** file_cluster_5: 6.634, file_cluster_7: 9.013, file_cluster_12: 10.219
- **Magnitude:** 174.3 | **LOC:** 503 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 3.148; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (88.5%), Guard Balance (formerly Safety Score) (80.0%), Concurrency Surface (formerly Concurrency) (22.7%), Mutation Surface (formerly State Flux) (14.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createIndex` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `onResponse` **(Annotated & Test Methods)** (Impact: 4.6)
  * `asyncSaveBatch` **(Generic / Templated Code)** (Impact: 4.2)
  * `asyncUpdateBatchIds` **(Generic / Templated Code)** (Impact: 4.2)
  * `asyncDeleteBatchIds` **(Generic / Templated Code)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 113`, `args: 40`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 4`, `unreferenced_by_name: 20`
* *Architecture:* `api: 45`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 50`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.148
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.007166
  * `Imports (Out-Degree: 6):` cn.hutool.core.collection.CollectionUtil, cn.hutool.core.map.MapUtil, cn.hutool.core.util.ReflectUtil, cn.hutool.core.util.StrUtil, cn.hutool.json.JSONUtil, io.github.dunwu.javadb.elasticsearch.ElasticsearchTemplate, io.github.dunwu.javadb.elasticsearch.constant.ResultCode, io.github.dunwu.javadb.elasticsearch.entity.BaseEsEntity...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/mapper/UserEsMapperTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.455)
- **Top Global Matches:** file_cluster_5: 6.455, file_cluster_12: 7.751, file_cluster_7: 8.272
- **Magnitude:** 152.56 | **LOC:** 473 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 2.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.8%), Complexity Load (formerly Cognitive Load) (16.6%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pojoPageByLastId` **(Annotated & Test Methods)** (Impact: 6.9)
  * `pojoPageByLastIdInDay` **(Annotated & Test Methods)** (Impact: 6.9)
  * `pojoScroll` **(Annotated & Test Methods)** (Impact: 6.0)
  * `pojoScrollInDay` **(Annotated & Test Methods)** (Impact: 6.0)
  * `getMockList` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *Api Near Db Sink:* 8 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 82`, `args: 30`, `func_start: 22`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 22`, `unreferenced_by_name: 14`
* *Architecture:* `api: 23`, `import: 24`
* *Defense:* `doc: 1`, `test: 52`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` cn.hutool.core.collection.CollectionUtil, cn.hutool.core.util.RandomUtil, cn.hutool.core.util.StrUtil, io.github.dunwu.javadb.elasticsearch.BaseApplicationTests, io.github.dunwu.javadb.elasticsearch.entity.User, io.github.dunwu.javadb.elasticsearch.entity.common.PageData, io.github.dunwu.javadb.elasticsearch.entity.common.ScrollData, io.github.dunwu.javadb.elasticsearch.util.JsonUtil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch03_listing_source.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.593)
- **Top Global Matches:** file_cluster_15: 6.593, file_cluster_12: 6.797, file_cluster_2: 8.673
- **Magnitude:** 137.74 | **LOC:** 508 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.7%), Debt Markers (formerly Tech Debt) (83.5%), Guard Balance (formerly Safety Score) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `article_vote` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* # <end id="exercise-fix-article-vote"/> # 从技术上来将，上面的 article_vote() 函数仍然有一些问题， # 这些问题可以通过下面展示的这段代码来解...
  * `add_to_cart` **(Compute Cores)** (Impact: 7.1)
  * `article_vote` **(Many-Argument Workhorses)** (Impact: 6.9)
    * *Intent:* # <start id="exercise-fix-article-vote"/> # 在进行投票之前，先检查这篇文章是否仍然处于可投票的时间之内 cutoff = time.time() - ONE...
  * `update_token` **(Many-Argument Workhorses)** (Impact: 5.1)
    * *Intent:* # <start id="exercise-update-token"/>
  * `update_token` **(Many-Argument Workhorses)** (Impact: 5.1)
    * *Intent:* # 在一次命令调用里面，同时为字符串键设置值和过期时间 conn.setex('login:' + token, user, THIRTY_DAYS) key = 'viewed:' + token ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 17`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `unreferenced_by_name: 4`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 2`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` redis, threading, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/HbaseTemplateScanTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.868)
- **Top Global Matches:** file_cluster_5: 6.868, file_cluster_12: 8.208, file_cluster_0: 9.151
- **Magnitude:** 119.32 | **LOC:** 243 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 2.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.7%), Complexity Load (formerly Cognitive Load) (58.5%), Connectivity (formerly Api Exposure) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clear` **(Annotated & Test Methods)** (Impact: 4.4)
  * `test04` **(Annotated & Test Methods)** (Impact: 4.3)
  * `test05` **(Annotated & Test Methods)** (Impact: 4.3)
  * `test06` **(Annotated & Test Methods)** (Impact: 4.2)
  * `test02` **(Annotated & Test Methods)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 63`, `args: 12`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 54`, `unreferenced_by_name: 8`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 2`, `doc: 1`, `test: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` cn.hutool.core.collection.CollectionUtil, cn.hutool.core.util.RandomUtil, cn.hutool.core.util.StrUtil, cn.hutool.json.JSONUtil, io.github.dunwu.javadb.hbase.entity.common.PageData, io.github.dunwu.javadb.hbase.entity.common.RowDo, io.github.dunwu.javadb.hbase.entity.common.ScrollData, io.github.dunwu.javadb.hbase.entity.scan.MultiFamilyScan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/mysql/SQL必知必会示例/populate.sql` (SQLITE | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.627)
- **Top Global Matches:** file_cluster_2: 3.627, file_cluster_17: 4.541, file_cluster_13: 5.374
- **Magnitude:** 113.64 | **LOC:** 119 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`, `args: 43`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/javadb/elasticsearch/elasticsearch6/src/test/java/io/github/dunwu/javadb/elasticsearch/BaseElasticsearchTemplateTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.173)
- **Top Global Matches:** file_cluster_5: 6.173, file_cluster_12: 8.192, file_cluster_7: 9.594
- **Magnitude:** 112.88 | **LOC:** 296 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 2.462; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.0%), Complexity Load (formerly Cognitive Load) (17.2%), Connectivity (formerly Api Exposure) (6.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pojoScroll` **(I/O & Config Routines)** (Impact: 7.0)
  * `pojoPageByLastId` **(Callbacks & Closures)** (Impact: 6.8)
  * `onResponse` **(Annotated & Test Methods)** (Impact: 4.6)
  * `deleteIndex` **(Stateful Encapsulated Methods)** (Impact: 3.8)
  * `query` **(Stateful Encapsulated Methods)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *Api Near Db Sink:* 4 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 72`, `args: 30`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 10`, `unreferenced_by_name: 13`
* *Architecture:* `api: 28`, `import: 23`
* *Defense:* `safety: 2`, `doc: 1`, `test: 23`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` cn.hutool.core.collection.CollectionUtil, cn.hutool.core.util.StrUtil, io.github.dunwu.javadb.elasticsearch.entity.BaseEsEntity, io.github.dunwu.javadb.elasticsearch.entity.common.PageData, io.github.dunwu.javadb.elasticsearch.entity.common.ScrollData, io.github.dunwu.javadb.elasticsearch.util.JsonUtil, java.io.IOException, java.util.Arrays...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codes/redis/redis-in-action-py/ch01_listing_source.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.246)
- **Top Global Matches:** file_cluster_12: 6.246, file_cluster_7: 7.94, file_cluster_15: 8.866
- **Magnitude:** 104.1 | **LOC:** 301 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.462; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.8%), Debt Markers (formerly Tech Debt) (62.2%), Complexity Load (formerly Cognitive Load) (29.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_remove_groups` **(Many-Argument Workhorses)** (Impact: 7.2)
    * *Intent:* # <end id="fetch-articles-code"/> # 代码清单 1-9 # <start id="add-remove-groups"/> # 构建存储文章信息的键名。 articl...
  * `article_vote` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* # 计算文章的投票截止时间。 cutoff = time.time() - ONE_WEEK_IN_SECONDS # 检查是否还可以对文章进行投票 # （虽然使用散列也可以获取文章的发布时间， # ...
  * `test_article_functionality` **(I/O & Config Routines)** (Impact: 6.3)
  * `get_group_articles` **(Many-Argument Workhorses)** (Impact: 5.2)
    * *Intent:* # <end id="add-remove-groups"/> # 代码清单 1-10 # <start id="fetch-articles-group"/> # 为每个群组的每种排列顺序都创建一个...
  * `get_articles` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* # 设置获取文章的起始索引和结束索引。 start = (page - 1) * ARTICLES_PER_PAGE end = start + ARTICLES_PER_PAGE - 1 # 获取多...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`, `unreferenced_by_name: 3`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `doc: 5`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pprint, redis, time, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `codes/javadb/h2/src/test/java/io/github/dunwu/javadb/h2/springboot/SpringBootJpaTest.java` (JAVA) | Magnitude: 32.88 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 40, test: 17, import: 14
- `codes/javadb/hbase/src/test/java/io/github/dunwu/javadb/hbase/OrderMapper.java` (JAVA) | Magnitude: 10.58 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, api: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java` (JAVA) | Magnitude: 341.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 358, core_var_decl: 97, structural_boundaries: 70, design_snake_case: 69
- `codes/javadb/redis/src/test/java/io/github/dunwu/javadb/redis/RedissonStandaloneTest.java` (JAVA) | Magnitude: 26.22 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 25, import: 12, core_var_decl: 8
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/constant/ResultCode.java` (JAVA) | Magnitude: 18.82 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 11, args: 9, func_start: 6
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/advanced/AdvancedIntegrationTests.java` (JAVA) | Magnitude: 11.08 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, import: 12, decorators: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/textsearch/TextSearchRepositoryTests.java` (JAVA) | Magnitude: 11.34 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 13, core_var_decl: 8, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `codes/javadb/mongodb/src/main/java/io/github/dunwu/javadb/mongodb/springboot/aggregation/OrderRepositoryCustom.java` (JAVA) | Magnitude: 1.58 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, args: 1, func_start: 1
- `codes/javadb/mongodb/src/main/java/io/github/dunwu/javadb/mongodb/springboot/projections/CustomerProjection.java` (JAVA) | Magnitude: 1.18 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/querybyexample/MongoOperationsIntegrationTests.java` (JAVA) | Magnitude: 26.62 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 45, import: 16, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `codes/javadb/mongodb/src/test/java/io/github/dunwu/javadb/mongodb/springboot/querybyexample/ContactRepositoryIntegrationTests.java` (JAVA) | Magnitude: 16.84 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 27, import: 12, test: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` -> **Severity: 0.05** (Bridge: 0.0006 * Flux: 89.3435%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 73.4912%)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/annotation/RowKeyUtil.java` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 99.9285%)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/mapper/BaseHbaseMapper.java` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 32.2141%)
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.8938%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/util/JsonUtil.java` -> **Severity: 2.123** (Embedded: 0.0265 * Error Risk: 80.0%)
- `codes/javadb/elasticsearch/elasticsearch6/src/main/java/io/github/dunwu/javadb/elasticsearch/ElasticsearchTemplate.java` -> **Severity: 1.36** (Embedded: 0.0195 * Error Risk: 69.7237%)
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/SortedSetDemo.java` -> **Severity: 1.325** (Embedded: 0.0255 * Error Risk: 51.9989%)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/HbaseTemplate.java` -> **Severity: 1.31** (Embedded: 0.0164 * Error Risk: 80.0%)
- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/annotation/RowKeyUtil.java` -> **Severity: 1.266** (Embedded: 0.0199 * Error Risk: 63.519%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `codes/javadb/hbase/src/main/java/io/github/dunwu/javadb/hbase/annotation/RowKeyUtil.java` -> **Severity: 1824.618** (Blast Radius: 20.679 * Doc Risk: 88.2353%)
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/SortedSetDemo.java` -> **Severity: 1748.0** (Blast Radius: 17.48 * Doc Risk: 100.0%)
- `codes/javadb/mongodb/src/main/java/io/github/dunwu/javadb/mongodb/springboot/textsearch/BlogPost.java` -> **Severity: 1020.7** (Blast Radius: 10.207 * Doc Risk: 100.0%)
- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter05.java` -> **Severity: 843.962** (Blast Radius: 9.328 * Doc Risk: 90.4762%)
- `codes/javadb/elasticsearch/elasticsearch7/src/main/java/io/github/dunwu/javadb/elasticsearch/springboot/entities/User.java` -> **Severity: 842.8** (Blast Radius: 8.428 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 313 literal sites + 4 sites through wrappers = 317

- `testBenchmarkUpdateToken` (function, debug_prints, primitive): 1 call sites in 1 files -- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter04.java`
- `testIsQualifiedForJob` (function, debug_prints, primitive): 1 call sites in 1 files -- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter07.java`
- `testLongZiplistPerformance` (function, debug_prints, primitive): 1 call sites in 1 files -- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/Chapter09.java`
- `zcard` (function, debug_prints, primitive): 1 call sites in 1 files -- `codes/redis/redis-in-action/src/main/java/io/github/dunwu/db/redis/SortedSetDemo.java`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6861 call pairs -- scoped 15.4%, unique 0.3%, ambiguous 11.0%, external 73.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 4935 | 15.9% | 0.5% | 14.6% | 69.0% |
| python | 1803 | 15.0% | 0.0% | 1.8% | 83.1% |
| shell | 87 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 36 | 2.8% | 0.0% | 0.0% | 97.2% |

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
