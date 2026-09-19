# ARCHITECTURAL_BRIEF: kafka
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apache/kafka` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 6579 analyzed artifact(s), 1083535 LOC.
- **Load-bearing artifact:** `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -- 873 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java` -- pulls in 370 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` at magnitude 8956.62 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 6579 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 621 |
| Total LOC | 1083535 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 91.4% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5646 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1531 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5842 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 253 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 5644 | 968719 | 85.8% |
| SCALA | 295 | 92672 | 4.5% |
| JSON | 293 | 8070 | 4.5% |
| PYTHON | 95 | 9430 | 1.4% |
| SHELL | 66 | 1925 | 1.0% |
| PLAINTEXT | 57 | 5 | 0.9% |
| YAML | 46 | 1675 | 0.7% |
| BATCH | 36 | 265 | 0.5% |
| XML | 22 | 0 | 0.3% |
| MARKDOWN | 15 | 0 | 0.2% |
| DOCKERFILE | 4 | 273 | 0.1% |
| GROOVY | 3 | 342 | 0.0% |
| HTML | 2 | 12 | 0.0% |
| RUBY | 1 | 147 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `3.073`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +3.07; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 20%, Generic / Templated Code Files 16%, Data / Markup / Trivial 15%, Encapsulated Accessors Files 12%, Declarative / Non-Code 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6507 | 98.9% |
| Unknown | 5 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 67 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 621*

