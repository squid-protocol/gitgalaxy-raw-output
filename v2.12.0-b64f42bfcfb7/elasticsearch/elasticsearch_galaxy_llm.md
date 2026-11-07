# ARCHITECTURAL_BRIEF: elasticsearch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/elastic/elasticsearch` |
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
- **Scope:** 8741 analyzed artifact(s), 876368 LOC.
- **Load-bearing artifact:** `test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java` -- 1834 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `test/framework/src/main/java/org/elasticsearch/test/ESIntegTestCase.java` -- pulls in 259 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `build-tools-internal/src/main/resources/run.ssl/private-ca.key` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 39212 |
| Analyzed Artifacts (Scanned) | 8741 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 30471 |
| Total LOC | 876368 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 22.3% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6501 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0968 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.8249 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 344 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 6170 | 839490 | 70.6% |
| PLAINTEXT | 1794 | 59 | 20.5% |
| GROOVY | 423 | 16646 | 4.8% |
| JSON | 123 | 12686 | 1.4% |
| SHELL | 67 | 2427 | 0.8% |
| XML | 65 | 0 | 0.7% |
| MARKDOWN | 47 | 0 | 0.5% |
| SQLITE | 13 | 300 | 0.1% |
| CSV | 11 | 2834 | 0.1% |
| DOCKERFILE | 7 | 188 | 0.1% |
| BATCH | 5 | 337 | 0.1% |
| PYTHON | 5 | 445 | 0.1% |
| TYPESCRIPT | 5 | 257 | 0.1% |
| CSS | 3 | 294 | 0.0% |
| POWERSHELL | 2 | 49 | 0.0% |
| RUBY | 1 | 356 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 8683 |
| unknown | unknown | 58 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Encapsulated Accessors Files 20%, Large Core Modules (3) 13%, Declarative / Non-Code 6%, State Mutators Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6896 | 78.9% |
| Unknown | 58 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1782 | 20.4% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 30471*

