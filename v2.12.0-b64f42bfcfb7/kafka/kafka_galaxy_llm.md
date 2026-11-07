# ARCHITECTURAL_BRIEF: kafka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/kafka` |
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
- **Scope:** 6698 analyzed artifact(s), 1115080 LOC.
- **Load-bearing artifact:** `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -- 882 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java` -- pulls in 370 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` at magnitude 8866.22 (structural weight, not risk).
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
| Total Artifacts | 7200 |
| Analyzed Artifacts (Scanned) | 6698 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 502 |
| Total LOC | 1115080 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 93.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5855 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1094 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.1762 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 246 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 5645 | 969461 | 84.3% |
| JSON | 300 | 8184 | 4.5% |
| SCALA | 298 | 109830 | 4.4% |
| PYTHON | 166 | 17722 | 2.5% |
| SHELL | 74 | 2335 | 1.1% |
| YAML | 72 | 3347 | 1.1% |
| PLAINTEXT | 58 | 5 | 0.9% |
| BATCH | 36 | 265 | 0.5% |
| XML | 22 | 0 | 0.3% |
| MARKDOWN | 17 | 0 | 0.3% |
| DOCKERFILE | 4 | 273 | 0.1% |
| GROOVY | 3 | 3499 | 0.0% |
| HTML | 2 | 12 | 0.0% |
| RUBY | 1 | 147 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 6693 |
| unknown | unknown | 5 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 19%, Generic / Templated Code Files 16%, Data / Markup / Trivial 15%, Encapsulated Accessors Files 12%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6623 | 98.9% |
| Unknown | 5 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 70 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 502*

**Composition by Extension & Reason:**
- `.java`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 47x Unsupported Format (.undeterminable), 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Binary Format Detected)
- `.png`: 47x Excluded (Explicitly Denied Extension: '.png')
- `.converter`: 16x Unsupported Format (.converter)
- `.py`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 93 LOC), 1x Excluded (Saturation: Line 40 exceeds 500 chars)
- `.scala`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.conf`: 3x Excluded (Unsupported Extension: '.conf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.conf)
- `.predicate`: 3x Unsupported Format (.predicate)
- `.json`: 1x Excluded (Massive Static Asset Blob: 2572 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.0`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 2x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.4 | 5.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.7 | 42.4 | 51.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.4 | 8.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 56.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.2 | 99.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6098 | 1450 | 2 | `server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java` |
| cleanup | 3753 | 956 | 1 | `core/src/test/java/kafka/server/share/SharePartitionTest.java` |
| guards | 132006 | 4961 | 47 | `streams/src/test/java/org/apache/kafka/streams/processor/internals/TaskManagerTest.java` |
| danger | 50440 | 3849 | 18 | `core/src/test/scala/integration/kafka/api/PlaintextAdminIntegrationTest.scala` |
| concurrency | 12334 | 1110 | 3 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupCoordinatorServiceTest.java` |
| connectivity | 70282 | 5969 | 23 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` |
| io | 4073 | 573 | 0 | `tests/docker/ducker-ak` |
| crypto | 1 | 1 | 0 | `tests/kafkatest/tests/connect/connect_test.py` |
| ipc | 78 | 26 | 0 | `docker/test/docker_sanity_test.py` |
| time | 4999 | 703 | 1 | `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/IQv2StoreIntegrationTest.java` |
| serialization | 288 | 71 | 0 | `connect/runtime/src/test/java/org/apache/kafka/connect/util/clusters/EmbeddedConnect.java` |
| regex | 589 | 160 | 0 | `streams/src/test/java/org/apache/kafka/streams/processor/internals/InternalTopologyBuilderTest.java` |
| events | 9186 | 1008 | 2 | `clients/src/test/java/org/apache/kafka/clients/consumer/internals/StreamsMembershipManagerTest.java` |
| tests | 104391 | 1951 | 34 | `core/src/test/java/kafka/server/share/SharePartitionTest.java` |
| docs | 16025 | 3433 | 6 | `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java` |
| debt | 4040 | 713 | 1 | `.github/scripts/develocity_reports.py` |
| mutation | 269832 | 5232 | 91 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` |
| dead_code | 28209 | 3038 | 10 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` |
| credential | 206 | 62 | 0 | `clients/src/test/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactoryTest.java` |
| threat | 21 | 6 | 0 | `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/PlaintextConsumerTest.java` |
| ml_ai | 1480 | 423 | 0 | `connect/json/src/test/java/org/apache/kafka/connect/json/JsonConverterTest.java` |
| ui | 156 | 42 | 0 | `core/src/test/scala/unit/kafka/server/ReplicaManagerTest.scala` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.6464**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/docker/ducker-ak` (Hits: 126)
- `streams/src/test/java/org/apache/kafka/streams/processor/internals/StateDirectoryTest.java` (Hits: 118)
- `tools/src/main/java/org/apache/kafka/tools/ManifestWorkspace.java` (Hits: 62)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TopicPartition.java** (`clients/src/main/java/org/apache/kafka/common/TopicPartition.java`) — 882 inbound connections
2. **Utils.java** (`clients/src/main/java/org/apache/kafka/common/utils/Utils.java`) — 720 inbound connections
3. **Errors.java** (`clients/src/main/java/org/apache/kafka/common/protocol/Errors.java`) — 580 inbound connections
4. **Time.java** (`clients/src/main/java/org/apache/kafka/common/utils/Time.java`) — 538 inbound connections
5. **Uuid.java** (`clients/src/main/java/org/apache/kafka/common/Uuid.java`) — 521 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RequestConvertToJson.java** (`server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java`) — 370 outbound dependencies
2. **KafkaAdminClientTest.java** (`clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java`) — 307 outbound dependencies
3. **RequestResponseTest.java** (`clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java`) — 305 outbound dependencies
4. **KafkaAdminClient.java** (`clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java`) — 287 outbound dependencies
5. **GroupMetadataManagerTest.java** (`group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java`) — 232 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `endTransaction` **(Many-Argument Workhorses)** (@ `core/src/main/scala/kafka/coordinator/transaction/TransactionCoordinator.scala`) -> Impact: **297.5** | LOC: 250
  * *Intent:* */ /** * Handling the endTxn request above the Transaction Version 2. * */
- `testFromPropsInvalid` **(Callbacks & Closures)** (@ `core/src/test/scala/unit/kafka/server/KafkaConfigTest.scala`) -> Impact: **290.4** | LOC: 327
- `__init__` **(Many-Argument Workhorses)** (@ `tests/kafkatest/services/kafka/kafka.py`) -> Impact: **240.2** | LOC: 279
- `endTransactionWithTV1` **(Many-Argument Workhorses)** (@ `core/src/main/scala/kafka/coordinator/transaction/TransactionCoordinator.scala`) -> Impact: **195.1** | LOC: 168
  * *Intent:* /** * Handling the endTxn request under the Transaction Version 1. * */
- `doParseRequest` **(Many-Argument Workhorses)** (@ `clients/src/main/java/org/apache/kafka/common/requests/AbstractRequest.java`) -> Impact: **193.2** | LOC: 185
- `parseResponse` **(Many-Argument Workhorses)** (@ `clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java`) -> Impact: **193.2** | LOC: 185
- `response` **(Type Conversions)** (@ `server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java`) -> Impact: **168.1** | LOC: 176
- `getRequest` **(Compute Cores)** (@ `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java`) -> Impact: **164.0** | LOC: 94
- `getResponse` **(Compute Cores)** (@ `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java`) -> Impact: **164.0** | LOC: 94
- `requestBuilder` **(Compute Cores)** (@ `core/src/test/scala/unit/kafka/server/RequestQuotaTest.scala`) -> Impact: **152.0** | LOC: 495

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `group-coordinator/src/test/java/org/apache/kafka/coordinator/group` | 18 | 15183.32 | 18.05% | 0.0% |
| `clients/src/test/java/org/apache/kafka/clients/consumer/internals` | 67 | 15161.48 | 18.08% | 0.0% |
| `streams/src/main/java/org/apache/kafka/streams/state/internals` | 203 | 14231.32 | 15.49% | 38.36% |
| `clients/src/main/java/org/apache/kafka/clients/consumer/internals` | 98 | 14202.16 | 21.27% | 33.5% |
| `streams/src/test/java/org/apache/kafka/streams/state/internals` | 151 | 13795.08 | 13.35% | 0.0% |
| `core/src/test/scala/unit/kafka/server` | 103 | 13659.66 | 14.95% | 0.0% |
| `streams/src/test/java/org/apache/kafka/streams/processor/internals` | 73 | 12802.88 | 12.16% | 0.0% |
| `streams/src/main/java/org/apache/kafka/streams/processor/internals` | 95 | 12151.38 | 18.19% | 34.7% |
| `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration` | 87 | 10743.7 | 22.97% | 0.0% |
| `docker/examples/fixtures/secrets` | 2 | 10000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `clients/src/main/java/org/apache/kafka/common/record/internal/AbstractLegacyRecordBatch.java` -> **100.0%** Exposure
- `clients/src/main/java/org/apache/kafka/common/record/internal/CompressionType.java` -> **100.0%** Exposure
- `core/src/main/java/kafka/docker/Log4jConfiguration.java` -> **100.0%** Exposure
- `generator/src/main/java/org/apache/kafka/message/FieldType.java` -> **100.0%** Exposure
- `metadata/src/main/java/org/apache/kafka/image/node/printer/MetadataNodeRedactionCriteria.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/scripts/checkstyle.py` -> **100.0%** Exposure
- `.github/scripts/develocity_reports.py` -> **100.0%** Exposure
- `.github/scripts/junit.py` -> **100.0%** Exposure
- `.github/scripts/pr-format.py` -> **100.0%** Exposure
- `.github/scripts/rat.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> **405** Orphaned Functions | **0** Duplicates
- `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java` -> **276** Orphaned Functions | **0** Duplicates
- `core/src/test/scala/unit/kafka/server/KafkaApisTest.scala` -> **270** Orphaned Functions | **2** Duplicates
- `core/src/test/java/kafka/server/share/SharePartitionTest.java` -> **262** Orphaned Functions | **0** Duplicates
- `core/src/test/scala/integration/kafka/api/AuthorizerIntegrationTest.scala` -> **185** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/assertion/AssertionUtils.java` -> **100.0%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactoryTest.java` -> **100.0%** Exposure
- `test-common/test-common-runtime/src/main/java/org/apache/kafka/common/test/JaasUtils.java` -> **100.0%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactory.java` -> **98.9215%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/oauthbearer/ClientAssertionKeycloakIntegrationTest.java` -> **97.3232%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `27` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `91220` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 11.692)
- **Top Global Matches:** file_cluster_12: 11.692, file_cluster_5: 12.819, file_cluster_13: 13.438
- **Magnitude:** 8866.22 | **LOC:** 27677 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 36.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **232**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.6%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (60.0%), Concurrency Surface (formerly Concurrency) (12.1%)
- **Documentation Coverage:** 99.7587% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generatePendingAssignmentCases` **(Many-Argument Workhorses)** (Impact: 58.6)
  * `testLastStaticConsumerProtocolMemberReplacedByClassicProtocolMember` **(Compute Cores)** (Impact: 24.4)
  * `testReconciliationProcess` **(I/O & Config Routines)** (Impact: 23.1)
  * `testStreamsReconciliationProcess` **(I/O & Config Routines)** (Impact: 22.5)
  * `testReconciliationInJoiningConsumerGroupWithCooperativeProtocol` **(I/O & Config Routines)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 6101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 4126`, `args: 764`, `func_start: 424`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 429`, `state_mutation: 6003`, `unreferenced_by_name: 405`
* *Architecture:* `api: 407`, `concurrency: 5`, `import: 232`
* *Defense:* `safety: 7`, `doc: 2`, `test: 2456`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 98):` java.nio.ByteBuffer, java.util.ArrayList, java.util.Arrays, java.util.Collections, java.util.Comparator, java.util.HashMap, java.util.HashSet, java.util.LinkedHashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/client-secrets/client.keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/secrets/kafka.truststore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/secrets/kafka01.keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/docker/ssh/id_rsa` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/docker/ssh/id_rsa.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.512)
- **Top Global Matches:** file_cluster_5: 7.512, file_cluster_12: 8.575, file_cluster_7: 9.748
- **Magnitude:** 3998.18 | **LOC:** 11791 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **307**; blast radius 0.058; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (56.4%), Concurrency Surface (formerly Concurrency) (43.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.2%)
- **Documentation Coverage:** 98.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareDescribeQuorumResponse` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `testAddRaftVoterRequest` **(Defensive Guards)** (Impact: 23.3)
  * `testRemoveRaftVoterRequest` **(Defensive Guards)** (Impact: 23.0)
  * `testDescribeTopicsWithDescribeTopicPartitionsApiEdgeCase` **(Annotated & Test Methods)** (Impact: 13.8)
  * `defaultQuorumInfo` **(Stateful Encapsulated Methods)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 215
* *State Mutation (weighted view):* 2129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 3279`, `args: 615`, `func_start: 362`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 473`, `state_mutation: 2017`, `unreferenced_by_name: 276`
* *Architecture:* `api: 292`, `concurrency: 60`, `import: 307`
* *Defense:* `safety: 344`, `doc: 6`, `test: 1110`, `sync_locks: 5`, `immutability_locks: 447`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000269
  * `Imports (Out-Degree: 277):` java.net.InetSocketAddress, java.nio.ByteBuffer, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collection, java.util.Collections...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.239)
- **Top Global Matches:** file_cluster_5: 7.239, file_cluster_12: 8.302, file_cluster_7: 10.632
- **Magnitude:** 3068.38 | **LOC:** 8993 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **231**; blast radius 0.075; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (98.6%), Guard Balance (formerly Safety Score) (62.5%), Concurrency Surface (formerly Concurrency) (19.1%)
- **Documentation Coverage:** 15.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `streamsGroupHeartbeat` **(Compute Cores)** (Impact: 44.4)
    * *Intent:* * @param rackId The rack ID from the request or null. * @param rebalanceTimeoutMs The rebalance time...
  * `maybeUpdateRegularExpressions` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /** * Check whether the member has updated its subscribed topic regular expression and * may trigger...
  * `getOrMaybeSubscribeStaticConsumerGroupMember` **(Many-Argument Workhorses)** (Impact: 29.6)
    * *Intent:* * previous static member if allowed. * * @param group The consumer group. * @param memberId The memb...
  * `maybeUpdateTopology` **(Stateful Encapsulated Methods)** (Impact: 28.3)
    * *Intent:* * Compares the topology from the request with the one in the group. * * - If the topology of the gro...
  * `classicGroupJoinExistingMember` **(I/O & Config Routines)** (Impact: 28.1)
    * *Intent:* /** * Handle a join group request for an existing member. * * @param context The request context. * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 228 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 1007
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 664`, `structural_boundaries: 1159`, `args: 378`, `func_start: 256`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 255`, `state_mutation: 551`
* *Architecture:* `api: 74`, `concurrency: 27`, `import: 231`
* *Defense:* `safety: 116`, `doc: 241`, `sync_locks: 1`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.01027
  * `Imports (Out-Degree: 93):` java.nio.ByteBuffer, java.util.ArrayList, java.util.Collections, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Map, java.util.Objects...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.756)
- **Top Global Matches:** file_cluster_5: 6.756, file_cluster_12: 9.345, file_cluster_7: 11.27
- **Magnitude:** 2967.1 | **LOC:** 5180 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **287**; blast radius 0.112; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Guard Balance (formerly Safety Score) (63.8%), Debt Markers (formerly Tech Debt) (51.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.5%)
- **Documentation Coverage:** 88.8112% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alterPartitionReassignments` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `getCreateTopicsCall` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `updateFeatures` **(Many-Argument Workhorses)** (Impact: 35.8)
  * `alterUserScramCredentials` **(Defensive Guards)** (Impact: 35.6)
  * `getCreatePartitionsCall` **(Many-Argument Workhorses)** (Impact: 35.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 179 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 500`, `structural_boundaries: 1281`, `args: 408`, `func_start: 322`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 194`, `state_mutation: 347`, `duplicate_logic: 43`
* *Architecture:* `api: 110`, `concurrency: 26`, `import: 287`
* *Defense:* `safety: 40`, `doc: 68`, `test: 2`, `sync_locks: 15`, `immutability_locks: 315`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.112
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.067002
  * `Imports (Out-Degree: 292):` java.security.InvalidKeyException, java.security.NoSuchAlgorithmException, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections, java.util.Comparator...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `core/src/test/java/kafka/server/share/SharePartitionTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.65)
- **Top Global Matches:** file_cluster_13: 8.65, file_cluster_0: 9.265, file_cluster_16: 9.38
- **Magnitude:** 2904.96 | **LOC:** 12683 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **94**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.6%), Concurrency Surface (formerly Concurrency) (75.9%), Guard Balance (formerly Safety Score) (34.8%), Complexity Load (formerly Cognitive Load) (24.9%)
- **Documentation Coverage:** 97.307% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testMaybeInitializeWithErrorPartitionResponse` **(I/O & Config Routines)** (Impact: 25.6)
  * `testWriteShareGroupStateFailure` **(I/O & Config Routines)** (Impact: 21.4)
  * `testContainsAbortMarker` **(Annotated & Test Methods)** (Impact: 17.7)
  * `testWriteShareGroupStateWithInvalidTopicsData` **(Annotated & Test Methods)** (Impact: 15.9)
  * `testDeliveryCompleteCountOnLockExpiryAndWriteFailureOnOffsetLastDelivery` **(Annotated & Test Methods)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 382
* *State Mutation (weighted view):* 813
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 1867`, `args: 508`, `func_start: 292`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 723`, `unreferenced_by_name: 262`
* *Architecture:* `api: 266`, `concurrency: 262`, `import: 94`
* *Defense:* `safety: 17`, `doc: 8`, `test: 3907`, `sync_locks: 4`, `immutability_locks: 18`, `cleanup: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` java.nio.ByteBuffer, java.util.ArrayList, java.util.HashMap, java.util.Iterator, java.util.List, java.util.Map, java.util.Optional, java.util.OptionalInt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupCoordinatorServiceTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.063)
- **Top Global Matches:** file_cluster_5: 7.063, file_cluster_12: 7.916, file_cluster_7: 9.159
- **Magnitude:** 2811.28 | **LOC:** 5962 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **141**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Complexity Load (formerly Cognitive Load) (71.6%), Guard Balance (formerly Safety Score) (65.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testFetchOffsets` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `testStreamsHeartbeatRequestValidation` **(I/O & Config Routines)** (Impact: 16.1)
  * `testFetchOffsetsWithWrappedError` **(Many-Argument Workhorses)** (Impact: 12.8)
  * `testDeleteShareGroupOffsetsSuccessWithErrorTopics` **(I/O & Config Routines)** (Impact: 10.2)
  * `testConsumerHeartbeatRequestValidation` **(I/O & Config Routines)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 42 instances
* *Amplified Cascading Flux:* 112 instances
* *Concurrency (weighted view):* 477
* *State Mutation (weighted view):* 1494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 1391`, `args: 214`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 205`, `state_mutation: 1270`, `unreferenced_by_name: 128`
* *Architecture:* `api: 134`, `concurrency: 267`, `import: 141`
* *Defense:* `test: 488`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 70):` java.net.InetAddress, java.util.Arrays, java.util.HashSet, java.util.List, java.util.Map, java.util.Optional, java.util.OptionalInt, java.util.Properties...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/test/scala/unit/kafka/server/KafkaApisTest.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.779)
- **Top Global Matches:** file_cluster_5: 7.779, file_cluster_12: 9.013, file_cluster_0: 11.001
- **Magnitude:** 2628.3 | **LOC:** 14799 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 10.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **222**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.7%), Guard Balance (formerly Safety Score) (54.7%), Connectivity (formerly Api Exposure) (9.9%), Complexity Load (formerly Cognitive Load) (9.6%)
- **Documentation Coverage:** 98.2456% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testFindCoordinatorWithTopicCreation` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `testListGroupsRequest` **(Compute Cores)** (Impact: 31.9)
  * `testHandleOffsetFetchAuthorization` **(Compute Cores)** (Impact: 30.9)
  * `testHandleShareFetchRequestSuccessfulShareSessionLifecycle` **(I/O & Config Routines)** (Impact: 24.4)
  * `testHandleOffsetFetchWithMultipleGroups` **(Compute Cores)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 605
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 2706`, `args: 543`, `func_start: 333`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 399`, `state_mutation: 565`, `duplicate_logic: 2`, `unreferenced_by_name: 270`
* *Architecture:* `io: 2`, `api: 300`, `import: 104`
* *Defense:* `doc: 6`, `test: 596`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 124):` java.lang.Byte, java.net.InetAddress, java.nio.ByteBuffer, java.nio.charset.StandardCharsets, java.util, java.util.Comparator, java.util.Optional, java.util.OptionalInt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/kafkatest/services/kafka/kafka.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.523)
- **Top Global Matches:** file_cluster_4: 6.523, file_cluster_12: 10.094, file_cluster_15: 11.635
- **Magnitude:** 2521.78 | **LOC:** 2048 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **71** in-repo importer(s); it depends on **18**; blast radius 1.124; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (83.9%), Connectivity (formerly Api Exposure) (62.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.2%), Complexity Load (formerly Cognitive Load) (28.3%)
- **Documentation Coverage:** 61.326% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 240.2)
  * `start` **(Many-Argument Workhorses)** (Impact: 72.0)
    * *Intent:* """ Start the Kafka broker and wait until it registers its ID in ZooKeeper Startup will be skipped f...
  * `start_node` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `isr_idx_list` **(Many-Argument Workhorses)** (Impact: 48.2)
    * *Intent:* """ Get in-sync replica list the given topic and partition. """
  * `kafka_topics_cmd_with_optional_security_settings` **(Many-Argument Workhorses)** (Impact: 38.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 329 instances
* *State Mutation (weighted view):* 1079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 448`, `structural_boundaries: 233`, `args: 100`, `func_start: 94`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 421`, `planned_debt: 3`
* *Architecture:* `io: 24`, `api: 89`, `import: 20`
* *Defense:* `safety: 6`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.124
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.010608
  * `Imports (Out-Degree: 10):` .config, ducktape.cluster.remoteaccount, ducktape.services.service, ducktape.utils.util, json, kafkatest.directory_layout.kafka_path, kafkatest.services.kafka, kafkatest.services.kafka.util...
  * `Imported By (In-Degree: 71):` (Excluded from Brief to save tokens)

### `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.71)
- **Top Global Matches:** file_cluster_16: 8.71, file_cluster_12: 8.751, file_cluster_13: 10.315
- **Magnitude:** 2442.8 | **LOC:** 4029 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **305**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.7%), Guard Balance (formerly Safety Score) (67.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.9%)
- **Documentation Coverage:** 99.3174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getRequest` **(Compute Cores)** (Impact: 164.0)
  * `getResponse` **(Compute Cores)** (Impact: 164.0)
  * `verifyDescribeConfigsResponse` **(Stateful Encapsulated Methods)** (Impact: 15.7)
  * `createFetchResponse` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `createOffsetFetchRequest` **(Stateful Encapsulated Methods)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 1427
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 1645`, `args: 281`, `func_start: 252`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 1235`, `unreferenced_by_name: 41`
* *Architecture:* `api: 42`, `import: 305`
* *Defense:* `safety: 5`, `doc: 1`, `test: 195`, `immutability_locks: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 160):` java.nio.BufferUnderflowException, java.nio.ByteBuffer, java.nio.charset.StandardCharsets, java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collections, java.util.Collections.emptyList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/scala/kafka/server/KafkaApis.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.696)
- **Top Global Matches:** file_cluster_4: 10.696, file_cluster_6: 10.933, file_cluster_5: 15.344
- **Magnitude:** 2350.96 | **LOC:** 4290 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 10.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **109**; blast radius 0.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.4%), Mutation Surface (formerly State Flux) (75.2%), Guard Balance (formerly Safety Score) (58.0%), Complexity Load (formerly Cognitive Load) (20.4%)
- **Documentation Coverage:** 91.9679% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Callbacks & Closures)** (Impact: 151.1)
    * *Intent:* /** * Top-level method that handles all requests and multiplexes to the right api */
  * `handleShareFetchRequest` **(Compute Cores)** (Impact: 75.4)
    * *Intent:* /** * Handle a shareFetch request */
  * `handleFetchRequest` **(Compute Cores)** (Impact: 68.7)
    * *Intent:* /** * Handle a fetch request */
  * `handleProduceRequest` **(Many-Argument Workhorses)** (Impact: 63.6)
    * *Intent:* /** * Handle a produce request */
  * `handleAddPartitionsToTxnRequest` **(Many-Argument Workhorses)** (Impact: 50.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 768`, `structural_boundaries: 423`, `args: 506`, `func_start: 136`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 120`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 112`, `import: 66`
* *Defense:* `doc: 11`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.012636
  * `Imports (Out-Degree: 84):` java.util, java.util.Collections, java.util.Optional, java.util.concurrent.CompletableFuture, java.util.concurrent.ConcurrentHashMap, java.util.concurrent.atomic.AtomicInteger, java.util.stream.Collectors, kafka.coordinator.transaction.InitProducerIdResult...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `streams/src/test/java/org/apache/kafka/streams/processor/internals/TaskManagerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.24)
- **Top Global Matches:** file_cluster_12: 9.24, file_cluster_13: 9.929, file_cluster_5: 10.107
- **Magnitude:** 1953.7 | **LOC:** 5001 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 47.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **105**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.7%), Complexity Load (formerly Cognitive Load) (42.3%), Guard Balance (formerly Safety Score) (37.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitDuringHandleCorruptedWithEOS` **(I/O & Config Routines)** (Impact: 28.0)
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitDuringRevocationWithEOS` **(I/O & Config Routines)** (Impact: 26.6)
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitWithAlos` **(I/O & Config Routines)** (Impact: 23.6)
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitDuringRevocationWithAlos` **(I/O & Config Routines)** (Impact: 21.2)
  * `shouldCommitAllActiveTasksThatNeedCommittingOnHandleRevocationWithEosV2` **(I/O & Config Routines)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 72 instances
* *Concurrency (weighted view):* 474
* *State Mutation (weighted view):* 269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 536`, `structural_boundaries: 796`, `args: 238`, `func_start: 178`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 125`, `unreferenced_by_name: 165`
* *Architecture:* `io: 12`, `api: 166`, `concurrency: 89`, `import: 105`
* *Defense:* `safety: 1`, `test: 1466`, `sync_locks: 5`, `immutability_locks: 811`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` java.io.File, java.nio.file.Files, java.nio.file.Path, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `raft/src/main/java/org/apache/kafka/raft/KafkaRaftClient.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.684)
- **Top Global Matches:** file_cluster_5: 6.684, file_cluster_12: 7.168, file_cluster_16: 9.813
- **Magnitude:** 1624.7 | **LOC:** 4153 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **105**; blast radius 0.186; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.4%), Guard Balance (formerly Safety Score) (59.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.2%), Concurrency Surface (formerly Concurrency) (31.5%)
- **Documentation Coverage:** 86.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleFetchResponse` **(Many-Argument Workhorses)** (Impact: 44.8)
  * `maybeHandleCommonResponse` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* * @param epoch Epoch received from the response * @param leaderEndpoints the endpoints of the leader...
  * `handleFetchSnapshotResponse` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `handleVoteResponse` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 31.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 83 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 519`, `args: 238`, `func_start: 164`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 172`
* *Architecture:* `io: 1`, `api: 33`, `concurrency: 28`, `import: 105`
* *Defense:* `safety: 23`, `doc: 26`, `sync_locks: 6`, `immutability_locks: 69`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.038617
  * `Imports (Out-Degree: 85):` java.net.InetSocketAddress, java.nio.ByteBuffer, java.util.Collection, java.util.HexFormat, java.util.IdentityHashMap, java.util.Iterator, java.util.List, java.util.Map...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.113)
- **Top Global Matches:** file_cluster_5: 7.113, file_cluster_12: 8.793, file_cluster_7: 9.609
- **Magnitude:** 1562.42 | **LOC:** 4753 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 31.8%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **107**; blast radius 0.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.3%), Guard Balance (formerly Safety Score) (57.5%), Complexity Load (formerly Cognitive Load) (56.7%)
- **Documentation Coverage:** 94.5848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumeMessages` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `ComplexShareConsumer` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `testFetchWithThrottledDeliveryValidateDeliveryCount` **(Callbacks & Closures)** (Impact: 11.7)
  * `testShareConsumerAfterCoordinatorMovement` **(I/O & Config Routines)** (Impact: 11.2)
  * `testRenewAcknowledgementNoResultInPoll` **(I/O & Config Routines)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 296
* *State Mutation (weighted view):* 525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 957`, `args: 388`, `func_start: 165`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 203`, `state_mutation: 333`, `unreferenced_by_name: 100`
* *Architecture:* `api: 117`, `concurrency: 101`, `import: 107`
* *Defense:* `safety: 170`, `doc: 9`, `test: 341`, `sync_locks: 6`, `immutability_locks: 30`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000622
  * `Imports (Out-Degree: 63):` com.yammer.metrics.core.Meter, java.nio.ByteBuffer, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.HashMap, java.util.HashSet...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.773)
- **Top Global Matches:** file_cluster_5: 7.773, file_cluster_12: 9.292, file_cluster_7: 10.627
- **Magnitude:** 1420.96 | **LOC:** 4430 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **130**; blast radius 0.058; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.6%), Concurrency Surface (formerly Concurrency) (18.4%), Complexity Load (formerly Cognitive Load) (18.2%), Connectivity (formerly Api Exposure) (7.0%)
- **Documentation Coverage:** 96.1686% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectRebalance` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* // Handles common initial part of rebalance callback. Does not handle instantiation of connectors an...
  * `testDoRestartConnectorAndTasksBoth` **(Annotated & Test Methods)** (Impact: 19.1)
  * `testJoinLeaderCatchUpFailsForIncrementalCooperative` **(I/O & Config Routines)** (Impact: 17.1)
  * `revokeAndReassign` **(I/O & Config Routines)** (Impact: 16.8)
  * `testTaskRequestedZombieFencingForwardingToLeader` **(Stateful Encapsulated Methods)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 517`, `structural_boundaries: 801`, `args: 273`, `func_start: 143`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 138`, `state_mutation: 170`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 113`
* *Architecture:* `io: 2`, `api: 119`, `concurrency: 11`, `import: 130`
* *Defense:* `safety: 4`, `doc: 5`, `test: 907`, `immutability_locks: 70`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.001568
  * `Imports (Out-Degree: 64):` jakarta.ws.rs.core.Response.Status.FORBIDDEN, jakarta.ws.rs.core.Response.Status.SERVICE_UNAVAILABLE, java.util.ArrayList, java.util.Collection, java.util.Collections, java.util.HashMap, java.util.HashSet, java.util.List...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `server-common/src/test/java/org/apache/kafka/server/share/persister/PersisterStateManagerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.781)
- **Top Global Matches:** file_cluster_5: 7.781, file_cluster_7: 8.8, file_cluster_12: 9.035
- **Magnitude:** 1412.4 | **LOC:** 4939 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **60**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.4%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (60.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testResponseErrorHandling` **(Annotated & Test Methods)** (Impact: 13.3)
  * `generatorDifferentStates` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `testWriteStateRequestBatchingWithCoordinatorNodeLookup` **(Callbacks & Closures)** (Impact: 8.1)
  * `testWriteStateRequestFailedMaxRetriesExhausted` **(I/O & Config Routines)** (Impact: 7.8)
  * `testInitializeStateRequestBatchingWithCoordinatorNodeLookup` **(Callbacks & Closures)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 302
* *State Mutation (weighted view):* 592
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 759`, `args: 175`, `func_start: 82`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 306`, `state_mutation: 558`, `duplicate_logic: 5`, `unreferenced_by_name: 57`
* *Architecture:* `api: 75`, `concurrency: 147`, `import: 60`
* *Defense:* `safety: 192`, `test: 278`, `immutability_locks: 11`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` java.util.ArrayList, java.util.List, java.util.Map, java.util.Optional, java.util.concurrent.CompletableFuture, java.util.concurrent.ExecutionException, java.util.concurrent.atomic.AtomicBoolean, java.util.stream.Stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/clients/consumer/KafkaConsumerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.291)
- **Top Global Matches:** file_cluster_5: 7.291, file_cluster_12: 9.202, file_cluster_7: 10.836
- **Magnitude:** 1366.34 | **LOC:** 4133 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **165**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (65.9%), Guard Balance (formerly Safety Score) (53.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.5%), Complexity Load (formerly Cognitive Load) (41.1%)
- **Documentation Coverage:** 98.452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumerCloseTest` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `prepareOffsetCommitResponse` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `fetchResponse` **(Stateful Encapsulated Methods)** (Impact: 8.5)
  * `testReturnRecordsDuringRebalance` **(Annotated & Test Methods)** (Impact: 8.4)
    * *Intent:* // TODO: this test requires rebalance logic which is not yet implemented in the CONSUMER group proto...
  * `mockErrorDeserializer` **(Stateful Encapsulated Methods)** (Impact: 8.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 477
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 1040`, `args: 304`, `func_start: 192`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 421`, `planned_debt: 34`, `fragile_debt: 14`, `duplicate_logic: 4`, `unreferenced_by_name: 126`
* *Architecture:* `api: 151`, `concurrency: 38`, `import: 165`
* *Defense:* `safety: 53`, `doc: 4`, `test: 524`, `sync_locks: 3`, `immutability_locks: 106`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 97):` java.lang.management.ManagementFactory, java.nio.ByteBuffer, java.time.Duration, java.util.AbstractMap, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.972)
- **Top Global Matches:** file_cluster_5: 7.972, file_cluster_12: 10.862, file_cluster_7: 10.99
- **Magnitude:** 1357.44 | **LOC:** 3033 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **101**; blast radius 0.087; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.1%), Guard Balance (formerly Safety Score) (80.0%), Concurrency Surface (formerly Concurrency) (74.9%), Complexity Load (formerly Cognitive Load) (32.5%)
- **Documentation Coverage:** 86.4583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tick` **(I/O & Config Routines)** (Impact: 37.4)
    * *Intent:* // public for testing
  * `doFenceZombieSourceTasks` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `DistributedHerder` **(Many-Argument Workhorses)** (Impact: 24.6)
    * *Intent:* // visible for testing
  * `validateSourceConnectorExactlyOnceSupport` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `handleRebalanceCompleted` **(I/O & Config Routines)** (Impact: 20.5)
    * *Intent:* /** * Handle post-assignment operations, either trying to resolve issues that kept assignment from c...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 498`, `args: 209`, `func_start: 129`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 243`, `state_mutation: 161`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 67`, `concurrency: 53`, `import: 101`
* *Defense:* `safety: 87`, `doc: 22`, `sync_locks: 22`, `immutability_locks: 102`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.087
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.00206
  * `Imports (Out-Degree: 74):` jakarta.ws.rs.core.Response, jakarta.ws.rs.core.UriBuilder, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Map...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `build.gradle` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.683)
- **Top Global Matches:** file_cluster_12: 6.683, file_cluster_10: 8.406, file_cluster_7: 8.926
- **Magnitude:** 1348.58 | **LOC:** 4173 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 10.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.057; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.4%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 47.973% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mavenJava` **(Callbacks & Closures)** (Impact: 9.2)
  * `integrationTest` **(State Mutators)** (Impact: 6.9)
  * `unitTest` **(State Mutators)** (Impact: 6.8)
  * `fineTuneEclipseClasspathFile` **(Callbacks & Closures)** (Impact: 6.7)
  * `determineCommitId` **(Compute Cores)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 164 instances
* *Concurrency (weighted view):* 326
* *State Mutation (weighted view):* 752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 123`, `args: 236`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 424`, `duplicate_logic: 8`, `unreferenced_by_name: 8`
* *Architecture:* `io: 57`, `concurrency: 66`, `import: 2`
* *Defense:* `safety: 8`, `doc: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.nio.charset.StandardCharsets, org.ajoberstar.grgit.Grgit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/scala/kafka/server/ReplicaManager.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.854)
- **Top Global Matches:** file_cluster_4: 9.854, file_cluster_5: 10.42, file_cluster_12: 10.927
- **Magnitude:** 1332.68 | **LOC:** 2569 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **144**; blast radius 0.146; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.7%), Mutation Surface (formerly State Flux) (58.1%), Guard Balance (formerly Safety Score) (55.8%), Connectivity (formerly Api Exposure) (34.8%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchOffset` **(Many-Argument Workhorses)** (Impact: 112.2)
  * `handleProduceAppend` **(Many-Argument Workhorses)** (Impact: 79.6)
    * *Intent:* * thread calling this method * * The responseCallback is wrapped so that it is scheduled on a reques...
  * `readFromLog` **(Many-Argument Workhorses)** (Impact: 65.2)
    * *Intent:* /** * Read from multiple topic partitions at the given offset up to maxSize bytes */
  * `fetchMessages` **(Many-Argument Workhorses)** (Impact: 48.9)
    * *Intent:* /** * Fetch messages from a replica, and wait until enough data can be fetched and return; * the cal...
  * `applyLocalFollowersDelta` **(Many-Argument Workhorses)** (Impact: 47.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 277`, `args: 268`, `func_start: 106`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 52`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 66`, `concurrency: 4`, `import: 67`
* *Defense:* `doc: 27`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.021028
  * `Imports (Out-Degree: 68):` com.yammer.metrics.core.Meter, java.io.File, java.lang.Long, java.nio.file.Files, java.nio.file.Paths, java.util, java.util.Collections, java.util.Optional...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `core/src/main/java/kafka/server/share/SharePartition.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.729)
- **Top Global Matches:** file_cluster_5: 7.729, file_cluster_12: 8.208, file_cluster_4: 10.628
- **Magnitude:** 1313.88 | **LOC:** 3427 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 31.6%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **73**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (23.5%)
- **Documentation Coverage:** 62.3853% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquire` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* * (the offset from which the log was read) with the first base offset of the fetch response. Any * b...
  * `acknowledgePerOffsetBatchRecords` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `acquireSubsetBatchRecords` **(Many-Argument Workhorses)** (Impact: 36.6)
  * `acknowledgeBatchRecords` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `maybeInitialize` **(I/O & Config Routines)** (Impact: 26.7)
    * *Intent:* /** * May initialize the share partition by reading the state from the persister. The share partitio...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 98 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 430`, `args: 124`, `func_start: 101`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 198`, `planned_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 9`, `concurrency: 24`, `import: 73`
* *Defense:* `safety: 87`, `doc: 75`, `sync_locks: 127`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.015732
  * `Imports (Out-Degree: 49):` java.util.ArrayList, java.util.Comparator, java.util.HashMap, java.util.HashSet, java.util.Iterator, java.util.List, java.util.Map, java.util.NavigableMap...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `transaction-coordinator/src/main/java/org/apache/kafka/coordinator/transaction/TransactionState.java` (JAVA) | Magnitude: 24.66 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 17, doc: 15, args: 9
- `core/src/test/scala/unit/kafka/cluster/AbstractPartitionTest.scala` (SCALA) | Magnitude: 56.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 105, core_var_decl: 52, structural_boundaries: 36, design_pascal_case: 26
- `streams/src/main/java/org/apache/kafka/streams/kstream/internals/SubscriptionStoreFactory.java` (JAVA) | Magnitude: 46.08 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 27, api: 13, func_start: 12
- `streams/src/test/java/org/apache/kafka/streams/state/NoOpWindowStore.java` (JAVA) | Magnitude: 54.96 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 40, immutability_locks: 24, api: 21
- `server/src/main/java/org/apache/kafka/server/share/metrics/SharePartitionMetrics.java` (JAVA) | Magnitude: 42.34 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 25, api: 15, args: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `core/src/test/scala/unit/kafka/server/ControllerRegistrationManagerTest.scala` (SCALA) | Magnitude: 75.38 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 63, core_var_decl: 41, args: 26
- `streams/src/test/java/org/apache/kafka/streams/tests/ShutdownDeadlockTest.java` (JAVA) | Magnitude: 17.76 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 27, import: 14, immutability_locks: 10
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupCoordinatorConfigTest.java` (JAVA) | Magnitude: 296.28 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 522, state_mutation: 201, test: 162, structural_boundaries: 134
- `core/src/main/scala/kafka/utils/Logging.scala` (SCALA) | Magnitude: 46.3 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, closures: 20, func_start: 17, args: 15
- `core/src/test/scala/unit/kafka/server/IsrExpirationTest.scala` (SCALA) | Magnitude: 52.06 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 155, core_var_decl: 63, structural_boundaries: 35, design_camel_case: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `clients/src/main/java/org/apache/kafka/common/IsolationLevel.java` (JAVA) | Magnitude: 17.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, branch: 4, args: 4
- `streams/src/test/java/org/apache/kafka/test/MockKeyValueStoreBuilder.java` (JAVA) | Magnitude: 9.72 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 12, import: 6, api: 4
- `tools/src/main/java/org/apache/kafka/tools/consumer/group/CsvUtils.java` (JAVA) | Magnitude: 0.08 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 33, api: 25, args: 21
- `tools/src/main/java/org/apache/kafka/tools/consumer/TransactionLogMessageFormatter.java` (JAVA) | Magnitude: 0.01 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, api: 5, args: 4
- `server-common/src/main/java/org/apache/kafka/server/config/QuotaConfig.java` (JAVA) | Magnitude: 92.58 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 167, api: 61, immutability_locks: 55, core_var_decl: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `trogdor/src/test/java/org/apache/kafka/trogdor/workload/PayloadGeneratorTest.java` (JAVA) | Magnitude: 79.14 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 84, core_var_decl: 60, test: 42
- `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/WorkerTransactionContext.java` (JAVA) | Magnitude: 43.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 47, core_var_decl: 11, args: 10
- `streams/src/test/java/org/apache/kafka/streams/state/internals/ChangeLoggingSessionBytesStoreWithHeadersTest.java` (JAVA) | Magnitude: 78.1 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 57, test: 38, core_var_decl: 29
- `metadata/src/main/java/org/apache/kafka/controller/errors/EventHandlerExceptionInfo.java` (JAVA) | Magnitude: 91.48 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 49, branch: 25, args: 13
- `tests/kafkatest/services/connect.py` (PYTHON) | Magnitude: 526.82 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 410, structural_boundaries: 145, core_var_decl: 113, state_mutation: 106

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `clients/src/test/java/org/apache/kafka/common/security/oauthbearer/internals/OAuthBearerClientInitialResponseTest.java` (JAVA) | Magnitude: 31.2 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 49, test: 34, core_var_decl: 21
- `streams/src/test/java/org/apache/kafka/test/MockRestoreCallback.java` (JAVA) | Magnitude: 6.14 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 5, import: 4, api: 3
- `streams/src/test/java/org/apache/kafka/streams/state/internals/RocksDBTimeOrderedSessionStoreWithHeadersTest.java` (JAVA) | Magnitude: 19.9 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 40, import: 22, core_var_decl: 13
- `tools/src/main/java/org/apache/kafka/tools/consumer/OffsetsMessageFormatter.java` (JAVA) | Magnitude: 0.01 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, import: 6, api: 5
- `clients/src/main/java/org/apache/kafka/common/requests/DescribeProducersResponse.java` (JAVA) | Magnitude: 23.12 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 20, api: 8, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `streams/src/test/java/org/apache/kafka/streams/query/VersionedKeyQueryTest.java` (JAVA) | Magnitude: 5.86 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, test: 6, args: 4
- `vagrant/vagrant-up.sh` (SHELL) | Magnitude: 177.28 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 105, core_var_decl: 53, design_snake_case: 37
- `clients/src/main/java/org/apache/kafka/common/internals/IdempotentCloser.java` (JAVA) | Magnitude: 63.9 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 15, api: 10, args: 9
- `clients/src/main/java/org/apache/kafka/common/security/ssl/CommonNameLoggingSslEngineFactory.java` (JAVA) | Magnitude: 6.08 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, import: 4, safety_bypasses: 3
- `clients/src/main/java/org/apache/kafka/clients/admin/AdminClient.java` (JAVA) | Magnitude: 6.42 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, api: 3, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `clients/src/main/java/org/apache/kafka/common/record/internal/MemoryRecords.java` (JAVA) | Magnitude: 396.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 620, structural_boundaries: 138, args: 69, func_start: 68
- `clients/src/main/java/org/apache/kafka/common/compress/GzipOutputStream.java` (JAVA) | Magnitude: 7.06 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, doc: 3, import: 3
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/ShareFetchMetricsRegistry.java` (JAVA) | Magnitude: 48.18 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 29, api: 22, state_mutation: 18
- `streams/src/main/java/org/apache/kafka/streams/StreamsMetrics.java` (JAVA) | Magnitude: 15.28 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, immutability_locks: 16, structural_boundaries: 8, doc: 7
- `coordinator-common/src/test/java/org/apache/kafka/coordinator/common/runtime/TestUtil.java` (JAVA) | Magnitude: 43.58 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 153, structural_boundaries: 57, import: 23, args: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `clients/src/test/java/org/apache/kafka/common/record/internal/InvalidMemoryRecordsProvider.java` (JAVA) | Magnitude: 17.98 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 28, encapsulation: 8, core_var_decl: 8
- `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/TimeWindowedKStreamIntegrationTest.java` (JAVA) | Magnitude: 138.66 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 354, structural_boundaries: 292, import: 58, state_mutation: 35
- `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/SlidingWindowedKStreamIntegrationTest.java` (JAVA) | Magnitude: 132.6 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 341, structural_boundaries: 303, import: 53, state_mutation: 34
- `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/KTableKTableForeignKeyJoinDistributedTest.java` (JAVA) | Magnitude: 70.0 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 77, import: 36, immutability_locks: 32
- `connect/runtime/src/main/java/org/apache/kafka/connect/tools/TransformationDoc.java` (JAVA) | Magnitude: 0.01 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 56, indent_spaces: 37, import: 18, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `clients/src/main/java/org/apache/kafka/common/errors/AuthenticationException.java` (JAVA) | Magnitude: 9.38 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, api: 4, args: 3
- `raft/src/main/java/org/apache/kafka/raft/errors/RaftException.java` (JAVA) | Magnitude: 9.38 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, api: 4, args: 3
- `clients/src/main/java/org/apache/kafka/common/errors/SerializationException.java` (JAVA) | Magnitude: 11.54 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, api: 5, structural_boundaries: 4, args: 4
- `clients/src/main/java/org/apache/kafka/clients/consumer/RetriableCommitFailedException.java` (JAVA) | Magnitude: 9.4 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 4, api: 4, args: 3
- `clients/src/main/java/org/apache/kafka/common/InvalidRecordException.java` (JAVA) | Magnitude: 6.72 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `connect/runtime/src/main/java/org/apache/kafka/connect/storage/PrivilegedWriteException.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `clients/src/main/java/org/apache/kafka/common/network/InvalidReceiveException.java` (JAVA) | Magnitude: 3.74 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/UnretryableException.java` (JAVA) | Magnitude: 3.74 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/RebalanceNeededException.java` (JAVA) | Magnitude: 3.74 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/modern/share/ShareGroupAssignmentBuilderTest.java` (JAVA) | Magnitude: 47.56 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 32, state_mutation: 30, core_var_decl: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `clients/src/main/java/org/apache/kafka/common/requests/AbstractRequest.java` (JAVA) | Magnitude: 267.7 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 127, branch: 96, api: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `streams/src/test/java/org/apache/kafka/streams/tests/SmokeTestDriver.java` (JAVA) | Magnitude: 462.96 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 645, structural_boundaries: 185, immutability_locks: 185, core_var_decl: 124
- `clients/src/main/java/org/apache/kafka/clients/admin/internals/AdminApiFuture.java` (JAVA) | Magnitude: 48.22 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 29, generics: 23, args: 16
- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/assignor/RangeSetTest.java` (JAVA) | Magnitude: 29.48 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 59, test: 50, core_var_decl: 27
- `server-common/src/main/java/org/apache/kafka/server/quota/SensorAccess.java` (JAVA) | Magnitude: 24.8 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, sync_locks: 13, structural_boundaries: 7, state_mutation: 5
- `clients/src/main/java/org/apache/kafka/common/serialization/FloatSerializer.java` (JAVA) | Magnitude: 6.4 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, bitwise_ops: 3, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `streams/src/test/java/org/apache/kafka/streams/state/internals/RocksDBGenericOptionsToDbOptionsColumnFamilyOptionsAdapterTest.java` (JAVA) | Magnitude: 210.14 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 265, structural_boundaries: 153, import: 52, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `storage/src/test/java/org/apache/kafka/tiered/storage/actions/ExpectListOffsetsAction.java` (JAVA) | Magnitude: 17.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 18, import: 12, api: 4
- `core/src/test/scala/integration/kafka/api/SaslGssapiSslEndToEndAuthorizationTest.scala` (SCALA) | Magnitude: 5.0 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, import: 5, safety_bypasses: 4
- `clients/src/main/java/org/apache/kafka/clients/admin/SupportedVersionRange.java` (JAVA) | Magnitude: 23.34 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 11, api: 7, args: 6
- `clients/src/main/java/org/apache/kafka/common/config/internals/BrokerSecurityConfigs.java` (JAVA) | Magnitude: 55.52 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 152, core_var_decl: 38, structural_boundaries: 37, api: 37
- `streams/src/main/java/org/apache/kafka/streams/errors/TaskIdFormatException.java` (JAVA) | Magnitude: 12.48 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 11, immutability_locks: 5, api: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `core/src/test/scala/integration/kafka/api/GroupEndToEndAuthorizationTest.scala` (SCALA) | Magnitude: 10.56 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, core_var_decl: 7, branch: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> Churn: **97.58%** | Cog Load: 59.9744% | Debt: 0.0%
- `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` -> Churn: **85.27%** | Cog Load: 56.7212% | Debt: 0.0%
- `build.gradle` -> Churn: **78.4%** | Cog Load: 50.7798% | Debt: 0.0%
- `streams/test-utils/src/main/java/org/apache/kafka/streams/TopologyTestDriver.java` -> Churn: **72.01%** | Cog Load: 18.441% | Debt: 99.9997%
- `streams/src/main/java/org/apache/kafka/streams/state/internals/MeteredWindowStore.java` -> Churn: **68.86%** | Cog Load: 18.0517% | Debt: 73.2256%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `streams/src/main/java/org/apache/kafka/streams/processor/internals/InternalTopologyBuilder.java` -> **Arpit Goyal** (100.0% isolated ownership) | Magnitude: 1240.76
- `metadata/src/test/java/org/apache/kafka/controller/ReplicationControlManagerTest.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 1227.14
- `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/WorkerTest.java` -> **Ken Huang** (100.0% isolated ownership) | Magnitude: 1213.16
- `clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 1154.64
- `clients/src/test/java/org/apache/kafka/clients/consumer/internals/FetcherTest.java` -> **Lianet Magrans** (100.0% isolated ownership) | Magnitude: 1150.26

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `clients/src/main/java/org/apache/kafka/common/utils/Utils.java` -> **Severity: 14.595** (Embedded: 0.2381 * Error Risk: 61.2909%)
- `clients/src/main/java/org/apache/kafka/common/config/ConfigDef.java` -> **Severity: 14.336** (Embedded: 0.1926 * Error Risk: 74.4139%)
- `clients/src/main/java/org/apache/kafka/common/utils/ChildFirstClassLoader.java` -> **Severity: 13.478** (Embedded: 0.1685 * Error Risk: 80.0%)
- `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -> **Severity: 12.08** (Embedded: 0.207 * Error Risk: 58.3496%)
- `clients/src/main/java/org/apache/kafka/common/utils/LogContext.java` -> **Severity: 11.182** (Embedded: 0.1398 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `clients/src/main/java/org/apache/kafka/common/KafkaException.java` -> **Severity: 2461.725** (Blast Radius: 32.823 * Doc Risk: 75.0%)
- `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -> **Severity: 1198.0** (Blast Radius: 11.98 * Doc Risk: 100.0%)
- `clients/src/main/java/org/apache/kafka/common/errors/ApiException.java` -> **Severity: 1093.28** (Blast Radius: 13.666 * Doc Risk: 80.0%)
- `clients/src/main/java/org/apache/kafka/common/config/ConfigDef.java` -> **Severity: 708.685** (Blast Radius: 13.356 * Doc Risk: 53.0612%)
- `clients/src/main/java/org/apache/kafka/common/config/ConfigException.java` -> **Severity: 494.2** (Blast Radius: 7.413 * Doc Risk: 66.6667%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2439 literal sites + 87 sites through wrappers = 2526
- **`panics_and_aborts`:** 7275 literal sites + 214 sites through wrappers = 7489

- `addAcls` (function, panics_and_aborts, primitive): 33 call sites in 1 files -- `core/src/test/scala/unit/kafka/security/authorizer/BaseAuthorizerTest.scala`
- `checkThrowsUnsupportedOperation` (function, panics_and_aborts, primitive): 19 call sites in 1 files -- `streams/src/test/java/org/apache/kafka/streams/processor/internals/ProcessorContextImplTest.java`
- `help` (function, debug_prints, primitive): 17 call sites in 9 files -- `vagrant/vagrant-up.sh`
- `help` (function, panics_and_aborts, primitive): 17 call sites in 9 files -- `vagrant/vagrant-up.sh`
- `printError` (function, debug_prints, primitive): 17 call sites in 1 files -- `tools/src/main/java/org/apache/kafka/tools/streams/StreamsGroupCommand.java`
- `cleanup` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `streams/src/test/java/org/apache/kafka/streams/state/internals/TimeOrderedKeyValueBufferTest.java`
- `commitAndThrow` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `tools/src/main/java/org/apache/kafka/tools/EndToEndLatency.java`
- `printError` (function, debug_prints, primitive): 8 call sites in 1 files -- `tools/src/main/java/org/apache/kafka/tools/consumer/group/ConsumerGroupCommand.java`
- `replicaPartitionState` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `core/src/test/scala/unit/kafka/server/MockFetcherThread.scala`
- `configEntry` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `core/src/test/scala/integration/kafka/server/DynamicBrokerReconfigurationTest.scala`
- `enqueueLast` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `coordinator-common/src/main/java/org/apache/kafka/coordinator/common/runtime/CoordinatorRuntime.java`
- `fail` (function, debug_prints, primitive): 6 call sites in 1 files -- `committer-tools/kafka-merge-pr.py`
*(+64 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 476514 call pairs -- scoped 41.8%, unique 1.6%, ambiguous 28.2%, external 28.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 422381 | 42.6% | 1.8% | 28.4% | 27.1% |
| scala | 48121 | 34.6% | 0.5% | 29.2% | 35.7% |
| python | 5330 | 41.4% | 0.0% | 5.1% | 53.5% |
| shell | 385 | 27.0% | 0.5% | 0.0% | 72.5% |
| groovy | 225 | 0.4% | 0.0% | 30.7% | 68.9% |
| ruby | 72 | 2.8% | 0.0% | 0.0% | 97.2% |

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
