# ARCHITECTURAL_BRIEF: gradle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gradle/gradle` |
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
- **Scope:** 19163 analyzed artifact(s), 1292755 LOC.
- **Load-bearing artifact:** `platforms/core-runtime/base-services/src/main/java/org/gradle/api/Action.java` -- 1076 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 19163 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7527 |
| Total LOC | 1292755 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.8% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6384 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.123 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 931 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 10707 | 537076 | 55.9% |
| GROOVY | 6428 | 620906 | 33.5% |
| KOTLIN | 1459 | 125764 | 7.6% |
| PLAINTEXT | 238 | 17 | 1.2% |
| XML | 139 | 0 | 0.7% |
| MARKDOWN | 43 | 0 | 0.2% |
| YAML | 31 | 1045 | 0.2% |
| CPP | 31 | 4324 | 0.2% |
| SCALA | 29 | 349 | 0.2% |
| C | 10 | 78 | 0.1% |
| CSS | 10 | 614 | 0.1% |
| JAVASCRIPT | 9 | 803 | 0.0% |
| HTML | 8 | 418 | 0.0% |
| PHP | 7 | 133 | 0.0% |
| SWIFT | 6 | 42 | 0.0% |
| SHELL | 3 | 165 | 0.0% |
| JSON | 3 | 778 | 0.0% |
| BATCH | 1 | 64 | 0.0% |
| CSV | 1 | 179 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 19146 |
| unknown | unknown | 17 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 17%, State Mutators Files 15%, Large Core Modules 12%, Generic / Templated Code Files 12%, Encapsulated Accessors Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18882 | 98.5% |
| Unknown | 17 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 264 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7527*

**Composition by Extension & Reason:**
- `.kts`: 1489x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Machine-Generated Source Code Signature: 44 LOC), 6x Excluded (Machine-Generated Source Code Signature: 45 LOC)
- `.gradle`: 1601x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 834x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.conf`: 714x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.conf)
- `.xml`: 574x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1396 LOC)
- `.out`: 429x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adoc`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 269x Excluded (Explicitly Denied Extension: '.png')
- `.groovy`: 157x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 24 exceeds 500 chars), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.txt`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `no_extension`: 78x Unsupported Format (.undeterminable), 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.toml`: 43x Unsupported Format (.toml), 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.toml')
- `.h`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1422 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5144 LOC)
- `.kt`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 13 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.8 | 29.3 | 43.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.0 | 5.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18457 | 3976 | 2 | `platforms/core-configuration/file-collections/src/test/groovy/org/gradle/api/internal/file/collections/DefaultConfigurableFileCollectionSpec.groovy` |
| cleanup | 1012 | 443 | 0 | `platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/LockOnDemandCrossProcessCacheAccessTest.groovy` |
| guards | 103189 | 10307 | 15 | `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java` |
| danger | 39106 | 6946 | 6 | `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapter.java` |
| concurrency | 13483 | 1876 | 0 | `subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskContainerTest.groovy` |
| connectivity | 75287 | 11797 | 10 | `platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/instantiation/generator/AsmBackedClassGeneratorTest.java` |
| io | 36162 | 5146 | 5 | `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy` |
| crypto | 0 | 0 | 0 | - |
| ipc | 39 | 17 | 0 | `subprojects/core/src/main/java/org/gradle/internal/classpath/Instrumented.java` |
| time | 421 | 122 | 0 | `testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/CrossVersionResultsStore.java` |
| serialization | 97 | 49 | 0 | `platforms/core-runtime/build-operations-trace/src/main/java/org/gradle/internal/operations/trace/BuildOperationTrace.java` |
| regex | 429 | 179 | 0 | `platforms/core-runtime/files/src/test/groovy/org/gradle/api/internal/file/pattern/RegExpPatternStepTest.java` |
| events | 3937 | 811 | 0 | `platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/sink/GroupingProgressLogEventGeneratorTest.groovy` |
| tests | 105341 | 5398 | 15 | `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy` |
| docs | 20168 | 6762 | 3 | `subprojects/core-api/src/main/java/org/gradle/api/Project.java` |
| debt | 8235 | 2379 | 1 | `platforms/software/publish/src/test/groovy/org/gradle/api/publish/internal/metadata/GradleModuleMetadataWriterTest.groovy` |
| mutation | 178723 | 12407 | 24 | `platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/ErrorParsingTest.kt` |
| dead_code | 46622 | 8901 | 7 | `platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/instantiation/generator/AsmBackedClassGeneratorTest.java` |
| credential | 181 | 118 | 0 | `testing/internal-performance-testing/src/test/groovy/org/gradle/performance/mutator/ClearArtifactTransformCacheWithoutInstrumentedJarsMutatorTest.groovy` |
| threat | 36 | 21 | 0 | `platforms/jvm/language-java/src/test/groovy/org/gradle/api/internal/tasks/compile/incremental/transaction/CompileTransactionTest.groovy` |
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

