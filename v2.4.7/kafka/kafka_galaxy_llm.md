# ARCHITECTURAL_BRIEF: kafka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/kafka` |
| **Timestamp** | `2026-08-07T05:03:27.495063+00:00` |
| **Scan Duration** | `27.04s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `eb111f6695ef30889e7367bbad759f7e772d65ea` |
| **Git Remote** | `https://github.com/apache/kafka` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6079 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.248`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 3119 | 48.1% |
| file_cluster_8 | 2479 | 38.2% |
| file_cluster_16 | 486 | 7.5% |
| file_cluster_0 | 230 | 3.5% |
| file_cluster_4 | 109 | 1.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 15.2 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 40.1 | 49.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 17.3 | 5.7 | 5.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 43.4 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.1 | 11.1 | 0.0 |
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

- `getOrMaybeSubscribeStaticConsumerGroupMe` (@ `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java`) -> Impact: **763.8** | LOC: 1235
- `parseValue` (@ `clients/src/main/java/org/apache/kafka/common/config/ConfigDef.java`) -> Impact: **577.7** | LOC: 994
- `consumerGroupFenceMembers` (@ `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java`) -> Impact: **559.6** | LOC: 1233
- `lastOffsetAndMaxRecordsToAcquire` (@ `core/src/main/java/kafka/server/share/SharePartition.java`) -> Impact: **551.2** | LOC: 1064
- `hasRestoredToEnd` (@ `streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreChangelogReader.java`) -> Impact: **512.0** | LOC: 834
- `testFromPropsInvalid` (@ `core/src/test/scala/unit/kafka/server/KafkaConfigTest.scala`) -> Impact: **490.9** | LOC: 327
- `revokeAndReassign` (@ `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java`) -> Impact: **480.0** | LOC: 1237
- `usage_[Truncated]` (@ `tests/docker/ducker-ak`) -> Impact: **478.4** | LOC: 687
  * *Intent:* # Display a usage message on the terminal and exit. # # $1: The exit status to use