**Composition by Extension & Reason:**
- `.java`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1486 LOC)
- `.md`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `no_extension`: 42x Unsupported Format (.undeterminable), 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Binary Format Detected)
- `.py`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 93 LOC)
- `.png`: 47x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.converter`: 16x Unsupported Format (.converter)
- `.scala`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Saturation: Line 29 exceeds 500 chars)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2572 LOC)
- `.jpg`: 7x Excluded (Explicitly Denied Extension: '.jpg')
- `.conf`: 3x Excluded (Unsupported Extension: '.conf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.conf)
- `.xml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.predicate`: 3x Unsupported Format (.predicate)
- `.properties`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.4 | 7.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 47.5 | 56.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.5 | 8.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 43.4 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.5 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5392 | 1398 | 2 | `server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java` |
| cleanup | 3696 | 948 | 1 | `core/src/test/java/kafka/server/share/SharePartitionTest.java` |
| guards | 131460 | 4907 | 48 | `streams/src/test/java/org/apache/kafka/streams/processor/internals/TaskManagerTest.java` |
| danger | 49501 | 3800 | 18 | `core/src/test/scala/integration/kafka/api/PlaintextAdminIntegrationTest.scala` |
| concurrency | 12164 | 1085 | 3 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupCoordinatorServiceTest.java` |
| connectivity | 69134 | 5883 | 23 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` |
| io | 3846 | 547 | 0 | `tests/docker/ducker-ak` |
| crypto | 0 | 0 | 0 | - |
| ipc | 61 | 23 | 0 | `committer-tools/reviewers.py` |
| time | 4953 | 686 | 1 | `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration/IQv2StoreIntegrationTest.java` |
| serialization | 288 | 71 | 0 | `connect/runtime/src/test/java/org/apache/kafka/connect/util/clusters/EmbeddedConnect.java` |
| regex | 406 | 131 | 0 | `streams/src/test/java/org/apache/kafka/streams/processor/internals/InternalTopologyBuilderTest.java` |
| events | 8910 | 963 | 2 | `clients/src/test/java/org/apache/kafka/clients/consumer/internals/StreamsMembershipManagerTest.java` |
| tests | 103534 | 1892 | 34 | `core/src/test/java/kafka/server/share/SharePartitionTest.java` |
| docs | 15603 | 3337 | 6 | `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java` |
| debt | 3904 | 686 | 1 | `.github/scripts/develocity_reports.py` |
| mutation | 259197 | 5133 | 89 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` |
| dead_code | 28145 | 3122 | 11 | `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` |
| credential | 198 | 60 | 0 | `clients/src/test/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactoryTest.java` |
| threat | 540 | 169 | 0 | `streams/streams-scala/src/main/scala/org/apache/kafka/streams/scala/ImplicitConversions.scala` |
| ml_ai | 1475 | 420 | 0 | `connect/json/src/test/java/org/apache/kafka/connect/json/JsonConverterTest.java` |
| ui | 120 | 36 | 0 | `core/src/test/scala/unit/kafka/server/ReplicaManagerTest.scala` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/docker/ducker-ak` (Hits: 126)
- `streams/src/test/java/org/apache/kafka/streams/processor/internals/StateDirectoryTest.java` (Hits: 117)
- `tools/src/main/java/org/apache/kafka/tools/ManifestWorkspace.java` (Hits: 62)

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

- `doParseRequest` **(Compute Cores)** (@ `clients/src/main/java/org/apache/kafka/common/requests/AbstractRequest.java`) -> Impact: **375.2** | LOC: 185
- `parseResponse` **(Compute Cores)** (@ `clients/src/main/java/org/apache/kafka/common/requests/AbstractResponse.java`) -> Impact: **375.2** | LOC: 185
- `getRequest` **(Compute Cores)** (@ `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java`) -> Impact: **319.9** | LOC: 94
- `getResponse` **(Compute Cores)** (@ `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java`) -> Impact: **319.9** | LOC: 94
- `endTransaction` **(Many-Argument Workhorses)** (@ `core/src/main/scala/kafka/coordinator/transaction/TransactionCoordinator.scala`) -> Impact: **318.5** | LOC: 250
  * *Intent:* */ /** * Handling the endTxn request above the Transaction Version 2. * */
- `testFromPropsInvalid` **(Callbacks & Closures)** (@ `core/src/test/scala/unit/kafka/server/KafkaConfigTest.scala`) -> Impact: **290.4** | LOC: 327
- `__init__` **(Many-Argument Workhorses)** (@ `tests/kafkatest/services/kafka/kafka.py`) -> Impact: **240.2** | LOC: 279
- `endTransactionWithTV1` **(Many-Argument Workhorses)** (@ `core/src/main/scala/kafka/coordinator/transaction/TransactionCoordinator.scala`) -> Impact: **214.9** | LOC: 168
  * *Intent:* /** * Handling the endTxn request under the Transaction Version 1. * */
- `fieldDefault` **(Defensive Guards)** (@ `generator/src/main/java/org/apache/kafka/message/FieldSpec.java`) -> Impact: **206.8** | LOC: 186
  * *Intent:* /** * Get a string representation of the field default. * * @param headerGenerator The header generator in case we need to add imports. * @param struc...
- `response` **(Type Conversions)** (@ `server/src/main/java/org/apache/kafka/network/RequestConvertToJson.java`) -> Impact: **169.9** | LOC: 176

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `clients/src/test/java/org/apache/kafka/clients/consumer/internals` | 67 | 15830.38 | 21.22% | 0.0% |
| `group-coordinator/src/test/java/org/apache/kafka/coordinator/group` | 18 | 15527.62 | 25.1% | 0.0% |
| `streams/src/main/java/org/apache/kafka/streams/state/internals` | 203 | 15500.02 | 16.79% | 39.36% |
| `clients/src/main/java/org/apache/kafka/clients/consumer/internals` | 97 | 15318.92 | 24.59% | 33.84% |
| `streams/src/main/java/org/apache/kafka/streams/processor/internals` | 95 | 14803.98 | 25.04% | 34.7% |
| `streams/src/test/java/org/apache/kafka/streams/state/internals` | 151 | 14565.28 | 14.38% | 0.0% |
| `streams/src/test/java/org/apache/kafka/streams/processor/internals` | 73 | 13810.88 | 17.08% | 0.0% |
| `streams/integration-tests/src/test/java/org/apache/kafka/streams/integration` | 87 | 11917.0 | 25.45% | 0.0% |
| `core/src/test/scala/unit/kafka/server` | 101 | 10919.6 | 15.77% | 0.0% |
| `clients/src/main/java/org/apache/kafka/common/requests` | 192 | 10440.32 | 20.23% | 3.44% |

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
- `core/src/test/java/kafka/server/share/SharePartitionTest.java` -> **262** Orphaned Functions | **0** Duplicates
- `streams/src/main/java/org/apache/kafka/streams/state/internals/RocksDBGenericOptionsToDbOptionsColumnFamilyOptionsAdapter.java` -> **175** Orphaned Functions | **0** Duplicates
- `streams/src/test/java/org/apache/kafka/streams/StreamsConfigTest.java` -> **170** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `clients/src/test/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactoryTest.java` -> **100.0%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/authenticator/SaslAuthenticatorTest.java` -> **99.9981%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/oauthbearer/internals/secured/assertion/AssertionUtils.java` -> **99.9795%** Exposure
- `clients/src/main/java/org/apache/kafka/common/security/ssl/DefaultSslEngineFactory.java` -> **68.1223%** Exposure
- `clients/src/test/java/org/apache/kafka/common/security/oauthbearer/ClientAssertionKeycloakIntegrationTest.java` -> **30.9556%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `27` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `90133` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 8956.62 | **LOC:** 27677 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **232**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.8%), Guard Balance (formerly Safety Score) (78.5%), Complexity Load (formerly Cognitive Load) (60.4%), Concurrency Surface (formerly Concurrency) (12.1%)
- **Documentation Coverage:** 99.7587% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generatePendingAssignmentCases` **(Many-Argument Workhorses)** (Impact: 58.6)
  * `testLastStaticConsumerProtocolMemberReplacedByClassicProtocolMember` **(Compute Cores)** (Impact: 28.6)
  * `testReconciliationProcess` **(I/O & Config Routines)** (Impact: 23.1)
  * `testStreamsReconciliationProcess` **(I/O & Config Routines)** (Impact: 22.5)
  * `testReconciliationInJoiningConsumerGroupWithCooperativeProtocol` **(I/O & Config Routines)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 6137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 4126`, `args: 764`, `func_start: 424`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 429`, `state_mutation: 6003`, `dead_code: 7`, `unreferenced_by_name: 405`