1. **Action.java** (`platforms/core-runtime/base-services/src/main/java/org/gradle/api/Action.java`) — 1076 inbound connections
2. **AbstractIntegrationSpec.groovy** (`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractIntegrationSpec.groovy`) — 911 inbound connections
3. **Scope.java** (`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/service/scopes/Scope.java`) — 831 inbound connections
4. **ServiceScope.java** (`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/service/scopes/ServiceScope.java`) — 775 inbound connections
5. **Rule.java** (`subprojects/core-api/src/main/java/org/gradle/api/Rule.java`) — 765 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **BuildProgressListenerAdapter.java** (`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapter.java`) — 261 outbound dependencies
2. **BuildScopeServices.java** (`subprojects/core/src/main/java/org/gradle/internal/service/scopes/BuildScopeServices.java`) — 245 outbound dependencies
3. **DefaultDependencyManagementServices.java** (`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/DefaultDependencyManagementServices.java`) — 141 outbound dependencies
4. **DefaultProject.java** (`subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultProject.java`) — 132 outbound dependencies
5. **ConfigurationCacheCodecs.kt** (`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ConfigurationCacheCodecs.kt`) — 131 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `startElement` **(Many-Argument Workhorses)** (@ `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyXmlModuleDescriptorParser.java`) -> Impact: **113.2** | LOC: 72
- `write` **(Defensive Guards)** (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/SnapshotSerializer.java`) -> Impact: **101.3** | LOC: 121
- `build` **(Defensive Guards)** (@ `platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/integtests/fixtures/publish/ModuleVersionSpec.groovy`) -> Impact: **93.2** | LOC: 167
- `visitINVOKESTATIC` **(Many-Argument Workhorses)** (@ `subprojects/core/src/main/java/org/gradle/internal/classpath/transforms/AdhocInterceptors.java`) -> Impact: **88.0** | LOC: 95
- `publishTo` **(Many-Argument Workhorses)** (@ `testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/gradle/GradleFileModuleAdapter.groovy`) -> Impact: **83.8** | LOC: 186
- `"writes file for component with attributes (with build id: #withBuildId)"` **(I/O & Config Routines)** (@ `platforms/software/publish/src/test/groovy/org/gradle/api/publish/internal/metadata/GradleModuleMetadataWriterTest.groovy`) -> Impact: **77.3** | LOC: 1226
- `modify` **(Many-Argument Workhorses)** (@ `platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentMapTrie.java`) -> Impact: **73.9** | LOC: 98
- `startElement` **(Many-Argument Workhorses)** (@ `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlReader.java`) -> Impact: **69.7** | LOC: 98
- `escapeJavaStyleString` **(Many-Argument Workhorses)** (@ `platforms/core-runtime/base-services/src/main/java/org/gradle/util/internal/TextUtil.java`) -> Impact: **68.9** | LOC: 81
- `variants` **(Callbacks & Closures)** (@ `testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/gradle/GradleFileModuleAdapter.groovy`) -> Impact: **67.2** | LOC: 157

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home` | 3 | 15000.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home` | 3 | 15000.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/default` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/subkey` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/gradle` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/invalid-key-ring` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/rfc9580v6sample` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/configurations/common` | 1 | 5000.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/maven-publish/groovy` | 1 | 5000.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/maven-publish/kotlin` | 1 | 5000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `build-logic/performance-testing/src/main/groovy/gradlebuild/performance/junit4/JUnit4ObjectFactory.groovy` -> **100.0%** Exposure
- `build-logic/performance-testing/src/main/groovy/gradlebuild/performance/junit4/JUnit4Testsuites.groovy` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheBuildOperationsIntegrationTest.groovy` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/process/instrument/AbstractProcessInstrumentationIntegrationTest.groovy` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/undeclared/UndeclaredFileAccess.groovy` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `gradlew` -> **100.0%** Exposure
- `platforms/core-runtime/process-services/src/test/groovy/org/gradle/api/internal/tasks/util/DefaultJavaForkOptionsTest.groovy` -> **100.0%** Exposure
- `platforms/extensibility/plugin-development/src/integTest/resources/org/gradle/compile/daemon/ParallelCompilerDaemonIntegrationTest/shared/GroovyClass.groovy` -> **100.0%** Exposure
- `platforms/extensibility/plugin-development/src/integTest/resources/org/gradle/compile/daemon/ParallelCompilerDaemonIntegrationTest/shared/build.gradle` -> **100.0%** Exposure
- `platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/groovyapplication/multi/list/LinkedList.groovy.template` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `81` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `124124` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `platforms/documentation/docs/src/snippets/signing/configurations/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/pubring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/trustdb.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/pubring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/trustdb.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/maven-publish/groovy/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/maven-publish/kotlin/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/tasks/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest/invalid-utf8-secret-key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/default/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/subkey/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/testFixtures/resources/keys/gradle/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/testFixtures/resources/keys/invalid-key-ring/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/testFixtures/resources/keys/rfc9580v6sample/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `testing/internal-integ-testing/src/main/resources/sshd-config/test-dsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/BuildScriptBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.973)
- **Top Global Matches:** file_cluster_5: 6.973, file_cluster_12: 8.108, file_cluster_7: 9.673
- **Magnitude:** 1267.94 | **LOC:** 2469 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **43**; blast radius 0.142; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.4%), Mutation Surface (formerly State Flux) (84.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.0%)
- **Documentation Coverage:** 86.4971% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `printStatement` **(Stateful Encapsulated Methods)** (Impact: 16.1)
  * `forInsecureProtocolOption` **(Compute Cores)** (Impact: 14.7)
  * `with` **(Compute Cores)** (Impact: 14.5)
  * `writeCodeTo` **(Compute Cores)** (Impact: 9.7)
  * `printFileHeader` **(Compute Cores)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *Api Near Db Sink:* 9 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 579`, `args: 309`, `func_start: 302`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 183`, `planned_debt: 4`, `duplicate_logic: 27`
