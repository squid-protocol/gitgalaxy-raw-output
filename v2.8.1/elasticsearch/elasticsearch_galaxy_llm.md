# ARCHITECTURAL_BRIEF: elasticsearch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/elastic/elasticsearch` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 38976 |
| Analyzed Artifacts (Scanned) | 31529 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7447 |
| Total LOC | 4240125 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.9% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5314 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1413 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 549 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 27584 | 4147372 | 87.5% |
| PLAINTEXT | 2209 | 308 | 7.0% |
| JSON | 1133 | 68317 | 3.6% |
| GROOVY | 134 | 8257 | 0.4% |
| CSV | 116 | 6546 | 0.4% |
| SHELL | 90 | 2596 | 0.3% |
| MARKDOWN | 83 | 0 | 0.3% |
| XML | 82 | 0 | 0.3% |
| BATCH | 26 | 695 | 0.1% |
| CPP | 21 | 3646 | 0.1% |
| SQLITE | 13 | 300 | 0.0% |
| DOCKERFILE | 11 | 582 | 0.0% |
| PYTHON | 5 | 445 | 0.0% |
| TYPESCRIPT | 5 | 257 | 0.0% |
| HTML | 4 | 45 | 0.0% |
| CSS | 3 | 294 | 0.0% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| POWERSHELL | 2 | 49 | 0.0% |
| PROTO | 2 | 31 | 0.0% |
| JAVASCRIPT | 2 | 31 | 0.0% |
| RUBY | 1 | 351 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +2.24; from the repo's file-archetype mix)
> **File Composition:** Annotated Framework Methods Files 35%, Large Core Modules 18%, Data / Markup / Trivial 15%, Interface Declarations Files 9%, Tests & Verification Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 29188 | 92.6% |
| Unknown | 107 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2184 | 6.9% |
| Static: Minified & Vendor Opaque Mass | 50 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7447*

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
- `no_extension`: 167x Unsupported Format (.undeterminable), 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.java`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Statistical Anomaly (Z-Score: -4.74 < -4.55), 1x Excluded (Embedded Array/Matrix Payload: 1969 commas in 634 LOC)
- `.csv-spec`: 178x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 36 exceeds 500 chars)
- `.yml`: 151x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 67 exceeds 500 chars), 2x Excluded (Saturation: Line 41 exceeds 500 chars)
- `.png`: 149x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 17.2 | 10.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 50.2 | 58.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.7 | 7.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 94.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 74.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 79.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 33216 | 8509 | 2 | `modules/lang-painless/src/test/java/org/elasticsearch/painless/StandardCastTests.java` |
| cleanup | 6486 | 2530 | 0 | `server/src/test/java/org/elasticsearch/index/engine/InternalEngineTests.java` |
| guards | 398420 | 24167 | 30 | `server/src/test/java/org/elasticsearch/index/engine/InternalEngineTests.java` |
| danger | 199195 | 18647 | 16 | `modules/lang-painless/src/test/java/org/elasticsearch/painless/StandardCastTests.java` |
| concurrency | 24532 | 2806 | 0 | `server/src/test/java/org/elasticsearch/index/engine/InternalEngineTests.java` |
| connectivity | 291454 | 27161 | 20 | `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LogicalPlanOptimizerTests.java` |
| io | 19770 | 3696 | 1 | `distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/InstallPluginActionTests.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 176 | 66 | 0 | `distribution/tools/server-launcher/src/test/java/org/elasticsearch/server/launcher/ServerLauncherTests.java` |
| time | 8484 | 1381 | 0 | `server/src/test/java/org/elasticsearch/common/time/DateFormattersTests.java` |
| serialization | 810 | 134 | 0 | `server/src/test/java/org/elasticsearch/index/mapper/DocumentParserTests.java` |
| regex | 957 | 398 | 0 | `server/src/main/java/org/elasticsearch/common/time/DateFormatters.java` |
| events | 32462 | 4296 | 2 | `x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/TokenService.java` |
| tests | 267604 | 9141 | 21 | `x-pack/plugin/core/src/test/java/org/elasticsearch/xpack/core/security/authz/store/ReservedRolesStoreTests.java` |
| docs | 49273 | 13140 | 4 | `x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/EsqlCapabilities.java` |
| debt | 12843 | 4228 | 1 | `server/src/internalClusterTest/java/org/elasticsearch/search/fetch/subphase/highlight/HighlighterSearchIT.java` |
| mutation | 870170 | 24061 | 70 | `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/PhysicalPlanOptimizerTests.java` |
| dead_code | 95929 | 15515 | 8 | `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LogicalPlanOptimizerTests.java` |
| credential | 552 | 136 | 0 | `x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/saml/SamlSpMetadataBuilderTests.java` |
| threat | 1184 | 402 | 0 | `x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/RealmsTests.java` |
| ml_ai | 12325 | 2764 | 0 | `libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/vectorization/PanamaESVectorUtilSupport.java` |
| ui | 1158 | 172 | 0 | `x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/services/elasticsearch/ElasticsearchInternalServiceTests.java` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.4902**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/InstallPluginActionTests.java` (Hits: 176)
- `build-tools/src/main/java/org/elasticsearch/gradle/testclusters/ElasticsearchNode.java` (Hits: 143)
- `.buildkite/hooks/pre-command` (Hits: 122)

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

- `getTableWithHeader` **(Compute Cores)** (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestIndicesAction.java`) -> Impact: **1024.2** | LOC: 374
- `getLegalCast` **(Many-Argument Workhorses)** (@ `modules/lang-painless/src/main/java/org/elasticsearch/painless/AnalyzerCaster.java`) -> Impact: **839.4** | LOC: 377
- `testApacheLog` **(Many-Argument Workhorses)** (@ `libs/grok/src/test/java/org/elasticsearch/grok/GrokTests.java`) -> Impact: **796.9** | LOC: 148
- `getTableWithHeader` **(Compute Cores)** (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestNodesAction.java`) -> Impact: **683.3** | LOC: 202
- `buildTable` **(Many-Argument Workhorses)** (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestIndicesAction.java`) -> Impact: **663.0** | LOC: 291
  * *Intent:* // package private for testing