* *Architecture:* `api: 407`, `concurrency: 5`, `import: 232`
* *Defense:* `safety: 7`, `doc: 2`, `test: 2456`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 104):` java.nio.ByteBuffer, java.util.ArrayList, java.util.Arrays, java.util.Collections, java.util.Comparator, java.util.HashMap, java.util.HashSet, java.util.LinkedHashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/examples/fixtures/client-secrets/client.keystore.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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

### `clients/src/test/java/org/apache/kafka/clients/admin/KafkaAdminClientTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 4140.38 | **LOC:** 11791 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **307**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.5%), Complexity Load (formerly Cognitive Load) (58.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.8%), Concurrency Surface (formerly Concurrency) (43.4%)
- **Documentation Coverage:** 98.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareDescribeQuorumResponse` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `testAddRaftVoterRequest` **(Defensive Guards)** (Impact: 23.3)
  * `testRemoveRaftVoterRequest` **(Defensive Guards)** (Impact: 23.0)
  * `defaultQuorumInfo` **(Stateful Encapsulated Methods)** (Impact: 19.1)
  * `testDescribeTopicsWithDescribeTopicPartitionsApiEdgeCase` **(Annotated & Test Methods)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 215
* *State Mutation (weighted view):* 2171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 3279`, `args: 615`, `func_start: 363`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 473`, `state_mutation: 2017`, `unreferenced_by_name: 276`
* *Architecture:* `api: 292`, `concurrency: 60`, `import: 307`
* *Defense:* `safety: 344`, `doc: 6`, `test: 1110`, `sync_locks: 5`, `immutability_locks: 447`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 155):` java.net.InetSocketAddress, java.nio.ByteBuffer, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collection, java.util.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/main/java/org/apache/kafka/clients/admin/KafkaAdminClient.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3398.0 | **LOC:** 5180 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **287**; blast radius 0.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.8%), Guard Balance (formerly Safety Score) (84.7%), Debt Markers (formerly Tech Debt) (54.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.9%)
- **Documentation Coverage:** 88.9655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alterPartitionReassignments` **(Many-Argument Workhorses)** (Impact: 74.9)
  * `getCreateTopicsCall` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `updateFeatures` **(Compute Cores)** (Impact: 51.4)
  * `describeReplicaLogDirs` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `listPartitionReassignments` **(Compute Cores)** (Impact: 43.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 182 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 669`, `structural_boundaries: 1281`, `args: 408`, `func_start: 328`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 194`, `state_mutation: 347`, `dead_code: 2`, `duplicate_logic: 45`
* *Architecture:* `api: 110`, `concurrency: 26`, `import: 287`
* *Defense:* `safety: 40`, `doc: 68`, `test: 2`, `sync_locks: 15`, `immutability_locks: 315`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.00076
  * `Imports (Out-Degree: 175):` java.security.InvalidKeyException, java.security.NoSuchAlgorithmException, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections, java.util.Comparator...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupMetadataManager.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3359.28 | **LOC:** 8993 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 31.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **231**; blast radius 0.072; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (82.4%), Concurrency Surface (formerly Concurrency) (19.1%)
- **Documentation Coverage:** 15.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `streamsGroupHeartbeat` **(Compute Cores)** (Impact: 48.7)
    * *Intent:* * @param rackId The rack ID from the request or null. * @param rebalanceTimeoutMs The rebalance time...
  * `maybeUpdateRegularExpressions` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* /** * Check whether the member has updated its subscribed topic regular expression and * may trigger...
  * `classicGroupLeaveToClassicGroup` **(Compute Cores)** (Impact: 39.0)
    * *Intent:* /** * Handle a classic LeaveGroupRequest to a ClassicGroup. * * @param group The ClassicGroup. * @pa...
  * `maybeUpdateTargetAssignment` **(Many-Argument Workhorses)** (Impact: 38.1)
    * *Intent:* /** * Updates the target assignment according to the updated member and subscription metadata. * * @...
  * `maybeUpdateTargetAssignment` **(Many-Argument Workhorses)** (Impact: 37.5)
    * *Intent:* /** * Updates the target assignment according to the updated member and subscription metadata. * * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 235 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 1021
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 838`, `structural_boundaries: 1159`, `args: 378`, `func_start: 256`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 255`, `state_mutation: 551`, `dead_code: 8`
* *Architecture:* `api: 74`, `concurrency: 27`, `import: 231`
* *Defense:* `safety: 116`, `doc: 241`, `sync_locks: 1`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.072
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000152
  * `Imports (Out-Degree: 124):` java.nio.ByteBuffer, java.util.ArrayList, java.util.Collections, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Map, java.util.Objects...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/test/java/kafka/server/share/SharePartitionTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 2933.06 | **LOC:** 12683 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 30.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **94**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.4%), Concurrency Surface (formerly Concurrency) (75.9%), Complexity Load (formerly Cognitive Load) (25.1%), Guard Balance (formerly Safety Score) (13.1%)
- **Documentation Coverage:** 97.307% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertionFailedMessage` **(Stateful Encapsulated Methods)** (Impact: 28.8)
  * `testMaybeInitializeWithErrorPartitionResponse` **(I/O & Config Routines)** (Impact: 25.6)
  * `testWriteShareGroupStateFailure` **(I/O & Config Routines)** (Impact: 21.4)
  * `testContainsAbortMarker` **(Annotated & Test Methods)** (Impact: 17.7)
  * `testWriteShareGroupStateWithInvalidTopicsData` **(Annotated & Test Methods)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 382
