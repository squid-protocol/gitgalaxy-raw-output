# ARCHITECTURAL_BRIEF: elasticsearch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/elasticsearch` |
| **Timestamp** | `2026-08-07T04:33:58.636066+00:00` |
| **Scan Duration** | `117.28s` |
| **Git Branch** | `main` |
| **Git Commit** | `294a6f34f172eedc0e922627982b1dbec702c77a` |
| **Git Remote** | `https://github.com/elastic/elasticsearch` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 27909 malicious artifacts.

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
| Total Artifacts | 38976 |
| Analyzed Artifacts (Scanned) | 31539 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7437 |
| Total LOC | 3853645 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.9% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1413 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 546 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 27594 | 3756838 | 87.5% |
| PLAINTEXT | 2209 | 761 | 7.0% |
| JSON | 1133 | 68317 | 3.6% |
| GROOVY | 134 | 11818 | 0.4% |
| CSV | 116 | 6546 | 0.4% |
| SHELL | 90 | 2559 | 0.3% |
| MARKDOWN | 83 | 0 | 0.3% |
| XML | 82 | 0 | 0.3% |
| BATCH | 26 | 775 | 0.1% |
| CPP | 21 | 3646 | 0.1% |
| SQLITE | 13 | 194 | 0.0% |
| DOCKERFILE | 11 | 582 | 0.0% |
| PYTHON | 5 | 444 | 0.0% |
| TYPESCRIPT | 5 | 257 | 0.0% |
| HTML | 4 | 45 | 0.0% |
| CSS | 3 | 294 | 0.0% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| POWERSHELL | 2 | 153 | 0.0% |
| PROTO | 2 | 31 | 0.0% |
| JAVASCRIPT | 2 | 31 | 0.0% |
| RUBY | 1 | 351 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.544`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 17565 | 55.7% |
| file_cluster_8 | 10050 | 31.9% |
| file_cluster_16 | 551 | 1.7% |
| file_cluster_0 | 543 | 1.7% |
| file_cluster_4 | 415 | 1.3% |
| Unknown | 107 | 0.3% |
| file_cluster_17 | 18 | 0.1% |
| file_cluster_12 | 16 | 0.1% |
| file_cluster_11 | 11 | 0.0% |
| file_cluster_6 | 10 | 0.0% |
| file_cluster_9 | 7 | 0.0% |
| file_cluster_7 | 7 | 0.0% |
| file_cluster_15 | 4 | 0.0% |
| file_cluster_2 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2184 | 6.9% |
| Static: Minified & Vendor Opaque Mass | 50 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7437*

**Composition by Extension & Reason:**
- `.md`: 2566x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 131 LOC)
- `.txt`: 783x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.gradle`: 496x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 382x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 362x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Embedded Array/Matrix Payload: 17589 commas in 780 LOC), 1x Excluded (Embedded Array/Matrix Payload: 6286 commas in 893 LOC)
- `.json`: 342x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6174 LOC), 1x Excluded (Massive Static Asset Blob: 3210 LOC)
- `.expected`: 190x Unsupported Format (.expected), 66x Excluded (Saturation: Line 3 exceeds 500 chars), 27x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.esql`: 255x Unsupported Format (.esql)
- `.svg`: 235x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.zip`: 222x Excluded (Explicitly Denied Extension: '.zip')
- `no_extension`: 164x Unsupported Format (.undeterminable), 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.csv-spec`: 178x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 36 exceeds 500 chars)
- `.java`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 1969 commas in 634 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5806 LOC)
- `.yml`: 151x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 67 exceeds 500 chars), 2x Excluded (Saturation: Line 41 exceeds 500 chars)
- `.png`: 149x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 14.3 | 8.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 42.7 | 53.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.3 | 6.2 | 6.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 95.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.0 | 1.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.3 | 18.6 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileInstrumentation.java` (Hits: 173)
- `distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/InstallPluginActionTests.java` (Hits: 108)
- `.buildkite/hooks/pre-command` (Hits: 86)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ESTestCase.java** (`test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java`) — 4351 inbound connections
2. **Settings.java** (`server/src/main/java/org/elasticsearch/common/settings/Settings.java`) — 4316 inbound connections
3. **StreamInput.java** (`server/src/main/java/org/elasticsearch/common/io/stream/StreamInput.java`) — 3478 inbound connections
4. **XContentBuilder.java** (`libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java`) — 3434 inbound connections
5. **StreamOutput.java** (`server/src/main/java/org/elasticsearch/common/io/stream/StreamOutput.java`) — 2997 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Security.java** (`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/Security.java`) — 468 outbound dependencies
2. **MachineLearning.java** (`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/MachineLearning.java`) — 464 outbound dependencies
3. **ActionModule.java** (`server/src/main/java/org/elasticsearch/action/ActionModule.java`) — 421 outbound dependencies
4. **EsqlFunctionRegistry.java** (`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/EsqlFunctionRegistry.java`) — 267 outbound dependencies
5. **NodeConstruction.java** (`server/src/main/java/org/elasticsearch/node/NodeConstruction.java`) — 266 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `init` (@ `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileInstrumentation.java`) -> Impact: **2149.7** | LOC: 422
- `init` (@ `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/NetworkInstrumentation.java`) -> Impact: **1903.0** | LOC: 533
- `getTableWithHeader` (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestIndicesAction.java`) -> Impact: **1899.8** | LOC: 374
- `testFailureStoreAccess` (@ `x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/failurestore/FailureStoreSecurityRestIT.java`) -> Impact: **1417.5** | LOC: 949
- `testBinaryComparisons` (@ `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/planner/QueryTranslatorTests.java`) -> Impact: **1409.2** | LOC: 343
- `assertUnitRoundingSameAsJavaUtilTimeImpl` (@ `server/src/test/java/org/elasticsearch/common/RoundingTests.java`) -> Impact: **1322.4** | LOC: 912
  * *Intent:* /** * Randomized test on TimeUnitRounding. Test uses random * {@link DateTimeUnit} and {@link ZoneId} and often (50% of the time) * chooses test dates...
- `getTableWithHeader` (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestNodesAction.java`) -> Impact: **1269.5** | LOC: 202
- `assertInterval` (@ `server/src/test/java/org/elasticsearch/common/RoundingTests.java`) -> Impact: **1184.9** | LOC: 898
  * *Intent:* /** * This test chooses a date in the middle of the transition, so that we can test * if the transition which is before the minLookup, but still shoul...
- `TestConfiguration` (@ `qa/vector/src/main/java/org/elasticsearch/test/knn/TestConfiguration.java`) -> Impact: **1150.6** | LOC: 894
- `getTableWithHeader` (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestShardsAction.java`) -> Impact: **1023.8** | LOC: 157

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/resources/ssl` | 13 | 60001.62 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl` | 12 | 55001.22 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/smoke-test-all-realms/src/javaRestTest/resources/ssl` | 10 | 45001.28 | 0.0% | 0.0% |
| `x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation` | 379 | 43522.64 | 14.58% | 68.6% |
| `x-pack/plugin/security/qa/tls-basic/src/javaRestTest/resources/ssl` | 8 | 35001.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/saml-rest-tests/src/javaRestTest/resources/ssl` | 7 | 30001.0 | 0.0% | 0.0% |
| `x-pack/qa/smoke-test-plugins-ssl/src/yamlRestTest/resources` | 6 | 30000.0 | 0.0% | 0.0% |
| `server/src/test/java/org/elasticsearch/index/mapper` | 173 | 27165.64 | 13.55% | 0.0% |
| `modules/data-streams/src/javaRestTest/resources/ssl` | 6 | 25001.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/service-account/src/javaRestTest/resources/ssl` | 6 | 25001.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.buildkite/hooks/pre-command` -> **100.0%** Exposure
- `.buildkite/scripts/branch-protection.sh` -> **100.0%** Exposure
- `.buildkite/scripts/cloud-deploy.sh` -> **100.0%** Exposure
- `.buildkite/scripts/cuvs-snapshot/configure.sh` -> **100.0%** Exposure
- `.buildkite/scripts/cuvs-snapshot/run-gradle.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.buildkite/hooks/pre-command` -> **100.0%** Exposure
- `.buildkite/scripts/branches.sh` -> **100.0%** Exposure
- `.buildkite/scripts/cuvs-snapshot/configure.sh` -> **100.0%** Exposure
- `.buildkite/scripts/dra-update-staging.sh` -> **100.0%** Exposure
- `.buildkite/scripts/dra-workflow.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/support/NoOpLogger.java` -> **0** Orphaned Functions | **371** Duplicates
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LogicalPlanOptimizerTests.java` -> **283** Orphaned Functions | **52** Duplicates
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/session/FieldNameUtilsTests.java` -> **234** Orphaned Functions | **7** Duplicates
- `modules/repository-s3/qa/insecure-credentials/src/test/java/org/elasticsearch/repositories/s3/AmazonS3Wrapper.java` -> **1** Orphaned Functions | **226** Duplicates
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/PhysicalPlanOptimizerTests.java` -> **151** Orphaned Functions | **49** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`libs/x-content/impl/src/test/java/org/elasticsearch/xcontent/support/filtering/FilterPathGeneratorFilteringTests.java`** -> AI Confidence: **99.48%**
2. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/VectorSearchIT.java`** -> AI Confidence: **99.48%**
3. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestIndicesAction.java`** -> AI Confidence: **99.48%**
4. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestNodesAction.java`** -> AI Confidence: **99.48%**
5. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestShardsAction.java`** -> AI Confidence: **99.48%**
6. **`server/src/test/java/org/elasticsearch/cluster/ClusterStateTests.java`** -> AI Confidence: **99.48%**
7. **`server/src/test/java/org/elasticsearch/cluster/metadata/ToAndFromJsonMetadataTests.java`** -> AI Confidence: **99.48%**
8. **`server/src/test/java/org/elasticsearch/common/RoundingTests.java`** -> AI Confidence: **99.48%**
9. **`server/src/test/java/org/elasticsearch/common/network/InetAddressesTests.java`** -> AI Confidence: **99.48%**
10. **`server/src/test/java/org/elasticsearch/common/time/DateFormattersTests.java`** -> AI Confidence: **99.48%**
11. **`server/src/test/java/org/elasticsearch/common/time/EpochTimeTests.java`** -> AI Confidence: **99.48%**
12. **`server/src/test/java/org/elasticsearch/http/HttpRouteStatsTests.java`** -> AI Confidence: **99.48%**
13. **`server/src/test/java/org/elasticsearch/index/mapper/IpPrefixAutomatonUtilTests.java`** -> AI Confidence: **99.48%**
14. **`server/src/test/java/org/elasticsearch/transport/TransportStatsTests.java`** -> AI Confidence: **99.48%**
15. **`test/framework/src/test/java/org/elasticsearch/test/AbstractQueryTestCaseTests.java`** -> AI Confidence: **99.48%**
16. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/connector/ConnectorFilteringTests.java`** -> AI Confidence: **99.48%**
17. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/connector/ConnectorTests.java`** -> AI Confidence: **99.48%**
18. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/connector/syncjob/ConnectorSyncJobTests.java`** -> AI Confidence: **99.48%**
19. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/MultiValueBlockTests.java`** -> AI Confidence: **99.48%**
20. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/AbstractCrossClusterQueryAllCombinationsIT.java`** -> AI Confidence: **99.48%**
21. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/analysis/VerifierTests.java`** -> AI Confidence: **99.48%**
22. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/OptimizerVerificationTests.java`** -> AI Confidence: **99.48%**
23. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/ParamsParserTests.java`** -> AI Confidence: **99.48%**
24. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/planner/QueryTranslatorTests.java`** -> AI Confidence: **99.48%**
25. **`x-pack/plugin/logsdb/src/internalClusterTest/java/org/elasticsearch/xpack/logsdb/LogsdbSortConfigIT.java`** -> AI Confidence: **99.48%**
26. **`x-pack/plugin/ml/qa/basic-multi-node/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/MlLearningToRankRescorerIT.java`** -> AI Confidence: **99.48%**
27. **`x-pack/plugin/ml/qa/ml-inference-service-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/ExampleModels.java`** -> AI Confidence: **99.48%**
28. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/DatafeedJobsRestIT.java`** -> AI Confidence: **99.48%**
29. **`x-pack/plugin/ml/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/InferencePipelineAggIT.java`** -> AI Confidence: **99.48%**
30. **`x-pack/plugin/ml/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/LearningToRankRescorerIT.java`** -> AI Confidence: **99.48%**
31. **`x-pack/plugin/otel-data/src/test/java/org/elasticsearch/xpack/oteldata/otlp/datapoint/ExponentialHistogramToExponentialHistogramConverterTests.java`** -> AI Confidence: **99.48%**
32. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityWithoutDlsAndFlsRestIT.java`** -> AI Confidence: **99.48%**
33. **`x-pack/plugin/security/qa/security-basic/src/javaRestTest/java/org/elasticsearch/xpack/security/ApiKeyAggsIT.java`** -> AI Confidence: **99.48%**
34. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/failurestore/FailureStoreSecurityRestIT.java`** -> AI Confidence: **99.48%**
35. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/IndexPrivilegeIntegTests.java`** -> AI Confidence: **99.48%**
36. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlSpMetadataBuilderTests.java`** -> AI Confidence: **99.48%**
37. **`x-pack/plugin/text-structure/src/test/java/org/elasticsearch/xpack/textstructure/structurefinder/DelimitedTextStructureFinderTests.java`** -> AI Confidence: **99.48%**
38. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformPivotRestIT.java`** -> AI Confidence: **99.48%**
39. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/RestrictedBuildApiService.java`** -> AI Confidence: **99.39%**
40. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransformer.java`** -> AI Confidence: **99.39%**
41. **`libs/grok/src/test/java/org/elasticsearch/grok/GrokTests.java`** -> AI Confidence: **99.39%**
42. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/LogsDataStreamIT.java`** -> AI Confidence: **99.39%**
43. **`plugins/analysis-phonetic/src/main/java/org/elasticsearch/plugin/analysis/phonetic/KoelnerPhonetik.java`** -> AI Confidence: **99.39%**
44. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/DownsampleIT.java`** -> AI Confidence: **99.39%**
45. **`server/src/main/java/org/elasticsearch/common/time/JavaDateMathParser.java`** -> AI Confidence: **99.39%**
46. **`server/src/test/java/org/elasticsearch/action/admin/cluster/stats/MappingStatsTests.java`** -> AI Confidence: **99.39%**
47. **`server/src/test/java/org/elasticsearch/index/mapper/IpFieldTypeTests.java`** -> AI Confidence: **99.39%**
48. **`server/src/test/java/org/elasticsearch/index/mapper/MapperServiceTests.java`** -> AI Confidence: **99.39%**
49. **`server/src/test/java/org/elasticsearch/index/mapper/TsidExtractingIdFieldMapperTests.java`** -> AI Confidence: **99.39%**
50. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/restspec/ClientYamlSuiteRestApiTests.java`** -> AI Confidence: **99.39%**
51. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/section/ClientYamlTestSectionTests.java`** -> AI Confidence: **99.39%**
52. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/section/SetupSectionTests.java`** -> AI Confidence: **99.39%**
53. **`x-pack/plugin/async-search/src/test/java/org/elasticsearch/xpack/search/AsyncSearchResponseTests.java`** -> AI Confidence: **99.39%**
54. **`x-pack/plugin/async-search/src/test/java/org/elasticsearch/xpack/search/AsyncStatusResponseTests.java`** -> AI Confidence: **99.39%**
55. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/HealthApiFeatureSetUsage.java`** -> AI Confidence: **99.39%**
56. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/apikey/GetApiKeyResponseTests.java`** -> AI Confidence: **99.39%**
57. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/role/RoleDescriptorRequestValidatorTests.java`** -> AI Confidence: **99.39%**
58. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/transform/transforms/pivot/DateHistogramGroupSourceTests.java`** -> AI Confidence: **99.39%**
59. **`x-pack/plugin/downsample/src/test/java/org/elasticsearch/xpack/downsample/TimeSeriesFieldsTests.java`** -> AI Confidence: **99.39%**
60. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InsensitiveEqualsTests.java`** -> AI Confidence: **99.39%**
61. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/GoogleVertexAiUnifiedStreamingProcessorTests.java`** -> AI Confidence: **99.39%**
62. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/OpenAiUnifiedStreamingProcessorTests.java`** -> AI Confidence: **99.39%**
63. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/TsdbIT.java`** -> AI Confidence: **99.39%**
64. **`x-pack/plugin/logsdb/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/LogsIndexModeEnabledRestTestIT.java`** -> AI Confidence: **99.39%**
65. **`x-pack/plugin/mapper-version/src/main/java/org/elasticsearch/xpack/versionfield/VersionFieldWildcardQuery.java`** -> AI Confidence: **99.39%**
66. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/InferenceIngestIT.java`** -> AI Confidence: **99.39%**
67. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/TextEmbeddingQueryIT.java`** -> AI Confidence: **99.39%**
68. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportEstimateModelMemoryAction.java`** -> AI Confidence: **99.39%**
69. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/cluster/ClusterStatsMonitoringDocTests.java`** -> AI Confidence: **99.39%**
70. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityWithDlsRestIT.java`** -> AI Confidence: **99.39%**
71. **`x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/FieldExtractorTestCase.java`** -> AI Confidence: **99.39%**
72. **`x-pack/plugin/sql/sql-action/src/test/java/org/elasticsearch/xpack/sql/action/SqlRequestParsersTests.java`** -> AI Confidence: **99.39%**
73. **`x-pack/plugin/sql/sql-client/src/test/java/org/elasticsearch/xpack/sql/client/UriUtilsTests.java`** -> AI Confidence: **99.39%**
74. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/analysis/analyzer/VerifierErrorMessagesTests.java`** -> AI Confidence: **99.39%**
75. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/TimestampFormatFinder.java`** -> AI Confidence: **99.39%**
76. **`x-pack/plugin/text-structure/src/test/java/org/elasticsearch/xpack/textstructure/structurefinder/GrokPatternCreatorTests.java`** -> AI Confidence: **99.39%**
77. **`x-pack/plugin/text-structure/src/test/java/org/elasticsearch/xpack/textstructure/structurefinder/TextStructureTestCase.java`** -> AI Confidence: **99.39%**
78. **`server/src/internalClusterTest/java/org/elasticsearch/reservedstate/service/ComponentTemplatesFileSettingsIT.java`** -> AI Confidence: **99.35%**
79. **`server/src/test/java/org/elasticsearch/action/admin/cluster/reroute/ClusterRerouteResponseTests.java`** -> AI Confidence: **99.35%**
80. **`x-pack/plugin/eql/qa/common/src/main/java/org/elasticsearch/test/eql/EqlRestTestCase.java`** -> AI Confidence: **99.35%**
81. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/DriverProfileTests.java`** -> AI Confidence: **99.35%**
82. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/AllSupportedFieldsTestCase.java`** -> AI Confidence: **99.35%**
83. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/AbstractRemoteClusterSecurityDlsAndFlsRestIT.java`** -> AI Confidence: **99.35%**
84. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformLatestRestIT.java`** -> AI Confidence: **99.35%**
85. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformPivotRestSpecialCasesIT.java`** -> AI Confidence: **99.35%**
86. **`x-pack/qa/rolling-upgrade/src/test/java/org/elasticsearch/upgrades/DataStreamsUpgradeIT.java`** -> AI Confidence: **99.35%**
87. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalGeoBoundsTests.java`** -> AI Confidence: **99.34%**
88. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/query/LuceneSourceOperatorStatusTests.java`** -> AI Confidence: **99.34%**
89. **`x-pack/test/idp-fixture/src/main/resources/oidc/Dockerfile`** -> AI Confidence: **99.34%**
90. **`x-pack/plugin/sql/connectors/tableau/package.sh`** -> AI Confidence: **99.32%**
91. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/section/TeardownSectionTests.java`** -> AI Confidence: **99.32%**
92. **`x-pack/dev-tools/smoke_test_xpack_rc.py`** -> AI Confidence: **99.31%**
93. **`x-pack/plugin/sql/connectors/tableau/tdvt/tdvt_run.py`** -> AI Confidence: **99.31%**
94. **`benchmarks/src/main/java/org/elasticsearch/benchmark/_nightly/esql/GroupedTopNBenchmark.java`** -> AI Confidence: **99.31%**
95. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/AggregatorBenchmark.java`** -> AI Confidence: **99.31%**
96. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockBenchmark.java`** -> AI Confidence: **99.31%**
97. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockKeepMaskBenchmark.java`** -> AI Confidence: **99.31%**
98. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockReadBenchmark.java`** -> AI Confidence: **99.31%**
99. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/MultivalueDedupeBenchmark.java`** -> AI Confidence: **99.31%**
100. **`benchmarks/src/main/java/org/elasticsearch/benchmark/esql/JsonExtractBenchmark.java`** -> AI Confidence: **99.31%**
101. **`benchmarks/src/main/java/org/elasticsearch/benchmark/index/mapper/KeywordFieldMapperBenchmark.java`** -> AI Confidence: **99.31%**
102. **`build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/HiddenFieldCheck.java`** -> AI Confidence: **99.31%**
103. **`build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/StringFormattingCheck.java`** -> AI Confidence: **99.31%**
104. **`build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/info/GitInfo.java`** -> AI Confidence: **99.31%**
105. **`build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/util/Util.java`** -> AI Confidence: **99.31%**
106. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/JdkDownloadPlugin.java`** -> AI Confidence: **99.31%**
107. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/RestTestsFromDocSnippetTask.java`** -> AI Confidence: **99.31%**
108. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/SnippetParser.java`** -> AI Confidence: **99.31%**
109. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/TransformLog4jConfigFilter.java`** -> AI Confidence: **99.31%**
110. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/RestResourcesPlugin.java`** -> AI Confidence: **99.31%**
111. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/transport/ValidateTransportVersionResourcesTask.java`** -> AI Confidence: **99.31%**
112. **`build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/checkstyle/SnipptLengthCheckTests.java`** -> AI Confidence: **99.31%**
113. **`build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/docker/DockerSupportServiceTests.java`** -> AI Confidence: **99.31%**
114. **`build-tools/reaper/src/main/java/org/elasticsearch/gradle/reaper/Reaper.java`** -> AI Confidence: **99.31%**
115. **`build-tools/src/main/java/org/elasticsearch/gradle/testclusters/RunTask.java`** -> AI Confidence: **99.31%**
116. **`build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClustersAware.java`** -> AI Confidence: **99.31%**
117. **`client/benchmark/src/main/java/org/elasticsearch/client/benchmark/AbstractBenchmark.java`** -> AI Confidence: **99.31%**
118. **`client/rest/src/main/java/org/elasticsearch/client/RequestLogger.java`** -> AI Confidence: **99.31%**
119. **`client/rest/src/test/java/org/elasticsearch/client/RestClientBuilderTests.java`** -> AI Confidence: **99.31%**
120. **`client/sniffer/src/main/java/org/elasticsearch/client/sniff/ElasticsearchNodesSniffer.java`** -> AI Confidence: **99.31%**
121. **`client/sniffer/src/test/java/org/elasticsearch/client/sniff/SnifferBuilderTests.java`** -> AI Confidence: **99.31%**
122. **`distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/JvmOptionsParser.java`** -> AI Confidence: **99.31%**
123. **`libs/core/src/main/java/org/elasticsearch/core/IOUtils.java`** -> AI Confidence: **99.31%**
124. **`libs/entitlement/asm-provider/src/main/java/org/elasticsearch/entitlement/instrumentation/impl/InstrumenterImpl.java`** -> AI Confidence: **99.31%**
125. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/ClassLoaderInstrumentation.java`** -> AI Confidence: **99.31%**
126. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileInstrumentation.java`** -> AI Confidence: **99.31%**
127. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileStoreInstrumentation.java`** -> AI Confidence: **99.31%**
128. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileSystemProviderInstrumentation.java`** -> AI Confidence: **99.31%**
129. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/L10nInstrumentation.java`** -> AI Confidence: **99.31%**
130. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/NetworkInstrumentation.java`** -> AI Confidence: **99.31%**
131. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/SecurityInstrumentation.java`** -> AI Confidence: **99.31%**
132. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/SystemInstrumentation.java`** -> AI Confidence: **99.31%**
133. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PathLookupImpl.java`** -> AI Confidence: **99.31%**
134. **`libs/exponential-histogram/src/test/java/org/elasticsearch/exponentialhistogram/ExponentialHistogramEqualityTests.java`** -> AI Confidence: **99.31%**
135. **`libs/exponential-histogram/src/test/java/org/elasticsearch/exponentialhistogram/ExponentialHistogramUtilsTests.java`** -> AI Confidence: **99.31%**
136. **`libs/exponential-histogram/src/test/java/org/elasticsearch/exponentialhistogram/ExponentialHistogramXContentTests.java`** -> AI Confidence: **99.31%**
137. **`libs/geo/src/main/java/org/elasticsearch/geometry/utils/WellKnownBinary.java`** -> AI Confidence: **99.31%**
138. **`libs/grok/src/main/java/org/elasticsearch/grok/Grok.java`** -> AI Confidence: **99.31%**
139. **`libs/lz4/src/main/java/org/elasticsearch/lz4/ESLZ4Decompressor.java`** -> AI Confidence: **99.31%**
140. **`libs/lz4/src/test/java/org/elasticsearch/lz4/ESLZ4Tests.java`** -> AI Confidence: **99.31%**
141. **`libs/native/src/test/java/org/elasticsearch/nativeaccess/ProcessLimitsTests.java`** -> AI Confidence: **99.31%**
142. **`libs/simdvec/src/main/java/org/elasticsearch/simdvec/ESVectorUtil.java`** -> AI Confidence: **99.31%**
143. **`libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/IndexInputUtils.java`** -> AI Confidence: **99.31%**
144. **`libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/Similarities.java`** -> AI Confidence: **99.31%**
145. **`libs/ssl-config/src/main/java/org/elasticsearch/common/ssl/CompositeTrustConfig.java`** -> AI Confidence: **99.31%**
146. **`libs/ssl-config/src/main/java/org/elasticsearch/common/ssl/PemUtils.java`** -> AI Confidence: **99.31%**
147. **`libs/ssl-config/src/main/java/org/elasticsearch/common/ssl/SslDiagnostics.java`** -> AI Confidence: **99.31%**
148. **`libs/ssl-config/src/test/java/org/elasticsearch/common/ssl/SslDiagnosticsTests.java`** -> AI Confidence: **99.31%**
149. **`libs/tdigest/src/main/java/org/elasticsearch/tdigest/AVLTreeDigest.java`** -> AI Confidence: **99.31%**
150. **`libs/tdigest/src/main/java/org/elasticsearch/tdigest/IntAVLTree.java`** -> AI Confidence: **99.31%**
151. **`libs/tdigest/src/test/java/org/elasticsearch/tdigest/MergingDigestTests.java`** -> AI Confidence: **99.31%**
152. **`libs/x-content/impl/src/test/java/org/elasticsearch/xcontent/provider/json/JsonXContentParserByteOffsetTests.java`** -> AI Confidence: **99.31%**
153. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/ObjectParser.java`** -> AI Confidence: **99.31%**
154. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/support/filtering/FilterPath.java`** -> AI Confidence: **99.31%**
155. **`libs/x-content/src/test/java/org/elasticsearch/xcontent/XContentParserTests.java`** -> AI Confidence: **99.31%**
156. **`modules/aggregations/src/internalClusterTest/java/org/elasticsearch/aggregations/bucket/TimeSeriesAggregationsIT.java`** -> AI Confidence: **99.31%**
157. **`modules/aggregations/src/internalClusterTest/java/org/elasticsearch/aggregations/pipeline/SerialDiffIT.java`** -> AI Confidence: **99.31%**
158. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/metric/ArrayValuesSourceParser.java`** -> AI Confidence: **99.31%**
159. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/pipeline/BucketSortPipelineAggregator.java`** -> AI Confidence: **99.31%**
160. **`modules/aggregations/src/test/java/org/elasticsearch/aggregations/bucket/histogram/AutoDateHistogramAggregatorTests.java`** -> AI Confidence: **99.31%**
161. **`modules/aggregations/src/test/java/org/elasticsearch/aggregations/bucket/histogram/InternalAutoDateHistogramTests.java`** -> AI Confidence: **99.31%**
162. **`modules/aggregations/src/test/java/org/elasticsearch/aggregations/pipeline/PipelineAggregationHelperTests.java`** -> AI Confidence: **99.31%**
163. **`modules/analysis-common/src/main/java/org/elasticsearch/analysis/common/CharGroupTokenizerFactory.java`** -> AI Confidence: **99.31%**
164. **`modules/analysis-common/src/test/java/org/elasticsearch/analysis/common/HighlighterWithAnalyzersTests.java`** -> AI Confidence: **99.31%**
165. **`modules/apm/src/main/java/org/elasticsearch/telemetry/apm/internal/metrics/OtelHelper.java`** -> AI Confidence: **99.31%**
166. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/DataStreamsRestIT.java`** -> AI Confidence: **99.31%**
167. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/EcsLogsDataStreamIT.java`** -> AI Confidence: **99.31%**
168. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/LogsDataStreamRestIT.java`** -> AI Confidence: **99.31%**
169. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/TsdbDataStreamRestIT.java`** -> AI Confidence: **99.31%**
170. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/lifecycle/DataStreamGlobalRetentionIT.java`** -> AI Confidence: **99.31%**
171. **`modules/data-streams/src/test/java/org/elasticsearch/datastreams/DataStreamIndexSettingsProviderTests.java`** -> AI Confidence: **99.31%**
172. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/CommunityIdProcessor.java`** -> AI Confidence: **99.31%**
173. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/CsvProcessor.java`** -> AI Confidence: **99.31%**
174. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/DotExpanderProcessor.java`** -> AI Confidence: **99.31%**
175. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/ForEachProcessor.java`** -> AI Confidence: **99.31%**
176. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/JsonProcessor.java`** -> AI Confidence: **99.31%**
177. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/KeyValueProcessor.java`** -> AI Confidence: **99.31%**
178. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/UserAgentProcessor.java`** -> AI Confidence: **99.31%**
179. **`modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/DateFormatTests.java`** -> AI Confidence: **99.31%**
180. **`modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/UriPartsProcessorTests.java`** -> AI Confidence: **99.31%**
181. **`modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/MaxmindIpDataLookups.java`** -> AI Confidence: **99.31%**
182. **`modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/GeoIpDownloaderTaskExecutorTests.java`** -> AI Confidence: **99.31%**
183. **`modules/ingest-otel/src/main/java/org/elasticsearch/ingest/otel/NormalizeForStreamProcessor.java`** -> AI Confidence: **99.31%**
184. **`modules/ingest-otel/src/test/java/org/elasticsearch/ingest/otel/OTelSemConvCrawler.java`** -> AI Confidence: **99.31%**
185. **`modules/kibana/src/javaRestTest/java/org/elasticsearch/kibana/KibanaSystemIndexIT.java`** -> AI Confidence: **99.31%**
186. **`modules/lang-mustache/src/internalClusterTest/java/org/elasticsearch/script/mustache/SearchUsageStatsIT.java`** -> AI Confidence: **99.31%**
187. **`modules/lang-mustache/src/test/java/org/elasticsearch/script/mustache/MustacheScriptEngineTests.java`** -> AI Confidence: **99.31%**
188. **`modules/lang-painless/spi/src/main/java/org/elasticsearch/painless/spi/WhitelistLoader.java`** -> AI Confidence: **99.31%**
189. **`modules/lang-painless/src/doc/java/org/elasticsearch/painless/ContextDocGenerator.java`** -> AI Confidence: **99.31%**
190. **`modules/lang-painless/src/doc/java/org/elasticsearch/painless/ContextGeneratorCommon.java`** -> AI Confidence: **99.31%**
191. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/DefBootstrap.java`** -> AI Confidence: **99.31%**
192. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/DefMath.java`** -> AI Confidence: **99.31%**
193. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/FunctionRef.java`** -> AI Confidence: **99.31%**
194. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/antlr/SuggestLexer.java`** -> AI Confidence: **99.31%**
195. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/lookup/PainlessLookup.java`** -> AI Confidence: **99.31%**
196. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/lookup/PainlessLookupBuilder.java`** -> AI Confidence: **99.31%**
197. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/phase/DefaultSemanticHeaderPhase.java`** -> AI Confidence: **99.31%**
198. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/phase/IRExpressionModifyingVisitor.java`** -> AI Confidence: **99.31%**
199. **`modules/lang-painless/src/test/java/org/elasticsearch/painless/BasicStatementTests.java`** -> AI Confidence: **99.31%**
200. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/mapper/LegacyGeoShapeFieldMapper.java`** -> AI Confidence: **99.31%**
201. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/parsers/GeoJsonParser.java`** -> AI Confidence: **99.31%**
202. **`modules/legacy-geo/src/test/java/org/elasticsearch/legacygeo/GeometryIOTests.java`** -> AI Confidence: **99.31%**
203. **`modules/legacy-geo/src/test/java/org/elasticsearch/legacygeo/test/ElasticsearchGeoAssertions.java`** -> AI Confidence: **99.31%**
204. **`modules/parent-join/src/internalClusterTest/java/org/elasticsearch/join/aggregations/ParentIT.java`** -> AI Confidence: **99.31%**
205. **`modules/reindex/src/main/java/org/elasticsearch/reindex/RethrottleRequest.java`** -> AI Confidence: **99.31%**
206. **`modules/reindex/src/main/java/org/elasticsearch/reindex/remote/RemoteRequestBuilders.java`** -> AI Confidence: **99.31%**
207. **`modules/repository-url/src/main/java/org/elasticsearch/common/blobstore/url/http/RetryingHttpInputStream.java`** -> AI Confidence: **99.31%**
208. **`modules/transport-netty4/src/main/java/org/elasticsearch/transport/netty4/Netty4WriteThrottlingHandler.java`** -> AI Confidence: **99.31%**
209. **`modules/user-agent/src/main/java/org/elasticsearch/useragent/DeviceTypeParser.java`** -> AI Confidence: **99.31%**
210. **`plugins/analysis-icu/src/main/java/org/elasticsearch/plugin/analysis/icu/IcuCollationTokenFilterFactory.java`** -> AI Confidence: **99.31%**
211. **`plugins/discovery-azure-classic/src/main/java/org/elasticsearch/discovery/azure/classic/AzureSeedHostsProvider.java`** -> AI Confidence: **99.31%**
212. **`plugins/discovery-ec2/src/main/java/org/elasticsearch/discovery/ec2/AwsEc2SeedHostsProvider.java`** -> AI Confidence: **99.31%**
213. **`plugins/repository-hdfs/src/test/java/org/elasticsearch/repositories/hdfs/HdfsTests.java`** -> AI Confidence: **99.31%**
214. **`qa/full-cluster-restart/src/javaRestTest/java/org/elasticsearch/upgrades/FullClusterRestartDownsampleIT.java`** -> AI Confidence: **99.31%**
215. **`qa/full-cluster-restart/src/javaRestTest/java/org/elasticsearch/upgrades/LogsIndexModeFullClusterRestartIT.java`** -> AI Confidence: **99.31%**
216. **`qa/full-cluster-restart/src/javaRestTest/java/org/elasticsearch/upgrades/QueryBuilderBWCIT.java`** -> AI Confidence: **99.31%**
217. **`qa/lucene-index-compatibility/src/javaRestTest/java/org/elasticsearch/lucene/FullClusterRestartLuceneIndexCompatibilityIT.java`** -> AI Confidence: **99.31%**
218. **`qa/mixed-cluster/src/test/java/org/elasticsearch/backwards/IndexingIT.java`** -> AI Confidence: **99.31%**
219. **`qa/packaging/src/test/java/org/elasticsearch/packaging/test/PackageUpgradeTests.java`** -> AI Confidence: **99.31%**
220. **`qa/packaging/src/test/java/org/elasticsearch/packaging/test/PasswordToolsTests.java`** -> AI Confidence: **99.31%**
221. **`qa/packaging/src/test/java/org/elasticsearch/packaging/util/docker/Docker.java`** -> AI Confidence: **99.31%**
222. **`qa/rolling-upgrade-legacy/src/test/java/org/elasticsearch/upgrades/RecoveryIT.java`** -> AI Confidence: **99.31%**
223. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/FailureStoreUpgradeIT.java`** -> AI Confidence: **99.31%**
224. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/IndexingIT.java`** -> AI Confidence: **99.31%**
225. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/SourceModeRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
226. **`qa/smoke-test-http/src/internalClusterTest/java/org/elasticsearch/http/BulkRestIT.java`** -> AI Confidence: **99.31%**
227. **`qa/vector/src/main/java/org/elasticsearch/test/knn/KnnIndexTester.java`** -> AI Confidence: **99.31%**
228. **`qa/vector/src/main/java/org/elasticsearch/test/knn/TestConfiguration.java`** -> AI Confidence: **99.31%**
229. **`server/src/internalClusterTest/java/org/elasticsearch/action/search/LookupRuntimeFieldIT.java`** -> AI Confidence: **99.31%**
230. **`server/src/internalClusterTest/java/org/elasticsearch/action/termvectors/GetTermVectorsIT.java`** -> AI Confidence: **99.31%**
231. **`server/src/internalClusterTest/java/org/elasticsearch/cluster/allocation/FilteringAllocationIT.java`** -> AI Confidence: **99.31%**
232. **`server/src/internalClusterTest/java/org/elasticsearch/cluster/settings/ClusterSettingsIT.java`** -> AI Confidence: **99.31%**
233. **`server/src/internalClusterTest/java/org/elasticsearch/index/FinalPipelineIT.java`** -> AI Confidence: **99.31%**
234. **`server/src/internalClusterTest/java/org/elasticsearch/index/seqno/GlobalCheckpointSyncIT.java`** -> AI Confidence: **99.31%**
235. **`server/src/internalClusterTest/java/org/elasticsearch/indices/mapping/UpdateMappingIntegrationIT.java`** -> AI Confidence: **99.31%**
236. **`server/src/internalClusterTest/java/org/elasticsearch/indices/memory/breaker/RandomExceptionCircuitBreakerIT.java`** -> AI Confidence: **99.31%**
237. **`server/src/internalClusterTest/java/org/elasticsearch/indices/stats/IndexStatsIT.java`** -> AI Confidence: **99.31%**
238. **`server/src/internalClusterTest/java/org/elasticsearch/recovery/RecoveryWhileUnderLoadIT.java`** -> AI Confidence: **99.31%**
239. **`server/src/internalClusterTest/java/org/elasticsearch/routing/AliasRoutingIT.java`** -> AI Confidence: **99.31%**
240. **`server/src/internalClusterTest/java/org/elasticsearch/routing/SimpleRoutingIT.java`** -> AI Confidence: **99.31%**
241. **`server/src/internalClusterTest/java/org/elasticsearch/search/aggregations/bucket/BooleanTermsIT.java`** -> AI Confidence: **99.31%**
242. **`server/src/internalClusterTest/java/org/elasticsearch/search/aggregations/bucket/DateRangeIT.java`** -> AI Confidence: **99.31%**
243. **`server/src/internalClusterTest/java/org/elasticsearch/search/aggregations/bucket/IpTermsIT.java`** -> AI Confidence: **99.31%**
244. **`server/src/internalClusterTest/java/org/elasticsearch/search/basic/SearchWithRandomExceptionsIT.java`** -> AI Confidence: **99.31%**
245. **`server/src/internalClusterTest/java/org/elasticsearch/search/basic/SearchWithRandomIOExceptionsIT.java`** -> AI Confidence: **99.31%**
246. **`server/src/internalClusterTest/java/org/elasticsearch/search/fetch/subphase/MatchedQueriesIT.java`** -> AI Confidence: **99.31%**
247. **`server/src/internalClusterTest/java/org/elasticsearch/search/nested/NestedSeqNoPruningIT.java`** -> AI Confidence: **99.31%**
248. **`server/src/internalClusterTest/java/org/elasticsearch/search/profile/query/QueryProfilerIT.java`** -> AI Confidence: **99.31%**
249. **`server/src/internalClusterTest/java/org/elasticsearch/search/scroll/DuelScrollIT.java`** -> AI Confidence: **99.31%**
250. **`server/src/internalClusterTest/java/org/elasticsearch/search/scroll/SearchScrollIT.java`** -> AI Confidence: **99.31%**
251. **`server/src/internalClusterTest/java/org/elasticsearch/versioning/SimpleVersioningIT.java`** -> AI Confidence: **99.31%**
252. **`server/src/main/java/org/elasticsearch/Build.java`** -> AI Confidence: **99.31%**
253. **`server/src/main/java/org/elasticsearch/ExceptionsHelper.java`** -> AI Confidence: **99.31%**
254. **`server/src/main/java/org/elasticsearch/TransportVersion.java`** -> AI Confidence: **99.31%**
255. **`server/src/main/java/org/elasticsearch/action/DocWriteRequest.java`** -> AI Confidence: **99.31%**
256. **`server/src/main/java/org/elasticsearch/action/admin/cluster/allocation/TransportClusterAllocationExplainAction.java`** -> AI Confidence: **99.31%**
257. **`server/src/main/java/org/elasticsearch/action/admin/cluster/health/TransportClusterHealthAction.java`** -> AI Confidence: **99.31%**
258. **`server/src/main/java/org/elasticsearch/action/admin/cluster/snapshots/get/FromSortValuePredicates.java`** -> AI Confidence: **99.31%**
259. **`server/src/main/java/org/elasticsearch/action/admin/cluster/stats/MappingStats.java`** -> AI Confidence: **99.31%**
260. **`server/src/main/java/org/elasticsearch/action/admin/cluster/stats/SearchUsageStats.java`** -> AI Confidence: **99.31%**
261. **`server/src/main/java/org/elasticsearch/action/admin/indices/get/GetIndexResponse.java`** -> AI Confidence: **99.31%**
262. **`server/src/main/java/org/elasticsearch/action/admin/indices/stats/CommonStats.java`** -> AI Confidence: **99.31%**
263. **`server/src/main/java/org/elasticsearch/action/bulk/BulkPrimaryExecutionContext.java`** -> AI Confidence: **99.31%**
264. **`server/src/main/java/org/elasticsearch/action/bulk/BulkShardRequest.java`** -> AI Confidence: **99.31%**
265. **`server/src/main/java/org/elasticsearch/action/get/MultiGetRequest.java`** -> AI Confidence: **99.31%**
266. **`server/src/main/java/org/elasticsearch/action/search/CCSSingleCoordinatorSearchProgressListener.java`** -> AI Confidence: **99.31%**
267. **`server/src/main/java/org/elasticsearch/action/search/ExpandSearchPhase.java`** -> AI Confidence: **99.31%**
268. **`server/src/main/java/org/elasticsearch/action/search/FetchLookupFieldsPhase.java`** -> AI Confidence: **99.31%**
269. **`server/src/main/java/org/elasticsearch/action/search/MultiSearchRequest.java`** -> AI Confidence: **99.31%**
270. **`server/src/main/java/org/elasticsearch/action/search/QueryPhaseResultConsumer.java`** -> AI Confidence: **99.31%**
271. **`server/src/main/java/org/elasticsearch/action/search/SearchPhaseController.java`** -> AI Confidence: **99.31%**
272. **`server/src/main/java/org/elasticsearch/action/search/SearchRequestAttributesExtractor.java`** -> AI Confidence: **99.31%**
273. **`server/src/main/java/org/elasticsearch/cluster/coordination/CoordinationState.java`** -> AI Confidence: **99.31%**
274. **`server/src/main/java/org/elasticsearch/cluster/coordination/Publication.java`** -> AI Confidence: **99.31%**
275. **`server/src/main/java/org/elasticsearch/cluster/metadata/AliasMetadata.java`** -> AI Confidence: **99.31%**
276. **`server/src/main/java/org/elasticsearch/cluster/metadata/AutoExpandReplicas.java`** -> AI Confidence: **99.31%**
277. **`server/src/main/java/org/elasticsearch/cluster/metadata/IndexAbstractionResolver.java`** -> AI Confidence: **99.31%**
278. **`server/src/main/java/org/elasticsearch/cluster/metadata/IndexNameExpressionResolver.java`** -> AI Confidence: **99.31%**
279. **`server/src/main/java/org/elasticsearch/cluster/metadata/LifecycleExecutionState.java`** -> AI Confidence: **99.31%**
280. **`server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java`** -> AI Confidence: **99.31%**
281. **`server/src/main/java/org/elasticsearch/cluster/metadata/ProjectMetadata.java`** -> AI Confidence: **99.31%**
282. **`server/src/main/java/org/elasticsearch/cluster/metadata/SystemIndexMetadataUpgradeService.java`** -> AI Confidence: **99.31%**
283. **`server/src/main/java/org/elasticsearch/cluster/node/DiscoveryNodeFilters.java`** -> AI Confidence: **99.31%**
284. **`server/src/main/java/org/elasticsearch/cluster/node/DiscoveryNodes.java`** -> AI Confidence: **99.31%**
285. **`server/src/main/java/org/elasticsearch/cluster/routing/ExpectedShardSizeEstimator.java`** -> AI Confidence: **99.31%**
286. **`server/src/main/java/org/elasticsearch/cluster/routing/IndexRoutingTable.java`** -> AI Confidence: **99.31%**
287. **`server/src/main/java/org/elasticsearch/cluster/routing/ShardRouting.java`** -> AI Confidence: **99.31%**
288. **`server/src/main/java/org/elasticsearch/cluster/routing/XContentParserTsidFunnel.java`** -> AI Confidence: **99.31%**
289. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/AllocationDecision.java`** -> AI Confidence: **99.31%**
290. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/DiskThresholdMonitor.java`** -> AI Confidence: **99.31%**
291. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/IndexMetadataUpdater.java`** -> AI Confidence: **99.31%**
292. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/MoveDecision.java`** -> AI Confidence: **99.31%**
293. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/allocator/BalancedShardsAllocator.java`** -> AI Confidence: **99.31%**
294. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/allocator/DesiredBalanceComputer.java`** -> AI Confidence: **99.31%**
295. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/ConcurrentRebalanceAllocationDecider.java`** -> AI Confidence: **99.31%**
296. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/DiskThresholdDecider.java`** -> AI Confidence: **99.31%**
297. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/EnableAllocationDecider.java`** -> AI Confidence: **99.31%**
298. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/MaxRetryAllocationDecider.java`** -> AI Confidence: **99.31%**
299. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/SameShardAllocationDecider.java`** -> AI Confidence: **99.31%**
300. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/SnapshotInProgressAllocationDecider.java`** -> AI Confidence: **99.31%**
301. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/ThrottlingAllocationDecider.java`** -> AI Confidence: **99.31%**
302. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/shards/StatefulShardsAvailabilityHealthIndicatorService.java`** -> AI Confidence: **99.31%**
303. **`server/src/main/java/org/elasticsearch/common/bytes/AbstractBytesReference.java`** -> AI Confidence: **99.31%**
304. **`server/src/main/java/org/elasticsearch/common/bytes/CompositeBytesReference.java`** -> AI Confidence: **99.31%**
305. **`server/src/main/java/org/elasticsearch/common/cache/Cache.java`** -> AI Confidence: **99.31%**
306. **`server/src/main/java/org/elasticsearch/common/geo/GenericPointParser.java`** -> AI Confidence: **99.31%**
307. **`server/src/main/java/org/elasticsearch/common/logging/HeaderWarning.java`** -> AI Confidence: **99.31%**
308. **`server/src/main/java/org/elasticsearch/common/logging/internal/LevelUtil.java`** -> AI Confidence: **99.31%**
309. **`server/src/main/java/org/elasticsearch/common/lucene/uid/PerThreadIDVersionAndSeqNoLookup.java`** -> AI Confidence: **99.31%**
310. **`server/src/main/java/org/elasticsearch/common/metrics/Counters.java`** -> AI Confidence: **99.31%**
311. **`server/src/main/java/org/elasticsearch/common/network/IfConfig.java`** -> AI Confidence: **99.31%**
312. **`server/src/main/java/org/elasticsearch/common/network/InetAddresses.java`** -> AI Confidence: **99.31%**
313. **`server/src/main/java/org/elasticsearch/common/network/NetworkService.java`** -> AI Confidence: **99.31%**
314. **`server/src/main/java/org/elasticsearch/common/path/PathTrie.java`** -> AI Confidence: **99.31%**
315. **`server/src/main/java/org/elasticsearch/common/regex/Regex.java`** -> AI Confidence: **99.31%**
316. **`server/src/main/java/org/elasticsearch/common/settings/AbstractScopedSettings.java`** -> AI Confidence: **99.31%**
317. **`server/src/main/java/org/elasticsearch/common/settings/ConsistentSettingsService.java`** -> AI Confidence: **99.31%**
318. **`server/src/main/java/org/elasticsearch/common/settings/SettingsModule.java`** -> AI Confidence: **99.31%**
319. **`server/src/main/java/org/elasticsearch/common/time/DateTime.java`** -> AI Confidence: **99.31%**
320. **`server/src/main/java/org/elasticsearch/common/time/Iso8601Parser.java`** -> AI Confidence: **99.31%**
321. **`server/src/main/java/org/elasticsearch/common/unit/ByteSizeValue.java`** -> AI Confidence: **99.31%**
322. **`server/src/main/java/org/elasticsearch/common/util/Maps.java`** -> AI Confidence: **99.31%**
323. **`server/src/main/java/org/elasticsearch/common/util/SetBackedScalingCuckooFilter.java`** -> AI Confidence: **99.31%**
324. **`server/src/main/java/org/elasticsearch/common/xcontent/support/XContentMapValues.java`** -> AI Confidence: **99.31%**
325. **`server/src/main/java/org/elasticsearch/gateway/AsyncShardFetch.java`** -> AI Confidence: **99.31%**
326. **`server/src/main/java/org/elasticsearch/gateway/PersistedClusterStateService.java`** -> AI Confidence: **99.31%**
327. **`server/src/main/java/org/elasticsearch/health/node/DiskHealthIndicatorService.java`** -> AI Confidence: **99.31%**
328. **`server/src/main/java/org/elasticsearch/health/stats/HealthApiStats.java`** -> AI Confidence: **99.31%**
329. **`server/src/main/java/org/elasticsearch/http/DefaultRestChannel.java`** -> AI Confidence: **99.31%**
330. **`server/src/main/java/org/elasticsearch/index/CompositeIndexEventListener.java`** -> AI Confidence: **99.31%**
331. **`server/src/main/java/org/elasticsearch/index/IndexService.java`** -> AI Confidence: **99.31%**
332. **`server/src/main/java/org/elasticsearch/index/IndexSortConfig.java`** -> AI Confidence: **99.31%**
333. **`server/src/main/java/org/elasticsearch/index/codec/postings/ES812PostingsReader.java`** -> AI Confidence: **99.31%**
334. **`server/src/main/java/org/elasticsearch/index/codec/postings/ES812PostingsWriter.java`** -> AI Confidence: **99.31%**
335. **`server/src/main/java/org/elasticsearch/index/codec/postings/PForUtil.java`** -> AI Confidence: **99.31%**
336. **`server/src/main/java/org/elasticsearch/index/codec/vectors/cluster/ClusteringFloatVectorValues.java`** -> AI Confidence: **99.31%**
337. **`server/src/main/java/org/elasticsearch/index/engine/Segment.java`** -> AI Confidence: **99.31%**
338. **`server/src/main/java/org/elasticsearch/index/mapper/DocumentMapper.java`** -> AI Confidence: **99.31%**
339. **`server/src/main/java/org/elasticsearch/index/mapper/DynamicTemplate.java`** -> AI Confidence: **99.31%**
340. **`server/src/main/java/org/elasticsearch/index/mapper/FieldTypeLookup.java`** -> AI Confidence: **99.31%**
341. **`server/src/main/java/org/elasticsearch/index/mapper/IpPrefixAutomatonUtil.java`** -> AI Confidence: **99.31%**
342. **`server/src/main/java/org/elasticsearch/index/mapper/ObjectMapper.java`** -> AI Confidence: **99.31%**
343. **`server/src/main/java/org/elasticsearch/index/mapper/RootObjectMapper.java`** -> AI Confidence: **99.31%**
344. **`server/src/main/java/org/elasticsearch/index/mapper/TextParams.java`** -> AI Confidence: **99.31%**
345. **`server/src/main/java/org/elasticsearch/index/mapper/TypeParsers.java`** -> AI Confidence: **99.31%**
346. **`server/src/main/java/org/elasticsearch/index/query/AbstractGeometryQueryBuilder.java`** -> AI Confidence: **99.31%**
347. **`server/src/main/java/org/elasticsearch/index/query/InnerHitBuilder.java`** -> AI Confidence: **99.31%**
348. **`server/src/main/java/org/elasticsearch/index/query/QueryStringQueryBuilder.java`** -> AI Confidence: **99.31%**
349. **`server/src/main/java/org/elasticsearch/index/query/support/AutoPrefilteringUtils.java`** -> AI Confidence: **99.31%**
350. **`server/src/main/java/org/elasticsearch/index/search/NestedHelper.java`** -> AI Confidence: **99.31%**
351. **`server/src/main/java/org/elasticsearch/index/search/QueryParserHelper.java`** -> AI Confidence: **99.31%**
352. **`server/src/main/java/org/elasticsearch/index/search/QueryStringQueryParser.java`** -> AI Confidence: **99.31%**
353. **`server/src/main/java/org/elasticsearch/index/shard/DenseVectorStats.java`** -> AI Confidence: **99.31%**
354. **`server/src/main/java/org/elasticsearch/index/shard/IndexLongFieldRange.java`** -> AI Confidence: **99.31%**
355. **`server/src/main/java/org/elasticsearch/index/shard/RefreshListeners.java`** -> AI Confidence: **99.31%**
356. **`server/src/main/java/org/elasticsearch/index/shard/SearchOperationListener.java`** -> AI Confidence: **99.31%**
357. **`server/src/main/java/org/elasticsearch/index/snapshots/blobstore/BlobStoreIndexShardSnapshot.java`** -> AI Confidence: **99.31%**
358. **`server/src/main/java/org/elasticsearch/index/snapshots/blobstore/BlobStoreIndexShardSnapshots.java`** -> AI Confidence: **99.31%**
359. **`server/src/main/java/org/elasticsearch/ingest/CompoundProcessor.java`** -> AI Confidence: **99.31%**
360. **`server/src/main/java/org/elasticsearch/ingest/IngestDocument.java`** -> AI Confidence: **99.31%**
361. **`server/src/main/java/org/elasticsearch/injection/PlanInterpreter.java`** -> AI Confidence: **99.31%**
362. **`server/src/main/java/org/elasticsearch/injection/guice/InjectorBuilder.java`** -> AI Confidence: **99.31%**
363. **`server/src/main/java/org/elasticsearch/injection/guice/TypeLiteral.java`** -> AI Confidence: **99.31%**
364. **`server/src/main/java/org/elasticsearch/injection/guice/internal/MoreTypes.java`** -> AI Confidence: **99.31%**
365. **`server/src/main/java/org/elasticsearch/lucene/search/vectorhighlight/CustomFieldQuery.java`** -> AI Confidence: **99.31%**
366. **`server/src/main/java/org/elasticsearch/lucene/spatial/CentroidCalculator.java`** -> AI Confidence: **99.31%**
367. **`server/src/main/java/org/elasticsearch/lucene/spatial/TriangleTreeWriter.java`** -> AI Confidence: **99.31%**
368. **`server/src/main/java/org/elasticsearch/lucene/util/automaton/MinimizationOperations.java`** -> AI Confidence: **99.31%**
369. **`server/src/main/java/org/elasticsearch/monitor/jvm/JvmGcMonitorService.java`** -> AI Confidence: **99.31%**
370. **`server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java`** -> AI Confidence: **99.31%**
371. **`server/src/main/java/org/elasticsearch/node/NodeService.java`** -> AI Confidence: **99.31%**
372. **`server/src/main/java/org/elasticsearch/node/ShutdownPrepareService.java`** -> AI Confidence: **99.31%**
373. **`server/src/main/java/org/elasticsearch/repositories/blobstore/FileRestoreContext.java`** -> AI Confidence: **99.31%**
374. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestAllocationAction.java`** -> AI Confidence: **99.31%**
375. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestCatCircuitBreakerAction.java`** -> AI Confidence: **99.31%**
376. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestCatRecoveryAction.java`** -> AI Confidence: **99.31%**
377. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestHealthAction.java`** -> AI Confidence: **99.31%**
378. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestSegmentsAction.java`** -> AI Confidence: **99.31%**
379. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestSnapshotAction.java`** -> AI Confidence: **99.31%**
380. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestTable.java`** -> AI Confidence: **99.31%**
381. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestTasksAction.java`** -> AI Confidence: **99.31%**
382. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestThreadPoolAction.java`** -> AI Confidence: **99.31%**
383. **`server/src/main/java/org/elasticsearch/script/Script.java`** -> AI Confidence: **99.31%**
384. **`server/src/main/java/org/elasticsearch/script/ScriptContextInfo.java`** -> AI Confidence: **99.31%**
385. **`server/src/main/java/org/elasticsearch/script/ScriptModule.java`** -> AI Confidence: **99.31%**
386. **`server/src/main/java/org/elasticsearch/script/ScriptService.java`** -> AI Confidence: **99.31%**
387. **`server/src/main/java/org/elasticsearch/script/ScriptTermStats.java`** -> AI Confidence: **99.31%**
388. **`server/src/main/java/org/elasticsearch/script/VectorScoreScriptUtils.java`** -> AI Confidence: **99.31%**
389. **`server/src/main/java/org/elasticsearch/script/field/WriteField.java`** -> AI Confidence: **99.31%**
390. **`server/src/main/java/org/elasticsearch/search/SearchModule.java`** -> AI Confidence: **99.31%**
391. **`server/src/main/java/org/elasticsearch/search/aggregations/AggregatorFactories.java`** -> AI Confidence: **99.31%**
392. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/CompositeValuesCollectorQueue.java`** -> AI Confidence: **99.31%**
393. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/CompositeValuesSourceParserHelper.java`** -> AI Confidence: **99.31%**
394. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/LongValuesSource.java`** -> AI Confidence: **99.31%**
395. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/TermsSortedDocsProducer.java`** -> AI Confidence: **99.31%**
396. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/range/BinaryRangeAggregator.java`** -> AI Confidence: **99.31%**
397. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/terms/AbstractInternalTerms.java`** -> AI Confidence: **99.31%**
398. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/terms/IncludeExclude.java`** -> AI Confidence: **99.31%**
399. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/TopHitsAggregationBuilder.java`** -> AI Confidence: **99.31%**
400. **`server/src/main/java/org/elasticsearch/search/aggregations/pipeline/BucketMetricsParser.java`** -> AI Confidence: **99.31%**
401. **`server/src/main/java/org/elasticsearch/search/aggregations/pipeline/BucketMetricsPipelineAggregator.java`** -> AI Confidence: **99.31%**
402. **`server/src/main/java/org/elasticsearch/search/aggregations/support/ValuesSourceRegistry.java`** -> AI Confidence: **99.31%**
403. **`server/src/main/java/org/elasticsearch/search/aggregations/support/values/ScriptDoubleValues.java`** -> AI Confidence: **99.31%**
404. **`server/src/main/java/org/elasticsearch/search/aggregations/support/values/ScriptLongValues.java`** -> AI Confidence: **99.31%**
405. **`server/src/main/java/org/elasticsearch/search/builder/SearchSourceBuilder.java`** -> AI Confidence: **99.31%**
406. **`server/src/main/java/org/elasticsearch/search/crossproject/CrossProjectIndexExpressionsRewriter.java`** -> AI Confidence: **99.31%**
407. **`server/src/main/java/org/elasticsearch/search/diversification/mmr/MMRResultDiversification.java`** -> AI Confidence: **99.31%**
408. **`server/src/main/java/org/elasticsearch/search/fetch/subphase/FetchSourceContext.java`** -> AI Confidence: **99.31%**
409. **`server/src/main/java/org/elasticsearch/search/fetch/subphase/UnmappedFieldFetcher.java`** -> AI Confidence: **99.31%**
410. **`server/src/main/java/org/elasticsearch/search/profile/AbstractProfileBreakdown.java`** -> AI Confidence: **99.31%**
411. **`server/src/main/java/org/elasticsearch/search/profile/query/ProfileCollectorManager.java`** -> AI Confidence: **99.31%**
412. **`server/src/main/java/org/elasticsearch/search/runtime/StringScriptFieldRangeQuery.java`** -> AI Confidence: **99.31%**
413. **`server/src/main/java/org/elasticsearch/search/searchafter/SearchAfterBuilder.java`** -> AI Confidence: **99.31%**
414. **`server/src/main/java/org/elasticsearch/search/sort/SortBuilder.java`** -> AI Confidence: **99.31%**
415. **`server/src/main/java/org/elasticsearch/search/sort/SortFieldValidation.java`** -> AI Confidence: **99.31%**
416. **`server/src/main/java/org/elasticsearch/search/suggest/phrase/PhraseSuggestionBuilder.java`** -> AI Confidence: **99.31%**
417. **`server/src/main/java/org/elasticsearch/search/vectors/VectorData.java`** -> AI Confidence: **99.31%**
418. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotInfo.java`** -> AI Confidence: **99.31%**
419. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotShutdownProgressTracker.java`** -> AI Confidence: **99.31%**
420. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotUtils.java`** -> AI Confidence: **99.31%**
421. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotsServiceUtils.java`** -> AI Confidence: **99.31%**
422. **`server/src/main/java/org/elasticsearch/transport/ClusterConnectionManager.java`** -> AI Confidence: **99.31%**
423. **`server/src/main/java/org/elasticsearch/transport/ForkingResponseHandlerRunnable.java`** -> AI Confidence: **99.31%**
424. **`server/src/main/java/org/elasticsearch/transport/InboundDecoder.java`** -> AI Confidence: **99.31%**
425. **`server/src/main/java/org/elasticsearch/transport/InboundHandler.java`** -> AI Confidence: **99.31%**
426. **`server/src/main/java/org/elasticsearch/transport/InboundPipeline.java`** -> AI Confidence: **99.31%**
427. **`server/src/main/java/org/elasticsearch/transport/Lz4TransportDecompressor.java`** -> AI Confidence: **99.31%**
428. **`server/src/main/java/org/elasticsearch/transport/RemoteClusterAware.java`** -> AI Confidence: **99.31%**
429. **`server/src/main/java/org/elasticsearch/transport/TransportLogger.java`** -> AI Confidence: **99.31%**
430. **`server/src/main/java/org/elasticsearch/watcher/FileWatcher.java`** -> AI Confidence: **99.31%**
431. **`server/src/test/java/org/elasticsearch/action/admin/cluster/snapshots/status/SnapshotStatsTests.java`** -> AI Confidence: **99.31%**
432. **`server/src/test/java/org/elasticsearch/action/admin/cluster/snapshots/status/SnapshotStatusTests.java`** -> AI Confidence: **99.31%**
433. **`server/src/test/java/org/elasticsearch/action/admin/cluster/stats/AnalysisStatsTests.java`** -> AI Confidence: **99.31%**
434. **`server/src/test/java/org/elasticsearch/action/admin/cluster/stats/CCSUsageTelemetryTests.java`** -> AI Confidence: **99.31%**
435. **`server/src/test/java/org/elasticsearch/action/admin/indices/rollover/RolloverConditionsTests.java`** -> AI Confidence: **99.31%**
436. **`server/src/test/java/org/elasticsearch/action/admin/indices/template/reservedstate/ReservedComposableIndexTemplateActionTests.java`** -> AI Confidence: **99.31%**
437. **`server/src/test/java/org/elasticsearch/action/bulk/BulkRequestParserTests.java`** -> AI Confidence: **99.31%**
438. **`server/src/test/java/org/elasticsearch/action/fieldcaps/FieldCapabilitiesFilterTests.java`** -> AI Confidence: **99.31%**
439. **`server/src/test/java/org/elasticsearch/action/fieldcaps/FieldCapabilitiesTests.java`** -> AI Confidence: **99.31%**
440. **`server/src/test/java/org/elasticsearch/action/fieldcaps/MergedFieldCapabilitiesResponseTests.java`** -> AI Confidence: **99.31%**
441. **`server/src/test/java/org/elasticsearch/action/get/MultiGetResponseTests.java`** -> AI Confidence: **99.31%**
442. **`server/src/test/java/org/elasticsearch/action/ingest/ReservedPipelineActionTests.java`** -> AI Confidence: **99.31%**
443. **`server/src/test/java/org/elasticsearch/action/ingest/SimulateIndexResponseTests.java`** -> AI Confidence: **99.31%**
444. **`server/src/test/java/org/elasticsearch/action/search/BottomSortValuesCollectorTests.java`** -> AI Confidence: **99.31%**
445. **`server/src/test/java/org/elasticsearch/action/search/SearchResponseMergerTests.java`** -> AI Confidence: **99.31%**
446. **`server/src/test/java/org/elasticsearch/action/search/SearchResponseTests.java`** -> AI Confidence: **99.31%**
447. **`server/src/test/java/org/elasticsearch/action/search/SearchShardsRequestTests.java`** -> AI Confidence: **99.31%**
448. **`server/src/test/java/org/elasticsearch/action/support/IndicesOptionsTests.java`** -> AI Confidence: **99.31%**
449. **`server/src/test/java/org/elasticsearch/action/support/replication/ReplicationResponseTests.java`** -> AI Confidence: **99.31%**
450. **`server/src/test/java/org/elasticsearch/action/update/UpdateResponseTests.java`** -> AI Confidence: **99.31%**
451. **`server/src/test/java/org/elasticsearch/cluster/coordination/MessagesTests.java`** -> AI Confidence: **99.31%**
452. **`server/src/test/java/org/elasticsearch/cluster/metadata/ComponentTemplateTests.java`** -> AI Confidence: **99.31%**
453. **`server/src/test/java/org/elasticsearch/cluster/metadata/ComposableIndexTemplateTests.java`** -> AI Confidence: **99.31%**
454. **`server/src/test/java/org/elasticsearch/cluster/metadata/IndexTemplateMetadataTests.java`** -> AI Confidence: **99.31%**
455. **`server/src/test/java/org/elasticsearch/cluster/metadata/MetadataTests.java`** -> AI Confidence: **99.31%**
456. **`server/src/test/java/org/elasticsearch/cluster/metadata/ProjectMetadataTests.java`** -> AI Confidence: **99.31%**
457. **`server/src/test/java/org/elasticsearch/cluster/metadata/SelectorResolverTests.java`** -> AI Confidence: **99.31%**
458. **`server/src/test/java/org/elasticsearch/cluster/routing/ShardRoutingTests.java`** -> AI Confidence: **99.31%**
459. **`server/src/test/java/org/elasticsearch/cluster/routing/XContentParserTsidFunnelTests.java`** -> AI Confidence: **99.31%**
460. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/AllocationDecisionTests.java`** -> AI Confidence: **99.31%**
461. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/ClusterRebalanceRoutingTests.java`** -> AI Confidence: **99.31%**
462. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/DataTierTests.java`** -> AI Confidence: **99.31%**
463. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/decider/EnableAllocationTests.java`** -> AI Confidence: **99.31%**
464. **`server/src/test/java/org/elasticsearch/common/cache/CacheTests.java`** -> AI Confidence: **99.31%**
465. **`server/src/test/java/org/elasticsearch/common/network/NetworkAddressTests.java`** -> AI Confidence: **99.31%**
466. **`server/src/test/java/org/elasticsearch/common/settings/SettingsUpdaterTests.java`** -> AI Confidence: **99.31%**
467. **`server/src/test/java/org/elasticsearch/common/time/Iso8601ParserTests.java`** -> AI Confidence: **99.31%**
468. **`server/src/test/java/org/elasticsearch/common/util/BitArrayTests.java`** -> AI Confidence: **99.31%**
469. **`server/src/test/java/org/elasticsearch/common/util/LongHashTests.java`** -> AI Confidence: **99.31%**
470. **`server/src/test/java/org/elasticsearch/common/util/MapsTests.java`** -> AI Confidence: **99.31%**
471. **`server/src/test/java/org/elasticsearch/common/util/iterable/IterablesTests.java`** -> AI Confidence: **99.31%**
472. **`server/src/test/java/org/elasticsearch/common/xcontent/BaseXContentTestCase.java`** -> AI Confidence: **99.31%**
473. **`server/src/test/java/org/elasticsearch/common/xcontent/support/XContentSourceFilterTests.java`** -> AI Confidence: **99.31%**
474. **`server/src/test/java/org/elasticsearch/index/codec/vectors/cluster/HierarchicalKMeansTests.java`** -> AI Confidence: **99.31%**
475. **`server/src/test/java/org/elasticsearch/index/engine/SearchBasedChangesSnapshotTests.java`** -> AI Confidence: **99.31%**
476. **`server/src/test/java/org/elasticsearch/index/fielddata/FloatDocValuesFieldTests.java`** -> AI Confidence: **99.31%**
477. **`server/src/test/java/org/elasticsearch/index/mapper/CompositeRuntimeFieldTests.java`** -> AI Confidence: **99.31%**
478. **`server/src/test/java/org/elasticsearch/index/mapper/DotExpandingXContentParserTests.java`** -> AI Confidence: **99.31%**
479. **`server/src/test/java/org/elasticsearch/index/mapper/DynamicMappingTests.java`** -> AI Confidence: **99.31%**
480. **`server/src/test/java/org/elasticsearch/index/mapper/DynamicTemplatesTests.java`** -> AI Confidence: **99.31%**
481. **`server/src/test/java/org/elasticsearch/index/mapper/FieldFilterMapperPluginTests.java`** -> AI Confidence: **99.31%**
482. **`server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java`** -> AI Confidence: **99.31%**
483. **`server/src/test/java/org/elasticsearch/index/mapper/IpFieldMapperTests.java`** -> AI Confidence: **99.31%**
484. **`server/src/test/java/org/elasticsearch/index/mapper/IpRangeFieldMapperTests.java`** -> AI Confidence: **99.31%**
485. **`server/src/test/java/org/elasticsearch/index/mapper/LookupRuntimeFieldTypeTests.java`** -> AI Confidence: **99.31%**
486. **`server/src/test/java/org/elasticsearch/index/mapper/ParametrizedMapperTests.java`** -> AI Confidence: **99.31%**
487. **`server/src/test/java/org/elasticsearch/index/mapper/RangeFieldTypeTests.java`** -> AI Confidence: **99.31%**
488. **`server/src/test/java/org/elasticsearch/index/mapper/blockloader/DateFieldBlockLoaderTests.java`** -> AI Confidence: **99.31%**
489. **`server/src/test/java/org/elasticsearch/index/mapper/flattened/FlattenedFieldSearchTests.java`** -> AI Confidence: **99.31%**
490. **`server/src/test/java/org/elasticsearch/index/query/DistanceFeatureQueryBuilderTests.java`** -> AI Confidence: **99.31%**
491. **`server/src/test/java/org/elasticsearch/index/query/FuzzyQueryBuilderTests.java`** -> AI Confidence: **99.31%**
492. **`server/src/test/java/org/elasticsearch/index/query/IntervalQueryBuilderTests.java`** -> AI Confidence: **99.31%**
493. **`server/src/test/java/org/elasticsearch/index/query/RangeQueryBuilderTests.java`** -> AI Confidence: **99.31%**
494. **`server/src/test/java/org/elasticsearch/index/query/SpanContainingQueryBuilderTests.java`** -> AI Confidence: **99.31%**
495. **`server/src/test/java/org/elasticsearch/index/query/SpanNearQueryBuilderTests.java`** -> AI Confidence: **99.31%**
496. **`server/src/test/java/org/elasticsearch/index/query/SpanNotQueryBuilderTests.java`** -> AI Confidence: **99.31%**
497. **`server/src/test/java/org/elasticsearch/index/query/SpanWithinQueryBuilderTests.java`** -> AI Confidence: **99.31%**
498. **`server/src/test/java/org/elasticsearch/index/query/support/AutoPrefilteringScopeTests.java`** -> AI Confidence: **99.31%**
499. **`server/src/test/java/org/elasticsearch/index/reindex/BulkByScrollTaskStatusWireSerializingTests.java`** -> AI Confidence: **99.31%**
500. **`server/src/test/java/org/elasticsearch/index/shard/DenseVectorStatsTests.java`** -> AI Confidence: **99.31%**
501. **`server/src/test/java/org/elasticsearch/index/shard/ShardGetServiceTests.java`** -> AI Confidence: **99.31%**
502. **`server/src/test/java/org/elasticsearch/indices/ShardLimitValidatorTests.java`** -> AI Confidence: **99.31%**
503. **`server/src/test/java/org/elasticsearch/inference/InferenceServiceConfigurationTests.java`** -> AI Confidence: **99.31%**
504. **`server/src/test/java/org/elasticsearch/inference/SettingsConfigurationTests.java`** -> AI Confidence: **99.31%**
505. **`server/src/test/java/org/elasticsearch/monitor/jvm/JvmGcMonitorServiceTests.java`** -> AI Confidence: **99.31%**
506. **`server/src/test/java/org/elasticsearch/persistent/BasePersistentTasksCustomMetadataTests.java`** -> AI Confidence: **99.31%**
507. **`server/src/test/java/org/elasticsearch/rest/RestUtilsTests.java`** -> AI Confidence: **99.31%**
508. **`server/src/test/java/org/elasticsearch/rest/action/RestActionsTests.java`** -> AI Confidence: **99.31%**
509. **`server/src/test/java/org/elasticsearch/rest/action/cat/RestCatRecoveryActionTests.java`** -> AI Confidence: **99.31%**
510. **`server/src/test/java/org/elasticsearch/rest/action/ingest/RestSimulateIngestActionTests.java`** -> AI Confidence: **99.31%**
511. **`server/src/test/java/org/elasticsearch/search/MultiValueModeTests.java`** -> AI Confidence: **99.31%**
512. **`server/src/test/java/org/elasticsearch/search/SearchHitsTests.java`** -> AI Confidence: **99.31%**
513. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/DateRangeTests.java`** -> AI Confidence: **99.31%**
514. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/GeoDistanceRangeTests.java`** -> AI Confidence: **99.31%**
515. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/HistogramTests.java`** -> AI Confidence: **99.31%**
516. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/RangeTests.java`** -> AI Confidence: **99.31%**
517. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/SignificantTermsTests.java`** -> AI Confidence: **99.31%**
518. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/TermsTests.java`** -> AI Confidence: **99.31%**
519. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/geogrid/GeoHashGridParserTests.java`** -> AI Confidence: **99.31%**
520. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/geogrid/GeoTileGridParserTests.java`** -> AI Confidence: **99.31%**
521. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/histogram/DateHistogramAggregatorTests.java`** -> AI Confidence: **99.31%**
522. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/histogram/DateRangeHistogramAggregatorTests.java`** -> AI Confidence: **99.31%**
523. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/prefix/IpPrefixAggregatorTests.java`** -> AI Confidence: **99.31%**
524. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/range/RangeAggregationBuilderTests.java`** -> AI Confidence: **99.31%**
525. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/DoubleTermsTests.java`** -> AI Confidence: **99.31%**
526. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/InternalRareTermsTestCase.java`** -> AI Confidence: **99.31%**
527. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/InternalSignificantTermsTestCase.java`** -> AI Confidence: **99.31%**
528. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/InternalTermsTestCase.java`** -> AI Confidence: **99.31%**
529. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/LongTermsTests.java`** -> AI Confidence: **99.31%**
530. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/SignificantLongTermsTests.java`** -> AI Confidence: **99.31%**
531. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/SignificantStringTermsTests.java`** -> AI Confidence: **99.31%**
532. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/StringTermsTests.java`** -> AI Confidence: **99.31%**
533. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/HistogramUnionStateTests.java`** -> AI Confidence: **99.31%**
534. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalExtendedStatsTests.java`** -> AI Confidence: **99.31%**
535. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalStatsTests.java`** -> AI Confidence: **99.31%**
536. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalValueCountTests.java`** -> AI Confidence: **99.31%**
537. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/MaxTests.java`** -> AI Confidence: **99.31%**
538. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/MemoryTrackingTDigestArraysTests.java`** -> AI Confidence: **99.31%**
539. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/MinTests.java`** -> AI Confidence: **99.31%**
540. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/SumTests.java`** -> AI Confidence: **99.31%**
541. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/TopHitsTests.java`** -> AI Confidence: **99.31%**
542. **`server/src/test/java/org/elasticsearch/search/aggregations/pipeline/InternalBucketMetricValueTests.java`** -> AI Confidence: **99.31%**
543. **`server/src/test/java/org/elasticsearch/search/crossproject/CrossProjectIndexExpressionsRewriterTests.java`** -> AI Confidence: **99.31%**
544. **`server/src/test/java/org/elasticsearch/search/fetch/subphase/FetchSourceContextTests.java`** -> AI Confidence: **99.31%**
545. **`server/src/test/java/org/elasticsearch/search/fetch/subphase/FieldFetcherTests.java`** -> AI Confidence: **99.31%**
546. **`server/src/test/java/org/elasticsearch/search/fetch/subphase/highlight/CustomUnifiedHighlighterTests.java`** -> AI Confidence: **99.31%**
547. **`server/src/test/java/org/elasticsearch/search/fetch/subphase/highlight/HighlightBuilderTests.java`** -> AI Confidence: **99.31%**
548. **`server/src/test/java/org/elasticsearch/search/lookup/LeafDocLookupTests.java`** -> AI Confidence: **99.31%**
549. **`server/src/test/java/org/elasticsearch/search/profile/ProfileResultTests.java`** -> AI Confidence: **99.31%**
550. **`server/src/test/java/org/elasticsearch/search/profile/query/CollectorResultTests.java`** -> AI Confidence: **99.31%**
551. **`server/src/test/java/org/elasticsearch/search/profile/query/RandomQueryGenerator.java`** -> AI Confidence: **99.31%**
552. **`server/src/test/java/org/elasticsearch/search/rescore/QueryRescorerBuilderTests.java`** -> AI Confidence: **99.31%**
553. **`server/src/test/java/org/elasticsearch/search/retriever/RetrieverBuilderErrorTests.java`** -> AI Confidence: **99.31%**
554. **`server/src/test/java/org/elasticsearch/search/sort/SortBuilderTests.java`** -> AI Confidence: **99.31%**
555. **`server/src/test/java/org/elasticsearch/search/suggest/completion/FuzzyOptionsTests.java`** -> AI Confidence: **99.31%**
556. **`server/src/test/java/org/elasticsearch/search/suggest/phrase/PhraseSuggestionBuilderTests.java`** -> AI Confidence: **99.31%**
557. **`server/src/test/java/org/elasticsearch/snapshots/ShardSnapshotStatusWireSerializationTests.java`** -> AI Confidence: **99.31%**
558. **`server/src/test/java/org/elasticsearch/snapshots/SnapshotInfoTestUtils.java`** -> AI Confidence: **99.31%**
559. **`server/src/test/java/org/elasticsearch/snapshots/SnapshotRequestsTests.java`** -> AI Confidence: **99.31%**
560. **`server/src/test/java/org/elasticsearch/snapshots/SnapshotsInProgressSerializationTests.java`** -> AI Confidence: **99.31%**
561. **`server/src/test/java/org/elasticsearch/threadpool/ScalingThreadPoolTests.java`** -> AI Confidence: **99.31%**
562. **`server/src/test/java/org/elasticsearch/transport/ConnectionProfileTests.java`** -> AI Confidence: **99.31%**
563. **`server/src/test/java/org/elasticsearch/transport/RemoteClusterPortSettingsTests.java`** -> AI Confidence: **99.31%**
564. **`server/src/test/java/org/elasticsearch/transport/TcpTransportTests.java`** -> AI Confidence: **99.31%**
565. **`server/src/test/java/org/elasticsearch/watcher/FileWatcherTests.java`** -> AI Confidence: **99.31%**
566. **`test/external-modules/apm-integration/src/javaRestTest/java/org/elasticsearch/test/apmintegration/RecordingApmServer.java`** -> AI Confidence: **99.31%**
567. **`test/external-modules/error-query/src/javaRestTest/java/org/elasticsearch/test/esql/EsqlPartialResultsIT.java`** -> AI Confidence: **99.31%**
568. **`test/external-modules/esql-heap-attack/src/javaRestTest/java/org/elasticsearch/xpack/esql/heap_attack/HeapAttackIT.java`** -> AI Confidence: **99.31%**
569. **`test/external-modules/esql-heap-attack/src/javaRestTest/java/org/elasticsearch/xpack/esql/heap_attack/HeapAttackLookupJoinIT.java`** -> AI Confidence: **99.31%**
570. **`test/external-modules/esql-heap-attack/src/javaRestTest/java/org/elasticsearch/xpack/esql/heap_attack/HeapAttackTestCase.java`** -> AI Confidence: **99.31%**
571. **`test/external-modules/multi-project/src/javaRestTest/java/org/elasticsearch/action/admin/cluster/node/stats/NodesStatsMultiProjectIT.java`** -> AI Confidence: **99.31%**
572. **`test/fixtures/azure-fixture/src/main/java/fixture/azure/AzureHttpHandler.java`** -> AI Confidence: **99.31%**
573. **`test/fixtures/gcs-fixture/src/main/java/fixture/gcs/GoogleCloudStorageHttpHandler.java`** -> AI Confidence: **99.31%**
574. **`test/fixtures/old-elasticsearch/src/main/java/oldes/OldElasticsearch.java`** -> AI Confidence: **99.31%**
575. **`test/fixtures/s3-fixture/src/main/java/fixture/s3/S3HttpHandler.java`** -> AI Confidence: **99.31%**
576. **`test/framework/src/main/java/org/elasticsearch/common/lucene/store/ESIndexInputTestCase.java`** -> AI Confidence: **99.31%**
577. **`test/framework/src/main/java/org/elasticsearch/index/alias/RandomAliasActionsGenerator.java`** -> AI Confidence: **99.31%**
578. **`test/framework/src/main/java/org/elasticsearch/index/mapper/KeywordFieldSyntheticSourceSupport.java`** -> AI Confidence: **99.31%**
579. **`test/framework/src/main/java/org/elasticsearch/search/RandomSearchRequestGenerator.java`** -> AI Confidence: **99.31%**
580. **`test/framework/src/main/java/org/elasticsearch/search/SearchResponseUtils.java`** -> AI Confidence: **99.31%**
581. **`test/framework/src/main/java/org/elasticsearch/search/geo/GeoBoundingBoxQueryBuilderTestCase.java`** -> AI Confidence: **99.31%**
582. **`test/framework/src/main/java/org/elasticsearch/search/geo/GeoDistanceQueryBuilderTestCase.java`** -> AI Confidence: **99.31%**
583. **`test/framework/src/main/java/org/elasticsearch/test/ListMatcher.java`** -> AI Confidence: **99.31%**
584. **`test/framework/src/main/java/org/elasticsearch/test/MapMatcher.java`** -> AI Confidence: **99.31%**
585. **`test/framework/src/main/java/org/elasticsearch/test/XContentTestUtils.java`** -> AI Confidence: **99.31%**
586. **`test/framework/src/test/java/org/elasticsearch/logsdb/datageneration/DataGenerationSnapshotTests.java`** -> AI Confidence: **99.31%**
587. **`test/framework/src/test/java/org/elasticsearch/test/ListMatcherTests.java`** -> AI Confidence: **99.31%**
588. **`test/framework/src/test/java/org/elasticsearch/test/MapMatcherTests.java`** -> AI Confidence: **99.31%**
589. **`test/test-clusters/src/main/java/org/elasticsearch/test/cluster/util/IOUtils.java`** -> AI Confidence: **99.31%**
590. **`test/test-clusters/src/main/java/org/elasticsearch/test/cluster/util/ProcessUtils.java`** -> AI Confidence: **99.31%**
591. **`test/yaml-rest-runner/src/main/java/org/elasticsearch/test/rest/yaml/restspec/ClientYamlSuiteRestApiParser.java`** -> AI Confidence: **99.31%**
592. **`test/yaml-rest-runner/src/main/java/org/elasticsearch/test/rest/yaml/section/PrerequisiteSection.java`** -> AI Confidence: **99.31%**
593. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/restspec/ClientYamlSuiteRestApiParserTests.java`** -> AI Confidence: **99.31%**
594. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/section/ClientYamlTestSuiteTests.java`** -> AI Confidence: **99.31%**
595. **`test/yaml-rest-runner/src/test/java/org/elasticsearch/test/rest/yaml/section/DoSectionTests.java`** -> AI Confidence: **99.31%**
596. **`x-pack/plugin/analytics/src/main/java/org/elasticsearch/xpack/analytics/AnalyticsPlugin.java`** -> AI Confidence: **99.31%**
597. **`x-pack/plugin/analytics/src/test/java/org/elasticsearch/xpack/analytics/mapper/ExponentialHistogramParserTests.java`** -> AI Confidence: **99.31%**
598. **`x-pack/plugin/analytics/src/test/java/org/elasticsearch/xpack/analytics/movingPercentiles/MovingPercentilesAbstractAggregatorTests.java`** -> AI Confidence: **99.31%**
599. **`x-pack/plugin/async-search/src/internalClusterTest/java/org/elasticsearch/xpack/search/AsyncSearchConcurrentStatusIT.java`** -> AI Confidence: **99.31%**
600. **`x-pack/plugin/async-search/src/internalClusterTest/java/org/elasticsearch/xpack/search/AsyncSearchErrorTraceIT.java`** -> AI Confidence: **99.31%**
601. **`x-pack/plugin/autoscaling/src/test/java/org/elasticsearch/xpack/autoscaling/storage/ReactiveStorageDeciderDecisionTests.java`** -> AI Confidence: **99.31%**
602. **`x-pack/plugin/blob-cache/src/main/java/org/elasticsearch/blobcache/common/ProgressListenableActionFuture.java`** -> AI Confidence: **99.31%**
603. **`x-pack/plugin/blob-cache/src/main/java/org/elasticsearch/blobcache/shared/SharedBytes.java`** -> AI Confidence: **99.31%**
604. **`x-pack/plugin/ccr/src/javaRestTest/java/org/elasticsearch/xpack/ccr/ChainIT.java`** -> AI Confidence: **99.31%**
605. **`x-pack/plugin/ccr/src/test/java/org/elasticsearch/xpack/monitoring/collector/ccr/AutoFollowStatsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
606. **`x-pack/plugin/ccr/src/test/java/org/elasticsearch/xpack/monitoring/collector/ccr/FollowStatsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
607. **`x-pack/plugin/core/src/javaRestTest/java/org/elasticsearch/xpack/core/DataStreamRestIT.java`** -> AI Confidence: **99.31%**
608. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/common/IteratingActionListener.java`** -> AI Confidence: **99.31%**
609. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java`** -> AI Confidence: **99.31%**
610. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ilm/TimeseriesLifecycleType.java`** -> AI Confidence: **99.31%**
611. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/datafeed/DatafeedConfig.java`** -> AI Confidence: **99.31%**
612. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/datafeed/DatafeedJobValidator.java`** -> AI Confidence: **99.31%**
613. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/datafeed/DatafeedUpdate.java`** -> AI Confidence: **99.31%**
614. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/dataframe/evaluation/Evaluation.java`** -> AI Confidence: **99.31%**
615. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/config/Job.java`** -> AI Confidence: **99.31%**
616. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/config/JobUpdate.java`** -> AI Confidence: **99.31%**
617. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/stats/StatsAccumulator.java`** -> AI Confidence: **99.31%**
618. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/utils/InferenceProcessorInfoExtractor.java`** -> AI Confidence: **99.31%**
619. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/scheduler/Cron.java`** -> AI Confidence: **99.31%**
620. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/apikey/CrossClusterApiKeyRoleDescriptorBuilder.java`** -> AI Confidence: **99.31%**
621. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/role/RoleDescriptorRequestValidator.java`** -> AI Confidence: **99.31%**
622. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/user/PutUserRequestBuilder.java`** -> AI Confidence: **99.31%**
623. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authc/Subject.java`** -> AI Confidence: **99.31%**
624. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authz/permission/IndicesPermission.java`** -> AI Confidence: **99.31%**
625. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authz/privilege/IndexPrivilege.java`** -> AI Confidence: **99.31%**
626. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authz/privilege/SystemPrivilege.java`** -> AI Confidence: **99.31%**
627. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/textstructure/structurefinder/TextStructure.java`** -> AI Confidence: **99.31%**
628. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/transform/transforms/SettingsConfig.java`** -> AI Confidence: **99.31%**
629. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/watcher/transform/TransformRegistry.java`** -> AI Confidence: **99.31%**
630. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/watcher/watch/WatchStatus.java`** -> AI Confidence: **99.31%**
631. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/datastreams/DataStreamFeatureSetUsageTests.java`** -> AI Confidence: **99.31%**
632. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ilm/IndexLifecycleExplainResponseTests.java`** -> AI Confidence: **99.31%**
633. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ilm/LifecycleExecutionStateTests.java`** -> AI Confidence: **99.31%**
634. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ilm/RolloverActionTests.java`** -> AI Confidence: **99.31%**
635. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/inference/action/UnifiedCompletionRequestTests.java`** -> AI Confidence: **99.31%**
636. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/inference/results/StreamingUnifiedChatCompletionResultsTests.java`** -> AI Confidence: **99.31%**
637. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/TrainedModelDefinitionTests.java`** -> AI Confidence: **99.31%**
638. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/assignment/AssignmentStatsTests.java`** -> AI Confidence: **99.31%**
639. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/results/InferenceResultsTestCase.java`** -> AI Confidence: **99.31%**
640. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/ModelPackageConfigTests.java`** -> AI Confidence: **99.31%**
641. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/inference/InferenceDefinitionTests.java`** -> AI Confidence: **99.31%**
642. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/tree/TreeNodeTests.java`** -> AI Confidence: **99.31%**
643. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/utils/ExponentialAverageCalculationContextTests.java`** -> AI Confidence: **99.31%**
644. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/scheduler/CronTimezoneTests.java`** -> AI Confidence: **99.31%**
645. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/apikey/CreateApiKeyRequestBuilderTests.java`** -> AI Confidence: **99.31%**
646. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/apikey/CrossClusterApiKeyRoleDescriptorBuilderTests.java`** -> AI Confidence: **99.31%**
647. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/profile/GetProfilesResponseTests.java`** -> AI Confidence: **99.31%**
648. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/user/GetUsersResponseTests.java`** -> AI Confidence: **99.31%**
649. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authc/AuthenticationTestHelper.java`** -> AI Confidence: **99.31%**
650. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authc/AuthenticationTests.java`** -> AI Confidence: **99.31%**
651. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/RoleDescriptorTests.java`** -> AI Confidence: **99.31%**
652. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/privilege/ApplicationPrivilegeTests.java`** -> AI Confidence: **99.31%**
653. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/privilege/IndexPrivilegeTests.java`** -> AI Confidence: **99.31%**
654. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/privilege/PrivilegeTests.java`** -> AI Confidence: **99.31%**
655. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/support/AutomatonPatternsTests.java`** -> AI Confidence: **99.31%**
656. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/slm/SnapshotLifecyclePolicyItemTests.java`** -> AI Confidence: **99.31%**
657. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/slm/SnapshotLifecyclePolicyMetadataTests.java`** -> AI Confidence: **99.31%**
658. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/textstructure/action/FindTextStructureActionRequestTests.java`** -> AI Confidence: **99.31%**
659. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/transform/action/GetCheckpointActionRequestTests.java`** -> AI Confidence: **99.31%**
660. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/transform/transforms/TransformConfigTests.java`** -> AI Confidence: **99.31%**
661. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/transform/transforms/pivot/PivotConfigTests.java`** -> AI Confidence: **99.31%**
662. **`x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/IndexDeprecationChecker.java`** -> AI Confidence: **99.31%**
663. **`x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/NodeDeprecationChecks.java`** -> AI Confidence: **99.31%**
664. **`x-pack/plugin/downsample/src/internalClusterTest/java/org/elasticsearch/xpack/downsample/DownsampleIT.java`** -> AI Confidence: **99.31%**
665. **`x-pack/plugin/downsample/src/internalClusterTest/java/org/elasticsearch/xpack/downsample/DownsampleRateIT.java`** -> AI Confidence: **99.31%**
666. **`x-pack/plugin/downsample/src/internalClusterTest/java/org/elasticsearch/xpack/downsample/DownsampleTransportFailureIT.java`** -> AI Confidence: **99.31%**
667. **`x-pack/plugin/downsample/src/main/java/org/elasticsearch/xpack/downsample/AggregateMetricDoubleFieldDownsampler.java`** -> AI Confidence: **99.31%**
668. **`x-pack/plugin/enrich/src/javaRestTest/java/org/elasticsearch/test/enrich/CommonEnrichRestTestCase.java`** -> AI Confidence: **99.31%**
669. **`x-pack/plugin/enrich/src/main/java/org/elasticsearch/xpack/enrich/EnrichPolicyRunner.java`** -> AI Confidence: **99.31%**
670. **`x-pack/plugin/enrich/src/test/java/org/elasticsearch/xpack/enrich/EnrichPolicyRunnerTests.java`** -> AI Confidence: **99.31%**
671. **`x-pack/plugin/enrich/src/test/java/org/elasticsearch/xpack/monitoring/collector/enrich/EnrichCoordinatorDocTests.java`** -> AI Confidence: **99.31%**
672. **`x-pack/plugin/enrich/src/test/java/org/elasticsearch/xpack/monitoring/collector/enrich/ExecutingPolicyDocTests.java`** -> AI Confidence: **99.31%**
673. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/connector/ConnectorConfigurationTests.java`** -> AI Confidence: **99.31%**
674. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/rules/QueryRuleTests.java`** -> AI Confidence: **99.31%**
675. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/rules/QueryRulesetTests.java`** -> AI Confidence: **99.31%**
676. **`x-pack/plugin/eql/qa/common/src/main/java/org/elasticsearch/test/eql/BaseEqlSpecTestCase.java`** -> AI Confidence: **99.31%**
677. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/analysis/AnalysisUtils.java`** -> AI Confidence: **99.31%**
678. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/analysis/Verifier.java`** -> AI Confidence: **99.31%**
679. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/execution/search/SourceGenerator.java`** -> AI Confidence: **99.31%**
680. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/execution/sequence/TumblingWindow.java`** -> AI Confidence: **99.31%**
681. **`x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/action/EqlRequestParserTests.java`** -> AI Confidence: **99.31%**
682. **`x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/analysis/VerifierTests.java`** -> AI Confidence: **99.31%**
683. **`x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/expression/function/scalar/string/BetweenFunctionPipeTests.java`** -> AI Confidence: **99.31%**
684. **`x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/expression/function/scalar/string/IndexOfFunctionPipeTests.java`** -> AI Confidence: **99.31%**
685. **`x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/expression/function/scalar/string/SubstringFunctionPipeTests.java`** -> AI Confidence: **99.31%**
686. **`x-pack/plugin/esql-core/src/main/java/org/elasticsearch/xpack/esql/core/util/StringUtils.java`** -> AI Confidence: **99.31%**
687. **`x-pack/plugin/esql-datasource-azure/src/main/java/org/elasticsearch/xpack/esql/datasource/azure/AzureStorageProvider.java`** -> AI Confidence: **99.31%**
688. **`x-pack/plugin/esql-datasource-csv/src/main/java/org/elasticsearch/xpack/esql/datasource/csv/CsvFixtureParser.java`** -> AI Confidence: **99.31%**
689. **`x-pack/plugin/esql-datasource-gcs/src/main/java/org/elasticsearch/xpack/esql/datasource/gcs/GcsStorageObject.java`** -> AI Confidence: **99.31%**
690. **`x-pack/plugin/esql-datasource-grpc/src/test/java/org/elasticsearch/xpack/esql/datasource/grpc/AsyncConnectorFactoryFlightTests.java`** -> AI Confidence: **99.31%**
691. **`x-pack/plugin/esql-datasource-grpc/src/test/java/org/elasticsearch/xpack/esql/datasource/grpc/FlightConnectorFactoryTests.java`** -> AI Confidence: **99.31%**
692. **`x-pack/plugin/esql-datasource-iceberg/src/main/java/org/elasticsearch/xpack/esql/datasource/iceberg/IcebergCatalogAdapter.java`** -> AI Confidence: **99.31%**
693. **`x-pack/plugin/esql-datasource-ndjson/src/main/java/org/elasticsearch/xpack/esql/datasource/ndjson/NdJsonPageDecoder.java`** -> AI Confidence: **99.31%**
694. **`x-pack/plugin/esql-datasource-ndjson/src/test/java/org/elasticsearch/xpack/esql/datasource/ndjson/NdJsonSchemaInferrerTests.java`** -> AI Confidence: **99.31%**
695. **`x-pack/plugin/esql-datasource-orc/src/main/java/org/elasticsearch/xpack/esql/datasource/orc/OrcFormatReader.java`** -> AI Confidence: **99.31%**
696. **`x-pack/plugin/esql-datasource-orc/src/main/java/org/elasticsearch/xpack/esql/datasource/orc/OrcPushdownFilters.java`** -> AI Confidence: **99.31%**
697. **`x-pack/plugin/esql-datasource-parquet/src/main/java/org/elasticsearch/xpack/esql/datasource/parquet/ParquetFilterPushdownSupport.java`** -> AI Confidence: **99.31%**
698. **`x-pack/plugin/esql-datasource-parquet/src/main/java/org/elasticsearch/xpack/esql/datasource/parquet/ParquetFormatReader.java`** -> AI Confidence: **99.31%**
699. **`x-pack/plugin/esql-datasource-s3/src/main/java/org/elasticsearch/xpack/esql/datasource/s3/S3StorageObject.java`** -> AI Confidence: **99.31%**
700. **`x-pack/plugin/esql/compute/gen/src/main/java/org/elasticsearch/compute/gen/AggregatorImplementer.java`** -> AI Confidence: **99.31%**
701. **`x-pack/plugin/esql/compute/gen/src/main/java/org/elasticsearch/compute/gen/GroupingAggregatorImplementer.java`** -> AI Confidence: **99.31%**
702. **`x-pack/plugin/esql/compute/gen/src/main/java/org/elasticsearch/compute/gen/MvEvaluatorImplementer.java`** -> AI Confidence: **99.31%**
703. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstBooleanByIntAggregator.java`** -> AI Confidence: **99.31%**
704. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstBooleanByLongAggregator.java`** -> AI Confidence: **99.31%**
705. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstBytesRefByIntAggregator.java`** -> AI Confidence: **99.31%**
706. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstBytesRefByLongAggregator.java`** -> AI Confidence: **99.31%**
707. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstDoubleByIntAggregator.java`** -> AI Confidence: **99.31%**
708. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstDoubleByLongAggregator.java`** -> AI Confidence: **99.31%**
709. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstFloatByIntAggregator.java`** -> AI Confidence: **99.31%**
710. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstFloatByLongAggregator.java`** -> AI Confidence: **99.31%**
711. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstIntByIntAggregator.java`** -> AI Confidence: **99.31%**
712. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstIntByLongAggregator.java`** -> AI Confidence: **99.31%**
713. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstLongByIntAggregator.java`** -> AI Confidence: **99.31%**
714. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllFirstLongByLongAggregator.java`** -> AI Confidence: **99.31%**
715. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastBooleanByIntAggregator.java`** -> AI Confidence: **99.31%**
716. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastBooleanByLongAggregator.java`** -> AI Confidence: **99.31%**
717. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastBytesRefByIntAggregator.java`** -> AI Confidence: **99.31%**
718. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastBytesRefByLongAggregator.java`** -> AI Confidence: **99.31%**
719. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastDoubleByIntAggregator.java`** -> AI Confidence: **99.31%**
720. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastDoubleByLongAggregator.java`** -> AI Confidence: **99.31%**
721. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastFloatByIntAggregator.java`** -> AI Confidence: **99.31%**
722. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastFloatByLongAggregator.java`** -> AI Confidence: **99.31%**
723. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastIntByIntAggregator.java`** -> AI Confidence: **99.31%**
724. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastIntByLongAggregator.java`** -> AI Confidence: **99.31%**
725. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastLongByIntAggregator.java`** -> AI Confidence: **99.31%**
726. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AllLastLongByLongAggregator.java`** -> AI Confidence: **99.31%**
727. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AnyBooleanAggregator.java`** -> AI Confidence: **99.31%**
728. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/RateDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.31%**
729. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/RateIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.31%**
730. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/RateLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.31%**
731. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/operator/mvdedupe/MultivalueDedupeBytesRef.java`** -> AI Confidence: **99.31%**
732. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/operator/mvdedupe/MultivalueDedupeDouble.java`** -> AI Confidence: **99.31%**
733. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/operator/mvdedupe/MultivalueDedupeInt.java`** -> AI Confidence: **99.31%**
734. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/operator/mvdedupe/MultivalueDedupeLong.java`** -> AI Confidence: **99.31%**
735. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/xpack/compute/operator/lookup/EnrichResultBuilderForBoolean.java`** -> AI Confidence: **99.31%**
736. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/xpack/compute/operator/lookup/EnrichResultBuilderForBytesRef.java`** -> AI Confidence: **99.31%**
737. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/xpack/compute/operator/lookup/EnrichResultBuilderForDouble.java`** -> AI Confidence: **99.31%**
738. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/xpack/compute/operator/lookup/EnrichResultBuilderForFloat.java`** -> AI Confidence: **99.31%**
739. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/xpack/compute/operator/lookup/EnrichResultBuilderForInt.java`** -> AI Confidence: **99.31%**
740. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/xpack/compute/operator/lookup/EnrichResultBuilderForLong.java`** -> AI Confidence: **99.31%**
741. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstDoubleByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
742. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstFloatByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
743. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstIntByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
744. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstLongByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
745. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastDoubleByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
746. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastFloatByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
747. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastIntByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
748. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastLongByTimestampAggregatorFunction.java`** -> AI Confidence: **99.31%**
749. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.31%**
750. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/SumDenseVectorGroupingState.java`** -> AI Confidence: **99.31%**
751. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/ValuesBytesRefAggregators.java`** -> AI Confidence: **99.31%**
752. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/AddPage.java`** -> AI Confidence: **99.31%**
753. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/AggregateMetricDoubleBlockBuilder.java`** -> AI Confidence: **99.31%**
754. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/BlockUtils.java`** -> AI Confidence: **99.31%**
755. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/ElementType.java`** -> AI Confidence: **99.31%**
756. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/TDigestArrayBlock.java`** -> AI Confidence: **99.31%**
757. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/arrow/AbstractArrowBufBlock.java`** -> AI Confidence: **99.31%**
758. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/arrow/BooleanArrowBufBlock.java`** -> AI Confidence: **99.31%**
759. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/arrow/BytesRefArrowBufBlock.java`** -> AI Confidence: **99.31%**
760. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/sort/BooleanBucketedSort.java`** -> AI Confidence: **99.31%**
761. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/FailureCollector.java`** -> AI Confidence: **99.31%**
762. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/StringExtractOperator.java`** -> AI Confidence: **99.31%**
763. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/exchange/BatchSortedExchangeSource.java`** -> AI Confidence: **99.31%**
764. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/exchange/BidirectionalBatchExchangeServer.java`** -> AI Confidence: **99.31%**
765. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/lookup/RightChunkedLeftJoin.java`** -> AI Confidence: **99.31%**
766. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/mvdedupe/IntLongBlockAdd.java`** -> AI Confidence: **99.31%**
767. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/mvdedupe/TopNMultivalueDedupeLong.java`** -> AI Confidence: **99.31%**
768. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/aggregation/ArrayStateTests.java`** -> AI Confidence: **99.31%**
769. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/aggregation/blockhash/TopNBlockHashTests.java`** -> AI Confidence: **99.31%**
770. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/BasicBlockTests.java`** -> AI Confidence: **99.31%**
771. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/BlockMultiValuedTests.java`** -> AI Confidence: **99.31%**
772. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/ExponentialHistogramBlockTests.java`** -> AI Confidence: **99.31%**
773. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/VectorBuilderTests.java`** -> AI Confidence: **99.31%**
774. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/VectorFixedBuilderTests.java`** -> AI Confidence: **99.31%**
775. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/read/ValueSourceReaderTypeConversionTests.java`** -> AI Confidence: **99.31%**
776. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/read/ValuesSourceReaderOperatorStatusTests.java`** -> AI Confidence: **99.31%**
777. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/DriverStatusTests.java`** -> AI Confidence: **99.31%**
778. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/MetricsInfoOperatorTests.java`** -> AI Confidence: **99.31%**
779. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/TsInfoOperatorTests.java`** -> AI Confidence: **99.31%**
780. **`x-pack/plugin/esql/compute/test/src/main/java/org/elasticsearch/compute/test/BlockTestUtils.java`** -> AI Confidence: **99.31%**
781. **`x-pack/plugin/esql/compute/test/src/main/java/org/elasticsearch/compute/test/CannedSourceOperator.java`** -> AI Confidence: **99.31%**
782. **`x-pack/plugin/esql/compute/test/src/main/java/org/elasticsearch/compute/test/NullInsertingSourceOperator.java`** -> AI Confidence: **99.31%**
783. **`x-pack/plugin/esql/compute/test/src/main/java/org/elasticsearch/compute/test/RandomBlock.java`** -> AI Confidence: **99.31%**
784. **`x-pack/plugin/esql/compute/test/src/main/java/org/elasticsearch/compute/test/TDigestTestUtils.java`** -> AI Confidence: **99.31%**
785. **`x-pack/plugin/esql/qa/server/multi-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/multi_node/ExternalDistributedResilienceIT.java`** -> AI Confidence: **99.31%**
786. **`x-pack/plugin/esql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/single_node/ArrowFormatIT.java`** -> AI Confidence: **99.31%**
787. **`x-pack/plugin/esql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/single_node/EsqlPartitioningIT.java`** -> AI Confidence: **99.31%**
788. **`x-pack/plugin/esql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/single_node/PushQueriesIT.java`** -> AI Confidence: **99.31%**
789. **`x-pack/plugin/esql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/single_node/RestEsqlIT.java`** -> AI Confidence: **99.31%**
790. **`x-pack/plugin/esql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/single_node/TSDBRestEsqlIT.java`** -> AI Confidence: **99.31%**
791. **`x-pack/plugin/esql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/single_node/TimezoneOutputIT.java`** -> AI Confidence: **99.31%**
792. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/datasources/FixtureUtils.java`** -> AI Confidence: **99.31%**
793. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/AbstractExternalSourceSpecTestCase.java`** -> AI Confidence: **99.31%**
794. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/RestEsqlTestCase.java`** -> AI Confidence: **99.31%**
795. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/SemanticMatchTestCase.java`** -> AI Confidence: **99.31%**
796. **`x-pack/plugin/esql/qa/server/src/orcFixtureGenerator/java/org/elasticsearch/xpack/esql/datasources/OrcFixtureGenerator.java`** -> AI Confidence: **99.31%**
797. **`x-pack/plugin/esql/qa/server/src/parquetFixtureGenerator/java/org/elasticsearch/xpack/esql/datasources/ParquetFixtureGenerator.java`** -> AI Confidence: **99.31%**
798. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/LoadMapping.java`** -> AI Confidence: **99.31%**
799. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/command/pipe/UriPartsGenerator.java`** -> AI Confidence: **99.31%**
800. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/function/ConditionalFunctionGenerator.java`** -> AI Confidence: **99.31%**
801. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/function/FullTextFunctionGenerator.java`** -> AI Confidence: **99.31%**
802. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterEnrichIT.java`** -> AI Confidence: **99.31%**
803. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterEnrichUnavailableClustersIT.java`** -> AI Confidence: **99.31%**
804. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterQueryDatastreamIT.java`** -> AI Confidence: **99.31%**
805. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterQueryUnavailableRemotesIT.java`** -> AI Confidence: **99.31%**
806. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterQueryWithFiltersIT.java`** -> AI Confidence: **99.31%**
807. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterSubqueryIT.java`** -> AI Confidence: **99.31%**
808. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterViewIT.java`** -> AI Confidence: **99.31%**
809. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/RandomizedTimeSeriesIT.java`** -> AI Confidence: **99.31%**
810. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InBooleanEvaluator.java`** -> AI Confidence: **99.31%**
811. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMaxBooleanEvaluator.java`** -> AI Confidence: **99.31%**
812. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMaxDoubleEvaluator.java`** -> AI Confidence: **99.31%**
813. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMaxIntegerEvaluator.java`** -> AI Confidence: **99.31%**
814. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMaxLongEvaluator.java`** -> AI Confidence: **99.31%**
815. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMinBooleanEvaluator.java`** -> AI Confidence: **99.31%**
816. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMinDoubleEvaluator.java`** -> AI Confidence: **99.31%**
817. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMinIntegerEvaluator.java`** -> AI Confidence: **99.31%**
818. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMinLongEvaluator.java`** -> AI Confidence: **99.31%**
819. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToIntegerBaseEvaluator.java`** -> AI Confidence: **99.31%**
820. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToLongBaseEvaluator.java`** -> AI Confidence: **99.31%**
821. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffConstantMillisEvaluator.java`** -> AI Confidence: **99.31%**
822. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffConstantMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
823. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffConstantNanosEvaluator.java`** -> AI Confidence: **99.31%**
824. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffConstantNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
825. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffMillisEvaluator.java`** -> AI Confidence: **99.31%**
826. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
827. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffNanosEvaluator.java`** -> AI Confidence: **99.31%**
828. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
829. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateExtractMillisEvaluator.java`** -> AI Confidence: **99.31%**
830. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateExtractNanosEvaluator.java`** -> AI Confidence: **99.31%**
831. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/ip/IpPrefixEvaluator.java`** -> AI Confidence: **99.31%**
832. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/ip/NetworkDirectionEvaluator.java`** -> AI Confidence: **99.31%**
833. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/Atan2Evaluator.java`** -> AI Confidence: **99.31%**
834. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CopySignDoubleEvaluator.java`** -> AI Confidence: **99.31%**
835. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CopySignFloatEvaluator.java`** -> AI Confidence: **99.31%**
836. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CopySignIntegerEvaluator.java`** -> AI Confidence: **99.31%**
837. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CopySignLongEvaluator.java`** -> AI Confidence: **99.31%**
838. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/HypotEvaluator.java`** -> AI Confidence: **99.31%**
839. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/LogEvaluator.java`** -> AI Confidence: **99.31%**
840. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/PowEvaluator.java`** -> AI Confidence: **99.31%**
841. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/RoundDoubleEvaluator.java`** -> AI Confidence: **99.31%**
842. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/RoundIntEvaluator.java`** -> AI Confidence: **99.31%**
843. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/RoundLongEvaluator.java`** -> AI Confidence: **99.31%**
844. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/RoundUnsignedLongEvaluator.java`** -> AI Confidence: **99.31%**
845. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/ScalbIntEvaluator.java`** -> AI Confidence: **99.31%**
846. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/ScalbLongEvaluator.java`** -> AI Confidence: **99.31%**
847. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvSliceBooleanEvaluator.java`** -> AI Confidence: **99.31%**
848. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvSliceBytesRefEvaluator.java`** -> AI Confidence: **99.31%**
849. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvSliceDoubleEvaluator.java`** -> AI Confidence: **99.31%**
850. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvSliceIntEvaluator.java`** -> AI Confidence: **99.31%**
851. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvSliceLongEvaluator.java`** -> AI Confidence: **99.31%**
852. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/JsonExtractEvaluator.java`** -> AI Confidence: **99.31%**
853. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/LocateEvaluator.java`** -> AI Confidence: **99.31%**
854. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/RepeatEvaluator.java`** -> AI Confidence: **99.31%**
855. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/ReplaceConstantEvaluator.java`** -> AI Confidence: **99.31%**
856. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/ReplaceEvaluator.java`** -> AI Confidence: **99.31%**
857. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/SubstringEvaluator.java`** -> AI Confidence: **99.31%**
858. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddDoublesEvaluator.java`** -> AI Confidence: **99.31%**
859. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddIntsEvaluator.java`** -> AI Confidence: **99.31%**
860. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddLongsEvaluator.java`** -> AI Confidence: **99.31%**
861. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddUnsignedLongsEvaluator.java`** -> AI Confidence: **99.31%**
862. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/DivDoublesEvaluator.java`** -> AI Confidence: **99.31%**
863. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/DivIntsEvaluator.java`** -> AI Confidence: **99.31%**
864. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/DivLongsEvaluator.java`** -> AI Confidence: **99.31%**
865. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/DivUnsignedLongsEvaluator.java`** -> AI Confidence: **99.31%**
866. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/ModDoublesEvaluator.java`** -> AI Confidence: **99.31%**
867. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/ModIntsEvaluator.java`** -> AI Confidence: **99.31%**
868. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/ModLongsEvaluator.java`** -> AI Confidence: **99.31%**
869. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/ModUnsignedLongsEvaluator.java`** -> AI Confidence: **99.31%**
870. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/MulDoublesEvaluator.java`** -> AI Confidence: **99.31%**
871. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/MulIntsEvaluator.java`** -> AI Confidence: **99.31%**
872. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/MulLongsEvaluator.java`** -> AI Confidence: **99.31%**
873. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/MulUnsignedLongsEvaluator.java`** -> AI Confidence: **99.31%**
874. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/SubDoublesEvaluator.java`** -> AI Confidence: **99.31%**
875. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/SubIntsEvaluator.java`** -> AI Confidence: **99.31%**
876. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/SubLongsEvaluator.java`** -> AI Confidence: **99.31%**
877. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/SubUnsignedLongsEvaluator.java`** -> AI Confidence: **99.31%**
878. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsBoolsEvaluator.java`** -> AI Confidence: **99.31%**
879. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsDoublesEvaluator.java`** -> AI Confidence: **99.31%**
880. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsIntsEvaluator.java`** -> AI Confidence: **99.31%**
881. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsLongsEvaluator.java`** -> AI Confidence: **99.31%**
882. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
883. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
884. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanDoublesEvaluator.java`** -> AI Confidence: **99.31%**
885. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanIntsEvaluator.java`** -> AI Confidence: **99.31%**
886. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanLongsEvaluator.java`** -> AI Confidence: **99.31%**
887. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
888. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
889. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqualDoublesEvaluator.java`** -> AI Confidence: **99.31%**
890. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqualIntsEvaluator.java`** -> AI Confidence: **99.31%**
891. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqualLongsEvaluator.java`** -> AI Confidence: **99.31%**
892. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqualMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
893. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqualNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
894. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanDoublesEvaluator.java`** -> AI Confidence: **99.31%**
895. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanIntsEvaluator.java`** -> AI Confidence: **99.31%**
896. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanLongsEvaluator.java`** -> AI Confidence: **99.31%**
897. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
898. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
899. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanOrEqualDoublesEvaluator.java`** -> AI Confidence: **99.31%**
900. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanOrEqualIntsEvaluator.java`** -> AI Confidence: **99.31%**
901. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanOrEqualLongsEvaluator.java`** -> AI Confidence: **99.31%**
902. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanOrEqualMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
903. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanOrEqualNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
904. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsBoolsEvaluator.java`** -> AI Confidence: **99.31%**
905. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsDoublesEvaluator.java`** -> AI Confidence: **99.31%**
906. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsIntsEvaluator.java`** -> AI Confidence: **99.31%**
907. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsLongsEvaluator.java`** -> AI Confidence: **99.31%**
908. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsMillisNanosEvaluator.java`** -> AI Confidence: **99.31%**
909. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsNanosMillisEvaluator.java`** -> AI Confidence: **99.31%**
910. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/ParseTables.java`** -> AI Confidence: **99.31%**
911. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/RequestXContent.java`** -> AI Confidence: **99.31%**
912. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/capabilities/TranslationAware.java`** -> AI Confidence: **99.31%**
913. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/common/spatial/H3SphericalUtil.java`** -> AI Confidence: **99.31%**
914. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/core/expression/Expressions.java`** -> AI Confidence: **99.31%**
915. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/core/expression/predicate/BinaryOperator.java`** -> AI Confidence: **99.31%**
916. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/core/tree/Node.java`** -> AI Confidence: **99.31%**
917. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/core/type/DataTypeConverter.java`** -> AI Confidence: **99.31%**
918. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/AsyncConnectorSourceOperatorFactory.java`** -> AI Confidence: **99.31%**
919. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/AsyncExternalSourceOperatorFactory.java`** -> AI Confidence: **99.31%**
920. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/FileSourceFactory.java`** -> AI Confidence: **99.31%**
921. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/FileSplitProvider.java`** -> AI Confidence: **99.31%**
922. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/GlobExpander.java`** -> AI Confidence: **99.31%**
923. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/HivePartitionDetector.java`** -> AI Confidence: **99.31%**
924. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/ParallelParsingCoordinator.java`** -> AI Confidence: **99.31%**
925. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/PartitionFilterHintExtractor.java`** -> AI Confidence: **99.31%**
926. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/TemplatePartitionDetector.java`** -> AI Confidence: **99.31%**
927. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/evaluator/command/UriPartsFunctionBridge.java`** -> AI Confidence: **99.31%**
928. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/aggregate/Values.java`** -> AI Confidence: **99.31%**
929. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToIntegerSurrogate.java`** -> AI Confidence: **99.31%**
930. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToLongSurrogate.java`** -> AI Confidence: **99.31%**
931. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/internal/InternalPacks.java`** -> AI Confidence: **99.31%**
932. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvMedianAbsoluteDeviation.java`** -> AI Confidence: **99.31%**
933. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/formatter/TextFormatter.java`** -> AI Confidence: **99.31%**
934. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/inference/textembedding/TextEmbeddingOutputBuilder.java`** -> AI Confidence: **99.31%**
935. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/PlanConsistencyChecker.java`** -> AI Confidence: **99.31%**
936. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/CombineBinaryComparisons.java`** -> AI Confidence: **99.31%**
937. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/PropagateEquals.java`** -> AI Confidence: **99.31%**
938. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/PushDownConjunctionsToKnnPrefilters.java`** -> AI Confidence: **99.31%**
939. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushCountQueryAndTagsToSource.java`** -> AI Confidence: **99.31%**
940. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/parser/promql/PromqlLogicalPlanBuilder.java`** -> AI Confidence: **99.31%**
941. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/parser/promql/PromqlParserUtils.java`** -> AI Confidence: **99.31%**
942. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plan/QuerySettings.java`** -> AI Confidence: **99.31%**
943. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/rule/RuleExecutor.java`** -> AI Confidence: **99.31%**
944. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/session/IndexResolver.java`** -> AI Confidence: **99.31%**
945. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/telemetry/Metrics.java`** -> AI Confidence: **99.31%**
946. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/action/EsqlQueryRequestTests.java`** -> AI Confidence: **99.31%**
947. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/action/EsqlQueryResponseTests.java`** -> AI Confidence: **99.31%**
948. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/analysis/AnalyzerParsingTests.java`** -> AI Confidence: **99.31%**
949. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/analysis/AnalyzerUnmappedTests.java`** -> AI Confidence: **99.31%**
950. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/datasources/spi/ColumnBlockConversionsTests.java`** -> AI Confidence: **99.31%**
951. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/enrich/EnrichOperatorStatusTests.java`** -> AI Confidence: **99.31%**
952. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/enrich/LookupFromIndexOperatorStatusTests.java`** -> AI Confidence: **99.31%**
953. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/evaluator/command/TestCompoundOutputEvaluatorTests.java`** -> AI Confidence: **99.31%**
954. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/AbstractScalarFunctionTestCase.java`** -> AI Confidence: **99.31%**
955. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/AbstractUrlEncodeDecodeTestCase.java`** -> AI Confidence: **99.31%**
956. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/DocsV3Support.java`** -> AI Confidence: **99.31%**
957. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/DocsV3SupportTests.java`** -> AI Confidence: **99.31%**
958. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/WindowFilterTests.java`** -> AI Confidence: **99.31%**
959. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/aggregate/AbstractFirstLastTestCase.java`** -> AI Confidence: **99.31%**
960. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/aggregate/AvgTests.java`** -> AI Confidence: **99.31%**
961. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/aggregate/SumTests.java`** -> AI Confidence: **99.31%**
962. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/aggregate/WeightedAvgTests.java`** -> AI Confidence: **99.31%**
963. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/fulltext/AbstractMatchFullTextFunctionTests.java`** -> AI Confidence: **99.31%**
964. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/grouping/BucketOffsetTests.java`** -> AI Confidence: **99.31%**
965. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToDateNanosTests.java`** -> AI Confidence: **99.31%**
966. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToDatetimeTests.java`** -> AI Confidence: **99.31%**
967. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToIntegerBaseErrorTests.java`** -> AI Confidence: **99.31%**
968. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToIntegerTests.java`** -> AI Confidence: **99.31%**
969. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToLongBaseErrorTests.java`** -> AI Confidence: **99.31%**
970. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToUnsignedLongTests.java`** -> AI Confidence: **99.31%**
971. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateDiffTests.java`** -> AI Confidence: **99.31%**
972. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateTruncTests.java`** -> AI Confidence: **99.31%**
973. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/date/TRangeTests.java`** -> AI Confidence: **99.31%**
974. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/histogram/ExtractHistogramComponentTests.java`** -> AI Confidence: **99.31%**
975. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/math/AbsTests.java`** -> AI Confidence: **99.31%**
976. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/math/CopySignTests.java`** -> AI Confidence: **99.31%**
977. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/math/SqrtTests.java`** -> AI Confidence: **99.31%**
978. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvIntersectsBlockTests.java`** -> AI Confidence: **99.31%**
979. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/spatial/BinarySpatialFunctionTestCase.java`** -> AI Confidence: **99.31%**
980. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/string/JsonExtractTests.java`** -> AI Confidence: **99.31%**
981. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/promql/PromqlCoverageAnalyzer.java`** -> AI Confidence: **99.31%**
982. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/SubstituteRoundToGoldenTests.java`** -> AI Confidence: **99.31%**
983. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/logical/inference/CompletionSerializationTests.java`** -> AI Confidence: **99.31%**
984. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/physical/ExternalSourceExecSerializationTests.java`** -> AI Confidence: **99.31%**
985. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/planner/GrokEvaluatorExtracterTests.java`** -> AI Confidence: **99.31%**
986. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plugin/ExtendedDistributionPropertyTests.java`** -> AI Confidence: **99.31%**
987. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/stats/SearchContextStatsTests.java`** -> AI Confidence: **99.31%**
988. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/type/EsqlDataTypeConverterTests.java`** -> AI Confidence: **99.31%**
989. **`x-pack/plugin/graph/src/main/java/org/elasticsearch/xpack/graph/action/TransportGraphExploreAction.java`** -> AI Confidence: **99.31%**
990. **`x-pack/plugin/graph/src/main/java/org/elasticsearch/xpack/graph/rest/action/RestGraphAction.java`** -> AI Confidence: **99.31%**
991. **`x-pack/plugin/identity-provider/src/test/java/org/elasticsearch/xpack/idp/privileges/UserPrivilegeResolverTests.java`** -> AI Confidence: **99.31%**
992. **`x-pack/plugin/identity-provider/src/test/java/org/elasticsearch/xpack/idp/saml/idp/SamlMetadataGeneratorTests.java`** -> AI Confidence: **99.31%**
993. **`x-pack/plugin/identity-provider/src/test/java/org/elasticsearch/xpack/idp/saml/sp/WildcardServiceProviderResolverTests.java`** -> AI Confidence: **99.31%**
994. **`x-pack/plugin/ilm/src/javaRestTest/java/org/elasticsearch/xpack/ilm/actions/DownsampleActionIT.java`** -> AI Confidence: **99.31%**
995. **`x-pack/plugin/ilm/src/test/java/org/elasticsearch/xpack/ilm/history/ILMHistoryItemTests.java`** -> AI Confidence: **99.31%**
996. **`x-pack/plugin/inference/qa/mixed-cluster/src/javaRestTest/java/org/elasticsearch/xpack/inference/qa/mixed/CohereServiceMixedIT.java`** -> AI Confidence: **99.31%**
997. **`x-pack/plugin/inference/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/application/CohereServiceUpgradeIT.java`** -> AI Confidence: **99.31%**
998. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/amazonbedrock/request/completion/AmazonBedrockConverseUtils.java`** -> AI Confidence: **99.31%**
999. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/cohere/response/CohereRankedResponseEntity.java`** -> AI Confidence: **99.31%**
1000. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/googlevertexai/request/GoogleVertexAiEmbeddingsRequestEntity.java`** -> AI Confidence: **99.31%**
1001. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/ibmwatsonx/response/IbmWatsonxRankedResponseEntity.java`** -> AI Confidence: **99.31%**
1002. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/sagemaker/schema/SageMakerSchema.java`** -> AI Confidence: **99.31%**
1003. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/action/GetInferenceFieldsInternalActionRequestTests.java`** -> AI Confidence: **99.31%**
1004. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/external/unified/UnifiedChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.31%**
1005. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/rank/textsimilarity/TextSimilarityRankDocTests.java`** -> AI Confidence: **99.31%**
1006. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/anthropic/AnthropicChatCompletionStreamingProcessorTests.java`** -> AI Confidence: **99.31%**
1007. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/anthropic/AnthropicStreamingProcessorTests.java`** -> AI Confidence: **99.31%**
1008. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/anthropic/response/AnthropicChatCompletionResponseEntityTests.java`** -> AI Confidence: **99.31%**
1009. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/azureopenai/response/AzureOpenAiCompletionResponseEntityTests.java`** -> AI Confidence: **99.31%**
1010. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/cohere/response/CohereCompletionResponseEntityTests.java`** -> AI Confidence: **99.31%**
1011. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/cohere/response/CohereEmbeddingsResponseEntityTests.java`** -> AI Confidence: **99.31%**
1012. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/cohere/response/CohereRankedResponseEntityTests.java`** -> AI Confidence: **99.31%**
1013. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/elastic/request/ElasticInferenceServiceUnifiedChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.31%**
1014. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/elastic/response/ElasticInferenceServiceAuthorizationResponseEntityTests.java`** -> AI Confidence: **99.31%**
1015. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googleaistudio/GoogleAiStudioStreamingProcessorTests.java`** -> AI Confidence: **99.31%**
1016. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googleaistudio/request/embeddings/GoogleAiStudioEmbeddingsRequestEntityTests.java`** -> AI Confidence: **99.31%**
1017. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googleaistudio/response/GoogleAiStudioCompletionResponseEntityTests.java`** -> AI Confidence: **99.31%**
1018. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/request/GoogleVertexAiRerankRequestEntityTests.java`** -> AI Confidence: **99.31%**
1019. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/request/completion/GoogleModelGardenAnthropicChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.31%**
1020. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/response/GoogleVertexAiCompletionResponseEntityTests.java`** -> AI Confidence: **99.31%**
1021. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/response/GoogleVertexAiEmbeddingsResponseEntityTests.java`** -> AI Confidence: **99.31%**
1022. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/response/GoogleVertexAiRerankResponseEntityTests.java`** -> AI Confidence: **99.31%**
1023. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/ibmwatsonx/request/IbmWatsonxRerankRequestEntityTests.java`** -> AI Confidence: **99.31%**
1024. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/jinaai/response/JinaAIEmbeddingsResponseEntityTests.java`** -> AI Confidence: **99.31%**
1025. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/jinaai/response/JinaAIRerankResponseEntityTests.java`** -> AI Confidence: **99.31%**
1026. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/response/OpenAiChatCompletionResponseEntityTests.java`** -> AI Confidence: **99.31%**
1027. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/response/OpenAiEmbeddingsResponseEntityTests.java`** -> AI Confidence: **99.31%**
1028. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openshiftai/completion/OpenShiftAiChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.31%**
1029. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/sagemaker/model/SageMakerModelBuilderTests.java`** -> AI Confidence: **99.31%**
1030. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/sagemaker/schema/openai/OpenAiCompletionPayloadTests.java`** -> AI Confidence: **99.31%**
1031. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/voyageai/response/VoyageAIEmbeddingsResponseEntityTests.java`** -> AI Confidence: **99.31%**
1032. **`x-pack/plugin/kql/src/main/java/org/elasticsearch/xpack/kql/parser/KqlAstBuilder.java`** -> AI Confidence: **99.31%**
1033. **`x-pack/plugin/kql/src/main/java/org/elasticsearch/xpack/kql/parser/ParserUtils.java`** -> AI Confidence: **99.31%**
1034. **`x-pack/plugin/kql/src/test/java/org/elasticsearch/xpack/kql/parser/ParserUtilsTests.java`** -> AI Confidence: **99.31%**
1035. **`x-pack/plugin/logsdb/qa/legacy-rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/NoLogsUsageRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
1036. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/LogsdbIndexingRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
1037. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/StandardToLogsDbIndexModeRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
1038. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/SyntheticSourceRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
1039. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/TsdbIndexingRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
1040. **`x-pack/plugin/logsdb/qa/with-basic/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/LogsdbWithBasicRestIT.java`** -> AI Confidence: **99.31%**
1041. **`x-pack/plugin/logsdb/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/LogsIndexModeCustomSettingsIT.java`** -> AI Confidence: **99.31%**
1042. **`x-pack/plugin/logsdb/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/LogsdbRestIT.java`** -> AI Confidence: **99.31%**
1043. **`x-pack/plugin/logsdb/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/LogsdbSnapshotRestoreIT.java`** -> AI Confidence: **99.31%**
1044. **`x-pack/plugin/logsdb/src/test/java/org/elasticsearch/xpack/logsdb/patterntext/PatternTextValueProcessorTests.java`** -> AI Confidence: **99.31%**
1045. **`x-pack/plugin/mapper-version/src/main/java/org/elasticsearch/xpack/versionfield/VersionEncoder.java`** -> AI Confidence: **99.31%**
1046. **`x-pack/plugin/ml-package-loader/src/test/java/org/elasticsearch/xpack/ml/packageloader/MachineLearningPackageLoaderTests.java`** -> AI Confidence: **99.31%**
1047. **`x-pack/plugin/ml/qa/basic-multi-node/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/MlBasicMultiNodeIT.java`** -> AI Confidence: **99.31%**
1048. **`x-pack/plugin/ml/qa/datafeed-multicluster-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/datafeed/DatafeedRemoteClusterClientIT.java`** -> AI Confidence: **99.31%**
1049. **`x-pack/plugin/ml/qa/ml-with-security/src/yamlRestTest/java/org/elasticsearch/smoketest/MlWithSecurityInsufficientRoleIT.java`** -> AI Confidence: **99.31%**
1050. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/CategorizationIT.java`** -> AI Confidence: **99.31%**
1051. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/InferenceIT.java`** -> AI Confidence: **99.31%**
1052. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/MlJobIT.java`** -> AI Confidence: **99.31%**
1053. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/RunDataFrameAnalyticsIT.java`** -> AI Confidence: **99.31%**
1054. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/TrainedModelIT.java`** -> AI Confidence: **99.31%**
1055. **`x-pack/plugin/ml/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/DatafeedWithoutSecurityRestIT.java`** -> AI Confidence: **99.31%**
1056. **`x-pack/plugin/ml/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/InferenceIT.java`** -> AI Confidence: **99.31%**
1057. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/MlAssignmentNotifier.java`** -> AI Confidence: **99.31%**
1058. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/MlAggsHelper.java`** -> AI Confidence: **99.31%**
1059. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/categorization/SerializableTokenListCategory.java`** -> AI Confidence: **99.31%**
1060. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/categorization/TokenListCategory.java`** -> AI Confidence: **99.31%**
1061. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/frequentitemsets/HashBasedTransactionStore.java`** -> AI Confidence: **99.31%**
1062. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/kstest/BucketCountKSTestAggregator.java`** -> AI Confidence: **99.31%**
1063. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/autoscaling/MlMemoryAutoscalingDecider.java`** -> AI Confidence: **99.31%**
1064. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/autoscaling/NativeMemoryCapacity.java`** -> AI Confidence: **99.31%**
1065. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/datafeed/DatafeedRunner.java`** -> AI Confidence: **99.31%**
1066. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/datafeed/extractor/aggregation/AggregationToJsonProcessor.java`** -> AI Confidence: **99.31%**
1067. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/dataframe/extractor/ExtractedFieldsDetector.java`** -> AI Confidence: **99.31%**
1068. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/dataframe/process/AnalyticsResultProcessor.java`** -> AI Confidence: **99.31%**
1069. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/extractor/GeoShapeField.java`** -> AI Confidence: **99.31%**
1070. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/TrainedModelAssignmentRebalancer.java`** -> AI Confidence: **99.31%**
1071. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/AbstractPreserveAllocations.java`** -> AI Confidence: **99.31%**
1072. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/AllocationReducer.java`** -> AI Confidence: **99.31%**
1073. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/AssignmentPlanner.java`** -> AI Confidence: **99.31%**
1074. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/LinearProgrammingPlanSolver.java`** -> AI Confidence: **99.31%**
1075. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/RandomizedAssignmentRounding.java`** -> AI Confidence: **99.31%**
1076. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/ZoneAwareAssignmentPlanner.java`** -> AI Confidence: **99.31%**
1077. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/NlpTokenizer.java`** -> AI Confidence: **99.31%**
1078. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/JobNodeSelector.java`** -> AI Confidence: **99.31%**
1079. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/persistence/StateStreamer.java`** -> AI Confidence: **99.31%**
1080. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/process/normalizer/Normalizer.java`** -> AI Confidence: **99.31%**
1081. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/process/NativeStorageProvider.java`** -> AI Confidence: **99.31%**
1082. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/rest/cat/RestCatJobsAction.java`** -> AI Confidence: **99.31%**
1083. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/aggs/categorization/CategorizeTextAggregatorTests.java`** -> AI Confidence: **99.31%**
1084. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/datafeed/extractor/aggregation/AggregationToJsonProcessorTests.java`** -> AI Confidence: **99.31%**
1085. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/inference/modelsize/ModelSizeInfoTests.java`** -> AI Confidence: **99.31%**
1086. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/categorization/GrokPatternCreatorTests.java`** -> AI Confidence: **99.31%**
1087. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/process/normalizer/output/NormalizerResultHandlerTests.java`** -> AI Confidence: **99.31%**
1088. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/process/logging/CppLogMessageHandlerTests.java`** -> AI Confidence: **99.31%**
1089. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/utils/time/DateTimeFormatterTimestampConverterTests.java`** -> AI Confidence: **99.31%**
1090. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/indices/IndexRecoveryMonitoringDocTests.java`** -> AI Confidence: **99.31%**
1091. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/indices/IndexStatsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
1092. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/indices/IndicesStatsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
1093. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/ml/JobStatsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
1094. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/node/NodeStatsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
1095. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/collector/shards/ShardsMonitoringDocTests.java`** -> AI Confidence: **99.31%**
1096. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/exporter/http/TemplateHttpResourceTests.java`** -> AI Confidence: **99.31%**
1097. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/Lucene40BlockTreeTermsReader.java`** -> AI Confidence: **99.31%**
1098. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/SegmentTermsEnum.java`** -> AI Confidence: **99.31%**
1099. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/SegmentTermsEnumFrame.java`** -> AI Confidence: **99.31%**
1100. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/Stats.java`** -> AI Confidence: **99.31%**
1101. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene54/Lucene54DocValuesConsumer.java`** -> AI Confidence: **99.31%**
1102. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene62/Lucene62SegmentInfoFormat.java`** -> AI Confidence: **99.31%**
1103. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene70/Lucene70DocValuesConsumer.java`** -> AI Confidence: **99.31%**
1104. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene70/fst/BytesStore.java`** -> AI Confidence: **99.31%**
1105. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene70/fst/Util.java`** -> AI Confidence: **99.31%**
1106. **`x-pack/plugin/old-lucene-versions/src/test/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene50/Lucene50PostingsWriter.java`** -> AI Confidence: **99.31%**
1107. **`x-pack/plugin/otel-data/src/main/java/org/elasticsearch/xpack/oteldata/otlp/datapoint/ExponentialHistogramConverter.java`** -> AI Confidence: **99.31%**
1108. **`x-pack/plugin/otel-data/src/main/java/org/elasticsearch/xpack/oteldata/otlp/tsid/AttributeListTsidFunnel.java`** -> AI Confidence: **99.31%**
1109. **`x-pack/plugin/prometheus/src/main/java/org/elasticsearch/xpack/prometheus/rest/PrometheusSeriesResponseListener.java`** -> AI Confidence: **99.31%**
1110. **`x-pack/plugin/prometheus/src/main/java/org/elasticsearch/xpack/prometheus/rest/SnappyBlockDecoder.java`** -> AI Confidence: **99.31%**
1111. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/Expressions.java`** -> AI Confidence: **99.31%**
1112. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/gen/script/Params.java`** -> AI Confidence: **99.31%**
1113. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/predicate/BinaryOperator.java`** -> AI Confidence: **99.31%**
1114. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/optimizer/OptimizerRules.java`** -> AI Confidence: **99.31%**
1115. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/tree/Node.java`** -> AI Confidence: **99.31%**
1116. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/type/DataTypeConverter.java`** -> AI Confidence: **99.31%**
1117. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/type/Types.java`** -> AI Confidence: **99.31%**
1118. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/util/StringUtils.java`** -> AI Confidence: **99.31%**
1119. **`x-pack/plugin/ql/src/test/java/org/elasticsearch/xpack/ql/action/QlStatusResponseTests.java`** -> AI Confidence: **99.31%**
1120. **`x-pack/plugin/ql/test-fixtures/src/main/java/org/elasticsearch/xpack/ql/CsvSpecReader.java`** -> AI Confidence: **99.31%**
1121. **`x-pack/plugin/rank-rrf/src/main/java/org/elasticsearch/xpack/rank/linear/LinearRankDoc.java`** -> AI Confidence: **99.31%**
1122. **`x-pack/plugin/rank-rrf/src/main/java/org/elasticsearch/xpack/rank/rrf/RRFQueryPhaseRankShardContext.java`** -> AI Confidence: **99.31%**
1123. **`x-pack/plugin/rank-rrf/src/test/java/org/elasticsearch/xpack/rank/linear/LinearRankDocTests.java`** -> AI Confidence: **99.31%**
1124. **`x-pack/plugin/rank-rrf/src/test/java/org/elasticsearch/xpack/rank/rrf/RRFRankDocTests.java`** -> AI Confidence: **99.31%**
1125. **`x-pack/plugin/rank-rrf/src/test/java/org/elasticsearch/xpack/rank/rrf/RRFRetrieverBuilderParsingTests.java`** -> AI Confidence: **99.31%**
1126. **`x-pack/plugin/rank-vectors/src/main/java/org/elasticsearch/xpack/rank/vectors/script/RankVectorsScoreScriptUtils.java`** -> AI Confidence: **99.31%**
1127. **`x-pack/plugin/rollup/src/main/java/org/elasticsearch/xpack/rollup/RollupJobIdentifierUtils.java`** -> AI Confidence: **99.31%**
1128. **`x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/action/SearchableSnapshotsStatsResponse.java`** -> AI Confidence: **99.31%**
1129. **`x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/cache/common/CacheFile.java`** -> AI Confidence: **99.31%**
1130. **`x-pack/plugin/security/cli/src/main/java/org/elasticsearch/xpack/security/cli/CertificateGenerateTool.java`** -> AI Confidence: **99.31%**
1131. **`x-pack/plugin/security/cli/src/main/java/org/elasticsearch/xpack/security/cli/HttpCertificateCommand.java`** -> AI Confidence: **99.31%**
1132. **`x-pack/plugin/security/cli/src/test/java/org/elasticsearch/xpack/security/cli/AutoConfigureNodeTests.java`** -> AI Confidence: **99.31%**
1133. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/AbstractRemoteClusterSecurityBWCRestIT.java`** -> AI Confidence: **99.31%**
1134. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/AbstractRemoteClusterSecurityFailureStoreRestIT.java`** -> AI Confidence: **99.31%**
1135. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/AbstractRemoteClusterSecurityWithMultipleRemotesRestIT.java`** -> AI Confidence: **99.31%**
1136. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/CrossClusterEsqlRCS1EnrichUnavailableRemotesIT.java`** -> AI Confidence: **99.31%**
1137. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/CrossClusterEsqlRCS1MissingIndicesIT.java`** -> AI Confidence: **99.31%**
1138. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/CrossClusterEsqlRCS1UnavailableRemotesIT.java`** -> AI Confidence: **99.31%**
1139. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/CrossClusterEsqlRCS2EnrichUnavailableRemotesIT.java`** -> AI Confidence: **99.31%**
1140. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/CrossClusterEsqlRCS2UnavailableRemotesIT.java`** -> AI Confidence: **99.31%**
1141. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityApiKeyRestIT.java`** -> AI Confidence: **99.31%**
1142. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityDataStreamEsqlRcs1IT.java`** -> AI Confidence: **99.31%**
1143. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityEsqlIT.java`** -> AI Confidence: **99.31%**
1144. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityMlIT.java`** -> AI Confidence: **99.31%**
1145. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS1FailureStoreRestIT.java`** -> AI Confidence: **99.31%**
1146. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS1PainlessExecuteIT.java`** -> AI Confidence: **99.31%**
1147. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS2FailureStoreRestIT.java`** -> AI Confidence: **99.31%**
1148. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS2PainlessExecuteIT.java`** -> AI Confidence: **99.31%**
1149. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRestIT.java`** -> AI Confidence: **99.31%**
1150. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecuritySlowLogRestIT.java`** -> AI Confidence: **99.31%**
1151. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecuritySpecialUserIT.java`** -> AI Confidence: **99.31%**
1152. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityTopologyRestIT.java`** -> AI Confidence: **99.31%**
1153. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityTransformIT.java`** -> AI Confidence: **99.31%**
1154. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityWithDlsAndFlsRestIT.java`** -> AI Confidence: **99.31%**
1155. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityWithFlsRestIT.java`** -> AI Confidence: **99.31%**
1156. **`x-pack/plugin/security/qa/profile/src/javaRestTest/java/org/elasticsearch/xpack/security/profile/ProfileIT.java`** -> AI Confidence: **99.31%**
1157. **`x-pack/plugin/security/qa/security-basic/src/javaRestTest/java/org/elasticsearch/xpack/security/QueryApiKeyIT.java`** -> AI Confidence: **99.31%**
1158. **`x-pack/plugin/security/qa/security-basic/src/javaRestTest/java/org/elasticsearch/xpack/security/QueryRoleIT.java`** -> AI Confidence: **99.31%**
1159. **`x-pack/plugin/security/qa/security-basic/src/javaRestTest/java/org/elasticsearch/xpack/security/QueryUserIT.java`** -> AI Confidence: **99.31%**
1160. **`x-pack/plugin/security/qa/security-basic/src/javaRestTest/java/org/elasticsearch/xpack/security/SecurityWithBasicLicenseIT.java`** -> AI Confidence: **99.31%**
1161. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/apikey/ApiKeyRestIT.java`** -> AI Confidence: **99.31%**
1162. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/apikey/ApiKeyWorkflowsRestrictionRestIT.java`** -> AI Confidence: **99.31%**
1163. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/crossclusteraccess/CrossClusterAccessHeadersForCcsRestIT.java`** -> AI Confidence: **99.31%**
1164. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/role/BulkDeleteRoleRestIT.java`** -> AI Confidence: **99.31%**
1165. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/role/PutRoleRestIT.java`** -> AI Confidence: **99.31%**
1166. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/role/RoleWithRemoteIndicesPrivilegesRestIT.java`** -> AI Confidence: **99.31%**
1167. **`x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/test/rest/CatIndicesWithSecurityIT.java`** -> AI Confidence: **99.31%**
1168. **`x-pack/plugin/security/qa/service-account/src/javaRestTest/java/org/elasticsearch/xpack/security/authc/service/ServiceAccountIT.java`** -> AI Confidence: **99.31%**
1169. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/ClusterPrivilegeIntegrationTests.java`** -> AI Confidence: **99.31%**
1170. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/DlsFlsRequestCacheTests.java`** -> AI Confidence: **99.31%**
1171. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/DocumentAndFieldLevelSecurityTests.java`** -> AI Confidence: **99.31%**
1172. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/DocumentLevelSecurityFeatureUsageTests.java`** -> AI Confidence: **99.31%**
1173. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/FieldLevelSecurityRandomTests.java`** -> AI Confidence: **99.31%**
1174. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/authz/AnalyzeTests.java`** -> AI Confidence: **99.31%**
1175. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/authz/IndexAliasesTests.java`** -> AI Confidence: **99.31%**
1176. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/ssl/SSLReloadDuringStartupIntegTests.java`** -> AI Confidence: **99.31%**
1177. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java`** -> AI Confidence: **99.31%**
1178. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/AuthenticatorChain.java`** -> AI Confidence: **99.31%**
1179. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/RealmsAuthenticator.java`** -> AI Confidence: **99.31%**
1180. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/TokenService.java`** -> AI Confidence: **99.31%**
1181. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/esnative/NativeUsersStore.java`** -> AI Confidence: **99.31%**
1182. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/esnative/tool/ResetPasswordTool.java`** -> AI Confidence: **99.31%**
1183. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/jwt/JwtAuthenticationToken.java`** -> AI Confidence: **99.31%**
1184. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/jwt/JwtDateClaimValidator.java`** -> AI Confidence: **99.31%**
1185. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/saml/SamlAuthenticator.java`** -> AI Confidence: **99.31%**
1186. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/saml/SamlResponseHandler.java`** -> AI Confidence: **99.31%**
1187. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/support/CachingUsernamePasswordRealm.java`** -> AI Confidence: **99.31%**
1188. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authz/AuthorizationDenialMessages.java`** -> AI Confidence: **99.31%**
1189. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authz/AuthorizationUtils.java`** -> AI Confidence: **99.31%**
1190. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authz/IndicesAndAliasesResolver.java`** -> AI Confidence: **99.31%**
1191. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authz/store/NativePrivilegeStore.java`** -> AI Confidence: **99.31%**
1192. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/transport/filter/PatternRule.java`** -> AI Confidence: **99.31%**
1193. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/core/security/action/privilege/PutPrivilegesRequestBuilderTests.java`** -> AI Confidence: **99.31%**
1194. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/action/apikey/TransportQueryApiKeyActionTests.java`** -> AI Confidence: **99.31%**
1195. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/action/reservedstate/ReservedRoleMappingActionTests.java`** -> AI Confidence: **99.31%**
1196. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/audit/logfile/LoggingAuditTrailFilterTests.java`** -> AI Confidence: **99.31%**
1197. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/audit/logfile/LoggingAuditTrailTests.java`** -> AI Confidence: **99.31%**
1198. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtRealmSettingsTests.java`** -> AI Confidence: **99.31%**
1199. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtRealmTestCase.java`** -> AI Confidence: **99.31%**
1200. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtStringClaimValidatorTests.java`** -> AI Confidence: **99.31%**
1201. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtUtilTests.java`** -> AI Confidence: **99.31%**
1202. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/oidc/OpenIdConnectRealmSettingsTests.java`** -> AI Confidence: **99.31%**
1203. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlLogoutResponseHandlerHttpPostTests.java`** -> AI Confidence: **99.31%**
1204. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlRealmTestHelper.java`** -> AI Confidence: **99.31%**
1205. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/support/mapper/ExpressionRoleMappingTests.java`** -> AI Confidence: **99.31%**
1206. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authz/AuthorizationDenialMessagesTests.java`** -> AI Confidence: **99.31%**
1207. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authz/accesscontrol/IndicesPermissionTests.java`** -> AI Confidence: **99.31%**
1208. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authz/permission/FieldPermissionsTests.java`** -> AI Confidence: **99.31%**
1209. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/enrollment/ExternalEnrollmentTokenGeneratorTests.java`** -> AI Confidence: **99.31%**
1210. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/support/ApiKeyBoolQueryBuilderTests.java`** -> AI Confidence: **99.31%**
1211. **`x-pack/plugin/slm/src/main/java/org/elasticsearch/xpack/slm/SlmHealthIndicatorService.java`** -> AI Confidence: **99.31%**
1212. **`x-pack/plugin/slm/src/test/java/org/elasticsearch/xpack/slm/SnapshotLifecyclePolicyTests.java`** -> AI Confidence: **99.31%**
1213. **`x-pack/plugin/slm/src/test/java/org/elasticsearch/xpack/slm/action/ReservedSnapshotLifecycleStateServiceTests.java`** -> AI Confidence: **99.31%**
1214. **`x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/common/H3SphericalUtil.java`** -> AI Confidence: **99.31%**
1215. **`x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/index/fielddata/Component2DRelationVisitor.java`** -> AI Confidence: **99.31%**
1216. **`x-pack/plugin/spatial/src/test/java/org/elasticsearch/xpack/spatial/search/aggregations/metrics/InternalCartesianBoundsTests.java`** -> AI Confidence: **99.31%**
1217. **`x-pack/plugin/sql/jdbc/src/main/java/org/elasticsearch/xpack/sql/jdbc/TypeConverter.java`** -> AI Confidence: **99.31%**
1218. **`x-pack/plugin/sql/jdbc/src/test/java/org/elasticsearch/xpack/sql/jdbc/JdbcConfigurationTests.java`** -> AI Confidence: **99.31%**
1219. **`x-pack/plugin/sql/qa/jdbc/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/PreparedStatementTestCase.java`** -> AI Confidence: **99.31%**
1220. **`x-pack/plugin/sql/qa/server/multi-cluster-with-security/src/javaRestTest/java/org/elasticsearch/xpack/sql/qa/multi_cluster_with_security/JdbcCsvSpecIT.java`** -> AI Confidence: **99.31%**
1221. **`x-pack/plugin/sql/qa/server/security/src/test/java/org/elasticsearch/xpack/sql/qa/security/JdbcApiKeyIT.java`** -> AI Confidence: **99.31%**
1222. **`x-pack/plugin/sql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/sql/qa/single_node/JdbcShardFailureIT.java`** -> AI Confidence: **99.31%**
1223. **`x-pack/plugin/sql/qa/server/single-node/src/javaRestTest/java/org/elasticsearch/xpack/sql/qa/single_node/RestSqlIT.java`** -> AI Confidence: **99.31%**
1224. **`x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/SqlProtocolTestCase.java`** -> AI Confidence: **99.31%**
1225. **`x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/cli/EmbeddedCli.java`** -> AI Confidence: **99.31%**
1226. **`x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/DatabaseMetaDataTestCase.java`** -> AI Confidence: **99.31%**
1227. **`x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/JdbcAssert.java`** -> AI Confidence: **99.31%**
1228. **`x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/rest/RestSqlTestCase.java`** -> AI Confidence: **99.31%**
1229. **`x-pack/plugin/sql/sql-client/src/main/java/org/elasticsearch/xpack/sql/client/RemoteFailure.java`** -> AI Confidence: **99.31%**
1230. **`x-pack/plugin/sql/sql-client/src/main/java/org/elasticsearch/xpack/sql/client/StringUtils.java`** -> AI Confidence: **99.31%**
1231. **`x-pack/plugin/sql/sql-client/src/main/java/org/elasticsearch/xpack/sql/client/UriUtils.java`** -> AI Confidence: **99.31%**
1232. **`x-pack/plugin/sql/sql-proto/src/main/java/org/elasticsearch/xpack/sql/proto/content/GeneratorUtils.java`** -> AI Confidence: **99.31%**
1233. **`x-pack/plugin/sql/sql-proto/src/main/java/org/elasticsearch/xpack/sql/proto/content/ObjectParser.java`** -> AI Confidence: **99.31%**
1234. **`x-pack/plugin/sql/sql-proto/src/main/java/org/elasticsearch/xpack/sql/proto/formatter/SimpleFormatter.java`** -> AI Confidence: **99.31%**
1235. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/execution/search/SearchHitRowSet.java`** -> AI Confidence: **99.31%**
1236. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/ToCharFormatter.java`** -> AI Confidence: **99.31%**
1237. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/expression/function/scalar/math/MathProcessor.java`** -> AI Confidence: **99.31%**
1238. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/parser/IdentifierBuilder.java`** -> AI Confidence: **99.31%**
1239. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/querydsl/agg/GroupByKey.java`** -> AI Confidence: **99.31%**
1240. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateAddPipeTests.java`** -> AI Confidence: **99.31%**
1241. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateAddProcessorTests.java`** -> AI Confidence: **99.31%**
1242. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateDiffPipeTests.java`** -> AI Confidence: **99.31%**
1243. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/string/InsertFunctionPipeTests.java`** -> AI Confidence: **99.31%**
1244. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/string/LocateFunctionPipeTests.java`** -> AI Confidence: **99.31%**
1245. **`x-pack/plugin/text-structure/src/javaRestTest/java/org/elasticsearch/xpack/textstructure/rest/TextStructureNestedJsonIT.java`** -> AI Confidence: **99.31%**
1246. **`x-pack/plugin/text-structure/src/javaRestTest/java/org/elasticsearch/xpack/textstructure/rest/TextStructureTimestampFormatsIT.java`** -> AI Confidence: **99.31%**
1247. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/DelimitedTextStructureFinder.java`** -> AI Confidence: **99.31%**
1248. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/FieldStatsCalculator.java`** -> AI Confidence: **99.31%**
1249. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/LogTextStructureFinder.java`** -> AI Confidence: **99.31%**
1250. **`x-pack/plugin/text-structure/src/test/java/org/elasticsearch/xpack/textstructure/structurefinder/EnhancedTimestampDetectionTests.java`** -> AI Confidence: **99.31%**
1251. **`x-pack/plugin/text-structure/src/test/java/org/elasticsearch/xpack/textstructure/structurefinder/LogTextStructureFinderTests.java`** -> AI Confidence: **99.31%**
1252. **`x-pack/plugin/text-structure/src/test/java/org/elasticsearch/xpack/textstructure/structurefinder/TextStructureUtilsTests.java`** -> AI Confidence: **99.31%**
1253. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/LatestIT.java`** -> AI Confidence: **99.31%**
1254. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformChainIT.java`** -> AI Confidence: **99.31%**
1255. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/continuous/DateHistogramGroupByOtherTimeFieldIT.java`** -> AI Confidence: **99.31%**
1256. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformRestTestCase.java`** -> AI Confidence: **99.31%**
1257. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformRobustnessIT.java`** -> AI Confidence: **99.31%**
1258. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/rest/action/RestCatTransformAction.java`** -> AI Confidence: **99.31%**
1259. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/TransformFailureHandler.java`** -> AI Confidence: **99.31%**
1260. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/pivot/GroupByOptimizer.java`** -> AI Confidence: **99.31%**
1261. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/pivot/SchemaUtil.java`** -> AI Confidence: **99.31%**
1262. **`x-pack/plugin/vector-tile/src/javaRestTest/java/org/elasticsearch/xpack/vectortile/VectorTileRestIT.java`** -> AI Confidence: **99.31%**
1263. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/common/http/HttpRequestTemplate.java`** -> AI Confidence: **99.31%**
1264. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/common/http/HttpResponse.java`** -> AI Confidence: **99.31%**
1265. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/input/InputRegistry.java`** -> AI Confidence: **99.31%**
1266. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/email/EmailTemplate.java`** -> AI Confidence: **99.31%**
1267. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/email/HtmlSanitizer.java`** -> AI Confidence: **99.31%**
1268. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/pagerduty/IncidentEvent.java`** -> AI Confidence: **99.31%**
1269. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/pagerduty/IncidentEventContext.java`** -> AI Confidence: **99.31%**
1270. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/slack/message/Attachment.java`** -> AI Confidence: **99.31%**
1271. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/slack/message/SlackMessage.java`** -> AI Confidence: **99.31%**
1272. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/support/XContentFilterKeysUtils.java`** -> AI Confidence: **99.31%**
1273. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/TriggerService.java`** -> AI Confidence: **99.31%**
1274. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/support/DayTimes.java`** -> AI Confidence: **99.31%**
1275. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/common/http/HttpRequestTests.java`** -> AI Confidence: **99.31%**
1276. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/notification/slack/message/SlackMessageTests.java`** -> AI Confidence: **99.31%**
1277. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/support/WatcherTemplateTests.java`** -> AI Confidence: **99.31%**
1278. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/support/search/WatcherSearchTemplateRequestTests.java`** -> AI Confidence: **99.31%**
1279. **`x-pack/plugin/write-load-forecaster/src/main/java/org/elasticsearch/xpack/writeloadforecaster/LicensedWriteLoadForecaster.java`** -> AI Confidence: **99.31%**
1280. **`x-pack/qa/full-cluster-restart/src/javaRestTest/java/org/elasticsearch/xpack/restart/FullClusterRestartIT.java`** -> AI Confidence: **99.31%**
1281. **`x-pack/qa/multi-node/src/javaRestTest/java/org/elasticsearch/multi_node/RollupIT.java`** -> AI Confidence: **99.31%**
1282. **`x-pack/qa/rolling-upgrade-multi-cluster/src/test/java/org/elasticsearch/upgrades/CcrRollingUpgradeIT.java`** -> AI Confidence: **99.31%**
1283. **`x-pack/qa/rolling-upgrade/src/test/java/org/elasticsearch/upgrades/DiskBBQVectorSearchIT.java`** -> AI Confidence: **99.31%**
1284. **`x-pack/qa/rolling-upgrade/src/test/java/org/elasticsearch/upgrades/IndexingIT.java`** -> AI Confidence: **99.31%**
1285. **`x-pack/qa/rolling-upgrade/src/test/java/org/elasticsearch/upgrades/MlTrainedModelsUpgradeIT.java`** -> AI Confidence: **99.31%**
1286. **`x-pack/qa/rolling-upgrade/src/test/java/org/elasticsearch/upgrades/SecurityIndexRolesMetadataMigrationIT.java`** -> AI Confidence: **99.31%**
1287. **`x-pack/qa/runtime-fields/with-security/src/javaRestTest/java/org/elasticsearch/xpack/security/PermissionsIT.java`** -> AI Confidence: **99.31%**
1288. **`build-tools-internal/src/integTest/groovy/org/elasticsearch/gradle/internal/SymbolicLinkPreservingTarFuncTest.groovy`** -> AI Confidence: **99.31%**
1289. **`build-tools-internal/src/main/groovy/elasticsearch.build-scan.gradle`** -> AI Confidence: **99.31%**
1290. **`build-tools-internal/src/main/groovy/elasticsearch.ide.gradle`** -> AI Confidence: **99.31%**
1291. **`libs/simdvec/native/src/vec/c/aarch64/score_1.cpp`** -> AI Confidence: **99.31%**
1292. **`libs/simdvec/native/src/vec/c/amd64/caps.cpp`** -> AI Confidence: **99.31%**
1293. **`libs/simdvec/native/src/vec/c/amd64/score_1.cpp`** -> AI Confidence: **99.31%**
1294. **`libs/simdvec/native/src/vec/c/amd64/vec_2.cpp`** -> AI Confidence: **99.31%**
1295. **`.buildkite/scripts/dra-workflow.sh`** -> AI Confidence: **99.29%**
1296. **`.buildkite/scripts/dra-workflow.trigger.sh`** -> AI Confidence: **99.29%**
1297. **`.buildkite/scripts/fwc-branches.sh`** -> AI Confidence: **99.29%**
1298. **`.buildkite/scripts/get-latest-test-mutes.sh`** -> AI Confidence: **99.29%**
1299. **`.buildkite/scripts/lucene-snapshot/update-branch.sh`** -> AI Confidence: **99.29%**
1300. **`.buildkite/scripts/run-pr-upgrade-tests.sh`** -> AI Confidence: **99.29%**
1301. **`.buildkite/scripts/setup-monitoring.sh`** -> AI Confidence: **99.29%**
1302. **`distribution/docker/src/docker/bin/docker-entrypoint.sh`** -> AI Confidence: **99.29%**
1303. **`distribution/packages/src/common/systemd/systemd-entrypoint`** -> AI Confidence: **99.29%**
1304. **`distribution/src/bin/elasticsearch-env`** -> AI Confidence: **99.29%**
1305. **`distribution/src/bin/elasticsearch-env-from-file`** -> AI Confidence: **99.29%**
1306. **`x-pack/test/idp-fixture/src/main/resources/oidc/entrypoint.sh`** -> AI Confidence: **99.29%**
1307. **`libs/h3/src/main/java/org/elasticsearch/h3/FastMath.java`** -> AI Confidence: **99.29%**
1308. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/action/PainlessContextTypeInfo.java`** -> AI Confidence: **99.29%**
1309. **`server/src/main/java/org/elasticsearch/common/time/DateUtilsRounding.java`** -> AI Confidence: **99.29%**
1310. **`server/src/main/java/org/elasticsearch/index/codec/bloomfilter/BloomFilterHashFunctions.java`** -> AI Confidence: **99.29%**
1311. **`server/src/test/java/org/elasticsearch/common/network/CIDRUtilsTests.java`** -> AI Confidence: **99.29%**
1312. **`server/src/test/java/org/elasticsearch/transport/TransportActionStatsTests.java`** -> AI Confidence: **99.29%**
1313. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/messages/Messages.java`** -> AI Confidence: **99.29%**
1314. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/transform/TransformMessages.java`** -> AI Confidence: **99.29%**
1315. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/MatchOnlyTextRollingUpgradeIT.java`** -> AI Confidence: **99.29%**
1316. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/PatternTextRollingUpgradeIT.java`** -> AI Confidence: **99.29%**
1317. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/TextRollingUpgradeIT.java`** -> AI Confidence: **99.29%**
1318. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/exporter/http/HttpHostBuilderTests.java`** -> AI Confidence: **99.29%**
1319. **`x-pack/plugin/security/qa/operator-privileges-tests/src/javaRestTest/java/org/elasticsearch/xpack/security/operator/Constants.java`** -> AI Confidence: **99.29%**
1320. **`build-tools-internal/src/main/groovy/elasticsearch.run-ccs.gradle`** -> AI Confidence: **99.29%**
1321. **`build-tools-internal/src/main/groovy/elasticsearch.run.gradle`** -> AI Confidence: **99.29%**
1322. **`build-tools-internal/src/test/groovy/org/elasticsearch/gradle/internal/doc/DocTestUtils.groovy`** -> AI Confidence: **99.29%**
1323. **`x-pack/plugin/esql/tools/build.gradle`** -> AI Confidence: **99.29%**
1324. **`distribution/docker/src/docker/dockerfiles/cloud_ess_fips/Dockerfile`** -> AI Confidence: **99.29%**
1325. **`distribution/docker/src/docker/dockerfiles/default/Dockerfile`** -> AI Confidence: **99.29%**
1326. **`distribution/docker/src/docker/dockerfiles/ironbank/Dockerfile`** -> AI Confidence: **99.29%**
1327. **`distribution/docker/src/docker/dockerfiles/wolfi/Dockerfile`** -> AI Confidence: **99.29%**
1328. **`x-pack/test/idp-fixture/src/main/resources/idp/Dockerfile`** -> AI Confidence: **99.29%**
1329. **`x-pack/test/idp-fixture/src/main/resources/nginx/Dockerfile`** -> AI Confidence: **99.29%**
1330. **`x-pack/test/smb-fixture/src/main/resources/Dockerfile`** -> AI Confidence: **99.29%**
1331. **`benchmarks/src/main/java/org/elasticsearch/benchmark/_nightly/esql/TopNBenchmark.java`** -> AI Confidence: **99.24%**
1332. **`benchmarks/src/main/java/org/elasticsearch/benchmark/_nightly/esql/ValuesSourceReaderBenchmark.java`** -> AI Confidence: **99.24%**
1333. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/EvalBenchmark.java`** -> AI Confidence: **99.24%**
1334. **`benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/ValuesAggregatorBenchmark.java`** -> AI Confidence: **99.24%**
1335. **`benchmarks/src/main/java/org/elasticsearch/benchmark/swisshash/BytesRefSwissHashBenchmark.java`** -> AI Confidence: **99.24%**
1336. **`benchmarks/src/main/java/org/elasticsearch/benchmark/swisshash/LongSwissHashBenchmark.java`** -> AI Confidence: **99.24%**
1337. **`benchmarks/src/main/java/org/elasticsearch/benchmark/vector/scorer/VectorScorerDistanceFunctionBenchmark.java`** -> AI Confidence: **99.24%**
1338. **`benchmarks/src/test/java/org/elasticsearch/benchmark/vector/scorer/VectorScorerBFloat16OperationBenchmarkTests.java`** -> AI Confidence: **99.24%**
1339. **`benchmarks/src/test/java/org/elasticsearch/benchmark/vector/scorer/VectorScorerByteBulkBenchmarkTests.java`** -> AI Confidence: **99.24%**
1340. **`benchmarks/src/test/java/org/elasticsearch/benchmark/vector/scorer/VectorScorerFloatBulkBenchmarkTests.java`** -> AI Confidence: **99.24%**
1341. **`benchmarks/src/test/java/org/elasticsearch/benchmark/vector/scorer/VectorScorerInt7uBulkBenchmarkTests.java`** -> AI Confidence: **99.24%**
1342. **`build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/SnippetLengthCheck.java`** -> AI Confidence: **99.24%**
1343. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalDistributionBwcSetupPlugin.java`** -> AI Confidence: **99.24%**
1344. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/Jdk.java`** -> AI Confidence: **99.24%**
1345. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/feature/FeatureInjector.java`** -> AI Confidence: **99.24%**
1346. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/toolchain/OracleOpenJdkToolchainResolver.java`** -> AI Confidence: **99.24%**
1347. **`build-tools/src/main/java/org/elasticsearch/gradle/testclusters/ElasticsearchNode.java`** -> AI Confidence: **99.24%**
1348. **`build-tools/src/main/java/org/elasticsearch/gradle/testclusters/MockApmServer.java`** -> AI Confidence: **99.24%**
1349. **`build-tools/src/main/java/org/elasticsearch/gradle/util/GradleUtils.java`** -> AI Confidence: **99.24%**
1350. **`client/rest/src/test/java/org/elasticsearch/client/RequestLoggerTests.java`** -> AI Confidence: **99.24%**
1351. **`client/rest/src/test/java/org/elasticsearch/client/RequestOptionsTests.java`** -> AI Confidence: **99.24%**
1352. **`client/rest/src/test/java/org/elasticsearch/client/RequestTests.java`** -> AI Confidence: **99.24%**
1353. **`client/rest/src/test/java/org/elasticsearch/client/RestClientSingleHostTests.java`** -> AI Confidence: **99.24%**
1354. **`client/sniffer/src/test/java/org/elasticsearch/client/sniff/ElasticsearchNodesSnifferTests.java`** -> AI Confidence: **99.24%**
1355. **`distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/AddStringKeyStoreCommand.java`** -> AI Confidence: **99.24%**
1356. **`distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/PluginsConfig.java`** -> AI Confidence: **99.24%**
1357. **`distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/RemovePluginAction.java`** -> AI Confidence: **99.24%**
1358. **`distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/ListPluginsCommandTests.java`** -> AI Confidence: **99.24%**
1359. **`distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/JvmErgonomics.java`** -> AI Confidence: **99.24%**
1360. **`distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/MachineDependentHeap.java`** -> AI Confidence: **99.24%**
1361. **`distribution/tools/server-launcher/src/main/java/org/elasticsearch/server/launcher/ErrorPumpThread.java`** -> AI Confidence: **99.24%**
1362. **`libs/cli/src/main/java/org/elasticsearch/cli/CliToolProvider.java`** -> AI Confidence: **99.24%**
1363. **`libs/core/src/main/java/org/elasticsearch/core/internal/provider/EmbeddedImplClassLoader.java`** -> AI Confidence: **99.24%**
1364. **`libs/core/src/main/java/org/elasticsearch/core/internal/provider/EmbeddedModulePath.java`** -> AI Confidence: **99.24%**
1365. **`libs/core/src/main/java/org/elasticsearch/jdk/JarHell.java`** -> AI Confidence: **99.24%**
1366. **`libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/AbstractEntitlementsIT.java`** -> AI Confidence: **99.24%**
1367. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java`** -> AI Confidence: **99.24%**
1368. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyUtils.java`** -> AI Confidence: **99.24%**
1369. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/FilesEntitlement.java`** -> AI Confidence: **99.24%**
1370. **`libs/entitlement/src/test/java/org/elasticsearch/entitlement/rules/EntitlementRulesBuilderTests.java`** -> AI Confidence: **99.24%**
1371. **`libs/entitlement/tools/jdk-api-extractor/src/main/java/org/elasticsearch/entitlement/tools/jdkapi/JdkApiExtractor.java`** -> AI Confidence: **99.24%**
1372. **`libs/entitlement/tools/securitymanager-scanner/src/main/java/org/elasticsearch/entitlement/tools/securitymanager/scanner/Main.java`** -> AI Confidence: **99.24%**
1373. **`libs/exponential-histogram/src/test/java/org/elasticsearch/exponentialhistogram/ExponentialHistogramBuilderTests.java`** -> AI Confidence: **99.24%**
1374. **`libs/exponential-histogram/src/test/java/org/elasticsearch/exponentialhistogram/ExponentialHistogramMergerTests.java`** -> AI Confidence: **99.24%**
1375. **`libs/geo/src/main/java/org/elasticsearch/geometry/simplify/GeometrySimplifier.java`** -> AI Confidence: **99.24%**
1376. **`libs/geo/src/main/java/org/elasticsearch/geometry/utils/WellKnownText.java`** -> AI Confidence: **99.24%**
1377. **`libs/geo/src/test/java/org/elasticsearch/geometry/utils/SpatialEnvelopeVisitorTests.java`** -> AI Confidence: **99.24%**
1378. **`libs/gpu-codec/src/main/java/org/elasticsearch/gpu/codec/ES92GpuHnswVectorsWriter.java`** -> AI Confidence: **99.24%**
1379. **`libs/lz4/src/main/java/org/elasticsearch/lz4/LZ4SafeUtils.java`** -> AI Confidence: **99.24%**
1380. **`libs/native/src/main/java/org/elasticsearch/nativeaccess/PosixNativeAccess.java`** -> AI Confidence: **99.24%**
1381. **`libs/native/src/main/java/org/elasticsearch/nativeaccess/WindowsNativeAccess.java`** -> AI Confidence: **99.24%**
1382. **`libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkVectorLibrary.java`** -> AI Confidence: **99.24%**
1383. **`libs/native/src/test/java/org/elasticsearch/nativeaccess/jdk/JDKVectorLibraryBFloat16Tests.java`** -> AI Confidence: **99.24%**
1384. **`libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/Int4Corrections.java`** -> AI Confidence: **99.24%**
1385. **`libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/vectorization/PanamaESVectorUtilSupport.java`** -> AI Confidence: **99.24%**
1386. **`libs/simdvec/src/test/java/org/elasticsearch/simdvec/internal/vectorization/ES92Int7VectorScorerTests.java`** -> AI Confidence: **99.24%**
1387. **`libs/ssl-config/src/test/java/org/elasticsearch/common/ssl/SslConfigurationLoaderTests.java`** -> AI Confidence: **99.24%**
1388. **`libs/tdigest/src/main/java/org/elasticsearch/tdigest/MergingDigest.java`** -> AI Confidence: **99.24%**
1389. **`libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java`** -> AI Confidence: **99.24%**
1390. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/ConstructingObjectParser.java`** -> AI Confidence: **99.24%**
1391. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/NamedXContentRegistry.java`** -> AI Confidence: **99.24%**
1392. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java`** -> AI Confidence: **99.24%**
1393. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentFactory.java`** -> AI Confidence: **99.24%**
1394. **`libs/x-content/src/main/java/org/elasticsearch/xcontent/support/MapXContentParser.java`** -> AI Confidence: **99.24%**
1395. **`libs/x-content/src/test/java/org/elasticsearch/xcontent/ConstructingObjectParserTests.java`** -> AI Confidence: **99.24%**
1396. **`libs/x-content/src/test/java/org/elasticsearch/xcontent/MapXContentParserTests.java`** -> AI Confidence: **99.24%**
1397. **`libs/x-content/src/test/java/org/elasticsearch/xcontent/ObjectParserTests.java`** -> AI Confidence: **99.24%**
1398. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/AggregationsPlugin.java`** -> AI Confidence: **99.24%**
1399. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/metric/InternalMatrixStats.java`** -> AI Confidence: **99.24%**
1400. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/metric/RunningStats.java`** -> AI Confidence: **99.24%**
1401. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/pipeline/BucketSelectorPipelineAggregationBuilder.java`** -> AI Confidence: **99.24%**
1402. **`modules/aggregations/src/main/java/org/elasticsearch/aggregations/pipeline/DerivativePipelineAggregationBuilder.java`** -> AI Confidence: **99.24%**
1403. **`modules/aggregations/src/test/java/org/elasticsearch/aggregations/pipeline/DerivativeAggregatorTests.java`** -> AI Confidence: **99.24%**
1404. **`modules/analysis-common/src/main/java/org/elasticsearch/analysis/common/MappingCharFilterFactory.java`** -> AI Confidence: **99.24%**
1405. **`modules/analysis-common/src/main/java/org/elasticsearch/analysis/common/WordDelimiterTokenFilterFactory.java`** -> AI Confidence: **99.24%**
1406. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/DataStreamUpgradeRestIT.java`** -> AI Confidence: **99.24%**
1407. **`modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/MultiClustersIT.java`** -> AI Confidence: **99.24%**
1408. **`modules/data-streams/src/main/java/org/elasticsearch/datastreams/action/TransportGetDataStreamsAction.java`** -> AI Confidence: **99.24%**
1409. **`modules/data-streams/src/test/java/org/elasticsearch/datastreams/lifecycle/action/DataStreamLifecycleStatsResponseTests.java`** -> AI Confidence: **99.24%**
1410. **`modules/dot-prefix-validation/src/main/java/org/elasticsearch/validation/DotPrefixValidator.java`** -> AI Confidence: **99.24%**
1411. **`modules/ingest-attachment/src/test/java/org/elasticsearch/ingest/attachment/TikaDocTests.java`** -> AI Confidence: **99.24%**
1412. **`modules/ingest-common/src/internalClusterTest/java/org/elasticsearch/ingest/common/IngestRestartIT.java`** -> AI Confidence: **99.24%**
1413. **`modules/ingest-common/src/main/java/org/elasticsearch/ingest/common/ConvertProcessor.java`** -> AI Confidence: **99.24%**
1414. **`modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/CefProcessorTests.java`** -> AI Confidence: **99.24%**
1415. **`modules/ingest-geoip/qa/file-based-update/src/javaRestTest/java/org/elasticsearch/ingest/geoip/UpdateDatabasesIT.java`** -> AI Confidence: **99.24%**
1416. **`modules/ingest-geoip/qa/geoip-reindexed/src/javaRestTest/java/org/elasticsearch/ingest/geoip/GeoIpReindexedIT.java`** -> AI Confidence: **99.24%**
1417. **`modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloaderTaskExecutor.java`** -> AI Confidence: **99.24%**
1418. **`modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpProcessor.java`** -> AI Confidence: **99.24%**
1419. **`modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/IpinfoIpDataLookups.java`** -> AI Confidence: **99.24%**
1420. **`modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/MaxMindSupportTests.java`** -> AI Confidence: **99.24%**
1421. **`modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/direct/DatabaseConfigurationTests.java`** -> AI Confidence: **99.24%**
1422. **`modules/lang-mustache/src/internalClusterTest/java/org/elasticsearch/script/mustache/SearchTemplateIT.java`** -> AI Confidence: **99.24%**
1423. **`modules/lang-mustache/src/test/java/org/elasticsearch/script/mustache/MustacheTests.java`** -> AI Confidence: **99.24%**
1424. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/Def.java`** -> AI Confidence: **99.24%**
1425. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/ScriptClassInfo.java`** -> AI Confidence: **99.24%**
1426. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/phase/DefaultConstantFoldingOptimizationPhase.java`** -> AI Confidence: **99.24%**
1427. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/phase/DefaultSemanticAnalysisPhase.java`** -> AI Confidence: **99.24%**
1428. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/phase/PainlessSemanticHeaderPhase.java`** -> AI Confidence: **99.24%**
1429. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/symbol/FunctionTable.java`** -> AI Confidence: **99.24%**
1430. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/GeoShapeType.java`** -> AI Confidence: **99.24%**
1431. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/builders/GeometryCollectionBuilder.java`** -> AI Confidence: **99.24%**
1432. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/builders/LineStringBuilder.java`** -> AI Confidence: **99.24%**
1433. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/parsers/GeoWKTParser.java`** -> AI Confidence: **99.24%**
1434. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/parsers/ShapeParser.java`** -> AI Confidence: **99.24%**
1435. **`modules/legacy-geo/src/main/java/org/elasticsearch/legacygeo/query/LegacyGeoShapeQueryProcessor.java`** -> AI Confidence: **99.24%**
1436. **`modules/legacy-geo/src/test/java/org/elasticsearch/legacygeo/test/RandomShapeGenerator.java`** -> AI Confidence: **99.24%**
1437. **`modules/mapper-extras/src/test/java/org/elasticsearch/index/mapper/extras/RankFeatureQueryBuilderTests.java`** -> AI Confidence: **99.24%**
1438. **`modules/parent-join/src/main/java/org/elasticsearch/join/ParentJoinPlugin.java`** -> AI Confidence: **99.24%**
1439. **`modules/percolator/src/test/java/org/elasticsearch/percolator/PercolatorQuerySearchTests.java`** -> AI Confidence: **99.24%**
1440. **`modules/reindex-management/src/javaRestTest/java/org/elasticsearch/reindex/management/ReindexRemoteIT.java`** -> AI Confidence: **99.24%**
1441. **`modules/reindex-management/src/main/java/org/elasticsearch/reindex/management/GetReindexResponse.java`** -> AI Confidence: **99.24%**
1442. **`modules/reindex/src/javaRestTest/java/org/elasticsearch/index/reindex/remote/ReindexFromOldRemoteIT.java`** -> AI Confidence: **99.24%**
1443. **`modules/repository-azure/src/main/java/org/elasticsearch/repositories/azure/AzureStorageSettings.java`** -> AI Confidence: **99.24%**
1444. **`modules/repository-gcs/src/main/java/org/elasticsearch/repositories/gcs/GoogleCloudStorageBlobStore.java`** -> AI Confidence: **99.24%**
1445. **`modules/repository-gcs/src/main/java/org/elasticsearch/repositories/gcs/GoogleCloudStorageRetryingInputStream.java`** -> AI Confidence: **99.24%**
1446. **`modules/repository-gcs/src/test/java/org/elasticsearch/repositories/gcs/GoogleCloudStorageClientSettingsTests.java`** -> AI Confidence: **99.24%**
1447. **`modules/repository-s3/src/test/java/org/elasticsearch/repositories/s3/S3ClientSettingsTests.java`** -> AI Confidence: **99.24%**
1448. **`modules/rest-root/src/test/java/org/elasticsearch/rest/root/MainResponseTests.java`** -> AI Confidence: **99.24%**
1449. **`modules/transport-netty4/src/main/java/org/elasticsearch/http/netty4/Netty4HttpRequestBodyStream.java`** -> AI Confidence: **99.24%**
1450. **`modules/user-agent/src/main/java/org/elasticsearch/useragent/UserAgentParserImpl.java`** -> AI Confidence: **99.24%**
1451. **`plugins/analysis-icu/src/internalClusterTest/java/org/elasticsearch/index/mapper/ICUCollationKeywordFieldMapperIT.java`** -> AI Confidence: **99.24%**
1452. **`plugins/analysis-icu/src/test/java/org/elasticsearch/plugin/analysis/icu/IndexableBinaryStringToolsTests.java`** -> AI Confidence: **99.24%**
1453. **`plugins/analysis-kuromoji/src/main/java/org/elasticsearch/plugin/analysis/kuromoji/AnalysisKuromojiPlugin.java`** -> AI Confidence: **99.24%**
1454. **`plugins/analysis-phonetic/src/main/java/org/elasticsearch/plugin/analysis/phonetic/PhoneticTokenFilterFactory.java`** -> AI Confidence: **99.24%**
1455. **`plugins/mapper-annotated-text/src/main/java/org/elasticsearch/index/mapper/annotatedtext/AnnotatedPassageFormatter.java`** -> AI Confidence: **99.24%**
1456. **`qa/ccs-rolling-upgrade-remote-cluster/src/test/java/org/elasticsearch/upgrades/AggregationsIT.java`** -> AI Confidence: **99.24%**
1457. **`qa/evil-tests/src/test/java/org/elasticsearch/monitor/os/EvilOsProbeTests.java`** -> AI Confidence: **99.24%**
1458. **`qa/full-cluster-restart/src/javaRestTest/java/org/elasticsearch/upgrades/FullClusterRestartIT.java`** -> AI Confidence: **99.24%**
1459. **`qa/packaging/src/test/java/org/elasticsearch/packaging/test/PackagingTestCase.java`** -> AI Confidence: **99.24%**
1460. **`qa/packaging/src/test/java/org/elasticsearch/packaging/test/WindowsServiceTests.java`** -> AI Confidence: **99.24%**
1461. **`qa/packaging/src/test/java/org/elasticsearch/packaging/util/docker/DockerRun.java`** -> AI Confidence: **99.24%**
1462. **`qa/repository-multi-version/src/test/java/org/elasticsearch/upgrades/MultiVersionRepositoryAccessIT.java`** -> AI Confidence: **99.24%**
1463. **`qa/restricted-loggers/src/test/java/org/elasticsearch/common/logging/LoggersTests.java`** -> AI Confidence: **99.24%**
1464. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/FeatureUpgradeIT.java`** -> AI Confidence: **99.24%**
1465. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/FieldCapsIT.java`** -> AI Confidence: **99.24%**
1466. **`qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/SystemIndicesUpgradeIT.java`** -> AI Confidence: **99.24%**
1467. **`qa/smoke-test-http/src/internalClusterTest/java/org/elasticsearch/http/PrevalidateNodeRemovalRestIT.java`** -> AI Confidence: **99.24%**
1468. **`server/src/internalClusterTest/java/org/elasticsearch/action/admin/cluster/allocation/ClusterAllocationExplainIT.java`** -> AI Confidence: **99.24%**
1469. **`server/src/internalClusterTest/java/org/elasticsearch/action/admin/cluster/repositories/RepositoryBlocksIT.java`** -> AI Confidence: **99.24%**
1470. **`server/src/internalClusterTest/java/org/elasticsearch/action/admin/cluster/snapshots/SnapshotBlocksIT.java`** -> AI Confidence: **99.24%**
1471. **`server/src/internalClusterTest/java/org/elasticsearch/action/bulk/BulkProcessor2RetryIT.java`** -> AI Confidence: **99.24%**
1472. **`server/src/internalClusterTest/java/org/elasticsearch/action/bulk/IncrementalBulkIT.java`** -> AI Confidence: **99.24%**
1473. **`server/src/internalClusterTest/java/org/elasticsearch/action/search/PointInTimeIT.java`** -> AI Confidence: **99.24%**
1474. **`server/src/internalClusterTest/java/org/elasticsearch/blocks/SimpleBlocksIT.java`** -> AI Confidence: **99.24%**
1475. **`server/src/internalClusterTest/java/org/elasticsearch/cluster/ClusterStateDiffIT.java`** -> AI Confidence: **99.24%**
1476. **`server/src/internalClusterTest/java/org/elasticsearch/cluster/routing/allocation/decider/MockDiskUsagesIT.java`** -> AI Confidence: **99.24%**
1477. **`server/src/internalClusterTest/java/org/elasticsearch/cluster/shards/ClusterShardLimitIT.java`** -> AI Confidence: **99.24%**
1478. **`server/src/internalClusterTest/java/org/elasticsearch/discovery/ClusterDisruptionIT.java`** -> AI Confidence: **99.24%**
1479. **`server/src/internalClusterTest/java/org/elasticsearch/get/GetActionIT.java`** -> AI Confidence: **99.24%**
1480. **`server/src/internalClusterTest/java/org/elasticsearch/indices/IndicesRequestCacheIT.java`** -> AI Confidence: **99.24%**
1481. **`server/src/internalClusterTest/java/org/elasticsearch/indices/template/ComposableTemplateIT.java`** -> AI Confidence: **99.24%**
1482. **`server/src/internalClusterTest/java/org/elasticsearch/ingest/IngestStatsNamesAndTypesIT.java`** -> AI Confidence: **99.24%**
1483. **`server/src/internalClusterTest/java/org/elasticsearch/monitor/metrics/NodeIndexingMetricsIT.java`** -> AI Confidence: **99.24%**
1484. **`server/src/internalClusterTest/java/org/elasticsearch/recovery/FullRollingRestartIT.java`** -> AI Confidence: **99.24%**
1485. **`server/src/internalClusterTest/java/org/elasticsearch/recovery/RelocationIT.java`** -> AI Confidence: **99.24%**
1486. **`server/src/internalClusterTest/java/org/elasticsearch/routing/PartitionedRoutingIT.java`** -> AI Confidence: **99.24%**
1487. **`server/src/internalClusterTest/java/org/elasticsearch/search/aggregations/bucket/IpRangeIT.java`** -> AI Confidence: **99.24%**
1488. **`server/src/internalClusterTest/java/org/elasticsearch/search/aggregations/pipeline/BucketScriptIT.java`** -> AI Confidence: **99.24%**
1489. **`server/src/internalClusterTest/java/org/elasticsearch/search/aggregations/pipeline/PercentilesBucketIT.java`** -> AI Confidence: **99.24%**
1490. **`server/src/internalClusterTest/java/org/elasticsearch/search/geo/GeoPointScriptDocValuesIT.java`** -> AI Confidence: **99.24%**
1491. **`server/src/internalClusterTest/java/org/elasticsearch/search/sort/FieldSortIT.java`** -> AI Confidence: **99.24%**
1492. **`server/src/internalClusterTest/java/org/elasticsearch/snapshots/SnapshotThrottlingIT.java`** -> AI Confidence: **99.24%**
1493. **`server/src/internalClusterTest/java/org/elasticsearch/threadpool/SimpleThreadPoolIT.java`** -> AI Confidence: **99.24%**
1494. **`server/src/main/java/org/elasticsearch/ElasticsearchException.java`** -> AI Confidence: **99.24%**
1495. **`server/src/main/java/org/elasticsearch/action/admin/cluster/shards/ClusterSearchShardsResponse.java`** -> AI Confidence: **99.24%**
1496. **`server/src/main/java/org/elasticsearch/action/admin/cluster/snapshots/create/CreateSnapshotRequest.java`** -> AI Confidence: **99.24%**
1497. **`server/src/main/java/org/elasticsearch/action/admin/cluster/snapshots/restore/RestoreSnapshotRequest.java`** -> AI Confidence: **99.24%**
1498. **`server/src/main/java/org/elasticsearch/action/admin/cluster/stats/AnalysisStats.java`** -> AI Confidence: **99.24%**
1499. **`server/src/main/java/org/elasticsearch/action/admin/cluster/stats/CCSTelemetrySnapshot.java`** -> AI Confidence: **99.24%**
1500. **`server/src/main/java/org/elasticsearch/action/admin/indices/alias/Alias.java`** -> AI Confidence: **99.24%**
1501. **`server/src/main/java/org/elasticsearch/action/admin/indices/rollover/RolloverConfiguration.java`** -> AI Confidence: **99.24%**
1502. **`server/src/main/java/org/elasticsearch/action/admin/indices/shrink/ResizeNumberOfShardsCalculator.java`** -> AI Confidence: **99.24%**
1503. **`server/src/main/java/org/elasticsearch/action/bulk/BulkRequestModifier.java`** -> AI Confidence: **99.24%**
1504. **`server/src/main/java/org/elasticsearch/action/bulk/TransportAbstractBulkAction.java`** -> AI Confidence: **99.24%**
1505. **`server/src/main/java/org/elasticsearch/action/datastreams/autosharding/DataStreamAutoShardingService.java`** -> AI Confidence: **99.24%**
1506. **`server/src/main/java/org/elasticsearch/action/fieldcaps/FieldCapabilities.java`** -> AI Confidence: **99.24%**
1507. **`server/src/main/java/org/elasticsearch/action/fieldcaps/RequestDispatcher.java`** -> AI Confidence: **99.24%**
1508. **`server/src/main/java/org/elasticsearch/action/ingest/GetPipelineResponse.java`** -> AI Confidence: **99.24%**
1509. **`server/src/main/java/org/elasticsearch/action/ingest/SimulateProcessorResult.java`** -> AI Confidence: **99.24%**
1510. **`server/src/main/java/org/elasticsearch/action/search/ClearScrollController.java`** -> AI Confidence: **99.24%**
1511. **`server/src/main/java/org/elasticsearch/action/search/SearchRequest.java`** -> AI Confidence: **99.24%**
1512. **`server/src/main/java/org/elasticsearch/action/search/SearchResponse.java`** -> AI Confidence: **99.24%**
1513. **`server/src/main/java/org/elasticsearch/action/search/SearchShardsResponse.java`** -> AI Confidence: **99.24%**
1514. **`server/src/main/java/org/elasticsearch/action/search/SearchTaskWatchdog.java`** -> AI Confidence: **99.24%**
1515. **`server/src/main/java/org/elasticsearch/action/support/ActiveShardCount.java`** -> AI Confidence: **99.24%**
1516. **`server/src/main/java/org/elasticsearch/action/support/AutoCreateIndex.java`** -> AI Confidence: **99.24%**
1517. **`server/src/main/java/org/elasticsearch/action/support/master/TransportMasterNodeAction.java`** -> AI Confidence: **99.24%**
1518. **`server/src/main/java/org/elasticsearch/action/support/replication/PendingReplicationActions.java`** -> AI Confidence: **99.24%**
1519. **`server/src/main/java/org/elasticsearch/action/support/replication/PostWriteRefresh.java`** -> AI Confidence: **99.24%**
1520. **`server/src/main/java/org/elasticsearch/action/support/replication/ReplicationResponse.java`** -> AI Confidence: **99.24%**
1521. **`server/src/main/java/org/elasticsearch/action/termvectors/MultiTermVectorsRequest.java`** -> AI Confidence: **99.24%**
1522. **`server/src/main/java/org/elasticsearch/action/termvectors/TermVectorsRequest.java`** -> AI Confidence: **99.24%**
1523. **`server/src/main/java/org/elasticsearch/cluster/ClusterInfo.java`** -> AI Confidence: **99.24%**
1524. **`server/src/main/java/org/elasticsearch/cluster/ClusterStateObserver.java`** -> AI Confidence: **99.24%**
1525. **`server/src/main/java/org/elasticsearch/cluster/DiskUsage.java`** -> AI Confidence: **99.24%**
1526. **`server/src/main/java/org/elasticsearch/cluster/SnapshotsInProgress.java`** -> AI Confidence: **99.24%**
1527. **`server/src/main/java/org/elasticsearch/cluster/coordination/CoordinationDiagnosticsService.java`** -> AI Confidence: **99.24%**
1528. **`server/src/main/java/org/elasticsearch/cluster/coordination/Coordinator.java`** -> AI Confidence: **99.24%**
1529. **`server/src/main/java/org/elasticsearch/cluster/coordination/NodeJoinExecutor.java`** -> AI Confidence: **99.24%**
1530. **`server/src/main/java/org/elasticsearch/cluster/coordination/Reconfigurator.java`** -> AI Confidence: **99.24%**
1531. **`server/src/main/java/org/elasticsearch/cluster/coordination/RemoveCustomsCommand.java`** -> AI Confidence: **99.24%**
1532. **`server/src/main/java/org/elasticsearch/cluster/metadata/DataStreamFailureStore.java`** -> AI Confidence: **99.24%**
1533. **`server/src/main/java/org/elasticsearch/cluster/metadata/DataStreamGlobalRetentionSettings.java`** -> AI Confidence: **99.24%**
1534. **`server/src/main/java/org/elasticsearch/cluster/metadata/DataStreamLifecycle.java`** -> AI Confidence: **99.24%**
1535. **`server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java`** -> AI Confidence: **99.24%**
1536. **`server/src/main/java/org/elasticsearch/cluster/metadata/IndexWriteLoad.java`** -> AI Confidence: **99.24%**
1537. **`server/src/main/java/org/elasticsearch/cluster/metadata/InferenceFieldMetadata.java`** -> AI Confidence: **99.24%**
1538. **`server/src/main/java/org/elasticsearch/cluster/metadata/MetadataIndexTemplateService.java`** -> AI Confidence: **99.24%**
1539. **`server/src/main/java/org/elasticsearch/cluster/metadata/MetadataUpdateSettingsService.java`** -> AI Confidence: **99.24%**
1540. **`server/src/main/java/org/elasticsearch/cluster/routing/OperationRouting.java`** -> AI Confidence: **99.24%**
1541. **`server/src/main/java/org/elasticsearch/cluster/routing/RoutingHashBuilder.java`** -> AI Confidence: **99.24%**
1542. **`server/src/main/java/org/elasticsearch/cluster/routing/RoutingNode.java`** -> AI Confidence: **99.24%**
1543. **`server/src/main/java/org/elasticsearch/cluster/routing/UnassignedInfo.java`** -> AI Confidence: **99.24%**
1544. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/AbstractAllocationDecision.java`** -> AI Confidence: **99.24%**
1545. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/AllocationService.java`** -> AI Confidence: **99.24%**
1546. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/allocator/DesiredBalanceMetrics.java`** -> AI Confidence: **99.24%**
1547. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/allocator/DesiredBalanceReconciler.java`** -> AI Confidence: **99.24%**
1548. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/allocator/WeightFunction.java`** -> AI Confidence: **99.24%**
1549. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/command/MoveAllocationCommand.java`** -> AI Confidence: **99.24%**
1550. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/AllocationDeciders.java`** -> AI Confidence: **99.24%**
1551. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/AwarenessAllocationDecider.java`** -> AI Confidence: **99.24%**
1552. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/ClusterRebalanceAllocationDecider.java`** -> AI Confidence: **99.24%**
1553. **`server/src/main/java/org/elasticsearch/cluster/routing/allocation/decider/Decision.java`** -> AI Confidence: **99.24%**
1554. **`server/src/main/java/org/elasticsearch/common/geo/GeoJson.java`** -> AI Confidence: **99.24%**
1555. **`server/src/main/java/org/elasticsearch/common/geo/GeoPolygonDecomposer.java`** -> AI Confidence: **99.24%**
1556. **`server/src/main/java/org/elasticsearch/common/geo/SimpleFeatureFactory.java`** -> AI Confidence: **99.24%**
1557. **`server/src/main/java/org/elasticsearch/common/io/FileSystemUtils.java`** -> AI Confidence: **99.24%**
1558. **`server/src/main/java/org/elasticsearch/common/io/stream/StreamOutput.java`** -> AI Confidence: **99.24%**
1559. **`server/src/main/java/org/elasticsearch/common/logging/Loggers.java`** -> AI Confidence: **99.24%**
1560. **`server/src/main/java/org/elasticsearch/common/lucene/index/FreqTermsEnum.java`** -> AI Confidence: **99.24%**
1561. **`server/src/main/java/org/elasticsearch/common/lucene/search/MultiPhrasePrefixQuery.java`** -> AI Confidence: **99.24%**
1562. **`server/src/main/java/org/elasticsearch/common/lucene/search/function/FunctionScoreQuery.java`** -> AI Confidence: **99.24%**
1563. **`server/src/main/java/org/elasticsearch/common/lucene/uid/VersionsAndSeqNoResolver.java`** -> AI Confidence: **99.24%**
1564. **`server/src/main/java/org/elasticsearch/common/network/NetworkUtils.java`** -> AI Confidence: **99.24%**
1565. **`server/src/main/java/org/elasticsearch/common/scheduler/SchedulerEngine.java`** -> AI Confidence: **99.24%**
1566. **`server/src/main/java/org/elasticsearch/common/settings/Settings.java`** -> AI Confidence: **99.24%**
1567. **`server/src/main/java/org/elasticsearch/common/time/DateFormatter.java`** -> AI Confidence: **99.24%**
1568. **`server/src/main/java/org/elasticsearch/common/time/DateFormatters.java`** -> AI Confidence: **99.24%**
1569. **`server/src/main/java/org/elasticsearch/common/time/JavaDateFormatter.java`** -> AI Confidence: **99.24%**
1570. **`server/src/main/java/org/elasticsearch/common/unit/Fuzziness.java`** -> AI Confidence: **99.24%**
1571. **`server/src/main/java/org/elasticsearch/common/util/CancellableSingleObjectCache.java`** -> AI Confidence: **99.24%**
1572. **`server/src/main/java/org/elasticsearch/common/util/CollectionUtils.java`** -> AI Confidence: **99.24%**
1573. **`server/src/main/java/org/elasticsearch/common/util/concurrent/AbstractAsyncTask.java`** -> AI Confidence: **99.24%**
1574. **`server/src/main/java/org/elasticsearch/common/util/set/Sets.java`** -> AI Confidence: **99.24%**
1575. **`server/src/main/java/org/elasticsearch/common/xcontent/XContentParserUtils.java`** -> AI Confidence: **99.24%**
1576. **`server/src/main/java/org/elasticsearch/discovery/PeerFinder.java`** -> AI Confidence: **99.24%**
1577. **`server/src/main/java/org/elasticsearch/gateway/GatewayMetaState.java`** -> AI Confidence: **99.24%**
1578. **`server/src/main/java/org/elasticsearch/health/HealthPeriodicLogger.java`** -> AI Confidence: **99.24%**
1579. **`server/src/main/java/org/elasticsearch/health/HealthService.java`** -> AI Confidence: **99.24%**
1580. **`server/src/main/java/org/elasticsearch/health/node/HealthInfo.java`** -> AI Confidence: **99.24%**
1581. **`server/src/main/java/org/elasticsearch/http/AbstractHttpServerTransport.java`** -> AI Confidence: **99.24%**
1582. **`server/src/main/java/org/elasticsearch/http/HttpClientStatsTracker.java`** -> AI Confidence: **99.24%**
1583. **`server/src/main/java/org/elasticsearch/index/MergePolicyConfig.java`** -> AI Confidence: **99.24%**
1584. **`server/src/main/java/org/elasticsearch/index/SearchSlowLog.java`** -> AI Confidence: **99.24%**
1585. **`server/src/main/java/org/elasticsearch/index/codec/postings/Lucene90BlockTreeTermsWriter.java`** -> AI Confidence: **99.24%**
1586. **`server/src/main/java/org/elasticsearch/index/codec/tsdb/PrefixedPartitionsWriter.java`** -> AI Confidence: **99.24%**
1587. **`server/src/main/java/org/elasticsearch/index/codec/tsdb/TSDBSyntheticIdDocValuesHolder.java`** -> AI Confidence: **99.24%**
1588. **`server/src/main/java/org/elasticsearch/index/codec/tsdb/es819/ES819TSDBDocValuesConsumer.java`** -> AI Confidence: **99.24%**
1589. **`server/src/main/java/org/elasticsearch/index/codec/vectors/diskbbq/IVFVectorsWriter.java`** -> AI Confidence: **99.24%**
1590. **`server/src/main/java/org/elasticsearch/index/codec/vectors/diskbbq/Preconditioner.java`** -> AI Confidence: **99.24%**
1591. **`server/src/main/java/org/elasticsearch/index/engine/FlushListeners.java`** -> AI Confidence: **99.24%**
1592. **`server/src/main/java/org/elasticsearch/index/engine/LazySoftDeletesDirectoryReaderWrapper.java`** -> AI Confidence: **99.24%**
1593. **`server/src/main/java/org/elasticsearch/index/engine/LuceneChangesSnapshot.java`** -> AI Confidence: **99.24%**
1594. **`server/src/main/java/org/elasticsearch/index/engine/LuceneSyntheticSourceChangesSnapshot.java`** -> AI Confidence: **99.24%**
1595. **`server/src/main/java/org/elasticsearch/index/engine/MergeMemoryEstimator.java`** -> AI Confidence: **99.24%**
1596. **`server/src/main/java/org/elasticsearch/index/engine/ThreadPoolMergeScheduler.java`** -> AI Confidence: **99.24%**
1597. **`server/src/main/java/org/elasticsearch/index/fielddata/IndexFieldData.java`** -> AI Confidence: **99.24%**
1598. **`server/src/main/java/org/elasticsearch/index/mapper/AbstractPointGeometryFieldMapper.java`** -> AI Confidence: **99.24%**
1599. **`server/src/main/java/org/elasticsearch/index/mapper/BooleanScriptFieldType.java`** -> AI Confidence: **99.24%**
1600. **`server/src/main/java/org/elasticsearch/index/mapper/DotExpandingXContentParser.java`** -> AI Confidence: **99.24%**
1601. **`server/src/main/java/org/elasticsearch/index/mapper/FieldMapper.java`** -> AI Confidence: **99.24%**
1602. **`server/src/main/java/org/elasticsearch/index/mapper/LuceneDocument.java`** -> AI Confidence: **99.24%**
1603. **`server/src/main/java/org/elasticsearch/index/mapper/MappingParser.java`** -> AI Confidence: **99.24%**
1604. **`server/src/main/java/org/elasticsearch/index/mapper/NumberFieldMapper.java`** -> AI Confidence: **99.24%**
1605. **`server/src/main/java/org/elasticsearch/index/mapper/RoutingPathFields.java`** -> AI Confidence: **99.24%**
1606. **`server/src/main/java/org/elasticsearch/index/mapper/RuntimeField.java`** -> AI Confidence: **99.24%**
1607. **`server/src/main/java/org/elasticsearch/index/mapper/SortedSetWithOffsetsDocValuesSyntheticFieldLoaderLayer.java`** -> AI Confidence: **99.24%**
1608. **`server/src/main/java/org/elasticsearch/index/mapper/SourceValueFetcher.java`** -> AI Confidence: **99.24%**
1609. **`server/src/main/java/org/elasticsearch/index/mapper/StringFieldType.java`** -> AI Confidence: **99.24%**
1610. **`server/src/main/java/org/elasticsearch/index/mapper/blockloader/docvalues/fn/Utf8CodePointsFromOrdsBlockLoader.java`** -> AI Confidence: **99.24%**
1611. **`server/src/main/java/org/elasticsearch/index/mapper/flattened/FlattenedFieldParser.java`** -> AI Confidence: **99.24%**
1612. **`server/src/main/java/org/elasticsearch/index/mapper/vectors/VectorEncoderDecoder.java`** -> AI Confidence: **99.24%**
1613. **`server/src/main/java/org/elasticsearch/index/query/GeoDistanceQueryBuilder.java`** -> AI Confidence: **99.24%**
1614. **`server/src/main/java/org/elasticsearch/index/query/GeoPolygonQueryBuilder.java`** -> AI Confidence: **99.24%**
1615. **`server/src/main/java/org/elasticsearch/index/query/MatchBoolPrefixQueryBuilder.java`** -> AI Confidence: **99.24%**
1616. **`server/src/main/java/org/elasticsearch/index/query/MatchPhrasePrefixQueryBuilder.java`** -> AI Confidence: **99.24%**
1617. **`server/src/main/java/org/elasticsearch/index/query/MatchQueryBuilder.java`** -> AI Confidence: **99.24%**
1618. **`server/src/main/java/org/elasticsearch/index/query/MoreLikeThisQueryBuilder.java`** -> AI Confidence: **99.24%**
1619. **`server/src/main/java/org/elasticsearch/index/query/MultiMatchQueryBuilder.java`** -> AI Confidence: **99.24%**
1620. **`server/src/main/java/org/elasticsearch/index/query/RangeQueryBuilder.java`** -> AI Confidence: **99.24%**
1621. **`server/src/main/java/org/elasticsearch/index/query/SimpleQueryStringBuilder.java`** -> AI Confidence: **99.24%**
1622. **`server/src/main/java/org/elasticsearch/index/query/TermQueryBuilder.java`** -> AI Confidence: **99.24%**
1623. **`server/src/main/java/org/elasticsearch/index/query/TermsQueryBuilder.java`** -> AI Confidence: **99.24%**
1624. **`server/src/main/java/org/elasticsearch/index/query/functionscore/DecayFunctionBuilder.java`** -> AI Confidence: **99.24%**
1625. **`server/src/main/java/org/elasticsearch/index/query/functionscore/FunctionScoreQueryBuilder.java`** -> AI Confidence: **99.24%**
1626. **`server/src/main/java/org/elasticsearch/index/query/functionscore/RandomScoreFunctionBuilder.java`** -> AI Confidence: **99.24%**
1627. **`server/src/main/java/org/elasticsearch/index/reindex/LeaderBulkByScrollTaskState.java`** -> AI Confidence: **99.24%**
1628. **`server/src/main/java/org/elasticsearch/index/search/MatchQueryParser.java`** -> AI Confidence: **99.24%**
1629. **`server/src/main/java/org/elasticsearch/index/search/MultiMatchQueryParser.java`** -> AI Confidence: **99.24%**
1630. **`server/src/main/java/org/elasticsearch/index/seqno/ReplicationTracker.java`** -> AI Confidence: **99.24%**
1631. **`server/src/main/java/org/elasticsearch/index/shard/GlobalCheckpointListeners.java`** -> AI Confidence: **99.24%**
1632. **`server/src/main/java/org/elasticsearch/index/shard/InternalIndexingStats.java`** -> AI Confidence: **99.24%**
1633. **`server/src/main/java/org/elasticsearch/index/shard/ShardPath.java`** -> AI Confidence: **99.24%**
1634. **`server/src/main/java/org/elasticsearch/index/shard/ShardStateMetadata.java`** -> AI Confidence: **99.24%**
1635. **`server/src/main/java/org/elasticsearch/index/store/AsyncDirectIOIndexInput.java`** -> AI Confidence: **99.24%**
1636. **`server/src/main/java/org/elasticsearch/index/store/DirectoryMetrics.java`** -> AI Confidence: **99.24%**
1637. **`server/src/main/java/org/elasticsearch/index/termvectors/TermVectorsService.java`** -> AI Confidence: **99.24%**
1638. **`server/src/main/java/org/elasticsearch/indices/IndexingMemoryController.java`** -> AI Confidence: **99.24%**
1639. **`server/src/main/java/org/elasticsearch/indices/SystemIndexDescriptor.java`** -> AI Confidence: **99.24%**
1640. **`server/src/main/java/org/elasticsearch/indices/breaker/HierarchyCircuitBreakerService.java`** -> AI Confidence: **99.24%**
1641. **`server/src/main/java/org/elasticsearch/indices/cluster/IndicesClusterStateService.java`** -> AI Confidence: **99.24%**
1642. **`server/src/main/java/org/elasticsearch/ingest/ConfigurationUtils.java`** -> AI Confidence: **99.24%**
1643. **`server/src/main/java/org/elasticsearch/ingest/PipelineConfiguration.java`** -> AI Confidence: **99.24%**
1644. **`server/src/main/java/org/elasticsearch/injection/Planner.java`** -> AI Confidence: **99.24%**
1645. **`server/src/main/java/org/elasticsearch/injection/guice/InheritingState.java`** -> AI Confidence: **99.24%**
1646. **`server/src/main/java/org/elasticsearch/injection/guice/internal/Errors.java`** -> AI Confidence: **99.24%**
1647. **`server/src/main/java/org/elasticsearch/injection/guice/spi/InjectionPoint.java`** -> AI Confidence: **99.24%**
1648. **`server/src/main/java/org/elasticsearch/lucene/grouping/SinglePassGroupingCollector.java`** -> AI Confidence: **99.24%**
1649. **`server/src/main/java/org/elasticsearch/lucene/grouping/TopFieldGroups.java`** -> AI Confidence: **99.24%**
1650. **`server/src/main/java/org/elasticsearch/lucene/queries/BlendedTermQuery.java`** -> AI Confidence: **99.24%**
1651. **`server/src/main/java/org/elasticsearch/monitor/fs/FsInfo.java`** -> AI Confidence: **99.24%**
1652. **`server/src/main/java/org/elasticsearch/monitor/os/OsProbe.java`** -> AI Confidence: **99.24%**
1653. **`server/src/main/java/org/elasticsearch/persistent/AllocatedPersistentTask.java`** -> AI Confidence: **99.24%**
1654. **`server/src/main/java/org/elasticsearch/plugins/PluginIntrospector.java`** -> AI Confidence: **99.24%**
1655. **`server/src/main/java/org/elasticsearch/plugins/PluginsService.java`** -> AI Confidence: **99.24%**
1656. **`server/src/main/java/org/elasticsearch/plugins/PluginsUtils.java`** -> AI Confidence: **99.24%**
1657. **`server/src/main/java/org/elasticsearch/repositories/IndexMetaDataGenerations.java`** -> AI Confidence: **99.24%**
1658. **`server/src/main/java/org/elasticsearch/repositories/RepositoriesService.java`** -> AI Confidence: **99.24%**
1659. **`server/src/main/java/org/elasticsearch/repositories/RepositoryData.java`** -> AI Confidence: **99.24%**
1660. **`server/src/main/java/org/elasticsearch/reservedstate/service/ReservedClusterStateService.java`** -> AI Confidence: **99.24%**
1661. **`server/src/main/java/org/elasticsearch/reservedstate/service/ReservedStateUpdateTask.java`** -> AI Confidence: **99.24%**
1662. **`server/src/main/java/org/elasticsearch/rest/action/admin/indices/RestIndexPutAliasAction.java`** -> AI Confidence: **99.24%**
1663. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestAliasAction.java`** -> AI Confidence: **99.24%**
1664. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestCatComponentTemplateAction.java`** -> AI Confidence: **99.24%**
1665. **`server/src/main/java/org/elasticsearch/rest/action/cat/RestNodeAttrsAction.java`** -> AI Confidence: **99.24%**
1666. **`server/src/main/java/org/elasticsearch/script/ScriptLanguagesInfo.java`** -> AI Confidence: **99.24%**
1667. **`server/src/main/java/org/elasticsearch/search/MultiValueMode.java`** -> AI Confidence: **99.24%**
1668. **`server/src/main/java/org/elasticsearch/search/NestedDocuments.java`** -> AI Confidence: **99.24%**
1669. **`server/src/main/java/org/elasticsearch/search/SearchHits.java`** -> AI Confidence: **99.24%**
1670. **`server/src/main/java/org/elasticsearch/search/SearchService.java`** -> AI Confidence: **99.24%**
1671. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/BinaryValuesSource.java`** -> AI Confidence: **99.24%**
1672. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/CompositeAggregationBuilder.java`** -> AI Confidence: **99.24%**
1673. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/composite/DoubleValuesSource.java`** -> AI Confidence: **99.24%**
1674. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/filter/FiltersAggregationBuilder.java`** -> AI Confidence: **99.24%**
1675. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/histogram/DateHistogramAggregationBuilder.java`** -> AI Confidence: **99.24%**
1676. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/histogram/LongBounds.java`** -> AI Confidence: **99.24%**
1677. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/histogram/RangeHistogramAggregator.java`** -> AI Confidence: **99.24%**
1678. **`server/src/main/java/org/elasticsearch/search/aggregations/bucket/range/GeoDistanceAggregationBuilder.java`** -> AI Confidence: **99.24%**
1679. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/AbstractInternalHDRPercentiles.java`** -> AI Confidence: **99.24%**
1680. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/AbstractInternalTDigestPercentiles.java`** -> AI Confidence: **99.24%**
1681. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/ExtendedStatsAggregator.java`** -> AI Confidence: **99.24%**
1682. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/HistogramUnionState.java`** -> AI Confidence: **99.24%**
1683. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/HyperLogLogPlusPlus.java`** -> AI Confidence: **99.24%**
1684. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/InternalBounds.java`** -> AI Confidence: **99.24%**
1685. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/InternalCentroid.java`** -> AI Confidence: **99.24%**
1686. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/InternalTopHits.java`** -> AI Confidence: **99.24%**
1687. **`server/src/main/java/org/elasticsearch/search/aggregations/metrics/ScriptedMetricAggregatorFactory.java`** -> AI Confidence: **99.24%**
1688. **`server/src/main/java/org/elasticsearch/search/aggregations/pipeline/BucketHelpers.java`** -> AI Confidence: **99.24%**
1689. **`server/src/main/java/org/elasticsearch/search/aggregations/pipeline/SerialDiffPipelineAggregationBuilder.java`** -> AI Confidence: **99.24%**
1690. **`server/src/main/java/org/elasticsearch/search/aggregations/support/MultiValuesSourceFieldConfig.java`** -> AI Confidence: **99.24%**
1691. **`server/src/main/java/org/elasticsearch/search/aggregations/support/ValuesSourceAggregationBuilder.java`** -> AI Confidence: **99.24%**
1692. **`server/src/main/java/org/elasticsearch/search/aggregations/support/ValuesSourceConfig.java`** -> AI Confidence: **99.24%**
1693. **`server/src/main/java/org/elasticsearch/search/aggregations/support/values/ScriptBytesValues.java`** -> AI Confidence: **99.24%**
1694. **`server/src/main/java/org/elasticsearch/search/dfs/DfsPhase.java`** -> AI Confidence: **99.24%**
1695. **`server/src/main/java/org/elasticsearch/search/fetch/StreamingFetchPhaseDocsIterator.java`** -> AI Confidence: **99.24%**
1696. **`server/src/main/java/org/elasticsearch/search/fetch/subphase/highlight/AbstractHighlighterBuilder.java`** -> AI Confidence: **99.24%**
1697. **`server/src/main/java/org/elasticsearch/search/lookup/LeafDocLookup.java`** -> AI Confidence: **99.24%**
1698. **`server/src/main/java/org/elasticsearch/search/rescore/RescorePhase.java`** -> AI Confidence: **99.24%**
1699. **`server/src/main/java/org/elasticsearch/search/retriever/RankDocsRetrieverBuilder.java`** -> AI Confidence: **99.24%**
1700. **`server/src/main/java/org/elasticsearch/search/runtime/GeoPointScriptFieldGeoShapeQuery.java`** -> AI Confidence: **99.24%**
1701. **`server/src/main/java/org/elasticsearch/search/suggest/Suggest.java`** -> AI Confidence: **99.24%**
1702. **`server/src/main/java/org/elasticsearch/search/suggest/SuggestBuilder.java`** -> AI Confidence: **99.24%**
1703. **`server/src/main/java/org/elasticsearch/search/suggest/SuggestionBuilder.java`** -> AI Confidence: **99.24%**
1704. **`server/src/main/java/org/elasticsearch/search/suggest/completion/context/ContextMappings.java`** -> AI Confidence: **99.24%**
1705. **`server/src/main/java/org/elasticsearch/search/suggest/completion/context/GeoContextMapping.java`** -> AI Confidence: **99.24%**
1706. **`server/src/main/java/org/elasticsearch/search/suggest/phrase/DirectCandidateGeneratorBuilder.java`** -> AI Confidence: **99.24%**
1707. **`server/src/main/java/org/elasticsearch/search/vectors/KnnScoreDocQueryBuilder.java`** -> AI Confidence: **99.24%**
1708. **`server/src/main/java/org/elasticsearch/search/vectors/KnnVectorQueryBuilder.java`** -> AI Confidence: **99.24%**
1709. **`server/src/main/java/org/elasticsearch/shutdown/PluginShutdownService.java`** -> AI Confidence: **99.24%**
1710. **`server/src/main/java/org/elasticsearch/snapshots/RestoreService.java`** -> AI Confidence: **99.24%**
1711. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotExternalChangesBatcher.java`** -> AI Confidence: **99.24%**
1712. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotShardsService.java`** -> AI Confidence: **99.24%**
1713. **`server/src/main/java/org/elasticsearch/snapshots/SnapshotsService.java`** -> AI Confidence: **99.24%**
1714. **`server/src/main/java/org/elasticsearch/synonyms/SynonymRule.java`** -> AI Confidence: **99.24%**
1715. **`server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java`** -> AI Confidence: **99.24%**
1716. **`server/src/main/java/org/elasticsearch/threadpool/ThreadPoolStats.java`** -> AI Confidence: **99.24%**
1717. **`server/src/main/java/org/elasticsearch/transport/InboundAggregator.java`** -> AI Confidence: **99.24%**
1718. **`server/src/main/java/org/elasticsearch/transport/OutboundHandler.java`** -> AI Confidence: **99.24%**
1719. **`server/src/test/java/org/elasticsearch/ElasticsearchExceptionTests.java`** -> AI Confidence: **99.24%**
1720. **`server/src/test/java/org/elasticsearch/action/admin/cluster/allocation/ClusterAllocationExplanationTests.java`** -> AI Confidence: **99.24%**
1721. **`server/src/test/java/org/elasticsearch/action/admin/cluster/allocation/DesiredBalanceResponseTests.java`** -> AI Confidence: **99.24%**
1722. **`server/src/test/java/org/elasticsearch/action/admin/cluster/node/stats/NodeStatsTests.java`** -> AI Confidence: **99.24%**
1723. **`server/src/test/java/org/elasticsearch/action/admin/cluster/stats/CCSTelemetrySnapshotTests.java`** -> AI Confidence: **99.24%**
1724. **`server/src/test/java/org/elasticsearch/action/admin/cluster/stats/ClusterStatsNodesTests.java`** -> AI Confidence: **99.24%**
1725. **`server/src/test/java/org/elasticsearch/action/admin/cluster/storedscripts/ScriptMethodInfoSerializingTests.java`** -> AI Confidence: **99.24%**
1726. **`server/src/test/java/org/elasticsearch/action/admin/indices/alias/AliasActionsTests.java`** -> AI Confidence: **99.24%**
1727. **`server/src/test/java/org/elasticsearch/action/admin/indices/alias/get/GetAliasesResponseTests.java`** -> AI Confidence: **99.24%**
1728. **`server/src/test/java/org/elasticsearch/action/admin/indices/close/CloseIndexResponseTests.java`** -> AI Confidence: **99.24%**
1729. **`server/src/test/java/org/elasticsearch/action/bulk/BulkItemResponseTests.java`** -> AI Confidence: **99.24%**
1730. **`server/src/test/java/org/elasticsearch/action/bulk/BulkItemResponseWireSerializingTests.java`** -> AI Confidence: **99.24%**
1731. **`server/src/test/java/org/elasticsearch/action/bulk/BulkRequestTests.java`** -> AI Confidence: **99.24%**
1732. **`server/src/test/java/org/elasticsearch/action/bulk/SimulateBulkRequestTests.java`** -> AI Confidence: **99.24%**
1733. **`server/src/test/java/org/elasticsearch/action/datastreams/UpdateDataStreamMappingsActionRequestTests.java`** -> AI Confidence: **99.24%**
1734. **`server/src/test/java/org/elasticsearch/action/datastreams/UpdateDataStreamSettingsActionRequestTests.java`** -> AI Confidence: **99.24%**
1735. **`server/src/test/java/org/elasticsearch/action/datastreams/lifecycle/ExplainDataStreamLifecycleResponseTests.java`** -> AI Confidence: **99.24%**
1736. **`server/src/test/java/org/elasticsearch/action/fieldcaps/RequestDispatcherTests.java`** -> AI Confidence: **99.24%**
1737. **`server/src/test/java/org/elasticsearch/action/ingest/SimulatePipelineResponseTests.java`** -> AI Confidence: **99.24%**
1738. **`server/src/test/java/org/elasticsearch/action/search/MultiSearchResponseTests.java`** -> AI Confidence: **99.24%**
1739. **`server/src/test/java/org/elasticsearch/cluster/ClusterSnapshotStatsTests.java`** -> AI Confidence: **99.24%**
1740. **`server/src/test/java/org/elasticsearch/cluster/coordination/CoordinatorVotingConfigurationTests.java`** -> AI Confidence: **99.24%**
1741. **`server/src/test/java/org/elasticsearch/cluster/metadata/DataStreamLifecycleTemplateTests.java`** -> AI Confidence: **99.24%**
1742. **`server/src/test/java/org/elasticsearch/cluster/metadata/DataStreamLifecycleTests.java`** -> AI Confidence: **99.24%**
1743. **`server/src/test/java/org/elasticsearch/cluster/metadata/DesiredNodesTests.java`** -> AI Confidence: **99.24%**
1744. **`server/src/test/java/org/elasticsearch/cluster/metadata/MetadataDataStreamsServiceTests.java`** -> AI Confidence: **99.24%**
1745. **`server/src/test/java/org/elasticsearch/cluster/node/DiscoveryNodeFiltersTests.java`** -> AI Confidence: **99.24%**
1746. **`server/src/test/java/org/elasticsearch/cluster/node/DiscoveryNodesTests.java`** -> AI Confidence: **99.24%**
1747. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/AllocateUnassignedDecisionTests.java`** -> AI Confidence: **99.24%**
1748. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/DiskThresholdMonitorTests.java`** -> AI Confidence: **99.24%**
1749. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/DiskThresholdSettingsTests.java`** -> AI Confidence: **99.24%**
1750. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/RandomAllocationDeciderTests.java`** -> AI Confidence: **99.24%**
1751. **`server/src/test/java/org/elasticsearch/cluster/routing/allocation/ResizeSourceIndexSettingsUpdaterTests.java`** -> AI Confidence: **99.24%**
1752. **`server/src/test/java/org/elasticsearch/common/compress/DeflateCompressTests.java`** -> AI Confidence: **99.24%**
1753. **`server/src/test/java/org/elasticsearch/common/network/NetworkUtilsTests.java`** -> AI Confidence: **99.24%**
1754. **`server/src/test/java/org/elasticsearch/common/time/JavaDateMathParserTests.java`** -> AI Confidence: **99.24%**
1755. **`server/src/test/java/org/elasticsearch/common/unit/FuzzinessTests.java`** -> AI Confidence: **99.24%**
1756. **`server/src/test/java/org/elasticsearch/common/util/BigArraysTests.java`** -> AI Confidence: **99.24%**
1757. **`server/src/test/java/org/elasticsearch/common/util/SetBackedScalingCuckooFilterTests.java`** -> AI Confidence: **99.24%**
1758. **`server/src/test/java/org/elasticsearch/common/util/concurrent/ReleasableLockTests.java`** -> AI Confidence: **99.24%**
1759. **`server/src/test/java/org/elasticsearch/discovery/SettingsBasedSeedHostsProviderTests.java`** -> AI Confidence: **99.24%**
1760. **`server/src/test/java/org/elasticsearch/gateway/GatewayMetaStatePersistedStateTests.java`** -> AI Confidence: **99.24%**
1761. **`server/src/test/java/org/elasticsearch/gateway/PersistedClusterStateServiceTests.java`** -> AI Confidence: **99.24%**
1762. **`server/src/test/java/org/elasticsearch/gateway/PriorityComparatorTests.java`** -> AI Confidence: **99.24%**
1763. **`server/src/test/java/org/elasticsearch/health/metadata/HealthMetadataSerializationTests.java`** -> AI Confidence: **99.24%**
1764. **`server/src/test/java/org/elasticsearch/index/codec/tsdb/DISIAccumulatorTests.java`** -> AI Confidence: **99.24%**
1765. **`server/src/test/java/org/elasticsearch/index/codec/tsdb/DocValuesCodecDuelTests.java`** -> AI Confidence: **99.24%**
1766. **`server/src/test/java/org/elasticsearch/index/codec/tsdb/es819/ES819TSDBDocValuesConsumerVersion0.java`** -> AI Confidence: **99.24%**
1767. **`server/src/test/java/org/elasticsearch/index/codec/tsdb/es819/TSDBDocValuesFormatSingleNodeTests.java`** -> AI Confidence: **99.24%**
1768. **`server/src/test/java/org/elasticsearch/index/codec/vectors/BaseBFloat16KnnVectorsFormatTestCase.java`** -> AI Confidence: **99.24%**
1769. **`server/src/test/java/org/elasticsearch/index/codec/vectors/cluster/KMeansLocalTests.java`** -> AI Confidence: **99.24%**
1770. **`server/src/test/java/org/elasticsearch/index/engine/InternalEngineTests.java`** -> AI Confidence: **99.24%**
1771. **`server/src/test/java/org/elasticsearch/index/engine/PruningMergePolicyTests.java`** -> AI Confidence: **99.24%**
1772. **`server/src/test/java/org/elasticsearch/index/engine/ReadOnlyEngineTests.java`** -> AI Confidence: **99.24%**
1773. **`server/src/test/java/org/elasticsearch/index/engine/SegmentTests.java`** -> AI Confidence: **99.24%**
1774. **`server/src/test/java/org/elasticsearch/index/fielddata/FilterFieldDataTests.java`** -> AI Confidence: **99.24%**
1775. **`server/src/test/java/org/elasticsearch/index/fielddata/ordinals/MultiOrdinalsTests.java`** -> AI Confidence: **99.24%**
1776. **`server/src/test/java/org/elasticsearch/index/get/GetResultTests.java`** -> AI Confidence: **99.24%**
1777. **`server/src/test/java/org/elasticsearch/index/mapper/BooleanFieldMapperTests.java`** -> AI Confidence: **99.24%**
1778. **`server/src/test/java/org/elasticsearch/index/mapper/CopyToMapperTests.java`** -> AI Confidence: **99.24%**
1779. **`server/src/test/java/org/elasticsearch/index/mapper/DocCountFieldMapperTests.java`** -> AI Confidence: **99.24%**
1780. **`server/src/test/java/org/elasticsearch/index/mapper/DocumentMapperTests.java`** -> AI Confidence: **99.24%**
1781. **`server/src/test/java/org/elasticsearch/index/mapper/DynamicTemplateParseTests.java`** -> AI Confidence: **99.24%**
1782. **`server/src/test/java/org/elasticsearch/index/mapper/IpScriptMapperTests.java`** -> AI Confidence: **99.24%**
1783. **`server/src/test/java/org/elasticsearch/index/mapper/RangeFieldMapperTests.java`** -> AI Confidence: **99.24%**
1784. **`server/src/test/java/org/elasticsearch/index/mapper/RootObjectMapperTests.java`** -> AI Confidence: **99.24%**
1785. **`server/src/test/java/org/elasticsearch/index/mapper/TimeSeriesMetadataFieldBlockLoaderTests.java`** -> AI Confidence: **99.24%**
1786. **`server/src/test/java/org/elasticsearch/index/mapper/blockloader/FlattenedFieldRootBlockLoaderTests.java`** -> AI Confidence: **99.24%**
1787. **`server/src/test/java/org/elasticsearch/index/mapper/blockloader/GeoPointFieldBlockLoaderTests.java`** -> AI Confidence: **99.24%**
1788. **`server/src/test/java/org/elasticsearch/index/mapper/blockloader/TextFieldBlockLoaderTests.java`** -> AI Confidence: **99.24%**
1789. **`server/src/test/java/org/elasticsearch/index/mapper/flattened/FlattenedFieldSyntheticWriterHelperTests.java`** -> AI Confidence: **99.24%**
1790. **`server/src/test/java/org/elasticsearch/index/query/FieldMaskingSpanQueryBuilderTests.java`** -> AI Confidence: **99.24%**
1791. **`server/src/test/java/org/elasticsearch/index/query/InnerHitBuilderTests.java`** -> AI Confidence: **99.24%**
1792. **`server/src/test/java/org/elasticsearch/index/query/QueryStringQueryBuilderMultiFieldTests.java`** -> AI Confidence: **99.24%**
1793. **`server/src/test/java/org/elasticsearch/index/query/SimpleQueryStringBuilderMultiFieldTests.java`** -> AI Confidence: **99.24%**
1794. **`server/src/test/java/org/elasticsearch/index/query/SpanGapQueryBuilderTests.java`** -> AI Confidence: **99.24%**
1795. **`server/src/test/java/org/elasticsearch/index/query/functionscore/FunctionScoreQueryBuilderTests.java`** -> AI Confidence: **99.24%**
1796. **`server/src/test/java/org/elasticsearch/index/reindex/BulkByScrollResponseTests.java`** -> AI Confidence: **99.24%**
1797. **`server/src/test/java/org/elasticsearch/index/reindex/BulkByScrollResponseWireSerializingTests.java`** -> AI Confidence: **99.24%**
1798. **`server/src/test/java/org/elasticsearch/index/replication/IndexLevelReplicationTests.java`** -> AI Confidence: **99.24%**
1799. **`server/src/test/java/org/elasticsearch/index/replication/RecoveryDuringReplicationTests.java`** -> AI Confidence: **99.24%**
1800. **`server/src/test/java/org/elasticsearch/index/seqno/PeerRecoveryRetentionLeaseExpiryTests.java`** -> AI Confidence: **99.24%**
1801. **`server/src/test/java/org/elasticsearch/index/snapshots/blobstore/FileInfoTests.java`** -> AI Confidence: **99.24%**
1802. **`server/src/test/java/org/elasticsearch/index/translog/TranslogTests.java`** -> AI Confidence: **99.24%**
1803. **`server/src/test/java/org/elasticsearch/indices/recovery/RecoveryRequestTrackerTests.java`** -> AI Confidence: **99.24%**
1804. **`server/src/test/java/org/elasticsearch/indices/recovery/StatelessPrimaryRelocationActionTests.java`** -> AI Confidence: **99.24%**
1805. **`server/src/test/java/org/elasticsearch/inference/completion/EncryptedReasoningDetailTests.java`** -> AI Confidence: **99.24%**
1806. **`server/src/test/java/org/elasticsearch/inference/completion/SummaryReasoningDetailTests.java`** -> AI Confidence: **99.24%**
1807. **`server/src/test/java/org/elasticsearch/inference/completion/TextReasoningDetailTests.java`** -> AI Confidence: **99.24%**
1808. **`server/src/test/java/org/elasticsearch/ingest/IngestMetadataTests.java`** -> AI Confidence: **99.24%**
1809. **`server/src/test/java/org/elasticsearch/rest/action/cat/RestIndicesActionTests.java`** -> AI Confidence: **99.24%**
1810. **`server/src/test/java/org/elasticsearch/search/SearchHitTests.java`** -> AI Confidence: **99.24%**
1811. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/histogram/InternalDateHistogramTests.java`** -> AI Confidence: **99.24%**
1812. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/histogram/InternalHistogramTests.java`** -> AI Confidence: **99.24%**
1813. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/range/InternalRangeTests.java`** -> AI Confidence: **99.24%**
1814. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/LongKeyedBucketOrdsTests.java`** -> AI Confidence: **99.24%**
1815. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/LongRareTermsTests.java`** -> AI Confidence: **99.24%**
1816. **`server/src/test/java/org/elasticsearch/search/aggregations/bucket/terms/StringRareTermsTests.java`** -> AI Confidence: **99.24%**
1817. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalHDRPercentilesTests.java`** -> AI Confidence: **99.24%**
1818. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalTDigestPercentilesTests.java`** -> AI Confidence: **99.24%**
1819. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalWeightedAvgTests.java`** -> AI Confidence: **99.24%**
1820. **`server/src/test/java/org/elasticsearch/search/aggregations/pipeline/InternalPercentilesBucketTests.java`** -> AI Confidence: **99.24%**
1821. **`server/src/test/java/org/elasticsearch/search/builder/SearchSourceBuilderTests.java`** -> AI Confidence: **99.24%**
1822. **`server/src/test/java/org/elasticsearch/search/suggest/SuggestionEntryTests.java`** -> AI Confidence: **99.24%**
1823. **`server/src/test/java/org/elasticsearch/search/suggest/SuggestionTests.java`** -> AI Confidence: **99.24%**
1824. **`server/src/test/java/org/elasticsearch/search/suggest/completion/GeoQueryContextTests.java`** -> AI Confidence: **99.24%**
1825. **`server/src/test/java/org/elasticsearch/search/suggest/phrase/DirectCandidateGeneratorTests.java`** -> AI Confidence: **99.24%**
1826. **`server/src/test/java/org/elasticsearch/search/suggest/term/TermSuggestionBuilderTests.java`** -> AI Confidence: **99.24%**
1827. **`server/src/test/java/org/elasticsearch/search/vectors/KnnScoreDocQueryBuilderTests.java`** -> AI Confidence: **99.24%**
1828. **`server/src/test/java/org/elasticsearch/tasks/CancellableTasksTrackerTests.java`** -> AI Confidence: **99.24%**
1829. **`server/src/test/java/org/elasticsearch/tasks/TaskInfoTests.java`** -> AI Confidence: **99.24%**
1830. **`server/src/test/java/org/elasticsearch/transport/InboundDecoderTests.java`** -> AI Confidence: **99.24%**
1831. **`server/src/test/java/org/elasticsearch/transport/Lz4TransportDecompressorTests.java`** -> AI Confidence: **99.24%**
1832. **`server/src/test/java/org/elasticsearch/transport/RemoteClusterAwareTests.java`** -> AI Confidence: **99.24%**
1833. **`server/src/test/java/org/elasticsearch/transport/RemoteClusterConnectionTests.java`** -> AI Confidence: **99.24%**
1834. **`test/fixtures/geoip-fixture/src/main/java/fixture/geoip/EnterpriseGeoIpHttpFixture.java`** -> AI Confidence: **99.24%**
1835. **`test/fixtures/minio-fixture/src/main/java/org/elasticsearch/test/fixtures/minio/MinioTestContainer.java`** -> AI Confidence: **99.24%**
1836. **`test/fixtures/testcontainer-utils/src/main/java/org/elasticsearch/test/fixtures/testcontainers/PullOrBuildImage.java`** -> AI Confidence: **99.24%**
1837. **`test/framework/src/main/java/org/elasticsearch/cluster/routing/RoutingNodesHelper.java`** -> AI Confidence: **99.24%**
1838. **`test/framework/src/main/java/org/elasticsearch/cluster/routing/TestShardRouting.java`** -> AI Confidence: **99.24%**
1839. **`test/framework/src/main/java/org/elasticsearch/datageneration/datasource/DefaultMappingParametersHandler.java`** -> AI Confidence: **99.24%**
1840. **`test/framework/src/main/java/org/elasticsearch/datageneration/matchers/source/FlattenedFieldMatcher.java`** -> AI Confidence: **99.24%**
1841. **`test/framework/src/main/java/org/elasticsearch/index/RandomCreateIndexGenerator.java`** -> AI Confidence: **99.24%**
1842. **`test/framework/src/main/java/org/elasticsearch/index/mapper/NumberFieldMapperTests.java`** -> AI Confidence: **99.24%**
1843. **`test/framework/src/main/java/org/elasticsearch/index/seqno/SequenceNumbersTestUtils.java`** -> AI Confidence: **99.24%**
1844. **`test/framework/src/main/java/org/elasticsearch/ingest/RandomDocumentPicks.java`** -> AI Confidence: **99.24%**
1845. **`test/framework/src/main/java/org/elasticsearch/plugins/MockPluginsService.java`** -> AI Confidence: **99.24%**
1846. **`test/framework/src/main/java/org/elasticsearch/search/aggregations/bucket/geogrid/GeoGridTestCase.java`** -> AI Confidence: **99.24%**
1847. **`test/framework/src/main/java/org/elasticsearch/telemetry/InstrumentType.java`** -> AI Confidence: **99.24%**
1848. **`test/framework/src/main/java/org/elasticsearch/test/BackgroundIndexer.java`** -> AI Confidence: **99.24%**
1849. **`test/framework/src/main/java/org/elasticsearch/test/BuildUtils.java`** -> AI Confidence: **99.24%**
1850. **`test/framework/src/main/java/org/elasticsearch/test/ESIntegTestCase.java`** -> AI Confidence: **99.24%**
1851. **`test/framework/src/main/java/org/elasticsearch/test/TestCluster.java`** -> AI Confidence: **99.24%**
1852. **`test/framework/src/main/java/org/elasticsearch/test/disruption/NetworkDisruption.java`** -> AI Confidence: **99.24%**
1853. **`test/framework/src/main/java/org/elasticsearch/test/rest/ESRestTestCase.java`** -> AI Confidence: **99.24%**
1854. **`test/framework/src/main/java/org/elasticsearch/test/rest/Stash.java`** -> AI Confidence: **99.24%**
1855. **`test/test-clusters/src/main/java/org/elasticsearch/test/cluster/local/AbstractLocalClusterFactory.java`** -> AI Confidence: **99.24%**
1856. **`test/test-clusters/src/main/java/org/elasticsearch/test/cluster/local/DefaultLocalClusterHandle.java`** -> AI Confidence: **99.24%**
1857. **`test/test-clusters/src/main/java/org/elasticsearch/test/cluster/util/ProcessReaper.java`** -> AI Confidence: **99.24%**
1858. **`test/yaml-rest-runner/src/main/java/org/elasticsearch/test/rest/yaml/section/ClientYamlTestSuite.java`** -> AI Confidence: **99.24%**
1859. **`test/yaml-rest-runner/src/main/java/org/elasticsearch/test/rest/yaml/section/DoSection.java`** -> AI Confidence: **99.24%**
1860. **`x-pack/plugin/analytics/src/main/java/org/elasticsearch/xpack/analytics/aggregations/bucket/range/HistoBackedRangeAggregator.java`** -> AI Confidence: **99.24%**
1861. **`x-pack/plugin/analytics/src/main/java/org/elasticsearch/xpack/analytics/mapper/ExponentialHistogramParser.java`** -> AI Confidence: **99.24%**
1862. **`x-pack/plugin/analytics/src/main/java/org/elasticsearch/xpack/analytics/movingPercentiles/MovingPercentilesPipelineAggregator.java`** -> AI Confidence: **99.24%**
1863. **`x-pack/plugin/analytics/src/main/java/org/elasticsearch/xpack/analytics/multiterms/MultiTermsAggregationBuilder.java`** -> AI Confidence: **99.24%**
1864. **`x-pack/plugin/analytics/src/main/java/org/elasticsearch/xpack/analytics/ttest/TTestAggregatorFactory.java`** -> AI Confidence: **99.24%**
1865. **`x-pack/plugin/analytics/src/test/java/org/elasticsearch/xpack/analytics/mapper/ExponentialHistogramFieldMapperTests.java`** -> AI Confidence: **99.24%**
1866. **`x-pack/plugin/analytics/src/test/java/org/elasticsearch/xpack/analytics/stringstats/InternalStringStatsTests.java`** -> AI Confidence: **99.24%**
1867. **`x-pack/plugin/analytics/src/test/java/org/elasticsearch/xpack/analytics/topmetrics/InternalTopMetricsTests.java`** -> AI Confidence: **99.24%**
1868. **`x-pack/plugin/async-search/src/internalClusterTest/java/org/elasticsearch/xpack/search/AsyncSearchActionIT.java`** -> AI Confidence: **99.24%**
1869. **`x-pack/plugin/async-search/src/internalClusterTest/java/org/elasticsearch/xpack/search/CrossClusterAsyncSearchIT.java`** -> AI Confidence: **99.24%**
1870. **`x-pack/plugin/async-search/src/main/java/org/elasticsearch/xpack/search/MutableSearchResponse.java`** -> AI Confidence: **99.24%**
1871. **`x-pack/plugin/autoscaling/src/main/java/org/elasticsearch/xpack/autoscaling/action/CapacityResponseCache.java`** -> AI Confidence: **99.24%**
1872. **`x-pack/plugin/autoscaling/src/main/java/org/elasticsearch/xpack/autoscaling/capacity/AutoscalingCalculateCapacityService.java`** -> AI Confidence: **99.24%**
1873. **`x-pack/plugin/autoscaling/src/main/java/org/elasticsearch/xpack/autoscaling/capacity/nodeinfo/AutoscalingNodeInfoService.java`** -> AI Confidence: **99.24%**
1874. **`x-pack/plugin/autoscaling/src/main/java/org/elasticsearch/xpack/autoscaling/storage/ReactiveStorageDeciderService.java`** -> AI Confidence: **99.24%**
1875. **`x-pack/plugin/autoscaling/src/test/java/org/elasticsearch/xpack/autoscaling/capacity/AutoscalingDeciderResultsTests.java`** -> AI Confidence: **99.24%**
1876. **`x-pack/plugin/blob-cache/src/main/java/org/elasticsearch/blobcache/common/BlobCacheBufferedIndexInput.java`** -> AI Confidence: **99.24%**
1877. **`x-pack/plugin/blob-cache/src/main/java/org/elasticsearch/blobcache/common/SparseFileTracker.java`** -> AI Confidence: **99.24%**
1878. **`x-pack/plugin/blob-cache/src/main/java/org/elasticsearch/blobcache/shared/SharedBlobCacheService.java`** -> AI Confidence: **99.24%**
1879. **`x-pack/plugin/blob-cache/src/test/java/org/elasticsearch/blobcache/common/ProgressListenableActionFutureTests.java`** -> AI Confidence: **99.24%**
1880. **`x-pack/plugin/blob-cache/src/test/java/org/elasticsearch/blobcache/common/SparseFileTrackerTests.java`** -> AI Confidence: **99.24%**
1881. **`x-pack/plugin/ccr/src/internalClusterTest/java/org/elasticsearch/xpack/ccr/CcrAliasesIT.java`** -> AI Confidence: **99.24%**
1882. **`x-pack/plugin/ccr/src/javaRestTest/java/org/elasticsearch/xpack/ccr/AutoFollowIT.java`** -> AI Confidence: **99.24%**
1883. **`x-pack/plugin/ccr/src/javaRestTest/java/org/elasticsearch/xpack/ccr/FollowIndexIT.java`** -> AI Confidence: **99.24%**
1884. **`x-pack/plugin/ccr/src/javaRestTest/java/org/elasticsearch/xpack/ccr/FollowIndexSecurityIT.java`** -> AI Confidence: **99.24%**
1885. **`x-pack/plugin/core/src/main/java/org/elasticsearch/index/engine/frozen/FrozenEngine.java`** -> AI Confidence: **99.24%**
1886. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/cluster/routing/allocation/DataTierAllocationDecider.java`** -> AI Confidence: **99.24%**
1887. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/action/TimeSeriesUsageTransportAction.java`** -> AI Confidence: **99.24%**
1888. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/async/DeleteAsyncResultsService.java`** -> AI Confidence: **99.24%**
1889. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ccr/action/FollowParameters.java`** -> AI Confidence: **99.24%**
1890. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/datastreams/TimeSeriesFeatureSetUsage.java`** -> AI Confidence: **99.24%**
1891. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ilm/GenerateSnapshotNameStep.java`** -> AI Confidence: **99.24%**
1892. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ilm/PhaseCacheManagement.java`** -> AI Confidence: **99.24%**
1893. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/MlTasks.java`** -> AI Confidence: **99.24%**
1894. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/annotations/Annotation.java`** -> AI Confidence: **99.24%**
1895. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/datafeed/DatafeedConfigUtils.java`** -> AI Confidence: **99.24%**
1896. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/dataframe/DataFrameAnalyticsConfig.java`** -> AI Confidence: **99.24%**
1897. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/dataframe/DataFrameAnalyticsConfigUpdate.java`** -> AI Confidence: **99.24%**
1898. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/TrainedModelConfig.java`** -> AI Confidence: **99.24%**
1899. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/preprocessing/NGram.java`** -> AI Confidence: **99.24%**
1900. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/InferenceHelpers.java`** -> AI Confidence: **99.24%**
1901. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/PredictionFieldType.java`** -> AI Confidence: **99.24%**
1902. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/ensemble/Ensemble.java`** -> AI Confidence: **99.24%**
1903. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/ensemble/WeightedMode.java`** -> AI Confidence: **99.24%**
1904. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/inference/TreeInferenceModel.java`** -> AI Confidence: **99.24%**
1905. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/tree/Tree.java`** -> AI Confidence: **99.24%**
1906. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/tree/TreeNode.java`** -> AI Confidence: **99.24%**
1907. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/config/AnalysisConfig.java`** -> AI Confidence: **99.24%**
1908. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/persistence/ElasticsearchMappings.java`** -> AI Confidence: **99.24%**
1909. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/results/AnomalyCause.java`** -> AI Confidence: **99.24%**
1910. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/results/AnomalyRecord.java`** -> AI Confidence: **99.24%**
1911. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/job/results/AnomalyScoreExplanation.java`** -> AI Confidence: **99.24%**
1912. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/utils/NameResolver.java`** -> AI Confidence: **99.24%**
1913. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/privilege/PutPrivilegesRequest.java`** -> AI Confidence: **99.24%**
1914. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/profile/SuggestProfilesRequest.java`** -> AI Confidence: **99.24%**
1915. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/token/InvalidateTokenRequest.java`** -> AI Confidence: **99.24%**
1916. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/action/user/GetUsersResponse.java`** -> AI Confidence: **99.24%**
1917. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authc/DefaultAuthenticationFailureHandler.java`** -> AI Confidence: **99.24%**
1918. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authc/RealmSettings.java`** -> AI Confidence: **99.24%**
1919. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authc/oidc/OpenIdConnectRealmSettings.java`** -> AI Confidence: **99.24%**
1920. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authz/RoleDescriptor.java`** -> AI Confidence: **99.24%**
1921. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/authz/privilege/ApplicationPrivilege.java`** -> AI Confidence: **99.24%**
1922. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/support/Automatons.java`** -> AI Confidence: **99.24%**
1923. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/slm/SnapshotLifecyclePolicy.java`** -> AI Confidence: **99.24%**
1924. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ssl/SSLConfigurationSettings.java`** -> AI Confidence: **99.24%**
1925. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ssl/X509KeyPairSettings.java`** -> AI Confidence: **99.24%**
1926. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/template/IndexTemplateRegistry.java`** -> AI Confidence: **99.24%**
1927. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/termsenum/action/TermsEnumAction.java`** -> AI Confidence: **99.24%**
1928. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/textstructure/action/AbstractFindStructureRequest.java`** -> AI Confidence: **99.24%**
1929. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/watcher/actions/ActionStatus.java`** -> AI Confidence: **99.24%**
1930. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/watcher/actions/ActionWrapper.java`** -> AI Confidence: **99.24%**
1931. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/watcher/support/WatcherDateTimeUtils.java`** -> AI Confidence: **99.24%**
1932. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/XPackSettingsTests.java`** -> AI Confidence: **99.24%**
1933. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/common/time/TimeUtilsTests.java`** -> AI Confidence: **99.24%**
1934. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/common/validation/RemoteClusterMinimumVersionValidationTests.java`** -> AI Confidence: **99.24%**
1935. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/datastreams/DataStreamLifecycleFeatureSetUsageTests.java`** -> AI Confidence: **99.24%**
1936. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ilm/AllocateActionTests.java`** -> AI Confidence: **99.24%**
1937. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ilm/PhaseCacheManagementTests.java`** -> AI Confidence: **99.24%**
1938. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ilm/SearchableSnapshotActionTests.java`** -> AI Confidence: **99.24%**
1939. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/inference/action/InferenceActionRequestTests.java`** -> AI Confidence: **99.24%**
1940. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/inference/usage/ModelStatsTests.java`** -> AI Confidence: **99.24%**
1941. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/action/InferModelActionRequestTests.java`** -> AI Confidence: **99.24%**
1942. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/action/PreviewDatafeedActionRequestTests.java`** -> AI Confidence: **99.24%**
1943. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/datafeed/DatafeedConfigTests.java`** -> AI Confidence: **99.24%**
1944. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/datafeed/DatafeedUpdateTests.java`** -> AI Confidence: **99.24%**
1945. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/preprocessing/customwordembedding/NGramFeatureExtractorTests.java`** -> AI Confidence: **99.24%**
1946. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/results/ClassificationInferenceResultsTests.java`** -> AI Confidence: **99.24%**
1947. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/QuestionAnsweringConfigUpdateTests.java`** -> AI Confidence: **99.24%**
1948. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/inference/trainedmodel/TextSimilarityConfigUpdateTests.java`** -> AI Confidence: **99.24%**
1949. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/job/config/AnalysisConfigTests.java`** -> AI Confidence: **99.24%**
1950. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/job/config/DetectionRuleTests.java`** -> AI Confidence: **99.24%**
1951. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/apikey/BulkUpdateApiKeyResponseTests.java`** -> AI Confidence: **99.24%**
1952. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/action/token/CreateTokenRequestTests.java`** -> AI Confidence: **99.24%**
1953. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/permission/DocumentPermissionsTests.java`** -> AI Confidence: **99.24%**
1954. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/permission/LimitedRoleTests.java`** -> AI Confidence: **99.24%**
1955. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/privilege/ApplicationPrivilegeDescriptorTests.java`** -> AI Confidence: **99.24%**
1956. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/template/TemplateUtilsTests.java`** -> AI Confidence: **99.24%**
1957. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/termsenum/TermsEnumTests.java`** -> AI Confidence: **99.24%**
1958. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/transform/action/UpdateTransformActionRequestTests.java`** -> AI Confidence: **99.24%**
1959. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/transform/transforms/SettingsConfigTests.java`** -> AI Confidence: **99.24%**
1960. **`x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java`** -> AI Confidence: **99.24%**
1961. **`x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/IlmPolicyDeprecationChecker.java`** -> AI Confidence: **99.24%**
1962. **`x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/TemplateDeprecationChecker.java`** -> AI Confidence: **99.24%**
1963. **`x-pack/plugin/dlm-frozen-transition/src/main/java/org/elasticsearch/xpack/dlm/frozen/DataStreamLifecycleConvertToFrozen.java`** -> AI Confidence: **99.24%**
1964. **`x-pack/plugin/downsample/src/main/java/org/elasticsearch/xpack/downsample/DimensionFieldDownsampler.java`** -> AI Confidence: **99.24%**
1965. **`x-pack/plugin/downsample/src/main/java/org/elasticsearch/xpack/downsample/DownsampleShardIndexer.java`** -> AI Confidence: **99.24%**
1966. **`x-pack/plugin/downsample/src/main/java/org/elasticsearch/xpack/downsample/TimeSeriesFields.java`** -> AI Confidence: **99.24%**
1967. **`x-pack/plugin/enrich/src/main/java/org/elasticsearch/xpack/enrich/EnrichCache.java`** -> AI Confidence: **99.24%**
1968. **`x-pack/plugin/ent-search/src/test/java/org/elasticsearch/xpack/application/connector/ConnectorFeaturesTests.java`** -> AI Confidence: **99.24%**
1969. **`x-pack/plugin/eql/qa/common/src/main/java/org/elasticsearch/test/eql/stats/EqlUsageRestTestCase.java`** -> AI Confidence: **99.24%**
1970. **`x-pack/plugin/eql/qa/correctness/src/javaRestTest/java/org/elasticsearch/xpack/eql/EqlSpecLoader.java`** -> AI Confidence: **99.24%**
1971. **`x-pack/plugin/eql/src/internalClusterTest/java/org/elasticsearch/xpack/eql/action/CCSPartialResultsIT.java`** -> AI Confidence: **99.24%**
1972. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/execution/assembler/BoxedQueryRequest.java`** -> AI Confidence: **99.24%**
1973. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/execution/sequence/SequenceMatcher.java`** -> AI Confidence: **99.24%**
1974. **`x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/parser/LogicalPlanBuilder.java`** -> AI Confidence: **99.24%**
1975. **`x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/execution/assembler/SeriesUtils.java`** -> AI Confidence: **99.24%**
1976. **`x-pack/plugin/esql-datasource-azure/src/main/java/org/elasticsearch/xpack/esql/datasource/azure/AzureStorageObject.java`** -> AI Confidence: **99.24%**
1977. **`x-pack/plugin/esql-datasource-bzip2/src/test/java/org/elasticsearch/xpack/esql/datasource/bzip2/Bzip2NdJsonSplitIntegrationTests.java`** -> AI Confidence: **99.24%**
1978. **`x-pack/plugin/esql-datasource-csv/src/main/java/org/elasticsearch/xpack/esql/datasource/csv/CsvSchemaInferrer.java`** -> AI Confidence: **99.24%**
1979. **`x-pack/plugin/esql-datasource-csv/src/test/java/org/elasticsearch/xpack/esql/datasource/csv/CsvFormatReaderTests.java`** -> AI Confidence: **99.24%**
1980. **`x-pack/plugin/esql-datasource-grpc/src/main/java/org/elasticsearch/xpack/esql/datasource/grpc/FlightTypeMapping.java`** -> AI Confidence: **99.24%**
1981. **`x-pack/plugin/esql-datasource-iceberg/qa/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/iceberg/InteractiveFixtureManual.java`** -> AI Confidence: **99.24%**
1982. **`x-pack/plugin/esql-datasource-iceberg/src/main/java/org/elasticsearch/xpack/esql/datasource/iceberg/IcebergTableMetadata.java`** -> AI Confidence: **99.24%**
1983. **`x-pack/plugin/esql-datasource-iceberg/src/test/java/org/elasticsearch/xpack/esql/datasource/iceberg/IcebergPushdownFiltersTests.java`** -> AI Confidence: **99.24%**
1984. **`x-pack/plugin/esql-datasource-ndjson/src/main/java/org/elasticsearch/xpack/esql/datasource/ndjson/NdJsonSchemaInferrer.java`** -> AI Confidence: **99.24%**
1985. **`x-pack/plugin/esql/compute/gen/src/main/java/org/elasticsearch/compute/gen/EvaluatorImplementer.java`** -> AI Confidence: **99.24%**
1986. **`x-pack/plugin/esql/compute/gen/src/main/java/org/elasticsearch/compute/gen/Types.java`** -> AI Confidence: **99.24%**
1987. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AnyBytesRefAggregator.java`** -> AI Confidence: **99.24%**
1988. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AnyDoubleAggregator.java`** -> AI Confidence: **99.24%**
1989. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AnyFloatAggregator.java`** -> AI Confidence: **99.24%**
1990. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AnyIntAggregator.java`** -> AI Confidence: **99.24%**
1991. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/AnyLongAggregator.java`** -> AI Confidence: **99.24%**
1992. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/BooleanFallibleArrayState.java`** -> AI Confidence: **99.24%**
1993. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/DoubleFallibleArrayState.java`** -> AI Confidence: **99.24%**
1994. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/FloatFallibleArrayState.java`** -> AI Confidence: **99.24%**
1995. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/IntFallibleArrayState.java`** -> AI Confidence: **99.24%**
1996. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/LongFallibleArrayState.java`** -> AI Confidence: **99.24%**
1997. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/BooleanBlockBuilder.java`** -> AI Confidence: **99.24%**
1998. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/DoubleBucketedSort.java`** -> AI Confidence: **99.24%**
1999. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/DoubleDoubleBucketedSort.java`** -> AI Confidence: **99.24%**
2000. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/DoubleFloatBucketedSort.java`** -> AI Confidence: **99.24%**
2001. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/DoubleIntBucketedSort.java`** -> AI Confidence: **99.24%**
2002. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/DoubleLongBucketedSort.java`** -> AI Confidence: **99.24%**
2003. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/FloatBucketedSort.java`** -> AI Confidence: **99.24%**
2004. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/FloatDoubleBucketedSort.java`** -> AI Confidence: **99.24%**
2005. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/FloatFloatBucketedSort.java`** -> AI Confidence: **99.24%**
2006. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/FloatIntBucketedSort.java`** -> AI Confidence: **99.24%**
2007. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/FloatLongBucketedSort.java`** -> AI Confidence: **99.24%**
2008. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/IntBucketedSort.java`** -> AI Confidence: **99.24%**
2009. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/IntDoubleBucketedSort.java`** -> AI Confidence: **99.24%**
2010. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/IntFloatBucketedSort.java`** -> AI Confidence: **99.24%**
2011. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/IntIntBucketedSort.java`** -> AI Confidence: **99.24%**
2012. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/IntLongBucketedSort.java`** -> AI Confidence: **99.24%**
2013. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/LongBucketedSort.java`** -> AI Confidence: **99.24%**
2014. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/LongDoubleBucketedSort.java`** -> AI Confidence: **99.24%**
2015. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/LongFloatBucketedSort.java`** -> AI Confidence: **99.24%**
2016. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/LongIntBucketedSort.java`** -> AI Confidence: **99.24%**
2017. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/sort/LongLongBucketedSort.java`** -> AI Confidence: **99.24%**
2018. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/CountDistinctBooleanGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2019. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/CountDistinctBytesRefGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2020. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/CountDistinctDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2021. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/CountDistinctFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2022. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/CountDistinctIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2023. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/CountDistinctLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2024. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DeltaDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2025. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DeltaFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2026. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DeltaIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2027. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DeltaLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2028. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DerivDoubleAggregatorFunction.java`** -> AI Confidence: **99.24%**
2029. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DerivDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2030. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DerivIntAggregatorFunction.java`** -> AI Confidence: **99.24%**
2031. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DerivIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2032. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DerivLongAggregatorFunction.java`** -> AI Confidence: **99.24%**
2033. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/DerivLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2034. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstBytesRefByTimestampAggregatorFunction.java`** -> AI Confidence: **99.24%**
2035. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstBytesRefByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2036. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstDoubleByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2037. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstExponentialHistogramByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2038. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstFloatByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2039. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstIntByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2040. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstLongByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2041. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/FirstTDigestByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2042. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/IrateDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2043. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/IrateFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2044. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/IrateIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2045. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/IrateLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2046. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastBytesRefByTimestampAggregatorFunction.java`** -> AI Confidence: **99.24%**
2047. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastBytesRefByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2048. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastDoubleByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2049. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastExponentialHistogramByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2050. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastFloatByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2051. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastIntByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2052. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastLongByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2053. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LastTDigestByTimestampGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2054. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/LossySumDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2055. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MaxBooleanAggregatorFunction.java`** -> AI Confidence: **99.24%**
2056. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MaxBooleanGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2057. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MaxDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2058. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MaxFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2059. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MaxIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2060. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MaxLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2061. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MedianAbsoluteDeviationDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2062. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MedianAbsoluteDeviationFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2063. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MedianAbsoluteDeviationIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2064. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MedianAbsoluteDeviationLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2065. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MinBooleanAggregatorFunction.java`** -> AI Confidence: **99.24%**
2066. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MinBooleanGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2067. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MinDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2068. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MinFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2069. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MinIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2070. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/MinLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2071. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/PercentileDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2072. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/PercentileFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2073. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/PercentileIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2074. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/PercentileLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2075. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SampleBooleanGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2076. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SampleBytesRefGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2077. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SampleDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2078. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SampleIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2079. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SampleLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2080. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/StdDevDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2081. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/StdDevFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2082. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/StdDevIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2083. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/StdDevLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2084. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SumDenseVectorGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2085. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SumDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2086. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SumFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2087. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SumIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2088. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/SumLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2089. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopBooleanGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2090. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopBytesRefGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2091. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleDoubleAggregatorFunction.java`** -> AI Confidence: **99.24%**
2092. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2093. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleFloatAggregatorFunction.java`** -> AI Confidence: **99.24%**
2094. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2095. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2096. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleIntAggregatorFunction.java`** -> AI Confidence: **99.24%**
2097. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2098. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleLongAggregatorFunction.java`** -> AI Confidence: **99.24%**
2099. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopDoubleLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2100. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatDoubleAggregatorFunction.java`** -> AI Confidence: **99.24%**
2101. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2102. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatFloatAggregatorFunction.java`** -> AI Confidence: **99.24%**
2103. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2104. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2105. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatIntAggregatorFunction.java`** -> AI Confidence: **99.24%**
2106. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2107. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatLongAggregatorFunction.java`** -> AI Confidence: **99.24%**
2108. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopFloatLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2109. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntDoubleAggregatorFunction.java`** -> AI Confidence: **99.24%**
2110. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2111. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntFloatAggregatorFunction.java`** -> AI Confidence: **99.24%**
2112. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2113. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2114. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntIntAggregatorFunction.java`** -> AI Confidence: **99.24%**
2115. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntLongAggregatorFunction.java`** -> AI Confidence: **99.24%**
2116. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIntLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2117. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopIpGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2118. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongDoubleAggregatorFunction.java`** -> AI Confidence: **99.24%**
2119. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2120. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongFloatAggregatorFunction.java`** -> AI Confidence: **99.24%**
2121. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2122. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2123. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongIntAggregatorFunction.java`** -> AI Confidence: **99.24%**
2124. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2125. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongLongAggregatorFunction.java`** -> AI Confidence: **99.24%**
2126. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/TopLongLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2127. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/ValuesBooleanGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2128. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/ValuesDoubleGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2129. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/ValuesFloatGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2130. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/ValuesIntGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2131. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/ValuesLongGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2132. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialCentroidCartesianPointDocValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2133. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialCentroidGeoPointDocValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2134. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialExtentCartesianPointDocValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2135. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialExtentCartesianPointSourceValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2136. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialExtentCartesianShapeSourceValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2137. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialExtentGeoPointDocValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2138. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialExtentGeoPointSourceValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2139. **`x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation/spatial/SpatialExtentGeoShapeSourceValuesGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2140. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/AbstractRateGroupingFunction.java`** -> AI Confidence: **99.24%**
2141. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/CountApproximateGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2142. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/CountGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2143. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/PresentGroupingAggregatorFunction.java`** -> AI Confidence: **99.24%**
2144. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/TDigestStates.java`** -> AI Confidence: **99.24%**
2145. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/BooleanBlockHash.java`** -> AI Confidence: **99.24%**
2146. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/BytesRef2BlockHash.java`** -> AI Confidence: **99.24%**
2147. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/BytesRef3BlockHash.java`** -> AI Confidence: **99.24%**
2148. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/BytesRefLongBlockHash.java`** -> AI Confidence: **99.24%**
2149. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/LongTopNBlockHash.java`** -> AI Confidence: **99.24%**
2150. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/PackedValuesBlockHash.java`** -> AI Confidence: **99.24%**
2151. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/aggregation/blockhash/TimeSeriesBlockHash.java`** -> AI Confidence: **99.24%**
2152. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/AggregateMetricDoubleArrayBlock.java`** -> AI Confidence: **99.24%**
2153. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/ExponentialHistogramArrayBlock.java`** -> AI Confidence: **99.24%**
2154. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/Page.java`** -> AI Confidence: **99.24%**
2155. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/sort/BytesRefBucketedSort.java`** -> AI Confidence: **99.24%**
2156. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/query/LuceneSliceQueue.java`** -> AI Confidence: **99.24%**
2157. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/query/LuceneSourceOperator.java`** -> AI Confidence: **99.24%**
2158. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/read/ValuesSourceReaderOperatorStatus.java`** -> AI Confidence: **99.24%**
2159. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/ChangePointOperator.java`** -> AI Confidence: **99.24%**
2160. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/DriverProfile.java`** -> AI Confidence: **99.24%**
2161. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/DriverScheduler.java`** -> AI Confidence: **99.24%**
2162. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/DriverStatus.java`** -> AI Confidence: **99.24%**
2163. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/GroupKeyEncoder.java`** -> AI Confidence: **99.24%**
2164. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/MetricsInfoOperator.java`** -> AI Confidence: **99.24%**
2165. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/TsInfoOperator.java`** -> AI Confidence: **99.24%**
2166. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/exchange/BidirectionalBatchExchangeClient.java`** -> AI Confidence: **99.24%**
2167. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/lookup/EnrichQuerySourceOperator.java`** -> AI Confidence: **99.24%**
2168. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/lookup/MergePositionsOperator.java`** -> AI Confidence: **99.24%**
2169. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/lookup/QueryList.java`** -> AI Confidence: **99.24%**
2170. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/mvdedupe/MultivalueDedupe.java`** -> AI Confidence: **99.24%**
2171. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/topn/GroupedTopNOperator.java`** -> AI Confidence: **99.24%**
2172. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/topn/ValueExtractor.java`** -> AI Confidence: **99.24%**
2173. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/aggregation/HllStatesTests.java`** -> AI Confidence: **99.24%**
2174. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/aggregation/blockhash/BlockHashTestCase.java`** -> AI Confidence: **99.24%**
2175. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/aggregation/blockhash/CategorizeBlockHashTests.java`** -> AI Confidence: **99.24%**
2176. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/BlockSerializationTests.java`** -> AI Confidence: **99.24%**
2177. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/arrow/BooleanArrowBufTests.java`** -> AI Confidence: **99.24%**
2178. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/arrow/BytesRefArrowBufTests.java`** -> AI Confidence: **99.24%**
2179. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/arrow/LongArrowBufTests.java`** -> AI Confidence: **99.24%**
2180. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/sort/BucketedSortTestCase.java`** -> AI Confidence: **99.24%**
2181. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/AddGarbageRowsSourceOperator.java`** -> AI Confidence: **99.24%**
2182. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/PositionMergingSourceOperator.java`** -> AI Confidence: **99.24%**
2183. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/lookup/EnrichResultBuilderTests.java`** -> AI Confidence: **99.24%**
2184. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/lookup/RightChunkedLeftJoinTests.java`** -> AI Confidence: **99.24%**
2185. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/mvdedupe/MultivalueDedupeTests.java`** -> AI Confidence: **99.24%**
2186. **`x-pack/plugin/esql/compute/test/src/main/java/org/elasticsearch/compute/test/operator/blocksource/ListRowsBlockSourceOperator.java`** -> AI Confidence: **99.24%**
2187. **`x-pack/plugin/esql/qa/action/src/internalClusterTest/java/org/elasticsearch/test/esql/qa/action/CoreEsqlActionIT.java`** -> AI Confidence: **99.24%**
2188. **`x-pack/plugin/esql/qa/server/multi-clusters/src/javaRestTest/java/org/elasticsearch/xpack/esql/ccq/Clusters.java`** -> AI Confidence: **99.24%**
2189. **`x-pack/plugin/esql/qa/server/multi-clusters/src/javaRestTest/java/org/elasticsearch/xpack/esql/ccq/MultiClusterTimeSeriesIT.java`** -> AI Confidence: **99.24%**
2190. **`x-pack/plugin/esql/qa/server/multi-node/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/multi_node/ExternalDistributedStressIT.java`** -> AI Confidence: **99.24%**
2191. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/KnnSemanticTextTestCase.java`** -> AI Confidence: **99.24%**
2192. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/RestEnrichTestCase.java`** -> AI Confidence: **99.24%**
2193. **`x-pack/plugin/esql/qa/server/src/main/java/org/elasticsearch/xpack/esql/qa/rest/RestRerankTestCase.java`** -> AI Confidence: **99.24%**
2194. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/CsvTestUtils.java`** -> AI Confidence: **99.24%**
2195. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/EsqlQueryGenerator.java`** -> AI Confidence: **99.24%**
2196. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/command/pipe/DropGenerator.java`** -> AI Confidence: **99.24%**
2197. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/command/pipe/RegisteredDomainGenerator.java`** -> AI Confidence: **99.24%**
2198. **`x-pack/plugin/esql/qa/testFixtures/src/main/java/org/elasticsearch/xpack/esql/generator/command/pipe/RenameGenerator.java`** -> AI Confidence: **99.24%**
2199. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/DenseVectorFieldTypeIT.java`** -> AI Confidence: **99.24%**
2200. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterLookupJoinFailuresIT.java`** -> AI Confidence: **99.24%**
2201. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterLookupJoinIT.java`** -> AI Confidence: **99.24%**
2202. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterQueryIT.java`** -> AI Confidence: **99.24%**
2203. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterSubqueryUnavailableRemotesIT.java`** -> AI Confidence: **99.24%**
2204. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/CrossClusterTimeSeriesIT.java`** -> AI Confidence: **99.24%**
2205. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/EsqlActionIT.java`** -> AI Confidence: **99.24%**
2206. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/EsqlRetryIT.java`** -> AI Confidence: **99.24%**
2207. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/FuseIT.java`** -> AI Confidence: **99.24%**
2208. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/QueryExecutionMetadataIT.java`** -> AI Confidence: **99.24%**
2209. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/action/TimeSeriesIT.java`** -> AI Confidence: **99.24%**
2210. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/plugin/RemoteIndexResolutionIT.java`** -> AI Confidence: **99.24%**
2211. **`x-pack/plugin/esql/src/internalClusterTest/java/org/elasticsearch/xpack/esql/spatial/SpatialPushDownTestCase.java`** -> AI Confidence: **99.24%**
2212. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceBooleanEvaluator.java`** -> AI Confidence: **99.24%**
2213. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceBytesRefEvaluator.java`** -> AI Confidence: **99.24%**
2214. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2215. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceExponentialHistogramEvaluator.java`** -> AI Confidence: **99.24%**
2216. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceFloatEvaluator.java`** -> AI Confidence: **99.24%**
2217. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceIntEvaluator.java`** -> AI Confidence: **99.24%**
2218. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceLongEvaluator.java`** -> AI Confidence: **99.24%**
2219. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/function/scalar/nulls/CoalesceTDigestEvaluator.java`** -> AI Confidence: **99.24%**
2220. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InBytesRefEvaluator.java`** -> AI Confidence: **99.24%**
2221. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2222. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InIntEvaluator.java`** -> AI Confidence: **99.24%**
2223. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InLongEvaluator.java`** -> AI Confidence: **99.24%**
2224. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InMillisNanosEvaluator.java`** -> AI Confidence: **99.24%**
2225. **`x-pack/plugin/esql/src/main/generated-src/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InNanosMillisEvaluator.java`** -> AI Confidence: **99.24%**
2226. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMaxBytesRefEvaluator.java`** -> AI Confidence: **99.24%**
2227. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/ClampMinBytesRefEvaluator.java`** -> AI Confidence: **99.24%**
2228. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/GreatestBooleanEvaluator.java`** -> AI Confidence: **99.24%**
2229. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/GreatestBytesRefEvaluator.java`** -> AI Confidence: **99.24%**
2230. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/GreatestDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2231. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/GreatestIntEvaluator.java`** -> AI Confidence: **99.24%**
2232. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/GreatestLongEvaluator.java`** -> AI Confidence: **99.24%**
2233. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/LeastBooleanEvaluator.java`** -> AI Confidence: **99.24%**
2234. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/LeastBytesRefEvaluator.java`** -> AI Confidence: **99.24%**
2235. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/LeastDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2236. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/LeastIntEvaluator.java`** -> AI Confidence: **99.24%**
2237. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/LeastLongEvaluator.java`** -> AI Confidence: **99.24%**
2238. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateFormatMillisEvaluator.java`** -> AI Confidence: **99.24%**
2239. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateFormatNanosEvaluator.java`** -> AI Confidence: **99.24%**
2240. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateParseEvaluator.java`** -> AI Confidence: **99.24%**
2241. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/histogram/HistogramPercentileExponentialHistogramEvaluator.java`** -> AI Confidence: **99.24%**
2242. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/histogram/HistogramPercentileTDigestEvaluator.java`** -> AI Confidence: **99.24%**
2243. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/ip/CIDRMatchEvaluator.java`** -> AI Confidence: **99.24%**
2244. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/AbsIntEvaluator.java`** -> AI Confidence: **99.24%**
2245. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/AbsLongEvaluator.java`** -> AI Confidence: **99.24%**
2246. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/AcosEvaluator.java`** -> AI Confidence: **99.24%**
2247. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/AcoshEvaluator.java`** -> AI Confidence: **99.24%**
2248. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/AsinEvaluator.java`** -> AI Confidence: **99.24%**
2249. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/AtanhEvaluator.java`** -> AI Confidence: **99.24%**
2250. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CbrtDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2251. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CbrtIntEvaluator.java`** -> AI Confidence: **99.24%**
2252. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CbrtLongEvaluator.java`** -> AI Confidence: **99.24%**
2253. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/CoshEvaluator.java`** -> AI Confidence: **99.24%**
2254. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/Log10DoubleEvaluator.java`** -> AI Confidence: **99.24%**
2255. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/Log10IntEvaluator.java`** -> AI Confidence: **99.24%**
2256. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/Log10LongEvaluator.java`** -> AI Confidence: **99.24%**
2257. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/Log10UnsignedLongEvaluator.java`** -> AI Confidence: **99.24%**
2258. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/LogConstantEvaluator.java`** -> AI Confidence: **99.24%**
2259. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/ScalbConstantIntEvaluator.java`** -> AI Confidence: **99.24%**
2260. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/ScalbConstantLongEvaluator.java`** -> AI Confidence: **99.24%**
2261. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/SinhEvaluator.java`** -> AI Confidence: **99.24%**
2262. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/SqrtDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2263. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/SqrtIntEvaluator.java`** -> AI Confidence: **99.24%**
2264. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/math/SqrtLongEvaluator.java`** -> AI Confidence: **99.24%**
2265. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvPercentileDoubleEvaluator.java`** -> AI Confidence: **99.24%**
2266. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvPercentileIntegerEvaluator.java`** -> AI Confidence: **99.24%**
2267. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvPercentileLongEvaluator.java`** -> AI Confidence: **99.24%**
2268. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvZipEvaluator.java`** -> AI Confidence: **99.24%**
2269. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/score/DecayDateNanosEvaluator.java`** -> AI Confidence: **99.24%**
2270. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/score/DecayDatetimeEvaluator.java`** -> AI Confidence: **99.24%**
2271. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/ConcatEvaluator.java`** -> AI Confidence: **99.24%**
2272. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/ContainsEvaluator.java`** -> AI Confidence: **99.24%**
2273. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/EndsWithEvaluator.java`** -> AI Confidence: **99.24%**
2274. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/HashEvaluator.java`** -> AI Confidence: **99.24%**
2275. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/JsonExtractConstantEvaluator.java`** -> AI Confidence: **99.24%**
2276. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/LeftEvaluator.java`** -> AI Confidence: **99.24%**
2277. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/LocateNoStartEvaluator.java`** -> AI Confidence: **99.24%**
2278. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/RightEvaluator.java`** -> AI Confidence: **99.24%**
2279. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/SpaceEvaluator.java`** -> AI Confidence: **99.24%**
2280. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/SplitVariableEvaluator.java`** -> AI Confidence: **99.24%**
2281. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/StartsWithEvaluator.java`** -> AI Confidence: **99.24%**
2282. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/string/SubstringNoLengthEvaluator.java`** -> AI Confidence: **99.24%**
2283. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddDateNanosEvaluator.java`** -> AI Confidence: **99.24%**
2284. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddDatetimesEvaluator.java`** -> AI Confidence: **99.24%**
2285. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/NegIntsEvaluator.java`** -> AI Confidence: **99.24%**
2286. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/NegLongsEvaluator.java`** -> AI Confidence: **99.24%**
2287. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/SubDateNanosEvaluator.java`** -> AI Confidence: **99.24%**
2288. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/SubDatetimesEvaluator.java`** -> AI Confidence: **99.24%**
2289. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsGeometriesEvaluator.java`** -> AI Confidence: **99.24%**
2290. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsKeywordsEvaluator.java`** -> AI Confidence: **99.24%**
2291. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanKeywordsEvaluator.java`** -> AI Confidence: **99.24%**
2292. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqualKeywordsEvaluator.java`** -> AI Confidence: **99.24%**
2293. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/InsensitiveEqualsEvaluator.java`** -> AI Confidence: **99.24%**
2294. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanKeywordsEvaluator.java`** -> AI Confidence: **99.24%**
2295. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/LessThanOrEqualKeywordsEvaluator.java`** -> AI Confidence: **99.24%**
2296. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsGeometriesEvaluator.java`** -> AI Confidence: **99.24%**
2297. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEqualsKeywordsEvaluator.java`** -> AI Confidence: **99.24%**
2298. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/EsqlQueryProfile.java`** -> AI Confidence: **99.24%**
2299. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/EsqlQueryResponse.java`** -> AI Confidence: **99.24%**
2300. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/EsqlResponseListener.java`** -> AI Confidence: **99.24%**
2301. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/core/expression/FieldAttribute.java`** -> AI Confidence: **99.24%**
2302. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/core/querydsl/QueryDslTimestampBoundsExtractor.java`** -> AI Confidence: **99.24%**
2303. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/ConcurrencyLimitedStorageObject.java`** -> AI Confidence: **99.24%**
2304. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/ExternalSourceResolver.java`** -> AI Confidence: **99.24%**
2305. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/FormatReaderRegistry.java`** -> AI Confidence: **99.24%**
2306. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/OperatorFactoryRegistry.java`** -> AI Confidence: **99.24%**
2307. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/RetryableStorageObject.java`** -> AI Confidence: **99.24%**
2308. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/SplitDiscoveryPhase.java`** -> AI Confidence: **99.24%**
2309. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/VirtualColumnInjector.java`** -> AI Confidence: **99.24%**
2310. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/enrich/EnrichPolicyResolver.java`** -> AI Confidence: **99.24%**
2311. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/enrich/ExpressionQueryList.java`** -> AI Confidence: **99.24%**
2312. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/enrich/StreamingLookupFromIndexOperator.java`** -> AI Confidence: **99.24%**
2313. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/evaluator/command/RegisteredDomainFunctionBridge.java`** -> AI Confidence: **99.24%**
2314. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/aggregate/Top.java`** -> AI Confidence: **99.24%**
2315. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/grouping/Bucket.java`** -> AI Confidence: **99.24%**
2316. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/grouping/TBucket.java`** -> AI Confidence: **99.24%**
2317. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/conditional/Case.java`** -> AI Confidence: **99.24%**
2318. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvUnion.java`** -> AI Confidence: **99.24%**
2319. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/string/AutomataMatch.java`** -> AI Confidence: **99.24%**
2320. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/string/ChickenArtBuilder.java`** -> AI Confidence: **99.24%**
2321. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/function/scalar/string/JsonExtract.java`** -> AI Confidence: **99.24%**
2322. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/Predicates.java`** -> AI Confidence: **99.24%**
2323. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/fulltext/FullTextUtils.java`** -> AI Confidence: **99.24%**
2324. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/Equals.java`** -> AI Confidence: **99.24%**
2325. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EsqlBinaryComparison.java`** -> AI Confidence: **99.24%**
2326. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThan.java`** -> AI Confidence: **99.24%**
2327. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/GreaterThanOrEqual.java`** -> AI Confidence: **99.24%**
2328. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/NotEquals.java`** -> AI Confidence: **99.24%**
2329. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/expression/promql/function/PromqlFunctionRegistry.java`** -> AI Confidence: **99.24%**
2330. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/inference/rerank/RerankOutputBuilder.java`** -> AI Confidence: **99.24%**
2331. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/OptimizerRules.java`** -> AI Confidence: **99.24%**
2332. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/PropagateNullable.java`** -> AI Confidence: **99.24%**
2333. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/PushDownAndCombineLimitBy.java`** -> AI Confidence: **99.24%**
2334. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/PushDownFilterAndLimitIntoUnionAll.java`** -> AI Confidence: **99.24%**
2335. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/SimplifyComparisonsArithmetics.java`** -> AI Confidence: **99.24%**
2336. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/TranslateTimeSeriesAggregate.java`** -> AI Confidence: **99.24%**
2337. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/LucenePushdownPredicates.java`** -> AI Confidence: **99.24%**
2338. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java`** -> AI Confidence: **99.24%**
2339. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushStatsToExternalSource.java`** -> AI Confidence: **99.24%**
2340. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/SpatialShapeDocValuesExtraction.java`** -> AI Confidence: **99.24%**
2341. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/parser/EsqlParser.java`** -> AI Confidence: **99.24%**
2342. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/parser/IdentifierBuilder.java`** -> AI Confidence: **99.24%**
2343. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/parser/LogicalPlanBuilder.java`** -> AI Confidence: **99.24%**
2344. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/parser/ParserUtils.java`** -> AI Confidence: **99.24%**
2345. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plan/logical/Fork.java`** -> AI Confidence: **99.24%**
2346. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/planner/AggregateMapper.java`** -> AI Confidence: **99.24%**
2347. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plugin/ComputeResponse.java`** -> AI Confidence: **99.24%**
2348. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plugin/DataNodeComputeResponse.java`** -> AI Confidence: **99.24%**
2349. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plugin/DataNodeRequestSender.java`** -> AI Confidence: **99.24%**
2350. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/session/EsqlCCSUtils.java`** -> AI Confidence: **99.24%**
2351. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/telemetry/FeatureMetric.java`** -> AI Confidence: **99.24%**
2352. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/type/EsqlDataTypeConverter.java`** -> AI Confidence: **99.24%**
2353. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/view/ViewResolver.java`** -> AI Confidence: **99.24%**
2354. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/IdentifierGenerator.java`** -> AI Confidence: **99.24%**
2355. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/core/querydsl/QueryDslTimestampBoundsExtractorTests.java`** -> AI Confidence: **99.24%**
2356. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/core/util/QueriesTests.java`** -> AI Confidence: **99.24%**
2357. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/evaluator/command/AbstractCompoundOutputEvaluatorTests.java`** -> AI Confidence: **99.24%**
2358. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/evaluator/command/UriPartsFunctionBridgeTests.java`** -> AI Confidence: **99.24%**
2359. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/AbstractAggregationTestCase.java`** -> AI Confidence: **99.24%**
2360. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/ErrorsForCasesWithoutExamplesTestCase.java`** -> AI Confidence: **99.24%**
2361. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/MultivalueTestCaseSupplier.java`** -> AI Confidence: **99.24%**
2362. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/ReferenceAttributeTests.java`** -> AI Confidence: **99.24%**
2363. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/aggregate/RateTests.java`** -> AI Confidence: **99.24%**
2364. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/VaragsTestCaseBuilder.java`** -> AI Confidence: **99.24%**
2365. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/convert/ToDegreesTests.java`** -> AI Confidence: **99.24%**
2366. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateFormatTests.java`** -> AI Confidence: **99.24%**
2367. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/date/DateParseTests.java`** -> AI Confidence: **99.24%**
2368. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/date/MonthNameTests.java`** -> AI Confidence: **99.24%**
2369. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/internal/InternalPacksTests.java`** -> AI Confidence: **99.24%**
2370. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/math/LogTests.java`** -> AI Confidence: **99.24%**
2371. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/math/RoundToTests.java`** -> AI Confidence: **99.24%**
2372. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvDedupeTests.java`** -> AI Confidence: **99.24%**
2373. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvZipTests.java`** -> AI Confidence: **99.24%**
2374. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/spatial/SpatialContainsErrorTests.java`** -> AI Confidence: **99.24%**
2375. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/AddTests.java`** -> AI Confidence: **99.24%**
2376. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/predicate/operator/arithmetic/DivTests.java`** -> AI Confidence: **99.24%**
2377. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/predicate/operator/comparison/EqualsTests.java`** -> AI Confidence: **99.24%**
2378. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/rules/logical/local/ReplaceDateTruncBucketWithRoundToTests.java`** -> AI Confidence: **99.24%**
2379. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/StatementParserTests.java`** -> AI Confidence: **99.24%**
2380. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/promql/PromqlParserTests.java`** -> AI Confidence: **99.24%**
2381. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/logical/LookupSerializationTests.java`** -> AI Confidence: **99.24%**
2382. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/logical/ParameterizedQuerySerializationTests.java`** -> AI Confidence: **99.24%**
2383. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/physical/AggregateExecSerializationTests.java`** -> AI Confidence: **99.24%**
2384. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/physical/LookupJoinExecSerializationTests.java`** -> AI Confidence: **99.24%**
2385. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/physical/inference/CompletionExecSerializationTests.java`** -> AI Confidence: **99.24%**
2386. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/session/ConfigurationSerializationTests.java`** -> AI Confidence: **99.24%**
2387. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/session/FieldNameUtilsTests.java`** -> AI Confidence: **99.24%**
2388. **`x-pack/plugin/frozen-indices/src/test/java/org/elasticsearch/index/engine/frozen/FrozenEngineTests.java`** -> AI Confidence: **99.24%**
2389. **`x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/java/org/elasticsearch/xpack/idp/IdentityProviderAuthenticationIT.java`** -> AI Confidence: **99.24%**
2390. **`x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/java/org/elasticsearch/xpack/idp/ManageServiceProviderRestIT.java`** -> AI Confidence: **99.24%**
2391. **`x-pack/plugin/identity-provider/src/main/java/org/elasticsearch/xpack/idp/privileges/UserPrivilegeResolver.java`** -> AI Confidence: **99.24%**
2392. **`x-pack/plugin/identity-provider/src/main/java/org/elasticsearch/xpack/idp/saml/idp/SamlIdentityProviderBuilder.java`** -> AI Confidence: **99.24%**
2393. **`x-pack/plugin/identity-provider/src/main/java/org/elasticsearch/xpack/idp/saml/sp/SamlServiceProviderDocument.java`** -> AI Confidence: **99.24%**
2394. **`x-pack/plugin/identity-provider/src/test/java/org/elasticsearch/xpack/idp/saml/idp/SamlIdentityProviderBuilderTests.java`** -> AI Confidence: **99.24%**
2395. **`x-pack/plugin/identity-provider/src/test/java/org/elasticsearch/xpack/idp/saml/idp/SamlIdpMetadataBuilderTests.java`** -> AI Confidence: **99.24%**
2396. **`x-pack/plugin/ilm/src/javaRestTest/java/org/elasticsearch/xpack/ilm/CCRIndexLifecycleIT.java`** -> AI Confidence: **99.24%**
2397. **`x-pack/plugin/ilm/src/javaRestTest/java/org/elasticsearch/xpack/ilm/TimeseriesMoveToStepIT.java`** -> AI Confidence: **99.24%**
2398. **`x-pack/plugin/ilm/src/main/java/org/elasticsearch/xpack/ilm/PolicyStepsRegistry.java`** -> AI Confidence: **99.24%**
2399. **`x-pack/plugin/ilm/src/main/java/org/elasticsearch/xpack/ilm/history/ILMHistoryStore.java`** -> AI Confidence: **99.24%**
2400. **`x-pack/plugin/inference/qa/mixed-cluster/src/javaRestTest/java/org/elasticsearch/xpack/inference/qa/mixed/OpenAIServiceMixedIT.java`** -> AI Confidence: **99.24%**
2401. **`x-pack/plugin/inference/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/application/OpenAiServiceUpgradeIT.java`** -> AI Confidence: **99.24%**
2402. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/common/DelegatingProcessor.java`** -> AI Confidence: **99.24%**
2403. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/ServiceUtils.java`** -> AI Confidence: **99.24%**
2404. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/alibabacloudsearch/request/AlibabaCloudSearchEmbeddingsRequestEntity.java`** -> AI Confidence: **99.24%**
2405. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/alibabacloudsearch/response/AlibabaCloudSearchRerankResponseEntity.java`** -> AI Confidence: **99.24%**
2406. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/alibabacloudsearch/response/AlibabaCloudSearchResponseEntity.java`** -> AI Confidence: **99.24%**
2407. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/amazonbedrock/client/AmazonBedrockInferenceClientCache.java`** -> AI Confidence: **99.24%**
2408. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/googlevertexai/request/completion/GoogleVertexAiUnifiedChatCompletionRequestEntity.java`** -> AI Confidence: **99.24%**
2409. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/huggingface/HuggingFaceResponseHandler.java`** -> AI Confidence: **99.24%**
2410. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/jinaai/request/JinaAIEmbeddingsRequestEntity.java`** -> AI Confidence: **99.24%**
2411. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/sagemaker/schema/SageMakerStreamSchema.java`** -> AI Confidence: **99.24%**
2412. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/sagemaker/schema/elastic/ElasticPayload.java`** -> AI Confidence: **99.24%**
2413. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/ai21/completion/Ai21ChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2414. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/ai21/request/Ai21ChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.24%**
2415. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/alibabacloudsearch/request/AlibabaCloudSearchCompletionRequestEntityTests.java`** -> AI Confidence: **99.24%**
2416. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/azureaistudio/response/AzureAiStudioRerankResponseEntityTests.java`** -> AI Confidence: **99.24%**
2417. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/azureopenai/request/AzureOpenAiChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.24%**
2418. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/azureopenai/response/AzureAndOpenAiExternalResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2419. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/custom/response/CompletionResponseParserTests.java`** -> AI Confidence: **99.24%**
2420. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/custom/response/DenseEmbeddingResponseParserTests.java`** -> AI Confidence: **99.24%**
2421. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/custom/response/RerankResponseParserTests.java`** -> AI Confidence: **99.24%**
2422. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/custom/response/SparseEmbeddingResponseParserTests.java`** -> AI Confidence: **99.24%**
2423. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/deepseek/DeepSeekServiceTests.java`** -> AI Confidence: **99.24%**
2424. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/googlevertexai/GoogleVertexAiStreamingProcessorTests.java`** -> AI Confidence: **99.24%**
2425. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/groq/completion/GroqChatCompletionServiceSettingsTests.java`** -> AI Confidence: **99.24%**
2426. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/huggingface/HuggingFaceChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2427. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/huggingface/request/HuggingFaceUnifiedChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.24%**
2428. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/huggingface/response/HuggingFaceRerankResponseEntityTests.java`** -> AI Confidence: **99.24%**
2429. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/jinaai/request/JinaAIRerankRequestEntityTests.java`** -> AI Confidence: **99.24%**
2430. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/llama/completion/LlamaChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2431. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/mistral/MistralUnifiedChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2432. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/mistral/request/completion/MistralChatCompletionRequestEntityTests.java`** -> AI Confidence: **99.24%**
2433. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/nvidia/completion/NvidiaChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2434. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/OpenAiServiceTests.java`** -> AI Confidence: **99.24%**
2435. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/OpenAiStreamingProcessorTests.java`** -> AI Confidence: **99.24%**
2436. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/OpenAiUnifiedChatCompletionResponseHandlerTests.java`** -> AI Confidence: **99.24%**
2437. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openai/action/OpenAiActionCreatorTests.java`** -> AI Confidence: **99.24%**
2438. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/openshiftai/action/OpenShiftAiActionCreatorTests.java`** -> AI Confidence: **99.24%**
2439. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/sagemaker/schema/elastic/ElasticCompletionPayloadTests.java`** -> AI Confidence: **99.24%**
2440. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/voyageai/response/VoyageAIRerankResponseEntityTests.java`** -> AI Confidence: **99.24%**
2441. **`x-pack/plugin/kql/src/test/java/org/elasticsearch/xpack/kql/parser/KqlNestedFieldQueryTests.java`** -> AI Confidence: **99.24%**
2442. **`x-pack/plugin/kql/src/test/java/org/elasticsearch/xpack/kql/parser/KqlParserFieldlessQueryTests.java`** -> AI Confidence: **99.24%**
2443. **`x-pack/plugin/logsdb/qa/legacy-rolling-upgrade/src/javaRestTest/java/org/elasticsearch/upgrades/LogsUsageRollingUpgradeIT.java`** -> AI Confidence: **99.24%**
2444. **`x-pack/plugin/logsdb/qa/rolling-upgrade/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/TSDBSyntheticIdUpgradeIT.java`** -> AI Confidence: **99.24%**
2445. **`x-pack/plugin/logsdb/src/test/java/org/elasticsearch/xpack/logsdb/LogsdbIndexModeSettingsProviderTests.java`** -> AI Confidence: **99.24%**
2446. **`x-pack/plugin/logsdb/src/test/java/org/elasticsearch/xpack/logsdb/LogsdbLicenseServiceTests.java`** -> AI Confidence: **99.24%**
2447. **`x-pack/plugin/logsdb/src/test/java/org/elasticsearch/xpack/logsdb/patterntext/PatternTextNestedObjectTests.java`** -> AI Confidence: **99.24%**
2448. **`x-pack/plugin/logstash/src/main/java/org/elasticsearch/xpack/logstash/action/TransportGetPipelineAction.java`** -> AI Confidence: **99.24%**
2449. **`x-pack/plugin/mapper-aggregate-metric/src/main/java/org/elasticsearch/xpack/aggregatemetric/mapper/AggregateMetricDoubleBlockLoader.java`** -> AI Confidence: **99.24%**
2450. **`x-pack/plugin/mapper-unsigned-long/src/main/java/org/elasticsearch/xpack/unsignedlong/UnsignedLongFieldMapper.java`** -> AI Confidence: **99.24%**
2451. **`x-pack/plugin/migrate/src/main/java/org/elasticsearch/system_indices/action/TransportGetFeatureUpgradeStatusAction.java`** -> AI Confidence: **99.24%**
2452. **`x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceTransportAction.java`** -> AI Confidence: **99.24%**
2453. **`x-pack/plugin/ml-package-loader/src/main/java/org/elasticsearch/xpack/ml/packageloader/action/ModelLoaderUtils.java`** -> AI Confidence: **99.24%**
2454. **`x-pack/plugin/ml/qa/ml-with-security/src/yamlRestTest/java/org/elasticsearch/smoketest/MlWithSecurityUserRoleIT.java`** -> AI Confidence: **99.24%**
2455. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/ExplainDataFrameAnalyticsRestIT.java`** -> AI Confidence: **99.24%**
2456. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/PyTorchModelIT.java`** -> AI Confidence: **99.24%**
2457. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/PyTorchModelRestTestCase.java`** -> AI Confidence: **99.24%**
2458. **`x-pack/plugin/ml/qa/native-multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/TextExpansionQueryIT.java`** -> AI Confidence: **99.24%**
2459. **`x-pack/plugin/ml/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/InferenceProcessorIT.java`** -> AI Confidence: **99.24%**
2460. **`x-pack/plugin/ml/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/ml/integration/InferenceTestCase.java`** -> AI Confidence: **99.24%**
2461. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/MlMetrics.java`** -> AI Confidence: **99.24%**
2462. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportForecastJobAction.java`** -> AI Confidence: **99.24%**
2463. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportGetDeploymentStatsAction.java`** -> AI Confidence: **99.24%**
2464. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportRevertModelSnapshotAction.java`** -> AI Confidence: **99.24%**
2465. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportStopDataFrameAnalyticsAction.java`** -> AI Confidence: **99.24%**
2466. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/ChangeDetector.java`** -> AI Confidence: **99.24%**
2467. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/inference/InferencePipelineAggregator.java`** -> AI Confidence: **99.24%**
2468. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/autoscaling/MlAutoscalingResourceTracker.java`** -> AI Confidence: **99.24%**
2469. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/datafeed/extractor/chunked/ChunkedDataExtractor.java`** -> AI Confidence: **99.24%**
2470. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/dataframe/process/MemoryUsageEstimationProcessManager.java`** -> AI Confidence: **99.24%**
2471. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/adaptiveallocations/AdaptiveAllocationsScalerService.java`** -> AI Confidence: **99.24%**
2472. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/TrainedModelAssignmentClusterService.java`** -> AI Confidence: **99.24%**
2473. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/assignment/planning/AssignmentPlan.java`** -> AI Confidence: **99.24%**
2474. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/deployment/InferencePyTorchAction.java`** -> AI Confidence: **99.24%**
2475. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/loadingservice/ModelLoadingService.java`** -> AI Confidence: **99.24%**
2476. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/ltr/LearningToRankRescorer.java`** -> AI Confidence: **99.24%**
2477. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/BertTokenizationResult.java`** -> AI Confidence: **99.24%**
2478. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/ControlCharFilter.java`** -> AI Confidence: **99.24%**
2479. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/DebertaTokenizationResult.java`** -> AI Confidence: **99.24%**
2480. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/MPNetTokenizationResult.java`** -> AI Confidence: **99.24%**
2481. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/PrecompiledCharMapNormalizer.java`** -> AI Confidence: **99.24%**
2482. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/RobertaTokenizationResult.java`** -> AI Confidence: **99.24%**
2483. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/TokenizationResult.java`** -> AI Confidence: **99.24%**
2484. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/inference/persistence/TrainedModelProvider.java`** -> AI Confidence: **99.24%**
2485. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/NodeLoadDetector.java`** -> AI Confidence: **99.24%**
2486. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/persistence/JobRenormalizedResultsPersister.java`** -> AI Confidence: **99.24%**
2487. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/process/autodetect/JobModelSnapshotUpgrader.java`** -> AI Confidence: **99.24%**
2488. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/process/autodetect/writer/XContentRecordReader.java`** -> AI Confidence: **99.24%**
2489. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/process/normalizer/ScoresUpdater.java`** -> AI Confidence: **99.24%**
2490. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/job/retention/UnusedStateRemover.java`** -> AI Confidence: **99.24%**
2491. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/process/ProcessPipes.java`** -> AI Confidence: **99.24%**
2492. **`x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/utils/NativeMemoryCalculator.java`** -> AI Confidence: **99.24%**
2493. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/aggs/categorization/TokenListCategorizerTests.java`** -> AI Confidence: **99.24%**
2494. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/datafeed/extractor/aggregation/AggregationTestUtils.java`** -> AI Confidence: **99.24%**
2495. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/datafeed/extractor/scroll/ScrollDataExtractorTests.java`** -> AI Confidence: **99.24%**
2496. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/dataframe/traintestsplit/StratifiedTrainTestSplitterTests.java`** -> AI Confidence: **99.24%**
2497. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/inference/nlp/tokenizers/CharSeqTokenTrieNodeTests.java`** -> AI Confidence: **99.24%**
2498. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/categorization/CategorizationAnalyzerTests.java`** -> AI Confidence: **99.24%**
2499. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/config/CategorizationAnalyzerConfigTests.java`** -> AI Confidence: **99.24%**
2500. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/config/JobBuilderTests.java`** -> AI Confidence: **99.24%**
2501. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/config/OperatorTests.java`** -> AI Confidence: **99.24%**
2502. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/results/AutodetectResultTests.java`** -> AI Confidence: **99.24%**
2503. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/results/ForecastRequestStatsTests.java`** -> AI Confidence: **99.24%**
2504. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/process/writer/LengthEncodedWriterTests.java`** -> AI Confidence: **99.24%**
2505. **`x-pack/plugin/monitoring/src/main/java/org/elasticsearch/xpack/monitoring/collector/TimeoutUtils.java`** -> AI Confidence: **99.24%**
2506. **`x-pack/plugin/monitoring/src/main/java/org/elasticsearch/xpack/monitoring/exporter/http/ClusterAlertHttpResource.java`** -> AI Confidence: **99.24%**
2507. **`x-pack/plugin/monitoring/src/main/java/org/elasticsearch/xpack/monitoring/exporter/http/HttpExporter.java`** -> AI Confidence: **99.24%**
2508. **`x-pack/plugin/monitoring/src/main/java/org/elasticsearch/xpack/monitoring/exporter/local/LocalBulk.java`** -> AI Confidence: **99.24%**
2509. **`x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/exporter/http/WatcherExistsHttpResourceTests.java`** -> AI Confidence: **99.24%**
2510. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/index/LegacyDocValuesIterables.java`** -> AI Confidence: **99.24%**
2511. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/IntersectTermsEnumFrame.java`** -> AI Confidence: **99.24%**
2512. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene50/Lucene50FieldInfosFormat.java`** -> AI Confidence: **99.24%**
2513. **`x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene70/fst/FST.java`** -> AI Confidence: **99.24%**
2514. **`x-pack/plugin/otel-data/src/test/java/org/elasticsearch/xpack/oteldata/otlp/datapoint/HistogramToExponentialHistogramConverterTests.java`** -> AI Confidence: **99.24%**
2515. **`x-pack/plugin/profiling/src/main/java/org/elasticsearch/xpack/profiling/action/InstanceType.java`** -> AI Confidence: **99.24%**
2516. **`x-pack/plugin/profiling/src/main/java/org/elasticsearch/xpack/profiling/action/KvIndexResolver.java`** -> AI Confidence: **99.24%**
2517. **`x-pack/plugin/profiling/src/main/java/org/elasticsearch/xpack/profiling/action/SubGroup.java`** -> AI Confidence: **99.24%**
2518. **`x-pack/plugin/prometheus/src/main/java/org/elasticsearch/xpack/prometheus/rest/PrometheusLabelValuesResponseListener.java`** -> AI Confidence: **99.24%**
2519. **`x-pack/plugin/prometheus/src/main/java/org/elasticsearch/xpack/prometheus/rest/PrometheusQueryRangeResponseListener.java`** -> AI Confidence: **99.24%**
2520. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/execution/search/extractor/AbstractFieldHitExtractor.java`** -> AI Confidence: **99.24%**
2521. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/TypeResolutions.java`** -> AI Confidence: **99.24%**
2522. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/gen/processor/ConstantProcessor.java`** -> AI Confidence: **99.24%**
2523. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/predicate/fulltext/FullTextUtils.java`** -> AI Confidence: **99.24%**
2524. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/index/IndexResolver.java`** -> AI Confidence: **99.24%**
2525. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/rule/RuleExecutor.java`** -> AI Confidence: **99.24%**
2526. **`x-pack/plugin/rank-rrf/src/internalClusterTest/java/org/elasticsearch/xpack/rank/rrf/RRFRetrieverBuilderNestedDocsIT.java`** -> AI Confidence: **99.24%**
2527. **`x-pack/plugin/rank-rrf/src/main/java/org/elasticsearch/xpack/rank/linear/LinearRetrieverBuilder.java`** -> AI Confidence: **99.24%**
2528. **`x-pack/plugin/rank-rrf/src/main/java/org/elasticsearch/xpack/rank/rrf/RRFQueryPhaseRankCoordinatorContext.java`** -> AI Confidence: **99.24%**
2529. **`x-pack/plugin/rank-vectors/src/test/java/org/elasticsearch/xpack/rank/vectors/mapper/RankVectorsFieldMapperTests.java`** -> AI Confidence: **99.24%**
2530. **`x-pack/plugin/rollup/src/main/java/org/elasticsearch/xpack/rollup/RollupRequestTranslator.java`** -> AI Confidence: **99.24%**
2531. **`x-pack/plugin/searchable-snapshots/src/internalClusterTest/java/org/elasticsearch/xpack/searchablesnapshots/SearchableSnapshotsRepositoryIntegTests.java`** -> AI Confidence: **99.24%**
2532. **`x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/store/input/CachedBlobContainerIndexInput.java`** -> AI Confidence: **99.24%**
2533. **`x-pack/plugin/searchable-snapshots/src/test/java/org/elasticsearch/xpack/searchablesnapshots/AbstractSearchableSnapshotsRestTestCase.java`** -> AI Confidence: **99.24%**
2534. **`x-pack/plugin/searchable-snapshots/src/test/java/org/elasticsearch/xpack/searchablesnapshots/store/SearchableSnapshotDirectoryStatsTests.java`** -> AI Confidence: **99.24%**
2535. **`x-pack/plugin/security/cli/src/main/java/org/elasticsearch/xpack/security/cli/CertificateTool.java`** -> AI Confidence: **99.24%**
2536. **`x-pack/plugin/security/cli/src/test/java/org/elasticsearch/xpack/security/cli/CertificateGenerateToolTests.java`** -> AI Confidence: **99.24%**
2537. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityCcrIT.java`** -> AI Confidence: **99.24%**
2538. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityCrossClusterApiKeySigningIT.java`** -> AI Confidence: **99.24%**
2539. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityLegacyCrossClusterApiKeysWithDlsFlsIT.java`** -> AI Confidence: **99.24%**
2540. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS1DeprecationIT.java`** -> AI Confidence: **99.24%**
2541. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS1ResolveClusterIT.java`** -> AI Confidence: **99.24%**
2542. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRCS2ResolveClusterIT.java`** -> AI Confidence: **99.24%**
2543. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityWithMixedModelRemotesRestIT.java`** -> AI Confidence: **99.24%**
2544. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterWithoutSecurityFailureStoreRestIT.java`** -> AI Confidence: **99.24%**
2545. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/DocumentLevelSecurityTests.java`** -> AI Confidence: **99.24%**
2546. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/FieldLevelSecurityFeatureUsageTests.java`** -> AI Confidence: **99.24%**
2547. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/FieldLevelSecurityTests.java`** -> AI Confidence: **99.24%**
2548. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/InternalUserAndRoleIntegTests.java`** -> AI Confidence: **99.24%**
2549. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/MultipleIndicesPermissionsTests.java`** -> AI Confidence: **99.24%**
2550. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/integration/PermissionPrecedenceTests.java`** -> AI Confidence: **99.24%**
2551. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/authc/RunAsIntegTests.java`** -> AI Confidence: **99.24%**
2552. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/authc/SecurityRealmSettingsTests.java`** -> AI Confidence: **99.24%**
2553. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/authc/pki/PkiAuthDelegationIntegTests.java`** -> AI Confidence: **99.24%**
2554. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/authz/store/NativePrivilegeStoreCacheTests.java`** -> AI Confidence: **99.24%**
2555. **`x-pack/plugin/security/src/internalClusterTest/java/org/elasticsearch/xpack/security/profile/ProfileUidIntegTests.java`** -> AI Confidence: **99.24%**
2556. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/core/security/transport/ProfileConfigurations.java`** -> AI Confidence: **99.24%**
2557. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/action/TransportGrantAction.java`** -> AI Confidence: **99.24%**
2558. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/action/user/TransportGetUsersAction.java`** -> AI Confidence: **99.24%**
2559. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/audit/logfile/LoggingAuditTrail.java`** -> AI Confidence: **99.24%**
2560. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/CrossClusterAccessAuthenticationService.java`** -> AI Confidence: **99.24%**
2561. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/PluggableAuthenticatorChain.java`** -> AI Confidence: **99.24%**
2562. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/Realms.java`** -> AI Confidence: **99.24%**
2563. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/esnative/ReservedRealm.java`** -> AI Confidence: **99.24%**
2564. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/file/FileUserRolesStore.java`** -> AI Confidence: **99.24%**
2565. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/jwt/JwtRealm.java`** -> AI Confidence: **99.24%**
2566. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/jwt/JwtSignatureValidator.java`** -> AI Confidence: **99.24%**
2567. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ldap/support/LdapMetadataResolver.java`** -> AI Confidence: **99.24%**
2568. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/pki/PkiRealm.java`** -> AI Confidence: **99.24%**
2569. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/service/CachingServiceAccountTokenStore.java`** -> AI Confidence: **99.24%**
2570. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/support/ClaimParser.java`** -> AI Confidence: **99.24%**
2571. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/support/mapper/NativeRoleMappingStore.java`** -> AI Confidence: **99.24%**
2572. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authz/RBACEngine.java`** -> AI Confidence: **99.24%**
2573. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authz/store/FileRolesStore.java`** -> AI Confidence: **99.24%**
2574. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/profile/ProfileService.java`** -> AI Confidence: **99.24%**
2575. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/support/CacheInvalidatorRegistry.java`** -> AI Confidence: **99.24%**
2576. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/support/FieldNameTranslators.java`** -> AI Confidence: **99.24%**
2577. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/support/QueryableBuiltInRolesSynchronizer.java`** -> AI Confidence: **99.24%**
2578. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/transport/CrossClusterApiKeySignatureManager.java`** -> AI Confidence: **99.24%**
2579. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/transport/filter/SecurityIpFilterRule.java`** -> AI Confidence: **99.24%**
2580. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/action/SecurityActionMapperTests.java`** -> AI Confidence: **99.24%**
2581. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/RealmsAuthenticatorTests.java`** -> AI Confidence: **99.24%**
2582. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtAuthenticatorTests.java`** -> AI Confidence: **99.24%**
2583. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtRealmAuthenticateAccessTokenTypeTests.java`** -> AI Confidence: **99.24%**
2584. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtRealmGenerateTests.java`** -> AI Confidence: **99.24%**
2585. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/jwt/JwtTestCase.java`** -> AI Confidence: **99.24%**
2586. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlAuthenticatorTests.java`** -> AI Confidence: **99.24%**
2587. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlMetadataCommandTests.java`** -> AI Confidence: **99.24%**
2588. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlRedirectTests.java`** -> AI Confidence: **99.24%**
2589. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/support/TokensInvalidationResultTests.java`** -> AI Confidence: **99.24%**
2590. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/operator/DefaultOperatorOnlyRegistryTests.java`** -> AI Confidence: **99.24%**
2591. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/operator/FileOperatorUsersStoreTests.java`** -> AI Confidence: **99.24%**
2592. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/rest/action/user/RestGetUserPrivilegesActionTests.java`** -> AI Confidence: **99.24%**
2593. **`x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/transport/filter/SecurityIpFilterRuleTests.java`** -> AI Confidence: **99.24%**
2594. **`x-pack/plugin/slm/src/javaRestTest/java/org/elasticsearch/xpack/slm/SnapshotLifecycleRestIT.java`** -> AI Confidence: **99.24%**
2595. **`x-pack/plugin/snapshot-repo-test-kit/src/main/java/org/elasticsearch/repositories/blobstore/testkit/analyze/BlobAnalyzeAction.java`** -> AI Confidence: **99.24%**
2596. **`x-pack/plugin/snapshot-repo-test-kit/src/main/java/org/elasticsearch/repositories/blobstore/testkit/integrity/RepositoryVerifyIntegrityParams.java`** -> AI Confidence: **99.24%**
2597. **`x-pack/plugin/snapshot-repo-test-kit/src/test/java/org/elasticsearch/repositories/blobstore/testkit/analyze/RandomBlobContentStreamTests.java`** -> AI Confidence: **99.24%**
2598. **`x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/search/aggregations/bucket/geogrid/GeoHexVisitor.java`** -> AI Confidence: **99.24%**
2599. **`x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/search/aggregations/bucket/geogrid/GeoTileGridTiler.java`** -> AI Confidence: **99.24%**
2600. **`x-pack/plugin/spatial/src/test/java/org/elasticsearch/xpack/spatial/index/mapper/GeometricShapeSyntheticSourceSupport.java`** -> AI Confidence: **99.24%**
2601. **`x-pack/plugin/spatial/src/test/java/org/elasticsearch/xpack/spatial/index/mapper/PointFieldBlockLoaderTests.java`** -> AI Confidence: **99.24%**
2602. **`x-pack/plugin/spatial/src/test/java/org/elasticsearch/xpack/spatial/search/aggregations/InternalGeoLineTests.java`** -> AI Confidence: **99.24%**
2603. **`x-pack/plugin/spatial/src/test/java/org/elasticsearch/xpack/spatial/search/aggregations/metrics/InternalCartesianCentroidTests.java`** -> AI Confidence: **99.24%**
2604. **`x-pack/plugin/sql/jdbc/src/main/java/org/elasticsearch/xpack/sql/jdbc/JdbcConfiguration.java`** -> AI Confidence: **99.24%**
2605. **`x-pack/plugin/sql/qa/jdbc/src/javaRestTest/java/org/elasticsearch/xpack/sql/qa/jdbc/single_node/SingleNodeJdbcShardFailureIT.java`** -> AI Confidence: **99.24%**
2606. **`x-pack/plugin/sql/qa/jdbc/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/FetchSizeTestCase.java`** -> AI Confidence: **99.24%**
2607. **`x-pack/plugin/sql/sql-action/src/main/java/org/elasticsearch/xpack/sql/action/SqlQueryResponse.java`** -> AI Confidence: **99.24%**
2608. **`x-pack/plugin/sql/sql-action/src/test/java/org/elasticsearch/xpack/sql/action/SqlQueryResponseTests.java`** -> AI Confidence: **99.24%**
2609. **`x-pack/plugin/sql/sql-cli/src/main/java/org/elasticsearch/xpack/sql/cli/ConnectionBuilder.java`** -> AI Confidence: **99.24%**
2610. **`x-pack/plugin/sql/sql-cli/src/main/java/org/elasticsearch/xpack/sql/cli/command/ServerQueryCliCommand.java`** -> AI Confidence: **99.24%**
2611. **`x-pack/plugin/sql/sql-cli/src/test/java/org/elasticsearch/xpack/sql/cli/ConnectionBuilderTests.java`** -> AI Confidence: **99.24%**
2612. **`x-pack/plugin/sql/sql-client/src/main/java/org/elasticsearch/xpack/sql/client/JreHttpUrlConnection.java`** -> AI Confidence: **99.24%**
2613. **`x-pack/plugin/sql/sql-client/src/test/java/org/elasticsearch/xpack/sql/client/RemoteFailureTests.java`** -> AI Confidence: **99.24%**
2614. **`x-pack/plugin/sql/sql-proto/src/main/java/org/elasticsearch/xpack/sql/proto/StringUtils.java`** -> AI Confidence: **99.24%**
2615. **`x-pack/plugin/sql/sql-proto/src/main/java/org/elasticsearch/xpack/sql/proto/content/ConstructingObjectParser.java`** -> AI Confidence: **99.24%**
2616. **`x-pack/plugin/sql/sql-proto/src/main/java/org/elasticsearch/xpack/sql/proto/content/ParserUtils.java`** -> AI Confidence: **99.24%**
2617. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/analysis/analyzer/Analyzer.java`** -> AI Confidence: **99.24%**
2618. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/execution/search/PivotRowSet.java`** -> AI Confidence: **99.24%**
2619. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/execution/search/SourceGenerator.java`** -> AI Confidence: **99.24%**
2620. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/expression/predicate/conditional/Case.java`** -> AI Confidence: **99.24%**
2621. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/plan/logical/command/sys/SysTables.java`** -> AI Confidence: **99.24%**
2622. **`x-pack/plugin/sql/src/main/java/org/elasticsearch/xpack/sql/type/SqlDataTypes.java`** -> AI Confidence: **99.24%**
2623. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/ProcessorTests.java`** -> AI Confidence: **99.24%**
2624. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DatePartPipeTests.java`** -> AI Confidence: **99.24%**
2625. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateTimeFormatPipeTests.java`** -> AI Confidence: **99.24%**
2626. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateTimeParseProcessorTests.java`** -> AI Confidence: **99.24%**
2627. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateTruncPipeTests.java`** -> AI Confidence: **99.24%**
2628. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateTruncProcessorTests.java`** -> AI Confidence: **99.24%**
2629. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/string/ReplaceFunctionPipeTests.java`** -> AI Confidence: **99.24%**
2630. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/string/SubstringFunctionPipeTests.java`** -> AI Confidence: **99.24%**
2631. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/literal/interval/IntervalsTests.java`** -> AI Confidence: **99.24%**
2632. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/parser/SqlParserTests.java`** -> AI Confidence: **99.24%**
2633. **`x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/type/SqlDataTypeConverterTests.java`** -> AI Confidence: **99.24%**
2634. **`x-pack/plugin/stack/src/javaRestTest/java/org/elasticsearch/xpack/stack/EcsDynamicTemplatesIT.java`** -> AI Confidence: **99.24%**
2635. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/GrokPatternCreator.java`** -> AI Confidence: **99.24%**
2636. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/NdJsonTextStructureFinderFactory.java`** -> AI Confidence: **99.24%**
2637. **`x-pack/plugin/text-structure/src/main/java/org/elasticsearch/xpack/textstructure/structurefinder/TextStructureFinderManager.java`** -> AI Confidence: **99.24%**
2638. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformInsufficientPermissionsIT.java`** -> AI Confidence: **99.24%**
2639. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/continuous/LatestContinuousIT.java`** -> AI Confidence: **99.24%**
2640. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/continuous/TermsGroupByIT.java`** -> AI Confidence: **99.24%**
2641. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/continuous/TermsOnDateGroupByIT.java`** -> AI Confidence: **99.24%**
2642. **`x-pack/plugin/transform/qa/multi-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/continuous/TransformContinuousIT.java`** -> AI Confidence: **99.24%**
2643. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformDestIndexIT.java`** -> AI Confidence: **99.24%**
2644. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformGetAndGetStatsIT.java`** -> AI Confidence: **99.24%**
2645. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformResetIT.java`** -> AI Confidence: **99.24%**
2646. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformScheduleNowIT.java`** -> AI Confidence: **99.24%**
2647. **`x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformUsageIT.java`** -> AI Confidence: **99.24%**
2648. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/action/TransportGetTransformStatsAction.java`** -> AI Confidence: **99.24%**
2649. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/action/TransportStopTransformAction.java`** -> AI Confidence: **99.24%**
2650. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/TransformIndexer.java`** -> AI Confidence: **99.24%**
2651. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/TransformTask.java`** -> AI Confidence: **99.24%**
2652. **`x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/pivot/TransformAggregations.java`** -> AI Confidence: **99.24%**
2653. **`x-pack/plugin/vector-tile/src/main/java/org/elasticsearch/xpack/vectortile/feature/PatchedJtsAdapter.java`** -> AI Confidence: **99.24%**
2654. **`x-pack/plugin/vector-tile/src/main/java/org/elasticsearch/xpack/vectortile/rest/RestVectorTileAction.java`** -> AI Confidence: **99.24%**
2655. **`x-pack/plugin/vector-tile/src/main/java/org/elasticsearch/xpack/vectortile/rest/VectorTileRequest.java`** -> AI Confidence: **99.24%**
2656. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/actions/index/ExecutableIndexAction.java`** -> AI Confidence: **99.24%**
2657. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/actions/jira/ExecutableJiraAction.java`** -> AI Confidence: **99.24%**
2658. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/common/http/HttpRequest.java`** -> AI Confidence: **99.24%**
2659. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/condition/ArrayCompareCondition.java`** -> AI Confidence: **99.24%**
2660. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/input/search/SearchInput.java`** -> AI Confidence: **99.24%**
2661. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/email/Account.java`** -> AI Confidence: **99.24%**
2662. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/email/Profile.java`** -> AI Confidence: **99.24%**
2663. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/jira/JiraIssue.java`** -> AI Confidence: **99.24%**
2664. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/notification/slack/message/Field.java`** -> AI Confidence: **99.24%**
2665. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/support/search/WatcherSearchTemplateRequest.java`** -> AI Confidence: **99.24%**
2666. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/HourlySchedule.java`** -> AI Confidence: **99.24%**
2667. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/engine/TickerScheduleTriggerEngine.java`** -> AI Confidence: **99.24%**
2668. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/support/MonthTimes.java`** -> AI Confidence: **99.24%**
2669. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/support/WeekTimes.java`** -> AI Confidence: **99.24%**
2670. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/support/YearTimes.java`** -> AI Confidence: **99.24%**
2671. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/trigger/schedule/tool/CronEvalTool.java`** -> AI Confidence: **99.24%**
2672. **`x-pack/plugin/watcher/src/main/java/org/elasticsearch/xpack/watcher/watch/WatchParser.java`** -> AI Confidence: **99.24%**
2673. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/actions/email/EmailActionTests.java`** -> AI Confidence: **99.24%**
2674. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/notification/jira/JiraIssueTests.java`** -> AI Confidence: **99.24%**
2675. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/notification/pagerduty/IncidentEventTests.java`** -> AI Confidence: **99.24%**
2676. **`x-pack/plugin/watcher/src/test/java/org/elasticsearch/xpack/watcher/trigger/schedule/ScheduleTestCase.java`** -> AI Confidence: **99.24%**
2677. **`x-pack/qa/oidc-op-tests/src/javaRestTest/java/org/elasticsearch/xpack/security/authc/oidc/OpenIdConnectAuthIT.java`** -> AI Confidence: **99.24%**
2678. **`x-pack/qa/repository-old-versions/src/test/java/org/elasticsearch/oldrepos/OldRepositoryAccessIT.java`** -> AI Confidence: **99.24%**
2679. **`x-pack/qa/rolling-upgrade-multi-cluster/src/test/java/org/elasticsearch/upgrades/AbstractMultiClusterUpgradeTestCase.java`** -> AI Confidence: **99.24%**
2680. **`x-pack/qa/security-setup-password-tests/src/javaRestTest/java/org/elasticsearch/xpack/security/authc/esnative/tool/ResetPasswordToolIT.java`** -> AI Confidence: **99.24%**
2681. **`x-pack/qa/third-party/active-directory/src/test/java/org/elasticsearch/xpack/security/authc/ldap/AbstractAdLdapRealmTestCase.java`** -> AI Confidence: **99.24%**
2682. **`build-tools/src/testFixtures/groovy/org/elasticsearch/gradle/fixtures/WiremockFixture.groovy`** -> AI Confidence: **99.24%**
2683. **`libs/simdvec/native/src/vec/c/amd64/score_2.cpp`** -> AI Confidence: **99.24%**
2684. **`build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dra/DraResolvePlugin.java`** -> AI Confidence: **99.23%**
2685. **`build-tools/src/main/java/org/elasticsearch/gradle/LazyPropertyList.java`** -> AI Confidence: **99.23%**
2686. **`distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/PluginSecurity.java`** -> AI Confidence: **99.23%**
2687. **`libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyChecker.java`** -> AI Confidence: **99.23%**
2688. **`libs/exponential-histogram/src/main/java/org/elasticsearch/exponentialhistogram/ExponentialHistogramXContent.java`** -> AI Confidence: **99.23%**
2689. **`libs/exponential-histogram/src/test/java/org/elasticsearch/exponentialhistogram/MergerFactoryImplTests.java`** -> AI Confidence: **99.23%**
2690. **`libs/grok/src/main/java/org/elasticsearch/grok/GrokCaptureConfig.java`** -> AI Confidence: **99.23%**
2691. **`libs/simdvec/src/main/java/org/elasticsearch/simdvec/ESNextOSQVectorsScorer.java`** -> AI Confidence: **99.23%**
2692. **`libs/ssl-config/src/main/java/org/elasticsearch/common/ssl/SslFileUtil.java`** -> AI Confidence: **99.23%**
2693. **`modules/aggregations/src/test/java/org/elasticsearch/aggregations/bucket/adjacency/InternalAdjacencyMatrixTests.java`** -> AI Confidence: **99.23%**
2694. **`modules/lang-painless/src/main/java/org/elasticsearch/painless/ClassWriter.java`** -> AI Confidence: **99.23%**
2695. **`modules/transport-netty4/src/main/java/org/elasticsearch/transport/netty4/NetUtils.java`** -> AI Confidence: **99.23%**
2696. **`qa/packaging/src/test/java/org/elasticsearch/packaging/util/LintianResultParser.java`** -> AI Confidence: **99.23%**
2697. **`server/src/main/java/org/elasticsearch/common/IndexNameGenerator.java`** -> AI Confidence: **99.23%**
2698. **`server/src/main/java/org/elasticsearch/common/Table.java`** -> AI Confidence: **99.23%**
2699. **`server/src/main/java/org/elasticsearch/common/io/stream/BufferedStreamOutput.java`** -> AI Confidence: **99.23%**
2700. **`server/src/main/java/org/elasticsearch/common/lucene/search/AutomatonQueries.java`** -> AI Confidence: **99.23%**
2701. **`server/src/main/java/org/elasticsearch/common/settings/SettingsFilter.java`** -> AI Confidence: **99.23%**
2702. **`server/src/main/java/org/elasticsearch/common/util/BitArray.java`** -> AI Confidence: **99.23%**
2703. **`server/src/main/java/org/elasticsearch/index/codec/vectors/AbstractHnswVectorsFormat.java`** -> AI Confidence: **99.23%**
2704. **`server/src/main/java/org/elasticsearch/index/mapper/NestedLookup.java`** -> AI Confidence: **99.23%**
2705. **`server/src/main/java/org/elasticsearch/index/mapper/SortedNumericWithOffsetsDocValuesSyntheticFieldLoaderLayer.java`** -> AI Confidence: **99.23%**
2706. **`server/src/main/java/org/elasticsearch/indices/store/CompositeIndexFoldersDeletionListener.java`** -> AI Confidence: **99.23%**
2707. **`server/src/main/java/org/elasticsearch/inference/InferenceServiceResults.java`** -> AI Confidence: **99.23%**
2708. **`server/src/main/java/org/elasticsearch/ingest/ConditionalProcessor.java`** -> AI Confidence: **99.23%**
2709. **`server/src/main/java/org/elasticsearch/search/SearchSortValuesAndFormats.java`** -> AI Confidence: **99.23%**
2710. **`server/src/main/java/org/elasticsearch/search/aggregations/MultiBucketCollector.java`** -> AI Confidence: **99.23%**
2711. **`server/src/test/java/org/elasticsearch/cluster/metadata/AliasMetadataTests.java`** -> AI Confidence: **99.23%**
2712. **`server/src/test/java/org/elasticsearch/cluster/metadata/ShutdownPersistentTasksStatusTests.java`** -> AI Confidence: **99.23%**
2713. **`server/src/test/java/org/elasticsearch/common/geo/SimpleFeatureFactoryTests.java`** -> AI Confidence: **99.23%**
2714. **`server/src/test/java/org/elasticsearch/common/io/stream/CountingFilterInputStreamTests.java`** -> AI Confidence: **99.23%**
2715. **`server/src/test/java/org/elasticsearch/common/util/CancellableThreadsTests.java`** -> AI Confidence: **99.23%**
2716. **`server/src/test/java/org/elasticsearch/health/node/HealthInfoTests.java`** -> AI Confidence: **99.23%**
2717. **`server/src/test/java/org/elasticsearch/index/engine/LuceneChangesSnapshotTests.java`** -> AI Confidence: **99.23%**
2718. **`server/src/test/java/org/elasticsearch/index/mapper/StoredNumericValuesTests.java`** -> AI Confidence: **99.23%**
2719. **`server/src/test/java/org/elasticsearch/index/mapper/blockloader/KeywordFieldBlockLoaderTests.java`** -> AI Confidence: **99.23%**
2720. **`server/src/test/java/org/elasticsearch/index/query/MatchIntervalsSourceProviderTests.java`** -> AI Confidence: **99.23%**
2721. **`server/src/test/java/org/elasticsearch/index/reindex/SearchFailureWireSerialisationTests.java`** -> AI Confidence: **99.23%**
2722. **`server/src/test/java/org/elasticsearch/indices/TermsLookupTests.java`** -> AI Confidence: **99.23%**
2723. **`server/src/test/java/org/elasticsearch/search/aggregations/AggregationTestScriptsPlugin.java`** -> AI Confidence: **99.23%**
2724. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalAvgTests.java`** -> AI Confidence: **99.23%**
2725. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalMedianAbsoluteDeviationTests.java`** -> AI Confidence: **99.23%**
2726. **`server/src/test/java/org/elasticsearch/search/aggregations/metrics/InternalTDigestPercentilesRanksTests.java`** -> AI Confidence: **99.23%**
2727. **`test/framework/src/main/java/org/elasticsearch/common/logging/TestLoggers.java`** -> AI Confidence: **99.23%**
2728. **`test/test-clusters/src/main/java/org/elasticsearch/test/cluster/local/DefaultSettingsProvider.java`** -> AI Confidence: **99.23%**
2729. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/analytics/mapper/TDigestParser.java`** -> AI Confidence: **99.23%**
2730. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/inference/results/ModelStoreResponse.java`** -> AI Confidence: **99.23%**
2731. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ml/utils/MlStrings.java`** -> AI Confidence: **99.23%**
2732. **`x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/watcher/common/stats/Counters.java`** -> AI Confidence: **99.23%**
2733. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/datastreams/TimeSeriesFeatureSetUsageTests.java`** -> AI Confidence: **99.23%**
2734. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/job/process/autodetect/state/ModelSizeStatsTests.java`** -> AI Confidence: **99.23%**
2735. **`x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/job/results/AnomalyCauseTests.java`** -> AI Confidence: **99.23%**
2736. **`x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/DeprecationInfoActionResponseTests.java`** -> AI Confidence: **99.23%**
2737. **`x-pack/plugin/enrich/src/javaRestTest/java/org/elasticsearch/test/enrich/EnrichAdvancedSecurityIT.java`** -> AI Confidence: **99.23%**
2738. **`x-pack/plugin/eql/qa/common/src/main/java/org/elasticsearch/test/eql/EqlSpecLoader.java`** -> AI Confidence: **99.23%**
2739. **`x-pack/plugin/esql-datasource-gcs/src/test/java/org/elasticsearch/xpack/esql/datasource/gcs/GcsConfigurationTests.java`** -> AI Confidence: **99.23%**
2740. **`x-pack/plugin/esql-datasource-iceberg/qa/src/javaRestTest/java/org/elasticsearch/xpack/esql/qa/iceberg/IcebergSpecTestCase.java`** -> AI Confidence: **99.23%**
2741. **`x-pack/plugin/esql-datasource-orc/src/main/java/org/elasticsearch/xpack/esql/datasource/orc/OrcAggregatePushdownSupport.java`** -> AI Confidence: **99.23%**
2742. **`x-pack/plugin/esql-datasource-parquet/src/main/java/org/elasticsearch/xpack/esql/datasource/parquet/ParquetAggregatePushdownSupport.java`** -> AI Confidence: **99.23%**
2743. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/BooleanArrayState.java`** -> AI Confidence: **99.23%**
2744. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/DoubleArrayState.java`** -> AI Confidence: **99.23%**
2745. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/FloatArrayState.java`** -> AI Confidence: **99.23%**
2746. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/IntArrayState.java`** -> AI Confidence: **99.23%**
2747. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/aggregation/LongArrayState.java`** -> AI Confidence: **99.23%**
2748. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/BooleanArrayBlock.java`** -> AI Confidence: **99.23%**
2749. **`x-pack/plugin/esql/compute/src/main/generated-src/org/elasticsearch/compute/data/BooleanBigArrayBlock.java`** -> AI Confidence: **99.23%**
2750. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/CompositeBlock.java`** -> AI Confidence: **99.23%**
2751. **`x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/topn/KeyExtractor.java`** -> AI Confidence: **99.23%**
2752. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/data/BigArrayBlockBuilderTests.java`** -> AI Confidence: **99.23%**
2753. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/AsyncOperatorStatusTests.java`** -> AI Confidence: **99.23%**
2754. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/topn/GroupedTopNOperatorStatusTests.java`** -> AI Confidence: **99.23%**
2755. **`x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/operator/topn/TopNOperatorStatusTests.java`** -> AI Confidence: **99.23%**
2756. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvMedianAbsoluteDeviationDoubleEvaluator.java`** -> AI Confidence: **99.23%**
2757. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvMedianAbsoluteDeviationIntEvaluator.java`** -> AI Confidence: **99.23%**
2758. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvMedianAbsoluteDeviationLongEvaluator.java`** -> AI Confidence: **99.23%**
2759. **`x-pack/plugin/esql/src/main/generated/org/elasticsearch/xpack/esql/expression/function/scalar/multivalue/MvMedianAbsoluteDeviationUnsignedLongEvaluator.java`** -> AI Confidence: **99.23%**
2760. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/DataSourceCapabilities.java`** -> AI Confidence: **99.23%**
2761. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/datasources/RetryPolicy.java`** -> AI Confidence: **99.23%**
2762. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/inference/completion/CompletionOutputBuilder.java`** -> AI Confidence: **99.23%**
2763. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plugin/WeightedRoundRobinStrategy.java`** -> AI Confidence: **99.23%**
2764. **`x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/session/SessionUtils.java`** -> AI Confidence: **99.23%**
2765. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/core/util/SpatialCoordinateTypesTests.java`** -> AI Confidence: **99.23%**
2766. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/UnresolvedAttributeTests.java`** -> AI Confidence: **99.23%**
2767. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/FieldAttributeTests.java`** -> AI Confidence: **99.23%**
2768. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/expression/function/scalar/score/DecaySerializationTests.java`** -> AI Confidence: **99.23%**
2769. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/logical/EsRelationSerializationTests.java`** -> AI Confidence: **99.23%**
2770. **`x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/plan/physical/TopNExecSerializationTests.java`** -> AI Confidence: **99.23%**
2771. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/amazonbedrock/request/completion/AmazonBedrockConverseRequestUtils.java`** -> AI Confidence: **99.23%**
2772. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/amazonbedrock/request/embeddings/AmazonBedrockCohereEmbeddingsRequestEntity.java`** -> AI Confidence: **99.23%**
2773. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/elastic/ElasticInferenceServiceResponseHandler.java`** -> AI Confidence: **99.23%**
2774. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/googleaistudio/request/GoogleAiStudioEmbeddingsRequestEntity.java`** -> AI Confidence: **99.23%**
2775. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/voyageai/request/VoyageAIEmbeddingsRequestEntity.java`** -> AI Confidence: **99.23%**
2776. **`x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/voyageai/request/VoyageAIRerankRequestEntity.java`** -> AI Confidence: **99.23%**
2777. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/external/response/XContentUtilsTests.java`** -> AI Confidence: **99.23%**
2778. **`x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/voyageai/request/VoyageAIRerankRequestEntityTests.java`** -> AI Confidence: **99.23%**
2779. **`x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/job/results/ForecastTests.java`** -> AI Confidence: **99.23%**
2780. **`x-pack/plugin/profiling/src/main/java/org/elasticsearch/xpack/profiling/action/IndexAllocation.java`** -> AI Confidence: **99.23%**
2781. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/predicate/Predicates.java`** -> AI Confidence: **99.23%**
2782. **`x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/expression/predicate/operator/comparison/BinaryComparisonProcessor.java`** -> AI Confidence: **99.23%**
2783. **`x-pack/plugin/ql/src/test/java/org/elasticsearch/xpack/ql/util/SpatialCoordinateTypesTests.java`** -> AI Confidence: **99.23%**
2784. **`x-pack/plugin/rank-rrf/src/main/java/org/elasticsearch/xpack/rank/rrf/RRFRankDoc.java`** -> AI Confidence: **99.23%**
2785. **`x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityWithSameModelRemotesRestIT.java`** -> AI Confidence: **99.23%**
2786. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/jwt/FallbackableClaim.java`** -> AI Confidence: **99.23%**
2787. **`x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/support/FileAttributesChecker.java`** -> AI Confidence: **99.23%**
2788. **`x-pack/plugin/shutdown/src/test/java/org/elasticsearch/xpack/shutdown/PutShutdownRequestTests.java`** -> AI Confidence: **99.23%**
2789. **`x-pack/plugin/slm/src/test/java/org/elasticsearch/xpack/slm/history/SnapshotHistoryItemTests.java`** -> AI Confidence: **99.23%**
2790. **`x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/search/aggregations/bucket/geogrid/GeoHashGridTiler.java`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/AddFileKeyStoreCommandTests.java` -> **100.0%** Exposure
- `distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/AddStringKeyStoreCommandTests.java` -> **100.0%** Exposure
- `distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/RemoveSettingKeyStoreCommandTests.java` -> **100.0%** Exposure
- `test/fixtures/gcs-fixture/src/main/java/fixture/gcs/TestUtils.java` -> **100.0%** Exposure
- `x-pack/plugin/esql-datasource-iceberg/src/test/java/org/elasticsearch/xpack/esql/datasource/iceberg/S3ConfigurationTests.java` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `68` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `441354` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `.buildkite/hooks/pre-command` (SHELL) -> Cumulative Risk: **795.68**
- **Archetype:** `file_cluster_4` (Distance: 13.545 IQR)
- **Magnitude:** 395.86 | **LOC:** 327 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 63.4), `Anonymous_Block` (Impact: 22.5), `__global_context__` (Impact: 14.7)

### 2. `x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/recovery/SearchableSnapshotRecoveryState.java` (JAVA) -> Cumulative Risk: **757.0**
- **Archetype:** `file_cluster_4` (Distance: 10.424 IQR)
- **Magnitude:** 160.6 | **LOC:** 190 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Tech Debt (99.9974%), Concurrency (99.563%)
- **Heaviest Functions:** `validateCurrentStage` (Impact: 24.1), `setStage` (Impact: 11.6), `addFileDetails` (Impact: 6.9)

### 3. `x-pack/plugin/migrate/src/internalClusterTest/java/org/elasticsearch/system_indices/action/AbstractFeatureMigrationIntegTest.java` (JAVA) -> Cumulative Risk: **714.63**
- **Archetype:** `file_cluster_13` (Distance: 11.475 IQR)
- **Magnitude:** 274.08 | **LOC:** 417 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.5936%), State Flux (94.2964%), Tech Debt (94.2268%)
- **Heaviest Functions:** `createSystemIndexForDescriptor` (Impact: 24.2), `blockAction` (Impact: 13.0), `assertNotNull` (Impact: 10.7)

### 4. `x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/amazonbedrock/client/AmazonBedrockStreamingProcessor.java` (JAVA) -> Cumulative Risk: **710.29**
- **Archetype:** `file_cluster_4` (Distance: 11.341 IQR)
- **Magnitude:** 210.18 | **LOC:** 154 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.851%)
- **Heaviest Functions:** `request` (Impact: 28.1), `subscribe` (Impact: 11.8), `onSubscribe` (Impact: 10.4)

### 5. `x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/external/http/StreamingHttpResult.java` (JAVA) -> Cumulative Risk: **706.11**
- **Archetype:** `file_cluster_4` (Distance: 9.865 IQR)
- **Magnitude:** 0.09 | **LOC:** 77 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `readFullResponse` (Impact: 10.3), `onError` (Impact: 10.0), `StreamingHttpResult` (Impact: 9.8)

### 6. `.buildkite/scripts/lucene-snapshot/upload-snapshot.sh` (SHELL) -> Cumulative Risk: **696.04**
- **Archetype:** `file_cluster_4` (Distance: 12.521 IQR)
- **Magnitude:** 4.79 | **LOC:** 44 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9473%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 6.2), `Anonymous_Block` (Impact: 6.2), `Anonymous_Block` (Impact: 5.2)

### 7. `x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/operator/DriverCompletionInfo.java` (JAVA) -> Cumulative Risk: **693.47**
- **Archetype:** `file_cluster_4` (Distance: 10.44 IQR)
- **Magnitude:** 125.54 | **LOC:** 153 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9328%)
- **Heaviest Functions:** `readFrom` (Impact: 17.6), `includingProfiles` (Impact: 15.5), `excludingProfiles` (Impact: 12.9)

### 8. `server/src/main/java/org/elasticsearch/action/support/broadcast/TransportBroadcastAction.java` (JAVA) -> Cumulative Risk: **692.18**
- **Archetype:** `file_cluster_13` (Distance: 11.106 IQR)
- **Magnitude:** 331.16 | **LOC:** 291 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.9937%), Documentation (88.8176%)
- **Heaviest Functions:** `checkRequestBlock` (Impact: 84.7), `onOperation` (Impact: 37.8), `performOperation` (Impact: 19.0)

### 9. `x-pack/plugin/sql/src/internalClusterTest/java/org/elasticsearch/xpack/sql/action/AbstractSqlBlockingIntegTestCase.java` (JAVA) -> Cumulative Risk: **687.72**
- **Archetype:** `file_cluster_13` (Distance: 11.083 IQR)
- **Magnitude:** 263.46 | **LOC:** 280 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (92.4903%), Documentation (90.6358%)
- **Heaviest Functions:** `initBlockFactory` (Impact: 16.4), `apply` (Impact: 16.3), `getActionFilters` (Impact: 15.7)

### 10. `x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/TransformContext.java` (JAVA) -> Cumulative Risk: **680.08**
- **Archetype:** `file_cluster_4` (Distance: 10.814 IQR)
- **Magnitude:** 333.66 | **LOC:** 305 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `incrementAndGetFailureCount` (Impact: 4.5), `incrementAndGetStatePersistenceFailureCo` (Impact: 4.4), `incrementAndGetStartUpFailureCount` (Impact: 4.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `build-tools-internal/src/main/resources/run.ssl/private-ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/private-cert1.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/private-cert2.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/public-ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `distribution/tools/plugin-cli/src/main/resources/public_key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/httpCa.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/reference/setup/install/docker/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/transport.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/node.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/node.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/azure-fixture/src/main/resources/fixture/azure/azure-http-fixture.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/azure-fixture/src/main/resources/fixture/azure/azure-http-fixture.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/core/snapshot.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/resources/idp-sign.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/resources/idp-sign.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/transport.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca-transport.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca-transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/URLConnectionFileActions.java` (JAVA) | Magnitude: 195.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 140, args: 84, branch: 59
- `server/src/main/java/org/elasticsearch/index/mapper/vectors/DenseVectorFieldMapper.java` (JAVA) | Magnitude: 1409.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1815, structural_boundaries: 462, args: 268, func_start: 226
- `server/src/main/java/org/elasticsearch/ingest/CompoundProcessor.java` (JAVA) | Magnitude: 249.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 276, branch: 51, structural_boundaries: 48, safety_bypasses: 40
- `server/src/main/java/org/elasticsearch/rest/LoggingChunkedRestResponseBodyPart.java` (JAVA) | Magnitude: 27.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 17, args: 7, api: 7
- `server/src/main/java/org/elasticsearch/search/aggregations/bucket/range/InternalRange.java` (JAVA) | Magnitude: 244.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 290, structural_boundaries: 87, api: 54, func_start: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/ml/annotations/AnnotationTests.java` (JAVA) | Magnitude: 137.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 45, indent_spaces: 42, branch: 27, structural_boundaries: 21
- `server/src/test/java/org/elasticsearch/search/aggregations/AggregationTestScriptsPlugin.java` (JAVA) | Magnitude: 77.36 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 29, state_mutation: 26, branch: 21
- `.buildkite/scripts/run-bc-upgrade-tests.sh` (SHELL) | Magnitude: 4.64 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 26, branch: 22, indent_spaces: 21, state_mutation: 18
- `.buildkite/scripts/dra-workflow.trigger.sh` (SHELL) | Magnitude: 5.73 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 28, branch: 23, io: 15
- `.buildkite/scripts/third-party-test-credentials.sh` (SHELL) | Magnitude: 8.62 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 37, indent_spaces: 34, structural_boundaries: 32, io: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `.buildkite/scripts/dra-workflow.sh` (SHELL) | Magnitude: 10.17 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 57, indent_spaces: 38, branch: 31, reflection_metaprogramming: 22
- `.buildkite/scripts/trigger-if-java-ea-new-build.sh` (SHELL) | Magnitude: 8.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 34, branch: 30, io: 20
- `test/fixtures/krb5kdc-fixture/src/main/resources/provision/addprinc.sh` (SHELL) | Magnitude: 0.07 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 39, safety_bypasses: 36, branch: 19, indent_spaces: 15
- `x-pack/test/idp-fixture/src/main/resources/idp/bin/run-jetty.sh` (SHELL) | Magnitude: 32.0 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, branch: 9, safety_bypasses: 8, indent_spaces: 5
- `.buildkite/scripts/generate-pr-performance-benchmark.sh` (SHELL) | Magnitude: 1.16 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 39, reflection_metaprogramming: 31, io: 14, dead_code: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/src/main/java/org/elasticsearch/features/InfrastructureFeatures.java` (JAVA) | Magnitude: 11.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, api: 6, args: 2
- `modules/lang-expression/src/main/java/org/elasticsearch/script/expression/ExpressionDoubleValuesScript.java` (JAVA) | Magnitude: 63.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 31, args: 12, func_start: 12
- `modules/transport-netty4/src/test/java/org/elasticsearch/http/netty4/ReadSniffer.java` (JAVA) | Magnitude: 4.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, api: 2, import: 2
- `qa/smoke-test-ingest-with-all-dependencies/src/yamlRestTest/java/org/elasticsearch/smoketest/SmokeTestIngestWithAllDepsClientYamlTestSuiteIT.java` (JAVA) | Magnitude: 10.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 19, import: 7, api: 5
- `server/src/main/java/org/elasticsearch/action/admin/cluster/snapshots/create/CreateSnapshotRequest.java` (JAVA) | Magnitude: 211.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 295, structural_boundaries: 69, doc: 53, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/NetworkInstrumentation.java` (JAVA) | Magnitude: 1915.96 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 765, indent_spaces: 488, args: 426, closures: 425
- `server/src/test/java/org/elasticsearch/common/network/NetworkAddressTests.java` (JAVA) | Magnitude: 199.08 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 80, indent_spaces: 64, structural_boundaries: 56, args: 44
- `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileInstrumentation.java` (JAVA) | Magnitude: 2162.76 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 868, structural_boundaries: 510, args: 479, closures: 478
- `server/src/main/java/org/elasticsearch/action/admin/cluster/snapshots/get/SnapshotSortKey.java` (JAVA) | Magnitude: 49.86 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, branch: 22, closures: 18, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `libs/geo/src/main/java/org/elasticsearch/geometry/GeometryCollection.java` (JAVA) | Magnitude: 63.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 26, api: 17, args: 12
- `test/framework/src/main/java/org/elasticsearch/datageneration/matchers/source/SourceTransforms.java` (JAVA) | Magnitude: 60.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 28, generics: 23, branch: 17
- `x-pack/plugin/core/src/test/java/org/elasticsearch/test/http/MockResponse.java` (JAVA) | Magnitude: 57.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, doc: 35, api: 19, structural_boundaries: 18
- `x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/rule/ParameterizedRuleExecutor.java` (JAVA) | Magnitude: 10.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, api: 5, args: 4
- `libs/x-content/src/main/java/org/elasticsearch/xcontent/NamedXContentRegistry.java` (JAVA) | Magnitude: 60.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 28, generics: 28, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.buildkite/scripts/setup-monitoring.sh` (SHELL) | Magnitude: 5.65 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 25, state_mutation: 24, indent_spaces: 23, safety_bypasses: 9
- `x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/ilm/TimeseriesLifecycleType.java` (JAVA) | Magnitude: 270.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 340, branch: 82, structural_boundaries: 65, comprehensions: 50
- `modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/CsvProcessorTests.java` (JAVA) | Magnitude: 179.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 281, structural_boundaries: 97, args: 48, comprehensions: 46
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/promql/PromqlCoverageAnalyzer.java` (JAVA) | Magnitude: 441.38 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 293, structural_boundaries: 99, branch: 94, args: 64
- `.buildkite/scripts/get-latest-test-mutes.sh` (SHELL) | Magnitude: 2.33 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 13, io: 7, state_mutation: 6, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/framework/src/main/java/org/elasticsearch/script/MockScriptEngine.java` (JAVA) | Magnitude: 129.96 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 743, structural_boundaries: 179, ui_framework: 97, branch: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/match/AddMatchTests.java` (JAVA) | Magnitude: 81.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 42, concurrency: 42, import: 17
- `server/src/internalClusterTest/java/org/elasticsearch/ingest/IngestFileSettingsIT.java` (JAVA) | Magnitude: 170.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 187, structural_boundaries: 85, concurrency: 66, branch: 41
- `server/src/test/java/org/elasticsearch/action/search/ExpandSearchPhaseTests.java` (JAVA) | Magnitude: 263.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 354, structural_boundaries: 147, safety_bypasses: 92, concurrency: 48
- `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/java/org/elasticsearch/xpack/remotecluster/RemoteClusterSecurityRestIT.java` (JAVA) | Magnitude: 789.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 644, branch: 178, structural_boundaries: 140, concurrency: 114
- `libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/JvmActions.java` (JAVA) | Magnitude: 93.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 38, state_mutation: 28, decorators: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `distribution/docker/src/docker/Dockerfile.ess` (DOCKERFILE) | Magnitude: 9.96 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, func_start: 9, branch: 7, state_mutation: 4
- `libs/entitlement/src/main/java/org/elasticsearch/entitlement/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 6, structural_boundaries: 1, doc: 1, planned_debt: 1
- `libs/plugin-api/src/main/java/org/elasticsearch/plugin/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1
- `server/src/main/java/org/elasticsearch/indices/recovery/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1
- `server/src/main/java/org/elasticsearch/search/aggregations/package-info.java` (JAVA) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `server/src/main/java/org/elasticsearch/common/blobstore/support/BlobMetadata.java` (JAVA) | Magnitude: 3.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, args: 1
- `x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/services/elastic/request/ElasticInferenceServiceRequestMetadata.java` (JAVA) | Magnitude: 4.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, args: 1
- `libs/native/src/main/java/org/elasticsearch/nativeaccess/ProcessLimits.java` (JAVA) | Magnitude: 6.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 4, doc: 4, structural_boundaries: 2, globals: 2
- `libs/h3/src/main/java/org/elasticsearch/h3/H3Index.java` (JAVA) | Magnitude: 57.5 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, doc: 24, api: 18, immutability_locks: 14
- `libs/h3/src/main/java/org/elasticsearch/h3/Constants.java` (JAVA) | Magnitude: 26.28 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, immutability_locks: 12, api: 11, globals: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkJavaLibrary.java` (JAVA) | Magnitude: 11.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, import: 5, args: 3
- `modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/direct/GetDatabaseConfigurationAction.java` (JAVA) | Magnitude: 172.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 182, structural_boundaries: 80, api: 38, func_start: 37
- `modules/lang-painless/src/main/java/org/elasticsearch/painless/ir/WhileLoopNode.java` (JAVA) | Magnitude: 15.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, api: 5, func_start: 4
- `modules/streams/src/internalClusterTest/java/org/elasticsearch/rest/streams/TestToggleIT.java` (JAVA) | Magnitude: 22.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 39, import: 17, func_start: 6
- `server/src/main/java/org/elasticsearch/index/query/MatchPhrasePrefixQueryBuilder.java` (JAVA) | Magnitude: 184.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 54, branch: 39, api: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `distribution/docker/src/docker/dockerfiles/wolfi/Dockerfile` (DOCKERFILE) | Magnitude: 21.64 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, branch: 22, func_start: 13, state_mutation: 11
- `x-pack/plugin/mapper-unsigned-long/src/main/java/module-info.java` (JAVA) | Magnitude: 15.2 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, dead_code: 1
- `x-pack/plugin/sql/qa/server/src/main/resources/ogc/sqltsch.sql` (SQLITE) | Magnitude: 1.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 6, sec_dead_code: 2, sec_high_risk_execution: 1
- `server/src/main/java/org/elasticsearch/injection/guice/MessageProcessor.java` (JAVA) | Magnitude: 6.46 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, func_start: 3, args: 2
- `distribution/docker/src/docker/dockerfiles/default/Dockerfile` (DOCKERFILE) | Magnitude: 30.36 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, branch: 21, func_start: 11, io: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/EsqlCapabilities.java` -> Churn: **74.05%** | Cog Load: 4.7809% | Debt: 99.9943%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `server/src/main/java/org/elasticsearch/index/shard/IndexShard.java` -> **Tanguy Leroux** (100.0% isolated ownership) | Magnitude: 3190.7
- `server/src/main/java/org/elasticsearch/snapshots/SnapshotsService.java` -> **Yang Wang** (100.0% isolated ownership) | Magnitude: 3036.2
- `x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/audit/logfile/LoggingAuditTrailTests.java` -> **Tim Vernum** (100.0% isolated ownership) | Magnitude: 2772.6
- `x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java` -> **Tim Vernum** (100.0% isolated ownership) | Magnitude: 2444.02
- `server/src/test/java/org/elasticsearch/cluster/ClusterStateTests.java` -> **David Turner** (100.0% isolated ownership) | Magnitude: 2202.88

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plugin/EsqlPlugin.java` -> **Severity: 3.152** (Bridge: 0.0323 * Flux: 97.7449%)
- `server/src/main/java/org/elasticsearch/cluster/ClusterModule.java` -> **Severity: 1.326** (Bridge: 0.0153 * Flux: 86.9141%)
- `x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/plan/logical/Aggregate.java` -> **Severity: 1.259** (Bridge: 0.0143 * Flux: 87.7781%)
- `server/src/main/java/org/elasticsearch/common/logging/LogConfigurator.java` -> **Severity: 1.185** (Bridge: 0.0119 * Flux: 99.3909%)
- `server/src/main/java/org/elasticsearch/ElasticsearchException.java` -> **Severity: 1.001** (Bridge: 0.0253 * Flux: 39.628%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/src/main/java/org/elasticsearch/common/io/stream/StreamInput.java` -> **Severity: 2771.3** (Blast Radius: 27.713 * Doc Risk: 100.0%)
- `server/src/main/java/org/elasticsearch/common/io/stream/StreamOutput.java` -> **Severity: 2109.9** (Blast Radius: 21.099 * Doc Risk: 100.0%)
- `libs/core/src/main/java/org/elasticsearch/core/RestApiVersion.java` -> **Severity: 889.571** (Blast Radius: 8.906 * Doc Risk: 99.8845%)
- `x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/ElementType.java` -> **Severity: 866.156** (Blast Radius: 20.783 * Doc Risk: 41.6762%)
- `libs/core/src/main/java/org/elasticsearch/core/TimeValue.java` -> **Severity: 760.399** (Blast Radius: 7.655 * Doc Risk: 99.3336%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