- `testBinaryComparisons` **(Compute Cores)** (@ `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/planner/QueryTranslatorTests.java`) -> Impact: **651.1** | LOC: 343
- `TestConfiguration` **(Many-Argument Workhorses)** (@ `qa/vector/src/main/java/org/elasticsearch/test/knn/TestConfiguration.java`) -> Impact: **612.1** | LOC: 918
  * *Intent:* /** * Command line arguments for the KNN index tester. * This class encapsulates all the parameters required to run the KNN index tests. */
- `buildTable` **(Many-Argument Workhorses)** (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestNodesAction.java`) -> Impact: **602.9** | LOC: 203
- `testFailureStoreAccess` **(Compute Cores)** (@ `x-pack/plugin/security/qa/security-trial/src/javaRestTest/java/org/elasticsearch/xpack/security/failurestore/FailureStoreSecurityRestIT.java`) -> Impact: **585.5** | LOC: 949
- `getTableWithHeader` **(Compute Cores)** (@ `server/src/main/java/org/elasticsearch/rest/action/cat/RestShardsAction.java`) -> Impact: **550.9** | LOC: 157

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/resources/ssl` | 13 | 60001.62 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl` | 12 | 55001.22 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/smoke-test-all-realms/src/javaRestTest/resources/ssl` | 10 | 45001.28 | 0.0% | 0.0% |
| `x-pack/plugin/esql/compute/src/main/generated/org/elasticsearch/compute/aggregation` | 379 | 40584.64 | 22.45% | 54.74% |
| `x-pack/plugin/security/qa/tls-basic/src/javaRestTest/resources/ssl` | 8 | 35001.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/saml-rest-tests/src/javaRestTest/resources/ssl` | 7 | 30001.0 | 0.0% | 0.0% |
| `x-pack/qa/smoke-test-plugins-ssl/src/yamlRestTest/resources` | 6 | 30000.0 | 0.0% | 0.0% |
| `modules/data-streams/src/javaRestTest/resources/ssl` | 6 | 25001.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/service-account/src/javaRestTest/resources/ssl` | 6 | 25001.0 | 0.0% | 0.0% |
| `x-pack/qa/reindex-tests-with-security/src/yamlRestTest/resources/ssl` | 6 | 25001.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerResult.java` -> **100.0%** Exposure
- `build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClusterConfiguration.java` -> **100.0%** Exposure
- `libs/exponential-histogram/src/main/java/org/elasticsearch/exponentialhistogram/EmptyExponentialHistogram.java` -> **100.0%** Exposure
- `libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/IngestDocumentBridge.java` -> **100.0%** Exposure
- `libs/native/src/main/java/org/elasticsearch/nativeaccess/NoopNativeAccess.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.buildkite/hooks/pre-command` -> **100.0%** Exposure
- `.buildkite/scripts/dra-workflow.sh` -> **100.0%** Exposure
- `.buildkite/scripts/dra-workflow.trigger.sh` -> **100.0%** Exposure
- `.buildkite/scripts/gradle-build-cache-validation.sh` -> **100.0%** Exposure
- `.buildkite/scripts/setup-monitoring.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LogicalPlanOptimizerTests.java` -> **404** Orphaned Functions | **0** Duplicates
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/session/FieldNameUtilsTests.java` -> **289** Orphaned Functions | **0** Duplicates
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/analysis/AnalyzerTests.java` -> **271** Orphaned Functions | **0** Duplicates
- `x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/PhysicalPlanOptimizerTests.java` -> **228** Orphaned Functions | **0** Duplicates
- `x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/analysis/analyzer/VerifierErrorMessagesTests.java` -> **204** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/AddFileKeyStoreCommandTests.java` -> **100.0%** Exposure
- `distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/AddStringKeyStoreCommandTests.java` -> **100.0%** Exposure
- `distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/RemoveSettingKeyStoreCommandTests.java` -> **100.0%** Exposure
- `modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/DataStreamWithSecurityIT.java` -> **100.0%** Exposure
- `test/fixtures/gcs-fixture/src/main/java/fixture/gcs/TestUtils.java` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `85` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `441314` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/SegmentTermsEnum.java` (JAVA) -> Cumulative Risk: **750.62**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.14)
- **Magnitude:** 647.58 | **LOC:** 1174 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (98.3369%), Safety Score (97.1049%)
- **Heaviest Functions:** `printSeekState` (Compute Cores, Impact: 66.4), `seekCeil` (Compute Cores, Impact: 58.7), `seekExact` (Compute Cores, Impact: 57.7)

### 2. `x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene40/blocktree/SegmentTermsEnumFrame.java` (JAVA) -> Cumulative Risk: **732.48**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.14)
- **Magnitude:** 423.2 | **LOC:** 770 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.1368%)
- **Heaviest Functions:** `scanToTermNonLeaf` (Many-Argument Workhorses, Impact: 28.4), `scanToTermLeaf` (Many-Argument Workhorses, Impact: 22.0), `loadBlock` (I/O & Config Routines, Impact: 16.9)

### 3. `x-pack/plugin/ql/src/main/java/org/elasticsearch/xpack/ql/rule/RuleExecutor.java` (JAVA) -> Cumulative Risk: **709.73**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.70)
- **Magnitude:** 142.28 | **LOC:** 214 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9833%), Tech Debt (99.8703%)
- **Heaviest Functions:** `executeWithInfo` (Compute Cores, Impact: 27.5), `Batch` (Annotated Framework Methods, Impact: 4.3), `Batch` (Annotated Framework Methods, Impact: 3.7)

### 4. `build-tools/src/main/java/org/elasticsearch/gradle/testclusters/WaitForHttpResource.java` (JAVA) -> Cumulative Risk: **693.82**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.70)
- **Magnitude:** 100.4 | **LOC:** 159 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.708%), State Flux (99.1563%)
- **Heaviest Functions:** `configureSslContext` (Defensive Guards, Impact: 7.4), `wait` (Defensive Guards, Impact: 6.7), `WaitForHttpResource` (Compute Cores, Impact: 6.2)

### 5. `server/src/main/java/org/elasticsearch/common/util/concurrent/PrioritizedEsThreadPoolExecutor.java` (JAVA) -> Cumulative Risk: **692.48**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.55)
- **Magnitude:** 265.54 | **LOC:** 263 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (97.2973%)
- **Heaviest Functions:** `addPending` (Defensive Guards, Impact: 18.9), `execute` (Defensive Guards, Impact: 10.7), `wrapRunnable` (Defensive Guards, Impact: 9.2)

### 6. `libs/simdvec/native/src/vec/c/aarch64/vec_1.cpp` (CPP) -> Cumulative Risk: **690.87**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.13)
- **Magnitude:** 394.8 | **LOC:** 680 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.0987%), Safety Score (92.2005%)
- **Heaviest Functions:** `cosi8_inner_bulk` (Many-Argument Workhorses, Impact: 23.9), `call_i8_bulk` (Many-Argument Workhorses, Impact: 17.6), `call_f32_bulk` (Many-Argument Workhorses, Impact: 17.2)

### 7. `build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/info/DefaultBuildParameterExtension.java` (JAVA) -> Cumulative Risk: **687.45**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z -1.51)
- **Magnitude:** 136.14 | **LOC:** 260 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9957%), State Flux (91.1678%)
- **Heaviest Functions:** `DefaultBuildParameterExtension` (Many-Argument Workhorses, Impact: 9.5), `getBuildDate` (Annotated Framework Methods, Impact: 3.6), `computeIfAbsent` (Generic / Templated Code, Impact: 3.2)

### 8. `server/src/main/java/org/elasticsearch/index/codec/tsdb/AbstractTSDBDocValuesProducer.java` (JAVA) -> Cumulative Risk: **686.99**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z -0.15)
- **Magnitude:** 1980.18 | **LOC:** 2935 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9599%), State Flux (98.2773%), Documentation (98.0952%)
- **Heaviest Functions:** `getNumeric` (Many-Argument Workhorses, Impact: 104.6), `tryRead` (Many-Argument Workhorses, Impact: 48.6), `decodeLengthsBulk` (Many-Argument Workhorses, Impact: 47.2)

### 9. `x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene54/Lucene54DocValuesProducer.java` (JAVA) -> Cumulative Risk: **684.06**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z -0.47)
- **Magnitude:** 1446.72 | **LOC:** 1864 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9876%), State Flux (99.97%), Documentation (97.6834%)
- **Heaviest Functions:** `readFields` (Compute Cores, Impact: 102.8), `readNumericEntry` (Compute Cores, Impact: 61.3), `getSortedNumeric` (Annotated Framework Methods, Impact: 45.2)

### 10. `x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/recovery/SearchableSnapshotRecoveryState.java` (JAVA) -> Cumulative Risk: **683.79**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.17)
- **Magnitude:** 116.94 | **LOC:** 190 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (89.724%)
- **Heaviest Functions:** `validateCurrentStage` (Defensive Guards, Impact: 7.9), `addFileDetails` (Defensive Guards, Impact: 6.9), `setStage` (Compute Cores, Impact: 6.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `build-tools-internal/src/main/resources/run.ssl/private-ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/private-cert1.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/private-cert2.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/public-ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `distribution/tools/plugin-cli/src/main/resources/public_key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/httpCa.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/reference/setup/install/docker/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/transport.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/node.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/node.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/azure-fixture/src/main/resources/fixture/azure/azure-http-fixture.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/azure-fixture/src/main/resources/fixture/azure/azure-http-fixture.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/core/snapshot.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/resources/idp-sign.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/resources/idp-sign.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/transport.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca-transport.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca-transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/action/EsqlCapabilities.java` -> Churn: **74.05%** | Cog Load: 3.9507% | Debt: 58.8987%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `server/src/main/java/org/elasticsearch/index/mapper/vectors/DenseVectorFieldMapper.java` -> **Benjamin Trent** (100.0% isolated ownership) | Magnitude: 2568.36
- `server/src/main/java/org/elasticsearch/index/shard/IndexShard.java` -> **Tanguy Leroux** (100.0% isolated ownership) | Magnitude: 2282.1
- `server/src/test/java/org/elasticsearch/index/shard/IndexShardTests.java` -> **Yang Wang** (100.0% isolated ownership) | Magnitude: 2141.3
- `x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/audit/logfile/LoggingAuditTrailTests.java` -> **Tim Vernum** (100.0% isolated ownership) | Magnitude: 2016.7
- `server/src/main/java/org/elasticsearch/index/codec/tsdb/AbstractTSDBDocValuesProducer.java` -> **Salvatore Campagna** (100.0% isolated ownership) | Magnitude: 1980.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/data/ElementType.java` -> **Severity: 1278.832** (Blast Radius: 20.781 * Doc Risk: 61.5385%)
- `server/src/main/java/org/elasticsearch/common/io/stream/StreamInput.java` -> **Severity: 1115.637** (Blast Radius: 27.711 * Doc Risk: 40.2597%)
- `libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java` -> **Severity: 1052.368** (Blast Radius: 13.269 * Doc Risk: 79.3103%)
- `libs/core/src/main/java/org/elasticsearch/core/RestApiVersion.java` -> **Severity: 890.5** (Blast Radius: 8.905 * Doc Risk: 100.0%)
- `libs/core/src/main/java/org/elasticsearch/core/TimeValue.java` -> **Severity: 635.202** (Blast Radius: 7.655 * Doc Risk: 82.9787%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