* *State Mutation (weighted view):* 813
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 1867`, `args: 508`, `func_start: 292`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 723`, `dead_code: 8`, `unreferenced_by_name: 262`
* *Architecture:* `api: 266`, `concurrency: 262`, `import: 94`
* *Defense:* `safety: 17`, `doc: 8`, `test: 3907`, `sync_locks: 4`, `immutability_locks: 18`, `cleanup: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` java.nio.ByteBuffer, java.util.ArrayList, java.util.HashMap, java.util.Iterator, java.util.List, java.util.Map, java.util.Optional, java.util.OptionalInt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/common/requests/RequestResponseTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 2919.2 | **LOC:** 4029 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **305**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Guard Balance (formerly Safety Score) (91.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.6%)
- **Documentation Coverage:** 99.3174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getRequest` **(Compute Cores)** (Impact: 319.9)
  * `getResponse` **(Compute Cores)** (Impact: 319.9)
  * `verifyDescribeConfigsResponse` **(Stateful Encapsulated Methods)** (Impact: 31.6)
  * `createOffsetFetchRequest` **(Stateful Encapsulated Methods)** (Impact: 16.5)
  * `createFetchResponse` **(Stateful Encapsulated Methods)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 1515
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 491`, `structural_boundaries: 1645`, `args: 281`, `func_start: 252`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 1235`, `unreferenced_by_name: 41`
* *Architecture:* `api: 42`, `import: 305`
* *Defense:* `safety: 5`, `doc: 1`, `test: 195`, `immutability_locks: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` java.nio.BufferUnderflowException, java.nio.ByteBuffer, java.nio.charset.StandardCharsets, java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collections, java.util.Collections.emptyList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupCoordinatorServiceTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2874.78 | **LOC:** 5962 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **141**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Guard Balance (formerly Safety Score) (87.8%), Complexity Load (formerly Cognitive Load) (73.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testFetchOffsets` **(Compute Cores)** (Impact: 22.1)
  * `testStreamsHeartbeatRequestValidation` **(I/O & Config Routines)** (Impact: 21.1)
  * `testFetchOffsetsWithWrappedError` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `testConsumerHeartbeatRequestValidation` **(I/O & Config Routines)** (Impact: 12.8)
  * `testDeleteShareGroupOffsetsSuccessWithErrorTopics` **(I/O & Config Routines)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 42 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 477
* *State Mutation (weighted view):* 1538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 1391`, `args: 214`, `func_start: 140`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 205`, `state_mutation: 1270`, `unreferenced_by_name: 128`
* *Architecture:* `api: 134`, `concurrency: 267`, `import: 141`
* *Defense:* `test: 488`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 63):` java.net.InetAddress, java.util.Arrays, java.util.HashSet, java.util.List, java.util.Map, java.util.Optional, java.util.OptionalInt, java.util.Properties...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/kafkatest/services/kafka/kafka.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2521.78 | **LOC:** 2048 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.3%), Connectivity (formerly Api Exposure) (62.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.7%), Complexity Load (formerly Cognitive Load) (28.3%)
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
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 421`, `dead_code: 3`, `planned_debt: 3`
* *Architecture:* `io: 24`, `api: 89`, `import: 20`
* *Defense:* `safety: 6`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .config, ducktape.cluster.remoteaccount, ducktape.services.service, ducktape.utils.util, json, kafkatest.directory_layout.kafka_path, kafkatest.services.kafka, kafkatest.services.kafka.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/scala/kafka/server/KafkaApis.scala` (SCALA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2385.26 | **LOC:** 4290 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 8.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **109**; blast radius 0.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.6%), Mutation Surface (formerly State Flux) (75.6%), Guard Balance (formerly Safety Score) (72.5%), Complexity Load (formerly Cognitive Load) (20.8%)
- **Documentation Coverage:** 91.9679% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Callbacks & Closures)** (Impact: 152.9)
    * *Intent:* /** * Top-level method that handles all requests and multiplexes to the right api */
  * `handleShareFetchRequest` **(Compute Cores)** (Impact: 78.2)
    * *Intent:* /** * Handle a shareFetch request */
  * `handleFetchRequest` **(Compute Cores)** (Impact: 68.7)
    * *Intent:* /** * Handle a fetch request */
  * `handleProduceRequest` **(Many-Argument Workhorses)** (Impact: 63.6)
    * *Intent:* /** * Handle a produce request */
  * `handleTopicMetadataRequest` **(Compute Cores)** (Impact: 54.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 782`, `structural_boundaries: 423`, `args: 506`, `func_start: 136`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 120`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 112`, `import: 66`