- `stopReconfiguredTasks` (@ `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java`) -> Impact: **476.2** | LOC: 803
- `updateConfigsWithIncrementalCooperative` (@ `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java`) -> Impact: **452.8** | LOC: 855

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `streams/src/test/java/org/apache/kafka/streams/state/internals` | 151 | 20706.04 | 17.0% | 0.0% |
| `streams/src/main/java/org/apache/kafka/streams/processor/internals` | 95 | 18963.4 | 16.81% | 57.26% |
| `clients/src/test/java/org/apache/kafka/clients/consumer/internals` | 67 | 16864.86 | 19.27% | 0.0% |
| `streams/src/main/java/org/apache/kafka/streams/state/internals` | 203 | 15846.72 | 11.81% | 56.66% |
| `clients/src/main/java/org/apache/kafka/clients/consumer/internals` | 97 | 15392.48 | 18.77% | 73.37% |
| `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration` | 87 | 14368.24 | 28.2% | 0.0% |
| `streams/src/test/java/org/apache/kafka/streams/processor/internals` | 73 | 13574.38 | 14.44% | 0.0% |
| `core/src/test/scala/unit/kafka/server` | 101 | 12920.78 | 23.12% | 0.0% |
| `clients/src/main/java/org/apache/kafka/common/requests` | 192 | 12378.26 | 19.31% | 29.99% |
| `group-coordinator/src/test/java/org/apache/kafka/coordinator/group` | 18 | 11731.58 | 26.53% | 0.0% |

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
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> **212** Orphaned Functions | **34** Duplicates
- `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` -> **77** Orphaned Functions | **121** Duplicates
- `streams/src/test/java/org/apache/kafka/streams/StreamsConfigTest.java` -> **145** Orphaned Functions | **29** Duplicates
- `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java` -> **133** Orphaned Functions | **35** Duplicates
- `streams/src/test/java/org/apache/kafka/streams/kstream/internals/KStreamImplTest.java` -> **93** Orphaned Functions | **69** Duplicates

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
263. **`bin/connect-distributed.sh`** -> AI Confidence: **99.29%**
264. **`bin/connect-mirror-maker.sh`** -> AI Confidence: **99.29%**
265. **`bin/connect-plugin-path.sh`** -> AI Confidence: **99.29%**
266. **`bin/connect-standalone.sh`** -> AI Confidence: **99.29%**
267. **`bin/kafka-console-consumer.sh`** -> AI Confidence: **99.29%**
268. **`bin/kafka-console-producer.sh`** -> AI Confidence: **99.29%**
269. **`bin/kafka-console-share-consumer.sh`** -> AI Confidence: **99.29%**
270. **`bin/kafka-consumer-perf-test.sh`** -> AI Confidence: **99.29%**
271. **`bin/kafka-producer-perf-test.sh`** -> AI Confidence: **99.29%**
272. **`bin/kafka-run-class.sh`** -> AI Confidence: **99.29%**
273. **`bin/kafka-server-start.sh`** -> AI Confidence: **99.29%**
274. **`bin/kafka-share-consumer-perf-test.sh`** -> AI Confidence: **99.29%**
275. **`bin/kafka-streams-application-reset.sh`** -> AI Confidence: **99.29%**
276. **`bin/kafka-verifiable-consumer.sh`** -> AI Confidence: **99.29%**
277. **`bin/kafka-verifiable-producer.sh`** -> AI Confidence: **99.29%**
278. **`bin/kafka-verifiable-share-consumer.sh`** -> AI Confidence: **99.29%**
279. **`docker/docker_official_images/3.7.0/jvm/jsa_launch`** -> AI Confidence: **99.29%**
280. **`docker/jvm/jsa_launch`** -> AI Confidence: **99.29%**
281. **`examples/bin/exactly-once-demo.sh`** -> AI Confidence: **99.29%**
282. **`examples/bin/java-producer-consumer-demo.sh`** -> AI Confidence: **99.29%**
283. **`jmh-benchmarks/jmh.sh`** -> AI Confidence: **99.29%**
284. **`raft/bin/test-kraft-server-start.sh`** -> AI Confidence: **99.29%**
285. **`tests/bin/flatten_html.sh`** -> AI Confidence: **99.29%**
286. **`tests/docker/run_tests.sh`** -> AI Confidence: **99.29%**
287. **`vagrant/aws/aws-init.sh`** -> AI Confidence: **99.29%**
288. **`Vagrantfile`** -> AI Confidence: **99.29%**
289. **`tests/docker/Dockerfile`** -> AI Confidence: **99.29%**
290. **`gradle/dependencies.gradle`** -> AI Confidence: **99.29%**
291. **`clients/src/main/java/org/apache/kafka/clients/NetworkClient.java`** -> AI Confidence: **99.25%**
292. **`clients/src/main/java/org/apache/kafka/clients/consumer/ConsumerConfig.java`** -> AI Confidence: **99.25%**
293. **`clients/src/main/java/org/apache/kafka/clients/producer/ProducerConfig.java`** -> AI Confidence: **99.25%**
294. **`clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java`** -> AI Confidence: **99.25%**
295. **`clients/src/main/java/org/apache/kafka/server/authorizer/Authorizer.java`** -> AI Confidence: **99.25%**
296. **`server-common/src/main/java/org/apache/kafka/server/common/MetadataVersion.java`** -> AI Confidence: **99.25%**
297. **`server-common/src/main/java/org/apache/kafka/server/config/QuotaConfig.java`** -> AI Confidence: **99.25%**
298. **`server-common/src/main/java/org/apache/kafka/server/purgatory/DelayedOperationPurgatory.java`** -> AI Confidence: **99.25%**
299. **`server-common/src/main/java/org/apache/kafka/server/share/persister/PersisterStateManager.java`** -> AI Confidence: **99.25%**
300. **`server-common/src/main/java/org/apache/kafka/server/util/CommandLineUtils.java`** -> AI Confidence: **99.25%**
301. **`server/src/main/java/org/apache/kafka/network/SocketServerConfigs.java`** -> AI Confidence: **99.25%**
302. **`test-common/test-common-internal-api/src/main/java/org/apache/kafka/common/test/api/ClusterTest.java`** -> AI Confidence: **99.25%**
303. **`core/src/main/scala/kafka/network/SocketServer.scala`** -> AI Confidence: **99.25%**
304. **`core/src/main/scala/kafka/server/KafkaConfig.scala`** -> AI Confidence: **99.25%**
305. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/MetricsDuringTopicCreationDeletionTest.java`** -> AI Confidence: **99.24%**
306. **`clients/src/main/java/org/apache/kafka/clients/ClientUtils.java`** -> AI Confidence: **99.24%**
307. **`clients/src/main/java/org/apache/kafka/clients/Metadata.java`** -> AI Confidence: **99.24%**
308. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/AbortTransactionHandler.java`** -> AI Confidence: **99.24%**
309. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/CoordinatorStrategy.java`** -> AI Confidence: **99.24%**
310. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DeleteConsumerGroupOffsetsHandler.java`** -> AI Confidence: **99.24%**
311. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeConsumerGroupsHandler.java`** -> AI Confidence: **99.24%**
312. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeProducersHandler.java`** -> AI Confidence: **99.24%**
313. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeStreamsGroupsHandler.java`** -> AI Confidence: **99.24%**
314. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/DescribeTransactionsHandler.java`** -> AI Confidence: **99.24%**
315. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/FenceProducersHandler.java`** -> AI Confidence: **99.24%**
316. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/ListConsumerGroupOffsetsHandler.java`** -> AI Confidence: **99.24%**
317. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/ListShareGroupOffsetsHandler.java`** -> AI Confidence: **99.24%**
318. **`clients/src/main/java/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.java`** -> AI Confidence: **99.24%**
319. **`clients/src/main/java/org/apache/kafka/clients/consumer/RangeAssignor.java`** -> AI Confidence: **99.24%**
320. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/AutoOffsetResetStrategy.java`** -> AI Confidence: **99.24%**
321. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerCoordinator.java`** -> AI Confidence: **99.24%**
322. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/FetchBuffer.java`** -> AI Confidence: **99.24%**
323. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/OffsetsRequestManager.java`** -> AI Confidence: **99.24%**
324. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/TopicMetadataFetcher.java`** -> AI Confidence: **99.24%**
325. **`clients/src/main/java/org/apache/kafka/common/config/AbstractConfig.java`** -> AI Confidence: **99.24%**
326. **`clients/src/main/java/org/apache/kafka/common/config/internals/BrokerSecurityConfigs.java`** -> AI Confidence: **99.24%**
327. **`clients/src/main/java/org/apache/kafka/common/metrics/internals/IntGaugeSuite.java`** -> AI Confidence: **99.24%**
328. **`clients/src/main/java/org/apache/kafka/common/network/SaslChannelBuilder.java`** -> AI Confidence: **99.24%**
329. **`clients/src/main/java/org/apache/kafka/common/protocol/Errors.java`** -> AI Confidence: **99.24%**
330. **`clients/src/main/java/org/apache/kafka/common/record/internal/ControlRecordType.java`** -> AI Confidence: **99.24%**
331. **`clients/src/main/java/org/apache/kafka/common/record/internal/DefaultRecord.java`** -> AI Confidence: **99.24%**
332. **`clients/src/main/java/org/apache/kafka/common/record/internal/LegacyRecord.java`** -> AI Confidence: **99.24%**
333. **`clients/src/main/java/org/apache/kafka/common/record/internal/MultiRecordsSend.java`** -> AI Confidence: **99.24%**
334. **`clients/src/main/java/org/apache/kafka/common/security/JaasConfig.java`** -> AI Confidence: **99.24%**
335. **`clients/src/main/java/org/apache/kafka/common/security/authenticator/SaslClientCallbackHandler.java`** -> AI Confidence: **99.24%**
336. **`clients/src/main/java/org/apache/kafka/common/security/kerberos/KerberosClientCallbackHandler.java`** -> AI Confidence: **99.24%**
337. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/OAuthBearerLoginModule.java`** -> AI Confidence: **99.24%**
338. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/expiring/ExpiringCredentialRefreshingLogin.java`** -> AI Confidence: **99.24%**
339. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/ConfigurationUtils.java`** -> AI Confidence: **99.24%**
340. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/RefreshingHttpsJwks.java`** -> AI Confidence: **99.24%**
341. **`clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/unsecured/OAuthBearerUnsecuredValidatorCallbackHandler.java`** -> AI Confidence: **99.24%**
342. **`clients/src/main/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactory.java`** -> AI Confidence: **99.24%**
343. **`clients/src/main/java/org/apache/kafka/common/serialization/ListDeserializer.java`** -> AI Confidence: **99.24%**
344. **`clients/src/main/java/org/apache/kafka/common/serialization/ListSerializer.java`** -> AI Confidence: **99.24%**
345. **`clients/src/main/java/org/apache/kafka/common/serialization/UUIDDeserializer.java`** -> AI Confidence: **99.24%**
346. **`clients/src/main/java/org/apache/kafka/common/utils/SecurityUtils.java`** -> AI Confidence: **99.24%**
347. **`clients/src/main/java/org/apache/kafka/common/utils/Utils.java`** -> AI Confidence: **99.24%**
348. **`clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java`** -> AI Confidence: **99.24%**
349. **`clients/src/test/java/org/apache/kafka/clients/consumer/internals/ConsumerHeartbeatRequestManagerTest.java`** -> AI Confidence: **99.24%**
350. **`clients/src/test/java/org/apache/kafka/common/message/ApiMessageTypeTest.java`** -> AI Confidence: **99.24%**
351. **`clients/src/test/java/org/apache/kafka/common/network/EchoServer.java`** -> AI Confidence: **99.24%**
352. **`clients/src/test/java/org/apache/kafka/common/protocol/ApiKeysTest.java`** -> AI Confidence: **99.24%**
353. **`clients/src/test/java/org/apache/kafka/common/security/authenticator/TestDigestLoginModule.java`** -> AI Confidence: **99.24%**
354. **`clients/src/test/java/org/apache/kafka/common/security/oauthbearer/internals/secured/CachedFileTest.java`** -> AI Confidence: **99.24%**
355. **`clients/src/test/java/org/apache/kafka/common/security/oauthbearer/internals/unsecured/OAuthBearerUnsecuredJwsTest.java`** -> AI Confidence: **99.24%**
356. **`clients/src/test/java/org/apache/kafka/common/utils/annotation/ApiKeyVersionsProviderTest.java`** -> AI Confidence: **99.24%**
357. **`connect/basic-auth-extension/src/main/java/org/apache/kafka/connect/rest/basic/auth/extension/PropertyFileLoginModule.java`** -> AI Confidence: **99.24%**
358. **`connect/json/src/main/java/org/apache/kafka/connect/json/JsonConverterConfig.java`** -> AI Confidence: **99.24%**
359. **`connect/mirror/src/main/java/org/apache/kafka/connect/mirror/CheckpointStore.java`** -> AI Confidence: **99.24%**
360. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/SourceTaskOffsetCommitter.java`** -> AI Confidence: **99.24%**
361. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/WorkerConnector.java`** -> AI Confidence: **99.24%**
362. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/WorkerSinkTask.java`** -> AI Confidence: **99.24%**
363. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedConfig.java`** -> AI Confidence: **99.24%**
364. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/errors/RetryWithToleranceOperator.java`** -> AI Confidence: **99.24%**
365. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/isolation/ReflectionScanner.java`** -> AI Confidence: **99.24%**
366. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/RestClient.java`** -> AI Confidence: **99.24%**
367. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/RestServer.java`** -> AI Confidence: **99.24%**
368. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/util/SSLUtils.java`** -> AI Confidence: **99.24%**
369. **`connect/runtime/src/main/java/org/apache/kafka/connect/storage/OffsetStorageWriter.java`** -> AI Confidence: **99.24%**
370. **`connect/runtime/src/main/java/org/apache/kafka/connect/util/RetryUtil.java`** -> AI Confidence: **99.24%**
371. **`connect/runtime/src/test/java/org/apache/kafka/connect/integration/BlockingConnectorTest.java`** -> AI Confidence: **99.24%**
372. **`connect/runtime/src/test/java/org/apache/kafka/connect/integration/ConnectorTopicsIntegrationTest.java`** -> AI Confidence: **99.24%**
373. **`connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java`** -> AI Confidence: **99.24%**
374. **`connect/runtime/src/test/java/org/apache/kafka/connect/runtime/isolation/TestPlugins.java`** -> AI Confidence: **99.24%**
375. **`connect/runtime/src/test/java/org/apache/kafka/connect/util/clusters/EmbeddedConnect.java`** -> AI Confidence: **99.24%**
376. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorLoaderImpl.java`** -> AI Confidence: **99.24%**
377. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorRuntime.java`** -> AI Confidence: **99.24%**
378. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorRuntimeMetricsImpl.java`** -> AI Confidence: **99.24%**
379. **`coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/MultiThreadedEventProcessor.java`** -> AI Confidence: **99.24%**
380. **`coordinator-common/src/test/java/org/apache/kafka/coordinator/common/runtime/DeferredEventCollectionTest.java`** -> AI Confidence: **99.24%**
381. **`core/src/main/java/kafka/server/share/DelayedShareFetch.java`** -> AI Confidence: **99.24%**
382. **`examples/src/main/java/kafka/examples/TransactionalClientDemo.java`** -> AI Confidence: **99.24%**
383. **`generator/src/main/java/org/apache/kafka/message/MessageGenerator.java`** -> AI Confidence: **99.24%**
384. **`generator/src/test/java/org/apache/kafka/message/MessageGeneratorTest.java`** -> AI Confidence: **99.24%**
385. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupConfig.java`** -> AI Confidence: **99.24%**
386. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java`** -> AI Confidence: **99.24%**
387. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/Utils.java`** -> AI Confidence: **99.24%**
388. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/modern/consumer/ConsumerGroup.java`** -> AI Confidence: **99.24%**
389. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/modern/consumer/CurrentAssignmentBuilder.java`** -> AI Confidence: **99.24%**
390. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/CurrentAssignmentBuilder.java`** -> AI Confidence: **99.24%**
391. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/StreamsTopology.java`** -> AI Confidence: **99.24%**
392. **`group-coordinator/src/main/java/org/apache/kafka/coordinator/group/streams/topics/ChangelogTopics.java`** -> AI Confidence: **99.24%**
393. **`jmh-benchmarks/src/main/java/org/apache/kafka/jmh/connect/ValuesBenchmark.java`** -> AI Confidence: **99.24%**
394. **`metadata/src/main/java/org/apache/kafka/controller/AclControlManager.java`** -> AI Confidence: **99.24%**
395. **`metadata/src/main/java/org/apache/kafka/controller/ClientQuotaControlManager.java`** -> AI Confidence: **99.24%**
396. **`metadata/src/main/java/org/apache/kafka/controller/ConfigurationControlManager.java`** -> AI Confidence: **99.24%**
397. **`metadata/src/main/java/org/apache/kafka/controller/PeriodicTaskControlManager.java`** -> AI Confidence: **99.24%**
398. **`metadata/src/main/java/org/apache/kafka/image/ClientQuotasImage.java`** -> AI Confidence: **99.24%**
399. **`metadata/src/main/java/org/apache/kafka/image/MetadataDelta.java`** -> AI Confidence: **99.24%**
400. **`metadata/src/main/java/org/apache/kafka/image/loader/MetadataLoader.java`** -> AI Confidence: **99.24%**
401. **`metadata/src/main/java/org/apache/kafka/image/publisher/BrokerRegistrationTracker.java`** -> AI Confidence: **99.24%**
402. **`metadata/src/main/java/org/apache/kafka/metadata/KafkaConfigSchema.java`** -> AI Confidence: **99.24%**
403. **`metadata/src/main/java/org/apache/kafka/metadata/authorizer/StandardAuthorizerData.java`** -> AI Confidence: **99.24%**
404. **`metadata/src/main/java/org/apache/kafka/metadata/storage/ScramParser.java`** -> AI Confidence: **99.24%**
405. **`metadata/src/test/java/org/apache/kafka/controller/metrics/ControllerMetadataMetricsTest.java`** -> AI Confidence: **99.24%**
406. **`metadata/src/test/java/org/apache/kafka/metadata/RecordTestUtils.java`** -> AI Confidence: **99.24%**
407. **`raft/src/main/java/org/apache/kafka/raft/ControlRecord.java`** -> AI Confidence: **99.24%**
408. **`raft/src/main/java/org/apache/kafka/raft/ElectionState.java`** -> AI Confidence: **99.24%**
409. **`raft/src/main/java/org/apache/kafka/raft/QuorumState.java`** -> AI Confidence: **99.24%**
410. **`raft/src/main/java/org/apache/kafka/raft/internals/RecordsIterator.java`** -> AI Confidence: **99.24%**
411. **`raft/src/main/java/org/apache/kafka/raft/internals/RemoveVoterHandler.java`** -> AI Confidence: **99.24%**
412. **`raft/src/test/java/org/apache/kafka/raft/ReplicatedCounter.java`** -> AI Confidence: **99.24%**
413. **`server-common/src/main/java/org/apache/kafka/server/network/EndpointReadyFutures.java`** -> AI Confidence: **99.24%**
414. **`server/src/main/java/org/apache/kafka/server/config/ReplicationConfigs.java`** -> AI Confidence: **99.24%**
415. **`server/src/main/java/org/apache/kafka/server/controller/ControllerRegistrationManager.java`** -> AI Confidence: **99.24%**
416. **`server/src/test/java/org/apache/kafka/server/metrics/ForwardingManagerMetricsTest.java`** -> AI Confidence: **99.24%**
417. **`storage/src/test/java/org/apache/kafka/tiered/storage/actions/ConsumeAction.java`** -> AI Confidence: **99.24%**
418. **`streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/KTableEfficientRangeQueryTest.java`** -> AI Confidence: **99.24%**
419. **`streams/src/main/java/org/apache/kafka/streams/kstream/TimeWindowedDeserializer.java`** -> AI Confidence: **99.24%**
420. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamImpl.java`** -> AI Confidence: **99.24%**
421. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KStreamImplJoin.java`** -> AI Confidence: **99.24%**
422. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/KeyValueStoreMaterializer.java`** -> AI Confidence: **99.24%**
423. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/StreamJoinedStoreFactory.java`** -> AI Confidence: **99.24%**
424. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/foreignkeyjoin/SubscriptionJoinProcessorSupplier.java`** -> AI Confidence: **99.24%**
425. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/graph/StreamSourceNode.java`** -> AI Confidence: **99.24%**
426. **`streams/src/main/java/org/apache/kafka/streams/processor/assignment/assignors/StickyTaskAssignor.java`** -> AI Confidence: **99.24%**
427. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/ChangelogTopics.java`** -> AI Confidence: **99.24%**
428. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/GlobalStreamThread.java`** -> AI Confidence: **99.24%**
429. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/PartitionGroup.java`** -> AI Confidence: **99.24%**
430. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RecordCollectorImpl.java`** -> AI Confidence: **99.24%**
431. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RecordDeserializer.java`** -> AI Confidence: **99.24%**
432. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/RecordQueue.java`** -> AI Confidence: **99.24%**
433. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/SinkNode.java`** -> AI Confidence: **99.24%**
434. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StateDirectory.java`** -> AI Confidence: **99.24%**
435. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StreamsPartitionAssignor.java`** -> AI Confidence: **99.24%**
436. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/TaskExecutionMetadata.java`** -> AI Confidence: **99.24%**
437. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/Tasks.java`** -> AI Confidence: **99.24%**
438. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/LegacyStickyTaskAssignor.java`** -> AI Confidence: **99.24%**
439. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/MinTrafficGraphConstructor.java`** -> AI Confidence: **99.24%**
440. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/assignment/TaskMovement.java`** -> AI Confidence: **99.24%**
441. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/tasks/DefaultTaskManager.java`** -> AI Confidence: **99.24%**
442. **`streams/src/main/java/org/apache/kafka/streams/query/Position.java`** -> AI Confidence: **99.24%**
443. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CachingKeyValueStore.java`** -> AI Confidence: **99.24%**
444. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CachingSessionStore.java`** -> AI Confidence: **99.24%**
445. **`streams/src/main/java/org/apache/kafka/streams/state/internals/CachingWindowStore.java`** -> AI Confidence: **99.24%**
446. **`streams/src/main/java/org/apache/kafka/streams/state/internals/InMemoryWindowStore.java`** -> AI Confidence: **99.24%**
447. **`streams/src/main/java/org/apache/kafka/streams/state/internals/LogicalSegmentIterator.java`** -> AI Confidence: **99.24%**
448. **`streams/src/main/java/org/apache/kafka/streams/state/internals/MeteredWindowStore.java`** -> AI Confidence: **99.24%**
449. **`streams/src/main/java/org/apache/kafka/streams/state/internals/PositionSerde.java`** -> AI Confidence: **99.24%**
450. **`streams/src/main/java/org/apache/kafka/streams/state/internals/RocksDBTimeOrderedWindowStore.java`** -> AI Confidence: **99.24%**
451. **`streams/src/main/java/org/apache/kafka/streams/state/internals/WrappedStateStore.java`** -> AI Confidence: **99.24%**
452. **`streams/src/test/java/org/apache/kafka/streams/internals/ApiUtilsTest.java`** -> AI Confidence: **99.24%**
453. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/NamedTopologyTest.java`** -> AI Confidence: **99.24%**
454. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/ReadOnlyTaskTest.java`** -> AI Confidence: **99.24%**
455. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/StateManagerUtilConverterTest.java`** -> AI Confidence: **99.24%**
456. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/StateManagerUtilTest.java`** -> AI Confidence: **99.24%**
457. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/assignment/TaskMovementTest.java`** -> AI Confidence: **99.24%**
458. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/metrics/RebalanceListenerMetricsTest.java`** -> AI Confidence: **99.24%**
459. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/metrics/TaskMetricsTest.java`** -> AI Confidence: **99.24%**
460. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/metrics/ThreadMetricsTest.java`** -> AI Confidence: **99.24%**
461. **`streams/src/test/java/org/apache/kafka/streams/processor/internals/tasks/DefaultTaskExecutorTest.java`** -> AI Confidence: **99.24%**
462. **`streams/src/test/java/org/apache/kafka/streams/state/internals/SessionStoreFetchTest.java`** -> AI Confidence: **99.24%**
463. **`streams/src/test/java/org/apache/kafka/streams/state/internals/metrics/RocksDBMetricsTest.java`** -> AI Confidence: **99.24%**
464. **`streams/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
465. **`streams/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
466. **`streams/src/test/java/org/apache/kafka/test/MockApiProcessor.java`** -> AI Confidence: **99.24%**
467. **`streams/upgrade-system-tests-24/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
468. **`streams/upgrade-system-tests-25/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
469. **`streams/upgrade-system-tests-26/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
470. **`streams/upgrade-system-tests-27/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
471. **`streams/upgrade-system-tests-28/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
472. **`streams/upgrade-system-tests-30/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
473. **`streams/upgrade-system-tests-30/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
474. **`streams/upgrade-system-tests-31/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
475. **`streams/upgrade-system-tests-31/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
476. **`streams/upgrade-system-tests-32/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
477. **`streams/upgrade-system-tests-32/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
478. **`streams/upgrade-system-tests-33/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
479. **`streams/upgrade-system-tests-33/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
480. **`streams/upgrade-system-tests-34/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
481. **`streams/upgrade-system-tests-34/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
482. **`streams/upgrade-system-tests-35/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
483. **`streams/upgrade-system-tests-35/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
484. **`streams/upgrade-system-tests-36/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
485. **`streams/upgrade-system-tests-36/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
486. **`streams/upgrade-system-tests-37/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
487. **`streams/upgrade-system-tests-37/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
488. **`streams/upgrade-system-tests-38/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
489. **`streams/upgrade-system-tests-38/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
490. **`streams/upgrade-system-tests-39/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
491. **`streams/upgrade-system-tests-39/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
492. **`streams/upgrade-system-tests-40/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
493. **`streams/upgrade-system-tests-40/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
494. **`streams/upgrade-system-tests-41/src/test/java/org/apache/kafka/streams/tests/SmokeTestClient.java`** -> AI Confidence: **99.24%**
495. **`streams/upgrade-system-tests-41/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java`** -> AI Confidence: **99.24%**
496. **`tools/src/main/java/org/apache/kafka/tools/ConsoleProducer.java`** -> AI Confidence: **99.24%**
497. **`tools/src/main/java/org/apache/kafka/tools/DelegationTokenCommand.java`** -> AI Confidence: **99.24%**
498. **`tools/src/main/java/org/apache/kafka/tools/DumpLogSegments.java`** -> AI Confidence: **99.24%**
499. **`tools/src/main/java/org/apache/kafka/tools/EndToEndLatency.java`** -> AI Confidence: **99.24%**
500. **`tools/src/main/java/org/apache/kafka/tools/GroupsCommand.java`** -> AI Confidence: **99.24%**
501. **`tools/src/main/java/org/apache/kafka/tools/LeaderElectionCommand.java`** -> AI Confidence: **99.24%**
502. **`tools/src/main/java/org/apache/kafka/tools/OffsetsUtils.java`** -> AI Confidence: **99.24%**
503. **`tools/src/main/java/org/apache/kafka/tools/ProducerPerformance.java`** -> AI Confidence: **99.24%**
504. **`tools/src/main/java/org/apache/kafka/tools/ReplicaVerificationTool.java`** -> AI Confidence: **99.24%**
505. **`tools/src/main/java/org/apache/kafka/tools/TopicCommand.java`** -> AI Confidence: **99.24%**
506. **`tools/src/main/java/org/apache/kafka/tools/consumer/ConsoleConsumer.java`** -> AI Confidence: **99.24%**
507. **`tools/src/main/java/org/apache/kafka/tools/consumer/group/ConsumerGroupCommand.java`** -> AI Confidence: **99.24%**
508. **`tools/src/main/java/org/apache/kafka/tools/reassign/ReassignPartitionsCommand.java`** -> AI Confidence: **99.24%**
509. **`tools/src/test/java/org/apache/kafka/tools/JmxToolTest.java`** -> AI Confidence: **99.24%**
510. **`tools/src/test/java/org/apache/kafka/tools/consumer/DefaultMessageFormatterTest.java`** -> AI Confidence: **99.24%**
511. **`transaction-coordinator/src/main/java/org/apache/kafka/coordinator/transaction/RPCProducerIdManager.java`** -> AI Confidence: **99.24%**
512. **`trogdor/src/main/java/org/apache/kafka/trogdor/coordinator/CoordinatorClient.java`** -> AI Confidence: **99.24%**
513. **`trogdor/src/main/java/org/apache/kafka/trogdor/coordinator/TaskManager.java`** -> AI Confidence: **99.24%**
514. **`trogdor/src/main/java/org/apache/kafka/trogdor/fault/DegradedNetworkFaultWorker.java`** -> AI Confidence: **99.24%**
515. **`core/src/main/scala/kafka/coordinator/transaction/TransactionMarkerChannelManager.scala`** -> AI Confidence: **99.24%**
516. **`core/src/main/scala/kafka/server/AlterPartitionManager.scala`** -> AI Confidence: **99.24%**
517. **`core/src/main/scala/kafka/server/AuthHelper.scala`** -> AI Confidence: **99.24%**
518. **`core/src/main/scala/kafka/server/BrokerServer.scala`** -> AI Confidence: **99.24%**
519. **`core/src/main/scala/kafka/server/KafkaRequestHandler.scala`** -> AI Confidence: **99.24%**
520. **`core/src/main/scala/kafka/tools/TestRaftRequestHandler.scala`** -> AI Confidence: **99.24%**
521. **`core/src/test/scala/integration/kafka/api/CustomQuotaCallbackTest.scala`** -> AI Confidence: **99.24%**
522. **`core/src/test/scala/integration/kafka/api/MetricsTest.scala`** -> AI Confidence: **99.24%**
523. **`core/src/test/scala/integration/kafka/api/SaslClientsWithInvalidCredentialsTest.scala`** -> AI Confidence: **99.24%**
524. **`core/src/test/scala/integration/kafka/api/TransactionsTest.scala`** -> AI Confidence: **99.24%**
525. **`core/src/test/scala/integration/kafka/network/DynamicConnectionQuotaTest.scala`** -> AI Confidence: **99.24%**
526. **`core/src/test/scala/unit/kafka/network/ConnectionQuotasTest.scala`** -> AI Confidence: **99.24%**
527. **`core/src/test/scala/unit/kafka/server/StreamsGroupHeartbeatRequestTest.scala`** -> AI Confidence: **99.24%**
528. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/AutoTopicCreationTest.java`** -> AI Confidence: **99.23%**
529. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/StreamsRebalanceListenerInvoker.java`** -> AI Confidence: **99.23%**
530. **`clients/src/main/java/org/apache/kafka/common/config/TopicConfig.java`** -> AI Confidence: **99.23%**
531. **`clients/src/main/java/org/apache/kafka/common/internals/KafkaFutureImpl.java`** -> AI Confidence: **99.23%**
532. **`clients/src/main/java/org/apache/kafka/common/protocol/types/TaggedFields.java`** -> AI Confidence: **99.23%**
533. **`clients/src/main/java/org/apache/kafka/common/requests/DescribeClientQuotasRequest.java`** -> AI Confidence: **99.23%**
534. **`clients/src/main/java/org/apache/kafka/common/security/kerberos/KerberosError.java`** -> AI Confidence: **99.23%**
535. **`clients/src/main/java/org/apache/kafka/common/utils/ByteUtils.java`** -> AI Confidence: **99.23%**
536. **`clients/src/main/java/org/apache/kafka/common/utils/ChildFirstClassLoader.java`** -> AI Confidence: **99.23%**
537. **`clients/src/main/java/org/apache/kafka/common/utils/ConfigUtils.java`** -> AI Confidence: **99.23%**
538. **`connect/runtime/src/main/java/org/apache/kafka/connect/runtime/rest/ConnectRestConfigurable.java`** -> AI Confidence: **99.23%**
539. **`metadata/src/main/java/org/apache/kafka/image/FeaturesDelta.java`** -> AI Confidence: **99.23%**
540. **`metadata/src/test/java/org/apache/kafka/controller/metrics/QuorumControllerMetricsTest.java`** -> AI Confidence: **99.23%**
541. **`raft/src/main/java/org/apache/kafka/raft/RequestManager.java`** -> AI Confidence: **99.23%**
542. **`server-common/src/main/java/org/apache/kafka/metadata/AssignmentsHelper.java`** -> AI Confidence: **99.23%**
543. **`server/src/main/java/org/apache/kafka/server/replica/Replica.java`** -> AI Confidence: **99.23%**
544. **`server/src/test/java/org/apache/kafka/network/SocketServerConfigsTest.java`** -> AI Confidence: **99.23%**
545. **`share-coordinator/src/main/java/org/apache/kafka/coordinator/share/PersisterStateBatchCombiner.java`** -> AI Confidence: **99.23%**
546. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/foreignkeyjoin/SubscriptionResponseWrapperSerde.java`** -> AI Confidence: **99.23%**
547. **`streams/src/main/java/org/apache/kafka/streams/kstream/internals/graph/StreamSinkNode.java`** -> AI Confidence: **99.23%**
548. **`streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreBuilderWrapper.java`** -> AI Confidence: **99.23%**
549. **`trogdor/src/test/java/org/apache/kafka/trogdor/basic/BasicPlatformTest.java`** -> AI Confidence: **99.23%**
550. **`core/src/test/scala/unit/kafka/server/DelayedProduceTest.scala`** -> AI Confidence: **99.23%**
551. **`generator/src/test/java/org/apache/kafka/message/MessageDataGeneratorTest.java`** -> AI Confidence: **99.22%**
552. **`shell/src/main/java/org/apache/kafka/shell/glob/GlobComponent.java`** -> AI Confidence: **99.2%**
553. **`committer-tools/refresh_collaborators.py`** -> AI Confidence: **99.18%**
554. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/CreateTopicsRequestWithPolicyTest.java`** -> AI Confidence: **99.18%**
555. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/TransactionsExpirationTest.java`** -> AI Confidence: **99.18%**
556. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/DeleteTopicTest.java`** -> AI Confidence: **99.18%**
557. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/RackAwareAutoTopicCreationTest.java`** -> AI Confidence: **99.18%**
558. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ConsumerBounceTest.java`** -> AI Confidence: **99.18%**
559. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java`** -> AI Confidence: **99.18%**
560. **`clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/producer/ProducerCompressionTest.java`** -> AI Confidence: **99.18%**
561. **`clients/src/main/java/org/apache/kafka/clients/admin/Admin.java`** -> AI Confidence: **99.18%**
562. **`clients/src/main/java/org/apache/kafka/clients/admin/DescribeProducersResult.java`** -> AI Confidence: **99.18%**
563. **`clients/src/main/java/org/apache/kafka/clients/admin/DescribeReplicaLogDirsResult.java`** -> AI Confidence: **99.18%**
564. **`clients/src/main/java/org/apache/kafka/clients/admin/DescribeTopicsResult.java`** -> AI Confidence: **99.18%**
565. **`clients/src/main/java/org/apache/kafka/clients/admin/ElectLeadersResult.java`** -> AI Confidence: **99.18%**
566. **`clients/src/main/java/org/apache/kafka/clients/admin/ListConsumerGroupOffsetsResult.java`** -> AI Confidence: **99.18%**
567. **`clients/src/main/java/org/apache/kafka/clients/admin/ListConsumerGroupsOptions.java`** -> AI Confidence: **99.18%**
568. **`clients/src/main/java/org/apache/kafka/clients/admin/ShareGroupDescription.java`** -> AI Confidence: **99.18%**
569. **`clients/src/main/java/org/apache/kafka/clients/admin/StreamsGroupDescription.java`** -> AI Confidence: **99.18%**
570. **`clients/src/main/java/org/apache/kafka/clients/admin/internals/ListTransactionsHandler.java`** -> AI Confidence: **99.18%**
571. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ConsumerUtils.java`** -> AI Confidence: **99.18%**
572. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/CoordinatorRequestManager.java`** -> AI Confidence: **99.18%**
573. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/Deserializers.java`** -> AI Confidence: **99.18%**
574. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/PositionsValidator.java`** -> AI Confidence: **99.18%**
575. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/RequestFuture.java`** -> AI Confidence: **99.18%**
576. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareConsumerDelegateCreator.java`** -> AI Confidence: **99.18%**
577. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareSessionHandler.java`** -> AI Confidence: **99.18%**
578. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/ApplicationEventHandler.java`** -> AI Confidence: **99.18%**
579. **`clients/src/main/java/org/apache/kafka/clients/consumer/internals/metrics/SensorBuilder.java`** -> AI Confidence: **99.18%**
580. **`clients/src/main/java/org/apache/kafka/clients/producer/MockProducer.java`** -> AI Confidence: **99.18%**
581. **`clients/src/main/java/org/apache/kafka/clients/producer/internals/BuiltInPartitioner.java`** -> AI Confidence: **99.18%**
582. **`clients/src/main/java/org/apache/kafka/clients/producer/internals/ProducerBatch.java`** -> AI Confidence: **99.18%**
583. **`clients/src/main/java/org/apache/kafka/common/Cluster.java`** -> AI Confidence: **99.18%**
584. **`clients/src/main/java/org/apache/kafka/common/config/provider/FileConfigProvider.java`** -> AI Confidence: **99.18%**
585. **`clients/src/main/java/org/apache/kafka/common/internals/LegacyStrategy.java`** -> AI Confidence: **99.18%**
586. **`clients/src/main/java/org/apache/kafka/common/memory/GarbageCollectedMemoryPool.java`** -> AI Confidence: **99.18%**
587. **`clients/src/main/java/org/apache/kafka/common/metrics/stats/Frequencies.java`** -> AI Confidence: **99.18%**
588. **`clients/src/main/java/org/apache/kafka/common/network/PlaintextChannelBuilder.java`** -> AI Confidence: **99.18%**
589. **`clients/src/main/java/org/apache/kafka/common/network/SslChannelBuilder.java`** -> AI Confidence: **99.18%**
590. **`clients/src/main/java/org/apache/kafka/common/protocol/MessageUtil.java`** -> AI Confidence: **99.18%**
591. **`clients/src/main/java/org/apache/kafka/common/protocol/types/Type.java`** -> AI Confidence: **99.18%**
592. **`clients/src/main/java/org/apache/kafka/common/record/internal/DefaultRecordBatch.java`** -> AI Confidence: **99.18%**
593. **`clients/src/main/java/org/apache/kafka/common/record/internal/EndTransactionMarker.java`** -> AI Confidence: **99.18%**
594. **`clients/src/main/java/org/apache/kafka/common/record/internal/FileLogInputStream.java`** -> AI Confidence: **99.18%**
595. **`clients/src/main/java/org/apache/kafka/common/record/internal/FileRecords.java`** -> AI Confidence: **99.18%**
596. **`clients/src/main/java/org/apache/kafka/common/requests/AddPartitionsToTxnRequest.java`** -> AI Confidence: **99.18%**
597. **`clients/src/main/java/org/apache/kafka/common/requests/AddPartitionsToTxnResponse.java`** -> AI Confidence: **99.18%**
598. **`clients/src/main/java/org/apache/kafka/common/requests/AlterClientQuotasResponse.java`** -> AI Confidence: **99.18%**
599. **`clients/src/main/java/org/apache/kafka/common/requests/CreateTopicsRequest.java`** -> AI Confidence: **99.18%**
600. **`clients/src/main/java/org/apache/kafka/common/requests/DeleteTopicsRequest.java`** -> AI Confidence: **99.18%**
601. **`clients/src/main/java/org/apache/kafka/common/requests/DescribeAclsResponse.java`** -> AI Confidence: **99.18%**
602. **`clients/src/main/java/org/apache/kafka/common/requests/DescribeClientQuotasResponse.java`** -> AI Confidence: **99.18%**
603. **`clients/src/main/java/org/apache/kafka/common/requests/ElectLeadersRequest.java`** -> AI Confidence: **99.18%**
604. **`clients/src/main/java/org/apache/kafka/common/requests/FetchRequest.java`** -> AI Confidence: **99.18%**
605. **`clients/src/main/java/org/apache/kafka/common/requests/FetchSnapshotResponse.java`** -> AI Confidence: **99.18%**
606. **`clients/src/main/java/org/apache/kafka/common/requests/LeaveGroupResponse.java`** -> AI Confidence: **99.18%**
607. **`clients/src/main/java/org/apache/kafka/common/requests/ListOffsetsRequest.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `clients/src/test/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactoryTest.java` -> **99.9995%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/assertion/AssertionUtils.java` -> **99.9795%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/oauthbearer/ClientAssertionKeycloakIntegrationTest.java` -> **75.625%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactory.java` -> **68.1223%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/authenticator/SaslAuthenticatorTest.java` -> **22.6166%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `32` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `89880` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `clients/src/main/java/org/apache/kafka/common/utils/CopyOnWriteMap.java` (JAVA) -> Cumulative Risk: **764.49**
- **Archetype:** `file_cluster_4` (Distance: 11.249 IQR)
- **Magnitude:** 155.0 | **LOC:** 151 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `replace` (Impact: 6.5), `remove` (Impact: 5.6), `replace` (Impact: 5.6)

### 2. `trogdor/src/main/java/org/apache/kafka/trogdor/workload/SustainedConnectionWorker.java` (JAVA) -> Cumulative Risk: **733.32**
- **Archetype:** `file_cluster_4` (Distance: 11.058 IQR)
- **Magnitude:** 378.68 | **LOC:** 533 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.384%)
- **Heaviest Functions:** `run` (Impact: 16.5), `start` (Impact: 16.2), `refresh` (Impact: 15.5)

### 3. `clients/src/main/java/org/apache/kafka/clients/consumer/MockConsumer.java` (JAVA) -> Cumulative Risk: **707.43**
- **Archetype:** `file_cluster_4` (Distance: 11.997 IQR)
- **Magnitude:** 695.86 | **LOC:** 722 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9249%)
- **Heaviest Functions:** `poll` (Impact: 29.6), `resetOffsetPosition` (Impact: 23.4), `updateFetchPosition` (Impact: 17.7)

### 4. `connect/runtime/src/main/java/org/apache/kafka/connect/storage/MemoryStatusBackingStore.java` (JAVA) -> Cumulative Risk: **698.68**
- **Archetype:** `file_cluster_4` (Distance: 12.087 IQR)
- **Magnitude:** 146.78 | **LOC:** 144 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9757%)
- **Heaviest Functions:** `put` (Impact: 8.3), `put` (Impact: 8.3), `getAllTopics` (Impact: 7.7)

### 5. `connect/runtime/src/main/java/org/apache/kafka/connect/storage/OffsetStorageReaderImpl.java` (JAVA) -> Cumulative Risk: **692.47**
- **Archetype:** `file_cluster_4` (Distance: 11.61 IQR)
- **Magnitude:** 130.48 | **LOC:** 160 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (97.8173%)
- **Heaviest Functions:** `offsets` (Impact: 38.9), `close` (Impact: 14.2), `synchronized` (Impact: 5.5)

### 6. `clients/src/main/java/org/apache/kafka/common/memory/SimpleMemoryPool.java` (JAVA) -> Cumulative Risk: **688.95**
- **Archetype:** `file_cluster_4` (Distance: 9.679 IQR)
- **Magnitude:** 123.14 | **LOC:** 139 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (99.3319%), Tech Debt (94.9539%)
- **Heaviest Functions:** `tryAllocate` (Impact: 28.6), `maybeRecordEndOfDrySpell` (Impact: 6.5), `release` (Impact: 5.3)

### 7. `server-common/src/main/java/org/apache/kafka/server/util/KafkaScheduler.java` (JAVA) -> Cumulative Risk: **684.57**
- **Archetype:** `file_cluster_4` (Distance: 10.429 IQR)
- **Magnitude:** 180.74 | **LOC:** 195 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Concurrency (99.9914%), Documentation (98.1524%)
- **Heaviest Functions:** `schedule` (Impact: 21.4), `synchronized` (Impact: 14.9), `compareTo` (Impact: 12.7)

### 8. `clients/src/main/java/org/apache/kafka/common/requests/ShareFetchRequest.java` (JAVA) -> Cumulative Risk: **681.87**
- **Archetype:** `file_cluster_13` (Distance: 11.459 IQR)
- **Magnitude:** 195.2 | **LOC:** 242 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (94.8113%)
- **Heaviest Functions:** `forConsumer` (Impact: 50.7), `build` (Impact: 10.5), `updateForgottenData` (Impact: 7.4)

### 9. `clients/src/main/java/org/apache/kafka/clients/consumer/internals/BaseHeartbeatThread.java` (JAVA) -> Cumulative Risk: **680.13**
- **Archetype:** `file_cluster_4` (Distance: 11.645 IQR)
- **Magnitude:** 86.72 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.7357%)
- **Heaviest Functions:** `setFailureCause` (Impact: 2.4), `enable` (Impact: 2.1), `disable` (Impact: 2.1)

### 10. `clients/src/main/java/org/apache/kafka/clients/consumer/MockShareConsumer.java` (JAVA) -> Cumulative Risk: **679.07**
- **Archetype:** `file_cluster_13` (Distance: 11.609 IQR)
- **Magnitude:** 166.9 | **LOC:** 188 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), Cognitive Load (99.9491%)
- **Heaviest Functions:** `poll` (Impact: 9.4), `ensureNotClosed` (Impact: 9.1), `clientInstanceId` (Impact: 5.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.37 IQR)
- **Top Global Matches:** file_cluster_8: 13.37, file_cluster_13: 13.623, file_cluster_0: 13.643
- **Magnitude:** 5919.96 | **LOC:** 27677 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 32.5%
- **Risk Profile:** Cognitive Load (56.9035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testListGroups` (Impact: 87.0)
  * `generatePendingAssignmentCases` (Impact: 64.5)
  * `testDynamicBrokerAndGroupConfigs` (Impact: 31.0)
  * `testStreamsReconciliationProcess` (Impact: 25.7)
  * `testNewMemberJoinExpiration` (Impact: 22.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 2663`, `args: 480`, `func_start: 335`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 290`, `state_mutation: 3684`, `dead_code: 5`, `duplicate_logic: 34`, `orphaned_logic: 212`
* *Architecture:* `api: 242`, `concurrency: 5`, `import: 232`
* *Defense:* `safety: 77`, `doc: 2`, `test: 1615`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 104):` org.apache.kafka.coordinator.group.generated.StreamsGroupTopologyValue, org.junit.jupiter.api.Test, org.apache.kafka.coordinator.group.streams.TaskAssignmentTestUtil.TaskRole, org.apache.kafka.coordinator.group.GroupMetadataManagerTestContext.DEFAULT_CLIENT_ADDRESS, org.apache.kafka.image.MetadataImage, org.apache.kafka.clients.consumer.internals.ConsumerProtocol, org.apache.kafka.clients.consumer.ConsumerPartitionAssignor, org.apache.kafka.common.message.ConsumerGroupHeartbeatRequestData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/client-secrets/client.keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `streams/src/main/java/org/apache/kafka/streams/processor/internals/StateDirectory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.019 IQR)
- **Top Global Matches:** file_cluster_13: 11.019, file_cluster_4: 11.565, file_cluster_8: 11.589
- **Magnitude:** 4421.01 | **LOC:** 978 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (22.4048%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 115`, `args: 22`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 32`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 10`, `concurrency: 21`, `import: 59`
* *Defense:* `safety: 11`, `doc: 15`, `sync_locks: 9`, `immutability_locks: 62`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.001472 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` java.nio.file.Path, java.util.stream.Collectors, org.apache.kafka.streams.processor.internals.StateManagerUtil.parseTaskDirectoryName, java.util.Objects, java.nio.file.Files, org.apache.kafka.streams.errors.LockException, java.util.Arrays, org.apache.kafka.streams.processor.StateStore...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.784 IQR)
- **Top Global Matches:** file_cluster_13: 13.784, file_cluster_16: 14.158, file_cluster_11: 14.243
- **Magnitude:** 3672.08 | **LOC:** 8993 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 29.8%
- **Risk Profile:** Cognitive Load (22.3369%), Tech Debt (39.5247%)
**Top Internal Functions/Classes:**
  * `getOrMaybeSubscribeStaticConsumerGroupMe` (Impact: 763.8)
  * `consumerGroupFenceMembers` (Impact: 559.6)
  * `getOrMaybeCreatePersistedShareGroup` (Impact: 448.3)
  * `classicGroupJoin` (Impact: 157.9)
    * *Intent:* /** * Checks whether the streams group can accept a new member or not based on the
  * `alterShareGroupOffsets` (Impact: 76.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 539`, `args: 164`, `func_start: 140`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 275`, `dead_code: 4`, `duplicate_logic: 18`
* *Architecture:* `api: 68`, `concurrency: 9`, `import: 231`
* *Defense:* `safety: 72`, `doc: 333`, `sync_locks: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 124):` org.apache.kafka.coordinator.group.generated.StreamsGroupTopologyValue, org.apache.kafka.coordinator.group.modern.consumer.TopicRegexResolver, org.apache.kafka.clients.consumer.internals.ConsumerProtocol, org.apache.kafka.common.message.ConsumerGroupHeartbeatRequestData, org.apache.kafka.common.message.StreamsGroupHeartbeatResponseData.Status, org.apache.kafka.common.requests.JoinGroupRequest, org.apache.kafka.coordinator.group.generated.StreamsGroupMetadataValue, org.apache.kafka.coordinator.group.generated.ShareGroupMetadataValue...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.067 IQR)
- **Top Global Matches:** file_cluster_13: 14.067, file_cluster_0: 14.204, file_cluster_4: 14.305
- **Magnitude:** 3571.9 | **LOC:** 11791 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (66.1927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testListOffsetsHandlesFulfillmentTimeout` (Impact: 216.1)
  * `prepareDescribeQuorumResponse` (Impact: 49.9)
  * `defaultQuorumInfo` (Impact: 32.5)
  * `prepareMetadataResponse` (Impact: 23.5)
  * `testCallFailWithUnsupportedVersionExcept` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 1883`, `args: 289`, `func_start: 231`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 200`, `state_mutation: 1695`, `duplicate_logic: 35`, `orphaned_logic: 133`
* *Architecture:* `api: 149`, `concurrency: 203`, `import: 307`
* *Defense:* `safety: 221`, `doc: 4`, `test: 497`, `sync_locks: 5`, `immutability_locks: 250`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 155):` org.junit.jupiter.api.Test, org.apache.kafka.common.requests.CreateAclsResponse, org.apache.kafka.clients.consumer.ConsumerPartitionAssignor, java.util.concurrent.ExecutionException, org.apache.kafka.common.requests.MetadataRequest, org.mockito.ArgumentMatchers.anyLong, org.junit.jupiter.api.Assertions.assertDoesNotThrow, org.apache.kafka.common.errors.AuthenticationException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.784 IQR)
- **Top Global Matches:** file_cluster_13: 13.784, file_cluster_8: 14.008, file_cluster_0: 14.223
- **Magnitude:** 3408.48 | **LOC:** 4029 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (94.7116%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRequest` (Impact: 319.9)
  * `getResponse` (Impact: 319.9)
  * `verifyDescribeConfigsResponse` (Impact: 31.6)
  * `createFetchResponse` (Impact: 19.8)
  * `createDescribeConfigsResponse` (Impact: 17.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 1644`, `args: 281`, `func_start: 269`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 1657`, `duplicate_logic: 13`, `orphaned_logic: 49`
* *Architecture:* `api: 42`, `import: 305`
* *Defense:* `safety: 23`, `doc: 1`, `test: 195`, `immutability_locks: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` org.apache.kafka.common.message.OffsetForLeaderEpochRequestData.OffsetForLeaderTopic, org.junit.jupiter.api.Test, org.apache.kafka.common.message.ListPartitionReassignmentsResponseData, org.apache.kafka.common.message.ListTransactionsResponseData, org.apache.kafka.common.message.OffsetForLeaderEpochRequestData.OffsetForLeaderTopicCollection, java.util.Collections.emptyList, org.apache.kafka.common.message.BeginQuorumEpochResponseData, org.apache.kafka.common.message.DeleteRecordsResponseData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.361 IQR)
- **Top Global Matches:** file_cluster_0: 13.361, file_cluster_4: 13.393, file_cluster_13: 13.423
- **Magnitude:** 2467.88 | **LOC:** 4753 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 30.8%
- **Risk Profile:** Cognitive Load (42.9147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try` (Impact: 197.9)
  * `testConsumerCloseInGroupSequential` (Impact: 197.7)
  * `testShareConsumerAfterCoordinatorMovemen` (Impact: 39.8)
  * `testMultipleConsumersInMultipleGroupsCon` (Impact: 33.0)
  * `testFetchWithThrottledDeliveryValidateDe` (Impact: 23.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 711`, `args: 289`, `func_start: 403`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 171`, `state_mutation: 327`, `dead_code: 1`, `duplicate_logic: 121`, `orphaned_logic: 77`
* *Architecture:* `api: 84`, `concurrency: 289`, `import: 107`
* *Defense:* `safety: 144`, `doc: 5`, `test: 241`, `sync_locks: 4`, `immutability_locks: 26`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` java.util.concurrent.Future, org.apache.kafka.clients.producer.Producer, java.util.Arrays, org.apache.kafka.clients.producer.ProducerRecord, org.apache.kafka.clients.admin.AlterShareGroupOffsetsOptions, org.apache.kafka.common.errors.RecordDeserializationException, java.util.concurrent.ExecutionException, org.junit.jupiter.api.Assertions.assertDoesNotThrow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.77 IQR)
- **Top Global Matches:** file_cluster_13: 11.77, file_cluster_4: 12.098, file_cluster_0: 12.184
- **Magnitude:** 2178.04 | **LOC:** 3033 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.2794%), Tech Debt (96.6281%)
**Top Internal Functions/Classes:**
  * `stopReconfiguredTasks` (Impact: 476.2)
  * `updateConfigsWithIncrementalCooperative` (Impact: 452.8)
  * `doPutConnectorConfig` (Impact: 349.2)
  * `tick` (Impact: 90.2)
  * `doRestartConnectorAndTasks` (Impact: 57.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 262`, `args: 92`, `func_start: 76`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 38`, `dead_code: 3`, `duplicate_logic: 23`
* *Architecture:* `io: 3`, `api: 47`, `concurrency: 90`, `import: 101`
* *Defense:* `safety: 40`, `doc: 39`, `sync_locks: 7`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 62):` org.apache.kafka.common.config.ConfigDef, org.apache.kafka.connect.source.SourceConnector, java.util.concurrent.Callable, org.apache.kafka.connect.runtime.SourceConnectorConfig, java.util.concurrent.Future, org.apache.kafka.connect.util.ConnectUtils, java.util.concurrent.ExecutionException, org.apache.kafka.common.utils.Time...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.032 IQR)
- **Top Global Matches:** file_cluster_13: 12.032, file_cluster_8: 12.071, file_cluster_0: 12.193
- **Magnitude:** 2156.28 | **LOC:** 4430 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.8311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `revokeAndReassign` (Impact: 480.0)
  * `expectRebalance` (Impact: 55.8)
  * `testExternalZombieFencingRequestDelayedC` (Impact: 52.5)
  * `testModifyOffsetsSourceConnectorExactlyO` (Impact: 41.3)
    * *Intent:* // No need to check herder.connectorConfig explicitly:
  * `testJoinLeaderCatchUpFails` (Impact: 37.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 413`, `structural_boundaries: 603`, `args: 211`, `func_start: 318`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 117`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 66`, `orphaned_logic: 66`
* *Architecture:* `io: 2`, `api: 80`, `concurrency: 14`, `import: 130`
* *Defense:* `safety: 6`, `doc: 5`, `test: 570`, `immutability_locks: 66`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` org.junit.jupiter.api.Test, org.apache.kafka.connect.source.SourceConnector, java.util.concurrent.Callable, org.apache.kafka.connect.runtime.SourceConnectorConfig, java.util.concurrent.Future, java.util.concurrent.ExecutionException, org.junit.jupiter.api.extension.ExtendWith, org.apache.kafka.connect.runtime.distributed.ConnectProtocol.CONNECT_PROTOCOL_V0...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/docker/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.64 IQR)
- **Top Global Matches:** file_cluster_8: 10.64, file_cluster_13: 11.19, file_cluster_4: 11.251
- **Magnitude:** 2020.13 | **LOC:** 164 | **CtrlFlow:** 93.2% | **Authorship Centralization:** 10.0%
- **Risk Profile:** Cognitive Load (31.1811%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 5`, `args: 7`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 58`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` build-native-image
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streams/src/test/java/org/apache/kafka/streams/KafkaStreamsTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.201 IQR)
- **Top Global Matches:** file_cluster_4: 13.201, file_cluster_0: 13.362, file_cluster_13: 13.367
- **Magnitude:** 2018.14 | **LOC:** 2056 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (90.526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepareStreams` (Impact: 55.7)
  * `shouldHandleCloseAfterErrorState` (Impact: 25.8)
  * `stateShouldTransitToRunningIfNonDeadThre` (Impact: 24.0)
  * `prepareThreadState` (Impact: 23.1)
  * `prepareThreadState` (Impact: 21.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 489`, `args: 186`, `func_start: 364`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 188`, `fragile_debt: 1`, `duplicate_logic: 107`
* *Architecture:* `api: 158`, `concurrency: 463`, `import: 113`
* *Defense:* `safety: 110`, `test: 270`, `sync_locks: 1`, `immutability_locks: 311`, `cleanup: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 43):` org.junit.jupiter.api.Test, org.apache.kafka.streams.processor.internals.StateDirectory, org.apache.kafka.streams.processor.internals.StreamThread, org.junit.jupiter.api.extension.ExtendWith, org.apache.kafka.common.utils.Time, org.apache.kafka.streams.processor.api.ProcessorContext, java.util.Collections, java.util.concurrent.ThreadFactory...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/main/java/kafka/server/share/SharePartition.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.491 IQR)
- **Top Global Matches:** file_cluster_13: 13.491, file_cluster_11: 13.834, file_cluster_16: 13.855
- **Magnitude:** 2002.38 | **LOC:** 3427 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (35.5796%), Tech Debt (31.6934%)
**Top Internal Functions/Classes:**
  * `lastOffsetAndMaxRecordsToAcquire` (Impact: 551.2)
  * `acknowledgePerOffsetBatchRecords` (Impact: 113.0)
  * `acquireSubsetBatchRecords` (Impact: 98.8)
  * `maybeUpdateCachedStateAndOffsets` (Impact: 98.7)
    * *Intent:* /** * Marks the share partition as fenced. */
  * `acknowledgeBatchRecords` (Impact: 72.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 430`, `structural_boundaries: 253`, `args: 71`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 172`, `dead_code: 8`, `duplicate_logic: 9`
* *Architecture:* `api: 25`, `concurrency: 25`, `import: 73`
* *Defense:* `safety: 98`, `doc: 83`, `sync_locks: 90`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` org.apache.kafka.server.share.persister.PartitionIdLeaderEpochData, org.apache.kafka.server.share.persister.GroupTopicPartitionData, org.apache.kafka.common.protocol.Errors, org.apache.kafka.common.errors.NotLeaderOrFollowerException, org.apache.kafka.server.share.fetch.AcquisitionLockTimeoutHandler, org.apache.kafka.server.share.fetch.RecordState, org.apache.kafka.server.share.metrics.SharePartitionMetrics, java.util.Objects...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `streams/src/test/java/org/apache/kafka/streams/TopologyTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.894 IQR)
- **Top Global Matches:** file_cluster_0: 11.894, file_cluster_8: 11.986, file_cluster_13: 12.076
- **Magnitude:** 2000.92 | **LOC:** 2489 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.5865%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tableNamedMaterializedCountWithTopologyC` (Impact: 53.2)
  * `tableNamedMaterializedCountShouldPreserv` (Impact: 47.4)
  * `tableAnonymousMaterializedCountShouldPre` (Impact: 47.4)
  * `tableAnonymousStoreTypedMaterializedCoun` (Impact: 47.4)
  * `streamStreamJoinTopologyWithCustomStores` (Impact: 44.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 386`, `args: 179`, `func_start: 151`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 123`, `duplicate_logic: 33`, `orphaned_logic: 98`
* *Architecture:* `api: 112`, `import: 70`
* *Defense:* `safety: 30`, `test: 262`, `immutability_locks: 330`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` org.apache.kafka.streams.utils.TestUtils.PROCESSOR_WRAPPER_COUNTER_CONFIG, org.junit.jupiter.api.Test, org.junit.jupiter.api.Assertions.assertThrows, org.junit.jupiter.params.ParameterizedTest, java.util.HashMap, java.util.regex.Pattern, org.apache.kafka.streams.processor.internals.StoreFactory, org.apache.kafka.streams.kstream.JoinWindows...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server-common/src/test/java/org/apache/kafka/server/share/persister/PersisterStateManagerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.478 IQR)
- **Top Global Matches:** file_cluster_8: 12.478, file_cluster_0: 12.645, file_cluster_4: 12.724
- **Magnitude:** 1954.7 | **LOC:** 4939 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (28.0946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testResponseErrorHandling` (Impact: 31.1)
  * `testWriteStateRequestBatchingWithCoordin` (Impact: 26.4)
    * *Intent:* // Verifying the coordinator node was populated correctly by the FIND_COORDINATOR request
  * `testInitializeStateRequestBatchingWithCo` (Impact: 26.2)
  * `testDeleteStateRequestBatchingWithCoordi` (Impact: 26.0)
  * `fail` (Impact: 25.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 759`, `args: 175`, `func_start: 163`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 306`, `state_mutation: 525`, `duplicate_logic: 53`, `orphaned_logic: 52`
* *Architecture:* `api: 75`, `concurrency: 202`, `import: 60`
* *Defense:* `safety: 202`, `test: 278`, `immutability_locks: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` org.junit.jupiter.api.Test, org.apache.kafka.common.message.ReadShareGroupStateResponseData, org.apache.kafka.common.protocol.Errors, org.mockito.Mockito.times, java.util.Optional, org.apache.kafka.common.message.InitializeShareGroupStateResponseData, org.apache.kafka.server.util.timer.SystemTimerReaper, org.apache.kafka.common.requests.InitializeShareGroupStateResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streams/src/main/java/org/apache/kafka/streams/kstream/KStream.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.142 IQR)
- **Top Global Matches:** file_cluster_16: 11.142, file_cluster_13: 11.696, file_cluster_8: 11.928
- **Magnitude:** 1944.58 | **LOC:** 1595 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.7918%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 60`, `args: 2`, `func_start: 36`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 20`
* *Defense:* `doc: 87`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.325
  * `Choke Point (Betweenness):` 0.001925 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` org.apache.kafka.streams.processor.api.FixedKeyProcessorSupplier, org.apache.kafka.streams.processor.StateStore, org.apache.kafka.streams.processor.api.ProcessorSupplier, org.apache.kafka.common.utils.Bytes, org.apache.kafka.streams.Topology, org.apache.kafka.streams.processor.api.Processor, org.apache.kafka.streams.state.StoreBuilder, org.apache.kafka.streams.StreamsBuilder...
  * `Imported By (In-Degree: 147):` (Excluded from Brief to save tokens)

### `streams/src/main/java/org/apache/kafka/streams/kstream/KTable.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.236 IQR)
- **Top Global Matches:** file_cluster_16: 12.236, file_cluster_13: 12.867, file_cluster_8: 13.033
- **Magnitude:** 1878.27 | **LOC:** 2472 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.7918%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 60`, `args: 1`, `func_start: 40`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `doc: 276`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.841
  * `Choke Point (Betweenness):` 0.009273 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` org.apache.kafka.common.utils.Bytes, org.apache.kafka.streams.StreamsConfig, org.apache.kafka.streams.Topology, org.apache.kafka.streams.query.StateQueryRequest, org.apache.kafka.streams.processor.StreamPartitioner, java.util.function.BiFunction, org.apache.kafka.streams.state.KeyValueBytesStoreSupplier, org.apache.kafka.streams.state.ReadOnlyKeyValueStore...
  * `Imported By (In-Degree: 115):` (Excluded from Brief to save tokens)

### `streams/src/main/java/org/apache/kafka/streams/processor/internals/TaskManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.467 IQR)
- **Top Global Matches:** file_cluster_13: 13.467, file_cluster_17: 13.524, file_cluster_11: 13.576
- **Magnitude:** 1851.78 | **LOC:** 2094 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 26.7%
- **Risk Profile:** Cognitive Load (57.7104%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `closeRunningTasksDirty` (Impact: 442.5)
  * `tryCloseCleanActiveTasks` (Impact: 318.1)
  * `maybeCloseTasksFromRemovedTopologies` (Impact: 37.0)
  * `handleCorruption` (Impact: 36.0)
    * *Intent:* // we should pause consumer only within the listener since // before then the assignment has not bee...
  * `shutdownStateUpdater` (Impact: 35.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 197`, `args: 138`, `func_start: 130`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 152`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 39`
* *Architecture:* `io: 1`, `api: 55`, `concurrency: 59`, `import: 53`
* *Defense:* `safety: 62`, `doc: 33`, `sync_locks: 3`, `immutability_locks: 264`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.084
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` org.apache.kafka.clients.admin.RecordsToDelete, java.util.stream.Collectors, org.apache.kafka.streams.processor.internals.StateManagerUtil.parseTaskDirectoryName, java.util.Objects, java.util.concurrent.TimeUnit, org.apache.kafka.streams.errors.LockException, org.apache.kafka.clients.consumer.OffsetAndMetadata, java.util.Comparator...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `clients/src/test/java/org/apache/kafka/clients/consumer/internals/ConsumerCoordinatorTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.984 IQR)
- **Top Global Matches:** file_cluster_0: 12.984, file_cluster_13: 13.058, file_cluster_4: 13.13
- **Magnitude:** 1790.16 | **LOC:** 4194 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (60.779%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAutoCommitAsyncWithUserAssignedType` (Impact: 68.7)
  * `verifyRebalanceWithMetadataChange` (Impact: 28.2)
  * `closeVerifyTimeout` (Impact: 26.2)
  * `testMetadataRefreshDuringRebalance` (Impact: 25.6)
  * `getLost` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 621`, `args: 240`, `func_start: 287`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 97`, `state_mutation: 379`, `duplicate_logic: 28`, `orphaned_logic: 127`
* *Architecture:* `api: 142`, `concurrency: 225`, `import: 113`
* *Defense:* `safety: 128`, `doc: 3`, `test: 529`, `immutability_locks: 130`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 59):` org.junit.jupiter.api.Test, java.util.concurrent.Future, java.util.Collections.emptyList, org.apache.kafka.clients.consumer.ConsumerPartitionAssignor, java.util.Arrays, org.apache.kafka.common.requests.JoinGroupRequest, org.apache.kafka.common.internals.ClusterResourceListeners, org.apache.kafka.clients.consumer.CloseOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/clients/producer/KafkaProducerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.498 IQR)
- **Top Global Matches:** file_cluster_13: 13.498, file_cluster_0: 13.55, file_cluster_11: 13.668
- **Magnitude:** 1751.72 | **LOC:** 3259 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (71.4227%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `shouldCloseProperlyAndThrowIfInterrupted` (Impact: 24.8)
  * `testCloseWhenWaitingForMetadataUpdate` (Impact: 20.1)
  * `testOnlyCanExecuteCloseAfterInitTransact` (Impact: 19.1)
  * `testAcksAndIdempotenceForIdempotentProdu` (Impact: 18.5)
  * `testCommitTransactionWithMetadataTimeout` (Impact: 17.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 890`, `args: 183`, `func_start: 192`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 107`, `state_mutation: 613`, `dead_code: 1`, `duplicate_logic: 48`, `orphaned_logic: 70`
* *Architecture:* `api: 111`, `concurrency: 131`, `import: 152`
* *Defense:* `safety: 74`, `test: 255`, `sync_locks: 3`, `immutability_locks: 36`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 80):` org.junit.jupiter.api.Test, java.util.concurrent.Future, org.apache.kafka.common.requests.TxnOffsetCommitResponse, org.apache.kafka.common.requests.EndTxnResponse, java.util.Arrays, org.apache.kafka.common.requests.JoinGroupRequest, org.apache.kafka.common.metrics.Monitorable, org.apache.kafka.common.internals.ClusterResourceListeners...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/test/scala/integration/kafka/api/PlaintextAdminIntegrationTest.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.53 IQR)
- **Top Global Matches:** file_cluster_8: 12.53, file_cluster_0: 12.601, file_cluster_16: 12.738
- **Magnitude:** 1720.7 | **LOC:** 5065 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 17.6%
- **Risk Profile:** Cognitive Load (22.5603%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testCreatePartitions` (Impact: 186.8)
  * `testElectPreferredLeaders` (Impact: 93.9)
  * `testConsumerGroupsDeprecatedConsumerGrou` (Impact: 55.1)
  * `testDescribeGroups` (Impact: 30.4)
  * `testListConsumerGroups` (Impact: 25.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 554`, `args: 305`, `func_start: 129`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 643`, `state_mutation: 379`, `duplicate_logic: 13`, `orphaned_logic: 88`
* *Architecture:* `io: 6`, `api: 118`, `concurrency: 9`, `import: 4`
* *Defense:* `safety: 10`, `doc: 18`, `test: 267`, `immutability_locks: 721`, `cleanup: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 55):` Timeout, scala.concurrent.Await, org.apache.kafka.clients.producer.KafkaProducer, Consumer, AclBindingFilter, LogFileUtils, ClientQuotaFilter, org.apache.kafka.common.utils.Time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/test/java/kafka/server/share/SharePartitionTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.843 IQR)
- **Top Global Matches:** file_cluster_8: 12.843, file_cluster_0: 12.921, file_cluster_13: 12.937
- **Magnitude:** 1654.08 | **LOC:** 12683 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (35.2997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMaybeInitializeWithErrorPartitionRes` (Impact: 49.0)
  * `testAcquireWhenBatchesAreRemovedFromBetw` (Impact: 47.1)
  * `testMaybeInitializeSharePartitionAgainCo` (Impact: 26.3)
  * `testMaybeInitializeDefaultStartEpochGrou` (Impact: 21.2)
    * *Intent:* // replicaManager.fetchOffsetForTimestamp should be called with "ListOffsetsRequest.LATEST_TIMESTAMP...
  * `testMaybeInitializeFetchOffsetForByDurat` (Impact: 20.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 754`, `args: 192`, `func_start: 187`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 463`, `dead_code: 5`, `duplicate_logic: 30`, `orphaned_logic: 83`
* *Architecture:* `api: 101`, `concurrency: 112`, `import: 94`
* *Defense:* `safety: 56`, `doc: 4`, `test: 1423`, `sync_locks: 1`, `immutability_locks: 18`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` org.junit.jupiter.api.Test, kafka.server.share.SharePartition.SharePartitionState, org.apache.kafka.common.record.internal.ControlRecordType, org.apache.kafka.common.record.internal.MemoryRecords, org.apache.kafka.common.requests.ListOffsetsRequest, org.apache.kafka.common.utils.Time, org.apache.kafka.coordinator.group.ShareGroupAutoOffsetResetStrategy, org.apache.kafka.common.record.internal.FileRecords...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `clients/src/test/java/org/apache/kafka/common/network/SslTransportLayerTest.java` (JAVA) | Magnitude: 657.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 909, structural_boundaries: 399, func_start: 133, args: 115
- `connect/api/src/test/java/org/apache/kafka/connect/data/FakeSchema.java` (JAVA) | Magnitude: 41.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 17, api: 13, func_start: 12
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/classic/ClassicGroupTest.java` (JAVA) | Magnitude: 750.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1333, structural_boundaries: 377, state_mutation: 281, test: 246
- `shell/src/main/java/org/apache/kafka/shell/command/PwdCommandHandler.java` (JAVA) | Magnitude: 37.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 26, api: 12, args: 10
- `streams/src/test/java/org/apache/kafka/streams/state/internals/TimestampedWindowStoreBuilderTest.java` (JAVA) | Magnitude: 82.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 72, test: 43, immutability_locks: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/StopFindCoordinatorOnCloseEvent.java` (JAVA) | Magnitude: 4.02 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, func_start: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bin/kafka-server-stop.sh` (SHELL) | Magnitude: 120.04 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 62, io: 53, state_mutation: 44, indent_spaces: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/docker/run_tests.sh` (SHELL) | Magnitude: 5.47 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 29, indent_spaces: 14, state_mutation: 12, reflection_metaprogramming: 11
- `tests/docker/ducker-ak` (SHELL) | Magnitude: 631.1 | Delta: **0.268 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 472, branch: 315, reflection_metaprogramming: 308, safety: 149
- `.github/scripts/label_small.sh` (SHELL) | Magnitude: 2.06 | Delta: **0.286 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 12, safety_bypasses: 8, branch: 5, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/StreamsOnTasksRevokedCallbackNeededEvent.java` (JAVA) | Magnitude: 11.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, func_start: 4, api: 4
- `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/isolation/SamplingTestPlugin.java` (JAVA) | Magnitude: 52.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 18, doc: 13, branch: 11
- `streams/src/main/java/org/apache/kafka/streams/processor/assignment/KafkaStreamsState.java` (JAVA) | Magnitude: 37.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 18, func_start: 8, indent_spaces: 8, structural_boundaries: 7
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/events/TopicSubscriptionChangeEvent.java` (JAVA) | Magnitude: 11.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, func_start: 4, api: 4
- `clients/src/main/java/org/apache/kafka/common/requests/SaslAuthenticateResponse.java` (JAVA) | Magnitude: 41.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 21, api: 16, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `clients/src/main/java/org/apache/kafka/clients/admin/RemoveMembersFromConsumerGroupOptions.java` (JAVA) | Magnitude: 23.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, api: 8, args: 6
- `clients/src/main/java/org/apache/kafka/common/config/LogLevelConfig.java` (JAVA) | Magnitude: 23.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, api: 8, doc: 7, immutability_locks: 7
- `core/src/main/scala/kafka/cluster/Partition.scala` (SCALA) | Magnitude: 636.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 733, branch: 160, args: 136, closures: 112
- `core/src/main/scala/kafka/server/KafkaRequestHandler.scala` (SCALA) | Magnitude: 41.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 17, branch: 11, state_mutation: 10
- `server/src/main/java/org/apache/kafka/server/share/fetch/PartitionMaxBytesStrategy.java` (JAVA) | Magnitude: 71.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 25, branch: 19, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tools/src/main/java/org/apache/kafka/tools/streams/StreamsGroupCommand.java` (JAVA) | Magnitude: 0.8 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 858, branch: 295, structural_boundaries: 237, generics: 117
- `streams/src/main/java/org/apache/kafka/streams/processor/internals/StoreChangelogReader.java` (JAVA) | Magnitude: 1157.68 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 741, branch: 198, immutability_locks: 191, structural_boundaries: 166
- `tools/src/main/java/org/apache/kafka/tools/OffsetsUtils.java` (JAVA) | Magnitude: 0.4 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 393, structural_boundaries: 138, branch: 103, state_mutation: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `committer-tools/update-cache.sh` (SHELL) | Magnitude: 14.0 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, io: 8, branch: 6, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/HandlingSourceTopicDeletionIntegrationTest.java` (JAVA) | Magnitude: 75.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 47, concurrency: 30, import: 25
- `streams/src/test/java/org/apache/kafka/test/MockProcessorNode.java` (JAVA) | Magnitude: 48.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 19, concurrency: 18, immutability_locks: 12
- `clients/src/main/java/org/apache/kafka/clients/producer/RoundRobinPartitioner.java` (JAVA) | Magnitude: 51.5 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 24, indent_spaces: 19, structural_boundaries: 18, doc: 8
- `streams/src/test/java/org/apache/kafka/streams/kstream/internals/InternalStreamsBuilderTest.java` (JAVA) | Magnitude: 915.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 925, structural_boundaries: 344, immutability_locks: 291, generics: 221
- `connect/mirror/src/main/java/org/apache/kafka/connect/mirror/OffsetSyncWriter.java` (JAVA) | Magnitude: 143.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 43, concurrency: 33, state_mutation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `clients/src/main/java/org/apache/kafka/common/ClusterResourceListener.java` (JAVA) | Magnitude: 17.22 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, planned_debt: 3, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `raft/src/main/java/org/apache/kafka/raft/RaftMessageQueue.java` (JAVA) | Magnitude: 28.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, args: 4, func_start: 4
- `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/OffsetExpirationCondition.java` (JAVA) | Magnitude: 18.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/admin/StaticBrokerConfigTest.java` (JAVA) | Magnitude: 45.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 47, test: 24, import: 22
- `server/src/main/java/org/apache/kafka/server/metrics/LinuxIoMetricsCollector.java` (JAVA) | Magnitude: 62.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 17, branch: 13, func_start: 10
- `trogdor/src/main/java/org/apache/kafka/trogdor/task/NoOpTaskController.java` (JAVA) | Magnitude: 7.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 3, args: 2
- `metadata/src/main/java/org/apache/kafka/image/loader/SnapshotManifest.java` (JAVA) | Magnitude: 5.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, api: 3, doc: 3
- `storage/src/test/java/org/apache/kafka/storage/internals/checkpoint/LeaderEpochCheckpointFileWithFailureHandlerTest.java` (JAVA) | Magnitude: 9.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 28, import: 8, test: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> Churn: **95.8%** | Cog Load: 56.9035% | Debt: 0.0%
- `core/src/main/scala/kafka/server/KafkaApis.scala` -> Churn: **90.0%** | Cog Load: 13.8522% | Debt: 80.4292%
- `streams/src/test/java/org/apache/kafka/streams/processor/internals/TaskManagerTest.java` -> Churn: **80.17%** | Cog Load: 86.4046% | Debt: 0.0%
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareConsumerImpl.java` -> Churn: **76.8%** | Cog Load: 24.123% | Debt: 99.9947%
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/AsyncKafkaConsumer.java` -> Churn: **70.53%** | Cog Load: 44.5079% | Debt: 99.7536%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java` -> **Sanskar Jhajharia** (100.0% isolated ownership) | Magnitude: 2178.04
- `metadata/src/test/java/org/apache/kafka/controller/ReplicationControlManagerTest.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 1627.3
- `streams/src/main/java/org/apache/kafka/streams/state/internals/RocksDBGenericOptionsToDbOptionsColumnFamilyOptionsAdapter.java` -> **Eduwer Camacaro** (100.0% isolated ownership) | Magnitude: 1486.7
- `clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 1363.54
- `streams/src/test/java/org/apache/kafka/streams/StreamsBuilderTest.java` -> **Alieh Saeedi** (100.0% isolated ownership) | Magnitude: 1059.54

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `clients/src/main/java/org/apache/kafka/clients/producer/internals/TransactionManager.java` -> **Severity: 0.149** (Bridge: 0.0024 * Flux: 62.7463%)
- `clients/src/main/java/org/apache/kafka/common/requests/ListOffsetsRequest.java` -> **Severity: 0.1** (Bridge: 0.001 * Flux: 100.0%)
- `clients/src/main/java/org/apache/kafka/common/protocol/Errors.java` -> **Severity: 0.092** (Bridge: 0.008 * Flux: 11.5049%)
- `clients/src/main/java/org/apache/kafka/common/requests/JoinGroupRequest.java` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 100.0%)
- `core/src/main/scala/kafka/network/RequestChannel.scala` -> **Severity: 0.073** (Bridge: 0.0014 * Flux: 50.8333%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `clients/src/main/java/org/apache/kafka/common/KafkaException.java` -> **Severity: 1470.274** (Blast Radius: 17.867 * Doc Risk: 82.2899%)
- `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -> **Severity: 1161.604** (Blast Radius: 13.417 * Doc Risk: 86.577%)
- `clients/src/main/java/org/apache/kafka/common/errors/TimeoutException.java` -> **Severity: 1085.815** (Blast Radius: 13.195 * Doc Risk: 82.2899%)
- `clients/src/main/java/org/apache/kafka/common/utils/internals/BytesUtils.java` -> **Severity: 1030.557** (Blast Radius: 12.112 * Doc Risk: 85.0856%)
- `clients/src/main/java/org/apache/kafka/common/Uuid.java` -> **Severity: 889.235** (Blast Radius: 10.346 * Doc Risk: 85.9496%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
