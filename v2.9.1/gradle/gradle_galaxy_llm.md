# ARCHITECTURAL_BRIEF: gradle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gradle/gradle` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 19036 analyzed artifact(s), 1287752 LOC.
- **Load-bearing artifact:** `platforms/core-runtime/base-services/src/main/java/org/gradle/api/Action.java` -- 1099 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapter.java` -- pulls in 261 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `platforms/documentation/docs/src/snippets/signing/configurations/common/secKeyRingFile.gpg` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 26690 |
| Analyzed Artifacts (Scanned) | 19036 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7654 |
| Total LOC | 1287752 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.3% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6078 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1359 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.3773 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 898 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 10705 | 537020 | 56.2% |
| GROOVY | 6422 | 620438 | 33.7% |
| KOTLIN | 1382 | 122437 | 7.3% |
| PLAINTEXT | 233 | 18 | 1.2% |
| XML | 138 | 0 | 0.7% |
| MARKDOWN | 39 | 0 | 0.2% |
| CPP | 31 | 4310 | 0.2% |
| SCALA | 29 | 349 | 0.2% |
| CSS | 10 | 614 | 0.1% |
| JAVASCRIPT | 9 | 803 | 0.0% |
| C | 9 | 81 | 0.0% |
| HTML | 8 | 418 | 0.0% |
| PHP | 7 | 133 | 0.0% |
| SWIFT | 6 | 42 | 0.0% |
| JSON | 3 | 778 | 0.0% |
| SHELL | 1 | 60 | 0.0% |
| YAML | 1 | 7 | 0.0% |
| BATCH | 1 | 64 | 0.0% |
| CSV | 1 | 179 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `3.176`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +3.18; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 17%, State Mutators Files 15%, Large Core Modules 12%, Generic / Templated Code Files 11%, Encapsulated Accessors Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18763 | 98.6% |
| Unknown | 19 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 254 | 1.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7654*

**Composition by Extension & Reason:**
- `.kts`: 1767x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 1602x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 834x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 78 exceeds 500 chars), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.conf`: 714x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.conf)
- `.xml`: 574x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 58 exceeds 500 chars), 1x Excluded (Static Asset Blob without Intent: 1396 LOC)
- `.out`: 429x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adoc`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 269x Excluded (Explicitly Denied Extension: '.png')
- `.groovy`: 157x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 24 exceeds 500 chars), 1x Excluded (Saturation: Line 84 exceeds 500 chars)
- `.txt`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1187 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2121 LOC)
- `no_extension`: 78x Unsupported Format (.undeterminable), 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.toml`: 43x Unsupported Format (.toml), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.toml')
- `.h`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 6563 commas in 1422 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5144 LOC)
- `.kt`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 13 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.1 | 2.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 32.7 | 36.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.3 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.1 | 5.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18630 | 3979 | 2 | `platforms/core-configuration/file-collections/src/test/groovy/org/gradle/api/internal/file/collections/DefaultConfigurableFileCollectionSpec.groovy` |
| cleanup | 1005 | 440 | 0 | `platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/LockOnDemandCrossProcessCacheAccessTest.groovy` |
| guards | 103163 | 10255 | 15 | `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java` |
| danger | 39044 | 6928 | 6 | `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapter.java` |
| concurrency | 13416 | 1871 | 0 | `subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskContainerTest.groovy` |
| connectivity | 75323 | 11781 | 10 | `platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/instantiation/generator/AsmBackedClassGeneratorTest.java` |
| io | 36010 | 5136 | 5 | `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy` |
| crypto | 0 | 0 | 0 | - |
| ipc | 36 | 16 | 0 | `subprojects/core/src/main/java/org/gradle/internal/classpath/Instrumented.java` |
| time | 421 | 122 | 0 | `testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/CrossVersionResultsStore.java` |
| serialization | 97 | 49 | 0 | `platforms/core-runtime/build-operations-trace/src/main/java/org/gradle/internal/operations/trace/BuildOperationTrace.java` |
| regex | 287 | 159 | 0 | `testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/OutputScrapingExecutionFailure.java` |
| events | 3915 | 800 | 0 | `platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/sink/GroupingProgressLogEventGeneratorTest.groovy` |
| tests | 105240 | 5392 | 15 | `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy` |
| docs | 20090 | 6729 | 3 | `subprojects/core-api/src/main/java/org/gradle/api/Project.java` |
| debt | 8179 | 2357 | 1 | `platforms/software/publish/src/test/groovy/org/gradle/api/publish/internal/metadata/GradleModuleMetadataWriterTest.groovy` |
| mutation | 178045 | 12317 | 25 | `platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/ErrorParsingTest.kt` |
| dead_code | 46794 | 8976 | 7 | `subprojects/core/src/main/java/org/gradle/api/internal/project/MutableStateAccessAwareProject.java` |
| credential | 181 | 118 | 0 | `testing/internal-performance-testing/src/test/groovy/org/gradle/performance/mutator/ClearArtifactTransformCacheWithoutInstrumentedJarsMutatorTest.groovy` |
| threat | 5651 | 1490 | 0 | `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/serialization/SchemaSerialization.kt` |
| ml_ai | 598 | 207 | 0 | `subprojects/core/src/main/java/org/gradle/internal/typeconversion/DefaultTypeConverter.java` |
| ui | 562 | 155 | 0 | `platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/DependencyCollectorFunctionExtractorAndRuntimeResolver.kt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy` (Hits: 293)
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/undeclared/MethodReferenceInstrumentationIntegrationTest.groovy` (Hits: 172)
- `platforms/documentation/samples/src/integTest/groovy/org/gradle/integtests/samples/files/SamplesCopyIntegrationTest.groovy` (Hits: 134)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Action.java** (`platforms/core-runtime/base-services/src/main/java/org/gradle/api/Action.java`) — 1099 inbound connections
2. **AbstractIntegrationSpec.groovy** (`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractIntegrationSpec.groovy`) — 910 inbound connections
3. **Scope.java** (`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/service/scopes/Scope.java`) — 814 inbound connections
4. **Rule.java** (`subprojects/core-api/src/main/java/org/gradle/api/Rule.java`) — 779 inbound connections
5. **ServiceScope.java** (`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/service/scopes/ServiceScope.java`) — 775 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **BuildProgressListenerAdapter.java** (`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapter.java`) — 261 outbound dependencies
2. **BuildScopeServices.java** (`subprojects/core/src/main/java/org/gradle/internal/service/scopes/BuildScopeServices.java`) — 245 outbound dependencies
3. **DefaultDependencyManagementServices.java** (`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/DefaultDependencyManagementServices.java`) — 141 outbound dependencies
4. **DefaultProject.java** (`subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultProject.java`) — 132 outbound dependencies
5. **ConfigurationCacheCodecs.kt** (`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ConfigurationCacheCodecs.kt`) — 131 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `doResolveAugmentation` **(Stateful Encapsulated Methods)** (@ `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/FunctionCallResolver.kt`) -> Impact: **222.1** | LOC: 670
- `writeViewMethods` **(Many-Argument Workhorses)** (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ManagedProxyClassGenerator.java`) -> Impact: **122.4** | LOC: 78
- `startElement` **(Many-Argument Workhorses)** (@ `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyXmlModuleDescriptorParser.java`) -> Impact: **117.6** | LOC: 72
- `startElement` **(Many-Argument Workhorses)** (@ `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlReader.java`) -> Impact: **114.5** | LOC: 98
- `write` **(Defensive Guards)** (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/SnapshotSerializer.java`) -> Impact: **108.2** | LOC: 121
- `stateFileForSharedObjects` **(Stateful Encapsulated Methods)** (@ `platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheState.kt`) -> Impact: **95.8** | LOC: 836
- `escapeJavaStyleString` **(Many-Argument Workhorses)** (@ `platforms/core-runtime/base-services/src/main/java/org/gradle/util/internal/TextUtil.java`) -> Impact: **93.5** | LOC: 81
- `build` **(Defensive Guards)** (@ `platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/integtests/fixtures/publish/ModuleVersionSpec.groovy`) -> Impact: **93.2** | LOC: 167
- `validate` **(Compute Cores)** (@ `testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/ResultAssertion.java`) -> Impact: **89.4** | LOC: 91
- `modify` **(Many-Argument Workhorses)** (@ `platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentMapTrie.java`) -> Impact: **88.9** | LOC: 98

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home` | 3 | 15000.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home` | 3 | 15000.0 | 0.0% | 0.0% |
| `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest` | 2 | 10000.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/default` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/subkey` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/gradle` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/invalid-key-ring` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/rfc9580v6sample` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/configurations/common` | 1 | 5000.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/maven-publish/groovy` | 1 | 5000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `platforms/core-configuration/input-tracking/src/main/java/org/gradle/internal/configuration/inputs/NoOpInputsListener.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/ClassGenerator.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ModelPropertyExtractionContext.java` -> **100.0%** Exposure
- `platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeatureBindingDeclaration.java` -> **100.0%** Exposure
- `platforms/core-execution/build-cache/src/jmh/java/org/gradle/caching/internal/tasks/InMemoryDataAccessor.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/CalculatedTaskInputFileCollection.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/ListValueSnapshot.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/util/internal/ClosureBackedAction.java` -> **100.0%** Exposure
- `platforms/core-runtime/base-services/src/main/java/org/gradle/internal/util/PropertiesUtils.java` -> **100.0%** Exposure
- `platforms/core-runtime/base-services/src/main/java/org/gradle/internal/util/Trie.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/instantiation/generator/AsmBackedClassGeneratorTest.java` -> **101** Orphaned Functions | **34** Duplicates
- `subprojects/core/src/main/java/org/gradle/api/internal/project/MutableStateAccessAwareProject.java` -> **104** Orphaned Functions | **0** Duplicates
- `platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/MapPropertySpec.groovy` -> **102** Orphaned Functions | **0** Duplicates
- `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy` -> **99** Orphaned Functions | **0** Duplicates
- `platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/CollectionPropertySpec.groovy` -> **97** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `platforms/software/security/src/test/groovy/org/gradle/security/internal/SecuritySupportSpec.groovy` -> **99.9735%** Exposure
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/S3ClientIntegrationTest.groovy` -> **99.6391%** Exposure
- `platforms/core-execution/build-cache-http/src/integTest/groovy/org/gradle/caching/http/internal/HttpBuildCacheServiceIntegrationTest.groovy` -> **38.5006%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `64` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `126489` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `platforms/documentation/docs/src/snippets/signing/configurations/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/pubring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/trustdb.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/pubring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/trustdb.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/maven-publish/groovy/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/maven-publish/kotlin/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/tasks/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest/invalid-utf8-public-key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest/invalid-utf8-secret-key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/default/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/subkey/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/testFixtures/resources/keys/gradle/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/testFixtures/resources/keys/invalid-key-ring/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/testFixtures/resources/keys/rfc9580v6sample/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `testing/internal-integ-testing/src/main/resources/sshd-config/test-dsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/BuildScriptBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1394.14 | **LOC:** 2469 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **43**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.4%), Mutation Surface (formerly State Flux) (86.7%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.4971% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forInsecureProtocolOption` **(Compute Cores)** (Impact: 26.7)
  * `printStatement` **(Stateful Encapsulated Methods)** (Impact: 21.7)
  * `writeCodeTo` **(Compute Cores)** (Impact: 15.3)
  * `writeBodyTo` **(Compute Cores)** (Impact: 15.0)
  * `with` **(Compute Cores)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *Api Near Db Sink:* 9 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 579`, `args: 309`, `func_start: 302`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 183`, `planned_debt: 4`, `duplicate_logic: 27`
* *Architecture:* `io: 61`, `api: 215`, `import: 43`
* *Defense:* `safety: 19`, `doc: 37`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000118
  * `Imports (Out-Degree: 17):` com.google.common.base.Objects, com.google.common.base.Splitter, com.google.common.collect.ListMultimap, com.google.common.collect.MultimapBuilder, java.io.File, java.io.PrintWriter, java.io.StringWriter, java.net.URI...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/GradleResolveVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1138.4 | **LOC:** 1670 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **57**; blast radius 0.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Complexity Load (formerly Cognitive Load) (65.8%), Debt Markers (formerly Tech Debt) (20.1%)
- **Documentation Coverage:** 94.0594% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveFromModule` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `checkCyclicInheritance` **(Stateful Encapsulated Methods)** (Impact: 38.0)
  * `visitClass` **(Compute Cores)** (Impact: 34.9)
  * `resolveNestedClass` **(Compute Cores)** (Impact: 32.8)
  * `transform` **(Defensive Guards)** (Impact: 28.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 123 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 337`, `args: 63`, `func_start: 63`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 177`, `dead_code: 3`, `planned_debt: 4`, `unreferenced_by_name: 8`
* *Architecture:* `io: 2`, `api: 39`, `import: 57`
* *Defense:* `safety: 50`, `doc: 5`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.collect.ImmutableMap, java.lang.annotation.Retention, java.lang.annotation.RetentionPolicy, java.lang.reflect.Modifier, java.util.HashMap, java.util.HashSet, java.util.LinkedHashMap, java.util.LinkedList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AbstractClassGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1123.88 | **LOC:** 1598 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **69**; blast radius 0.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Guard Balance (formerly Safety Score) (80.2%), Complexity Load (formerly Cognitive Load) (69.4%), Debt Markers (formerly Tech Debt) (28.2%)
- **Documentation Coverage:** 94.0928% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspectType` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `generateUnderLock` **(Compute Cores)** (Impact: 45.5)
  * `AbstractClassGenerator` **(Stateful Encapsulated Methods)** (Impact: 44.0)
  * `validateMethod` **(Stateful Encapsulated Methods)** (Impact: 36.8)
  * `assembleProperties` **(Stateful Encapsulated Methods)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 432`, `args: 176`, `func_start: 171`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 72`, `import: 69`
* *Defense:* `safety: 3`, `doc: 12`, `test: 5`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` com.google.common.collect.ImmutableCollection, com.google.common.collect.ImmutableList, com.google.common.collect.ImmutableListMultimap, com.google.common.collect.ImmutableMultimap, com.google.common.collect.ImmutableSet, com.google.common.collect.LinkedHashMultimap, com.google.common.collect.Ordering, com.google.common.collect.SetMultimap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyXmlModuleDescriptorParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1100.7 | **LOC:** 1415 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **79**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (91.1%), Complexity Load (formerly Cognitive Load) (82.9%), Connectivity (formerly Api Exposure) (21.3%)
- **Documentation Coverage:** 97.8417% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startElement` **(Many-Argument Workhorses)** (Impact: 117.6)
  * `endElement` **(Many-Argument Workhorses)** (Impact: 79.2)
  * `parseDepsConfs` **(Many-Argument Workhorses)** (Impact: 67.5)
  * `confStarted` **(Compute Cores)** (Impact: 40.5)
  * `parseRule` **(Stateful Encapsulated Methods)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 72 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 307`, `args: 93`, `func_start: 93`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 115`, `dead_code: 2`
* *Architecture:* `io: 6`, `api: 52`, `concurrency: 3`, `import: 79`
* *Defense:* `safety: 23`, `doc: 4`, `sync_locks: 7`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000172
  * `Imports (Out-Degree: 28):` com.google.common.base.Joiner, com.google.common.collect.Sets, java.io.File, java.io.IOException, java.io.InputStream, java.net.MalformedURLException, java.net.URL, java.text.ParseException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/DefaultServiceRegistry.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1080.0 | **LOC:** 1498 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **31**; blast radius 0.108; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (37.2%)
- **Documentation Coverage:** 89.4309% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collectProvidersForClassHierarchyOf` **(Stateful Encapsulated Methods)** (Impact: 29.1)
  * `getService` **(Generic / Templated Code)** (Impact: 24.4)
  * `ConstructorService` **(Stateful Encapsulated Methods)** (Impact: 23.0)
  * `instanceRealized` **(Defensive Guards)** (Impact: 21.1)
  * `find` **(Stateful Encapsulated Methods)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 358`, `args: 159`, `func_start: 155`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 85`, `planned_debt: 5`, `duplicate_logic: 5`
* *Architecture:* `api: 95`, `concurrency: 8`, `import: 31`
* *Defense:* `safety: 35`, `doc: 12`, `test: 13`, `sync_locks: 3`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.024681
  * `Imports (Out-Degree: 6):` java.io.Closeable, java.lang.annotation.Annotation, java.lang.reflect.Constructor, java.lang.reflect.InvocationTargetException, java.lang.reflect.Modifier, java.lang.reflect.ParameterizedType, java.lang.reflect.Type, java.lang.reflect.WildcardType...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/PropertySpec.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1000.32 | **LOC:** 3128 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.5%), Mutation Surface (formerly State Flux) (79.8%), Connectivity (formerly Api Exposure) (65.0%), Guard Balance (formerly Safety Score) (62.1%)
- **Documentation Coverage:** 97.5779% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `namedConsumer` **(Stateful Encapsulated Methods)** (Impact: 12.8)
  * `"cannot set value after value finalized"` **(I/O & Config Routines)** (Impact: 6.8)
  * `"cannot set value after value finalized implicitly and before queried"` **(I/O & Config Routines)** (Impact: 6.8)
  * `"cannot set value after value finalized implicitly"` **(Type Conversions)** (Impact: 6.8)
  * `"cannot set value after value finalized after value finalized implicitly"` **(I/O & Config Routines)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 149
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 613`, `args: 156`, `func_start: 156`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 150`, `state_mutation: 171`, `planned_debt: 7`
* *Architecture:* `api: 134`, `concurrency: 54`, `import: 16`
* *Defense:* `safety: 5`, `doc: 5`, `test: 576`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.3e-05
  * `Imports (Out-Degree: 13):` java.util.concurrent.Callable, java.util.function.Consumer, org.gradle.api.Action, org.gradle.api.Task, org.gradle.api.Transformer, org.gradle.api.internal.provider.CircularEvaluationSpec.CircularChainEvaluationSpec, org.gradle.api.internal.provider.CircularEvaluationSpec.ProviderConsumer.GET_PRODUCER, org.gradle.api.provider.Provider...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 949.98 | **LOC:** 2094 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **93**; blast radius 0.04; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.6%), Mutation Surface (formerly State Flux) (34.8%), Complexity Load (formerly Cognitive Load) (28.1%), Connectivity (formerly Api Exposure) (23.1%)
- **Documentation Coverage:** 95.5645% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitArrayElements` **(Stateful Encapsulated Methods)** (Impact: 37.1)
  * `visitAnnotationValues` **(Stateful Encapsulated Methods)** (Impact: 25.4)
  * `applyReadOnlyManagedStateToGetter` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `decorateAndInject` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* /** * Returns a generator that applies DSL mix-in, extensibility and service injection for generated...
  * `addConstructor` **(Compute Cores)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 409`, `args: 169`, `func_start: 152`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 81`, `dead_code: 22`, `planned_debt: 7`
* *Architecture:* `api: 93`, `concurrency: 3`, `import: 93`
* *Defense:* `safety: 18`, `doc: 6`, `immutability_locks: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` 0.000138 | `Ripple Effect (Closeness):` 0.015888
  * `Imports (Out-Degree: 44):` com.google.common.collect.ImmutableSet, groovy.lang.Closure, groovy.lang.GroovyObject, groovy.lang.GroovySystem, groovy.lang.MetaClass, groovy.lang.MetaClassRegistry, groovy.lang.MetaProperty.getSetterName, java.lang.annotation.Annotation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperGenerationIntegrationTest.groovy` -> Churn: **70.87%** | Cog Load: 73.4791% | Debt: 99.9483%
- `platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/dependencyConfigurationSchema.kt` -> Churn: **58.86%** | Cog Load: 12.5904% | Debt: 99.7527%
- `platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/TaskbarProgressResetFunctionalTest.groovy` -> Churn: **58.86%** | Cog Load: 0.0% | Debt: 99.3307%
- `platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperHttpIntegrationTest.groovy` -> Churn: **58.86%** | Cog Load: 8.1179% | Debt: 96.7751%
- `subprojects/core/src/main/java/org/gradle/initialization/DefaultSettingsPreparer.java` -> Churn: **56.41%** | Cog Load: 22.4596% | Debt: 65.6752%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/DefaultServiceRegistry.java` -> **Alex Semin** (100.0% isolated ownership) | Magnitude: 1080.0
- `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java` -> **Sterling Greene** (100.0% isolated ownership) | Magnitude: 949.98
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/adapter/ProtocolToModelAdapter.java` -> **Justin Van Dort** (100.0% isolated ownership) | Magnitude: 871.66
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/DefaultConfiguration.java` -> **Gary Hale** (100.0% isolated ownership) | Magnitude: 864.54
- `subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultProject.java` -> **Gary Hale** (100.0% isolated ownership) | Magnitude: 774.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `subprojects/core/src/testFixtures/groovy/org/gradle/util/TestUtil.groovy` -> **Severity: 0.153** (Bridge: 0.0021 * Flux: 72.652%)
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/Collectors.java` -> **Severity: 0.078** (Bridge: 0.0011 * Flux: 71.5669%)
- `platforms/core-runtime/start-parameter/src/main/java/org/gradle/StartParameter.java` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 99.8225%)
- `platforms/extensibility/unit-test-fixtures/src/main/java/org/gradle/testfixtures/internal/ProjectBuilderImpl.java` -> **Severity: 0.034** (Bridge: 0.0009 * Flux: 37.0634%)
- `platforms/core-runtime/build-state/src/main/java/org/gradle/internal/buildprocess/BuildProcessState.java` -> **Severity: 0.031** (Bridge: 0.001 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/UncheckedException.java` -> **Severity: 9.992** (Embedded: 0.1249 * Error Risk: 80.0%)
- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/Cast.java` -> **Severity: 8.346** (Embedded: 0.1039 * Error Risk: 80.3089%)
- `platforms/core-runtime/base-services/src/main/java/org/gradle/internal/SystemProperties.java` -> **Severity: 7.127** (Embedded: 0.0883 * Error Risk: 80.717%)
- `platforms/core-runtime/start-parameter/src/main/java/org/gradle/StartParameter.java` -> **Severity: 7.065** (Embedded: 0.089 * Error Risk: 79.3512%)
- `platforms/core-execution/hashing/src/main/java/org/gradle/internal/hash/HashCode.java` -> **Severity: 6.834** (Embedded: 0.0948 * Error Risk: 72.0537%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/file/TestFile.java` -> **Severity: 895.539** (Blast Radius: 11.296 * Doc Risk: 79.2793%)
- `testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractIntegrationSpec.groovy` -> **Severity: 684.207** (Blast Radius: 7.757 * Doc Risk: 88.2051%)
- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/api/UncheckedIOException.java` -> **Severity: 459.75** (Blast Radius: 6.13 * Doc Risk: 75.0%)
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/Collectors.java` -> **Severity: 415.1** (Blast Radius: 4.151 * Doc Risk: 100.0%)
- `platforms/core-execution/hashing/src/main/java/org/gradle/internal/hash/HashCode.java` -> **Severity: 371.339** (Blast Radius: 4.159 * Doc Risk: 89.2857%)

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