* *Defense:* `doc: 11`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000304
  * `Imports (Out-Degree: 53):` AddPartitionsToTxnResultCollection, ApiMessage, ClientMetricsManager, ConcurrentHashMap, DeleteRecordsTopicResult, Errors, FetchManager, FetchParams...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `streams/src/test/java/org/apache/kafka/streams/processor/internals/TaskManagerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1978.7 | **LOC:** 5001 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **105**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Complexity Load (formerly Cognitive Load) (42.9%), Guard Balance (formerly Safety Score) (16.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitDuringHandleCorruptedWithEOS` **(I/O & Config Routines)** (Impact: 28.0)
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitDuringRevocationWithEOS` **(I/O & Config Routines)** (Impact: 26.6)
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitWithAlos` **(I/O & Config Routines)** (Impact: 23.6)
  * `shouldCloseAndReviveUncorruptedTasksWhenTimeoutExceptionThrownFromCommitDuringRevocationWithAlos` **(I/O & Config Routines)** (Impact: 21.2)
  * `shouldCommitAllActiveTasksThatNeedCommittingOnHandleRevocationWithEosV2` **(I/O & Config Routines)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 73 instances
* *Concurrency (weighted view):* 474
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 796`, `args: 238`, `func_start: 178`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 125`, `dead_code: 4`, `unreferenced_by_name: 165`
* *Architecture:* `io: 12`, `api: 166`, `concurrency: 89`, `import: 105`
* *Defense:* `safety: 1`, `test: 1466`, `sync_locks: 5`, `immutability_locks: 811`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` java.io.File, java.nio.file.Files, java.nio.file.Path, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Arrays.asList, java.util.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/main/java/kafka/server/share/SharePartition.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1910.38 | **LOC:** 3427 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 26.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **73**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.6%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (52.0%)
- **Documentation Coverage:** 62.3853% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acquire` **(Many-Argument Workhorses)** (Impact: 154.0)
    * *Intent:* * (the offset from which the log was read) with the first base offset of the fetch response. Any * b...
  * `acknowledgePerOffsetBatchRecords` **(Many-Argument Workhorses)** (Impact: 103.2)
  * `acquireSubsetBatchRecords` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `acknowledgeBatchRecords` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `acknowledgeCompleteBatch` **(Many-Argument Workhorses)** (Impact: 62.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 113 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 575`, `structural_boundaries: 430`, `args: 124`, `func_start: 101`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 198`, `dead_code: 8`, `planned_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 9`, `concurrency: 24`, `import: 73`
* *Defense:* `safety: 87`, `doc: 75`, `sync_locks: 127`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000152
  * `Imports (Out-Degree: 45):` java.util.ArrayList, java.util.Comparator, java.util.HashMap, java.util.HashSet, java.util.Iterator, java.util.List, java.util.Map, java.util.NavigableMap...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `raft/src/main/java/org/apache/kafka/raft/KafkaRaftClient.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1712.2 | **LOC:** 4153 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **105**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.2%), Guard Balance (formerly Safety Score) (75.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.9%), Concurrency Surface (formerly Concurrency) (31.5%)
- **Documentation Coverage:** 85.7868% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybeHandleCommonResponse` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* * @param epoch Epoch received from the response * @param leaderEndpoints the endpoints of the leader...
  * `handleFetchResponse` **(Many-Argument Workhorses)** (Impact: 46.5)
  * `handleFetchSnapshotResponse` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `handleVoteResponse` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 85 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 519`, `args: 238`, `func_start: 166`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 172`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 33`, `concurrency: 28`, `import: 105`
* *Defense:* `safety: 23`, `doc: 26`, `sync_locks: 6`, `immutability_locks: 69`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.000643 | `Ripple Effect (Closeness):` 0.012906
  * `Imports (Out-Degree: 60):` java.net.InetSocketAddress, java.nio.ByteBuffer, java.util.Collection, java.util.HexFormat, java.util.IdentityHashMap, java.util.Iterator, java.util.List, java.util.Map...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `connect/runtime/src/main/java/org/apache/kafka/connect/runtime/distributed/DistributedHerder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1697.64 | **LOC:** 3033 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **101**; blast radius 0.109; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.2%), Guard Balance (formerly Safety Score) (90.7%), Concurrency Surface (formerly Concurrency) (74.9%), Complexity Load (formerly Cognitive Load) (40.0%)
