# ARCHITECTURAL_BRIEF: kafka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/kafka` |
| **Timestamp** | `2026-08-03T20:59:58.990203+00:00` |
| **Scan Duration** | `29.53s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `eb111f6695ef30889e7367bbad759f7e772d65ea` |
| **Git Remote** | `https://github.com/apache/kafka` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6079 malicious artifacts.

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
| Total Artifacts | 7200 |
| Analyzed Artifacts (Scanned) | 6489 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 711 |
| Total LOC | 913380 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 90.1% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1546 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 242 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 5644 | 825139 | 87.0% |
| SCALA | 295 | 72612 | 4.5% |
| JSON | 292 | 8070 | 4.5% |
| SHELL | 66 | 1903 | 1.0% |
| YAML | 40 | 1324 | 0.6% |
| PLAINTEXT | 38 | 5 | 0.6% |
| BATCH | 36 | 799 | 0.6% |
| PYTHON | 30 | 2771 | 0.5% |
| XML | 22 | 0 | 0.3% |
| MARKDOWN | 16 | 0 | 0.2% |
| DOCKERFILE | 4 | 273 | 0.1% |
| GROOVY | 3 | 325 | 0.0% |
| HTML | 2 | 12 | 0.0% |
| RUBY | 1 | 147 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.255`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 3127 | 48.2% |
| file_cluster_8 | 2475 | 38.1% |
| file_cluster_16 | 487 | 7.5% |
| file_cluster_0 | 224 | 3.5% |
| file_cluster_4 | 110 | 1.7% |
| Unknown | 5 | 0.1% |
| file_cluster_12 | 3 | 0.0% |
| file_cluster_17 | 3 | 0.0% |
| file_cluster_7 | 2 | 0.0% |
| file_cluster_11 | 1 | 0.0% |
| file_cluster_2 | 1 | 0.0% |
| file_cluster_1 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 49 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 711*

**Composition by Extension & Reason:**
- `.java`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1486 LOC)
- `.py`: 146x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 93 LOC)
- `.md`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `no_extension`: 42x Unsupported Format (.undeterminable), 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Binary Format Detected)
- `.png`: 47x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.converter`: 16x Unsupported Format (.converter)
- `.scala`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Saturation: Line 29 exceeds 500 chars)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2572 LOC)
- `.yaml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.conf`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.conf'), 1x Unsupported Format (.conf)
- `.xml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.predicate`: 3x Unsupported Format (.predicate)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.2 | 8.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 38.8 | 47.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 17.3 | 5.7 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 43.4 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 41.2 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 69.5 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 52.3 | 92.4 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/docker/ducker-ak` (Hits: 126)
- `tools/src/main/java/org/apache/kafka/tools/ManifestWorkspace.java` (Hits: 62)
- `tests/docker/Dockerfile` (Hits: 58)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TopicPartition.java** (`clients/src/main/java/org/apache/kafka/common/TopicPartition.java`) — 873 inbound connections
2. **Errors.java** (`clients/src/main/java/org/apache/kafka/common/protocol/Errors.java`) — 572 inbound connections
3. **Utils.java** (`clients/src/main/java/org/apache/kafka/common/utils/Utils.java`) — 520 inbound connections
4. **Time.java** (`clients/src/main/java/org/apache/kafka/common/utils/Time.java`) — 518 inbound connections
5. **Uuid.java** (`clients/src/main/java/org/apache/kafka/common/Uuid.java`) — 512 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RequestConvertToJson.java** (`server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java`) — 370 outbound dependencies
2. **KafkaAdminClientTest.java** (`clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java`) — 307 outbound dependencies
3. **RequestResponseTest.java** (`clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java`) — 305 outbound dependencies
4. **KafkaAdminClient.java** (`clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java`) — 287 outbound dependencies
5. **GroupMetadataManagerTest.java** (`group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java`) — 232 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `hasRestoredToEnd` (@ `streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreChangelogReader.java`) -> Impact: **3333.8** | LOC: 834
- `parseResponse` (@ `clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java`) -> Impact: **2571.2** | LOC: 185
- `provide` (@ `clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java`) -> Impact: **2472.6** | LOC: 1012
- `parseValue` (@ `clients/src/main/java/org/apache/kafka/common/config/ConfigDef.java`) -> Impact: **1897.7** | LOC: 994
- `flushCurrentBatch` (@ `coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorRuntime.java`) -> Impact: **1834.8** | LOC: 1136
- `lastOffsetAndMaxRecordsToAcquire` (@ `core/src/main/java/kafka/server/share/SharePartition.java`) -> Impact: **1796.2** | LOC: 1064
- `ready` (@ `clients/src/main/java/org/apache/kafka/clients/NetworkClient.java`) -> Impact: **1646.9** | LOC: 687
  * *Intent:* /* the client id used to identify this client in requests to the server */
- `fieldDefault` (@ `generator/src/main/java/org/apache/kafka/message/FieldSpec.java`) -> Impact: **1585.5** | LOC: 186
- `revokeAndReassign` (@ `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java`) -> Impact: **1525.4** | LOC: 1237
- `doMapValues` (@ `streams/src/main/java/org/apache/kafka/streams/kstream/internals/KTableImpl.java`) -> Impact: **1495.3** | LOC: 415

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `yaml_to_all_tests` (@ `.github/scripts/format-test-catalog.py`) -> **O(2^N) [Recursive]**
- `merge_pr` (@ `committer-tools/kafka-merge-pr.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # merge the requested PR and return the merge hash
- `consumeMessages` (@ `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java`) -> **O(2^N) [Recursive]**
- `consumeMessages` (@ `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java`) -> **O(2^N) [Recursive]**
- `createNetworkClient` (@ `clients/src/main/java/org/apache/kafka/clients/ClientUtils.java`) -> **O(2^N) [Recursive]**
- `ClusterConnectionStates` (@ `clients/src/main/java/org/apache/kafka/clients/ClusterConnectionStates.java`) -> **O(2^N) [Recursive]**
- `toString` (@ `clients/src/main/java/org/apache/kafka/clients/FetchSessionHandler.java`) -> **O(2^N) [Recursive]**
- `ready` (@ `clients/src/main/java/org/apache/kafka/clients/NetworkClient.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /* the client id used to identify this client in requests to the server */
- `toString` (@ `clients/src/main/java/org/apache/kafka/clients/NodeApiVersions.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Create a NodeApiVersions object with a single ApiKey. It is mainly used in tests. * * @param apiKey ApiKey's id.
- `provide` (@ `clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `usage_[Truncated]` (@ `tests/docker/ducker-ak`) -> DB Complexity: **410**
  * *Intent:* # Display a usage message on the terminal and exit. # # $1: The exit status to use
- `testListOffsetsHandlesFulfillmentTimeout` (@ `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java`) -> DB Complexity: **183**
- `testStreamsReconciliationProcess` (@ `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java`) -> DB Complexity: **180**
- `testFetchOffsetsWithTopicIdsDoesNotFailO` (@ `clients/src/test/java/org/apache/kafka/clients/consumer/internals/CommitRequestManagerTest.java`) -> DB Complexity: **152**
- `Anonymous_Block` (@ `bin/kafka-run-class.sh`) -> DB Complexity: **145**
  * *Intent:* # WINDOWS_OS_FORMAT == 1 if Cygwin or MinGW is detected, else 0.
- `testCancelReassignPartitions` (@ `metadata/src/test/java/org/apache/kafka/controller/ReplicationControlManagerTest.java`) -> DB Complexity: **127**
- `testProducerIdCountMetrics` (@ `core/src/test/scala/unit/kafka/server/ReplicaManagerTest.scala`) -> DB Complexity: **112**
- `testSyncGroupWithOldConsumerGroupProtoco` (@ `core/src/test/scala/unit/kafka/server/SyncGroupRequestTest.scala`) -> DB Complexity: **102**
- `buildResponseWithPartitionErrorWithMulti` (@ `clients/src/test/java/org/apache/kafka/clients/admin/internals/ListConsumerGroupOffsetsHandlerTest.java`) -> DB Complexity: **90**
- `testEntityTypes` (@ `metadata/src/test/java/org/apache/kafka/controller/ClientQuotaControlManagerTest.java`) -> DB Complexity: **89**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `streams/src/main/java/org/apache/kafka/streams/processor/internals` | 95 | 39326.63 | 16.72% | 47.76% |
| `streams/src/main/java/org/apache/kafka/streams/state/internals` | 203 | 38528.12 | 11.99% | 51.19% |
| `streams/src/test/java/org/apache/kafka/streams/state/internals` | 151 | 32646.24 | 16.4% | 0.0% |
| `clients/src/main/java/org/apache/kafka/clients/consumer/internals` | 97 | 31075.38 | 18.94% | 62.71% |
| `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration` | 87 | 28201.64 | 28.49% | 0.0% |
| `clients/src/test/java/org/apache/kafka/clients/consumer/internals` | 67 | 25343.36 | 19.23% | 0.0% |
| `clients/src/main/java/org/apache/kafka/common/requests` | 192 | 24405.26 | 19.5% | 28.93% |
| `streams/src/test/java/org/apache/kafka/streams/processor/internals` | 73 | 21863.88 | 14.41% | 0.0% |
| `streams/src/test/java/org/apache/kafka/streams/kstream/internals` | 63 | 20492.5 | 19.81% | 0.0% |
| `streams/src/main/java/org/apache/kafka/streams/kstream/internals` | 105 | 19804.16 | 12.78% | 56.07% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/label_small.sh` -> **100.0%** Exposure
- `bin/connect-distributed.sh` -> **100.0%** Exposure
- `bin/connect-mirror-maker.sh` -> **100.0%** Exposure
- `bin/connect-plugin-path.sh` -> **100.0%** Exposure
- `bin/connect-standalone.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/scripts/label_small.sh` -> **100.0%** Exposure
- `bin/connect-distributed.sh` -> **100.0%** Exposure
- `bin/connect-mirror-maker.sh` -> **100.0%** Exposure
- `bin/connect-standalone.sh` -> **100.0%** Exposure
- `bin/kafka-run-class.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> **211** Orphaned Functions | **31** Duplicates
- `streams/src/test/java/org/apache/kafka/streams/StreamsConfigTest.java` -> **145** Orphaned Functions | **23** Duplicates
- `streams/src/test/java/org/apache/kafka/streams/kstream/internals/KStreamImplTest.java` -> **93** Orphaned Functions | **64** Duplicates
- `clients/src/main/java/org/apache/kafka/common/protocol/types/Type.java` -> **0** Orphaned Functions | **145** Duplicates
- `streams/src/test/java/org/apache/kafka/streams/StreamsBuilderTest.java` -> **105** Orphaned Functions | **37** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`clients/src/test/java/org/apache/kafka/common/network/ServerConnectionIdTest.java`** -> AI Confidence: **99.48%**
2. **`generator/src/test/java/org/apache/kafka/message/checker/EvolutionVerifierTest.java`** -> AI Confidence: **99.48%**
3. **`jmh-benchmarks/src/main/java/org/apache/kafka/jmh/connect/JsonConverterBenchmark.java`** -> AI Confidence: **99.48%**
4. **`raft/src/test/java/org/apache/kafka/raft/RaftUtilTest.java`** -> AI Confidence: **99.48%**
5. **`tools/src/test/java/org/apache/kafka/tools/consumer/GroupMetadataMessageFormatterTest.java`** -> AI Confidence: **99.48%**
6. **`tools/src/test/java/org/apache/kafka/tools/consumer/OffsetMessageFormatterTest.java`** -> AI Confidence: **99.48%**
7. **`generator/src/test/java/org/apache/kafka/message/StructRegistryTest.java`** -> AI Confidence: **99.39%**
8. **`streams/src/test/java/org/apache/kafka/streams/kstream/RepartitionTopicNamingTest.java`** -> AI Confidence: **99.39%**
9. **`streams/src/test/java/org/apache/kafka/streams/kstream/internals/graph/StreamsGraphTest.java`** -> AI Confidence: **99.39%**
10. **`tools/src/main/java/org/apache/kafka/tools/consumer/group/ConsumerGroupCommandOptions.java`** -> AI Confidence: **99.39%**
11. **`tools/src/main/java/org/apache/kafka/tools/consumer/group/ShareGroupCommandOptions.java`** -> AI Confidence: **99.39%**
12. **`tools/src/main/java/org/apache/kafka/tools/streams/StreamsGroupCommandOptions.java`** -> AI Confidence: **99.39%**
13. **`tools/src/test/java/org/apache/kafka/tools/consumer/ShareGroupMessageFormatterTest.java`** -> AI Confidence: **99.39%**
14. **`core/src/main/scala/kafka/coordinator/transaction/TransactionCoordinator.scala`** -> AI Confidence: **99.39%**
15. **`core/src/main/scala/kafka/server/AbstractFetcherThread.scala`** -> AI Confidence: **99.39%**
16. **`core/src/main/scala/kafka/tools/StorageTool.scala`** -> AI Confidence: **99.39%**
17. **`core/src/test/scala/unit/kafka/docker/KafkaDockerWrapperTest.scala`** -> AI Confidence: **99.39%**
18. **`core/src/test/scala/unit/kafka/server/KafkaConfigTest.scala`** -> AI Confidence: **99.39%**
19. **`core/src/test/scala/unit/kafka/server/ListGroupsRequestTest.scala`** -> AI Confidence: **99.35%**
20. **`core/src/main/scala/kafka/coordinator/transaction/TransactionMarkerRequestCompletionHandler.scala`** -> AI Confidence: **99.34%**
21. **`clients/src/test/java/org/apache/kafka/common/protocol/ProtoUtilsTest.java`** -> AI Confidence: **99.32%**
22. **`clients/src/test/java/org/apache/kafka/common/security/ssl/SslPrincipalMapperTest.java`** -> AI Confidence: **99.32%**
23. **`.github/scripts/checkstyle.py`** -> AI Confidence: **99.31%**
24. **`.github/scripts/develocity_reports.py`** -> AI Confidence: **99.31%**
25. **`.github/scripts/junit.py`** -> AI Confidence: **99.31%**
26. **`.github/scripts/pr-format.py`** -> AI Confidence: **99.31%**
27. **`committer-tools/kafka-merge-pr.py`** -> AI Confidence: **99.31%**
28. **`committer-tools/reviewers.py`** -> AI Confidence: **99.31%**
29. **`committer-tools/verify_license.py`** -> AI Confidence: **99.31%**
30. **`clients/src/main/java/org/apache/kafka/clients/CommonClientConfigs.java`** -> AI Confidence: **99.31%**
31. **`clients/src/main/java/org/apache/kafka/clients/FetchSessionHandler.java`** -> AI Confidence: **99.31%**
32. **`clients/src/main/java/org/apache/kafka/clients/admin/AlterConsumerGroupOffsetsResult.java`** -> AI Confidence: **99.31%**
33. **`clients/src/main/java/org/apache/kafka/clients/admin/AlterShareGroupOffsetsResult.java`** -> AI Confidence: **99.31%**
34. **`clients/src/main/java/org/apache/kafka/clients/admin/RemoveMembersFromConsumerGroupResult.java`** -> AI Confidence: **99.31%**
35. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/AlterConsumerGroupOffsetsHandler.java`** -> AI Confidence: **99.31%**
36. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/AlterShareGroupOffsetsHandler.java`** -> AI Confidence: **99.31%**
37. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DeleteGroupsHandler.java`** -> AI Confidence: **99.31%**
38. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DeleteShareGroupOffsetsHandler.java`** -> AI Confidence: **99.31%**
39. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/PartitionLeaderStrategy.java`** -> AI Confidence: **99.31%**
40. **`clients/src/main/java/org/apache/kafka/clients/consumer/StickyAssignor.java`** -> AI Confidence: **99.31%**
41. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/AbstractStickyAssignor.java`** -> AI Confidence: **99.31%**
42. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/CommitRequestManager.java`** -> AI Confidence: **99.31%**
43. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerNetworkClient.java`** -> AI Confidence: **99.31%**
44. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerProtocol.java`** -> AI Confidence: **99.31%**
45. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerRebalanceListenerInvoker.java`** -> AI Confidence: **99.31%**
46. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/FetchCollector.java`** -> AI Confidence: **99.31%**
47. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/OffsetsForLeaderEpochUtils.java`** -> AI Confidence: **99.31%**
48. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareFetchBuffer.java`** -> AI Confidence: **99.31%**
49. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareFetchCollector.java`** -> AI Confidence: **99.31%**
50. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/StreamsGroupHeartbeatRequestManager.java`** -> AI Confidence: **99.31%**
51. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/StreamsMembershipManager.java`** -> AI Confidence: **99.31%**
52. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/ApplicationEventProcessor.java`** -> AI Confidence: **99.31%**
53. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/CompletableEventReaper.java`** -> AI Confidence: **99.31%**
54. **`clients/src/main/java/org/apache/kafka/clients/producer/internals/BufferPool.java`** -> AI Confidence: **99.31%**
55. **`clients/src/main/java/org/apache/kafka/clients/producer/internals/Sender.java`** -> AI Confidence: **99.31%**
56. **`clients/src/main/java/org/apache/kafka/common/config/ConfigDef.java`** -> AI Confidence: **99.31%**
57. **`clients/src/main/java/org/apache/kafka/common/config/ConfigTransformer.java`** -> AI Confidence: **99.31%**
58. **`clients/src/main/java/org/apache/kafka/common/network/SslTransportLayer.java`** -> AI Confidence: **99.31%**
59. **`clients/src/main/java/org/apache/kafka/common/protocol/Protocol.java`** -> AI Confidence: **99.31%**
60. **`clients/src/main/java/org/apache/kafka/common/requests/AbstractRequest.java`** -> AI Confidence: **99.31%**
61. **`clients/src/main/java/org/apache/kafka/common/security/JaasContext.java`** -> AI Confidence: **99.31%**
62. **`clients/src/main/java/org/apache/kafka/common/security/authenticator/SaslClientAuthenticator.java`** -> AI Confidence: **99.31%**
63. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/OAuthBearerClientInitialResponse.java`** -> AI Confidence: **99.31%**
64. **`clients/src/main/java/org/apache/kafka/common/security/scram/internals/ScramMessages.java`** -> AI Confidence: **99.31%**
65. **`clients/src/main/java/org/apache/kafka/common/security/ssl/SslFactory.java`** -> AI Confidence: **99.31%**
66. **`clients/src/main/java/org/apache/kafka/common/security/ssl/SslPrincipalMapper.java`** -> AI Confidence: **99.31%**
67. **`clients/src/main/java/org/apache/kafka/common/telemetry/internals/ClientTelemetryReporter.java`** -> AI Confidence: **99.31%**
68. **`clients/src/main/java/org/apache/kafka/common/telemetry/internals/ClientTelemetryUtils.java`** -> AI Confidence: **99.31%**
69. **`clients/src/test/java/org/apache/kafka/clients/ClientUtilsTest.java`** -> AI Confidence: **99.31%**
70. **`clients/src/test/java/org/apache/kafka/common/config/ConfigTransformerTest.java`** -> AI Confidence: **99.31%**
71. **`clients/src/test/java/org/apache/kafka/common/internals/TopicTest.java`** -> AI Confidence: **99.31%**
72. **`clients/src/test/java/org/apache/kafka/common/security/authenticator/TestJaasConfig.java`** -> AI Confidence: **99.31%**
73. **`clients/src/test/java/org/apache/kafka/common/security/kerberos/KerberosNameTest.java`** -> AI Confidence: **99.31%**
74. **`clients/src/test/java/org/apache/kafka/common/security/oauthbearer/internals/unsecured/OAuthBearerValidationUtilsTest.java`** -> AI Confidence: **99.31%**
75. **`clients/src/test/java/org/apache/kafka/common/utils/UtilsTest.java`** -> AI Confidence: **99.31%**
76. **`connect/api/src/main/java/org/apache/kafka/connect/data/ConnectSchema.java`** -> AI Confidence: **99.31%**
77. **`connect/api/src/main/java/org/apache/kafka/connect/data/SchemaProjector.java`** -> AI Confidence: **99.31%**
78. **`connect/api/src/main/java/org/apache/kafka/connect/data/Values.java`** -> AI Confidence: **99.31%**
79. **`connect/api/src/main/java/org/apache/kafka/connect/header/ConnectHeaders.java`** -> AI Confidence: **99.31%**
80. **`connect/json/src/test/java/org/apache/kafka/connect/json/JsonConverterTest.java`** -> AI Confidence: **99.31%**
81. **`connect/mirror/src/main/java/org/apache/kafka/connect/mirror/MirrorCheckpointTask.java`** -> AI Confidence: **99.31%**
82. **`connect/mirror/src/main/java/org/apache/kafka/connect/mirror/MirrorHerder.java`** -> AI Confidence: **99.31%**
83. **`connect/mirror/src/main/java/org/apache/kafka/connect/mirror/OffsetSyncStore.java`** -> AI Confidence: **99.31%**
84. **`connect/mirror/src/main/java/org/apache/kafka/connect/mirror/Scheduler.java`** -> AI Confidence: **99.31%**
85. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/Worker.java`** -> AI Confidence: **99.31%**
86. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java`** -> AI Confidence: **99.31%**
87. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/IncrementalCooperativeAssignor.java`** -> AI Confidence: **99.31%**
88. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/isolation/DelegatingClassLoader.java`** -> AI Confidence: **99.31%**
89. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/isolation/PluginScanResult.java`** -> AI Confidence: **99.31%**
90. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/isolation/PluginScanner.java`** -> AI Confidence: **99.31%**
91. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/RestServerConfig.java`** -> AI Confidence: **99.31%**
92. **`connect/runtime/src/main/java/org/apache/kafka/connect/storage/OffsetStorageReaderImpl.java`** -> AI Confidence: **99.31%**
93. **`connect/runtime/src/main/java/org/apache/kafka/connect/storage/OffsetUtils.java`** -> AI Confidence: **99.31%**
94. **`connect/runtime/src/main/java/org/apache/kafka/connect/util/SinkUtils.java`** -> AI Confidence: **99.31%**
95. **`connect/runtime/src/test/java/org/apache/kafka/connect/runtime/rest/RestServerConfigTest.java`** -> AI Confidence: **99.31%**
96. **`connect/transforms/src/main/java/org/apache/kafka/connect/transforms/Cast.java`** -> AI Confidence: **99.31%**
97. **`connect/transforms/src/main/java/org/apache/kafka/connect/transforms/Flatten.java`** -> AI Confidence: **99.31%**
98. **`connect/transforms/src/main/java/org/apache/kafka/connect/transforms/field/SingleFieldPath.java`** -> AI Confidence: **99.31%**
99. **`core/src/main/java/kafka/server/logger/RuntimeLoggerManager.java`** -> AI Confidence: **99.31%**
100. **`core/src/main/java/kafka/server/share/SharePartition.java`** -> AI Confidence: **99.31%**
101. **`generator/src/main/java/org/apache/kafka/message/ApiMessageTypeGenerator.java`** -> AI Confidence: **99.31%**
102. **`generator/src/main/java/org/apache/kafka/message/FieldSpec.java`** -> AI Confidence: **99.31%**
103. **`generator/src/main/java/org/apache/kafka/message/MessageDataGenerator.java`** -> AI Confidence: **99.31%**
104. **`generator/src/main/java/org/apache/kafka/message/checker/MetadataSchemaCheckerTool.java`** -> AI Confidence: **99.31%**
105. **`generator/src/test/java/org/apache/kafka/message/checker/MetadataSchemaCheckerToolTest.java`** -> AI Confidence: **99.31%**
106. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/assignor/SimpleHeterogeneousAssignmentBuilder.java`** -> AI Confidence: **99.31%**
107. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/assignor/SimpleHomogeneousAssignmentBuilder.java`** -> AI Confidence: **99.31%**
108. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/assignor/UniformHomogeneousAssignmentBuilder.java`** -> AI Confidence: **99.31%**
109. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/assignor/StickyTaskAssignor.java`** -> AI Confidence: **99.31%**
110. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/topics/InternalTopicManager.java`** -> AI Confidence: **99.31%**
111. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/topics/RepartitionTopics.java`** -> AI Confidence: **99.31%**
112. **`group-coordinator/src/test/java/org/apache/kafka/coordinator/group/Assertions.java`** -> AI Confidence: **99.31%**
113. **`jmh-benchmarks/src/main/java/org/apache/kafka/jmh/util/ByteUtilsBenchmark.java`** -> AI Confidence: **99.31%**
114. **`jmh-benchmarks/src/main/java/org/apache/kafka/jmh/util/ConcurrentMapBenchmark.java`** -> AI Confidence: **99.31%**
115. **`metadata/src/main/java/org/apache/kafka/controller/BrokersToElrs.java`** -> AI Confidence: **99.31%**
116. **`metadata/src/main/java/org/apache/kafka/controller/BrokersToIsrs.java`** -> AI Confidence: **99.31%**
117. **`metadata/src/main/java/org/apache/kafka/controller/metrics/ControllerMetadataMetricsPublisher.java`** -> AI Confidence: **99.31%**
118. **`metadata/src/main/java/org/apache/kafka/image/ScramImage.java`** -> AI Confidence: **99.31%**
119. **`metadata/src/main/java/org/apache/kafka/image/loader/MetadataBatchLoader.java`** -> AI Confidence: **99.31%**
120. **`metadata/src/main/java/org/apache/kafka/image/node/ClientQuotasImageNode.java`** -> AI Confidence: **99.31%**
121. **`metadata/src/main/java/org/apache/kafka/metadata/placement/StripedReplicaPlacer.java`** -> AI Confidence: **99.31%**
122. **`metadata/src/test/java/org/apache/kafka/image/loader/metrics/MetadataLoaderMetricsTest.java`** -> AI Confidence: **99.31%**
123. **`raft/src/main/java/org/apache/kafka/raft/KafkaRaftClient.java`** -> AI Confidence: **99.31%**
124. **`raft/src/main/java/org/apache/kafka/raft/internals/AddVoterHandler.java`** -> AI Confidence: **99.31%**
125. **`raft/src/test/java/org/apache/kafka/raft/DynamicVoterTest.java`** -> AI Confidence: **99.31%**
126. **`raft/src/test/java/org/apache/kafka/raft/DynamicVotersTest.java`** -> AI Confidence: **99.31%**
127. **`server-common/src/main/java/org/apache/kafka/deferred/DeferredEventQueue.java`** -> AI Confidence: **99.31%**
128. **`server-common/src/main/java/org/apache/kafka/queue/KafkaEventQueue.java`** -> AI Confidence: **99.31%**
129. **`server-common/src/main/java/org/apache/kafka/server/share/persister/DefaultStatePersister.java`** -> AI Confidence: **99.31%**
130. **`server/src/main/java/org/apache/kafka/server/DynamicThreadPool.java`** -> AI Confidence: **99.31%**
131. **`storage/src/main/java/org/apache/kafka/storage/internals/epoch/LeaderEpochFileCache.java`** -> AI Confidence: **99.31%**
132. **`streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/IQv2StoreIntegrationTest.java`** -> AI Confidence: **99.31%**
133. **`streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/KTableKTableForeignKeyJoinIntegrationTest.java`** -> AI Confidence: **99.31%**
134. **`streams/src/main/java/org/apache/kafka/streams/kstream/KStream.java`** -> AI Confidence: **99.31%**
135. **`streams/src/main/java/org/apache/kafka/streams/kstream/KTable.java`** -> AI Confidence: **99.31%**
136. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/ChangedSerializer.java`** -> AI Confidence: **99.31%**
137. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/CogroupedStreamAggregateBuilder.java`** -> AI Confidence: **99.31%**
138. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/InternalStreamsBuilder.java`** -> AI Confidence: **99.31%**
139. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamKTableJoin.java`** -> AI Confidence: **99.31%**
140. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KTableImpl.java`** -> AI Confidence: **99.31%**
141. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KTableRepartitionMap.java`** -> AI Confidence: **99.31%**
142. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/foreignkeyjoin/CombinedKeySchema.java`** -> AI Confidence: **99.31%**
143. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/foreignkeyjoin/SubscriptionWrapperSerde.java`** -> AI Confidence: **99.31%**
144. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/graph/KTableKTableJoinNode.java`** -> AI Confidence: **99.31%**
145. **`streams/src/main/java/org/apache/kafka/streams/processor/assignment/TaskAssignmentUtils.java`** -> AI Confidence: **99.31%**
146. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/DefaultStateUpdater.java`** -> AI Confidence: **99.31%**
147. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/GlobalStateManagerImpl.java`** -> AI Confidence: **99.31%**
148. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/InternalTopicManager.java`** -> AI Confidence: **99.31%**
149. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/ProcessorNode.java`** -> AI Confidence: **99.31%**
150. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/ProcessorStateManager.java`** -> AI Confidence: **99.31%**
151. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/ProcessorTopology.java`** -> AI Confidence: **99.31%**
152. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RepartitionTopics.java`** -> AI Confidence: **99.31%**
153. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StandbyTask.java`** -> AI Confidence: **99.31%**
154. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreChangelogReader.java`** -> AI Confidence: **99.31%**
155. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StreamTask.java`** -> AI Confidence: **99.31%**
156. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StreamsRebalanceListener.java`** -> AI Confidence: **99.31%**
157. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/TaskExecutor.java`** -> AI Confidence: **99.31%**
158. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/TaskManager.java`** -> AI Confidence: **99.31%**
159. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/AssignmentInfo.java`** -> AI Confidence: **99.31%**
160. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/BalanceSubtopologyGraphConstructor.java`** -> AI Confidence: **99.31%**
161. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/ClientTagAwareStandbyTaskAssignor.java`** -> AI Confidence: **99.31%**
162. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/ConsumerProtocolUtils.java`** -> AI Confidence: **99.31%**
163. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/Graph.java`** -> AI Confidence: **99.31%**
164. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/HighAvailabilityTaskAssignor.java`** -> AI Confidence: **99.31%**
165. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/RackAwareGraphConstructor.java`** -> AI Confidence: **99.31%**
166. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/RackUtils.java`** -> AI Confidence: **99.31%**
167. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/tasks/DefaultTaskExecutor.java`** -> AI Confidence: **99.31%**
168. **`streams/src/main/java/org/apache/kafka/streams/state/internals/ChangeLoggingTimestampedKeyValueBytesStoreWithHeaders.java`** -> AI Confidence: **99.31%**
169. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CompositeReadOnlySessionStore.java`** -> AI Confidence: **99.31%**
170. **`streams/src/main/java/org/apache/kafka/streams/state/internals/DualColumnFamilyAccessor.java`** -> AI Confidence: **99.31%**
171. **`streams/src/main/java/org/apache/kafka/streams/state/internals/LegacyCheckpointingStateStore.java`** -> AI Confidence: **99.31%**
172. **`streams/src/main/java/org/apache/kafka/streams/state/internals/StreamThreadStateStoreProvider.java`** -> AI Confidence: **99.31%**
173. **`streams/src/test/java/org/apache/kafka/streams/TopologyTest.java`** -> AI Confidence: **99.31%**
174. **`streams/src/test/java/org/apache/kafka/streams/kstream/internals/CogroupedKStreamImplTest.java`** -> AI Confidence: **99.31%**
175. **`streams/src/test/java/org/apache/kafka/streams/kstream/internals/KStreamKStreamJoinTest.java`** -> AI Confidence: **99.31%**
176. **`streams/src/test/java/org/apache/kafka/streams/kstream/internals/SuppressTopologyTest.java`** -> AI Confidence: **99.31%**
177. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/RepartitionOptimizingTest.java`** -> AI Confidence: **99.31%**
178. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/RepartitionWithMergeOptimizingTest.java`** -> AI Confidence: **99.31%**
179. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/assignment/RackAwareGraphConstructorTest.java`** -> AI Confidence: **99.31%**
180. **`streams/src/test/java/org/apache/kafka/streams/state/internals/RocksDBGenericOptionsToDbOptionsColumnFamilyOptionsAdapterTest.java`** -> AI Confidence: **99.31%**
181. **`streams/src/test/java/org/apache/kafka/streams/state/internals/RocksDBRangeIteratorTest.java`** -> AI Confidence: **99.31%**
182. **`streams/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
183. **`streams/test-utils/src/test/java/org/apache/kafka/streams/test/MockProcessorContextStateStoreTest.java`** -> AI Confidence: **99.31%**
184. **`streams/upgrade-system-tests-22/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.31%**
185. **`streams/upgrade-system-tests-22/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
186. **`streams/upgrade-system-tests-23/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.31%**
187. **`streams/upgrade-system-tests-23/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
188. **`streams/upgrade-system-tests-24/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
189. **`streams/upgrade-system-tests-25/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
190. **`streams/upgrade-system-tests-26/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
191. **`streams/upgrade-system-tests-27/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
192. **`streams/upgrade-system-tests-28/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
193. **`streams/upgrade-system-tests-30/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
194. **`streams/upgrade-system-tests-31/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
195. **`streams/upgrade-system-tests-32/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
196. **`streams/upgrade-system-tests-33/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
197. **`streams/upgrade-system-tests-34/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
198. **`streams/upgrade-system-tests-35/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
199. **`streams/upgrade-system-tests-36/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
200. **`streams/upgrade-system-tests-37/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
201. **`streams/upgrade-system-tests-38/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
202. **`streams/upgrade-system-tests-39/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
203. **`streams/upgrade-system-tests-40/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
204. **`streams/upgrade-system-tests-41/src/test/java/org/apache/kafka/streams/tests/StreamsSmokeTest.java`** -> AI Confidence: **99.31%**
205. **`tools/src/main/java/org/apache/kafka/tools/AclCommand.java`** -> AI Confidence: **99.31%**
206. **`tools/src/main/java/org/apache/kafka/tools/ClusterTool.java`** -> AI Confidence: **99.31%**
207. **`tools/src/main/java/org/apache/kafka/tools/ConnectPluginPath.java`** -> AI Confidence: **99.31%**
208. **`tools/src/main/java/org/apache/kafka/tools/FeatureCommand.java`** -> AI Confidence: **99.31%**
209. **`tools/src/main/java/org/apache/kafka/tools/GetOffsetShell.java`** -> AI Confidence: **99.31%**
210. **`tools/src/main/java/org/apache/kafka/tools/JmxTool.java`** -> AI Confidence: **99.31%**
211. **`tools/src/main/java/org/apache/kafka/tools/LineMessageReader.java`** -> AI Confidence: **99.31%**
212. **`tools/src/main/java/org/apache/kafka/tools/MetadataQuorumCommand.java`** -> AI Confidence: **99.31%**
213. **`tools/src/main/java/org/apache/kafka/tools/StreamsResetter.java`** -> AI Confidence: **99.31%**
214. **`tools/src/main/java/org/apache/kafka/tools/ToolsUtils.java`** -> AI Confidence: **99.31%**
215. **`tools/src/main/java/org/apache/kafka/tools/consumer/ConsoleConsumerOptions.java`** -> AI Confidence: **99.31%**
216. **`tools/src/main/java/org/apache/kafka/tools/consumer/ConsoleShareConsumerOptions.java`** -> AI Confidence: **99.31%**
217. **`tools/src/main/java/org/apache/kafka/tools/consumer/DefaultMessageFormatter.java`** -> AI Confidence: **99.31%**
218. **`tools/src/main/java/org/apache/kafka/tools/consumer/group/ShareGroupCommand.java`** -> AI Confidence: **99.31%**
219. **`tools/src/main/java/org/apache/kafka/tools/streams/StreamsGroupCommand.java`** -> AI Confidence: **99.31%**
220. **`tools/src/test/java/org/apache/kafka/tools/DelegationTokenCommandTest.java`** -> AI Confidence: **99.31%**
221. **`tools/src/test/java/org/apache/kafka/tools/DeleteRecordsCommandTest.java`** -> AI Confidence: **99.31%**
222. **`tools/src/test/java/org/apache/kafka/tools/MetadataQuorumCommandTest.java`** -> AI Confidence: **99.31%**
223. **`tools/src/test/java/org/apache/kafka/tools/consumer/group/share/ShareGroupStateMessageFormatterTest.java`** -> AI Confidence: **99.31%**
224. **`trogdor/src/main/java/org/apache/kafka/trogdor/agent/WorkerManager.java`** -> AI Confidence: **99.31%**
225. **`trogdor/src/main/java/org/apache/kafka/trogdor/rest/RestExceptionMapper.java`** -> AI Confidence: **99.31%**
226. **`trogdor/src/main/java/org/apache/kafka/trogdor/workload/ExternalCommandWorker.java`** -> AI Confidence: **99.31%**
227. **`trogdor/src/main/java/org/apache/kafka/trogdor/workload/PartitionsSpec.java`** -> AI Confidence: **99.31%**
228. **`core/src/main/scala/kafka/Kafka.scala`** -> AI Confidence: **99.31%**
229. **`core/src/main/scala/kafka/admin/ConfigCommand.scala`** -> AI Confidence: **99.31%**
230. **`core/src/main/scala/kafka/cluster/Partition.scala`** -> AI Confidence: **99.31%**
231. **`core/src/main/scala/kafka/coordinator/transaction/TransactionStateManager.scala`** -> AI Confidence: **99.31%**
232. **`core/src/main/scala/kafka/docker/KafkaDockerWrapper.scala`** -> AI Confidence: **99.31%**
233. **`core/src/main/scala/kafka/server/AbstractFetcherManager.scala`** -> AI Confidence: **99.31%**
234. **`core/src/main/scala/kafka/server/AutoTopicCreationManager.scala`** -> AI Confidence: **99.31%**
235. **`core/src/main/scala/kafka/server/ConfigAdminManager.scala`** -> AI Confidence: **99.31%**
236. **`core/src/main/scala/kafka/server/ConfigHandler.scala`** -> AI Confidence: **99.31%**
237. **`core/src/main/scala/kafka/server/ConfigHelper.scala`** -> AI Confidence: **99.31%**
238. **`core/src/main/scala/kafka/server/ControllerApis.scala`** -> AI Confidence: **99.31%**
239. **`core/src/main/scala/kafka/server/ControllerConfigurationValidator.scala`** -> AI Confidence: **99.31%**
240. **`core/src/main/scala/kafka/server/DelayedFetch.scala`** -> AI Confidence: **99.31%**
241. **`core/src/main/scala/kafka/server/DynamicBrokerConfig.scala`** -> AI Confidence: **99.31%**
242. **`core/src/main/scala/kafka/server/EnvelopeUtils.scala`** -> AI Confidence: **99.31%**
243. **`core/src/main/scala/kafka/server/KafkaApis.scala`** -> AI Confidence: **99.31%**
244. **`core/src/main/scala/kafka/server/LocalLeaderEndPoint.scala`** -> AI Confidence: **99.31%**
245. **`core/src/main/scala/kafka/server/RemoteLeaderEndPoint.scala`** -> AI Confidence: **99.31%**
246. **`core/src/main/scala/kafka/server/ReplicaAlterLogDirsThread.scala`** -> AI Confidence: **99.31%**
247. **`core/src/main/scala/kafka/server/ReplicaFetcherThread.scala`** -> AI Confidence: **99.31%**
248. **`core/src/main/scala/kafka/server/RequestHandlerHelper.scala`** -> AI Confidence: **99.31%**
249. **`core/src/main/scala/kafka/server/metadata/BrokerMetadataPublisher.scala`** -> AI Confidence: **99.31%**
250. **`core/src/main/scala/kafka/server/metadata/ClientQuotaMetadataManager.scala`** -> AI Confidence: **99.31%**
251. **`core/src/test/scala/integration/kafka/api/BaseProducerSendTest.scala`** -> AI Confidence: **99.31%**
252. **`core/src/test/scala/integration/kafka/api/BaseQuotaTest.scala`** -> AI Confidence: **99.31%**
253. **`core/src/test/scala/integration/kafka/api/PlaintextConsumerAssignorsTest.scala`** -> AI Confidence: **99.31%**
254. **`core/src/test/scala/unit/kafka/server/AbstractApiVersionsRequestTest.scala`** -> AI Confidence: **99.31%**
255. **`core/src/test/scala/unit/kafka/server/AbstractCreateTopicsRequestTest.scala`** -> AI Confidence: **99.31%**
256. **`core/src/test/scala/unit/kafka/server/LeaveGroupRequestTest.scala`** -> AI Confidence: **99.31%**
257. **`core/src/test/scala/unit/kafka/server/MockFetcherThread.scala`** -> AI Confidence: **99.31%**
258. **`core/src/test/scala/unit/kafka/server/MockLeaderEndPoint.scala`** -> AI Confidence: **99.31%**
259. **`core/src/test/scala/unit/kafka/server/MockNodeToControllerChannelManager.scala`** -> AI Confidence: **99.31%**
260. **`core/src/test/scala/unit/kafka/server/OffsetCommitRequestTest.scala`** -> AI Confidence: **99.31%**
261. **`core/src/test/scala/unit/kafka/server/TxnOffsetCommitRequestTest.scala`** -> AI Confidence: **99.31%**
262. **`core/src/test/scala/unit/kafka/server/WriteTxnMarkersRequestTest.scala`** -> AI Confidence: **99.31%**
263. **`bin/kafka-run-class.sh`** -> AI Confidence: **99.29%**
264. **`jmh-benchmarks/jmh.sh`** -> AI Confidence: **99.29%**
265. **`Vagrantfile`** -> AI Confidence: **99.29%**
266. **`tests/docker/Dockerfile`** -> AI Confidence: **99.29%**
267. **`gradle/dependencies.gradle`** -> AI Confidence: **99.29%**
268. **`settings.gradle`** -> AI Confidence: **99.29%**
269. **`wrapper.gradle`** -> AI Confidence: **99.29%**
270. **`clients/src/main/java/org/apache/kafka/clients/NetworkClient.java`** -> AI Confidence: **99.25%**
271. **`clients/src/main/java/org/apache/kafka/clients/consumer/ConsumerConfig.java`** -> AI Confidence: **99.25%**
272. **`clients/src/main/java/org/apache/kafka/clients/producer/ProducerConfig.java`** -> AI Confidence: **99.25%**
273. **`clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java`** -> AI Confidence: **99.25%**
274. **`clients/src/main/java/org/apache/kafka/server/authorizer/Authorizer.java`** -> AI Confidence: **99.25%**
275. **`server-common/src/main/java/org/apache/kafka/server/common/MetadataVersion.java`** -> AI Confidence: **99.25%**
276. **`server-common/src/main/java/org/apache/kafka/server/config/QuotaConfig.java`** -> AI Confidence: **99.25%**
277. **`server-common/src/main/java/org/apache/kafka/server/purgatory/DelayedOperationPurgatory.java`** -> AI Confidence: **99.25%**
278. **`server-common/src/main/java/org/apache/kafka/server/share/persister/PersisterStateManager.java`** -> AI Confidence: **99.25%**
279. **`server-common/src/main/java/org/apache/kafka/server/util/CommandLineUtils.java`** -> AI Confidence: **99.25%**
280. **`server/src/main/java/org/apache/kafka/network/SocketServerConfigs.java`** -> AI Confidence: **99.25%**
281. **`test-common/test-common-internal-api/src/main/java/org/apache/kafka/common/test/api/ClusterTest.java`** -> AI Confidence: **99.25%**
282. **`core/src/main/scala/kafka/network/SocketServer.scala`** -> AI Confidence: **99.25%**
283. **`core/src/main/scala/kafka/server/KafkaConfig.scala`** -> AI Confidence: **99.25%**
284. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/MetricsDuringTopicCreationDeletionTest.java`** -> AI Confidence: **99.24%**
285. **`clients/src/main/java/org/apache/kafka/clients/ClientUtils.java`** -> AI Confidence: **99.24%**
286. **`clients/src/main/java/org/apache/kafka/clients/Metadata.java`** -> AI Confidence: **99.24%**
287. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/AbortTransactionHandler.java`** -> AI Confidence: **99.24%**
288. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/CoordinatorStrategy.java`** -> AI Confidence: **99.24%**
289. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DeleteConsumerGroupOffsetsHandler.java`** -> AI Confidence: **99.24%**
290. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeConsumerGroupsHandler.java`** -> AI Confidence: **99.24%**
291. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeProducersHandler.java`** -> AI Confidence: **99.24%**
292. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeStreamsGroupsHandler.java`** -> AI Confidence: **99.24%**
293. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeTransactionsHandler.java`** -> AI Confidence: **99.24%**
294. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/FenceProducersHandler.java`** -> AI Confidence: **99.24%**
295. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/ListConsumerGroupOffsetsHandler.java`** -> AI Confidence: **99.24%**
296. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/ListShareGroupOffsetsHandler.java`** -> AI Confidence: **99.24%**
297. **`clients/src/main/java/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.java`** -> AI Confidence: **99.24%**
298. **`clients/src/main/java/org/apache/kafka/clients/consumer/RangeAssignor.java`** -> AI Confidence: **99.24%**
299. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/AutoOffsetResetStrategy.java`** -> AI Confidence: **99.24%**
300. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerCoordinator.java`** -> AI Confidence: **99.24%**
301. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/FetchBuffer.java`** -> AI Confidence: **99.24%**
302. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/OffsetsRequestManager.java`** -> AI Confidence: **99.24%**
303. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/TopicMetadataFetcher.java`** -> AI Confidence: **99.24%**
304. **`clients/src/main/java/org/apache/kafka/common/config/AbstractConfig.java`** -> AI Confidence: **99.24%**
305. **`clients/src/main/java/org/apache/kafka/common/config/internals/BrokerSecurityConfigs.java`** -> AI Confidence: **99.24%**
306. **`clients/src/main/java/org/apache/kafka/common/metrics/internals/IntGaugeSuite.java`** -> AI Confidence: **99.24%**
307. **`clients/src/main/java/org/apache/kafka/common/network/SaslChannelBuilder.java`** -> AI Confidence: **99.24%**
308. **`clients/src/main/java/org/apache/kafka/common/protocol/Errors.java`** -> AI Confidence: **99.24%**
309. **`clients/src/main/java/org/apache/kafka/common/record/internal/ControlRecordType.java`** -> AI Confidence: **99.24%**
310. **`clients/src/main/java/org/apache/kafka/common/record/internal/DefaultRecord.java`** -> AI Confidence: **99.24%**
311. **`clients/src/main/java/org/apache/kafka/common/record/internal/LegacyRecord.java`** -> AI Confidence: **99.24%**
312. **`clients/src/main/java/org/apache/kafka/common/record/internal/MultiRecordsSend.java`** -> AI Confidence: **99.24%**
313. **`clients/src/main/java/org/apache/kafka/common/security/JaasConfig.java`** -> AI Confidence: **99.24%**
314. **`clients/src/main/java/org/apache/kafka/common/security/authenticator/SaslClientCallbackHandler.java`** -> AI Confidence: **99.24%**
315. **`clients/src/main/java/org/apache/kafka/common/security/kerberos/KerberosClientCallbackHandler.java`** -> AI Confidence: **99.24%**
316. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/OAuthBearerLoginModule.java`** -> AI Confidence: **99.24%**
317. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/expiring/ExpiringCredentialRefreshingLogin.java`** -> AI Confidence: **99.24%**
318. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/ConfigurationUtils.java`** -> AI Confidence: **99.24%**
319. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/RefreshingHttpsJwks.java`** -> AI Confidence: **99.24%**
320. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/unsecured/OAuthBearerUnsecuredValidatorCallbackHandler.java`** -> AI Confidence: **99.24%**
321. **`clients/src/main/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactory.java`** -> AI Confidence: **99.24%**
322. **`clients/src/main/java/org/apache/kafka/common/serialization/ListDeserializer.java`** -> AI Confidence: **99.24%**
323. **`clients/src/main/java/org/apache/kafka/common/serialization/ListSerializer.java`** -> AI Confidence: **99.24%**
324. **`clients/src/main/java/org/apache/kafka/common/serialization/UUIDDeserializer.java`** -> AI Confidence: **99.24%**
325. **`clients/src/main/java/org/apache/kafka/common/utils/SecurityUtils.java`** -> AI Confidence: **99.24%**
326. **`clients/src/main/java/org/apache/kafka/common/utils/Utils.java`** -> AI Confidence: **99.24%**
327. **`clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java`** -> AI Confidence: **99.24%**
328. **`clients/src/test/java/org/apache/kafka/clients/consumer/internals/ConsumerHeartbeatRequestManagerTest.java`** -> AI Confidence: **99.24%**
329. **`clients/src/test/java/org/apache/kafka/common/message/ApiMessageTypeTest.java`** -> AI Confidence: **99.24%**
330. **`clients/src/test/java/org/apache/kafka/common/network/EchoServer.java`** -> AI Confidence: **99.24%**
331. **`clients/src/test/java/org/apache/kafka/common/protocol/ApiKeysTest.java`** -> AI Confidence: **99.24%**
332. **`clients/src/test/java/org/apache/kafka/common/security/authenticator/TestDigestLoginModule.java`** -> AI Confidence: **99.24%**
333. **`clients/src/test/java/org/apache/kafka/common/security/oauthbearer/internals/secured/CachedFileTest.java`** -> AI Confidence: **99.24%**
334. **`clients/src/test/java/org/apache/kafka/common/security/oauthbearer/internals/unsecured/OAuthBearerUnsecuredJwsTest.java`** -> AI Confidence: **99.24%**
335. **`clients/src/test/java/org/apache/kafka/common/utils/annotation/ApiKeyVersionsProviderTest.java`** -> AI Confidence: **99.24%**
336. **`connect/basic-auth-extension/src/main/java/org/apache/kafka/connect/rest/basic/auth/extension/PropertyFileLoginModule.java`** -> AI Confidence: **99.24%**
337. **`connect/json/src/main/java/org/apache/kafka/connect/json/JsonConverterConfig.java`** -> AI Confidence: **99.24%**
338. **`connect/mirror/src/main/java/org/apache/kafka/connect/mirror/CheckpointStore.java`** -> AI Confidence: **99.24%**
339. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/SourceTaskOffsetCommitter.java`** -> AI Confidence: **99.24%**
340. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/WorkerConnector.java`** -> AI Confidence: **99.24%**
341. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/WorkerSinkTask.java`** -> AI Confidence: **99.24%**
342. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedConfig.java`** -> AI Confidence: **99.24%**
343. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/errors/RetryWithToleranceOperator.java`** -> AI Confidence: **99.24%**
344. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/isolation/ReflectionScanner.java`** -> AI Confidence: **99.24%**
345. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/RestClient.java`** -> AI Confidence: **99.24%**
346. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/RestServer.java`** -> AI Confidence: **99.24%**
347. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/util/SSLUtils.java`** -> AI Confidence: **99.24%**
348. **`connect/runtime/src/main/java/org/apache/kafka/connect/storage/OffsetStorageWriter.java`** -> AI Confidence: **99.24%**
349. **`connect/runtime/src/main/java/org/apache/kafka/connect/util/RetryUtil.java`** -> AI Confidence: **99.24%**
350. **`connect/runtime/src/test/java/org/apache/kafka/connect/integration/BlockingConnectorTest.java`** -> AI Confidence: **99.24%**
351. **`connect/runtime/src/test/java/org/apache/kafka/connect/integration/ConnectorTopicsIntegrationTest.java`** -> AI Confidence: **99.24%**
352. **`connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java`** -> AI Confidence: **99.24%**
353. **`connect/runtime/src/test/java/org/apache/kafka/connect/runtime/isolation/TestPlugins.java`** -> AI Confidence: **99.24%**
354. **`connect/runtime/src/test/java/org/apache/kafka/connect/util/clusters/EmbeddedConnect.java`** -> AI Confidence: **99.24%**
355. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorLoaderImpl.java`** -> AI Confidence: **99.24%**
356. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorRuntime.java`** -> AI Confidence: **99.24%**
357. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorRuntimeMetricsImpl.java`** -> AI Confidence: **99.24%**
358. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/MultiThreadedEventProcessor.java`** -> AI Confidence: **99.24%**
359. **`coordinator-common/src/test/java/org/apache/kafka/coordinator/common/runtime/DeferredEventCollectionTest.java`** -> AI Confidence: **99.24%**
360. **`core/src/main/java/kafka/server/share/DelayedShareFetch.java`** -> AI Confidence: **99.24%**
361. **`examples/src/main/java/kafka/examples/TransactionalClientDemo.java`** -> AI Confidence: **99.24%**
362. **`generator/src/main/java/org/apache/kafka/message/MessageGenerator.java`** -> AI Confidence: **99.24%**
363. **`generator/src/test/java/org/apache/kafka/message/MessageGeneratorTest.java`** -> AI Confidence: **99.24%**
364. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupConfig.java`** -> AI Confidence: **99.24%**
365. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java`** -> AI Confidence: **99.24%**
366. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/Utils.java`** -> AI Confidence: **99.24%**
367. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/modern/consumer/ConsumerGroup.java`** -> AI Confidence: **99.24%**
368. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/modern/consumer/CurrentAssignmentBuilder.java`** -> AI Confidence: **99.24%**
369. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/CurrentAssignmentBuilder.java`** -> AI Confidence: **99.24%**
370. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/StreamsTopology.java`** -> AI Confidence: **99.24%**
371. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/topics/ChangelogTopics.java`** -> AI Confidence: **99.24%**
372. **`jmh-benchmarks/src/main/java/org/apache/kafka/jmh/connect/ValuesBenchmark.java`** -> AI Confidence: **99.24%**
373. **`metadata/src/main/java/org/apache/kafka/controller/AclControlManager.java`** -> AI Confidence: **99.24%**
374. **`metadata/src/main/java/org/apache/kafka/controller/ClientQuotaControlManager.java`** -> AI Confidence: **99.24%**
375. **`metadata/src/main/java/org/apache/kafka/controller/ConfigurationControlManager.java`** -> AI Confidence: **99.24%**
376. **`metadata/src/main/java/org/apache/kafka/controller/PeriodicTaskControlManager.java`** -> AI Confidence: **99.24%**
377. **`metadata/src/main/java/org/apache/kafka/image/ClientQuotasImage.java`** -> AI Confidence: **99.24%**
378. **`metadata/src/main/java/org/apache/kafka/image/MetadataDelta.java`** -> AI Confidence: **99.24%**
379. **`metadata/src/main/java/org/apache/kafka/image/loader/MetadataLoader.java`** -> AI Confidence: **99.24%**
380. **`metadata/src/main/java/org/apache/kafka/image/publisher/BrokerRegistrationTracker.java`** -> AI Confidence: **99.24%**
381. **`metadata/src/main/java/org/apache/kafka/metadata/KafkaConfigSchema.java`** -> AI Confidence: **99.24%**
382. **`metadata/src/main/java/org/apache/kafka/metadata/authorizer/StandardAuthorizerData.java`** -> AI Confidence: **99.24%**
383. **`metadata/src/main/java/org/apache/kafka/metadata/storage/ScramParser.java`** -> AI Confidence: **99.24%**
384. **`metadata/src/test/java/org/apache/kafka/controller/metrics/ControllerMetadataMetricsTest.java`** -> AI Confidence: **99.24%**
385. **`metadata/src/test/java/org/apache/kafka/metadata/RecordTestUtils.java`** -> AI Confidence: **99.24%**
386. **`raft/src/main/java/org/apache/kafka/raft/ControlRecord.java`** -> AI Confidence: **99.24%**
387. **`raft/src/main/java/org/apache/kafka/raft/ElectionState.java`** -> AI Confidence: **99.24%**
388. **`raft/src/main/java/org/apache/kafka/raft/QuorumState.java`** -> AI Confidence: **99.24%**
389. **`raft/src/main/java/org/apache/kafka/raft/internals/RecordsIterator.java`** -> AI Confidence: **99.24%**
390. **`raft/src/main/java/org/apache/kafka/raft/internals/RemoveVoterHandler.java`** -> AI Confidence: **99.24%**
391. **`raft/src/test/java/org/apache/kafka/raft/ReplicatedCounter.java`** -> AI Confidence: **99.24%**
392. **`server-common/src/main/java/org/apache/kafka/server/network/EndpointReadyFutures.java`** -> AI Confidence: **99.24%**
393. **`server/src/main/java/org/apache/kafka/server/config/ReplicationConfigs.java`** -> AI Confidence: **99.24%**
394. **`server/src/main/java/org/apache/kafka/server/controller/ControllerRegistrationManager.java`** -> AI Confidence: **99.24%**
395. **`server/src/test/java/org/apache/kafka/server/metrics/ForwardingManagerMetricsTest.java`** -> AI Confidence: **99.24%**
396. **`storage/src/test/java/org/apache/kafka/tiered/storage/actions/ConsumeAction.java`** -> AI Confidence: **99.24%**
397. **`streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/KTableEfficientRangeQueryTest.java`** -> AI Confidence: **99.24%**
398. **`streams/src/main/java/org/apache/kafka/streams/kstream/TimeWindowedDeserializer.java`** -> AI Confidence: **99.24%**
399. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamImpl.java`** -> AI Confidence: **99.24%**
400. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamImplJoin.java`** -> AI Confidence: **99.24%**
401. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KeyValueStoreMaterializer.java`** -> AI Confidence: **99.24%**
402. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/StreamJoinedStoreFactory.java`** -> AI Confidence: **99.24%**
403. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/foreignkeyjoin/SubscriptionJoinProcessorSupplier.java`** -> AI Confidence: **99.24%**
404. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/graph/StreamSourceNode.java`** -> AI Confidence: **99.24%**
405. **`streams/src/main/java/org/apache/kafka/streams/processor/assignment/assignors/StickyTaskAssignor.java`** -> AI Confidence: **99.24%**
406. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/ChangelogTopics.java`** -> AI Confidence: **99.24%**
407. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/GlobalStreamThread.java`** -> AI Confidence: **99.24%**
408. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/PartitionGroup.java`** -> AI Confidence: **99.24%**
409. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RecordCollectorImpl.java`** -> AI Confidence: **99.24%**
410. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RecordDeserializer.java`** -> AI Confidence: **99.24%**
411. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RecordQueue.java`** -> AI Confidence: **99.24%**
412. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/SinkNode.java`** -> AI Confidence: **99.24%**
413. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StateDirectory.java`** -> AI Confidence: **99.24%**
414. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StreamsPartitionAssignor.java`** -> AI Confidence: **99.24%**
415. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/TaskExecutionMetadata.java`** -> AI Confidence: **99.24%**
416. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/Tasks.java`** -> AI Confidence: **99.24%**
417. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/LegacyStickyTaskAssignor.java`** -> AI Confidence: **99.24%**
418. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/MinTrafficGraphConstructor.java`** -> AI Confidence: **99.24%**
419. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/TaskMovement.java`** -> AI Confidence: **99.24%**
420. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/tasks/DefaultTaskManager.java`** -> AI Confidence: **99.24%**
421. **`streams/src/main/java/org/apache/kafka/streams/query/Position.java`** -> AI Confidence: **99.24%**
422. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CachingKeyValueStore.java`** -> AI Confidence: **99.24%**
423. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CachingSessionStore.java`** -> AI Confidence: **99.24%**
424. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CachingWindowStore.java`** -> AI Confidence: **99.24%**
425. **`streams/src/main/java/org/apache/kafka/streams/state/internals/InMemoryWindowStore.java`** -> AI Confidence: **99.24%**
426. **`streams/src/main/java/org/apache/kafka/streams/state/internals/LogicalSegmentIterator.java`** -> AI Confidence: **99.24%**
427. **`streams/src/main/java/org/apache/kafka/streams/state/internals/MeteredWindowStore.java`** -> AI Confidence: **99.24%**
428. **`streams/src/main/java/org/apache/kafka/streams/state/internals/PositionSerde.java`** -> AI Confidence: **99.24%**
429. **`streams/src/main/java/org/apache/kafka/streams/state/internals/RocksDBTimeOrderedWindowStore.java`** -> AI Confidence: **99.24%**
430. **`streams/src/main/java/org/apache/kafka/streams/state/internals/WrappedStateStore.java`** -> AI Confidence: **99.24%**
431. **`streams/src/test/java/org/apache/kafka/streams/internals/ApiUtilsTest.java`** -> AI Confidence: **99.24%**
432. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/NamedTopologyTest.java`** -> AI Confidence: **99.24%**
433. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/ReadOnlyTaskTest.java`** -> AI Confidence: **99.24%**
434. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/StateManagerUtilConverterTest.java`** -> AI Confidence: **99.24%**
435. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/StateManagerUtilTest.java`** -> AI Confidence: **99.24%**
436. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/assignment/TaskMovementTest.java`** -> AI Confidence: **99.24%**
437. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/metrics/RebalanceListenerMetricsTest.java`** -> AI Confidence: **99.24%**
438. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/metrics/TaskMetricsTest.java`** -> AI Confidence: **99.24%**
439. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/metrics/ThreadMetricsTest.java`** -> AI Confidence: **99.24%**
440. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/tasks/DefaultTaskExecutorTest.java`** -> AI Confidence: **99.24%**
441. **`streams/src/test/java/org/apache/kafka/streams/state/internals/SessionStoreFetchTest.java`** -> AI Confidence: **99.24%**
442. **`streams/src/test/java/org/apache/kafka/streams/state/internals/metrics/RocksDBMetricsTest.java`** -> AI Confidence: **99.24%**
443. **`streams/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
444. **`streams/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
445. **`streams/src/test/java/org/apache/kafka/test/MockApiProcessor.java`** -> AI Confidence: **99.24%**
446. **`streams/upgrade-system-tests-24/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
447. **`streams/upgrade-system-tests-25/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
448. **`streams/upgrade-system-tests-26/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
449. **`streams/upgrade-system-tests-27/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
450. **`streams/upgrade-system-tests-28/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
451. **`streams/upgrade-system-tests-30/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
452. **`streams/upgrade-system-tests-30/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
453. **`streams/upgrade-system-tests-31/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
454. **`streams/upgrade-system-tests-31/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
455. **`streams/upgrade-system-tests-32/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
456. **`streams/upgrade-system-tests-32/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
457. **`streams/upgrade-system-tests-33/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
458. **`streams/upgrade-system-tests-33/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
459. **`streams/upgrade-system-tests-34/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
460. **`streams/upgrade-system-tests-34/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
461. **`streams/upgrade-system-tests-35/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
462. **`streams/upgrade-system-tests-35/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
463. **`streams/upgrade-system-tests-36/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
464. **`streams/upgrade-system-tests-36/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
465. **`streams/upgrade-system-tests-37/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
466. **`streams/upgrade-system-tests-37/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
467. **`streams/upgrade-system-tests-38/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
468. **`streams/upgrade-system-tests-38/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
469. **`streams/upgrade-system-tests-39/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
470. **`streams/upgrade-system-tests-39/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
471. **`streams/upgrade-system-tests-40/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
472. **`streams/upgrade-system-tests-40/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
473. **`streams/upgrade-system-tests-41/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
474. **`streams/upgrade-system-tests-41/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
475. **`tools/src/main/java/org/apache/kafka/tools/ConsoleProducer.java`** -> AI Confidence: **99.24%**
476. **`tools/src/main/java/org/apache/kafka/tools/DelegationTokenCommand.java`** -> AI Confidence: **99.24%**
477. **`tools/src/main/java/org/apache/kafka/tools/DumpLogSegments.java`** -> AI Confidence: **99.24%**
478. **`tools/src/main/java/org/apache/kafka/tools/EndToEndLatency.java`** -> AI Confidence: **99.24%**
479. **`tools/src/main/java/org/apache/kafka/tools/GroupsCommand.java`** -> AI Confidence: **99.24%**
480. **`tools/src/main/java/org/apache/kafka/tools/LeaderElectionCommand.java`** -> AI Confidence: **99.24%**
481. **`tools/src/main/java/org/apache/kafka/tools/OffsetsUtils.java`** -> AI Confidence: **99.24%**
482. **`tools/src/main/java/org/apache/kafka/tools/ProducerPerformance.java`** -> AI Confidence: **99.24%**
483. **`tools/src/main/java/org/apache/kafka/tools/ReplicaVerificationTool.java`** -> AI Confidence: **99.24%**
484. **`tools/src/main/java/org/apache/kafka/tools/TopicCommand.java`** -> AI Confidence: **99.24%**
485. **`tools/src/main/java/org/apache/kafka/tools/consumer/ConsoleConsumer.java`** -> AI Confidence: **99.24%**
486. **`tools/src/main/java/org/apache/kafka/tools/consumer/group/ConsumerGroupCommand.java`** -> AI Confidence: **99.24%**
487. **`tools/src/main/java/org/apache/kafka/tools/reassign/ReassignPartitionsCommand.java`** -> AI Confidence: **99.24%**
488. **`tools/src/test/java/org/apache/kafka/tools/JmxToolTest.java`** -> AI Confidence: **99.24%**
489. **`tools/src/test/java/org/apache/kafka/tools/consumer/DefaultMessageFormatterTest.java`** -> AI Confidence: **99.24%**
490. **`transaction-coordinator/src/main/java/org/apache/kafka/coordinator/transaction/RPCProducerIdManager.java`** -> AI Confidence: **99.24%**
491. **`trogdor/src/main/java/org/apache/kafka/trogdor/coordinator/CoordinatorClient.java`** -> AI Confidence: **99.24%**
492. **`trogdor/src/main/java/org/apache/kafka/trogdor/coordinator/TaskManager.java`** -> AI Confidence: **99.24%**
493. **`trogdor/src/main/java/org/apache/kafka/trogdor/fault/DegradedNetworkFaultWorker.java`** -> AI Confidence: **99.24%**
494. **`core/src/main/scala/kafka/coordinator/transaction/TransactionMarkerChannelManager.scala`** -> AI Confidence: **99.24%**
495. **`core/src/main/scala/kafka/server/AlterPartitionManager.scala`** -> AI Confidence: **99.24%**
496. **`core/src/main/scala/kafka/server/AuthHelper.scala`** -> AI Confidence: **99.24%**
497. **`core/src/main/scala/kafka/server/BrokerServer.scala`** -> AI Confidence: **99.24%**
498. **`core/src/main/scala/kafka/server/KafkaRequestHandler.scala`** -> AI Confidence: **99.24%**
499. **`core/src/main/scala/kafka/tools/TestRaftRequestHandler.scala`** -> AI Confidence: **99.24%**
500. **`core/src/test/scala/integration/kafka/api/CustomQuotaCallbackTest.scala`** -> AI Confidence: **99.24%**
501. **`core/src/test/scala/integration/kafka/api/MetricsTest.scala`** -> AI Confidence: **99.24%**
502. **`core/src/test/scala/integration/kafka/api/SaslClientsWithInvalidCredentialsTest.scala`** -> AI Confidence: **99.24%**
503. **`core/src/test/scala/integration/kafka/api/TransactionsTest.scala`** -> AI Confidence: **99.24%**
504. **`core/src/test/scala/integration/kafka/network/DynamicConnectionQuotaTest.scala`** -> AI Confidence: **99.24%**
505. **`core/src/test/scala/unit/kafka/network/ConnectionQuotasTest.scala`** -> AI Confidence: **99.24%**
506. **`core/src/test/scala/unit/kafka/server/StreamsGroupHeartbeatRequestTest.scala`** -> AI Confidence: **99.24%**
507. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/AutoTopicCreationTest.java`** -> AI Confidence: **99.23%**
508. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/StreamsRebalanceListenerInvoker.java`** -> AI Confidence: **99.23%**
509. **`clients/src/main/java/org/apache/kafka/common/config/TopicConfig.java`** -> AI Confidence: **99.23%**
510. **`clients/src/main/java/org/apache/kafka/common/internals/KafkaFutureImpl.java`** -> AI Confidence: **99.23%**
511. **`clients/src/main/java/org/apache/kafka/common/protocol/types/TaggedFields.java`** -> AI Confidence: **99.23%**
512. **`clients/src/main/java/org/apache/kafka/common/requests/DescribeClientQuotasRequest.java`** -> AI Confidence: **99.23%**
513. **`clients/src/main/java/org/apache/kafka/common/security/kerberos/KerberosError.java`** -> AI Confidence: **99.23%**
514. **`clients/src/main/java/org/apache/kafka/common/utils/ByteUtils.java`** -> AI Confidence: **99.23%**
515. **`clients/src/main/java/org/apache/kafka/common/utils/ChildFirstClassLoader.java`** -> AI Confidence: **99.23%**
516. **`clients/src/main/java/org/apache/kafka/common/utils/ConfigUtils.java`** -> AI Confidence: **99.23%**
517. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/ConnectRestConfigurable.java`** -> AI Confidence: **99.23%**
518. **`metadata/src/main/java/org/apache/kafka/image/FeaturesDelta.java`** -> AI Confidence: **99.23%**
519. **`metadata/src/test/java/org/apache/kafka/controller/metrics/QuorumControllerMetricsTest.java`** -> AI Confidence: **99.23%**
520. **`raft/src/main/java/org/apache/kafka/raft/RequestManager.java`** -> AI Confidence: **99.23%**
521. **`server-common/src/main/java/org/apache/kafka/metadata/AssignmentsHelper.java`** -> AI Confidence: **99.23%**
522. **`server/src/main/java/org/apache/kafka/server/replica/Replica.java`** -> AI Confidence: **99.23%**
523. **`server/src/test/java/org/apache/kafka/network/SocketServerConfigsTest.java`** -> AI Confidence: **99.23%**
524. **`share-coordinator/src/main/java/org/apache/kafka/coordinator/share/PersisterStateBatchCombiner.java`** -> AI Confidence: **99.23%**
525. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/foreignkeyjoin/SubscriptionResponseWrapperSerde.java`** -> AI Confidence: **99.23%**
526. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/graph/StreamSinkNode.java`** -> AI Confidence: **99.23%**
527. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreBuilderWrapper.java`** -> AI Confidence: **99.23%**
528. **`trogdor/src/test/java/org/apache/kafka/trogdor/basic/BasicPlatformTest.java`** -> AI Confidence: **99.23%**
529. **`core/src/test/scala/unit/kafka/server/DelayedProduceTest.scala`** -> AI Confidence: **99.23%**
530. **`generator/src/test/java/org/apache/kafka/message/MessageDataGeneratorTest.java`** -> AI Confidence: **99.22%**
531. **`shell/src/main/java/org/apache/kafka/shell/glob/GlobComponent.java`** -> AI Confidence: **99.2%**
532. **`committer-tools/refresh_collaborators.py`** -> AI Confidence: **99.18%**
533. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/CreateTopicsRequestWithPolicyTest.java`** -> AI Confidence: **99.18%**
534. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/TransactionsExpirationTest.java`** -> AI Confidence: **99.18%**
535. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/DeleteTopicTest.java`** -> AI Confidence: **99.18%**
536. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/RackAwareAutoTopicCreationTest.java`** -> AI Confidence: **99.18%**
537. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ConsumerBounceTest.java`** -> AI Confidence: **99.18%**
538. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java`** -> AI Confidence: **99.18%**
539. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/producer/ProducerCompressionTest.java`** -> AI Confidence: **99.18%**
540. **`clients/src/main/java/org/apache/kafka/clients/admin/Admin.java`** -> AI Confidence: **99.18%**
541. **`clients/src/main/java/org/apache/kafka/clients/admin/DescribeProducersResult.java`** -> AI Confidence: **99.18%**
542. **`clients/src/main/java/org/apache/kafka/clients/admin/DescribeReplicaLogDirsResult.java`** -> AI Confidence: **99.18%**
543. **`clients/src/main/java/org/apache/kafka/clients/admin/DescribeTopicsResult.java`** -> AI Confidence: **99.18%**
544. **`clients/src/main/java/org/apache/kafka/clients/admin/ElectLeadersResult.java`** -> AI Confidence: **99.18%**
545. **`clients/src/main/java/org/apache/kafka/clients/admin/ListConsumerGroupOffsetsResult.java`** -> AI Confidence: **99.18%**
546. **`clients/src/main/java/org/apache/kafka/clients/admin/ListConsumerGroupsOptions.java`** -> AI Confidence: **99.18%**
547. **`clients/src/main/java/org/apache/kafka/clients/admin/ShareGroupDescription.java`** -> AI Confidence: **99.18%**
548. **`clients/src/main/java/org/apache/kafka/clients/admin/StreamsGroupDescription.java`** -> AI Confidence: **99.18%**
549. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/ListTransactionsHandler.java`** -> AI Confidence: **99.18%**
550. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerUtils.java`** -> AI Confidence: **99.18%**
551. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/CoordinatorRequestManager.java`** -> AI Confidence: **99.18%**
552. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/Deserializers.java`** -> AI Confidence: **99.18%**
553. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/PositionsValidator.java`** -> AI Confidence: **99.18%**
554. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/RequestFuture.java`** -> AI Confidence: **99.18%**
555. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareConsumerDelegateCreator.java`** -> AI Confidence: **99.18%**
556. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareSessionHandler.java`** -> AI Confidence: **99.18%**
557. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/ApplicationEventHandler.java`** -> AI Confidence: **99.18%**
558. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/metrics/SensorBuilder.java`** -> AI Confidence: **99.18%**
559. **`clients/src/main/java/org/apache/kafka/clients/producer/MockProducer.java`** -> AI Confidence: **99.18%**
560. **`clients/src/main/java/org/apache/kafka/clients/producer/internals/BuiltInPartitioner.java`** -> AI Confidence: **99.18%**
561. **`clients/src/main/java/org/apache/kafka/clients/producer/internals/ProducerBatch.java`** -> AI Confidence: **99.18%**
562. **`clients/src/main/java/org/apache/kafka/common/Cluster.java`** -> AI Confidence: **99.18%**
563. **`clients/src/main/java/org/apache/kafka/common/config/provider/FileConfigProvider.java`** -> AI Confidence: **99.18%**
564. **`clients/src/main/java/org/apache/kafka/common/internals/LegacyStrategy.java`** -> AI Confidence: **99.18%**
565. **`clients/src/main/java/org/apache/kafka/common/memory/GarbageCollectedMemoryPool.java`** -> AI Confidence: **99.18%**
566. **`clients/src/main/java/org/apache/kafka/common/metrics/stats/Frequencies.java`** -> AI Confidence: **99.18%**
567. **`clients/src/main/java/org/apache/kafka/common/network/PlaintextChannelBuilder.java`** -> AI Confidence: **99.18%**
568. **`clients/src/main/java/org/apache/kafka/common/network/SslChannelBuilder.java`** -> AI Confidence: **99.18%**
569. **`clients/src/main/java/org/apache/kafka/common/protocol/MessageUtil.java`** -> AI Confidence: **99.18%**
570. **`clients/src/main/java/org/apache/kafka/common/protocol/types/Type.java`** -> AI Confidence: **99.18%**
571. **`clients/src/main/java/org/apache/kafka/common/record/internal/DefaultRecordBatch.java`** -> AI Confidence: **99.18%**
572. **`clients/src/main/java/org/apache/kafka/common/record/internal/EndTransactionMarker.java`** -> AI Confidence: **99.18%**
573. **`clients/src/main/java/org/apache/kafka/common/record/internal/FileLogInputStream.java`** -> AI Confidence: **99.18%**
574. **`clients/src/main/java/org/apache/kafka/common/record/internal/FileRecords.java`** -> AI Confidence: **99.18%**
575. **`clients/src/main/java/org/apache/kafka/common/requests/AddPartitionsToTxnRequest.java`** -> AI Confidence: **99.18%**
576. **`clients/src/main/java/org/apache/kafka/common/requests/AddPartitionsToTxnResponse.java`** -> AI Confidence: **99.18%**
577. **`clients/src/main/java/org/apache/kafka/common/requests/AlterClientQuotasResponse.java`** -> AI Confidence: **99.18%**
578. **`clients/src/main/java/org/apache/kafka/common/requests/CreateTopicsRequest.java`** -> AI Confidence: **99.18%**
579. **`clients/src/main/java/org/apache/kafka/common/requests/DeleteTopicsRequest.java`** -> AI Confidence: **99.18%**
580. **`clients/src/main/java/org/apache/kafka/common/requests/DescribeAclsResponse.java`** -> AI Confidence: **99.18%**
581. **`clients/src/main/java/org/apache/kafka/common/requests/DescribeClientQuotasResponse.java`** -> AI Confidence: **99.18%**
582. **`clients/src/main/java/org/apache/kafka/common/requests/ElectLeadersRequest.java`** -> AI Confidence: **99.18%**
583. **`clients/src/main/java/org/apache/kafka/common/requests/FetchRequest.java`** -> AI Confidence: **99.18%**
584. **`clients/src/main/java/org/apache/kafka/common/requests/FetchSnapshotResponse.java`** -> AI Confidence: **99.18%**
585. **`clients/src/main/java/org/apache/kafka/common/requests/LeaveGroupResponse.java`** -> AI Confidence: **99.18%**
586. **`clients/src/main/java/org/apache/kafka/common/requests/ListOffsetsRequest.java`** -> AI Confidence: **99.18%**
587. **`clients/src/main/java/org/apache/kafka/common/requests/MetadataRequest.java`** -> AI Confidence: **99.18%**
588. **`clients/src/main/java/org/apache/kafka/common/requests/ProduceResponse.java`** -> AI Confidence: **99.18%**
589. **`clients/src/main/java/org/apache/kafka/common/requests/ShareFetchRequest.java`** -> AI Confidence: **99.18%**
590. **`clients/src/main/java/org/apache/kafka/common/security/authenticator/AbstractLogin.java`** -> AI Confidence: **99.18%**
591. **`clients/src/main/java/org/apache/kafka/common/security/authenticator/SaslServerAuthenticator.java`** -> AI Confidence: **99.18%**
592. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/OAuthBearerValidatorCallbackHandler.java`** -> AI Confidence: **99.18%**
593. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/OAuthBearerRefreshingLogin.java`** -> AI Confidence: **99.18%**
594. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/ClientCredentialsRequestFormatterFactory.java`** -> AI Confidence: **99.18%**
595. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/JaasOptionsUtils.java`** -> AI Confidence: **99.18%**
596. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/VerificationKeyResolverFactory.java`** -> AI Confidence: **99.18%**
597. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/assertion/AssertionSupplierFactory.java`** -> AI Confidence: **99.18%**
598. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/assertion/AssertionUtils.java`** -> AI Confidence: **99.18%**
599. **`clients/src/main/java/org/apache/kafka/common/security/plain/internals/PlainServerCallbackHandler.java`** -> AI Confidence: **99.18%**
600. **`clients/src/main/java/org/apache/kafka/common/security/scram/ScramLoginModule.java`** -> AI Confidence: **99.18%**
601. **`clients/src/main/java/org/apache/kafka/common/telemetry/internals/KafkaMetricsCollector.java`** -> AI Confidence: **99.18%**
602. **`clients/src/main/java/org/apache/kafka/common/utils/ImplicitLinkedHashCollection.java`** -> AI Confidence: **99.18%**
603. **`clients/src/main/java/org/apache/kafka/common/utils/LoggingSignalHandler.java`** -> AI Confidence: **99.18%**
604. **`clients/src/test/java/org/apache/kafka/clients/admin/internals/AdminBootstrapAddressesTest.java`** -> AI Confidence: **99.18%**
605. **`clients/src/test/java/org/apache/kafka/clients/consumer/internals/AutoOffsetResetStrategyTest.java`** -> AI Confidence: **99.18%**
606. **`clients/src/test/java/org/apache/kafka/clients/consumer/internals/CommitRequestManagerTest.java`** -> AI Confidence: **99.18%**
607. **`clients/src/test/java/org/apache/kafka/clients/consumer/internals/ConsumerMembershipManagerTest.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `settings.gradle` -> **0.0233%** Exposure
### Exploit Generation Surface
- `.github/scripts/checkstyle.py` -> **100.0%** Exposure
- `.github/scripts/develocity_reports.py` -> **100.0%** Exposure
- `.github/scripts/junit.py` -> **100.0%** Exposure
- `.github/scripts/pr-format.py` -> **100.0%** Exposure
- `committer-tools/kafka-merge-pr.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `docker/common.py` -> **100.0%** Exposure
- `bin/kafka-server-stop.sh` -> **100.0%** Exposure
- `vagrant/aws/aws-init.sh` -> **100.0%** Exposure
- `vagrant/base.sh` -> **100.0%** Exposure
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/AbstractFetch.java` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `clients/src/test/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactoryTest.java` -> **99.9995%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/assertion/AssertionUtils.java` -> **99.9795%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/oauthbearer/ClientAssertionKeycloakIntegrationTest.java` -> **75.625%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactory.java` -> **68.1223%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/authenticator/SaslAuthenticatorTest.java` -> **22.6166%** Exposure
### Algorithmic DoS Exposure
- `.github/scripts/checkstyle.py` -> **100.0%** Exposure
- `.github/scripts/develocity_reports.py` -> **100.0%** Exposure
- `.github/scripts/format-test-catalog.py` -> **100.0%** Exposure
- `.github/scripts/junit.py` -> **100.0%** Exposure
- `.github/scripts/pr-format.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `32` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `89880` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `clients/src/main/java/org/apache/kafka/common/utils/CopyOnWriteMap.java` (JAVA) -> Cumulative Risk: **967.35**
- **Archetype:** `file_cluster_4` (Distance: 11.283 IQR)
- **Magnitude:** 231.4 | **LOC:** 151 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `remove` (Impact: 21.2), `putAll` (Impact: 15.8), `replace` (Impact: 12.4)

### 2. `metadata/src/main/java/org/apache/kafka/metadata/KRaftMetadataCache.java` (JAVA) -> Cumulative Risk: **952.51**
- **Archetype:** `file_cluster_13` (Distance: 13.317 IQR)
- **Magnitude:** 908.7 | **LOC:** 524 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `partitionMetadata` (Impact: 223.2), `describeTopicResponse` (Impact: 132.4), `getPartitionReplicaEndpoints` (Impact: 43.4)

### 3. `trogdor/src/main/java/org/apache/kafka/trogdor/workload/SustainedConnectionWorker.java` (JAVA) -> Cumulative Risk: **934.85**
- **Archetype:** `file_cluster_4` (Distance: 11.059 IQR)
- **Magnitude:** 604.58 | **LOC:** 533 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `run` (Impact: 49.8), `start` (Impact: 44.1), `refresh` (Impact: 44.0)

### 4. `clients/src/main/java/org/apache/kafka/clients/consumer/MockConsumer.java` (JAVA) -> Cumulative Risk: **907.68**
- **Archetype:** `file_cluster_4` (Distance: 12.049 IQR)
- **Magnitude:** 1320.26 | **LOC:** 722 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `poll` (Impact: 185.5), `subscribe` (Impact: 70.3), `resetOffsetPosition` (Impact: 56.9)

### 5. `server-common/src/main/java/org/apache/kafka/server/share/persister/NoOpStatePersister.java` (JAVA) -> Cumulative Risk: **900.52**
- **Archetype:** `file_cluster_4` (Distance: 14.429 IQR)
- **Magnitude:** 168.92 | **LOC:** 108 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `readSummary` (Impact: 20.9), `readState` (Impact: 20.8), `initializeState` (Impact: 17.3)

### 6. `connect/runtime/src/main/java/org/apache/kafka/connect/storage/MemoryStatusBackingStore.java` (JAVA) -> Cumulative Risk: **898.71**
- **Archetype:** `file_cluster_4` (Distance: 12.066 IQR)
- **Magnitude:** 227.48 | **LOC:** 144 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `put` (Impact: 29.7), `put` (Impact: 29.7), `getAllTopics` (Impact: 13.7)

### 7. `server-common/src/main/java/org/apache/kafka/server/util/timer/TimerTaskList.java` (JAVA) -> Cumulative Risk: **895.78**
- **Archetype:** `file_cluster_4` (Distance: 10.61 IQR)
- **Magnitude:** 186.36 | **LOC:** 132 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `add` (Impact: 24.7), `foreach` (Impact: 15.1), `remove` (Impact: 12.8)

### 8. `server-common/src/main/java/org/apache/kafka/server/util/timer/SystemTimer.java` (JAVA) -> Cumulative Risk: **894.9**
- **Archetype:** `file_cluster_4` (Distance: 10.335 IQR)
- **Magnitude:** 209.88 | **LOC:** 122 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `advanceClock` (Impact: 108.2), `addTimerTaskEntry` (Impact: 17.2), `add` (Impact: 13.8)

### 9. `server-common/src/main/java/org/apache/kafka/server/util/KafkaScheduler.java` (JAVA) -> Cumulative Risk: **886.98**
- **Archetype:** `file_cluster_4` (Distance: 10.473 IQR)
- **Magnitude:** 353.34 | **LOC:** 195 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `schedule` (Impact: 142.1), `shutdown` (Impact: 30.7), `compareTo` (Impact: 28.4)

### 10. `streams/src/main/java/org/apache/kafka/streams/processor/internals/Tasks.java` (JAVA) -> Cumulative Risk: **883.23**
- **Archetype:** `file_cluster_0` (Distance: 12.224 IQR)
- **Magnitude:** 646.86 | **LOC:** 404 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `removeTask` (Impact: 73.8), `addActiveTask` (Impact: 43.2), `addStandbyTask` (Impact: 32.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.626 IQR)
- **Top Global Matches:** file_cluster_8: 13.626, file_cluster_13: 13.869, file_cluster_0: 13.892
- **Magnitude:** 7502.36 | **LOC:** 27677 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 32.5%
- **Algorithmic:** O(N^6) | **DB Complexity:** 180
- **Risk Profile:** Cognitive Load (56.9031%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testListGroups` (Impact: 218.7 | O(N^5) | DB: 55)
  * `generatePendingAssignmentCases` (Impact: 204.3 | O(N^6) | DB: 29)
  * `testLastStaticConsumerProtocolMemberRepl` (Impact: 133.3 | O(N^6) | DB: 42)
  * `verifyClassicGroupJoinResponses` (Impact: 55.4 | O(N^5) | DB: 1)
  * `testDynamicBrokerAndGroupConfigs` (Impact: 53.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 2663`, `args: 908`, `func_start: 1898`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 290`, `state_mutation: 3684`, `dead_code: 5`, `duplicate_logic: 31`, `orphaned_logic: 211`
* *Architecture:* `api: 242`, `concurrency: 5`, `import: 232`
* *Defense:* `safety: 77`, `doc: 2`, `test: 1615`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 104):` org.apache.kafka.coordinator.group.metrics.GroupCoordinatorMetricsShard, org.apache.kafka.common.message.StreamsGroupHeartbeatRequestData.TopicInfo, org.apache.kafka.common.message.ConsumerGroupDescribeResponseData, org.mockito.Mockito.times, org.junit.jupiter.api.Test, org.apache.kafka.coordinator.group.modern.MemberState, org.junit.jupiter.params.provider.MethodSource, org.apache.kafka.coordinator.common.runtime.MockCoordinatorTimer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.909 IQR)
- **Top Global Matches:** file_cluster_13: 13.909, file_cluster_8: 14.133, file_cluster_11: 14.344
- **Magnitude:** 5385.78 | **LOC:** 4029 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (94.7551%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRequest` (Impact: 635.2 | O(N^3) | DB: 5)
  * `getResponse` (Impact: 635.2 | O(N^3) | DB: 5)
  * `verifyDescribeConfigsResponse` (Impact: 106.7 | O(N^6))
  * `createDescribeConfigsResponse` (Impact: 56.7 | O(N^6) | DB: 29)
  * `createFetchResponse` (Impact: 55.6 | O(N^5) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 1644`, `args: 336`, `func_start: 517`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 1657`, `duplicate_logic: 11`, `orphaned_logic: 48`
* *Architecture:* `api: 42`, `import: 305`
* *Defense:* `safety: 23`, `doc: 1`, `test: 195`, `immutability_locks: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` org.apache.kafka.common.message.AlterConfigsResponseData, org.apache.kafka.common.message.DescribeUserScramCredentialsResponseData, org.apache.kafka.common.message.ApiVersionsResponseData, org.apache.kafka.common.message.ConsumerGroupDescribeRequestData, org.apache.kafka.common.message.ConsumerGroupDescribeResponseData, org.apache.kafka.common.protocol.ApiKeys.LIST_GROUPS, org.apache.kafka.common.utils.SecurityUtils, java.util.LinkedHashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/client-secrets/client.keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/secrets/kafka.truststore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/secrets/kafka01.keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/docker/ssh/id_rsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/docker/ssh/id_rsa.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.27 IQR)
- **Top Global Matches:** file_cluster_13: 14.27, file_cluster_0: 14.409, file_cluster_4: 14.501
- **Magnitude:** 4948.6 | **LOC:** 11791 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 183
- **Risk Profile:** Cognitive Load (66.3601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testListOffsetsHandlesFulfillmentTimeout` (Impact: 578.1 | O(N^6) | DB: 183)
  * `prepareDescribeQuorumResponse` (Impact: 146.1 | O(N^5) | DB: 22)
  * `defaultQuorumInfo` (Impact: 112.2 | O(N^6))
  * `prepareMetadataResponse` (Impact: 67.5 | O(N^5) | DB: 13)
  * `verifyListConsumerGroupOffsetsOptions` (Impact: 37.8 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 1883`, `args: 437`, `func_start: 781`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 200`, `state_mutation: 1699`, `duplicate_logic: 28`, `orphaned_logic: 106`
* *Architecture:* `api: 149`, `concurrency: 203`, `import: 307`
* *Defense:* `safety: 221`, `doc: 4`, `test: 497`, `sync_locks: 5`, `immutability_locks: 250`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 155):` org.apache.kafka.common.message.LeaveGroupResponseData.MemberResponse, org.apache.kafka.common.requests.DescribeQuorumRequest, org.apache.kafka.clients.consumer.OffsetAndMetadata, org.apache.kafka.common.message.DescribeUserScramCredentialsResponseData, org.apache.kafka.common.message.FindCoordinatorResponseData, org.apache.kafka.common.requests.DescribeConfigsResponse, org.apache.kafka.common.message.DescribeShareGroupOffsetsRequestData, org.apache.kafka.common.message.IncrementalAlterConfigsResponseData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streams/src/main/java/org/apache/kafka/streams/processor/internals/StateDirectory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.033 IQR)
- **Top Global Matches:** file_cluster_13: 11.033, file_cluster_4: 11.578, file_cluster_8: 11.602
- **Magnitude:** 4598.64 | **LOC:** 978 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.4048%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 115`, `args: 24`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 10`, `concurrency: 21`, `import: 59`
* *Defense:* `safety: 11`, `doc: 15`, `sync_locks: 9`, `immutability_locks: 62`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.001472 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` org.apache.kafka.streams.internals.StreamsConfigUtils, org.apache.kafka.streams.state.internals.ThreadCache, org.apache.kafka.streams.processor.Punctuator, java.util.Collection, java.io.File, org.apache.kafka.streams.processor.To, org.apache.kafka.streams.errors.TaskCorruptedException, com.fasterxml.jackson.databind.ObjectMapper...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `raft/src/test/java/org/apache/kafka/raft/RaftUtilTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.504 IQR)
- **Top Global Matches:** file_cluster_13: 10.504, file_cluster_8: 10.605, file_cluster_0: 10.868
- **Magnitude:** 4184.14 | **LOC:** 695 | **CtrlFlow:** 81.6% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (59.8451%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `singletonFetchRequestTestCases` (Impact: 855.0 | O(N^6))
  * `singletonFetchResponseTestCases` (Impact: 823.7 | O(N^6))
  * `describeQuorumResponseTestCases` (Impact: 478.4 | O(N^6))
  * `voteRequestTestCases` (Impact: 377.0 | O(N^6))
  * `voteResponseTestCases` (Impact: 282.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 115`, `args: 35`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`, `orphaned_logic: 17`
* *Architecture:* `api: 14`, `import: 54`
* *Defense:* `safety: 1`, `test: 37`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` org.apache.kafka.common.message.DescribeQuorumRequestData, org.apache.kafka.common.record.internal.MemoryRecords, org.apache.kafka.common.message.FetchResponseData, org.apache.kafka.common.Uuid, org.junit.jupiter.api.Test, org.junit.jupiter.params.ParameterizedTest, org.junit.jupiter.params.provider.MethodSource, org.apache.kafka.common.message.BeginQuorumEpochResponseDataJsonConverter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/kafka/server/share/SharePartition.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.546 IQR)
- **Top Global Matches:** file_cluster_13: 13.546, file_cluster_11: 13.885, file_cluster_16: 13.904
- **Magnitude:** 3596.58 | **LOC:** 3427 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (35.5674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lastOffsetAndMaxRecordsToAcquire` (Impact: 1796.2 | O(N^6) | DB: 59)
  * `acknowledge` (Impact: 269.9 | O(2^N))
    * *Intent:* /**
  * `releaseAcquiredRecordsForPerOffsetBatch` (Impact: 182.1 | O(N^6) | DB: 3)
    * *Intent:* /** * The load start time is used to track the time taken to load the share partition.
  * `archiveRecords` (Impact: 168.8 | O(N^6) | DB: 4)
    * *Intent:* // The previousBatchLastOffset is used to track the last offset of the previous batch. // For the fi...
  * `updateCacheAndOffsets` (Impact: 135.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 430`, `structural_boundaries: 253`, `args: 81`, `func_start: 74`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 174`, `dead_code: 8`
* *Architecture:* `api: 15`, `concurrency: 25`, `import: 73`
* *Defense:* `safety: 98`, `doc: 83`, `sync_locks: 90`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` java.util.concurrent.ConcurrentSkipListMap, kafka.server.ReplicaManager, org.apache.kafka.server.util.timer.Timer, org.apache.kafka.server.share.persister.WriteShareGroupStateParameters, org.apache.kafka.server.share.persister.PartitionFactory, org.apache.kafka.common.message.FetchResponseData, org.apache.kafka.common.Uuid, java.util.concurrent.atomic.AtomicInteger...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreChangelogReader.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.842 IQR)
- **Top Global Matches:** file_cluster_17: 12.842, file_cluster_13: 12.862, file_cluster_11: 12.891
- **Magnitude:** 3583.28 | **LOC:** 1136 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (36.6891%), Tech Debt (9.579%)
**Top Internal Functions/Classes:**
  * `hasRestoredToEnd` (Impact: 3333.8 | O(2^N) | DB: 21)
  * `StoreChangelogReader` (Impact: 64.2 | O(2^N))
  * `transitTo` (Impact: 18.7 | O(N^4))
  * `recordEndOffset` (Impact: 16.0 | O(N^2))
  * `clear` (Impact: 8.2 | O(2^N) | DB: 2)
    * *Intent:* // the end offset beyond which records should not be applied (yet) to restore the states // // for b...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 166`, `args: 79`, `func_start: 87`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 61`, `dead_code: 12`, `planned_debt: 4`
* *Architecture:* `api: 18`, `import: 40`
* *Defense:* `safety: 32`, `doc: 4`, `immutability_locks: 191`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` java.util.Collection, java.util.OptionalLong, org.apache.kafka.streams.errors.TaskCorruptedException, java.util.Set, java.util.ArrayList, java.util.List, org.slf4j.Logger, java.util.concurrent.ExecutionException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streams/src/test/java/org/apache/kafka/streams/TopologyTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.015 IQR)
- **Top Global Matches:** file_cluster_0: 12.015, file_cluster_8: 12.1, file_cluster_13: 12.192
- **Magnitude:** 3509.32 | **LOC:** 2489 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (19.5865%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tableNamedMaterializedCountWithTopologyC` (Impact: 106.2 | O(N^4) | DB: 2)
  * `tableNamedMaterializedCountShouldPreserv` (Impact: 100.0 | O(N^4) | DB: 2)
  * `tableAnonymousMaterializedCountShouldPre` (Impact: 100.0 | O(N^4) | DB: 2)
  * `tableAnonymousStoreTypedMaterializedCoun` (Impact: 100.0 | O(N^4) | DB: 2)
  * `streamStreamJoinTopologyWithCustomStores` (Impact: 87.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 386`, `args: 182`, `func_start: 299`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 123`, `duplicate_logic: 10`, `orphaned_logic: 95`
* *Architecture:* `api: 112`, `import: 70`
* *Defense:* `safety: 30`, `test: 262`, `immutability_locks: 330`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` org.apache.kafka.test.MockKeyValueStore, org.mockito.quality.Strictness, org.apache.kafka.streams.utils.TestUtils.PROCESSOR_WRAPPER_COUNTER_CONFIG, org.apache.kafka.streams.state.StoreBuilder, org.mockito.Mockito.mock, org.apache.kafka.test.MockApiProcessorSupplier, org.apache.kafka.streams.state.SessionStore, org.junit.jupiter.api.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.242 IQR)
- **Top Global Matches:** file_cluster_13: 12.242, file_cluster_8: 12.276, file_cluster_0: 12.407
- **Magnitude:** 3352.28 | **LOC:** 4430 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (21.3957%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `revokeAndReassign` (Impact: 1525.4 | O(N^6) | DB: 30)
  * `expectRebalance` (Impact: 188.4 | O(N^6))
  * `testModifyOffsetsSourceConnectorExactlyO` (Impact: 88.2 | O(N^4))
    * *Intent:* // No need to check herder.connectorConfig explicitly: // all the related parts are mocked and that ...
  * `testModifyOffsetsSourceConnectorExactlyO` (Impact: 72.3 | O(N^4) | DB: 1)
  * `exactlyOnceSnapshot` (Impact: 62.6 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 603`, `args: 220`, `func_start: 823`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 117`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 23`, `orphaned_logic: 33`
* *Architecture:* `io: 2`, `api: 80`, `concurrency: 14`, `import: 130`
* *Defense:* `safety: 6`, `doc: 5`, `test: 570`, `immutability_locks: 66`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` org.mockito.quality.Strictness, org.apache.kafka.connect.runtime.rest.entities.ConnectorType, org.apache.kafka.connect.source.SourceConnector, jakarta.ws.rs.core.Response.Status.SERVICE_UNAVAILABLE, org.mockito.Mockito.times, org.junit.jupiter.api.Test, org.apache.kafka.connect.runtime.rest.entities.ConnectorOffset, org.mockito.ArgumentMatchers.any...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.846 IQR)
- **Top Global Matches:** file_cluster_13: 13.846, file_cluster_16: 14.217, file_cluster_8: 14.282
- **Magnitude:** 3093.28 | **LOC:** 8993 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 29.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (22.6593%), Tech Debt (15.5359%)
**Top Internal Functions/Classes:**
  * `getOrMaybeCreatePersistedShareGroup` (Impact: 1422.6 | O(N^6) | DB: 68)
  * `completeClassicGroupJoin` (Impact: 210.8 | O(2^N) | DB: 10)
    * *Intent:* /** * Validates the member epoch provided in the heartbeat request. * * @param member The streams gr...
  * `classicGroupLeaveToClassicGroup` (Impact: 187.0 | O(N^6) | DB: 20)
  * `maybeDeleteEmptyClassicGroup` (Impact: 138.3 | O(N^3) | DB: 2)
  * `expirePendingSync` (Impact: 80.6 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 539`, `args: 201`, `func_start: 161`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 279`, `dead_code: 4`, `duplicate_logic: 7`
* *Architecture:* `api: 36`, `concurrency: 9`, `import: 231`
* *Defense:* `safety: 72`, `doc: 333`, `sync_locks: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 124):` org.apache.kafka.coordinator.group.Group.GroupType.STREAMS, org.apache.kafka.common.message.LeaveGroupResponseData.MemberResponse, org.apache.kafka.coordinator.group.metrics.GroupCoordinatorMetricsShard, org.apache.kafka.coordinator.group.generated.ConsumerGroupRegularExpressionValue, org.apache.kafka.coordinator.group.streams.StreamsGroupMember.hasAssignedTasksChanged, org.apache.kafka.coordinator.group.streams.StreamsCoordinatorRecordHelpers.newStreamsGroupTargetAssignmentTombstoneRecord, org.apache.kafka.common.message.ConsumerGroupDescribeResponseData, org.apache.kafka.coordinator.group.generated.StreamsGroupTargetAssignmentMetadataValue...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.265 IQR)
- **Top Global Matches:** file_cluster_0: 12.265, file_cluster_13: 12.278, file_cluster_16: 12.3
- **Magnitude:** 3027.74 | **LOC:** 1605 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (77.0336%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleIncrementalResourceAlteration` (Impact: 393.6 | O(N^6) | DB: 12)
  * `updateFeatures` (Impact: 220.3 | O(N^6) | DB: 2)
  * `getResourceDescription` (Impact: 173.5 | O(N^6))
  * `addTopic` (Impact: 112.9 | O(N^6) | DB: 4)
  * `createTopics` (Impact: 100.1 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 439`, `args: 132`, `func_start: 118`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 210`, `planned_debt: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 178`, `concurrency: 74`, `import: 56`
* *Defense:* `safety: 22`, `doc: 2`, `sync_locks: 59`, `immutability_locks: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` org.apache.kafka.common.GroupState, org.apache.kafka.common.MetricName, org.apache.kafka.common.errors.KafkaStorageException, org.apache.kafka.common.errors.TopicExistsException, org.apache.kafka.clients.consumer.OffsetAndMetadata, java.util.Collection, org.apache.kafka.common.Uuid, org.apache.kafka.common.acl.AclBindingFilter...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `server-common/src/test/java/org/apache/kafka/server/share/persister/PersisterStateManagerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.672 IQR)
- **Top Global Matches:** file_cluster_8: 12.672, file_cluster_0: 12.844, file_cluster_13: 12.921
- **Magnitude:** 3027.3 | **LOC:** 4939 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (28.0946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testWriteStateRequestBatchingWithCoordin` (Impact: 74.0 | O(N^6) | DB: 10)
  * `testInitializeStateRequestBatchingWithCo` (Impact: 73.8 | O(N^6) | DB: 10)
    * *Intent:* // Verifying the coordinator node was populated correctly by the FIND_COORDINATOR request
  * `testDeleteStateRequestBatchingWithCoordi` (Impact: 73.5 | O(N^6) | DB: 10)
    * *Intent:* // Verifying the coordinator node was populated correctly by the FIND_COORDINATOR request
  * `testResponseErrorHandling` (Impact: 63.3 | O(N^4))
  * `generatorDifferentStates` (Impact: 57.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 759`, `args: 271`, `func_start: 386`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 306`, `state_mutation: 525`, `duplicate_logic: 4`, `orphaned_logic: 51`
* *Architecture:* `api: 75`, `concurrency: 202`, `import: 60`
* *Defense:* `safety: 202`, `test: 278`, `immutability_locks: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` org.apache.kafka.clients.MockClient, org.mockito.Mockito.verify, org.apache.kafka.common.message.FindCoordinatorResponseData, org.apache.kafka.server.util.timer.Timer, org.mockito.Mockito.mock, org.apache.kafka.common.requests.InitializeShareGroupStateRequest, org.apache.kafka.common.Uuid, org.junit.jupiter.api.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.096 IQR)
- **Top Global Matches:** file_cluster_13: 12.096, file_cluster_8: 12.657, file_cluster_0: 12.689
- **Magnitude:** 2962.0 | **LOC:** 5180 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (27.8166%), Tech Debt (10.957%)
**Top Internal Functions/Classes:**
  * `provide` (Impact: 2472.6 | O(2^N) | DB: 53)
  * `close` (Impact: 230.3 | O(2^N))
    * *Intent:* /** * The default implementation of {@link Admin}. An instance of this class is created by invoking ...
  * `configureDefaultApiTimeoutMs` (Impact: 41.1 | O(N^5))
  * `supportsUseControllers` (Impact: 18.4 | O(2^N))
  * `ConstantNodeIdProvider` (Impact: 4.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 482`, `args: 92`, `func_start: 112`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 121`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `concurrency: 22`, `import: 287`
* *Defense:* `safety: 22`, `doc: 27`, `sync_locks: 2`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.089
  * `Choke Point (Betweenness):` 0.000531 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 175):` org.apache.kafka.common.errors.KafkaStorageException, org.apache.kafka.common.requests.UnregisterBrokerRequest, org.apache.kafka.common.internals.Topic.CLUSTER_METADATA_TOPIC_PARTITION, org.apache.kafka.common.requests.DescribeQuorumRequest, org.apache.kafka.clients.consumer.OffsetAndMetadata, org.apache.kafka.common.message.DescribeUserScramCredentialsResponseData, org.apache.kafka.common.requests.AlterClientQuotasResponse, org.apache.kafka.clients.admin.internals.AdminUtils.validAclOperations...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `server-common/src/main/java/org/apache/kafka/server/share/persister/PersisterStateManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.892 IQR)
- **Top Global Matches:** file_cluster_13: 11.892, file_cluster_0: 12.009, file_cluster_8: 12.055
- **Magnitude:** 2933.1 | **LOC:** 1737 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (62.7507%), Tech Debt (99.9885%)
**Top Internal Functions/Classes:**
  * `handleRequestResponse` (Impact: 348.6 | O(N^6) | DB: 6)
  * `handleRequestResponse` (Impact: 348.6 | O(N^6) | DB: 6)
  * `handleRequestResponse` (Impact: 348.5 | O(N^6) | DB: 6)
  * `handleFindCoordinatorResponse` (Impact: 348.0 | O(N^6) | DB: 5)
  * `handleRequestResponse` (Impact: 340.6 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 323`, `args: 108`, `func_start: 173`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 133`, `duplicate_logic: 56`
* *Architecture:* `api: 81`, `concurrency: 45`, `import: 61`
* *Defense:* `safety: 23`, `doc: 8`, `sync_locks: 1`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` java.util.Collection, org.apache.kafka.common.message.FindCoordinatorResponseData, org.apache.kafka.server.util.timer.Timer, org.apache.kafka.server.util.RequestAndCompletionHandler, org.apache.kafka.common.requests.InitializeShareGroupStateRequest, org.apache.kafka.common.Uuid, org.apache.kafka.common.message.ReadShareGroupStateResponseData, org.apache.kafka.common.requests.AbstractRequest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.485 IQR)
- **Top Global Matches:** file_cluster_0: 13.485, file_cluster_4: 13.519, file_cluster_13: 13.541
- **Magnitude:** 2874.98 | **LOC:** 4753 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (42.9147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testConsumerCloseInGroupSequential` (Impact: 502.6 | O(N^6) | DB: 37)
  * `testMultipleConsumersInMultipleGroupsCon` (Impact: 93.0 | O(N^5) | DB: 13)
  * `consumeMessages` (Impact: 61.0 | O(N^6) | DB: 1)
  * `testMultipleConsumersInGroupConcurrentCo` (Impact: 55.6 | O(N^5) | DB: 5)
  * `testDynamicPartitionMaxRecordLocks` (Impact: 51.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 711`, `args: 299`, `func_start: 666`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 327`, `dead_code: 1`, `duplicate_logic: 21`, `orphaned_logic: 57`
* *Architecture:* `api: 84`, `concurrency: 289`, `import: 107`
* *Defense:* `safety: 144`, `doc: 5`, `test: 241`, `sync_locks: 4`, `immutability_locks: 26`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` org.apache.kafka.clients.admin.SharePartitionOffsetInfo, java.util.HashMap, org.apache.kafka.common.serialization.Deserializer, java.util.concurrent.ScheduledExecutorService, java.util.stream.IntStream, org.apache.kafka.clients.producer.ProducerConfig, java.util.Iterator, org.apache.kafka.common.errors.SerializationException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `raft/src/main/java/org/apache/kafka/raft/KafkaRaftClient.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.877 IQR)
- **Top Global Matches:** file_cluster_8: 11.877, file_cluster_13: 11.919, file_cluster_16: 12.227
- **Magnitude:** 2840.22 | **LOC:** 4153 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (15.5015%), Tech Debt (16.071%)
**Top Internal Functions/Classes:**
  * `resign` (Impact: 216.9 | O(2^N))
  * `maybeHandleCommonResponse` (Impact: 135.3 | O(N^4))
    * *Intent:* /** * Handle a Vote request. This API may return the following errors:
  * `computeFetchSnapshotLeaderEndpoints` (Impact: 105.6 | O(N^6) | DB: 2)
  * `handleBeginQuorumEpochResponse` (Impact: 70.5 | O(N^5))
  * `handleVoteRequest` (Impact: 70.2 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 375`, `args: 209`, `func_start: 146`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 103`, `dead_code: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 1`, `api: 38`, `concurrency: 42`, `import: 105`
* *Defense:* `safety: 58`, `doc: 31`, `sync_locks: 6`, `immutability_locks: 31`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.000193 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 60):` org.apache.kafka.common.requests.DescribeQuorumRequest, org.apache.kafka.common.message.ApiVersionsResponseData, org.apache.kafka.common.errors.CorruptRecordException, org.apache.kafka.common.record.internal.Records, java.util.concurrent.CompletableFuture.completedFuture, org.apache.kafka.common.message.BeginQuorumEpochResponseData, org.apache.kafka.raft.internals.CloseListener, org.apache.kafka.server.common.serialization.RecordSerde...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/Worker.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.559 IQR)
- **Top Global Matches:** file_cluster_13: 12.559, file_cluster_16: 12.863, file_cluster_11: 12.929
- **Magnitude:** 2741.56 | **LOC:** 2416 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (22.6324%), Tech Debt (28.6734%)
**Top Internal Functions/Classes:**
  * `alterSinkConnectorOffsets` (Impact: 1252.2 | O(N^6) | DB: 19)
  * `modifySinkConnectorOffsets` (Impact: 328.8 | O(N^6) | DB: 3)
  * `startConnector` (Impact: 112.5 | O(N^6) | DB: 3)
  * `fenceZombies` (Impact: 103.6 | O(N^6))
  * `sinkConnectorOffsets` (Impact: 96.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 260`, `args: 89`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 111`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 38`, `concurrency: 11`, `import: 108`
* *Defense:* `safety: 55`, `doc: 75`, `sync_locks: 3`, `immutability_locks: 36`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 83):` org.apache.kafka.clients.consumer.OffsetAndMetadata, org.apache.kafka.connect.source.SourceConnector, org.apache.kafka.connect.storage.OffsetUtils, org.apache.kafka.connect.json.JsonConverterConfig, org.apache.kafka.connect.storage.Converter, org.apache.kafka.connect.runtime.isolation.Plugins.ClassLoaderUsage, org.apache.kafka.connect.runtime.rest.entities.ConnectorOffset, org.apache.kafka.connect.connector.ConnectRecord...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `generator/src/main/java/org/apache/kafka/message/FieldSpec.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.805 IQR)
- **Top Global Matches:** file_cluster_8: 10.805, file_cluster_0: 10.986, file_cluster_7: 11.235
- **Magnitude:** 2692.16 | **LOC:** 664 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.5319%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fieldDefault` (Impact: 1585.5 | O(2^N))
  * `generateNonDefaultValueCheck` (Impact: 345.7 | O(N^6))
  * `FieldSpec` (Impact: 274.1 | O(2^N))
  * `fieldAbstractJavaType` (Impact: 202.5 | O(N^6))
  * `checkTagInvariants` (Impact: 55.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 121`, `args: 37`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 54`, `doc: 23`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.regex.Pattern, com.fasterxml.jackson.annotation.JsonCreator, java.util.Optional, java.util.Base64, com.fasterxml.jackson.annotation.JsonProperty, java.util.Objects, java.nio.ByteBuffer, java.util.List
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.799 IQR)
- **Top Global Matches:** file_cluster_8: 8.799, file_cluster_13: 9.083, file_cluster_7: 9.297
- **Magnitude:** 2689.84 | **LOC:** 331 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (35.7736%), Tech Debt (90.6446%)
**Top Internal Functions/Classes:**
  * `parseResponse` (Impact: 2571.2 | O(2^N))
  * `parseResponse` (Impact: 35.4 | O(2^N))
  * `errorCounts` (Impact: 12.3 | O(2^N))
  * `apiErrorCounts` (Impact: 8.3 | O(N^3))
    * *Intent:* /**
  * `apiKey` (Impact: 6.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 126`, `args: 15`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 21`, `import: 14`
* *Defense:* `doc: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.476
  * `Choke Point (Betweenness):` 0.000134 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.apache.kafka.common.protocol.SendBuilder, org.apache.kafka.common.protocol.Errors, java.util.Collection, org.apache.kafka.common.protocol.Readable, java.util.Collections, org.apache.kafka.common.network.Send, org.apache.kafka.common.protocol.ApiKeys, java.util.EnumMap...
  * `Imported By (In-Degree: 58):` (Excluded from Brief to save tokens)

### `metadata/src/main/java/org/apache/kafka/controller/QuorumController.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.04 IQR)
- **Top Global Matches:** file_cluster_13: 12.04, file_cluster_8: 12.32, file_cluster_0: 12.355
- **Magnitude:** 2647.06 | **LOC:** 2191 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (26.0389%), Tech Debt (80.5795%)
**Top Internal Functions/Classes:**
  * `claim` (Impact: 292.8 | O(2^N))
    * *Intent:* /** * Append records to the Raft log. They will be written out asynchronously. * * @param log The lo...
  * `handleLoadSnapshot` (Impact: 190.0 | O(2^N))
  * `QuorumController` (Impact: 170.9 | O(2^N) | DB: 56)
  * `accept` (Impact: 158.1 | O(N^6))
  * `handleLeaderChange` (Impact: 158.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 379`, `args: 187`, `func_start: 215`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 122`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 110`, `concurrency: 62`, `import: 129`
* *Defense:* `safety: 27`, `doc: 46`, `immutability_locks: 39`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.072
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 75):` org.apache.kafka.common.metadata.RemoveAccessControlEntryRecord, org.apache.kafka.server.fault.FaultHandler, org.apache.kafka.common.metadata.ConfigRecord, org.apache.kafka.common.message.UpdateFeaturesRequestData, org.apache.kafka.common.message.RenewDelegationTokenResponseData, org.apache.kafka.common.message.UpdateFeaturesResponseData, java.util.HashMap, org.apache.kafka.common.metadata.UnfenceBrokerRecord...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `streams/src/test/java/org/apache/kafka/streams/processor/internals/DefaultStateUpdaterTest.java` (JAVA) | Magnitude: 2024.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1679, func_start: 656, structural_boundaries: 422, immutability_locks: 360
- `streams/src/test/java/org/apache/kafka/streams/state/internals/TimeOrderedKeyValueBufferTest.java` (JAVA) | Magnitude: 519.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 435, structural_boundaries: 136, func_start: 120, immutability_locks: 101
- `clients/src/main/java/org/apache/kafka/common/protocol/ByteBufferAccessor.java` (JAVA) | Magnitude: 179.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 108, api: 39, structural_boundaries: 32, args: 25
- `shell/src/test/java/org/apache/kafka/shell/glob/GlobVisitorTest.java` (JAVA) | Magnitude: 159.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 81, args: 29, func_start: 20
- `streams/src/main/java/org/apache/kafka/streams/state/internals/AbstractStoreBuilder.java` (JAVA) | Magnitude: 51.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 19, api: 16, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/StopFindCoordinatorOnCloseEvent.java` (JAVA) | Magnitude: 4.82 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, func_start: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bin/kafka-server-stop.sh` (SHELL) | Magnitude: 119.94 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 53, state_mutation: 44, branch: 34, indent_spaces: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/docker/run_tests.sh` (SHELL) | Magnitude: 5.72 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 25, indent_spaces: 14, state_mutation: 12, reflection_metaprogramming: 11
- `.github/scripts/label_small.sh` (SHELL) | Magnitude: 1.86 | Delta: **0.266 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, safety_bypasses: 8, io: 4, reflection_metaprogramming: 4
- `tests/docker/ducker-ak` (SHELL) | Magnitude: 1258.3 | Delta: **0.267 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 472, reflection_metaprogramming: 308, branch: 304, structural_boundaries: 157

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/isolation/SamplingTestPlugin.java` (JAVA) | Magnitude: 120.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 18, doc: 13, branch: 11
- `streams/src/main/java/org/apache/kafka/streams/processor/assignment/KafkaStreamsState.java` (JAVA) | Magnitude: 37.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 18, func_start: 8, indent_spaces: 8, structural_boundaries: 7
- `clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/Retry.java` (JAVA) | Magnitude: 47.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, branch: 6, func_start: 4
- `clients/src/test/java/org/apache/kafka/common/network/SslTransportLayerTest.java` (JAVA) | Magnitude: 1096.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 909, structural_boundaries: 399, func_start: 188, args: 114
- `clients/src/test/java/org/apache/kafka/common/requests/FindCoordinatorRequestTest.java` (JAVA) | Magnitude: 5.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, import: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `clients/src/main/java/org/apache/kafka/clients/admin/RemoveMembersFromConsumerGroupOptions.java` (JAVA) | Magnitude: 42.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, api: 8, args: 6
- `core/src/main/scala/kafka/cluster/Partition.scala` (SCALA) | Magnitude: 997.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 733, branch: 160, args: 136, closures: 112
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/StreamsOnTasksRevokedCallbackNeededEvent.java` (JAVA) | Magnitude: 16.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, api: 4, generics: 4
- `clients/src/main/java/org/apache/kafka/common/config/LogLevelConfig.java` (JAVA) | Magnitude: 23.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, api: 8, doc: 7, immutability_locks: 7
- `streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamFilter.java` (JAVA) | Magnitude: 23.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 17, generics: 7, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tools/src/main/java/org/apache/kafka/tools/streams/StreamsGroupCommand.java` (JAVA) | Magnitude: 1.88 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 858, branch: 295, structural_boundaries: 237, generics: 117
- `streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreChangelogReader.java` (JAVA) | Magnitude: 3583.28 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 741, branch: 198, immutability_locks: 191, structural_boundaries: 166
- `tools/src/main/java/org/apache/kafka/tools/OffsetsUtils.java` (JAVA) | Magnitude: 0.82 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 393, structural_boundaries: 138, branch: 103, state_mutation: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `committer-tools/update-cache.sh` (SHELL) | Magnitude: 14.0 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, io: 8, branch: 6, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `server-common/src/test/java/org/apache/kafka/server/util/ShutdownableThreadTest.java` (JAVA) | Magnitude: 125.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 39, concurrency: 19, import: 16
- `vagrant/zk.sh` (SHELL) | Magnitude: 20.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 21, io: 15, branch: 7, debug_prints: 7
- `clients/src/main/java/org/apache/kafka/clients/producer/RoundRobinPartitioner.java` (JAVA) | Magnitude: 77.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 24, indent_spaces: 19, structural_boundaries: 18, doc: 8
- `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/WorkerConnector.java` (JAVA) | Magnitude: 1002.62 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 426, structural_boundaries: 98, branch: 83, func_start: 69
- `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/HandlingSourceTopicDeletionIntegrationTest.java` (JAVA) | Magnitude: 83.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 47, concurrency: 30, import: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `clients/src/main/java/org/apache/kafka/common/ClusterResourceListener.java` (JAVA) | Magnitude: 17.22 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, planned_debt: 3, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `raft/src/main/java/org/apache/kafka/raft/RaftMessageQueue.java` (JAVA) | Magnitude: 28.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, args: 4, func_start: 4
- `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/OffsetExpirationCondition.java` (JAVA) | Magnitude: 18.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `clients/src/main/java/org/apache/kafka/common/requests/SaslAuthenticateResponse.java` (JAVA) | Magnitude: 65.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 21, api: 16, func_start: 12
- `connect/runtime/src/test/java/org/apache/kafka/connect/util/TopicCreationTest.java` (JAVA) | Magnitude: 168.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 457, func_start: 232, test: 229, structural_boundaries: 92
- `coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorBackgroundThreadPoolExecutor.java` (JAVA) | Magnitude: 44.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 13, import: 6, safety: 5
- `metadata/src/main/java/org/apache/kafka/image/loader/SnapshotManifest.java` (JAVA) | Magnitude: 6.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, api: 3, doc: 3
- `metadata/src/test/java/org/apache/kafka/controller/errors/ControllerExceptionsTest.java` (JAVA) | Magnitude: 71.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 40, func_start: 30, test: 26

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> Churn: **95.8%** | Cog Load: 56.9031% | Debt: 0.0%
- `streams/src/test/java/org/apache/kafka/streams/processor/internals/TaskManagerTest.java` -> Churn: **80.17%** | Cog Load: 86.4046% | Debt: 0.0%
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareConsumerImpl.java` -> Churn: **76.8%** | Cog Load: 25.1057% | Debt: 88.2682%
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/AsyncKafkaConsumer.java` -> Churn: **70.53%** | Cog Load: 45.798% | Debt: 65.8902%
- `streams/test-utils/src/main/java/org/apache/kafka/streams/TopologyTestDriver.java` -> Churn: **70.31%** | Cog Load: 9.4077% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 3027.74
- `clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java` -> **Jonah Hooper** (100.0% isolated ownership) | Magnitude: 2689.84
- `streams/src/main/java/org/apache/kafka/streams/state/internals/RocksDBGenericOptionsToDbOptionsColumnFamilyOptionsAdapter.java` -> **Eduwer Camacaro** (100.0% isolated ownership) | Magnitude: 2389.3
- `connect/json/src/test/java/org/apache/kafka/connect/json/JsonConverterTest.java` -> **Priyanka K U** (100.0% isolated ownership) | Magnitude: 2344.8
- `streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamImpl.java` -> **Matthias J. Sax** (100.0% isolated ownership) | Magnitude: 2339.94

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `clients/src/main/java/org/apache/kafka/clients/producer/internals/TransactionManager.java` -> **Severity: 0.159** (Bridge: 0.0024 * Flux: 66.8437%)
- `clients/src/main/java/org/apache/kafka/common/requests/ListOffsetsRequest.java` -> **Severity: 0.1** (Bridge: 0.001 * Flux: 100.0%)
- `clients/src/main/java/org/apache/kafka/common/protocol/Errors.java` -> **Severity: 0.092** (Bridge: 0.008 * Flux: 11.5049%)
- `clients/src/main/java/org/apache/kafka/common/requests/JoinGroupRequest.java` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 100.0%)
- `core/src/main/scala/kafka/network/RequestChannel.scala` -> **Severity: 0.073** (Bridge: 0.0014 * Flux: 50.8333%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `clients/src/main/java/org/apache/kafka/common/KafkaException.java` -> **Severity: 1782.085** (Blast Radius: 17.867 * Doc Risk: 99.7417%)
- `clients/src/main/java/org/apache/kafka/common/utils/Bytes.java` -> **Severity: 1500.9** (Blast Radius: 15.009 * Doc Risk: 100.0%)
- `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -> **Severity: 1341.696** (Blast Radius: 13.417 * Doc Risk: 99.9997%)
- `clients/src/main/java/org/apache/kafka/common/errors/TimeoutException.java` -> **Severity: 1316.092** (Blast Radius: 13.195 * Doc Risk: 99.7417%)
- `clients/src/main/java/org/apache/kafka/common/utils/internals/BytesUtils.java` -> **Severity: 1211.2** (Blast Radius: 12.112 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