* *Architecture:* `io: 61`, `api: 215`, `import: 43`
* *Defense:* `safety: 19`, `doc: 37`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 21):` com.google.common.base.Objects, com.google.common.base.Splitter, com.google.common.collect.ListMultimap, com.google.common.collect.MultimapBuilder, java.io.File, java.io.PrintWriter, java.io.StringWriter, java.net.URI...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/GradleResolveVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.854)
- **Top Global Matches:** file_cluster_5: 9.854, file_cluster_12: 10.666, file_cluster_7: 10.982
- **Magnitude:** 1074.2 | **LOC:** 1670 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **57**; blast radius 0.028; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (62.6%), Debt Markers (formerly Tech Debt) (20.1%)
- **Documentation Coverage:** 94.0594% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveFromModule` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `checkCyclicInheritance` **(Stateful Encapsulated Methods)** (Impact: 29.9)
  * `transform` **(Defensive Guards)** (Impact: 28.4)
  * `visitClass` **(Compute Cores)** (Impact: 27.8)
  * `resolveNestedClass` **(Compute Cores)** (Impact: 27.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 123 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 337`, `args: 63`, `func_start: 63`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 177`, `planned_debt: 4`, `unreferenced_by_name: 8`
* *Architecture:* `io: 2`, `api: 39`, `import: 57`
* *Defense:* `safety: 50`, `doc: 5`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` com.google.common.collect.ImmutableMap, java.lang.annotation.Retention, java.lang.annotation.RetentionPolicy, java.lang.reflect.Modifier, java.util.HashMap, java.util.HashSet, java.util.LinkedHashMap, java.util.LinkedList...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyXmlModuleDescriptorParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.741)
- **Top Global Matches:** file_cluster_5: 8.741, file_cluster_12: 9.655, file_cluster_7: 10.346
- **Magnitude:** 946.8 | **LOC:** 1415 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **79**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (72.2%), Guard Balance (formerly Safety Score) (68.1%), Connectivity (formerly Api Exposure) (21.3%)
- **Documentation Coverage:** 97.8417% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startElement` **(Many-Argument Workhorses)** (Impact: 113.2)
  * `endElement` **(Many-Argument Workhorses)** (Impact: 67.2)
  * `parseDepsConfs` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `parseRule` **(Stateful Encapsulated Methods)** (Impact: 30.2)
  * `confStarted` **(Compute Cores)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 66 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 307`, `args: 93`, `func_start: 93`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 115`
* *Architecture:* `io: 6`, `api: 52`, `concurrency: 3`, `import: 79`
* *Defense:* `safety: 23`, `doc: 4`, `sync_locks: 7`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 31):` com.google.common.base.Joiner, com.google.common.collect.Sets, java.io.File, java.io.IOException, java.io.InputStream, java.net.MalformedURLException, java.net.URL, java.text.ParseException...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.305)
- **Top Global Matches:** file_cluster_12: 8.305, file_cluster_11: 8.64, file_cluster_13: 8.659
- **Magnitude:** 930.78 | **LOC:** 2486 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (87.5%), Guard Balance (formerly Safety Score) (34.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.7%)
- **Documentation Coverage:** 99.2701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestNode` **(Generic / Templated Code)** (Impact: 8.0)
  * `nodes` **(Defensive Guards)** (Impact: 7.5)
  * `assertTasksReady` **(Defensive Guards)** (Impact: 6.7)
  * `assertNodesReady` **(Defensive Guards)** (Impact: 6.7)
  * `visitPreExecutionNodes` **(Generic / Templated Code)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 499
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 368`, `args: 143`, `func_start: 137`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 18`, `planned_debt: 11`, `unreferenced_by_name: 99`
* *Architecture:* `io: 112`, `concurrency: 494`, `import: 29`
* *Defense:* `safety: 66`, `doc: 1`, `test: 582`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 34):` java.util.function.Consumer, javax.annotation.Nullable, org.gradle.api.DefaultTask, org.gradle.api.Task, org.gradle.api.file.FileCollection, org.gradle.api.internal.TaskInternal, org.gradle.api.internal.project.ProjectInternal, org.gradle.api.internal.project.taskfactory.TestTaskIdentities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskContainerTest.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.034)
- **Top Global Matches:** file_cluster_12: 8.034, file_cluster_7: 9.064, file_cluster_5: 9.23
- **Magnitude:** 863.84 | **LOC:** 1683 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (85.0%), Guard Balance (formerly Safety Score) (44.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `void` **(I/O & Config Routines)** (Impact: 3.6)
  * `void` **(Type Conversions)** (Impact: 3.1)
  * `void` **(I/O & Config Routines)** (Impact: 3.1)
  * `void` **(Type Conversions)** (Impact: 3.0)
  * `void` **(Type Conversions)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Concurrency (weighted view):* 660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 257`, `args: 96`, `func_start: 92`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 12`, `planned_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 550`, `import: 33`
* *Defense:* `test: 282`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 33):` java.util.Collections.singletonMap, org.gradle.api.Action, org.gradle.api.DefaultTask, org.gradle.api.GradleException, org.gradle.api.InvalidUserDataException, org.gradle.api.PolymorphicDomainObjectContainer, org.gradle.api.Rule, org.gradle.api.Task...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/instantiation/generator/AsmBackedClassGeneratorTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.08)
- **Top Global Matches:** file_cluster_5: 10.08, file_cluster_12: 11.701, file_cluster_7: 12.775
- **Magnitude:** 862.6 | **LOC:** 2149 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **93**; blast radius 0.023; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (14.3%), Connectivity (formerly Api Exposure) (12.9%), Dead Code Surface (formerly Dead Code) (9.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newInstance` **(Stateful Encapsulated Methods)** (Impact: 15.1)
  * `includesGenericTypeInformationForOverriddenConstructor` **(Type Conversions)** (Impact: 7.9)
  * `getConventionValue` **(Defensive Guards)** (Impact: 5.5)
  * `appliesConventionMappingToGroovyBoolean` **(Annotated & Test Methods)** (Impact: 3.2)
  * `appliesConventionMappingToPropertyWithMultipleSetters` **(Annotated & Test Methods)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *Api Near Db Sink:* 4 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 728`, `args: 287`, `func_start: 287`, `class_start: 88`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 118`, `dead_code: 7`, `duplicate_logic: 34`, `unreferenced_by_name: 101`
* *Architecture:* `api: 288`, `import: 93`
* *Defense:* `safety: 50`, `test: 318`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 50):` com.google.common.base.Joiner, groovy.lang.Closure, groovy.lang.GroovyObject, groovy.lang.MissingMethodException, java.io.IOException, java.lang.annotation.Annotation, java.lang.annotation.ElementType, java.lang.annotation.Retention...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AbstractClassGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.744)
- **Top Global Matches:** file_cluster_5: 6.744, file_cluster_12: 8.518, file_cluster_0: 9.444
- **Magnitude:** 850.58 | **LOC:** 1598 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **69**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (60.2%), Complexity Load (formerly Cognitive Load) (45.8%), Debt Markers (formerly Tech Debt) (28.2%)
- **Documentation Coverage:** 94.0928% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspectType` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `generateUnderLock` **(Compute Cores)** (Impact: 24.2)
  * `validateMethod` **(Stateful Encapsulated Methods)** (Impact: 23.4)
  * `AbstractClassGenerator` **(Stateful Encapsulated Methods)** (Impact: 17.2)
  * `assembleProperties` **(Stateful Encapsulated Methods)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 432`, `args: 176`, `func_start: 171`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 72`, `import: 69`
* *Defense:* `safety: 3`, `doc: 12`, `test: 5`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 41):` com.google.common.collect.ImmutableCollection, com.google.common.collect.ImmutableList, com.google.common.collect.ImmutableListMultimap, com.google.common.collect.ImmutableMultimap, com.google.common.collect.ImmutableSet, com.google.common.collect.LinkedHashMultimap, com.google.common.collect.Ordering, com.google.common.collect.SetMultimap...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/PropertySpec.groovy` (GROOVY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.765)
- **Top Global Matches:** file_cluster_5: 8.765, file_cluster_12: 9.444, file_cluster_7: 9.812
- **Magnitude:** 848.32 | **LOC:** 3128 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.5%), Connectivity (formerly Api Exposure) (65.0%), Guard Balance (formerly Safety Score) (62.1%), Mutation Surface (formerly State Flux) (53.6%)
- **Documentation Coverage:** 97.5779% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `namedConsumer` **(Stateful Encapsulated Methods)** (Impact: 12.8)
  * `"calling #consumer throws exception with proper chain if wrapped property sets convention to itself"` **(Generic / Templated Code)** (Impact: 5.1)
  * `"calling #consumer throws exception with proper chain if wrapped property sets convention to itself and discards producer"` **(Generic / Templated Code)** (Impact: 5.1)
  * `"calling #consumer is safe even if wrapped property sets convention to itself"` **(Generic / Templated Code)** (Impact: 5.1)
  * `accept` **(Generic / Templated Code)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 149
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 613`, `args: 156`, `func_start: 156`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 150`, `state_mutation: 171`, `planned_debt: 7`
* *Architecture:* `api: 134`, `concurrency: 54`, `import: 16`
* *Defense:* `safety: 5`, `doc: 5`, `test: 576`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 21):` java.util.concurrent.Callable, java.util.function.Consumer, org.gradle.api.Action, org.gradle.api.Task, org.gradle.api.Transformer, org.gradle.api.internal.provider.CircularEvaluationSpec.CircularChainEvaluationSpec, org.gradle.api.internal.provider.CircularEvaluationSpec.ProviderConsumer.GET_PRODUCER, org.gradle.api.provider.Provider...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `platforms/native/language-native/src/integTest/groovy/org/gradle/language/fixtures/app/DuplicateObjectiveCBaseNamesTestApp.groovy` (GROOVY) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, args: 4, func_start: 4
- `platforms/native/language-native/src/main/java/org/gradle/language/cpp/internal/DefaultCppLibrary.java` (JAVA) | Magnitude: 51.54 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 51, import: 27, args: 17
- `platforms/core-configuration/model-core/src/integTest/groovy/org/gradle/model/ScalarCollectionIntegrationTest.groovy` (GROOVY) | Magnitude: 2.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 22, test: 8, structural_boundaries: 7, args: 2
- `platforms/enterprise/enterprise-operations/src/main/java/org/gradle/initialization/LoadBuildBuildOperationType.java` (JAVA) | Magnitude: 5.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, class_start: 3, api: 3
- `platforms/native/language-native/src/main/java/org/gradle/language/cpp/internal/DefaultCppComponent.java` (JAVA) | Magnitude: 39.24 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 34, import: 15, api: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `platforms/core-runtime/process-memory-services/src/test/groovy/org/gradle/process/internal/health/memory/DefaultMemoryManagerTest.groovy` (GROOVY) | Magnitude: 54.44 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 57, test: 39, core_var_decl: 36
- `platforms/jvm/plugins-application/src/integTest/groovy/org/gradle/integtests/ApplicationIntegrationSpec.groovy` (GROOVY) | Magnitude: 72.1 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 218, io: 72, structural_boundaries: 63, test: 50
- `platforms/native/platform-native/src/test/groovy/org/gradle/nativeplatform/toolchain/internal/swift/SwiftLinkerTest.groovy` (GROOVY) | Magnitude: 28.56 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 44, core_var_decl: 33, design_camel_case: 21
- `platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/local/model/LocalComponentGraphResolveStateFactoryTest.groovy` (GROOVY) | Magnitude: 48.76 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 106, core_var_decl: 71, design_snake_case: 42
- `testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/nativeplatform/SwiftBuildPerformanceTest.groovy` (GROOVY) | Magnitude: 22.02 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 20, test: 8, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/maven/MavenPublishS3IntegrationTest.groovy` (GROOVY) | Magnitude: 19.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 27, test: 20, import: 11
- `testing/smoke-test/src/smokeTest/resources/org/gradle/play/integtest/fixtures/external/basicplayapp/app/controllers/Application.scala.old` (SCALA) | Magnitude: 0.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 7, ssr_boundaries: 6, structural_boundaries: 5, func_start: 2
- `platforms/core-execution/build-cache/src/test/groovy/org/gradle/caching/internal/controller/service/StoreTargetTest.groovy` (GROOVY) | Magnitude: 11.18 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 15, test: 9, core_var_decl: 6
- `subprojects/core/src/test/groovy/org/gradle/cache/internal/AbstractCrossBuildInMemoryCacheTest.groovy` (GROOVY) | Magnitude: 12.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 36, core_var_decl: 24, design_snake_case: 23
- `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanTest.groovy` (GROOVY) | Magnitude: 480.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 879, core_var_decl: 257, concurrency: 232, design_snake_case: 224

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/DefaultCapabilitiesConflictHandlerTest.groovy` (GROOVY) | Magnitude: 18.92 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 28, core_var_decl: 18, import: 17
- `build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/nullaway/NullawayStatusService.kt` (KOTLIN) | Magnitude: 26.7 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 15, branch: 8, debug_prints: 8
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformIsolationIntegrationTest.groovy` (GROOVY) | Magnitude: 32.42 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 22, io: 19, test: 16
- `platforms/core-configuration/kotlin-dsl-tooling-builders/src/test/kotlin/org/gradle/kotlin/dsl/tooling/builders/EditorReportsBuilderTest.kt` (KOTLIN) | Magnitude: 10.72 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 69, test: 24, structural_boundaries: 16, import: 9
- `platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/EmptyBlocksTest.kt` (KOTLIN) | Magnitude: 13.68 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 22, core_var_decl: 14, design_snake_case: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/VariantAttributesRulesIntegrationTest.groovy` (GROOVY) | Magnitude: 205.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 293, args: 54, duplicate_logic: 23, test: 22
- `platforms/native/language-native/src/integTest/groovy/org/gradle/language/fixtures/app/DuplicateAssemblerBaseNamesTestApp.groovy` (GROOVY) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, args: 4, func_start: 4
- `platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/AbstractServiceRegistry.java` (JAVA) | Magnitude: 1.18 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, class_start: 1
- `platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/cpp/CppUnitTestComponentWithoutComponentIntegrationTest.groovy` (GROOVY) | Magnitude: 4.44 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, args: 3, func_start: 3
- `build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/ide/ExtractAndroidStudioTask.kt` (KOTLIN) | Magnitude: 20.12 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 22, import: 15, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/serializer/LogEventSerializerTest.groovy` (GROOVY) | Magnitude: 8.76 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 21, safety_bypasses: 11, core_var_decl: 10
- `platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/TransformingClassLoader.java` (JAVA) | Magnitude: 49.98 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 28, safety_bypasses: 16, import: 11
- `testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/timeout/IntegrationTestTimeoutInterceptor.groovy` (GROOVY) | Magnitude: 0.01 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 15, safety_bypasses: 9, import: 9
- `platforms/jvm/jvm-services/src/test/groovy/org/gradle/jvm/toolchain/internal/MavenToolchainsInstallationSupplierTest.groovy` (GROOVY) | Magnitude: 75.26 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 209, structural_boundaries: 70, test: 48, core_var_decl: 44
- `platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/components/internal/RendererUtils.java` (JAVA) | Magnitude: 23.72 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, core_var_decl: 7, safety_bypasses: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/ModuleForcingResolveRuleSpec.groovy` (GROOVY) | Magnitude: 12.24 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 16, test: 10, import: 7
- `platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/InstrumentedExecutionAccessListener.kt` (KOTLIN) | Magnitude: 4.38 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, encapsulation: 6, import: 4, indent_spaces: 4
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/TransformLoggingIntegrationTest.groovy` (GROOVY) | Magnitude: 24.96 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 60, test: 17, structural_boundaries: 16, core_var_decl: 9
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/catalog/ProjectAccessorsSourceGenerator.java` (JAVA) | Magnitude: 11.5 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, func_start: 4, api: 4
- `build-logic/buildquality/src/main/kotlin/gradlebuild.arch-test.gradle.kts` (KOTLIN) | Magnitude: 10.86 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 5, state_mutation: 5, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/TestTaskJavaVersionIntegrationTest.groovy` (GROOVY) | Magnitude: 21.36 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 19, test: 17, args: 9
- `platforms/software/build-init/src/testFixtures/groovy/org/gradle/buildinit/plugins/fixtures/WrapperTestFixture.groovy` (GROOVY) | Magnitude: 0.01 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, io: 9, test: 9, api: 6
- `subprojects/core/src/main/java/org/gradle/initialization/DefaultClassLoaderRegistry.java` (JAVA) | Magnitude: 38.26 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 22, reflection_metaprogramming: 14, args: 10
- `testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/concurrent/BlockTarget.groovy` (GROOVY) | Magnitude: 0.0 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, args: 2, func_start: 2
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheClassLoaderCachingIntegrationTest.groovy` (GROOVY) | Magnitude: 18.52 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 77, test: 14, structural_boundaries: 9, io: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/Logger.kt` (KOTLIN) | Magnitude: 14.12 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, encapsulation: 3, api: 1
- `platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/KotlinScriptHashing.kt` (KOTLIN) | Magnitude: 4.28 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 2, func_start: 2
- `testing/performance/src/templates/cpp-source/lib.h` (C) | Magnitude: 13.12 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: macros: 2
- `build-logic/performance-testing/src/main/groovy/gradlebuild/performance/generator/MavenScope.groovy` (GROOVY) | Magnitude: 2.24 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, args: 1, func_start: 1
- `platforms/ide/ide-native/src/testFixtures/groovy/org/gradle/ide/xcode/fixtures/SchemeFile.groovy` (GROOVY) | Magnitude: 0.01 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, state_mutation: 3, immutability_locks: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/model/eclipse/EclipseWorkspaceProject.java` (JAVA) | Magnitude: 7.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 4, doc: 4, structural_boundaries: 3, args: 3
- `platforms/core-runtime/daemon-messaging/src/main/java/org/gradle/launcher/daemon/protocol/ReportStatus.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `platforms/core-runtime/daemon-messaging/src/main/java/org/gradle/launcher/daemon/protocol/Stop.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `platforms/core-runtime/daemon-messaging/src/main/java/org/gradle/launcher/daemon/protocol/StopWhenIdle.java` (JAVA) | Magnitude: 4.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `platforms/core-configuration/declarative-dsl-tooling-models/src/main/kotlin/org/gradle/declarative/dsl/schema/DataProperty.kt` (KOTLIN) | Magnitude: 15.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 14, class_start: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ClassMembersForSchema.kt` (KOTLIN) | Magnitude: 198.44 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 238, structural_boundaries: 79, branch: 60, core_var_decl: 42
- `platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/modelreader/impl/TypeUtils.java` (JAVA) | Magnitude: 64.28 | Delta: **0.249** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 43, branch: 21, import: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `subprojects/core/src/main/java/org/gradle/internal/classpath/intercept/CallInterceptorRegistry.java` (JAVA) | Magnitude: 40.34 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 34, args: 11, core_var_decl: 10
- `subprojects/core/src/integTest/groovy/org/gradle/api/internal/DynamicModulesClassPathProviderTest.groovy` (GROOVY) | Magnitude: 8.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 19, import: 11, test: 10
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/ExternalResourceResolverDescriptorParseContext.java` (JAVA) | Magnitude: 26.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 41, import: 28, core_var_decl: 10
- `platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/Preconditions.java` (JAVA) | Magnitude: 8.44 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, safety_bypasses: 4, args: 3
- `testing/internal-integ-testing/src/main/groovy/org/gradle/test/fixtures/maven/MavenJavaPlatformModule.groovy` (GROOVY) | Magnitude: 0.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 49, safety: 12, test: 10, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `platforms/ide/ide/src/main/java/org/gradle/plugins/ide/idea/model/Path.java` (JAVA) | Magnitude: 27.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 11, api: 9, args: 8
- `subprojects/core/src/main/java/org/gradle/api/internal/tasks/options/MethodSignature.java` (JAVA) | Magnitude: 20.58 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 13, args: 6, func_start: 6
- `subprojects/core/src/main/resources/org/gradle/reporting/base-style.css` (CSS) | Magnitude: 0.89 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 78, class_start: 36, safety_bypasses: 4, globals: 2
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dependencies/DefaultPluginDependency.java` (JAVA) | Magnitude: 25.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 14, api: 7, args: 6
- `platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/JavaCompileExecutableUtils.java` (JAVA) | Magnitude: 10.44 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, import: 7, safety_bypasses: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/EstablishBuildEnvironment.java` (JAVA) | Magnitude: 23.52 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 24, import: 13, core_var_decl: 6
- `platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/conversion/AnalysisAndConversionStepRunner.kt` (KOTLIN) | Magnitude: 23.9 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 28, encapsulation: 18, import: 17
- `testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/logging/comparison/DiffUtils.java` (JAVA) | Magnitude: 0.2 | Delta: **0.166** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 51, core_var_decl: 41, structural_boundaries: 27
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/DependencyGraphPathResolver.java` (JAVA) | Magnitude: 65.24 | Delta: **0.226** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 24, branch: 14, core_var_decl: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperGenerationIntegrationTest.groovy` -> Churn: **70.87%** | Cog Load: 73.046% | Debt: 99.9279%
- `platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/TaskbarProgressResetFunctionalTest.groovy` -> Churn: **58.86%** | Cog Load: 0.0% | Debt: 97.0688%
- `platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperHttpIntegrationTest.groovy` -> Churn: **58.86%** | Cog Load: 7.9318% | Debt: 96.3105%
- `platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/dependencyConfigurationSchema.kt` -> Churn: **58.86%** | Cog Load: 0.0% | Debt: 99.593%
- `subprojects/core/src/main/java/org/gradle/initialization/DefaultSettingsPreparer.java` -> Churn: **56.41%** | Cog Load: 16.9162% | Debt: 65.6752%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/DefaultServiceRegistry.java` -> **Alex Semin** (100.0% isolated ownership) | Magnitude: 826.4
- `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java` -> **Sterling Greene** (100.0% isolated ownership) | Magnitude: 799.68
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/DefaultConfiguration.java` -> **Gary Hale** (100.0% isolated ownership) | Magnitude: 781.44
- `subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultProject.java` -> **Gary Hale** (100.0% isolated ownership) | Magnitude: 704.3
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/NodeState.java` -> **Justin Van Dort** (100.0% isolated ownership) | Magnitude: 659.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/file/TestFile.java` -> **Severity: 901.802** (Blast Radius: 11.375 * Doc Risk: 79.2793%)
- `testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractIntegrationSpec.groovy` -> **Severity: 648.749** (Blast Radius: 7.355 * Doc Risk: 88.2051%)
- `platforms/core-execution/hashing/src/main/java/org/gradle/internal/hash/HashCode.java` -> **Severity: 491.786** (Blast Radius: 5.508 * Doc Risk: 89.2857%)
- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/api/GradleException.java` -> **Severity: 361.267** (Blast Radius: 5.419 * Doc Risk: 66.6667%)
- `platforms/core-execution/snapshots/src/main/java/org/gradle/internal/snapshot/ChildMap.java` -> **Severity: 236.8** (Blast Radius: 2.368 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1221 literal sites + 37 sites through wrappers = 1258
- **`memory_alloc`:** 22 literal sites + 8 sites through wrappers = 30
- **`panics_and_aborts`:** 8087 literal sites + 666 sites through wrappers = 8753

- `shouldNotBeUsed` (function, panics_and_aborts, primitive): 30 call sites in 1 files -- `platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ProblemReportingCrossProjectModelAccess.kt`
- `gradleStep` (function, panics_and_aborts, primitive): 25 call sites in 1 files -- `.teamcity/src/test/kotlin/PromotionProjectTests.kt`
- `generateCodeFrom` (function, panics_and_aborts, primitive): 18 call sites in 1 files -- `platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/MutatedDocumentTextGeneratorTest.kt`
- `givenKotlinScriptInBuildSrcContains` (function, panics_and_aborts, primitive): 18 call sites in 2 files -- `platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/AbstractCompileAvoidanceIntegrationTest.kt`
- `convertBlockToDocument` (function, panics_and_aborts, primitive): 13 call sites in 7 files -- `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/fromLanguageTree/LanguageTreeToDom.kt`
- `createFromPaths` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/DefaultIgnoredConfigurationInputsTest.kt`
- `setupModelFor` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `.teamcity/src/test/kotlin/PromotionProjectTests.kt`
- `throwVersionCatalogProblemException` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/catalog/DefaultVersionCatalogBuilder.java`
- `failureOnUnexpectedOutput` (function, panics_and_aborts, primitive): 12 call sites in 2 files -- `testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/OutputScrapingExecutionResult.java`
- `givenKotlinClassInBuildSrcContains` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/AbstractCompileAvoidanceIntegrationTest.kt`
- `failWithUnsupportedMethod` (function, panics_and_aborts, primitive): 10 call sites in 1 files -- `subprojects/core/src/main/java/org/gradle/api/internal/tasks/TaskInputsDeprecationSupport.java`
- `givenPrecompiledKotlinScript` (function, panics_and_aborts, primitive): 10 call sites in 3 files -- `platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/AbstractKotlinIntegrationTest.kt`
*(+293 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 331245 call pairs -- scoped 35.2%, unique 1.9%, ambiguous 40.2%, external 22.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| groovy | 165170 | 33.3% | 1.8% | 37.9% | 26.9% |
| java | 137633 | 37.9% | 2.0% | 45.2% | 14.9% |
| kotlin | 27667 | 32.9% | 2.6% | 28.9% | 35.6% |
| cpp | 449 | 32.5% | 0.2% | 20.3% | 47.0% |
| javascript | 232 | 22.4% | 0.0% | 0.4% | 77.2% |
| scala | 60 | 18.3% | 0.0% | 58.3% | 23.3% |
| shell | 19 | 26.3% | 0.0% | 0.0% | 73.7% |
| c | 9 | 0.0% | 0.0% | 0.0% | 100.0% |
| swift | 6 | 0.0% | 33.3% | 33.3% | 33.3% |

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