- **Documentation Coverage:** 86.6029% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tick` **(I/O & Config Routines)** (Impact: 59.4)
    * *Intent:* // public for testing
  * `DistributedHerder` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* // visible for testing
  * `doFenceZombieSourceTasks` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `validateSourceConnectorExactlyOnceSupport` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `modifyConnectorOffsets` **(Stateful Encapsulated Methods)** (Impact: 37.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 85 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 466`, `structural_boundaries: 498`, `args: 209`, `func_start: 146`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 243`, `state_mutation: 161`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 67`, `concurrency: 53`, `import: 101`
* *Defense:* `safety: 87`, `doc: 22`, `sync_locks: 22`, `immutability_locks: 102`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.001064
  * `Imports (Out-Degree: 62):` jakarta.ws.rs.core.Response, jakarta.ws.rs.core.UriBuilder, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Map...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `clients/src/test/java/org/apache/kafka/clients/consumer/KafkaConsumerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1665.14 | **LOC:** 4133 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **165**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.8%), Concurrency Surface (formerly Concurrency) (65.9%), Complexity Load (formerly Cognitive Load) (59.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.6%)
- **Documentation Coverage:** 98.452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumerCloseTest` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `testPollSendsRequestToJoin` **(Annotated & Test Methods)** (Impact: 13.9)
  * `prepareOffsetCommitResponse` **(Stateful Encapsulated Methods)** (Impact: 13.1)
  * `newConsumerConfig` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `listOffsetsResponse` **(Stateful Encapsulated Methods)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 653
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 1040`, `args: 304`, `func_start: 192`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 421`, `dead_code: 1`, `planned_debt: 34`, `fragile_debt: 14`, `duplicate_logic: 4`, `unreferenced_by_name: 126`
* *Architecture:* `api: 151`, `concurrency: 38`, `import: 165`
* *Defense:* `safety: 53`, `doc: 4`, `test: 524`, `sync_locks: 3`, `immutability_locks: 106`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 84):` java.lang.management.ManagementFactory, java.nio.ByteBuffer, java.time.Duration, java.util.AbstractMap, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1660.72 | **LOC:** 4753 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 30.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **107**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.1%), Guard Balance (formerly Safety Score) (68.9%), Complexity Load (formerly Cognitive Load) (60.8%)
- **Documentation Coverage:** 94.5848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumeMessages` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `testRenewAcknowledgementNoResultInPoll` **(I/O & Config Routines)** (Impact: 14.2)
  * `testFetchWithThrottledDeliveryValidateDeliveryCount` **(Callbacks & Closures)** (Impact: 12.7)
  * `ComplexShareConsumer` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `testShareConsumerAfterCoordinatorMovement` **(I/O & Config Routines)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 296
* *State Mutation (weighted view):* 565
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 957`, `args: 388`, `func_start: 165`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 203`, `state_mutation: 333`, `dead_code: 1`, `unreferenced_by_name: 100`
* *Architecture:* `api: 117`, `concurrency: 101`, `import: 107`
* *Defense:* `safety: 170`, `doc: 9`, `test: 341`, `sync_locks: 6`, `immutability_locks: 30`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` com.yammer.metrics.core.Meter, java.nio.ByteBuffer, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.HashMap, java.util.HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streams/src/main/java/org/apache/kafka/streams/processor/internals/InternalTopologyBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1623.66 | **LOC:** 2354 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **37** in-repo importer(s); it depends on **49**; blast radius 0.944; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.5%), Complexity Load (formerly Cognitive Load) (72.4%), Connectivity (formerly Api Exposure) (59.8%), Mutation Surface (formerly State Flux) (46.0%)
- **Documentation Coverage:** 90.0332% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Defensive Guards)** (Impact: 57.7)
  * `buildSinkNode` **(Stateful Encapsulated Methods)** (Impact: 55.2)
  * `buildProcessorNode` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `maybeAddToResetList` **(Stateful Encapsulated Methods)** (Impact: 35.6)
  * `connectProcessorAndStateStore` **(Stateful Encapsulated Methods)** (Impact: 34.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 494`, `structural_boundaries: 455`, `args: 172`, `func_start: 176`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 176`, `dead_code: 6`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 140`, `concurrency: 16`, `import: 49`