**Composition by Extension & Reason:**
- `.java`: 21597x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3841 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1711 LOC)
- `.md`: 2589x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1349x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6174 LOC)
- `.txt`: 874x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.csv`: 470x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 437x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 355x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 67 exceeds 500 chars), 2x Excluded (Saturation: Line 41 exceeds 500 chars)
- `.expected`: 329x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.crt`: 232x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 27x Unsupported Format (.crt), 2x Excluded (Binary Format Detected)
- `no_extension`: 208x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 46x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.esql`: 255x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 235x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.zip`: 222x Excluded (Explicitly Denied Extension: '.zip')
- `.gradle`: 207x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv-spec`: 155x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Unsupported Format (.undeterminable)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.6 | 6.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.0 | 42.9 | 52.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.7 | 6.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 45.5 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 77.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6285 | 1564 | 1 | `x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/planner/QueryTranslatorTests.java` |
| cleanup | 999 | 428 | 0 | `libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/FileCheckActions.java` |
| guards | 81908 | 5417 | 25 | `test/framework/src/main/java/org/elasticsearch/test/rest/ESRestTestCase.java` |
| danger | 41825 | 4014 | 13 | `modules/parent-join/src/internalClusterTest/java/org/elasticsearch/join/query/ChildQuerySearchIT.java` |
| concurrency | 5698 | 752 | 0 | `rest-api-spec/build.gradle` |
| connectivity | 55936 | 6037 | 15 | `test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java` |
| io | 9053 | 1268 | 2 | `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileInstrumentation.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 110 | 48 | 0 | `dev-tools/delete_branch_jobs.sh` |
| time | 2180 | 367 | 0 | `modules/aggregations/src/test/java/org/elasticsearch/aggregations/bucket/histogram/AutoDateHistogramAggregatorTests.java` |
| serialization | 203 | 57 | 0 | `qa/packaging/src/test/java/org/elasticsearch/packaging/util/docker/Docker.java` |
| regex | 535 | 191 | 0 | `libs/x-content/src/test/java/org/elasticsearch/xcontent/support/filtering/FilterPathTests.java` |
| events | 6749 | 1057 | 1 | `x-pack/plugin/transform/src/main/java/org/elasticsearch/xpack/transform/transforms/TransformIndexer.java` |
| tests | 58406 | 2208 | 17 | `x-pack/plugin/async-search/src/internalClusterTest/java/org/elasticsearch/xpack/search/CrossClusterAsyncSearchIT.java` |
| docs | 9259 | 2716 | 2 | `test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java` |
| debt | 2584 | 826 | 0 | `test/framework/src/main/java/org/elasticsearch/transport/AbstractSimpleTransportTestCase.java` |
| mutation | 175780 | 5638 | 55 | `x-pack/plugin/blob-cache/src/test/java/org/elasticsearch/blobcache/shared/SharedBlobCacheServiceTests.java` |
| dead_code | 23095 | 3966 | 7 | `x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/analysis/analyzer/VerifierErrorMessagesTests.java` |
| credential | 354 | 63 | 0 | `.buildkite/scripts/third-party-test-credentials.sh` |
| threat | 413 | 7 | 0 | `x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/parser/EqlBaseLexer.java` |
| ml_ai | 2084 | 505 | 0 | `x-pack/plugin/sql/qa/jdbc/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/ResultSetTestCase.java` |
| ui | 23 | 9 | 0 | `x-pack/plugin/ml-package-loader/src/main/java/org/elasticsearch/xpack/ml/packageloader/action/ModelImporter.java` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `libs/entitlement/src/main/java/org/elasticsearch/entitlement/config/FileInstrumentation.java` (Hits: 173)
- `build-tools/src/main/java/org/elasticsearch/gradle/testclusters/ElasticsearchNode.java` (Hits: 143)
- `.buildkite/hooks/pre-command` (Hits: 122)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ESTestCase.java** (`test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java`) — 1834 inbound connections
2. **XContentBuilder.java** (`libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java`) — 566 inbound connections
3. **TimeValue.java** (`libs/core/src/main/java/org/elasticsearch/core/TimeValue.java`) — 521 inbound connections
4. **XContentType.java** (`libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentType.java`) — 362 inbound connections
5. **ESRestTestCase.java** (`test/framework/src/main/java/org/elasticsearch/test/rest/ESRestTestCase.java`) — 355 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ESIntegTestCase.java** (`test/framework/src/main/java/org/elasticsearch/test/ESIntegTestCase.java`) — 259 outbound dependencies
2. **ESTestCase.java** (`test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java`) — 229 outbound dependencies
3. **AggregatorTestCase.java** (`test/framework/src/main/java/org/elasticsearch/search/aggregations/AggregatorTestCase.java`) — 184 outbound dependencies
4. **InternalTestCluster.java** (`test/framework/src/main/java/org/elasticsearch/test/InternalTestCluster.java`) — 157 outbound dependencies
5. **AbstractCoordinatorTestCase.java** (`test/framework/src/main/java/org/elasticsearch/cluster/coordination/AbstractCoordinatorTestCase.java`) — 146 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `randomSearchSourceBuilder` **(Many-Argument Workhorses)** (@ `test/framework/src/main/java/org/elasticsearch/search/RandomSearchRequestGenerator.java`) -> Impact: **244.0** | LOC: 276
- `create` **(Compute Cores)** (@ `modules/analysis-common/src/main/java/org/elasticsearch/analysis/common/StemmerTokenFilterFactory.java`) -> Impact: **185.5** | LOC: 203
- `compile` **(Many-Argument Workhorses)** (@ `test/framework/src/main/java/org/elasticsearch/script/MockScriptEngine.java`) -> Impact: **178.9** | LOC: 314
- `buildBlocks` **(Many-Argument Workhorses)** (@ `benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockBenchmark.java`) -> Impact: **175.5** | LOC: 430
- `read` **(Many-Argument Workhorses)** (@ `x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene62/Lucene62SegmentInfoFormat.java`) -> Impact: **147.5** | LOC: 177
- `checkGrouped` **(Many-Argument Workhorses)** (@ `benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/AggregatorBenchmark.java`) -> Impact: **141.9** | LOC: 139
- `parse` **(Many-Argument Workhorses)** (@ `test/yaml-rest-runner/src/main/java/org/elasticsearch/test/rest/yaml/restspec/ClientYamlSuiteRestApiParser.java`) -> Impact: **138.5** | LOC: 242
- `checkExpected` **(Many-Argument Workhorses)** (@ `benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/EvalBenchmark.java`) -> Impact: **136.6** | LOC: 204
- `addNumericField` **(Many-Argument Workhorses)** (@ `x-pack/plugin/old-lucene-versions/src/main/java/org/elasticsearch/xpack/lucene/bwc/codecs/lucene54/Lucene54DocValuesConsumer.java`) -> Impact: **130.2** | LOC: 204
- `handle` **(Many-Argument Workhorses)** (@ `test/fixtures/s3-fixture/src/main/java/fixture/s3/S3HttpHandler.java`) -> Impact: **123.6** | LOC: 351

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl` | 6 | 30000.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/resources/ssl` | 6 | 30000.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/smoke-test-all-realms/src/javaRestTest/resources/ssl` | 5 | 25000.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/tls-basic/src/javaRestTest/resources/ssl` | 4 | 20000.0 | 0.0% | 0.0% |
| `x-pack/qa/smoke-test-plugins-ssl/src/yamlRestTest/resources` | 4 | 20000.0 | 0.0% | 0.0% |
| `build-tools-internal/src/main/resources/run.ssl` | 4 | 15001.1 | 0.0% | 0.0% |
| `modules/data-streams/src/javaRestTest/resources/ssl` | 4 | 15001.0 | 0.0% | 0.0% |
| `x-pack/qa/reindex-tests-with-security/src/yamlRestTest/resources/ssl` | 4 | 15001.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/saml-rest-tests/src/javaRestTest/resources/ssl` | 3 | 15000.0 | 0.0% | 0.0% |
| `x-pack/plugin/security/qa/service-account/src/javaRestTest/resources/ssl` | 3 | 15000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerResult.java` -> **100.0%** Exposure
- `build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClusterConfiguration.java` -> **100.0%** Exposure
- `libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/IngestDocumentBridge.java` -> **100.0%** Exposure
- `libs/native/src/main/java/org/elasticsearch/nativeaccess/NoopNativeAccess.java` -> **100.0%** Exposure
- `libs/x-content/src/main/java/org/elasticsearch/xcontent/FilterXContentParser.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.buildkite/hooks/pre-command` -> **100.0%** Exposure
- `.buildkite/scripts/dra-workflow.sh` -> **100.0%** Exposure
- `.buildkite/scripts/dra-workflow.trigger.sh` -> **100.0%** Exposure
- `.buildkite/scripts/gradle-build-cache-validation.sh` -> **100.0%** Exposure
- `.buildkite/scripts/setup-monitoring.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/analysis/analyzer/VerifierErrorMessagesTests.java` -> **204** Orphaned Functions | **0** Duplicates
- `x-pack/plugin/sql/jdbc/src/main/java/org/elasticsearch/xpack/sql/jdbc/JdbcDatabaseMetaData.java` -> **175** Orphaned Functions | **0** Duplicates
- `test/framework/src/main/java/org/elasticsearch/transport/AbstractSimpleTransportTestCase.java` -> **57** Orphaned Functions | **97** Duplicates
- `libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/DummyImplementations.java` -> **82** Orphaned Functions | **26** Duplicates
- `libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/FileCheckActions.java` -> **105** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `.buildkite/hooks/pre-command` -> **100.0%** Exposure
- `.buildkite/scripts/setup-monitoring.sh` -> **100.0%** Exposure
- `.buildkite/scripts/third-party-test-credentials.sh` -> **100.0%** Exposure
- `build-tools-internal/src/main/groovy/elasticsearch.run-ccs.gradle` -> **100.0%** Exposure
- `x-pack/plugin/transform/qa/multi-cluster-tests-with-security/build.gradle` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `36` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `100462` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `build-tools-internal/src/main/resources/run.ssl/private-ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/private-cert1.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-tools-internal/src/main/resources/run.ssl/private-cert2.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/httpCa.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/reference/setup/install/docker/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docs/transport.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/ca.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/data-streams/src/javaRestTest/resources/ssl/node.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/azure-fixture/src/main/resources/fixture/azure/azure-http-fixture.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/core/snapshot.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/identity-provider/qa/idp-rest-tests/src/javaRestTest/resources/idp-sign.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/basic-enable-security/src/javaRestTest/resources/ssl/transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca-transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/ca.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/http.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/pki.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/jwt-realm/src/javaRestTest/resources/ssl/transport.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/microsoft-graph-authz-tests/src/javaRestTest/resources/saml/signing.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/microsoft-graph-authz-tests/src/javaRestTest/resources/server/cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/resources/signing/signing.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/resources/ssl/remote-cluster-ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x-pack/plugin/security/qa/multi-cluster/src/javaRestTest/resources/ssl/remote-cluster-client-ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchJavaModulePathPlugin.java` (JAVA) | Magnitude: 102.94 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 89, args: 31, import: 31
- `build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/BuildConfigurationAwareGradleRunner.java` (JAVA) | Magnitude: 76.34 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 44, api: 24, func_start: 23
- `x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/LocalStateMonitoring.java` (JAVA) | Magnitude: 55.14 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 70, import: 32, api: 19
- `x-pack/test/deprecated-query/src/main/java/org/elasticsearch/query/DeprecatedQueryPlugin.java` (JAVA) | Magnitude: 5.54 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 5, args: 4, import: 4
- `test/external-modules/esql-heap-attack/src/javaRestTest/java/org/elasticsearch/xpack/esql/heap_attack/HeapAttackIT.java` (JAVA) | Magnitude: 523.5 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 845, structural_boundaries: 215, core_var_decl: 206, design_snake_case: 176

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `x-pack/plugin/searchable-snapshots/src/test/java/org/elasticsearch/xpack/searchablesnapshots/cache/common/CacheKeyTests.java` (JAVA) | Magnitude: 25.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 23, args: 14, closures: 11
- `libs/ssl-config/src/test/java/org/elasticsearch/common/ssl/SslConfigurationTests.java` (JAVA) | Magnitude: 39.04 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 40, immutability_locks: 31, core_var_decl: 31
- `modules/mapper-extras/src/test/java/org/elasticsearch/index/mapper/extras/SourceIntervalsSourceTests.java` (JAVA) | Magnitude: 22.38 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 47, test: 39, import: 27
- `modules/percolator/src/test/java/org/elasticsearch/percolator/QueryAnalyzerTests.java` (JAVA) | Magnitude: 559.06 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1118, structural_boundaries: 508, test: 457, state_mutation: 358
- `build-tools-internal/src/test/groovy/org/elasticsearch/gradle/internal/info/GlobalBuildInfoPluginSpec.groovy` (GROOVY) | Magnitude: 22.68 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 29, core_var_decl: 18, import: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/ShowTablesTestCase.java` (JAVA) | Magnitude: 13.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, sec_db_hooks: 24, structural_boundaries: 13, io: 11
- `libs/entitlement/qa/entitled-plugin/src/main/java/org/elasticsearch/entitlement/qa/entitled/EntitledActions.java` (JAVA) | Magnitude: 50.18 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 69, io: 32, args: 20
- `x-pack/plugin/autoscaling/src/test/java/org/elasticsearch/xpack/autoscaling/action/TransportGetAutoscalingPolicyActionTests.java` (JAVA) | Magnitude: 17.22 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 49, import: 24, core_var_decl: 22
- `build-tools-internal/src/integTest/groovy/org/elasticsearch/gradle/internal/transport/TransportVersionGenerationFuncTest.groovy` (GROOVY) | Magnitude: 108.5 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 385, test: 198, structural_boundaries: 76, args: 39
- `x-pack/plugin/autoscaling/src/internalClusterTest/java/org/elasticsearch/xpack/autoscaling/shards/FrozenShardsDeciderIT.java` (JAVA) | Magnitude: 11.9 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, api: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `x-pack/plugin/wildcard/src/internalClusterTest/java/org/elasticsearch/xpack/wildcard/search/WildcardSearchIT.java` (JAVA) | Magnitude: 74.56 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 46, core_var_decl: 21, import: 18
- `test/fixtures/ec2-imds-fixture/src/test/java/fixture/aws/imds/Ec2ImdsHttpHandlerTests.java` (JAVA) | Magnitude: 0.1 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 109, args: 39, immutability_locks: 39
- `x-pack/plugin/transform/src/internalClusterTest/java/org/elasticsearch/xpack/transform/checkpoint/TransformGetCheckpointTests.java` (JAVA) | Magnitude: 123.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 114, import: 57, core_var_decl: 44
- `x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/execution/search/SearchHitCursorTests.java` (JAVA) | Magnitude: 51.86 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 59, import: 25, args: 15
- `x-pack/plugin/sql/sql-client/src/test/java/org/elasticsearch/xpack/sql/client/RemoteFailureTests.java` (JAVA) | Magnitude: 53.92 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 226, test: 56, structural_boundaries: 55, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `plugins/store-smb/src/main/java/org/elasticsearch/index/store/smb/SmbMmapFsDirectoryFactory.java` (JAVA) | Magnitude: 4.78 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 17, import: 9, indent_spaces: 7, io: 2
- `test/external-modules/multi-project/src/main/java/org/elasticsearch/multiproject/TestOnlyMultiProjectFeatureSpecification.java` (JAVA) | Magnitude: 3.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, import: 4, indent_spaces: 4, api: 2
- `x-pack/plugin/logsdb/src/javaRestTest/java/org/elasticsearch/xpack/logsdb/qa/BulkDynamicMappingChallengeRestIT.java` (JAVA) | Magnitude: 7.04 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, args: 3, api: 3
- `x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/search/aggregations/metrics/CartesianBoundsAggregatorFactory.java` (JAVA) | Magnitude: 10.44 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 21, import: 11, args: 4
- `x-pack/plugin/mapper-version/src/test/java/org/elasticsearch/xpack/versionfield/VersionStringFieldMapperTests.java` (JAVA) | Magnitude: 54.38 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 68, args: 30, import: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/expression/function/scalar/string/SubstringFunctionProcessorTests.java` (JAVA) | Magnitude: 6.38 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 14, safety_bypasses: 5, args: 4
- `x-pack/plugin/eql/src/test/java/org/elasticsearch/xpack/eql/execution/search/OrdinalTests.java` (JAVA) | Magnitude: 38.58 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 104, core_var_decl: 46, structural_boundaries: 45, design_snake_case: 40
- `.buildkite/scripts/get-latest-test-mutes.sh` (SHELL) | Magnitude: 1.43 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 15, io: 7, indent_spaces: 6, branch: 4
- `modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/JsonProcessorFactoryTests.java` (JAVA) | Magnitude: 53.96 | Delta: **0.187** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 49, core_var_decl: 37, safety_bypasses: 28
- `test/framework/src/main/java/org/elasticsearch/datageneration/fields/leaf/DateFieldDataGenerator.java` (JAVA) | Magnitude: 23.9 | Delta: **0.193** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 16, import: 10, safety_bypasses: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `x-pack/plugin/transform/qa/single-node-tests/src/javaRestTest/java/org/elasticsearch/xpack/transform/integration/TransformConfigurationIndexIT.java` (JAVA) | Magnitude: 8.88 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 24, import: 14, core_var_decl: 8
- `x-pack/plugin/sql/src/test/java/org/elasticsearch/xpack/sql/expression/function/scalar/datetime/DateTimeTestUtils.java` (JAVA) | Magnitude: 39.24 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 23, time_date_logic: 19, args: 12
- `build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dependencies/rules/ComponentMetadataRulesPlugin.java` (JAVA) | Magnitude: 32.06 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 270, indent_spaces: 261, import: 4, args: 3
- `x-pack/plugin/sql/jdbc/src/main/java/org/elasticsearch/xpack/sql/jdbc/JdbcTestUtils.java` (JAVA) | Magnitude: 2.94 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, time_date_logic: 5, import: 4
- `x-pack/plugin/spatial/src/main/java/org/elasticsearch/xpack/spatial/common/H3CartesianGeometry.java` (JAVA) | Magnitude: 230.1 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 296, structural_boundaries: 57, branch: 41, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/allocation/decider/SearchableSnapshotEnableAllocationDecider.java` (JAVA) | Magnitude: 24.82 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 18, import: 9, branch: 5
- `x-pack/plugin/ilm/src/javaRestTest/java/org/elasticsearch/xpack/IlmESRestTestCase.java` (JAVA) | Magnitude: 13.54 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 26, import: 10, api: 7
- `modules/data-streams/src/javaRestTest/java/org/elasticsearch/datastreams/DisabledSecurityDataStreamTestCase.java` (JAVA) | Magnitude: 12.38 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 16, import: 9, api: 5
- `test/framework/src/main/java/org/elasticsearch/search/aggregations/metrics/AbstractGeoTestCase.java` (JAVA) | Magnitude: 171.88 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 227, state_mutation: 52, core_var_decl: 52, structural_boundaries: 46
- `libs/ssl-config/src/test/java/org/elasticsearch/common/ssl/PemTrustConfigTests.java` (JAVA) | Magnitude: 45.86 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 58, test: 32, core_var_decl: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `x-pack/plugin/searchable-snapshots/src/internalClusterTest/java/org/elasticsearch/xpack/searchablesnapshots/SearchableSnapshotsRecoverFromSnapshotIntegTests.java` (JAVA) | Magnitude: 14.18 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 31, import: 16, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `x-pack/plugin/searchable-snapshots/src/main/java/org/elasticsearch/xpack/searchablesnapshots/cache/common/CacheKey.java` (JAVA) | Magnitude: 8.78 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, safety: 4, state_mutation: 4
- `test/fixtures/hdfs-fixture/build.gradle` (GROOVY) | Magnitude: 0.05 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 215, state_mutation: 20, core_var_decl: 18, args: 14
- `x-pack/plugin/write-load-forecaster/src/test/java/org/elasticsearch/xpack/writeloadforecaster/ClusterInfoWriteLoadForecasterTests.java` (JAVA) | Magnitude: 6.36 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 20, core_var_decl: 16, design_camel_case: 11
- `libs/ssl-config/build.gradle` (GROOVY) | Magnitude: 15.4 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, closures: 2, dependency_injection: 2, args: 1
- `build-tools/src/main/java/org/elasticsearch/gradle/FileSystemOperationsAware.java` (JAVA) | Magnitude: 3.6 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `plugins/examples/custom-suggester/src/main/java/org/elasticsearch/example/customsuggester/CustomSuggestionBuilder.java` (JAVA) | Magnitude: 82.56 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 37, branch: 18, core_var_decl: 17
- `x-pack/plugin/sql/qa/server/src/main/java/org/elasticsearch/xpack/sql/qa/jdbc/DataLoader.java` (JAVA) | Magnitude: 175.08 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 376, structural_boundaries: 83, core_var_decl: 38, branch: 27
- `libs/ssl-config/src/main/java/org/elasticsearch/common/ssl/PemUtils.java` (JAVA) | Magnitude: 377.04 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 489, core_var_decl: 159, structural_boundaries: 158, branch: 122
- `test/framework/src/main/java/org/elasticsearch/test/BackgroundIndexer.java` (JAVA) | Magnitude: 254.6 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 69, core_var_decl: 40, state_mutation: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `modules/analysis-common/src/main/java/org/elasticsearch/analysis/common/SynonymGraphTokenFilterFactory.java` (JAVA) | Magnitude: 30.06 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 28, import: 16, args: 8
- `x-pack/plugin/searchable-snapshots/src/internalClusterTest/java/org/elasticsearch/xpack/searchablesnapshots/recovery/SearchableSnapshotRecoveryStateIntegrationTests.java` (JAVA) | Magnitude: 46.5 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 68, import: 45, core_var_decl: 38
- `x-pack/qa/oidc-op-tests/src/javaRestTest/java/org/elasticsearch/xpack/security/authc/oidc/OpenIdConnectAuthIT.java` (JAVA) | Magnitude: 87.26 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 291, structural_boundaries: 83, core_var_decl: 58, immutability_locks: 35
- `x-pack/plugin/autoscaling/src/test/java/org/elasticsearch/xpack/autoscaling/storage/ReactiveStorageDeciderDecisionTests.java` (JAVA) | Magnitude: 218.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 674, structural_boundaries: 174, args: 166, closures: 108
- `modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/RenameProcessorTests.java` (JAVA) | Magnitude: 58.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 170, structural_boundaries: 66, core_var_decl: 44, test: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `x-pack/plugin/ilm/src/javaRestTest/java/org/elasticsearch/xpack/ilm/actions/SearchableSnapshotActionIT.java` (JAVA) | Magnitude: 188.7 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 851, structural_boundaries: 229, safety_bypasses: 127, core_var_decl: 124
- `x-pack/plugin/fleet/src/main/java/org/elasticsearch/xpack/fleet/action/PostSecretRequest.java` (JAVA) | Magnitude: 33.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 33, api: 12, args: 11
- `x-pack/plugin/slm/src/internalClusterTest/java/org/elasticsearch/xpack/slm/SLMSnapshotBlockingIntegTests.java` (JAVA) | Magnitude: 147.04 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 638, structural_boundaries: 131, core_var_decl: 87, test: 86
- `libs/core/src/main/java/org/elasticsearch/core/CharArrays.java` (JAVA) | Magnitude: 97.2 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 20, core_var_decl: 17, branch: 16
- `x-pack/plugin/eql/src/main/java/org/elasticsearch/xpack/eql/expression/function/scalar/string/BetweenFunctionProcessor.java` (JAVA) | Magnitude: 51.46 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 28, api: 14, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `x-pack/plugin/spatial/src/test/java/org/elasticsearch/xpack/spatial/common/H3SphericalGeometryTests.java` (JAVA) | Magnitude: 45.1 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 34, core_var_decl: 24, import: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/framework/src/main/java/org/elasticsearch/transport/AbstractSimpleTransportTestCase.java` -> **Brian Seeders** (100.0% isolated ownership) | Magnitude: 1312.18
- `test/framework/src/main/java/org/elasticsearch/test/InternalTestCluster.java` -> **Iraklis Psaroudakis** (100.0% isolated ownership) | Magnitude: 1270.1
- `x-pack/plugin/blob-cache/src/main/java/org/elasticsearch/blobcache/shared/SharedBlobCacheService.java` -> **Chris Hegarty** (100.0% isolated ownership) | Magnitude: 1157.46
- `test/framework/src/main/java/org/elasticsearch/cluster/coordination/AbstractCoordinatorTestCase.java` -> **David Turner** (100.0% isolated ownership) | Magnitude: 1013.28
- `x-pack/plugin/blob-cache/src/test/java/org/elasticsearch/blobcache/shared/SharedBlobCacheServiceTests.java` -> **Chris Hegarty** (100.0% isolated ownership) | Magnitude: 901.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `x-pack/plugin/mapper-aggregate-metric/src/main/java/org/elasticsearch/xpack/aggregatemetric/mapper/AggregateMetricDoubleBlockLoader.java` -> **Severity: 0.28** (Bridge: 0.0028 * Flux: 99.9816%)
- `libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java` -> **Severity: 0.088** (Bridge: 0.0028 * Flux: 31.4547%)
- `modules/percolator/src/main/java/org/elasticsearch/percolator/PercolatorFieldMapper.java` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 98.784%)
- `x-pack/plugin/snapshot-repo-test-kit/src/main/java/org/elasticsearch/repositories/blobstore/testkit/analyze/RepositoryAnalyzeAction.java` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 93.337%)
- `modules/aggregations/src/main/java/org/elasticsearch/aggregations/bucket/histogram/InternalAutoDateHistogram.java` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.9786%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java` -> **Severity: 14.533** (Embedded: 0.1817 * Error Risk: 80.0%)
- `x-pack/plugin/mapper-aggregate-metric/src/main/java/org/elasticsearch/xpack/aggregatemetric/mapper/AggregateMetricDoubleBlockLoader.java` -> **Severity: 9.879** (Embedded: 0.1229 * Error Risk: 80.3623%)
- `test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java` -> **Severity: 9.678** (Embedded: 0.1715 * Error Risk: 56.4201%)
- `libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentType.java` -> **Severity: 9.308** (Embedded: 0.1695 * Error Risk: 54.915%)
- `libs/core/src/main/java/org/elasticsearch/core/TimeValue.java` -> **Severity: 9.101** (Embedded: 0.1554 * Error Risk: 58.5734%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libs/x-content/src/main/java/org/elasticsearch/xcontent/XContentBuilder.java` -> **Severity: 1213.606** (Blast Radius: 15.302 * Doc Risk: 79.3103%)
- `test/framework/src/main/java/org/elasticsearch/test/ESTestCase.java` -> **Severity: 1199.015** (Blast Radius: 27.455 * Doc Risk: 43.672%)
- `libs/core/src/main/java/org/elasticsearch/core/TimeValue.java` -> **Severity: 1084.864** (Blast Radius: 13.074 * Doc Risk: 82.9787%)
- `libs/core/src/main/java/org/elasticsearch/core/RestApiVersion.java` -> **Severity: 835.5** (Blast Radius: 8.355 * Doc Risk: 100.0%)
- `libs/geo/src/main/java/org/elasticsearch/geometry/utils/WellKnownText.java` -> **Severity: 606.004** (Blast Radius: 6.269 * Doc Risk: 96.6667%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 460 literal sites + 7 sites through wrappers = 467
- **`panics_and_aborts`:** 5796 literal sites + 333 sites through wrappers = 6129

- `readCefMessageFile` (function, panics_and_aborts, primitive): 28 call sites in 1 files -- `modules/ingest-common/src/test/java/org/elasticsearch/ingest/common/CefProcessorTests.java`
- `failAndThrow` (function, panics_and_aborts, primitive): 22 call sites in 2 files -- `test/fixtures/gcs-fixture/src/main/java/fixture/gcs/MockGcsBlobStore.java`
- `expectZipException` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/FileCheckActions.java`
- `requestHandlerShouldNotBeCalled` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `test/framework/src/test/java/org/elasticsearch/transport/DisruptableMockTransportTests.java`
- `throwDefinitionFailure` (function, panics_and_aborts, primitive): 15 call sites in 1 files -- `build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/transport/ValidateTransportVersionResourcesTask.java`
- `callSingleDistanceFloat` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkVectorLibrary.java`
- `mv` (function, panics_and_aborts, primitive): 9 call sites in 4 files -- `qa/packaging/src/test/java/org/elasticsearch/packaging/util/FileUtils.java`
- `parseValue` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `x-pack/plugin/sql/sql-client/src/main/java/org/elasticsearch/xpack/sql/client/ConnectionConfiguration.java`
- `assertUnblockIn10s` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `x-pack/plugin/rollup/src/test/java/org/elasticsearch/xpack/rollup/job/RollupJobTaskTests.java`
- `nativeSimilarityBulk` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `libs/native/src/test/java/org/elasticsearch/nativeaccess/jdk/JDKVectorLibraryBBQTests.java`
- `responseException` (function, panics_and_aborts, primitive): 7 call sites in 3 files -- `x-pack/plugin/monitoring/src/test/java/org/elasticsearch/xpack/monitoring/exporter/http/AbstractPublishableHttpResourceTestCase.java`
- `similarityBulk` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `libs/native/src/test/java/org/elasticsearch/nativeaccess/jdk/JDKVectorLibraryInt4Tests.java`
*(+99 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 329592 call pairs -- scoped 30.6%, unique 1.1%, ambiguous 32.9%, external 35.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 326165 | 30.7% | 1.1% | 33.0% | 35.2% |
| groovy | 2599 | 22.0% | 1.4% | 34.0% | 42.6% |
| shell | 518 | 12.7% | 0.0% | 0.0% | 87.3% |
| python | 192 | 18.2% | 0.0% | 0.0% | 81.8% |
| typescript | 60 | 23.3% | 0.0% | 0.0% | 76.7% |
| ruby | 58 | 29.3% | 0.0% | 0.0% | 70.7% |

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