* *Defense:* `safety: 43`, `doc: 12`, `sync_locks: 16`, `immutability_locks: 492`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.944
  * `Choke Point (Betweenness):` 0.000982 | `Ripple Effect (Closeness):` 0.038097
  * `Imports (Out-Degree: 22):` java.io.Serializable, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections, java.util.Comparator, java.util.HashMap...
  * `Imported By (In-Degree: 37):` (Excluded from Brief to save tokens)

### `metadata/src/main/java/org/apache/kafka/controller/ReplicationControlManager.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1582.96 | **LOC:** 2550 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **120**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (89.0%), Complexity Load (formerly Cognitive Load) (39.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.9%)
- **Documentation Coverage:** 83.7037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createTopic` **(Many-Argument Workhorses)** (Impact: 105.2)
  * `validateAlterPartitionData` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* /** * Validate the partition information included in the alter partition request. * * @param brokerI...
  * `createPartitions` **(Many-Argument Workhorses)** (Impact: 46.8)
  * `generateLeaderAndIsrUpdates` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* * changes if necessary. * * @param context A human-readable context string used in log4j logging. * ...
  * `alterPartition` **(Many-Argument Workhorses)** (Impact: 40.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 567`, `args: 118`, `func_start: 92`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 210`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 44`, `import: 120`
* *Defense:* `safety: 26`, `doc: 34`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000152
  * `Imports (Out-Degree: 53):` java.util.AbstractMap.SimpleImmutableEntry, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections, java.util.HashMap, java.util.HashSet, java.util.Iterator...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/WorkerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1509.16 | **LOC:** 3241 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **154**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.9%), Concurrency Surface (formerly Concurrency) (55.2%), Complexity Load (formerly Cognitive Load) (48.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.1%)
- **Documentation Coverage:** 98.9637% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alterOffsetsSinkConnector` **(Stateful Encapsulated Methods)** (Impact: 26.1)
  * `testConnectorGeneratesTooManyTasks` **(Compute Cores)** (Impact: 23.7)
  * `mockVersionedTaskIsolation` **(Stateful Encapsulated Methods)** (Impact: 22.4)
  * `mockAdminListConsumerGroupOffsets` **(Stateful Encapsulated Methods)** (Impact: 15.5)
  * `testAlterOffsetsSinkConnectorDeleteOffsetsError` **(Annotated & Test Methods)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 123 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 658
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 847`, `args: 173`, `func_start: 115`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 154`, `state_mutation: 412`, `dead_code: 16`, `planned_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 68`
* *Architecture:* `api: 73`, `concurrency: 48`, `import: 154`
* *Defense:* `safety: 10`, `doc: 2`, `test: 618`, `immutability_locks: 30`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 72):` java.lang.management.ManagementFactory, java.util.Collection, java.util.Collections, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Map, java.util.Set...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streams/src/test/java/org/apache/kafka/streams/TopologyTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1496.84 | **LOC:** 2489 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **70**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.7%), Complexity Load (formerly Cognitive Load) (49.6%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tableNamedMaterializedCountWithTopologyConfigShouldPreserveTopologyStructure` **(Compute Cores)** (Impact: 26.3)
  * `tableNamedMaterializedCountShouldPreserveTopologyStructure` **(Compute Cores)** (Impact: 24.8)
  * `tableAnonymousMaterializedCountShouldPreserveTopologyStructure` **(Compute Cores)** (Impact: 24.8)
  * `tableAnonymousStoreTypedMaterializedCountShouldPreserveTopologyStructure` **(Compute Cores)** (Impact: 24.7)
  * `addProcessorWithStore` **(Stateful Encapsulated Methods)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 513`, `structural_boundaries: 392`, `args: 185`, `func_start: 125`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 250`, `unreferenced_by_name: 110`
* *Architecture:* `api: 115`, `import: 70`
* *Defense:* `safety: 30`, `test: 268`, `immutability_locks: 339`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` java.time.Duration, java.time.Duration.ofMillis, java.util.Collections, java.util.HashMap, java.util.HashSet, java.util.Map, java.util.Properties, java.util.Random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/src/test/java/org/apache/kafka/clients/producer/KafkaProducerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1491.0 | **LOC:** 3259 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **152**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.4%), Concurrency Surface (formerly Concurrency) (69.1%), Complexity Load (formerly Cognitive Load) (48.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectAppend` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `testAcksAndIdempotenceForIdempotentProducers` **(I/O & Config Routines)** (Impact: 11.1)
  * `testInitTransactionsWithKeepPreparedTxnAndTwoPhaseCommit` **(Defensive Guards)** (Impact: 9.5)
  * `testSendNotAllowedInPreparedTransactionState` **(Annotated & Test Methods)** (Impact: 8.3)
  * `testSendOffsetsNotAllowedInPreparedTransactionState` **(Annotated & Test Methods)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 192 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 664
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 1109`, `args: 240`, `func_start: 146`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 146`, `state_mutation: 280`, `dead_code: 1`, `duplicate_logic: 14`, `unreferenced_by_name: 100`
* *Architecture:* `api: 136`, `concurrency: 48`, `import: 152`
* *Defense:* `safety: 100`, `test: 380`, `sync_locks: 3`, `immutability_locks: 47`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 80):` java.lang.management.ManagementFactory, java.nio.charset.StandardCharsets, java.time.Duration, java.util.ArrayList, java.util.Arrays, java.util.Collection, java.util.Collections, java.util.Collections.emptyMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupMetadataManagerTest.java` -> Churn: **96.81%** | Cog Load: 60.3804% | Debt: 0.0%
- `core/src/main/java/kafka/server/share/SharePartition.java` -> Churn: **89.63%** | Cog Load: 51.9891% | Debt: 13.7236%
- `clients/clients-integration-tests/src/test/java/org/apache/kafka/clients/consumer/ShareConsumerTest.java` -> Churn: **85.07%** | Cog Load: 60.7848% | Debt: 0.0%
- `streams/test-utils/src/main/java/org/apache/kafka/streams/TopologyTestDriver.java` -> Churn: **71.55%** | Cog Load: 21.3587% | Debt: 99.9997%
- `streams/src/main/java/org/apache/kafka/streams/state/internals/MeteredWindowStore.java` -> Churn: **67.58%** | Cog Load: 21.603% | Debt: 73.2256%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `streams/src/main/java/org/apache/kafka/streams/processor/internals/InternalTopologyBuilder.java` -> **Arpit Goyal** (100.0% isolated ownership) | Magnitude: 1623.66
- `connect/runtime/src/test/java/org/apache/kafka/connect/runtime/distributed/DistributedHerderTest.java` -> **majialong** (100.0% isolated ownership) | Magnitude: 1475.36
- `metadata/src/test/java/org/apache/kafka/controller/ReplicationControlManagerTest.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 1293.44
- `clients/src/test/java/org/apache/kafka/clients/admin/MockAdminClient.java` -> **Mickael Maison** (100.0% isolated ownership) | Magnitude: 1290.24
- `generator/src/main/java/org/apache/kafka/message/MessageDataGenerator.java` -> **Sanskar Jhajharia** (100.0% isolated ownership) | Magnitude: 1011.8

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `clients/src/main/java/org/apache/kafka/clients/producer/KafkaProducer.java` -> **Severity: 0.556** (Bridge: 0.0058 * Flux: 96.6519%)
- `clients/src/main/java/org/apache/kafka/clients/consumer/internals/AsyncKafkaConsumer.java` -> **Severity: 0.228** (Bridge: 0.0026 * Flux: 87.5209%)
- `streams/src/main/java/org/apache/kafka/streams/processor/internals/StreamThread.java` -> **Severity: 0.202** (Bridge: 0.0034 * Flux: 59.638%)
- `clients/src/main/java/org/apache/kafka/clients/producer/internals/TransactionManager.java` -> **Severity: 0.167** (Bridge: 0.0018 * Flux: 95.1086%)
- `core/src/test/scala/unit/kafka/utils/TestUtils.scala` -> **Severity: 0.144** (Bridge: 0.0014 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `clients/src/main/java/org/apache/kafka/common/utils/Utils.java` -> **Severity: 15.345** (Embedded: 0.1907 * Error Risk: 80.4536%)
- `clients/src/main/java/org/apache/kafka/common/config/ConfigDef.java` -> **Severity: 14.042** (Embedded: 0.1589 * Error Risk: 88.3896%)
- `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -> **Severity: 13.365** (Embedded: 0.1823 * Error Risk: 73.33%)
- `clients/src/main/java/org/apache/kafka/common/Uuid.java` -> **Severity: 12.109** (Embedded: 0.1495 * Error Risk: 80.9998%)
- `clients/src/main/java/org/apache/kafka/common/config/ConfigException.java` -> **Severity: 9.963** (Embedded: 0.1602 * Error Risk: 62.1788%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `clients/src/main/java/org/apache/kafka/common/TopicPartition.java` -> **Severity: 1327.7** (Blast Radius: 13.277 * Doc Risk: 100.0%)
- `clients/src/main/java/org/apache/kafka/common/KafkaException.java` -> **Severity: 1326.0** (Blast Radius: 17.68 * Doc Risk: 75.0%)
- `clients/src/main/java/org/apache/kafka/common/errors/TimeoutException.java` -> **Severity: 979.275** (Blast Radius: 13.057 * Doc Risk: 75.0%)
- `clients/src/main/java/org/apache/kafka/common/utils/internals/BytesUtils.java` -> **Severity: 599.1** (Blast Radius: 11.982 * Doc Risk: 50.0%)
- `clients/src/main/java/org/apache/kafka/common/protocol/ApiKeys.java` -> **Severity: 575.092** (Blast Radius: 6.251 * Doc Risk: 92.0%)

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
