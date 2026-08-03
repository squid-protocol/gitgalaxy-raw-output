# ARCHITECTURAL_BRIEF: gradle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/gradle` |
| **Timestamp** | `2026-08-03T20:58:26.200315+00:00` |
| **Scan Duration** | `60.85s` |
| **Git Branch** | `master` |
| **Git Commit** | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` |
| **Git Remote** | `https://github.com/gradle/gradle` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 18604 malicious artifacts.

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
| Total Artifacts | 26690 |
| Analyzed Artifacts (Scanned) | 19038 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7652 |
| Total LOC | 1431299 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.3% |
| Dominant Lang | GROOVY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1362 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 891 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 10705 | 512085 | 56.2% |
| GROOVY | 6422 | 794738 | 33.7% |
| KOTLIN | 1382 | 118288 | 7.3% |
| PLAINTEXT | 233 | 18 | 1.2% |
| XML | 138 | 0 | 0.7% |
| MARKDOWN | 39 | 0 | 0.2% |
| CPP | 31 | 2407 | 0.2% |
| SCALA | 29 | 349 | 0.2% |
| CSS | 10 | 614 | 0.1% |
| JAVASCRIPT | 9 | 803 | 0.0% |
| PHP | 9 | 389 | 0.0% |
| HTML | 8 | 418 | 0.0% |
| C | 8 | 65 | 0.0% |
| SWIFT | 6 | 42 | 0.0% |
| JSON | 3 | 716 | 0.0% |
| YAML | 2 | 64 | 0.0% |
| SHELL | 1 | 60 | 0.0% |
| BATCH | 1 | 63 | 0.0% |
| CSV | 1 | 179 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.367`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 9932 | 52.2% |
| file_cluster_13 | 7056 | 37.1% |
| file_cluster_16 | 1066 | 5.6% |
| file_cluster_0 | 427 | 2.2% |
| file_cluster_4 | 233 | 1.2% |
| file_cluster_17 | 29 | 0.2% |
| Unknown | 19 | 0.1% |
| file_cluster_9 | 8 | 0.0% |
| file_cluster_2 | 6 | 0.0% |
| file_cluster_11 | 4 | 0.0% |
| file_cluster_7 | 3 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 254 | 1.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7652*

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.4 | 8.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 22.6 | 3.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.3 | 1.2 | 0.0 |
| API Exposure | 0.0 | 16.2 | 2.9 | 2.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 48.2 | 34.3 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 44.5 | 16.5 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 32.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/AndroidProjectCachingSmokeTest.groovy` (Hits: 404)
- `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy` (Hits: 390)
- `testing/integ-test/src/integTest/groovy/org/gradle/integtests/SyncTaskIntegrationTest.groovy` (Hits: 214)

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

- `def` (@ `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy`) -> Impact: **6674.4** | LOC: 1288
- `def` (@ `platforms/software/publish/src/test/groovy/org/gradle/api/publish/internal/metadata/GradleModuleMetadataWriterTest.groovy`) -> Impact: **4314.1** | LOC: 1083
- `def` (@ `platforms/software/ivy/src/integTest/groovy/org/gradle/api/publish/ivy/IvyPublishJavaIntegTest.groovy`) -> Impact: **3840.4** | LOC: 508
- `def` (@ `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy`) -> Impact: **3825.8** | LOC: 1344
- `def` (@ `platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/java/compile/AbstractJavaCompileAvoidanceIntegrationSpec.groovy`) -> Impact: **2366.8** | LOC: 305
- `def` (@ `subprojects/core/src/integTest/groovy/org/gradle/internal/operations/notify/BuildOperationNotificationIntegrationTest.groovy`) -> Impact: **2269.0** | LOC: 126
- `def` (@ `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientKotlinDslScriptsModelBuilderCrossVersionSpec.groovy`) -> Impact: **1841.4** | LOC: 603
- `def` (@ `testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/BomSupportPluginsSmokeTest.groovy`) -> Impact: **1826.5** | LOC: 157
- `def` (@ `subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildBuildSrcBuildOperationsIntegrationTest.groovy`) -> Impact: **1604.8** | LOC: 96
- `setup` (@ `subprojects/core/src/integTest/groovy/org/gradle/execution/taskgraph/ParallelTaskExecutionIntegrationTest.groovy`) -> Impact: **1501.5** | LOC: 568

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `addToAntBuilder` (@ `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AntFileCollectionMatchingTaskBuilder.java`) -> **O(2^N) [Recursive]**
- `visit` (@ `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/ReproducibleDirectoryWalker.java`) -> **O(2^N) [Recursive]**
- `getSourceTrees` (@ `platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/DefaultSourceDirectorySet.java`) -> **O(2^N) [Recursive]**
- `execute` (@ `platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/DuplicateHandlingCopyActionDecorator.java`) -> **O(2^N) [Recursive]**
- `add` (@ `platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/FilterChain.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Transforms the given InputStream. The original InputStream will be closed by the returned InputStream.
- `execute` (@ `platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/NormalizingCopyActionDecorator.java`) -> **O(2^N) [Recursive]**
- `visitDependencies` (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/DefaultTaskDependency.java`) -> **O(2^N) [Recursive]**
- `find` (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/isolated/IsolationScheme.java`) -> **O(2^N) [Recursive]**
- `setProperty` (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/metaobject/BeanDynamicObject.java`) -> **O(2^N) [Recursive]**
- `getProperty` (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/metaobject/BeanDynamicObject.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `def` (@ `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy`) -> DB Complexity: **967**
- `def` (@ `platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileIntegrationTest.groovy`) -> DB Complexity: **300**
- `writeCustomTestSourceEmittingTestEngineS` (@ `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/AbstractResourceBasedTestingCrossVersionSpec.groovy`) -> DB Complexity: **285**
- `def` (@ `platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/checkstyle/CheckstylePluginVersionIntegrationTest.groovy`) -> DB Complexity: **217**
- `canUseDefaultJvmArgsToPassMultipleOption` (@ `platforms/jvm/plugins-application/src/integTest/groovy/org/gradle/integtests/ApplicationIntegrationSpec.groovy`) -> DB Complexity: **214**
- `def` (@ `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientKotlinDslScriptsModelBuilderCrossVersionSpec.groovy`) -> DB Complexity: **191**
- `def` (@ `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy`) -> DB Complexity: **164**
- `def` (@ `testing/internal-performance-testing/src/test/groovy/org/gradle/performance/mutator/ClearArtifactTransformCacheWithoutInstrumentedJarsMutatorTest.groovy`) -> DB Complexity: **159**
  * *Intent:* * Copyright 2023 the original author or authors. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file excep...
- `def` (@ `testing/internal-performance-testing/src/test/groovy/org/gradle/performance/mutator/ClearArtifactTransformCacheWithoutInstrumentedJarsMutatorTest.groovy`) -> DB Complexity: **156**
- `def` (@ `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/undeclared/MethodReferenceInstrumentationIntegrationTest.groovy`) -> DB Complexity: **155**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve` | 65 | 53129.54 | 29.18% | 82.6% |
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform` | 23 | 41053.84 | 42.29% | 77.55% |
| `subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite` | 47 | 39263.68 | 52.59% | 85.62% |
| `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl` | 80 | 38761.52 | 42.3% | 68.55% |
| `subprojects/core/src/integTest/groovy/org/gradle/api/tasks` | 80 | 38447.16 | 58.12% | 90.41% |
| `platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven` | 38 | 31504.68 | 31.68% | 86.5% |
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven` | 32 | 22216.94 | 33.29% | 96.62% |
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes` | 18 | 20661.9 | 34.83% | 92.25% |
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy` | 26 | 19471.12 | 38.47% | 92.54% |
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules` | 20 | 19160.78 | 28.73% | 80.09% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `build-logic-commons/code-quality-rules/src/main/java/gradlebuild/codenarc/rules/IntegrationTestFixturesRule.java` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForEachProjectInParallel.java` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForSameProjectInParallel.java` -> **100.0%** Exposure
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AbstractFilePermissions.java` -> **100.0%** Exposure
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AbstractOpaqueFileCollection.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/DirectoryWalker.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/MapEntryCollector.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/ValueCollector.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/DelegatingBaseExecSpec.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/DelegatingExecSpec.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/PropertySpec.groovy` -> **0** Orphaned Functions | **135** Duplicates
- `platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/BuildScriptBuilder.java` -> **0** Orphaned Functions | **125** Duplicates
- `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy` -> **11** Orphaned Functions | **96** Duplicates
- `platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/MapPropertySpec.groovy` -> **6** Orphaned Functions | **98** Duplicates
- `platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/CollectionPropertySpec.groovy` -> **5** Orphaned Functions | **92** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`.teamcity/src/main/kotlin/common/CommonExtensions.kt`** -> AI Confidence: **99.48%**
2. **`.teamcity/src/main/kotlin/configurations/DocsTest.kt`** -> AI Confidence: **99.48%**
3. **`.teamcity/src/main/kotlin/configurations/FlakyTestQuarantine.kt`** -> AI Confidence: **99.48%**
4. **`.teamcity/src/main/kotlin/configurations/FunctionalTest.kt`** -> AI Confidence: **99.48%**
5. **`.teamcity/src/main/kotlin/configurations/GitHubMergeQueueCheckPass.kt`** -> AI Confidence: **99.48%**
6. **`.teamcity/src/main/kotlin/configurations/GradleBuildConfigurationDefaults.kt`** -> AI Confidence: **99.48%**
7. **`.teamcity/src/main/kotlin/configurations/Gradleception.kt`** -> AI Confidence: **99.48%**
8. **`.teamcity/src/main/kotlin/configurations/LightweightChecks.kt`** -> AI Confidence: **99.48%**
9. **`.teamcity/src/main/kotlin/configurations/PerformanceTest.kt`** -> AI Confidence: **99.48%**
10. **`.teamcity/src/main/kotlin/configurations/PerformanceTestsPass.kt`** -> AI Confidence: **99.48%**
11. **`.teamcity/src/main/kotlin/configurations/SmokeIdeTests.kt`** -> AI Confidence: **99.48%**
12. **`.teamcity/src/main/kotlin/configurations/SmokeTests.kt`** -> AI Confidence: **99.48%**
13. **`.teamcity/src/main/kotlin/configurations/StageTriggers.kt`** -> AI Confidence: **99.48%**
14. **`.teamcity/src/main/kotlin/configurations/TestPerformanceTest.kt`** -> AI Confidence: **99.48%**
15. **`.teamcity/src/main/kotlin/model/CIBuildModel.kt`** -> AI Confidence: **99.48%**
16. **`.teamcity/src/main/kotlin/model/FunctionalTestBucketGenerator.kt`** -> AI Confidence: **99.48%**
17. **`.teamcity/src/main/kotlin/model/FunctionalTestBucketProvider.kt`** -> AI Confidence: **99.48%**
18. **`.teamcity/src/main/kotlin/model/PerformanceTestBucketProvider.kt`** -> AI Confidence: **99.48%**
19. **`.teamcity/src/main/kotlin/projects/CheckProject.kt`** -> AI Confidence: **99.48%**
20. **`.teamcity/src/main/kotlin/projects/GradleBuildToolRootProject.kt`** -> AI Confidence: **99.48%**
21. **`.teamcity/src/main/kotlin/projects/StageProject.kt`** -> AI Confidence: **99.48%**
22. **`.teamcity/src/main/kotlin/promotion/PromotionProject.kt`** -> AI Confidence: **99.48%**
23. **`.teamcity/src/main/kotlin/promotion/SanityCheck.kt`** -> AI Confidence: **99.48%**
24. **`.teamcity/src/main/kotlin/util/AdHocPerformanceScenario.kt`** -> AI Confidence: **99.48%**
25. **`.teamcity/src/main/kotlin/util/RerunFlakyTest.kt`** -> AI Confidence: **99.48%**
26. **`.teamcity/src/main/kotlin/util/UpdateWrapper.kt`** -> AI Confidence: **99.48%**
27. **`.teamcity/src/test/kotlin/ApplyDefaultConfigurationTest.kt`** -> AI Confidence: **99.48%**
28. **`.teamcity/src/test/kotlin/BuildTypeTest.kt`** -> AI Confidence: **99.48%**
29. **`.teamcity/src/test/kotlin/CIConfigIntegrationTests.kt`** -> AI Confidence: **99.48%**
30. **`.teamcity/src/test/kotlin/PerformanceTestBuildTypeTest.kt`** -> AI Confidence: **99.48%**
31. **`.teamcity/src/test/kotlin/PromotionProjectTests.kt`** -> AI Confidence: **99.48%**
32. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/BuildEnvironment.kt`** -> AI Confidence: **99.48%**
33. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/BuildParams.kt`** -> AI Confidence: **99.48%**
34. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/classanalysis/AnalyzeAndShade.kt`** -> AI Confidence: **99.48%**
35. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/tasks/PackageListGenerator.kt`** -> AI Confidence: **99.48%**
36. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/transforms/Minify.kt`** -> AI Confidence: **99.48%**
37. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/util/KotlinSourceParser.kt`** -> AI Confidence: **99.48%**
38. **`build-logic-commons/basics/src/test/kotlin/gradlebuild/basics/tasks/PackageListGeneratorIntegrationTest.kt`** -> AI Confidence: **99.48%**
39. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.cache-miss-monitor.gradle.kts`** -> AI Confidence: **99.48%**
40. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.code-quality.gradle.kts`** -> AI Confidence: **99.48%**
41. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.collect-failed-tasks.gradle.kts`** -> AI Confidence: **99.48%**
42. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/AbstractBuildScanInfoCollectingService.kt`** -> AI Confidence: **99.48%**
43. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/nullaway/NullawayStatusTask.kt`** -> AI Confidence: **99.48%**
44. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/testcleanup/TestFilesCleanupService.kt`** -> AI Confidence: **99.48%**
45. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild.module-identity.gradle.kts`** -> AI Confidence: **99.48%**
46. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild/identity/extension/GradleModuleExtension.kt`** -> AI Confidence: **99.48%**
47. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild/identity/provider/BuildTimestampValueSource.kt`** -> AI Confidence: **99.48%**
48. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild/identity/tasks/BuildReceipt.kt`** -> AI Confidence: **99.48%**
49. **`build-logic-settings/architecture-docs/src/main/kotlin/gradlebuild/GeneratePackageInfoDataTask.kt`** -> AI Confidence: **99.48%**
50. **`build-logic-settings/architecture-docs/src/main/kotlin/gradlebuild/GeneratePlatformsDataTask.kt`** -> AI Confidence: **99.48%**
51. **`build-logic-settings/architecture-docs/src/main/kotlin/gradlebuild/GeneratorTask.kt`** -> AI Confidence: **99.48%**
52. **`build-logic-settings/build-environment/src/main/kotlin/gradlebuild/basics/BuildEnvironmentService.kt`** -> AI Confidence: **99.48%**
53. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/AbstractAcceptedApiChangesMaintenanceTask.kt`** -> AI Confidence: **99.48%**
54. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/BinaryCompatibilityRepository.kt`** -> AI Confidence: **99.48%**
55. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/JavassistExtensions.kt`** -> AI Confidence: **99.48%**
56. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/metadata/HasKotlinFlagsMetadataQuery.kt`** -> AI Confidence: **99.48%**
57. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/metadata/KotlinMetadataQueries.kt`** -> AI Confidence: **99.48%**
58. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/sources/JavaSourceQueries.kt`** -> AI Confidence: **99.48%**
59. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/sources/KotlinSourceQueries.kt`** -> AI Confidence: **99.48%**
60. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/sources/SourcesRepository.kt`** -> AI Confidence: **99.48%**
61. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/AbstractBinaryCompatibilityTest.kt`** -> AI Confidence: **99.48%**
62. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild.update-versions.gradle.kts`** -> AI Confidence: **99.48%**
63. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/runtimes/CheckTargetRuntimes.kt`** -> AI Confidence: **99.48%**
64. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/AbstractCheckOrUpdateContributorsInReleaseNotes.kt`** -> AI Confidence: **99.48%**
65. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/AbstractVersionsUpdateTask.kt`** -> AI Confidence: **99.48%**
66. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/PreparePatchRelease.kt`** -> AI Confidence: **99.48%**
67. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/SubprojectsInfo.kt`** -> AI Confidence: **99.48%**
68. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateAgpVersions.kt`** -> AI Confidence: **99.48%**
69. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateFixedIssuesInReleaseNotes.kt`** -> AI Confidence: **99.48%**
70. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateInitPluginTemplateVersionFile.kt`** -> AI Confidence: **99.48%**
71. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateKotlinVersions.kt`** -> AI Confidence: **99.48%**
72. **`build-logic/buildquality/src/main/kotlin/gradlebuild.configure-ci-artifacts.gradle.kts`** -> AI Confidence: **99.48%**
73. **`build-logic/buildquality/src/main/kotlin/gradlebuild/codenarc/rules/IntegrationTestFixturesRule.kt`** -> AI Confidence: **99.48%**
74. **`build-logic/buildquality/src/main/kotlin/gradlebuild/incubation/action/IncubatingApiReportWorkAction.kt`** -> AI Confidence: **99.48%**
75. **`build-logic/buildquality/src/test/kotlin/gradlebuild/testcleanup/TestFilesCleanupServiceTest.kt`** -> AI Confidence: **99.48%**
76. **`build-logic/cleanup/src/main/kotlin/gradlebuild/cleanup/Cleanup.kt`** -> AI Confidence: **99.48%**
77. **`build-logic/cleanup/src/main/kotlin/gradlebuild/cleanup/services/CachesCleaner.kt`** -> AI Confidence: **99.48%**
78. **`build-logic/cleanup/src/main/kotlin/gradlebuild/cleanup/services/DaemonTracker.kt`** -> AI Confidence: **99.48%**
79. **`build-logic/cleanup/src/main/kotlin/gradlebuild/testing/services/BuildBucketProvider.kt`** -> AI Confidence: **99.48%**
80. **`build-logic/integration-testing/src/main/kotlin/gradlebuild.cross-version-tests.gradle.kts`** -> AI Confidence: **99.48%**
81. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/action/AnnotationGeneratorWorkAction.kt`** -> AI Confidence: **99.48%**
82. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/androidhomewarmup/AndroidHomeWarmupTask.kt`** -> AI Confidence: **99.48%**
83. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/ide/AndroidStudioProvisioningPlugin.kt`** -> AI Confidence: **99.48%**
84. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/ide/AndroidStudioSystemProperties.kt`** -> AI Confidence: **99.48%**
85. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/ide/ExtractAndroidStudioTask.kt`** -> AI Confidence: **99.48%**
86. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/shared-configuration.kt`** -> AI Confidence: **99.48%**
87. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/tasks/DistributionTest.kt`** -> AI Confidence: **99.48%**
88. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/tasks/GenerateAutoTestedSamplesTestTask.kt`** -> AI Confidence: **99.48%**
89. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/tasks/GenerateLanguageAnnotations.kt`** -> AI Confidence: **99.48%**
90. **`build-logic/jvm/src/main/kotlin/gradlebuild.unittest-and-compile.gradle.kts`** -> AI Confidence: **99.48%**
91. **`build-logic/jvm/src/main/kotlin/gradlebuild/jvm/JvmCompilation.kt`** -> AI Confidence: **99.48%**
92. **`build-logic/jvm/src/main/kotlin/gradlebuild/jvm/argumentproviders/CiEnvironmentProvider.kt`** -> AI Confidence: **99.48%**
93. **`build-logic/jvm/src/main/kotlin/gradlebuild/startscript/tasks/GradleStartScriptGenerator.kt`** -> AI Confidence: **99.48%**
94. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/codegen/ApiTypeProvider.kt`** -> AI Confidence: **99.48%**
95. **`build-logic/kotlin-dsl/src/main/kotlin/gradlebuild/kotlindsl/generator/codegen/FunctionSinceRepository.kt`** -> AI Confidence: **99.48%**
96. **`build-logic/kotlin-dsl/src/main/kotlin/gradlebuild/kotlindsl/generator/tasks/GenerateKotlinDependencyExtensions.kt`** -> AI Confidence: **99.48%**
97. **`build-logic/kotlin-dsl/src/main/kotlin/gradlebuild/kotlindsl/generator/tasks/GenerateKotlinExtensionsForGradleApi.kt`** -> AI Confidence: **99.48%**
98. **`build-logic/lifecycle/src/main/kotlin/gradlebuild.teamcity-import-test-data.gradle.kts`** -> AI Confidence: **99.48%**
99. **`build-logic/packaging/src/main/kotlin/gradlebuild.distributions.gradle.kts`** -> AI Confidence: **99.48%**
100. **`build-logic/packaging/src/main/kotlin/gradlebuild.shaded-jar.gradle.kts`** -> AI Confidence: **99.48%**
101. **`build-logic/packaging/src/main/kotlin/gradlebuild/instrumentation/extensions/InstrumentationMetadataExtension.kt`** -> AI Confidence: **99.48%**
102. **`build-logic/packaging/src/main/kotlin/gradlebuild/instrumentation/tasks/InstrumentedSuperTypesMergeTask.kt`** -> AI Confidence: **99.48%**
103. **`build-logic/packaging/src/main/kotlin/gradlebuild/instrumentation/tasks/UpgradedPropertiesMergeTask.kt`** -> AI Confidence: **99.48%**
104. **`build-logic/packaging/src/main/kotlin/gradlebuild/instrumentation/transforms/InstrumentationMetadataTransform.kt`** -> AI Confidence: **99.48%**
105. **`build-logic/packaging/src/main/kotlin/gradlebuild/nomoduleannotation/NoModuleAnnotation.kt`** -> AI Confidence: **99.48%**
106. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/GradleDistributionSpecs.kt`** -> AI Confidence: **99.48%**
107. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/ExtractJavaAbi.kt`** -> AI Confidence: **99.48%**
108. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/GenerateClasspathModuleProperties.kt`** -> AI Confidence: **99.48%**
109. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/GenerateLicenseFile.kt`** -> AI Confidence: **99.48%**
110. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/PathPrefixLister.kt`** -> AI Confidence: **99.48%**
111. **`build-logic/packaging/src/main/kotlin/gradlebuild/shade/tasks/ShadedJar.kt`** -> AI Confidence: **99.48%**
112. **`build-logic/packaging/src/main/kotlin/gradlebuild/shade/transforms/ShadeClasses.kt`** -> AI Confidence: **99.48%**
113. **`build-logic/packaging/src/test/kotlin/gradlebuild/packaging/GradleDistributionInstallTest.kt`** -> AI Confidence: **99.48%**
114. **`build-logic/performance-testing/src/main/kotlin/gradlebuild/performance/PerformanceTestPlugin.kt`** -> AI Confidence: **99.48%**
115. **`build-logic/performance-testing/src/main/kotlin/gradlebuild/performance/tasks/BuildCommitDistribution.kt`** -> AI Confidence: **99.48%**
116. **`build-logic/performance-testing/src/main/kotlin/gradlebuild/performance/tasks/DetermineBaselines.kt`** -> AI Confidence: **99.48%**
117. **`build-logic/performance-testing/src/main/kotlin/gradlebuild/performance/tasks/PerformanceTestReport.kt`** -> AI Confidence: **99.48%**
118. **`build-logic/performance-testing/src/test/kotlin/gradlebuild/performance/tasks/DetermineBaselinesTest.kt`** -> AI Confidence: **99.48%**
119. **`build-logic/profiling/src/main/kotlin/gradlebuild.buildscan.gradle.kts`** -> AI Confidence: **99.48%**
120. **`build-logic/profiling/src/main/kotlin/gradlebuild/jmh/tasks/JmhHTMLReport.kt`** -> AI Confidence: **99.48%**
121. **`platforms/core-configuration/bean-serialization-services/src/main/kotlin/org/gradle/internal/serialize/beans/services/BeanConstructors.kt`** -> AI Confidence: **99.48%**
122. **`platforms/core-configuration/bean-serialization-services/src/main/kotlin/org/gradle/internal/serialize/beans/services/BeanPropertyReader.kt`** -> AI Confidence: **99.48%**
123. **`platforms/core-configuration/bean-serialization-services/src/main/kotlin/org/gradle/internal/serialize/beans/services/BeanPropertyWriter.kt`** -> AI Confidence: **99.48%**
124. **`platforms/core-configuration/bean-serialization-services/src/main/kotlin/org/gradle/internal/serialize/beans/services/BeanSchema.kt`** -> AI Confidence: **99.48%**
125. **`platforms/core-configuration/configuration-cache-base/src/main/kotlin/org/gradle/internal/cc/base/services/ProjectRefResolver.kt`** -> AI Confidence: **99.48%**
126. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/buildtree/control/BuildModelParametersProvider.kt`** -> AI Confidence: **99.48%**
127. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/BuildModelControllerServices.kt`** -> AI Confidence: **99.48%**
128. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/BuildTreeModelControllerServices.kt`** -> AI Confidence: **99.48%**
129. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareBuildToolingModelController.kt`** -> AI Confidence: **99.48%**
130. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareBuildTreeWorkController.kt`** -> AI Confidence: **99.48%**
131. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheBuildTreeLifecycleControllerFactory.kt`** -> AI Confidence: **99.48%**
132. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheClassLoaderScopeRegistryListener.kt`** -> AI Confidence: **99.48%**
133. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheKey.kt`** -> AI Confidence: **99.48%**
134. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheRepository.kt`** -> AI Confidence: **99.48%**
135. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheServices.kt`** -> AI Confidence: **99.48%**
136. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheState.kt`** -> AI Confidence: **99.48%**
137. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CrossProjectConfigurationReportingGradle.kt`** -> AI Confidence: **99.48%**
138. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CrossProjectConfigurationReportingTaskExecutionGraph.kt`** -> AI Confidence: **99.48%**
139. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CrossProjectModelAccessTrackingParentDynamicObject.kt`** -> AI Confidence: **99.48%**
140. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultBuildToolingModelControllerFactory.kt`** -> AI Confidence: **99.48%**
141. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCache.kt`** -> AI Confidence: **99.48%**
142. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCacheDegradationController.kt`** -> AI Confidence: **99.48%**
143. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCacheHost.kt`** -> AI Confidence: **99.48%**
144. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCacheIO.kt`** -> AI Confidence: **99.48%**
145. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultIgnoredConfigurationInputs.kt`** -> AI Confidence: **99.48%**
146. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DeprecatedFeaturesListener.kt`** -> AI Confidence: **99.48%**
147. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ProblemReportingCrossProjectModelAccess.kt`** -> AI Confidence: **99.48%**
148. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/RelevantProjectsRegistry.kt`** -> AI Confidence: **99.48%**
149. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/TrackingDynamicLookupRoutine.kt`** -> AI Confidence: **99.48%**
150. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/VintageBuildTreeLifecycleControllerFactory.kt`** -> AI Confidence: **99.48%**
151. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/VintageBuildTreeWorkController.kt`** -> AI Confidence: **99.48%**
152. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/barrier/BarrierAwareBuildTreeLifecycleControllerFactory.kt`** -> AI Confidence: **99.48%**
153. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/barrier/VintageConfigurationTimeActionRunner.kt`** -> AI Confidence: **99.48%**
154. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ClassLoaderScopesFingerprintController.kt`** -> AI Confidence: **99.48%**
155. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprint.kt`** -> AI Confidence: **99.48%**
156. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprintChecker.kt`** -> AI Confidence: **99.48%**
157. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprintController.kt`** -> AI Confidence: **99.48%**
158. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprintEventHandler.kt`** -> AI Confidence: **99.48%**
159. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprintWriter.kt`** -> AI Confidence: **99.48%**
160. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheInputFileChecker.kt`** -> AI Confidence: **99.48%**
161. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ScopedFingerprintWriter.kt`** -> AI Confidence: **99.48%**
162. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/AbstractInjectedClasspathInstrumentationStrategy.kt`** -> AI Confidence: **99.48%**
163. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/ConfigurationCacheProblemsListener.kt`** -> AI Confidence: **99.48%**
164. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/ConfigurationCacheStartParameter.kt`** -> AI Confidence: **99.48%**
165. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/metadata/ProjectMetadataController.kt`** -> AI Confidence: **99.48%**
166. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/models/BuildTreeModelSideEffectStore.kt`** -> AI Confidence: **99.48%**
167. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/models/IntermediateModelController.kt`** -> AI Confidence: **99.48%**
168. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/models/ProjectStateStore.kt`** -> AI Confidence: **99.48%**
169. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/problems/ConfigurationCacheProblems.kt`** -> AI Confidence: **99.48%**
170. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/problems/ConfigurationCacheProblemsSummary.kt`** -> AI Confidence: **99.48%**
171. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/promo/ConfigurationCachePromoHandler.kt`** -> AI Confidence: **99.48%**
172. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ClassLoaderScopes.kt`** -> AI Confidence: **99.48%**
173. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ClassPathEncodingExtensions.kt`** -> AI Confidence: **99.48%**
174. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/DefaultClassDecoder.kt`** -> AI Confidence: **99.48%**
175. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/DefaultClassEncoder.kt`** -> AI Confidence: **99.48%**
176. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/DefaultSharedObjectCodec.kt`** -> AI Confidence: **99.48%**
177. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ParallelStringDecoder.kt`** -> AI Confidence: **99.48%**
178. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ParallelStringEncoder.kt`** -> AI Confidence: **99.48%**
179. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/services/RemoteScriptUpToDateChecker.kt`** -> AI Confidence: **99.48%**
180. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/operations/ConfigurationCacheBuildOperations.kt`** -> AI Confidence: **99.48%**
181. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheKeyTest.kt`** -> AI Confidence: **99.48%**
182. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprintCheckerTest.kt`** -> AI Confidence: **99.48%**
183. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/problems/ConfigurationCacheProblemsSummaryTest.kt`** -> AI Confidence: **99.48%**
184. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/serialization/codecs/AbstractUserTypeCodecTest.kt`** -> AI Confidence: **99.48%**
185. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/serialization/codecs/BindingsBackedCodecTest.kt`** -> AI Confidence: **99.48%**
186. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/serialization/codecs/JavaObjectSerializationCodecTest.kt`** -> AI Confidence: **99.48%**
187. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/cc/impl/problems/BuildNameProvider.kt`** -> AI Confidence: **99.48%**
188. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/configuration/problems/CommonReport.kt`** -> AI Confidence: **99.48%**
189. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/configuration/problems/DefaultProblemFactory.kt`** -> AI Confidence: **99.48%**
190. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/configuration/problems/PropertyProblem.kt`** -> AI Confidence: **99.48%**
191. **`platforms/core-configuration/configuration-problems-base/src/test/kotlin/org/gradle/problems/internal/impl/JsonWriterTest.kt`** -> AI Confidence: **99.48%**
192. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/ActionNodeCodec.kt`** -> AI Confidence: **99.48%**
193. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/CalculatedValueContainerCodec.kt`** -> AI Confidence: **99.48%**
194. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/ConfigurableFileCollectionCodec.kt`** -> AI Confidence: **99.48%**
195. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/ConfigurableFileTreeCodec.kt`** -> AI Confidence: **99.48%**
196. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/DefaultCopySpecCodec.kt`** -> AI Confidence: **99.48%**
197. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/DestinationRootCopySpecCodec.kt`** -> AI Confidence: **99.48%**
198. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/FileCodecs.kt`** -> AI Confidence: **99.48%**
199. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/FileCollectionCodec.kt`** -> AI Confidence: **99.48%**
200. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/FileTreeCodec.kt`** -> AI Confidence: **99.48%**
201. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/GradlePropertiesCodec.kt`** -> AI Confidence: **99.48%**
202. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/GroovyCodecs.kt`** -> AI Confidence: **99.48%**
203. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/IsolatedCodecs.kt`** -> AI Confidence: **99.48%**
204. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/JavaRecordCodec.kt`** -> AI Confidence: **99.48%**
205. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/OrdinalNodeCodec.kt`** -> AI Confidence: **99.48%**
206. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/PathToFileResolverCodec.kt`** -> AI Confidence: **99.48%**
207. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/PatternSetCodec.kt`** -> AI Confidence: **99.48%**
208. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/ProviderCodecs.kt`** -> AI Confidence: **99.48%**
209. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/SerializedLambdaParametersCheckingCodec.kt`** -> AI Confidence: **99.48%**
210. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/TaskInAnotherBuildCodec.kt`** -> AI Confidence: **99.48%**
211. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/TaskNodeCodec.kt`** -> AI Confidence: **99.48%**
212. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/TaskReferenceCodec.kt`** -> AI Confidence: **99.48%**
213. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/UnsupportedTypesCodecs.kt`** -> AI Confidence: **99.48%**
214. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/WorkNodeCodec.kt`** -> AI Confidence: **99.48%**
215. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/jos/JavaObjectSerializationCodec.kt`** -> AI Confidence: **99.48%**
216. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/jos/JavaSerializationEncodingLookup.kt`** -> AI Confidence: **99.48%**
217. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/jos/ObjectInputStreamAdapter.kt`** -> AI Confidence: **99.48%**
218. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/AnalyzedStatementUtils.kt`** -> AI Confidence: **99.48%**
219. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/DefaultAnalysisSchema.kt`** -> AI Confidence: **99.48%**
220. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/ExpressionResolver.kt`** -> AI Confidence: **99.48%**
221. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/FunctionCallResolver.kt`** -> AI Confidence: **99.48%**
222. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/NamedReferenceResolver.kt`** -> AI Confidence: **99.48%**
223. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/ResolutionOutput.kt`** -> AI Confidence: **99.48%**
224. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/ResolutionTracer.kt`** -> AI Confidence: **99.48%**
225. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/StatementResolver.kt`** -> AI Confidence: **99.48%**
226. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/context.kt`** -> AI Confidence: **99.48%**
227. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/defaultCodeResolver.kt`** -> AI Confidence: **99.48%**
228. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/utils.kt`** -> AI Confidence: **99.48%**
229. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/DataStructuralEquality.kt`** -> AI Confidence: **99.48%**
230. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/fromLanguageTree/LanguageTreeToDom.kt`** -> AI Confidence: **99.48%**
231. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/DefaultModelToDocumentMutationPlanner.kt`** -> AI Confidence: **99.48%**
232. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/DocumentTextMutationPlanner.kt`** -> AI Confidence: **99.48%**
233. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/MutationApplicabilityChecker.kt`** -> AI Confidence: **99.48%**
234. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/ScopeLocationMatcher.kt`** -> AI Confidence: **99.48%**
235. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/operations/overlay/DocumentOverlay.kt`** -> AI Confidence: **99.48%**
236. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/operations/overlay/OverlayRoutedDataContainers.kt`** -> AI Confidence: **99.48%**
237. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/resolution/DefaultDocumentResolutionContainer.kt`** -> AI Confidence: **99.48%**
238. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/DeclarativeReflectionToObjectConverter.kt`** -> AI Confidence: **99.48%**
239. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/DeclarativeRuntimeFunction.kt`** -> AI Confidence: **99.48%**
240. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/FunctionBinding.kt`** -> AI Confidence: **99.48%**
241. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/RuntimeFunctionResolver.kt`** -> AI Confidence: **99.48%**
242. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/RuntimePropertyResolver.kt`** -> AI Confidence: **99.48%**
243. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/objectGraph/PropertyLinkTrace.kt`** -> AI Confidence: **99.48%**
244. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/objectGraph/PropertyLinksResolver.kt`** -> AI Confidence: **99.48%**
245. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/objectGraph/reflectObject.kt`** -> AI Confidence: **99.48%**
246. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/FailureCollectorContext.kt`** -> AI Confidence: **99.48%**
247. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/FailureUtils.kt`** -> AI Confidence: **99.48%**
248. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/GrammarToTree.kt`** -> AI Confidence: **99.48%**
249. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/LightTreeUtil.kt`** -> AI Confidence: **99.48%**
250. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ClassMembersForSchema.kt`** -> AI Confidence: **99.48%**
251. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ConfigureLambdaHandler.kt`** -> AI Confidence: **99.48%**
252. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/DataSchemaBuilder.kt`** -> AI Confidence: **99.48%**
253. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/FunctionExtractor.kt`** -> AI Confidence: **99.48%**
254. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/PropertyExtractor.kt`** -> AI Confidence: **99.48%**
255. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/SchemaResult.kt`** -> AI Confidence: **99.48%**
256. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaUtils/AnalysisSchemaUtils.kt`** -> AI Confidence: **99.48%**
257. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/AugmentationResolutionTest.kt`** -> AI Confidence: **99.48%**
258. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/LocalValueTest.kt`** -> AI Confidence: **99.48%**
259. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/PropertyTest.kt`** -> AI Confidence: **99.48%**
260. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/ResolutionTracerTest.kt`** -> AI Confidence: **99.48%**
261. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/demo/demoUtils.kt`** -> AI Confidence: **99.48%**
262. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/demo/reflection/utils.kt`** -> AI Confidence: **99.48%**
263. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/MutatedDocumentTextGeneratorTest.kt`** -> AI Confidence: **99.48%**
264. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/ModelMutationSubtypingTest.kt`** -> AI Confidence: **99.48%**
265. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/ModelToDocumentMutationPlannerTest.kt`** -> AI Confidence: **99.48%**
266. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/MutationApplicabilityCheckerTest.kt`** -> AI Confidence: **99.48%**
267. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/MutationAsTextRunnerTest.kt`** -> AI Confidence: **99.48%**
268. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/ScopeLocationTest.kt`** -> AI Confidence: **99.48%**
269. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/operations/overlay/DocumentOverlayTest.kt`** -> AI Confidence: **99.48%**
270. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/resolution/DomResolutionTest.kt`** -> AI Confidence: **99.48%**
271. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/resolution/GenericFunctionResolutionTest.kt`** -> AI Confidence: **99.48%**
272. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/resolution/VarargResolutionTest.kt`** -> AI Confidence: **99.48%**
273. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/AccessorTest.kt`** -> AI Confidence: **99.48%**
274. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/CustomLambdasTest.kt`** -> AI Confidence: **99.48%**
275. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/EmptyBlocksTest.kt`** -> AI Confidence: **99.48%**
276. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/TopLevelFunctionInvocationTest.kt`** -> AI Confidence: **99.48%**
277. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/ImportTest.kt`** -> AI Confidence: **99.48%**
278. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/RandomInputParsingTest.kt`** -> AI Confidence: **99.48%**
279. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/prettyPrintResults.kt`** -> AI Confidence: **99.48%**
280. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/ConfiguringFunctionsFromPropertiesTest.kt`** -> AI Confidence: **99.48%**
281. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/ExternalFunctionsTest.kt`** -> AI Confidence: **99.48%**
282. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/FunctionExtractorTest.kt`** -> AI Confidence: **99.48%**
283. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/GenericOpaqueTypesTest.kt`** -> AI Confidence: **99.48%**
284. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/NullableTypesTest.kt`** -> AI Confidence: **99.48%**
285. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/SchemaSupertypeMemberVisibilityTest.kt`** -> AI Confidence: **99.48%**
286. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/schemaBuidler/SchemeExtractionErrorTest.kt`** -> AI Confidence: **99.48%**
287. **`platforms/core-configuration/declarative-dsl-core/src/testFixtures/kotlin/org/gradle/internal/declarativedsl/Augmentations.kt`** -> AI Confidence: **99.48%**
288. **`platforms/core-configuration/declarative-dsl-core/src/testFixtures/kotlin/org/gradle/internal/declarativedsl/demo/resolve.kt`** -> AI Confidence: **99.48%**
289. **`platforms/core-configuration/declarative-dsl-core/src/testFixtures/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/runtimeInstanceFromResult.kt`** -> AI Confidence: **99.48%**
290. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/EvaluationFailureMessageGenerator.kt`** -> AI Confidence: **99.48%**
291. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/checks/AccessOnCurrentReceiverCheck.kt`** -> AI Confidence: **99.48%**
292. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/checks/DocumentCheck.kt`** -> AI Confidence: **99.48%**
293. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/conversion/AnalysisAndConversionStepRunner.kt`** -> AI Confidence: **99.48%**
294. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/defaults/ApplyModelDefaultsHandler.kt`** -> AI Confidence: **99.48%**
295. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/main/AnalysisDocumentUtils.kt`** -> AI Confidence: **99.48%**
296. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/main/SimpleAnalysisEvaluator.kt`** -> AI Confidence: **99.48%**
297. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/runner/AnalysisStepRunner.kt`** -> AI Confidence: **99.48%**
298. **`platforms/core-configuration/declarative-dsl-evaluator/src/testFixtures/kotlin/org/gradle/internal/declarative/dsl/checks/RunChecks.kt`** -> AI Confidence: **99.48%**
299. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/common/GradlePropertyApiAnalysisSchemaComponent.kt`** -> AI Confidence: **99.48%**
300. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/common/MinimalSchemaBuildingComponent.kt`** -> AI Confidence: **99.48%**
301. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/common/StandardLibraryComponent.kt`** -> AI Confidence: **99.48%**
302. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/common/UnsupportedSyntaxFeatureCheck.kt`** -> AI Confidence: **99.48%**
303. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/defaults/ProjectFeatureDeclarationsIntegration.kt`** -> AI Confidence: **99.48%**
304. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/DependencyCollectorFunctionExtractorAndRuntimeResolver.kt`** -> AI Confidence: **99.48%**
305. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/dependencyConfigurationSchema.kt`** -> AI Confidence: **99.48%**
306. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/evaluationSchema/SchemaComponents.kt`** -> AI Confidence: **99.48%**
307. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/features/schemaFromProjectFeatures.kt`** -> AI Confidence: **99.48%**
308. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/DeclarativeKotlinScriptEvaluator.kt`** -> AI Confidence: **99.48%**
309. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/GradleProcessInterpretationSchemaBuilder.kt`** -> AI Confidence: **99.48%**
310. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/StoringInterpretationSchemaBuilder.kt`** -> AI Confidence: **99.48%**
311. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/defaults/ActionBasedModelDefaultsHandler.kt`** -> AI Confidence: **99.48%**
312. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/defaults/DeclarativeModelDefaultsHandler.kt`** -> AI Confidence: **99.48%**
313. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/ndoc/ContainersSchemaComponent.kt`** -> AI Confidence: **99.48%**
314. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/ndoc/DclContainerMemberExtractionUtils.kt`** -> AI Confidence: **99.48%**
315. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/project/ExtensionProperties.kt`** -> AI Confidence: **99.48%**
316. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/project/ProjectSchema.kt`** -> AI Confidence: **99.48%**
317. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/project/TypesafeProjectAccessorsComponent.kt`** -> AI Confidence: **99.48%**
318. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/project/schemaFromGradleExtensions.kt`** -> AI Confidence: **99.48%**
319. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/provider/DeclarativeDslScriptPluginFactory.kt`** -> AI Confidence: **99.48%**
320. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/provider/DeclarativeDslServices.kt`** -> AI Confidence: **99.48%**
321. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/provider/SchemaBuildingFailureProblems.kt`** -> AI Confidence: **99.48%**
322. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/provider/SettingsUnderInitialization.kt`** -> AI Confidence: **99.48%**
323. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/settings/PluginsInterpretationSequenceStep.kt`** -> AI Confidence: **99.48%**
324. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/settings/SettingsBlocksCheck.kt`** -> AI Confidence: **99.48%**
325. **`platforms/core-configuration/declarative-dsl-provider/src/test/kotlin/org/gradle/internal/declarativedsl/ContainersSchemaComponentTest.kt`** -> AI Confidence: **99.48%**
326. **`platforms/core-configuration/declarative-dsl-provider/src/test/kotlin/org/gradle/internal/declarativedsl/DependencyCollectorsComponentTest.kt`** -> AI Confidence: **99.48%**
327. **`platforms/core-configuration/declarative-dsl-provider/src/test/kotlin/org/gradle/internal/declarativedsl/common/StandardLibraryComponentTest.kt`** -> AI Confidence: **99.48%**
328. **`platforms/core-configuration/declarative-dsl-provider/src/test/kotlin/org/gradle/internal/declarativedsl/common/UnsupportedSyntaxFeatureCheckTest.kt`** -> AI Confidence: **99.48%**
329. **`platforms/core-configuration/declarative-dsl-provider/src/test/kotlin/org/gradle/internal/declarativedsl/settings/SettingsBlockCheckTest.kt`** -> AI Confidence: **99.48%**
330. **`platforms/core-configuration/declarative-dsl-provider/src/test/kotlin/org/gradle/internal/declarativedsl/utils/DclContainerMemberExtractionUtilsTest.kt`** -> AI Confidence: **99.48%**
331. **`platforms/core-configuration/declarative-dsl-tooling-builders/src/main/kotlin/org/gradle/declarative/dsl/tooling/builders/DeclarativeSchemaModelBuilder.kt`** -> AI Confidence: **99.48%**
332. **`platforms/core-configuration/declarative-dsl-tooling-builders/src/main/kotlin/org/gradle/declarative/dsl/tooling/builders/internal/ToolingModelServices.kt`** -> AI Confidence: **99.48%**
333. **`platforms/core-configuration/declarative-dsl-tooling-models/src/main/kotlin/org/gradle/declarative/dsl/schema/FunctionSemantics.kt`** -> AI Confidence: **99.48%**
334. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/ArtifactCollectionCodec.kt`** -> AI Confidence: **99.48%**
335. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/AttributeContainerCodecs.kt`** -> AI Confidence: **99.48%**
336. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/DefaultResolvableArtifactCodec.kt`** -> AI Confidence: **99.48%**
337. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/DefaultResolvedArtifactResultCodec.kt`** -> AI Confidence: **99.48%**
338. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/ImmutableAttributesSchemaCodec.kt`** -> AI Confidence: **99.48%**
339. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/LocalFileDependencyBackedArtifactSetCodec.kt`** -> AI Confidence: **99.48%**
340. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/CalculateArtifactsCodec.kt`** -> AI Confidence: **99.48%**
341. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/ChainedTransformStepNodeCodec.kt`** -> AI Confidence: **99.48%**
342. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/ComponentVariantIdentifierCodec.kt`** -> AI Confidence: **99.48%**
343. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/DefaultTransformCodec.kt`** -> AI Confidence: **99.48%**
344. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/FinalizeTransformDependenciesNodeCodec.kt`** -> AI Confidence: **99.48%**
345. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/InitialTransformStepNodeCodec.kt`** -> AI Confidence: **99.48%**
346. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/IsolateTransformParametersCodec.kt`** -> AI Confidence: **99.48%**
347. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/TransformStepCodec.kt`** -> AI Confidence: **99.48%**
348. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/TransformedArtifactCodec.kt`** -> AI Confidence: **99.48%**
349. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/TransformedExternalArtifactSetCodec.kt`** -> AI Confidence: **99.48%**
350. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/TransformedProjectArtifactSetCodec.kt`** -> AI Confidence: **99.48%**
351. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/Transforms.kt`** -> AI Confidence: **99.48%**
352. **`platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/DefaultEncryptionService.kt`** -> AI Confidence: **99.48%**
353. **`platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/KeyStoreKeySource.kt`** -> AI Confidence: **99.48%**
354. **`platforms/core-configuration/flow-services/src/main/kotlin/org/gradle/internal/flow/services/BuildFlowScope.kt`** -> AI Confidence: **99.48%**
355. **`platforms/core-configuration/flow-services/src/main/kotlin/org/gradle/internal/flow/services/DefaultFlowProviders.kt`** -> AI Confidence: **99.48%**
356. **`platforms/core-configuration/flow-services/src/main/kotlin/org/gradle/internal/flow/services/FlowParametersInstantiator.kt`** -> AI Confidence: **99.48%**
357. **`platforms/core-configuration/flow-services/src/main/kotlin/org/gradle/internal/flow/services/FlowScheduler.kt`** -> AI Confidence: **99.48%**
358. **`platforms/core-configuration/graph-isolation/src/main/kotlin/org/gradle/internal/isolate/graph/IsolatedActionSerializer.kt`** -> AI Confidence: **99.48%**
359. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Codec.kt`** -> AI Confidence: **99.48%**
360. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Combinators.kt`** -> AI Confidence: **99.48%**
361. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Contexts.kt`** -> AI Confidence: **99.48%**
362. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Logging.kt`** -> AI Confidence: **99.48%**
363. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/codecs/BindingsBackedCodec.kt`** -> AI Confidence: **99.48%**
364. **`platforms/core-configuration/isolated-action-services/src/main/kotlin/org/gradle/internal/isolate/actions/services/DefaultIsolatedProjectEvaluationListenerProvider.kt`** -> AI Confidence: **99.48%**
365. **`platforms/core-configuration/isolated-action-services/src/test/kotlin/org/gradle/internal/isolate/actions/services/IsolatedActionCodecsFactoryTest.kt`** -> AI Confidence: **99.48%**
366. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/DependencyManagementIntegrationTest.kt`** -> AI Confidence: **99.48%**
367. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/GradleApiExtensionsIntegrationTest.kt`** -> AI Confidence: **99.48%**
368. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/GradleKotlinDslIntegrationTest.kt`** -> AI Confidence: **99.48%**
369. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/GradleKotlinDslRegressionsTest.kt`** -> AI Confidence: **99.48%**
370. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinDslJvmTargetIntegrationTest.kt`** -> AI Confidence: **99.48%**
371. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinDslNullnessIntegrationTest.kt`** -> AI Confidence: **99.48%**
372. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PrecompiledScriptPluginAccessorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
373. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PrecompiledScriptPluginErrorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
374. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PrecompiledScriptPluginSyntheticIntegrationTest.kt`** -> AI Confidence: **99.48%**
375. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PrecompiledScriptPluginTasksIntegrationTest.kt`** -> AI Confidence: **99.48%**
376. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/ProjectSchemaAccessorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
377. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/SkipMetadataVersionCheckTest.kt`** -> AI Confidence: **99.48%**
378. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/declarative/KotlinDslContainerElementFactoryIntegrationTest.kt`** -> AI Confidence: **99.48%**
379. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/dsl/KotlinDslPluginCrossVersionSmokeTest.kt`** -> AI Confidence: **99.48%**
380. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/dsl/KotlinDslPluginGradlePluginCrossVersionSmokeTest.kt`** -> AI Confidence: **99.48%**
381. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/dsl/KotlinDslPluginTest.kt`** -> AI Confidence: **99.48%**
382. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/embedded/EmbeddedKotlinPluginIntegTest.kt`** -> AI Confidence: **99.48%**
383. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/precompiled/KotlinParser.kt`** -> AI Confidence: **99.48%**
384. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/precompiled/PrecompiledScriptPluginAccessorsTest.kt`** -> AI Confidence: **99.48%**
385. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/precompiled/PrecompiledScriptPluginTemplatesTest.kt`** -> AI Confidence: **99.48%**
386. **`platforms/core-configuration/kotlin-dsl-plugins/src/main/kotlin/org/gradle/kotlin/dsl/plugins/dsl/KotlinDslPlugin.kt`** -> AI Confidence: **99.48%**
387. **`platforms/core-configuration/kotlin-dsl-plugins/src/main/kotlin/org/gradle/kotlin/dsl/plugins/embedded/EmbeddedKotlinPlugin.kt`** -> AI Confidence: **99.48%**
388. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/DefaultProjectSchemaProvider.kt`** -> AI Confidence: **99.48%**
389. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/KotlinDslDclSchemaCollector.kt`** -> AI Confidence: **99.48%**
390. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/DefaultPrecompiledScriptPluginsSupport.kt`** -> AI Confidence: **99.48%**
391. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/PrecompiledScriptPlugin.kt`** -> AI Confidence: **99.48%**
392. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/tasks/ClassPathAware.kt`** -> AI Confidence: **99.48%**
393. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/tasks/ExtractPrecompiledScriptPluginPlugins.kt`** -> AI Confidence: **99.48%**
394. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/tasks/GenerateScriptPluginAdapters.kt`** -> AI Confidence: **99.48%**
395. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/test/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/PrecompiledScriptPluginTest.kt`** -> AI Confidence: **99.48%**
396. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/BuildSrcClassPathModeConfigurationAction.kt`** -> AI Confidence: **99.48%**
397. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/KotlinBuildScriptModelBuilder.kt`** -> AI Confidence: **99.48%**
398. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/KotlinDslScriptsModelBuilder.kt`** -> AI Confidence: **99.48%**
399. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/internal/IsolatedProjectsSafeKotlinDslScriptsModelBuilder.kt`** -> AI Confidence: **99.48%**
400. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/internal/KotlinScriptingModelBuildersRegistrant.kt`** -> AI Confidence: **99.48%**
401. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/internal/KotlinScriptingModelBuildersServices.kt`** -> AI Confidence: **99.48%**
402. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/test/kotlin/org/gradle/kotlin/dsl/tooling/builders/EditorReportsBuilderTest.kt`** -> AI Confidence: **99.48%**
403. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/codegen/ApiTypeProviderTest.kt`** -> AI Confidence: **99.48%**
404. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/AbstractCompileAvoidanceIntegrationTest.kt`** -> AI Confidence: **99.48%**
405. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/DeprecationInAccessorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
406. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/OptInAccessorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
407. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/dcl/DclInterpreterIntegrationTest.kt`** -> AI Confidence: **99.48%**
408. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/dcl/DeprecationInDclAccessorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
409. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinBuildScriptIntegrationTest.kt`** -> AI Confidence: **99.48%**
410. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinSettingsScriptIntegrationTest.kt`** -> AI Confidence: **99.48%**
411. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PluginSpecBuilderAccessorsIntegrationTest.kt`** -> AI Confidence: **99.48%**
412. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/resolver/SourceDistributionResolverIntegrationTest.kt`** -> AI Confidence: **99.48%**
413. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/support/ClassBytesRepositoryTest.kt`** -> AI Confidence: **99.48%**
414. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/support/EmbeddedKotlinProviderTest.kt`** -> AI Confidence: **99.48%**
415. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/DependencyHandlerExtensions.kt`** -> AI Confidence: **99.48%**
416. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/DependencyHandlerScope.kt`** -> AI Confidence: **99.48%**
417. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/InitScriptApi.kt`** -> AI Confidence: **99.48%**
418. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/KotlinGradleScriptTemplate.kt`** -> AI Confidence: **99.48%**
419. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/KotlinInitScript.kt`** -> AI Confidence: **99.48%**
420. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/KotlinSettingsScript.kt`** -> AI Confidence: **99.48%**
421. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/KotlinSettingsScriptTemplate.kt`** -> AI Confidence: **99.48%**
422. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/NamedDomainObjectCollectionExtensions.kt`** -> AI Confidence: **99.48%**
423. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/NamedDomainObjectContainerExtensions.kt`** -> AI Confidence: **99.48%**
424. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/PropertyDelegate.kt`** -> AI Confidence: **99.48%**
425. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/SettingsScriptApi.kt`** -> AI Confidence: **99.48%**
426. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/TaskContainerExtensions.kt`** -> AI Confidence: **99.48%**
427. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/AccessorFragments.kt`** -> AI Confidence: **99.48%**
428. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/AccessorsClassPath.kt`** -> AI Confidence: **99.48%**
429. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/Emitter.kt`** -> AI Confidence: **99.48%**
430. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/GeneratePluginSpecBuilderAccessors.kt`** -> AI Confidence: **99.48%**
431. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/GenerateVersionCatalogAccessors.kt`** -> AI Confidence: **99.48%**
432. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/OptInAnnotationsCollector.kt`** -> AI Confidence: **99.48%**
433. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/Stage1BlocksAccessorClassPath.kt`** -> AI Confidence: **99.48%**
434. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/runtime/Runtime.kt`** -> AI Confidence: **99.48%**
435. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/tasks/PrintAccessors.kt`** -> AI Confidence: **99.48%**
436. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/concurrent/BuildServices.kt`** -> AI Confidence: **99.48%**
437. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/concurrent/future.kt`** -> AI Confidence: **99.48%**
438. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/Combinators.kt`** -> AI Confidence: **99.48%**
439. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/DefaultKotlinMetadataCompatibilityChecker.kt`** -> AI Confidence: **99.48%**
440. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/GradleUserHomeServices.kt`** -> AI Confidence: **99.48%**
441. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/Interpreter.kt`** -> AI Confidence: **99.48%**
442. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/KotlinGrammar.kt`** -> AI Confidence: **99.48%**
443. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/Lexer.kt`** -> AI Confidence: **99.48%**
444. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/PartialEvaluator.kt`** -> AI Confidence: **99.48%**
445. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/ResidualProgramCompiler.kt`** -> AI Confidence: **99.48%**
446. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/metadataCompatibilityCheck.kt`** -> AI Confidence: **99.48%**
447. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/normalization/GradleUserHomeServices.kt`** -> AI Confidence: **99.48%**
448. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/normalization/KotlinApiMemberWriter.kt`** -> AI Confidence: **99.48%**
449. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/normalization/KotlinCompileClasspathFingerprinter.kt`** -> AI Confidence: **99.48%**
450. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/precompile/PrecompiledScriptDependenciesResolver.kt`** -> AI Confidence: **99.48%**
451. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/precompile/v1/PrecompiledScriptTemplates.kt`** -> AI Confidence: **99.48%**
452. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/BuildServices.kt`** -> AI Confidence: **99.48%**
453. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/KotlinScriptClassPathProvider.kt`** -> AI Confidence: **99.48%**
454. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/KotlinScriptEvaluator.kt`** -> AI Confidence: **99.48%**
455. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/KotlinScriptPluginFactory.kt`** -> AI Confidence: **99.48%**
456. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/PluginRequestsHandler.kt`** -> AI Confidence: **99.48%**
457. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/FindGradleSources.kt`** -> AI Confidence: **99.48%**
458. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/KotlinBuildScriptDependenciesResolver.kt`** -> AI Confidence: **99.48%**
459. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/KotlinBuildScriptModelRequest.kt`** -> AI Confidence: **99.48%**
460. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/ResolverEventLogger.kt`** -> AI Confidence: **99.48%**
461. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/SourceDistributionProvider.kt`** -> AI Confidence: **99.48%**
462. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/SourcePathProvider.kt`** -> AI Confidence: **99.48%**
463. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/internal/GradleDistRepoDescriptorLocator.kt`** -> AI Confidence: **99.48%**
464. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/DefaultKotlinScript.kt`** -> AI Confidence: **99.48%**
465. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/KotlinScriptHost.kt`** -> AI Confidence: **99.48%**
466. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/bytecode/AsmExtensions.kt`** -> AI Confidence: **99.48%**
467. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/bytecode/KotlinMetadata.kt`** -> AI Confidence: **99.48%**
468. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/delegates/GradleDelegate.kt`** -> AI Confidence: **99.48%**
469. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/delegates/SettingsDelegate.kt`** -> AI Confidence: **99.48%**
470. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/delegates/TaskContainerDelegate.kt`** -> AI Confidence: **99.48%**
471. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/ArtifactHandlerExtensionsTest.kt`** -> AI Confidence: **99.48%**
472. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/BuildCacheConfigurationExtensionsTest.kt`** -> AI Confidence: **99.48%**
473. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/ComponentSelectionRulesTest.kt`** -> AI Confidence: **99.48%**
474. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/DelegatedGradlePropertiesExtensionsTest.kt`** -> AI Confidence: **99.48%**
475. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/ExtensionContainerExtensionsTest.kt`** -> AI Confidence: **99.48%**
476. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/GroovyInteroperabilityTest.kt`** -> AI Confidence: **99.48%**
477. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/PluginAwareExtensionsTest.kt`** -> AI Confidence: **99.48%**
478. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/ProjectExtensionsTest.kt`** -> AI Confidence: **99.48%**
479. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/ScriptHandlerScopeTest.kt`** -> AI Confidence: **99.48%**
480. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/SourceControlExtensionsTest.kt`** -> AI Confidence: **99.48%**
481. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/accessors/ProjectAccessorsClassPathTest.kt`** -> AI Confidence: **99.48%**
482. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/accessors/ProjectSchemaTest.kt`** -> AI Confidence: **99.48%**
483. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/accessors/TestWithClassPath.kt`** -> AI Confidence: **99.48%**
484. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/accessors/tasks/PrintAccessorsTest.kt`** -> AI Confidence: **99.48%**
485. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/codegen/GradleApiExtensionsTest.kt`** -> AI Confidence: **99.48%**
486. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/concurrent/JavaSystemPropertiesAsyncIOScopeSettingsTest.kt`** -> AI Confidence: **99.48%**
487. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/PartialEvaluatorTest.kt`** -> AI Confidence: **99.48%**
488. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/TopLevelBlockExtractionTest.kt`** -> AI Confidence: **99.48%**
489. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/integration/GradleApiParameterNamesTest.kt`** -> AI Confidence: **99.48%**
490. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/normalization/KotlinApiClassExtractorTest.kt`** -> AI Confidence: **99.48%**
491. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/provider/ScriptApiTest.kt`** -> AI Confidence: **99.48%**
492. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/resolver/KotlinBuildScriptModelRepositoryTest.kt`** -> AI Confidence: **99.48%**
493. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/resolver/SourcePathProviderTest.kt`** -> AI Confidence: **99.48%**
494. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/support/ZipTest.kt`** -> AI Confidence: **99.48%**
495. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/AbstractKotlinIntegrationTest.kt`** -> AI Confidence: **99.48%**
496. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/SimplifiedKotlinScriptEvaluator.kt`** -> AI Confidence: **99.48%**
497. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/TestKotlinCompiler.kt`** -> AI Confidence: **99.48%**
498. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/Testing.kt`** -> AI Confidence: **99.48%**
499. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/bytecode/AsmExtensions.kt`** -> AI Confidence: **99.48%**
500. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/zip.kt`** -> AI Confidence: **99.48%**
501. **`platforms/core-configuration/project-features-demos/src/main/kotlin/org/gradle/api/plugins/antlr/AntlrProjectFeaturePlugin.kt`** -> AI Confidence: **99.48%**
502. **`platforms/core-configuration/project-features-demos/src/main/kotlin/org/gradle/api/plugins/java/plugin/JvmBuildLogicUtils.kt`** -> AI Confidence: **99.48%**
503. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/ProxyCodec.kt`** -> AI Confidence: **99.48%**
504. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/StreamCodecs.kt`** -> AI Confidence: **99.48%**
505. **`platforms/ide/problems/src/main/kotlin/org/gradle/problems/internal/impl/DefaultProblemsReportCreator.kt`** -> AI Confidence: **99.48%**
506. **`testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/validate-external-gradle-plugin.gradle.kts`** -> AI Confidence: **99.48%**
507. **`testing/soak/src/integTest/kotlin/org/gradle/kotlin/dsl/caching/ScriptCachingIntegrationTest.kt`** -> AI Confidence: **99.48%**
508. **`testing/soak/src/integTest/kotlin/org/gradle/kotlin/dsl/caching/fixtures/CompilationCache.kt`** -> AI Confidence: **99.48%**
509. **`platforms/core-configuration/base-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/HelpTaskIntegrationTest.groovy`** -> AI Confidence: **99.48%**
510. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheBuildTreeStructureIntegrationTest.groovy`** -> AI Confidence: **99.48%**
511. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheGradlePropertiesIntegrationTest.groovy`** -> AI Confidence: **99.48%**
512. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheProblemReportingIntegrationTest.groovy`** -> AI Confidence: **99.48%**
513. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/slf4j/OutputEventListenerBackedLoggerTest.groovy`** -> AI Confidence: **99.48%**
514. **`platforms/core-runtime/wrapper-main/src/crossVersionTest/groovy/org/gradle/integtests/wrapper/WrapperPropertiesLoaderCrossVersionTest.groovy`** -> AI Confidence: **99.48%**
515. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioMultiProjectIntegrationTest.groovy`** -> AI Confidence: **99.48%**
516. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioSoftwareModelMultiProjectIntegrationTest.groovy`** -> AI Confidence: **99.48%**
517. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeMultipleSwiftProjectIntegrationTest.groovy`** -> AI Confidence: **99.48%**
518. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeSwiftExternalSourceDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.48%**
519. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r27/TestLauncherCrossVersionSpec.groovy`** -> AI Confidence: **99.48%**
520. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/TaskDependenciesCrossVersionSpec.groovy`** -> AI Confidence: **99.48%**
521. **`platforms/jvm/jvm-services/src/test/groovy/org/gradle/internal/jvm/inspection/DefaultJvmMetadataDetectorTest.groovy`** -> AI Confidence: **99.48%**
522. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/integtests/ConfigurationCacheJavaIntegrationTest.groovy`** -> AI Confidence: **99.48%**
523. **`platforms/jvm/plugins-application/src/integTest/groovy/org/gradle/api/plugins/ApplicationPluginIntegrationTest.groovy`** -> AI Confidence: **99.48%**
524. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/integtests/JavaProjectIntegrationTest.groovy`** -> AI Confidence: **99.48%**
525. **`platforms/jvm/scala/src/test/groovy/org/gradle/scala/compile/internal/ScalaCompileOptionsConfigurerTest.groovy`** -> AI Confidence: **99.48%**
526. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/junit5/jupiter/JUnit5JupiterParameterizedClassIntegrationTest.groovy`** -> AI Confidence: **99.48%**
527. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/junit6/jupiter/JUnit6JupiterParameterizedClassIntegrationTest.groovy`** -> AI Confidence: **99.48%**
528. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftApplicationCppInteroperabilityIntegrationTest.groovy`** -> AI Confidence: **99.48%**
529. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftApplicationIntegrationTest.groovy`** -> AI Confidence: **99.48%**
530. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftLibraryIntegrationTest.groovy`** -> AI Confidence: **99.48%**
531. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/internal/component/resolution/failure/ResolutionFailureHandlerIntegrationTest.groovy`** -> AI Confidence: **99.48%**
532. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ArtifactDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.48%**
533. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ConfigurationCacheDependencyResolutionFeaturesIntegrationTest.groovy`** -> AI Confidence: **99.48%**
534. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ConfigurationCacheDependencyResolutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
535. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/DependencyManagementResultsAsInputsIntegrationTest.groovy`** -> AI Confidence: **99.48%**
536. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/alignment/ForcingUsingStrictlyPlatformAlignmentTest.groovy`** -> AI Confidence: **99.48%**
537. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ResolvedArtifactsApiIntegrationTest.groovy`** -> AI Confidence: **99.48%**
538. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/caching/RecoverFromBrokenResolutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
539. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/catalog/TomlDependenciesExtensionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
540. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/catalog/VersionCatalogExtensionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
541. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyBrokenRemoteResolveIntegrationTest.groovy`** -> AI Confidence: **99.48%**
542. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyDynamicRevisionRemoteResolveIntegrationTest.groovy`** -> AI Confidence: **99.48%**
543. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyHttpRepoResolveIntegrationTest.groovy`** -> AI Confidence: **99.48%**
544. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenBrokenRemoteResolveIntegrationTest.groovy`** -> AI Confidence: **99.48%**
545. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenRemoteDependencyWithGradleMetadataResolutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
546. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/suppliers/DynamicRevisionRemoteResolveWithMetadataSupplierIntegrationTest.groovy`** -> AI Confidence: **99.48%**
547. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.48%**
548. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformIntegrationTest.groovy`** -> AI Confidence: **99.48%**
549. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformWithDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.48%**
550. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationIntegrityCheckIntegTest.groovy`** -> AI Confidence: **99.48%**
551. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy`** -> AI Confidence: **99.48%**
552. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/versions/VersionConflictResolutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
553. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/GradleModuleMetadataParserTest.groovy`** -> AI Confidence: **99.48%**
554. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/notations/ComponentIdentifierParserTest.groovy`** -> AI Confidence: **99.48%**
555. **`platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/AbstractMavenPublishJavaIntegTest.groovy`** -> AI Confidence: **99.48%**
556. **`platforms/software/reporting/src/integTest/groovy/org/gradle/api/reporting/plugins/BuildDashboardPluginIntegrationTest.groovy`** -> AI Confidence: **99.48%**
557. **`platforms/software/software-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/DependencyInsightReportVariantDetailsIntegrationTest.groovy`** -> AI Confidence: **99.48%**
558. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildBuildSrcBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.48%**
559. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildConfigurationAttributesResolveIntegrationTest.groovy`** -> AI Confidence: **99.48%**
560. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildDependencyGraphIntegrationTest.groovy`** -> AI Confidence: **99.48%**
561. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.48%**
562. **`subprojects/core/src/integTest/groovy/org/gradle/api/ConfigurationOnDemandIntegrationTest.groovy`** -> AI Confidence: **99.48%**
563. **`subprojects/core/src/integTest/groovy/org/gradle/api/FinalizerTaskIntegrationTest.groovy`** -> AI Confidence: **99.48%**
564. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/IncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.48%**
565. **`subprojects/core/src/integTest/groovy/org/gradle/execution/taskgraph/ParallelTaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
566. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/CalculateTaskGraphBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.48%**
567. **`subprojects/core/src/integTest/groovy/org/gradle/internal/operations/notify/BuildOperationNotificationIntegrationTest.groovy`** -> AI Confidence: **99.48%**
568. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/TaskErrorExecutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
569. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/TaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.48%**
570. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/NebulaPluginsSmokeTest.groovy`** -> AI Confidence: **99.48%**
571. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DaemonStateCoordinator.java`** -> AI Confidence: **99.39%**
572. **`platforms/jvm/jvm-services/src/main/java/org/gradle/api/internal/artifacts/JavaEcosystemAttributesDescriber.java`** -> AI Confidence: **99.39%**
573. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/KotlinCompiler.kt`** -> AI Confidence: **99.39%**
574. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiIdeaProjectIntegrationTest.groovy`** -> AI Confidence: **99.39%**
575. **`platforms/core-configuration/declarative-dsl-provider/src/integTest/groovy/org/gradle/internal/declarativedsl/settings/DeclarativeDslProjectSettingsIntegrationSpec.groovy`** -> AI Confidence: **99.39%**
576. **`platforms/core-configuration/declarative-dsl-provider/src/integTest/groovy/org/gradle/internal/declarativedsl/settings/ProjectTypeModelDefaultsIntegrationTest.groovy`** -> AI Confidence: **99.39%**
577. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/MapPropertySpec.groovy`** -> AI Confidence: **99.39%**
578. **`platforms/core-configuration/model-reflect/src/test/groovy/org/gradle/internal/reflect/validation/ValidationMessageCheckerTest.groovy`** -> AI Confidence: **99.39%**
579. **`platforms/core-configuration/project-features/src/integTest/groovy/org/gradle/features/ProjectFeatureDeclarationIntegrationTest.groovy`** -> AI Confidence: **99.39%**
580. **`platforms/core-execution/build-cache-http/src/integTest/groovy/org/gradle/caching/http/internal/HttpBuildCacheServiceIntegrationTest.groovy`** -> AI Confidence: **99.39%**
581. **`platforms/core-execution/execution/src/test/groovy/org/gradle/internal/execution/history/changes/ClasspathCompareStrategyTest.groovy`** -> AI Confidence: **99.39%**
582. **`platforms/core-runtime/build-configuration/src/integTest/groovy/org/gradle/interal/buildconfiguration/tasks/UpdateDaemonJvmIntegrationTest.groovy`** -> AI Confidence: **99.39%**
583. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonLifecycleSpec.groovy`** -> AI Confidence: **99.39%**
584. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/DeprecationHandlingIntegrationTest.groovy`** -> AI Confidence: **99.39%**
585. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/LoggingIntegrationTest.groovy`** -> AI Confidence: **99.39%**
586. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/deprecation/DeprecationMessagesTest.groovy`** -> AI Confidence: **99.39%**
587. **`platforms/extensibility/plugin-use/src/integTest/groovy/org/gradle/plugin/repository/ResolvingFromSingleCustomPluginRepositorySpec.groovy`** -> AI Confidence: **99.39%**
588. **`platforms/extensibility/plugin-use/src/integTest/groovy/org/gradle/plugin/repository/ResolvingWithPluginManagementSpec.groovy`** -> AI Confidence: **99.39%**
589. **`platforms/extensibility/plugin-use/src/integTest/groovy/org/gradle/plugin/use/AlreadyOnClasspathPluginUseIntegrationTest.groovy`** -> AI Confidence: **99.39%**
590. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioSoftwareModelSingleProjectIntegrationTest.groovy`** -> AI Confidence: **99.39%**
591. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeCppApplicationProjectIntegrationTest.groovy`** -> AI Confidence: **99.39%**
592. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeCppExternalSourceDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
593. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeSingleSwiftProjectIntegrationTest.groovy`** -> AI Confidence: **99.39%**
594. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeSwiftApplicationProjectIntegrationTest.groovy`** -> AI Confidence: **99.39%**
595. **`platforms/ide/ide-plugins/src/integTest/groovy/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest.groovy`** -> AI Confidence: **99.39%**
596. **`platforms/ide/ide/src/integTest/groovy/org/gradle/plugins/ide/AbstractSourcesAndJavadocJarsIntegrationTest.groovy`** -> AI Confidence: **99.39%**
597. **`platforms/ide/ide/src/integTest/groovy/org/gradle/plugins/ide/eclipse/EclipseClasspathIntegrationTest.groovy`** -> AI Confidence: **99.39%**
598. **`platforms/ide/problems-api/src/integTest/groovy/org/gradle/api/problems/ProblemsServiceIntegrationTest.groovy`** -> AI Confidence: **99.39%**
599. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r112/BuildInvocationsCrossVersionSpec.groovy`** -> AI Confidence: **99.39%**
600. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r26/TestLauncherCrossVersionSpec.groovy`** -> AI Confidence: **99.39%**
601. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r76/TestLauncherTaskExecutionCrossVersionSpec.groovy`** -> AI Confidence: **99.39%**
602. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/r214/ToolingApiEclipseModelWtpClasspathAttributesCrossVersionSpec.groovy`** -> AI Confidence: **99.39%**
603. **`platforms/jvm/ear/src/integTest/groovy/org/gradle/plugins/ear/EarPluginIntegrationTest.groovy`** -> AI Confidence: **99.39%**
604. **`platforms/jvm/plugins-java-library/src/integTest/groovy/org/gradle/java/JavaLibraryFeatureCompilationIntegrationTest.groovy`** -> AI Confidence: **99.39%**
605. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/java/compile/AbstractJavaCompileAvoidanceIntegrationSpec.groovy`** -> AI Confidence: **99.39%**
606. **`platforms/jvm/testing-jvm-infrastructure/src/test/groovy/org/gradle/api/internal/tasks/testing/testng/TestNGTestDefinitionProcessorTest.groovy`** -> AI Confidence: **99.39%**
607. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testsuites/dependencies/TestSuitesKotlinDSLDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
608. **`platforms/jvm/toolchains-jvm/src/test/groovy/org/gradle/jvm/toolchain/internal/ShowToolchainsTaskTest.groovy`** -> AI Confidence: **99.39%**
609. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/AbstractNativeLanguageIncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.39%**
610. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppApplicationIntegrationTest.groovy`** -> AI Confidence: **99.39%**
611. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppLibraryIntegrationTest.groovy`** -> AI Confidence: **99.39%**
612. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/nativeplatform/NativeLanguageSamplesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
613. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/NativeBinariesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
614. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/NativePlatformSamplesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
615. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/AbstractNativeUnitTestIntegrationTest.groovy`** -> AI Confidence: **99.39%**
616. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/cunit/CUnitIntegrationTest.groovy`** -> AI Confidence: **99.39%**
617. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/googletest/GoogleTestIntegrationTest.groovy`** -> AI Confidence: **99.39%**
618. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/DependencyUnresolvedModuleIntegrationTest.groovy`** -> AI Confidence: **99.39%**
619. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/RepositoriesDeclaredInSettingsIntegrationTest.groovy`** -> AI Confidence: **99.39%**
620. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ConfigurationDefaultsIntegrationTest.groovy`** -> AI Confidence: **99.39%**
621. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ConfigurationMutationIntegrationTest.groovy`** -> AI Confidence: **99.39%**
622. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ConfigurationRoleUsageIntegrationTest.groovy`** -> AI Confidence: **99.39%**
623. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ConfigurationRolesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
624. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/MetadataSourcesResolveIntegrationTest.groovy`** -> AI Confidence: **99.39%**
625. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenHttpRepoResolveIntegrationTest.groovy`** -> AI Confidence: **99.39%**
626. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest.groovy`** -> AI Confidence: **99.39%**
627. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlWriterTest.groovy`** -> AI Confidence: **99.39%**
628. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/model/GraphVariantSelectorTest.groovy`** -> AI Confidence: **99.39%**
629. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/resolve/ModuleVersionNotFoundExceptionTest.groovy`** -> AI Confidence: **99.39%**
630. **`platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/integtests/fixtures/publish/ModuleVersionSpec.groovy`** -> AI Confidence: **99.39%**
631. **`platforms/software/ivy/src/integTest/groovy/org/gradle/api/publish/ivy/IvyPublishHttpIntegTest.groovy`** -> AI Confidence: **99.39%**
632. **`platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/MavenPublishIssuesIntegTest.groovy`** -> AI Confidence: **99.39%**
633. **`platforms/software/publish/src/test/groovy/org/gradle/api/publish/internal/metadata/GradleModuleMetadataWriterTest.groovy`** -> AI Confidence: **99.39%**
634. **`platforms/software/resources-gcs/src/integTest/groovy/org/gradle/integtests/resource/gcs/maven/MavenGcsRepoErrorsIntegrationTest.groovy`** -> AI Confidence: **99.39%**
635. **`platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/fixtures/S3Server.groovy`** -> AI Confidence: **99.39%**
636. **`platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/maven/MavenS3RepoErrorsIntegrationTest.groovy`** -> AI Confidence: **99.39%**
637. **`platforms/software/signing/src/integTest/groovy/org/gradle/plugins/signing/SigningTasksIntegrationSpec.groovy`** -> AI Confidence: **99.39%**
638. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/tasks/userinput/UserInputHandlingIntegrationTest.groovy`** -> AI Confidence: **99.39%**
639. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/BuildResultLoggerIntegrationTest.groovy`** -> AI Confidence: **99.39%**
640. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy`** -> AI Confidence: **99.39%**
641. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/GradleBuildTaskIntegrationTest.groovy`** -> AI Confidence: **99.39%**
642. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/ReproducibleArchivesIntegrationTest.groovy`** -> AI Confidence: **99.39%**
643. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/bundling/ArchiveIntegrationTest.groovy`** -> AI Confidence: **99.39%**
644. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/outputorigin/IncrementalBuildOutputOriginIntegrationTest.groovy`** -> AI Confidence: **99.39%**
645. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/buildsrc/BuildSrcIdentityIntegrationTest.groovy`** -> AI Confidence: **99.39%**
646. **`subprojects/core/src/test/groovy/org/gradle/configuration/project/LifecycleProjectEvaluatorTest.groovy`** -> AI Confidence: **99.39%**
647. **`subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy`** -> AI Confidence: **99.39%**
648. **`subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanTest.groovy`** -> AI Confidence: **99.39%**
649. **`subprojects/core/src/test/groovy/org/gradle/execution/selection/DefaultBuildTaskSelectorTest.groovy`** -> AI Confidence: **99.39%**
650. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/SyncTaskIntegrationTest.groovy`** -> AI Confidence: **99.39%**
651. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest-printers.h`** -> AI Confidence: **99.39%**
652. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-param-util.h`** -> AI Confidence: **99.39%**
653. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/JvmProjectInitDescriptor.java`** -> AI Confidence: **99.35%**
654. **`platforms/core-execution/execution/src/test/groovy/org/gradle/internal/execution/history/changes/FingerprintCompareStrategyTest.groovy`** -> AI Confidence: **99.35%**
655. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/BuildInitPluginIntegrationTest.groovy`** -> AI Confidence: **99.35%**
656. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/HttpAuthenticationDependencyResolutionIntegrationTest.groovy`** -> AI Confidence: **99.35%**
657. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenSnapshotResolveIntegrationTest.groovy`** -> AI Confidence: **99.35%**
658. **`platforms/software/version-control/src/integTest/groovy/org/gradle/vcs/internal/SourceDependencyBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.35%**
659. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/buildsrc/BuildSrcBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.35%**
660. **`subprojects/core/src/integTest/groovy/org/gradle/normalization/ConfigureRuntimeClasspathNormalizationIntegrationTest.groovy`** -> AI Confidence: **99.35%**
661. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/ProjectLoadingIntegrationTest.java`** -> AI Confidence: **99.34%**
662. **`.teamcity/src/main/kotlin/promotion/BasePublishGradleDistribution.kt`** -> AI Confidence: **99.34%**
663. **`.teamcity/src/main/kotlin/promotion/StartReleaseCycleTest.kt`** -> AI Confidence: **99.34%**
664. **`build-logic-commons/basics/src/main/kotlin/gradlebuild.minify.gradle.kts`** -> AI Confidence: **99.34%**
665. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/BuildScanInfoCollectingServices.kt`** -> AI Confidence: **99.34%**
666. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/nullaway/NullawayAttributes.kt`** -> AI Confidence: **99.34%**
667. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild/identity/extension/ReleasedVersionsDetails.kt`** -> AI Confidence: **99.34%**
668. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild/identity/provider/BuildTimestampFromBuildReceiptValueSource.kt`** -> AI Confidence: **99.34%**
669. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/BinaryCompatibilityRepositoryLifecycle.kt`** -> AI Confidence: **99.34%**
670. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/ReleasedVersionsHelper.kt`** -> AI Confidence: **99.34%**
671. **`build-logic/dependency-modules/src/main/kotlin/gradlebuild.dependency-modules.gradle.kts`** -> AI Confidence: **99.34%**
672. **`build-logic/idea/src/main/kotlin/gradlebuild.ide.gradle.kts`** -> AI Confidence: **99.34%**
673. **`build-logic/integration-testing/src/main/kotlin/gradlebuild.distribution-testing.gradle.kts`** -> AI Confidence: **99.34%**
674. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/tasks/IntegrationTest.kt`** -> AI Confidence: **99.34%**
675. **`build-logic/jvm/src/main/kotlin/gradlebuild.module-target-runtimes.gradle.kts`** -> AI Confidence: **99.34%**
676. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/codegen/PluginEntry.kt`** -> AI Confidence: **99.34%**
677. **`build-logic/kotlin-dsl/src/main/kotlin/gradlebuild/kotlindsl/generator/codegen/GradleApiMetadata.kt`** -> AI Confidence: **99.34%**
678. **`build-logic/kotlin-dsl/src/main/kotlin/gradlebuild/kotlindsl/generator/codegen/KotlinExtensionsForGradleApiFacade.kt`** -> AI Confidence: **99.34%**
679. **`build-logic/packaging/src/main/kotlin/gradlebuild.public-api-jar.gradle.kts`** -> AI Confidence: **99.34%**
680. **`build-logic/packaging/src/test/kotlin/gradlebuild/instrumentation/InstrumentationMetadataPluginTest.kt`** -> AI Confidence: **99.34%**
681. **`build-logic/performance-testing/src/test/kotlin/gradlebuild/performance/junit4/SecureUnmarshallerTest.kt`** -> AI Confidence: **99.34%**
682. **`gradle/shared-with-buildSrc/mirrors.settings.gradle.kts`** -> AI Confidence: **99.34%**
683. **`platforms/core-configuration/configuration-cache-base/src/main/kotlin/org/gradle/internal/cc/base/serialize/ProjectRef.kt`** -> AI Confidence: **99.34%**
684. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/buildtree/control/DefaultBuildModelParametersFactory.kt`** -> AI Confidence: **99.34%**
685. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CachedBuildState.kt`** -> AI Confidence: **99.34%**
686. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareBuildModelController.kt`** -> AI Confidence: **99.34%**
687. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CrossProjectModelAccessTrackingClosure.kt`** -> AI Confidence: **99.34%**
688. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DynamicCallProblemReporting.kt`** -> AI Confidence: **99.34%**
689. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/TaskExecutionAccessCheckers.kt`** -> AI Confidence: **99.34%**
690. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/models/DefaultToolingModelParameterCarrierFactory.kt`** -> AI Confidence: **99.34%**
691. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/promo/PromoInputsListener.kt`** -> AI Confidence: **99.34%**
692. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/DefaultIgnoredConfigurationInputsTest.kt`** -> AI Confidence: **99.34%**
693. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/InputTrackingStateTest.kt`** -> AI Confidence: **99.34%**
694. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/serialization/codecs/UserTypesCodecTest.kt`** -> AI Confidence: **99.34%**
695. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/configuration/problems/DecoratedReportProblem.kt`** -> AI Confidence: **99.34%**
696. **`platforms/core-configuration/core-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/core/FileSystemExtensions.kt`** -> AI Confidence: **99.34%**
697. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/WorkNodeActionCodec.kt`** -> AI Confidence: **99.34%**
698. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/jos/ReadResolveCache.kt`** -> AI Confidence: **99.34%**
699. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/CodeAnalyzer.kt`** -> AI Confidence: **99.34%**
700. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/Resolver.kt`** -> AI Confidence: **99.34%**
701. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/MutationAsTextRunner.kt`** -> AI Confidence: **99.34%**
702. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/writing/CanonicalDocumentTextGenerator.kt`** -> AI Confidence: **99.34%**
703. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/writing/MutatedDocumentTextGenerator.kt`** -> AI Confidence: **99.34%**
704. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/writing/TextPreservingTree.kt`** -> AI Confidence: **99.34%**
705. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/intrinsics/IntrinsicTopLevelFunctionBridge.kt`** -> AI Confidence: **99.34%**
706. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/Parser.kt`** -> AI Confidence: **99.34%**
707. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/DefaultSchemaBuildingFailure.kt`** -> AI Confidence: **99.34%**
708. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/schemaBuildingUtils.kt`** -> AI Confidence: **99.34%**
709. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/FunctionOverloadResolutionTest.kt`** -> AI Confidence: **99.34%**
710. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/LambdaTest.kt`** -> AI Confidence: **99.34%**
711. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/DomTest.kt`** -> AI Confidence: **99.34%**
712. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/conversion/DefaultEvaluationAndConversionSchema.kt`** -> AI Confidence: **99.34%**
713. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/defaults/ModelDefaultsDefinitionHandler.kt`** -> AI Confidence: **99.34%**
714. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/defaults/ModelDefaultsDocumentTransformation.kt`** -> AI Confidence: **99.34%**
715. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/defaults/ModelDefaultsResolutionProcessor.kt`** -> AI Confidence: **99.34%**
716. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/runner/EvaluationResult.kt`** -> AI Confidence: **99.34%**
717. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/DefaultComponentArtifactsResultCodec.kt`** -> AI Confidence: **99.34%**
718. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/DefaultUnresolvedComponentResultCodec.kt`** -> AI Confidence: **99.34%**
719. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/PublishArtifactLocalArtifactMetadataCodec.kt`** -> AI Confidence: **99.34%**
720. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/ResolveArtifactNodeCodec.kt`** -> AI Confidence: **99.34%**
721. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/TransformChainCodec.kt`** -> AI Confidence: **99.34%**
722. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/BeanPropertyExtensions.kt`** -> AI Confidence: **99.34%**
723. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Running.kt`** -> AI Confidence: **99.34%**
724. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/codecs/DelegatingCodec.kt`** -> AI Confidence: **99.34%**
725. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/codecs/NotImplementedCodec.kt`** -> AI Confidence: **99.34%**
726. **`platforms/core-configuration/guava-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/guava/ImmutableListCodec.kt`** -> AI Confidence: **99.34%**
727. **`platforms/core-configuration/guava-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/guava/ImmutableMapCodec.kt`** -> AI Confidence: **99.34%**
728. **`platforms/core-configuration/guava-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/guava/ImmutableSetCodec.kt`** -> AI Confidence: **99.34%**
729. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinDslAssignmentIntegrationTest.kt`** -> AI Confidence: **99.34%**
730. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinDslIntellijPlatformIntegrationTest.kt`** -> AI Confidence: **99.34%**
731. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/SettingsSchemaAccessorsIntegrationTest.kt`** -> AI Confidence: **99.34%**
732. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/dsl/KotlinDslPluginForOldestKotlinVersionTest.kt`** -> AI Confidence: **99.34%**
733. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/precompiled/PrecompiledScriptPluginAccessorSettingEvaluationTest.kt`** -> AI Confidence: **99.34%**
734. **`platforms/core-configuration/kotlin-dsl-plugins/src/test/kotlin/org/gradle/kotlin/dsl/plugins/dsl/ExperimentalCompilerWarningSilencerTest.kt`** -> AI Confidence: **99.34%**
735. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/PrecompiledScriptException.kt`** -> AI Confidence: **99.34%**
736. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/EditorReportsBuilder.kt`** -> AI Confidence: **99.34%**
737. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/BuildOperationsAssertions.kt`** -> AI Confidence: **99.34%**
738. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/BuildScriptCompileAvoidanceIntegrationTest.kt`** -> AI Confidence: **99.34%**
739. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/ExtraPropertiesExtensions.kt`** -> AI Confidence: **99.34%**
740. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/GroovyInteroperability.kt`** -> AI Confidence: **99.34%**
741. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/CodeGenerator.kt`** -> AI Confidence: **99.34%**
742. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/ProjectSchemaProvider.kt`** -> AI Confidence: **99.34%**
743. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/LexerTest.kt`** -> AI Confidence: **99.34%**
744. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/ParserToCompilerTest.kt`** -> AI Confidence: **99.34%**
745. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/resolver/ConcurrentGroupingQueueTest.kt`** -> AI Confidence: **99.34%**
746. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/resolver/ProjectRootOfTest.kt`** -> AI Confidence: **99.34%**
747. **`platforms/core-configuration/project-features/src/main/kotlin/org/gradle/features/internal/binding/TargetTypeInformationChecks.kt`** -> AI Confidence: **99.34%**
748. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/EnumCodec.kt`** -> AI Confidence: **99.34%**
749. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/HashSetCodec.kt`** -> AI Confidence: **99.34%**
750. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/MethodCodec.kt`** -> AI Confidence: **99.34%**
751. **`settings.gradle.kts`** -> AI Confidence: **99.34%**
752. **`testing/performance/src/templates/kts-project-with-source/build.gradle.kts`** -> AI Confidence: **99.34%**
753. **`testing/soak/src/integTest/kotlin/org/gradle/kotlin/dsl/caching/fixtures/KotlinDslCacheFixtures.kt`** -> AI Confidence: **99.34%**
754. **`platforms/core-configuration/base-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/TaskGraphIntegrationTest.groovy`** -> AI Confidence: **99.34%**
755. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheDebugLogIntegrationTest.groovy`** -> AI Confidence: **99.34%**
756. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheIncompatibleTasksIntegrationTest.groovy`** -> AI Confidence: **99.34%**
757. **`platforms/core-configuration/configuration-cache/src/test/groovy/org/gradle/internal/buildtree/BuildModelParametersProviderTest.groovy`** -> AI Confidence: **99.34%**
758. **`platforms/core-execution/execution-e2e-tests/src/integTest/groovy/org/gradle/integtests/ParallelProjectExecutionIntegrationTest.groovy`** -> AI Confidence: **99.34%**
759. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/classloader/FilteringClassLoaderTest.groovy`** -> AI Confidence: **99.34%**
760. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/util/PathTest.groovy`** -> AI Confidence: **99.34%**
761. **`platforms/core-runtime/build-configuration/src/test/groovy/org/gradle/internal/buildconfiguration/DaemonJvmPropertiesAccessorTest.groovy`** -> AI Confidence: **99.34%**
762. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/continuous/SmokeContinuousIntegrationTest.groovy`** -> AI Confidence: **99.34%**
763. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/taskgrouping/AbstractBasicGroupedTaskLoggingFunctionalTest.groovy`** -> AI Confidence: **99.34%**
764. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeMultipleCppProjectIntegrationTest.groovy`** -> AI Confidence: **99.34%**
765. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeSingleCppProjectIntegrationTest.groovy`** -> AI Confidence: **99.34%**
766. **`platforms/ide/ide-plugins/src/integTest/groovy/org/gradle/plugins/ide/eclipse/EclipseWtpModelIntegrationTest.groovy`** -> AI Confidence: **99.34%**
767. **`platforms/ide/ide-plugins/src/integTest/groovy/org/gradle/plugins/ide/idea/CompositeBuildIdeaProjectIntegrationTest.groovy`** -> AI Confidence: **99.34%**
768. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/eclipse/EclipseWtpPluginTest.groovy`** -> AI Confidence: **99.34%**
769. **`platforms/ide/ide/src/integTest/groovy/org/gradle/plugins/ide/idea/IdeaJavaLanguageSettingsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
770. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r76/TestLauncherTestSpecCrossVersionSpec.groovy`** -> AI Confidence: **99.34%**
771. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r82/TestLauncherTestSpecCrossVersionSpec.groovy`** -> AI Confidence: **99.34%**
772. **`platforms/jvm/jacoco/src/integTest/groovy/org/gradle/testing/jacoco/plugins/JacocoPluginIntegrationTest.groovy`** -> AI Confidence: **99.34%**
773. **`platforms/jvm/java-platform/src/integTest/groovy/org/gradle/integtests/resolve/platforms/NativeAlignmentWithJavaPlatformResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
774. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/javadoc/JavadocWorkAvoidanceIntegrationTest.groovy`** -> AI Confidence: **99.34%**
775. **`platforms/jvm/plugins-groovy/src/integTest/groovy/org/gradle/groovy/GroovyJavaLibraryInteractionIntegrationTest.groovy`** -> AI Confidence: **99.34%**
776. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/java/JavaProjectOutgoingVariantsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
777. **`platforms/jvm/plugins-jvm-test-fixtures/src/testFixtures/groovy/org/gradle/java/fixtures/AbstractJavaProjectTestFixturesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
778. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/UpToDateScalaCompileIntegrationTest.groovy`** -> AI Confidence: **99.34%**
779. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testsuites/dependencies/TestSuitesGroovyDSLDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
780. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppIncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.34%**
781. **`platforms/native/language-native/src/integTest/groovy/org/gradle/swiftpm/SwiftPackageManagerSwiftBuildExportIntegrationTest.groovy`** -> AI Confidence: **99.34%**
782. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/LibraryBinariesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
783. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/LibraryDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
784. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/PrebuiltLibrariesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
785. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ModuleDependencyExcludeResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
786. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ProjectDependencyResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
787. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/RepositoryInteractionDependencyResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
788. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ResolutionIssuesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
789. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/alignment/ForcingPlatformAlignmentTest.groovy`** -> AI Confidence: **99.34%**
790. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/MultiStringDependencyNotationIntegrationTest.groovy`** -> AI Confidence: **99.34%**
791. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/UnsupportedConfigurationMutationTest.groovy`** -> AI Confidence: **99.34%**
792. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/DependenciesAttributesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
793. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/MultipleVariantSelectionIntegrationTest.groovy`** -> AI Confidence: **99.34%**
794. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/bundling/JavaBundlingResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
795. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/capabilities/CapabilitiesConflictResolutionIssuesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
796. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/constraints/DependencyConstraintsAndResolutionStrategiesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
797. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyDynamicRevisionResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
798. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/locking/AbstractLockingIntegrationTest.groovy`** -> AI Confidence: **99.34%**
799. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/AbstractDependencyMetadataRulesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
800. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/ComponentAttributesRulesIntegrationTest.groovy`** -> AI Confidence: **99.34%**
801. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/strict/EndorseStrictVersionsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
802. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/strict/StrictVersionConstraintsFeatureInteractionIntegrationTest.groovy`** -> AI Confidence: **99.34%**
803. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformInputArtifactIntegrationTest.groovy`** -> AI Confidence: **99.34%**
804. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/validation/GradleMetadataValidationResolveIntegrationTest.groovy`** -> AI Confidence: **99.34%**
805. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationWritingIntegTest.groovy`** -> AI Confidence: **99.34%**
806. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/versions/AbstractRichVersionConstraintsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
807. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/local/model/DefaultLibraryComponentSelectorTest.groovy`** -> AI Confidence: **99.34%**
808. **`platforms/software/ivy/src/integTest/groovy/org/gradle/api/publish/ivy/IvyPublishJavaIntegTest.groovy`** -> AI Confidence: **99.34%**
809. **`platforms/software/resources-sftp/src/integTest/groovy/org/gradle/integtests/resolve/resource/sftp/ivy/IvySftpRepoErrorsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
810. **`platforms/software/resources/src/test/groovy/org/gradle/internal/resource/ExternalResourceNameTest.groovy`** -> AI Confidence: **99.34%**
811. **`platforms/software/software-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/DependencyInsightReportTaskIntegrationTest.groovy`** -> AI Confidence: **99.34%**
812. **`platforms/software/version-control/src/integTest/groovy/org/gradle/vcs/internal/GitVersionSelectionIntegrationTest.groovy`** -> AI Confidence: **99.34%**
813. **`platforms/software/version-control/src/integTest/groovy/org/gradle/vcs/internal/NestedSourceDependencyIntegrationTest.groovy`** -> AI Confidence: **99.34%**
814. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildCommandLineArgsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
815. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildEventsIntegrationTest.groovy`** -> AI Confidence: **99.34%**
816. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/changedetection/state/TaskEnumTypesInputPropertyIntegrationTest.groovy`** -> AI Confidence: **99.34%**
817. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/AbstractPathSensitivityIntegrationSpec.groovy`** -> AI Confidence: **99.34%**
818. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/DeleteTaskIntegrationTest.groovy`** -> AI Confidence: **99.34%**
819. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/AntProjectIntegrationTest.groovy`** -> AI Confidence: **99.34%**
820. **`testing/internal-integ-testing/src/test/groovy/org/gradle/integtests/fixtures/configurationcache/ConfigurationCacheProblemsFixtureTest.groovy`** -> AI Confidence: **99.34%**
821. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/AndroidProjectCachingSmokeTest.groovy`** -> AI Confidence: **99.34%**
822. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/GradleBuildDocumentationConfigurationCacheSmokeTest.groovy`** -> AI Confidence: **99.34%**
823. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/WithAndroidDeprecations.groovy`** -> AI Confidence: **99.34%**
824. **`.teamcity/src/main/kotlin/common/BuildScanUtils.kt`** -> AI Confidence: **99.32%**
825. **`.teamcity/src/main/kotlin/model/FunctionalTestBucketModel.kt`** -> AI Confidence: **99.32%**
826. **`.teamcity/src/main/kotlin/model/PerformanceTestSpec.kt`** -> AI Confidence: **99.32%**
827. **`.teamcity/src/main/kotlin/promotion/PublishNightlyDocumentation.kt`** -> AI Confidence: **99.32%**
828. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/kotlindsl/kotlin-dsl-upstream-candidates.kt`** -> AI Confidence: **99.32%**
829. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/JSpecifyNullabilityChangesTest.kt`** -> AI Confidence: **99.32%**
830. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/RichReportScrapper.kt`** -> AI Confidence: **99.32%**
831. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/CheckContributorsInReleaseNotes.kt`** -> AI Confidence: **99.32%**
832. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/CheckSubprojectsInfo.kt`** -> AI Confidence: **99.32%**
833. **`build-logic/buildquality/src/main/kotlin/gradlebuild/incubation/action/IncubatingApiReportAggregationWorkAction.kt`** -> AI Confidence: **99.32%**
834. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/androidhomewarmup/AndroidHomeWarmupExtension.kt`** -> AI Confidence: **99.32%**
835. **`build-logic/packaging/src/main/kotlin/gradlebuild.no-module-annotation.gradle.kts`** -> AI Confidence: **99.32%**
836. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/support/FileLinesValueSource.kt`** -> AI Confidence: **99.32%**
837. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/support/PomLicenseUtils.kt`** -> AI Confidence: **99.32%**
838. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareBuildTreeModelCreator.kt`** -> AI Confidence: **99.32%**
839. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ExecutionAccessChecker.kt`** -> AI Confidence: **99.32%**
840. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/barrier/BarrierAwareBuildTreeWorkPreparer.kt`** -> AI Confidence: **99.32%**
841. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/heap/HeapDumper.kt`** -> AI Confidence: **99.32%**
842. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/services/DeferredRootBuildGradle.kt`** -> AI Confidence: **99.32%**
843. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/configuration/problems/HtmlReportTemplateLoader.kt`** -> AI Confidence: **99.32%**
844. **`platforms/core-configuration/core-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/core/ProjectExtensions.kt`** -> AI Confidence: **99.32%**
845. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/TypeDiscovery.kt`** -> AI Confidence: **99.32%**
846. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/util.kt`** -> AI Confidence: **99.32%**
847. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/MemoizedInterpretationSchemaBuilder.kt`** -> AI Confidence: **99.32%**
848. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/plugins/PluginsBlockSchema.kt`** -> AI Confidence: **99.32%**
849. **`platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/EnvironmentVarKeySource.kt`** -> AI Confidence: **99.32%**
850. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Identities.kt`** -> AI Confidence: **99.32%**
851. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PrecompiledScriptPluginVersionCatalogIntegrationTest.kt`** -> AI Confidence: **99.32%**
852. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/test/kotlin/org/gradle/kotlin/dsl/tooling/builders/CommonListPrefixTest.kt`** -> AI Confidence: **99.32%**
853. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/ContentFilterableExtensions.kt`** -> AI Confidence: **99.32%**
854. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/ExtensionContainerExtensions.kt`** -> AI Confidence: **99.32%**
855. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/PluginAwareExtensions.kt`** -> AI Confidence: **99.32%**
856. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/ProgramId.kt`** -> AI Confidence: **99.32%**
857. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/KotlinCompilerOptions.kt`** -> AI Confidence: **99.32%**
858. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/LinePreservingSubstringTest.kt`** -> AI Confidence: **99.32%**
859. **`platforms/core-configuration/stdlib-kotlin-extensions/src/test/kotlin/org/gradle/internal/extensions/stdlib/ThreadLocalExtensionsTest.kt`** -> AI Confidence: **99.32%**
860. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheIncludedBuildLogicIntegrationTest.groovy`** -> AI Confidence: **99.32%**
861. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsAccessFromGroovyDslIntegrationTest.groovy`** -> AI Confidence: **99.32%**
862. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
863. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeMultipleProjectIntegrationTest.groovy`** -> AI Confidence: **99.32%**
864. **`platforms/ide/ide/src/integTest/groovy/org/gradle/plugins/ide/idea/IdeaCompositeBuildIntegrationTest.groovy`** -> AI Confidence: **99.32%**
865. **`platforms/jvm/plugins-application/src/integTest/groovy/org/gradle/java/JavaApplicationOutgoingVariantsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
866. **`platforms/jvm/plugins-java-library/src/integTest/groovy/org/gradle/java/JavaLibraryCrossProjectTargetJvmVersionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
867. **`platforms/jvm/plugins-java-library/src/integTest/groovy/org/gradle/java/JavaLibraryDocumentationIntegrationTest.groovy`** -> AI Confidence: **99.32%**
868. **`platforms/jvm/plugins-java-library/src/integTest/groovy/org/gradle/java/JavaLibraryPublishedTargetJvmEnvironmentIntegrationTest.groovy`** -> AI Confidence: **99.32%**
869. **`platforms/jvm/plugins-java-library/src/integTest/groovy/org/gradle/java/JavaLibraryPublishedTargetJvmVersionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
870. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftDependenciesCppInteroperabilityIntegrationTest.groovy`** -> AI Confidence: **99.32%**
871. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftIncrementalCppInteroperabilityIntegrationTest.groovy`** -> AI Confidence: **99.32%**
872. **`platforms/native/language-native/src/integTest/groovy/org/gradle/swiftpm/SwiftPackageManagerCppBuildExportIntegrationTest.groovy`** -> AI Confidence: **99.32%**
873. **`platforms/native/platform-native/src/test/groovy/org/gradle/nativeplatform/platform/internal/ReadelfBinaryInfoTest.groovy`** -> AI Confidence: **99.32%**
874. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/internal/component/resolution/failure/ModuleRejectedIncompatibleConstraintsFailureDescriberIntegrationTest.groovy`** -> AI Confidence: **99.32%**
875. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/DirectoryOutputArtifactIntegrationTest.groovy`** -> AI Confidence: **99.32%**
876. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ProjectDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.32%**
877. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/PublishedRichVersionConstraintsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
878. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/VariantsDependencySubstitutionRulesIntegrationTest.groovy`** -> AI Confidence: **99.32%**
879. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ResolvedConfigurationApiIntegrationTest.groovy`** -> AI Confidence: **99.32%**
880. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/AbstractConfigurationAttributesResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
881. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/CrossProjectMultipleVariantSelectionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
882. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/capabilities/CapabilitiesConflictResolutionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
883. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/capabilities/CapabilitiesUseCasesIntegrationTest.groovy`** -> AI Confidence: **99.32%**
884. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/capabilities/PublishedCapabilitiesIntegrationTest.groovy`** -> AI Confidence: **99.32%**
885. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/capabilities/PublishedCapabilityRequestsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
886. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/constraints/DependencyConstraintsBugsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
887. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/features/FeaturesResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
888. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/ComponentSelectionRulesDependencyResolveIntegTest.groovy`** -> AI Confidence: **99.32%**
889. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/ComponentSelectionRulesErrorHandlingIntegTest.groovy`** -> AI Confidence: **99.32%**
890. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyGradleMetadataRedirectionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
891. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/ClassifierToVariantResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
892. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenDependencyResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
893. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenGradleMetadataRedirectionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
894. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenLocalDependencyWithGradleMetadataResolutionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
895. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenVersionRangeResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
896. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/override/ComponentOverrideMetadataResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
897. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/reproducibility/FailOnChangingVersionsResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
898. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/reproducibility/FailOnDynamicVersionsResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
899. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/VariantAttributesRulesIntegrationTest.groovy`** -> AI Confidence: **99.32%**
900. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/VariantFilesMetadataRulesIntegrationTest.groovy`** -> AI Confidence: **99.32%**
901. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/strict/StrictVersionConstraintsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
902. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/suppliers/CustomVersionListerIntegrationTest.groovy`** -> AI Confidence: **99.32%**
903. **`platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/MavenPublishPomCustomizationIntegTest.groovy`** -> AI Confidence: **99.32%**
904. **`platforms/software/software-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/BuildEnvironmentReportTaskIntegrationTest.groovy`** -> AI Confidence: **99.32%**
905. **`platforms/software/version-control/src/integTest/groovy/org/gradle/vcs/internal/NestedSourceDependencyIdentityIntegrationTest.groovy`** -> AI Confidence: **99.32%**
906. **`platforms/software/version-control/src/integTest/groovy/org/gradle/vcs/internal/SourceDependencyIdentityIntegrationTest.groovy`** -> AI Confidence: **99.32%**
907. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildConfigurationTimeResolveIntegrationTest.groovy`** -> AI Confidence: **99.32%**
908. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildContinueOnSingleFailureIntegrationTest.groovy`** -> AI Confidence: **99.32%**
909. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildDeclaredSubstitutionsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
910. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildDependencyCycleIntegrationTest.groovy`** -> AI Confidence: **99.32%**
911. **`subprojects/core-api/src/test/groovy/org/gradle/api/internal/provider/views/MapPropertyMapViewTest.groovy`** -> AI Confidence: **99.32%**
912. **`subprojects/core/src/integTest/groovy/org/gradle/api/invocation/GradleLifecycleBeforeProjectEagerExecutionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
913. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/options/MultipleTaskOptionsIntegrationTest.groovy`** -> AI Confidence: **99.32%**
914. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/buildsrc/BuildSrcTaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.32%**
915. **`subprojects/core/src/test/groovy/org/gradle/api/internal/project/NewDefaultProjectTest.groovy`** -> AI Confidence: **99.32%**
916. **`testing/internal-integ-testing/src/test/groovy/org/gradle/integtests/fixtures/logging/NativeComponentReportOutputNormalizerTest.groovy`** -> AI Confidence: **99.32%**
917. **`testing/internal-integ-testing/src/test/groovy/org/gradle/integtests/fixtures/logging/ZincScalaCompilerOutputNormalizerTest.groovy`** -> AI Confidence: **99.32%**
918. **`testing/performance/src/templates/cpp-source/exe.cpp`** -> AI Confidence: **99.32%**
919. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-linked_ptr.h`** -> AI Confidence: **99.32%**
920. **`build-logic/cleanup/src/main/java/gradlebuild/cleanup/services/KillLeakingJavaProcesses.java`** -> AI Confidence: **99.31%**
921. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/configuration/TaskDetailPrinter.java`** -> AI Confidence: **99.31%**
922. **`platforms/core-configuration/java-api-extractor/src/main/java/org/gradle/internal/tools/api/impl/JavaApiMemberWriter.java`** -> AI Confidence: **99.31%**
923. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/OrElseValueProducer.java`** -> AI Confidence: **99.31%**
924. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/DefaultTaskDependency.java`** -> AI Confidence: **99.31%**
925. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/DependencyInjectingInstantiator.java`** -> AI Confidence: **99.31%**
926. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/properties/annotations/AbstractTypeMetadataWalker.java`** -> AI Confidence: **99.31%**
927. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/AbstractValueProcessor.java`** -> AI Confidence: **99.31%**
928. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/SnapshotSerializer.java`** -> AI Confidence: **99.31%**
929. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/ModelTypeInitializationException.java`** -> AI Confidence: **99.31%**
930. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/FormattingValidationProblemCollector.java`** -> AI Confidence: **99.31%**
931. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/ModelRuleExtractor.java`** -> AI Confidence: **99.31%**
932. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/binding/DefaultStructBindingsStore.java`** -> AI Confidence: **99.31%**
933. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/cache/ModelSchemaCache.java`** -> AI Confidence: **99.31%**
934. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/StructSchemaExtractionStrategySupport.java`** -> AI Confidence: **99.31%**
935. **`platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/model/internal/fixture/ModelActionBuilder.java`** -> AI Confidence: **99.31%**
936. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/ClassInspector.java`** -> AI Confidence: **99.31%**
937. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/Types.java`** -> AI Confidence: **99.31%**
938. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/annotations/impl/DefaultTypeAnnotationMetadataStore.java`** -> AI Confidence: **99.31%**
939. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/validation/DefaultTypeAwareProblemBuilder.java`** -> AI Confidence: **99.31%**
940. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/FingerprintMapSerializer.java`** -> AI Confidence: **99.31%**
941. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/ExecuteWorkBuildOperationFiringStep.java`** -> AI Confidence: **99.31%**
942. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/RemovePreviousOutputsStep.java`** -> AI Confidence: **99.31%**
943. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/DefaultFileWatcherProbeRegistry.java`** -> AI Confidence: **99.31%**
944. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/LockOnDemandCrossProcessCacheAccess.java`** -> AI Confidence: **99.31%**
945. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/LockOnDemandEagerReleaseCrossProcessCacheAccess.java`** -> AI Confidence: **99.31%**
946. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/reflect/DirectInstantiator.java`** -> AI Confidence: **99.31%**
947. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/util/NumberUtil.java`** -> AI Confidence: **99.31%**
948. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/work/DefaultConditionalExecutionQueue.java`** -> AI Confidence: **99.31%**
949. **`platforms/core-runtime/base-services/src/main/java/org/gradle/util/internal/TextUtil.java`** -> AI Confidence: **99.31%**
950. **`platforms/core-runtime/build-operations-trace/src/main/java/org/gradle/internal/operations/trace/BuildOperationRecord.java`** -> AI Confidence: **99.31%**
951. **`platforms/core-runtime/concurrent/src/main/java/org/gradle/internal/concurrent/MultiProducerSingleConsumerProcessor.java`** -> AI Confidence: **99.31%**
952. **`platforms/core-runtime/files/src/main/java/org/gradle/internal/file/nio/PosixFilePermissionConverter.java`** -> AI Confidence: **99.31%**
953. **`platforms/core-runtime/groovy-loader/src/main/java/org/gradle/internal/groovyloader/ClassInfoCleaningGroovySystemLoader.java`** -> AI Confidence: **99.31%**
954. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/extensions/property/PropertyUpgradeClassSourceGenerator.java`** -> AI Confidence: **99.31%**
955. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/JavadocUtils.java`** -> AI Confidence: **99.31%**
956. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/groovy/CodeGeneratingSignatureTreeVisitor.java`** -> AI Confidence: **99.31%**
957. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/FileSystemWatchingBuildActionRunner.java`** -> AI Confidence: **99.31%**
958. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/continuous/FileEventCollector.java`** -> AI Confidence: **99.31%**
959. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/BuildStatusRenderer.java`** -> AI Confidence: **99.31%**
960. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/ConsoleConfigureAction.java`** -> AI Confidence: **99.31%**
961. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/OutputEventTransformer.java`** -> AI Confidence: **99.31%**
962. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/ProgressLogEventGenerator.java`** -> AI Confidence: **99.31%**
963. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/text/TreeFormatter.java`** -> AI Confidence: **99.31%**
964. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/dispatch/AsyncDispatch.java`** -> AI Confidence: **99.31%**
965. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/event/AbstractBroadcastDispatch.java`** -> AI Confidence: **99.31%**
966. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/hub/MessageHub.java`** -> AI Confidence: **99.31%**
967. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/filesystem/services/NativePlatformBackedFileMetadataAccessor.java`** -> AI Confidence: **99.31%**
968. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/jansi/JansiBootPathConfigurer.java`** -> AI Confidence: **99.31%**
969. **`platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/util/MergeOptionsUtil.java`** -> AI Confidence: **99.31%**
970. **`platforms/core-runtime/serialization/src/main/java/org/gradle/internal/serialize/DefaultSerializerRegistry.java`** -> AI Confidence: **99.31%**
971. **`platforms/core-runtime/serialization/src/main/java/org/gradle/internal/serialize/ExceptionPlaceholder.java`** -> AI Confidence: **99.31%**
972. **`platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/ServiceScopeValidator.java`** -> AI Confidence: **99.31%**
973. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/tasks/internal/ValidationProblemSerialization.java`** -> AI Confidence: **99.31%**
974. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/Project.java`** -> AI Confidence: **99.31%**
975. **`platforms/ide/problems-rendering/src/main/java/org/gradle/problems/internal/rendering/ProblemBodyWriter.java`** -> AI Confidence: **99.31%**
976. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/adapter/TypeInspector.java`** -> AI Confidence: **99.31%**
977. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/async/ServiceLifecycle.java`** -> AI Confidence: **99.31%**
978. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/ToolingParameterProxy.java`** -> AI Confidence: **99.31%**
979. **`platforms/jvm/antlr/src/main/java/org/gradle/api/plugins/antlr/internal/antlr2/GenerationPlanBuilder.java`** -> AI Confidence: **99.31%**
980. **`platforms/jvm/code-quality-workers/src/main/java/org/gradle/api/plugins/quality/internal/PmdInvoker.java`** -> AI Confidence: **99.31%**
981. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/JavaCompilerArgumentsBuilder.java`** -> AI Confidence: **99.31%**
982. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/deps/ClassSetAnalysisData.java`** -> AI Confidence: **99.31%**
983. **`platforms/jvm/scala/src/main/java/org/gradle/api/tasks/scala/internal/ScalaCompileOptionsConfigurer.java`** -> AI Confidence: **99.31%**
984. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/junit/CategoryFilter.java`** -> AI Confidence: **99.31%**
985. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/sourceparser/AbstractExpression.java`** -> AI Confidence: **99.31%**
986. **`platforms/native/language-native/src/main/java/org/gradle/swiftpm/tasks/GenerateSwiftPackageManagerManifest.java`** -> AI Confidence: **99.31%**
987. **`platforms/software/build-init-specs/src/main/java/org/gradle/buildinit/specs/internal/BuildInitSpecRegistry.java`** -> AI Confidence: **99.31%**
988. **`platforms/software/build-init/src/main/java/org/gradle/api/tasks/wrapper/internal/GradleVersionResolver.java`** -> AI Confidence: **99.31%**
989. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/JvmApplicationProjectInitDescriptor.java`** -> AI Confidence: **99.31%**
990. **`platforms/software/build-init/src/main/java/org/gradle/unexported/buildinit/plugins/internal/maven/Maven2Gradle.java`** -> AI Confidence: **99.31%**
991. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/AbstractJVMVersionTooNewFailureDescriber.java`** -> AI Confidence: **99.31%**
992. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/ComponentSelectionRulesProcessor.java`** -> AI Confidence: **99.31%**
993. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/GradleModuleMetadataParser.java`** -> AI Confidence: **99.31%**
994. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/PomDomParser.java`** -> AI Confidence: **99.31%**
995. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/report/DependencyVerificationReportWriter.java`** -> AI Confidence: **99.31%**
996. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/writer/PgpKeyGrouper.java`** -> AI Confidence: **99.31%**
997. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/factories/Unions.java`** -> AI Confidence: **99.31%**
998. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/DependencyGraphPathResolver.java`** -> AI Confidence: **99.31%**
999. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/ComponentRejectedMessageBuilder.java`** -> AI Confidence: **99.31%**
1000. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/DependencyGraphBuilder.java`** -> AI Confidence: **99.31%**
1001. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/CapabilityConflictResolver.java`** -> AI Confidence: **99.31%**
1002. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ComponentIdentifierSerializer.java`** -> AI Confidence: **99.31%**
1003. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlReader.java`** -> AI Confidence: **99.31%**
1004. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/verifier/DependencyVerifier.java`** -> AI Confidence: **99.31%**
1005. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/immutable/ImmutableAttributesSchema.java`** -> AI Confidence: **99.31%**
1006. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/immutable/artifact/ImmutableArtifactTypeRegistry.java`** -> AI Confidence: **99.31%**
1007. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/matching/DefaultAttributeSelectionSchema.java`** -> AI Confidence: **99.31%**
1008. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/DependencyMapNotationConverter.java`** -> AI Confidence: **99.31%**
1009. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/DefaultConfigurationMetadata.java`** -> AI Confidence: **99.31%**
1010. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ivy/IvyConfigurationHelper.java`** -> AI Confidence: **99.31%**
1011. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ivy/IvyDependencyDescriptor.java`** -> AI Confidence: **99.31%**
1012. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/AbstractResolutionFailureDescriber.java`** -> AI Confidence: **99.31%**
1013. **`platforms/software/platform-base/src/main/java/org/gradle/language/base/internal/model/BinarySourceTransformations.java`** -> AI Confidence: **99.31%**
1014. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/registry/ModelMapBasedRule.java`** -> AI Confidence: **99.31%**
1015. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/ApacheDirectoryListingParser.java`** -> AI Confidence: **99.31%**
1016. **`platforms/software/resources/src/main/java/org/gradle/internal/resource/ExternalResourceName.java`** -> AI Confidence: **99.31%**
1017. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/configurations/model/ConfigurationReportModelFactory.java`** -> AI Confidence: **99.31%**
1018. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/junit/result/TestEventReporterAsListener.java`** -> AI Confidence: **99.31%**
1019. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/TestTreeModel.java`** -> AI Confidence: **99.31%**
1020. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/TestState.java`** -> AI Confidence: **99.31%**
1021. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/serializable/TestOutputReader.java`** -> AI Confidence: **99.31%**
1022. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/serializable/TestOutputWriter.java`** -> AI Confidence: **99.31%**
1023. **`subprojects/core-api/src/main/java/org/gradle/api/internal/cache/CacheDirUtil.java`** -> AI Confidence: **99.31%**
1024. **`subprojects/core/src/main/java/org/gradle/api/internal/attributes/DefaultImmutableAttributesContainer.java`** -> AI Confidence: **99.31%**
1025. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/DefaultSharedModelDefaults.java`** -> AI Confidence: **99.31%**
1026. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/DefaultTaskRequiredServices.java`** -> AI Confidence: **99.31%**
1027. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/ExecuteTaskBuildOperationResult.java`** -> AI Confidence: **99.31%**
1028. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/ValidationActions.java`** -> AI Confidence: **99.31%**
1029. **`subprojects/core/src/main/java/org/gradle/api/services/internal/BuildServiceRegistryInternal.java`** -> AI Confidence: **99.31%**
1030. **`subprojects/core/src/main/java/org/gradle/execution/plan/DefaultFinalizedExecutionPlan.java`** -> AI Confidence: **99.31%**
1031. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/GradleResolveVisitor.java`** -> AI Confidence: **99.31%**
1032. **`subprojects/core/src/main/java/org/gradle/initialization/exception/DefaultExceptionAnalyser.java`** -> AI Confidence: **99.31%**
1033. **`subprojects/core/src/main/java/org/gradle/internal/operations/DefaultBuildOperationQueue.java`** -> AI Confidence: **99.31%**
1034. **`subprojects/core/src/main/java/org/gradle/internal/work/DefaultAsyncWorkTracker.java`** -> AI Confidence: **99.31%**
1035. **`subprojects/core/src/main/java/org/gradle/plugin/use/internal/PluginUseScriptBlockMetadataCompiler.java`** -> AI Confidence: **99.31%**
1036. **`subprojects/core/src/main/java/org/gradle/util/internal/NameMatcher.java`** -> AI Confidence: **99.31%**
1037. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/compatibility/AbstractContextualMultiVersionTestInterceptor.java`** -> AI Confidence: **99.31%**
1038. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/daemon/DaemonContextParser.java`** -> AI Confidence: **99.31%**
1039. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/OutputScrapingExecutionFailure.java`** -> AI Confidence: **99.31%**
1040. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/ResultAssertion.java`** -> AI Confidence: **99.31%**
1041. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/logging/GroupedOutputFixture.java`** -> AI Confidence: **99.31%**
1042. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/logging/comparison/DiffUtils.java`** -> AI Confidence: **99.31%**
1043. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/ChainingHttpHandler.java`** -> AI Confidence: **99.31%**
1044. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/ExpectMaxNConcurrentRequests.java`** -> AI Confidence: **99.31%**
1045. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/SendPartialResponseThenBlock.java`** -> AI Confidence: **99.31%**
1046. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/measure/DataSeries.java`** -> AI Confidence: **99.31%**
1047. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/BaseCrossBuildResultsStore.java`** -> AI Confidence: **99.31%**
1048. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/AbstractTablePageGenerator.java`** -> AI Confidence: **99.31%**
1049. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/DefaultPerformanceExecutionDataProvider.java`** -> AI Confidence: **99.31%**
1050. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/IndexPageGenerator.java`** -> AI Confidence: **99.31%**
1051. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/tasks/GeneratePrecompiledScriptPluginAccessors.kt`** -> AI Confidence: **99.31%**
1052. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/resolver/KotlinScriptDependenciesResolverTest.kt`** -> AI Confidence: **99.31%**
1053. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/ResidualProgramCompilerTest.kt`** -> AI Confidence: **99.31%**
1054. **`build-logic/binary-compatibility/src/test/groovy/gradlebuild/binarycompatibility/PublicAPIRulesTest.groovy`** -> AI Confidence: **99.31%**
1055. **`build-logic/performance-testing/src/main/groovy/gradlebuild.performance-templates.gradle`** -> AI Confidence: **99.31%**
1056. **`build-logic/performance-testing/src/main/groovy/gradlebuild/performance/generator/tasks/AbstractProjectGeneratorTask.groovy`** -> AI Confidence: **99.31%**
1057. **`build-logic/performance-testing/src/main/groovy/gradlebuild/performance/generator/tasks/JvmProjectGeneratorTask.groovy`** -> AI Confidence: **99.31%**
1058. **`platforms/core-configuration/base-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/ProjectReportTaskIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1059. **`platforms/core-configuration/base-diagnostics/src/test/groovy/org/gradle/api/tasks/diagnostics/internal/TextReportRendererSpec.groovy`** -> AI Confidence: **99.31%**
1060. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1061. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheBuildServiceIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1062. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheEncryptionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1063. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheSupportedTypesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1064. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/fixtures/BuildLogicChangeFixture.groovy`** -> AI Confidence: **99.31%**
1065. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/process/ProcessInTransformIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1066. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/undeclared/MethodReferenceInstrumentationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1067. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/inputs/undeclared/UndeclaredBuildInputsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1068. **`platforms/core-configuration/declarative-dsl-provider/src/integTest/groovy/org/gradle/internal/declarativedsl/agp/DeclarativeAgpSmokeSpec.groovy`** -> AI Confidence: **99.31%**
1069. **`platforms/core-configuration/declarative-dsl-tooling-builders/src/crossVersionTest/groovy/org/gradle/declarative/dsl/tooling/builders/r814/AndroidEcosystemPrototypeCrossVersionTest.groovy`** -> AI Confidence: **99.31%**
1070. **`platforms/core-configuration/file-collections/src/integTest/groovy/org/gradle/api/file/FileCollectionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1071. **`platforms/core-configuration/file-collections/src/test/groovy/org/gradle/api/internal/file/collections/DefaultConfigurableFileCollectionSpec.groovy`** -> AI Confidence: **99.31%**
1072. **`platforms/core-configuration/file-collections/src/test/groovy/org/gradle/api/internal/file/collections/SingleIncludePatternFileTreeSpec.groovy`** -> AI Confidence: **99.31%**
1073. **`platforms/core-configuration/input-tracking/src/test/groovy/org/gradle/internal/configuration/inputs/AccessTrackingPropertiesNonStringTest.groovy`** -> AI Confidence: **99.31%**
1074. **`platforms/core-configuration/input-tracking/src/test/groovy/org/gradle/internal/configuration/inputs/AccessTrackingPropertiesTest.groovy`** -> AI Confidence: **99.31%**
1075. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/plugins/PrecompiledKotlinPluginCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1076. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/plugins/ProjectTheExtensionCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1077. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/tooling/builders/r60/KotlinDslScriptsModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1078. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/tooling/builders/r93/GradleDslBaseScriptModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1079. **`platforms/core-configuration/model-core/src/integTest/groovy/org/gradle/model/managed/InterfaceBackedManagedTypeIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1080. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/CollectionPropertySpec.groovy`** -> AI Confidence: **99.31%**
1081. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/CredentialsProviderFactoryTest.groovy`** -> AI Confidence: **99.31%**
1082. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/sources/process/ProcessOutputValueSourceTest.groovy`** -> AI Confidence: **99.31%**
1083. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskDependencyTest.groovy`** -> AI Confidence: **99.31%**
1084. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/extensibility/DefaultExtensionContainerSpec.groovy`** -> AI Confidence: **99.31%**
1085. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/extensibility/ExtensionContainerTest.groovy`** -> AI Confidence: **99.31%**
1086. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/properties/annotations/AbstractTypeMetadataWalkerTest.groovy`** -> AI Confidence: **99.31%**
1087. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/snapshot/impl/DefaultValueSnapshotterTest.groovy`** -> AI Confidence: **99.31%**
1088. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/snapshot/impl/IsolatableSerializerRegistryTest.groovy`** -> AI Confidence: **99.31%**
1089. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/NodeBackedModelMapSpec.groovy`** -> AI Confidence: **99.31%**
1090. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/inspect/ManagedModelInitializerTest.groovy`** -> AI Confidence: **99.31%**
1091. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/inspect/ModelRuleExtractorTest.groovy`** -> AI Confidence: **99.31%**
1092. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/manage/binding/DefaultStructBindingsStoreTest.groovy`** -> AI Confidence: **99.31%**
1093. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/registry/DefaultModelRegistryTest.groovy`** -> AI Confidence: **99.31%**
1094. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/registry/RuleBindingsTest.groovy`** -> AI Confidence: **99.31%**
1095. **`platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/CircularEvaluationSpec.groovy`** -> AI Confidence: **99.31%**
1096. **`platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/PropertySpec.groovy`** -> AI Confidence: **99.31%**
1097. **`platforms/core-configuration/project-features/src/integTest/groovy/org/gradle/features/ProjectFeatureSafetyIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1098. **`platforms/core-configuration/project-features/src/integTest/groovy/org/gradle/features/ProjectTypeDeclarationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1099. **`platforms/core-execution/execution-e2e-tests/src/integTest/groovy/org/gradle/integtests/CachedKotlinTaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1100. **`platforms/core-execution/execution-e2e-tests/src/integTest/groovy/org/gradle/integtests/NestedInputKotlinImplementationTrackingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1101. **`platforms/core-execution/execution-e2e-tests/src/integTest/groovy/org/gradle/integtests/StaleOutputHistoryLossIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1102. **`platforms/core-execution/execution/src/integTest/groovy/org/gradle/internal/execution/IncrementalExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1103. **`platforms/core-execution/file-watching/src/integTest/groovy/org/gradle/internal/watch/LoggingFileSystemWatchingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1104. **`platforms/core-execution/file-watching/src/integTest/groovy/org/gradle/internal/watch/WatchedDirectoriesFileSystemWatchingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1105. **`platforms/core-execution/file-watching/src/test/groovy/org/gradle/internal/watch/vfs/impl/WatchingVirtualFileSystemTest.groovy`** -> AI Confidence: **99.31%**
1106. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/AbstractFileLockManagerTest.groovy`** -> AI Confidence: **99.31%**
1107. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/DefaultCacheBuilderTest.groovy`** -> AI Confidence: **99.31%**
1108. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/DefaultCacheFactoryTest.groovy`** -> AI Confidence: **99.31%**
1109. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/DefaultExclusiveCacheAccessCoordinatorTest.groovy`** -> AI Confidence: **99.31%**
1110. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/DefaultPersistentDirectoryCacheTest.groovy`** -> AI Confidence: **99.31%**
1111. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/FileBackedObjectHolderTest.groovy`** -> AI Confidence: **99.31%**
1112. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/LockOnDemandCrossProcessCacheAccessTest.groovy`** -> AI Confidence: **99.31%**
1113. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/LockOnDemandEagerReleaseCrossProcessCacheAccessTest.groovy`** -> AI Confidence: **99.31%**
1114. **`platforms/core-execution/snapshots/src/test/groovy/org/gradle/internal/snapshot/impl/DirectorySnapshotterStatisticsTest.groovy`** -> AI Confidence: **99.31%**
1115. **`platforms/core-execution/snapshots/src/test/groovy/org/gradle/internal/vfs/impl/DefaultSnapshotHierarchyTest.groovy`** -> AI Confidence: **99.31%**
1116. **`platforms/core-execution/worker-process-services/src/integTest/groovy/org/gradle/process/internal/WorkerProcessIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1117. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorErrorHandlingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1118. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1119. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParallelBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1120. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParallelIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1121. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParametersIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1122. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParametersKotlinIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1123. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/ActionsTest.groovy`** -> AI Confidence: **99.31%**
1124. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/SafeFileLocationUtilsTest.groovy`** -> AI Confidence: **99.31%**
1125. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/jvm/JvmTest.groovy`** -> AI Confidence: **99.31%**
1126. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/work/DefaultWorkerLeaseServiceProjectLockTest.groovy`** -> AI Confidence: **99.31%**
1127. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/util/internal/GUtilTest.groovy`** -> AI Confidence: **99.31%**
1128. **`platforms/core-runtime/build-configuration/src/test/groovy/org/gradle/internal/buildconfiguration/DaemonJvmPropertiesModifierTest.groovy`** -> AI Confidence: **99.31%**
1129. **`platforms/core-runtime/build-process-services/src/test/groovy/org/gradle/api/internal/classpath/DefaultModuleRegistryTest.groovy`** -> AI Confidence: **99.31%**
1130. **`platforms/core-runtime/build-profile/src/integTest/groovy/org/gradle/profile/ProfilingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1131. **`platforms/core-runtime/client-services/src/test/groovy/org/gradle/launcher/daemon/client/ReportDaemonStatusClientTest.groovy`** -> AI Confidence: **99.31%**
1132. **`platforms/core-runtime/daemon-protocol/src/test/groovy/org/gradle/launcher/daemon/context/DaemonCompatibilitySpecSpec.groovy`** -> AI Confidence: **99.31%**
1133. **`platforms/core-runtime/daemon-services/src/test/groovy/org/gradle/api/internal/tasks/userinput/DefaultUserInputHandlerTest.groovy`** -> AI Confidence: **99.31%**
1134. **`platforms/core-runtime/files/src/test/groovy/org/gradle/internal/file/impl/DefaultDeleterTest.groovy`** -> AI Confidence: **99.31%**
1135. **`platforms/core-runtime/gradle-cli/src/test/groovy/org/gradle/launcher/cli/DefaultCommandLineActionFactoryTest.groovy`** -> AI Confidence: **99.31%**
1136. **`platforms/core-runtime/gradle-cli/src/test/groovy/org/gradle/launcher/cli/WelcomeMessageActionTest.groovy`** -> AI Confidence: **99.31%**
1137. **`platforms/core-runtime/instrumentation-agent-services/src/integTest/groovy/org/gradle/internal/instrumentation/agent/AgentApplicationTest.groovy`** -> AI Confidence: **99.31%**
1138. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/BuildEnvironmentIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1139. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/CommandLineIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1140. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/GradleConfigurabilityIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1141. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/SupportedBuildJvmVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1142. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/continuous/ContinuousBuildCancellationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1143. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonFeedbackIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1144. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonInitScriptHandlingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1145. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonInitialCommunicationFailureIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1146. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonReuseIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1147. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonToolchainDownloadIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1148. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonToolchainInvalidCriteriaIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1149. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/LocaleSupportDaemonIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1150. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/ProcessCrashHandlingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1151. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/server/scaninfo/DaemonScanInfoIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1152. **`platforms/core-runtime/launcher/src/test/groovy/org/gradle/launcher/cli/converter/PropertiesToDaemonParametersConverterTest.groovy`** -> AI Confidence: **99.31%**
1153. **`platforms/core-runtime/launcher/src/test/groovy/org/gradle/launcher/daemon/server/health/HealthExpirationStrategyTest.groovy`** -> AI Confidence: **99.31%**
1154. **`platforms/core-runtime/launcher/src/test/groovy/org/gradle/launcher/daemon/server/health/LowMemoryDaemonExpirationStrategyTest.groovy`** -> AI Confidence: **99.31%**
1155. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/AbstractConsoleBuildPhaseFunctionalTest.groovy`** -> AI Confidence: **99.31%**
1156. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/AbstractConsoleConfigurationProgressFunctionalTest.groovy`** -> AI Confidence: **99.31%**
1157. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/deprecation/DeprecationLoggerTest.groovy`** -> AI Confidence: **99.31%**
1158. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/deprecation/LoggingDeprecatedFeatureHandlerTest.groovy`** -> AI Confidence: **99.31%**
1159. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/console/BuildStatusRendererTest.groovy`** -> AI Confidence: **99.31%**
1160. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/console/DefaultColorMapTest.groovy`** -> AI Confidence: **99.31%**
1161. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/console/UserInputConsoleRendererTest.groovy`** -> AI Confidence: **99.31%**
1162. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/console/UserInputStandardOutputRendererTest.groovy`** -> AI Confidence: **99.31%**
1163. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/services/DefaultLoggingManagerTest.groovy`** -> AI Confidence: **99.31%**
1164. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/services/LoggingServiceRegistryTest.groovy`** -> AI Confidence: **99.31%**
1165. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/sink/GroupingProgressLogEventGeneratorTest.groovy`** -> AI Confidence: **99.31%**
1166. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/sink/OutputEventRendererTest.groovy`** -> AI Confidence: **99.31%**
1167. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/source/JavaUtilLoggingSystemTest.groovy`** -> AI Confidence: **99.31%**
1168. **`platforms/core-runtime/messaging/src/integTest/groovy/org/gradle/internal/serialize/ExceptionPlaceholderIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1169. **`platforms/core-runtime/messaging/src/test/groovy/org/gradle/internal/remote/internal/hub/MessageHubTest.groovy`** -> AI Confidence: **99.31%**
1170. **`platforms/core-runtime/native/src/test/groovy/org/gradle/internal/nativeintegration/console/NativePlatformConsoleDetectorTest.groovy`** -> AI Confidence: **99.31%**
1171. **`platforms/core-runtime/process-services/src/integTest/groovy/org/gradle/process/internal/CancellationBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1172. **`platforms/core-runtime/process-services/src/integTest/groovy/org/gradle/process/internal/CancellationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1173. **`platforms/core-runtime/process-services/src/test/groovy/org/gradle/api/internal/tasks/util/DefaultJavaForkOptionsTest.groovy`** -> AI Confidence: **99.31%**
1174. **`platforms/core-runtime/process-services/src/test/groovy/org/gradle/process/internal/JavaExecHandleBuilderTest.groovy`** -> AI Confidence: **99.31%**
1175. **`platforms/core-runtime/process-services/src/test/groovy/org/gradle/process/internal/JvmOptionsTest.groovy`** -> AI Confidence: **99.31%**
1176. **`platforms/core-runtime/start-parameter/src/test/groovy/org/gradle/StartParameterTest.groovy`** -> AI Confidence: **99.31%**
1177. **`platforms/core-runtime/stdlib-java-extensions/src/test/groovy/org/gradle/internal/os/OperatingSystemTest.groovy`** -> AI Confidence: **99.31%**
1178. **`platforms/core-runtime/stdlib-java-extensions/src/test/groovy/org/gradle/util/internal/CollectionUtilsTest.groovy`** -> AI Confidence: **99.31%**
1179. **`platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperChecksumVerificationTest.groovy`** -> AI Confidence: **99.31%**
1180. **`platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperGenerationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1181. **`platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperHttpsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1182. **`platforms/core-runtime/wrapper-shared/src/test/groovy/org/gradle/wrapper/InstallTest.groovy`** -> AI Confidence: **99.31%**
1183. **`platforms/documentation/samples/src/integTest/groovy/org/gradle/integtests/samples/files/SamplesCopyIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1184. **`platforms/documentation/samples/src/integTest/groovy/org/gradle/integtests/samples/java/SamplesJavaTestingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1185. **`platforms/enterprise/enterprise-plugin-performance/src/testFixtures/groovy/org/gradle/performance/fixture/BuildScanPerformanceTestRunner.groovy`** -> AI Confidence: **99.31%**
1186. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/AbstractDevelocityInputIgnoringServiceIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1187. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/DevelocityPluginCheckInIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1188. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/DevelocityPluginConfigIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1189. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/DevelocityPluginConfigurationCachingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1190. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/core/BuildScanAutoApplyIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1191. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/core/BuildScanBuildFailureHintIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1192. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/api/plugins/BuildSrcPluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1193. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/plugins/JavaGradlePluginPluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1194. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/plugins/PrecompiledGroovyPluginsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1195. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/tasks/AbstractPluginValidationIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1196. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/tasks/ValidatePluginsPart1IntegrationTest.groovy`** -> AI Confidence: **99.31%**
1197. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/tasks/ValidatePluginsPart2IntegrationTest.groovy`** -> AI Confidence: **99.31%**
1198. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/variants/GradlePluginWithVariantsPublicationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1199. **`platforms/extensibility/plugin-use/src/integTest/groovy/org/gradle/plugin/repository/ResolvingFromMultipleCustomPluginRepositorySpec.groovy`** -> AI Confidence: **99.31%**
1200. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerBuildFailureIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1201. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerConventionalPluginClasspathInjectionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1202. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerMechanicalFailureIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1203. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerPluginClasspathInjectionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1204. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerResultIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1205. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/enduser/GradleRunnerConventionalPluginClasspathInjectionEndUserIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1206. **`platforms/extensibility/test-kit/src/test/groovy/org/gradle/testkit/runner/internal/DefaultGradleRunnerTest.groovy`** -> AI Confidence: **99.31%**
1207. **`platforms/extensibility/unit-test-fixtures/src/integTest/groovy/org/gradle/testfixtures/ProjectBuilderEndUserIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1208. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/AbstractVisualStudioProjectIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1209. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/NativeIdeSamplesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1210. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/idea/IdeaPluginTest.groovy`** -> AI Confidence: **99.31%**
1211. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/internal/tooling/eclipse/EclipseModelBuilderDependenciesTest.groovy`** -> AI Confidence: **99.31%**
1212. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/internal/tooling/eclipse/EclipseModelBuilderTest.groovy`** -> AI Confidence: **99.31%**
1213. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/internal/tooling/eclipse/RunBuildDependenciesTaskBuilderTest.groovy`** -> AI Confidence: **99.31%**
1214. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/internal/tooling/idea/IdeaModelBuilderTest.groovy`** -> AI Confidence: **99.31%**
1215. **`platforms/ide/ide/src/test/groovy/org/gradle/plugins/ide/eclipse/model/EclipseModelTest.groovy`** -> AI Confidence: **99.31%**
1216. **`platforms/ide/problems-api/src/integTest/groovy/org/gradle/api/problems/ProblemsApiBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1217. **`platforms/ide/problems-rendering/src/test/groovy/org/gradle/problems/internal/rendering/GroupingProblemWriterTest.groovy`** -> AI Confidence: **99.31%**
1218. **`platforms/ide/problems-rendering/src/test/groovy/org/gradle/problems/internal/rendering/SimpleProblemWriterTest.groovy`** -> AI Confidence: **99.31%**
1219. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r18/BuildActionCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1220. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r213/ModelsWithGradleProjectCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1221. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r25/ProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1222. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r25/TaskProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1223. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r25/TestProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1224. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r33/BuildProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1225. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r40/ProjectConfigurationChildrenProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1226. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r40/ResolveArtifactsProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1227. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/ProjectConfigurationProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1228. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/TaskExecutionResultCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1229. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/TaskOriginCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1230. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/TransformProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1231. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r68/CompositeBuildTaskExecutionCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1232. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r76/BuildPhaseOperationEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1233. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r76/TestFailureProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1234. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r812/ProblemProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1235. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r83/TestLauncherCustomTestTaskCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1236. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r84/TestLauncherCompositeBuildCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1237. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r85/TestLauncherDebugCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1238. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r88/ProblemProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1239. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r89/ProblemProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1240. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r930/FetchBuildActionCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1241. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/DummyModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1242. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/PhasedBuildActionCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1243. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientGradleBuildBuilderCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1244. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientKotlinDslScriptsModelBuilderCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1245. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResourceBasedTestingCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1246. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/m5/ToolingApiIdeaModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1247. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/r210/ToolingApiEclipseModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1248. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/r211/ToolingApiEclipseModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1249. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/r211/ToolingApiIdeaModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1250. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/r31/ToolingApiIdeaModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1251. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/r35/ToolingApiEclipseModelDependencyAccessRuleCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1252. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiClientJdkCompatibilityTest.groovy`** -> AI Confidence: **99.31%**
1253. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiLoggingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1254. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiRemoteIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1255. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiUnsupportedVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1256. **`platforms/ide/tooling-api/src/test/groovy/org/gradle/tooling/internal/adapter/WeakIdentityHashMapTest.groovy`** -> AI Confidence: **99.31%**
1257. **`platforms/ide/tooling-api/src/test/groovy/org/gradle/tooling/internal/consumer/DefaultModelBuilderTest.groovy`** -> AI Confidence: **99.31%**
1258. **`platforms/ide/tooling-api/src/test/groovy/org/gradle/tooling/internal/consumer/DefaultTestLauncherTest.groovy`** -> AI Confidence: **99.31%**
1259. **`platforms/ide/tooling-api/src/test/groovy/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapterForTaskOperationsTest.groovy`** -> AI Confidence: **99.31%**
1260. **`platforms/jvm/antlr/src/integTest/groovy/org/gradle/api/plugins/antlr/Antlr3PluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1261. **`platforms/jvm/antlr/src/integTest/groovy/org/gradle/api/plugins/antlr/Antlr4PluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1262. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/AntWorkerMemoryLeakIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1263. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/checkstyle/CheckstylePluginMultiProjectTest.groovy`** -> AI Confidence: **99.31%**
1264. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/checkstyle/CheckstylePluginVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1265. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/codenarc/CodeNarcPluginVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1266. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/pmd/PmdPluginAuxclasspathIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1267. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/pmd/PmdPluginToolchainsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1268. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/pmd/PmdPluginVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1269. **`platforms/jvm/ear/src/test/groovy/org/gradle/plugins/ear/EarPluginTest.groovy`** -> AI Confidence: **99.31%**
1270. **`platforms/jvm/ear/src/test/groovy/org/gradle/plugins/ear/descriptor/internal/DefaultDeploymentDescriptorTest.groovy`** -> AI Confidence: **99.31%**
1271. **`platforms/jvm/jacoco/src/integTest/groovy/org/gradle/testing/jacoco/plugins/JacocoAggregationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1272. **`platforms/jvm/jacoco/src/test/groovy/org/gradle/testing/jacoco/plugins/JacocoPluginSpec.groovy`** -> AI Confidence: **99.31%**
1273. **`platforms/jvm/jacoco/src/test/groovy/org/gradle/testing/jacoco/plugins/JacocoTaskExtensionSpec.groovy`** -> AI Confidence: **99.31%**
1274. **`platforms/jvm/java-compiler-worker/src/test/groovy/org/gradle/api/internal/tasks/compile/JavaCompilerArgumentsBuilderTest.groovy`** -> AI Confidence: **99.31%**
1275. **`platforms/jvm/java-platform/src/integTest/groovy/org/gradle/api/plugins/JavaPlatformPluginTest.groovy`** -> AI Confidence: **99.31%**
1276. **`platforms/jvm/jvm-services/src/test/groovy/org/gradle/jvm/toolchain/internal/MavenToolchainsInstallationSupplierTest.groovy`** -> AI Confidence: **99.31%**
1277. **`platforms/jvm/language-groovy/src/integTest/groovy/org/gradle/groovy/compile/GroovyCompileToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1278. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecDebugIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1279. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1280. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1281. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecWithLongCommandLineIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1282. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaToolchainBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1283. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaToolchainUpToDateIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1284. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaAnnotationProcessingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1285. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileAvoidanceWithBuildCacheServiceIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1286. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileCompatibilityIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1287. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1288. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileJavaVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1289. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileProblemsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1290. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1291. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/javadoc/JavadocIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1292. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/javadoc/JavadocToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1293. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/integtests/ExecIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1294. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/jvm/toolchain/JavaToolchainDownloadIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1295. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/jvm/toolchain/JavaToolchainDownloadSpiAuthenticationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1296. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/jvm/toolchain/JavaToolchainDownloadSpiIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1297. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/jvm/toolchain/JavaToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1298. **`platforms/jvm/language-java/src/test/groovy/org/gradle/api/internal/tasks/compile/AnnotationProcessorDiscoveringCompilerTest.groovy`** -> AI Confidence: **99.31%**
1299. **`platforms/jvm/language-java/src/test/groovy/org/gradle/api/internal/tasks/compile/incremental/deps/ClassSetAnalysisTest.groovy`** -> AI Confidence: **99.31%**
1300. **`platforms/jvm/language-java/src/test/groovy/org/gradle/api/internal/tasks/compile/processing/AnnotationProcessorDetectorTest.groovy`** -> AI Confidence: **99.31%**
1301. **`platforms/jvm/language-jvm/src/integTest/groovy/org/gradle/api/tasks/bundling/JarEncodingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1302. **`platforms/jvm/language-jvm/src/test/groovy/org/gradle/api/plugins/jvm/internal/JvmComponentDependenciesTest.groovy`** -> AI Confidence: **99.31%**
1303. **`platforms/jvm/normalization-java/src/test/groovy/org/gradle/api/internal/changedetection/state/MetaInfAwareClasspathResourceHasherTest.groovy`** -> AI Confidence: **99.31%**
1304. **`platforms/jvm/platform-jvm/src/test/groovy/org/gradle/api/java/archives/internal/DefaultManifestMergeSpecTest.groovy`** -> AI Confidence: **99.31%**
1305. **`platforms/jvm/platform-jvm/src/test/groovy/org/gradle/api/java/archives/internal/DefaultManifestTest.groovy`** -> AI Confidence: **99.31%**
1306. **`platforms/jvm/plugins-groovy/src/crossVersionTest/groovy/org/gradle/integtests/StaticGroovyTaskSubclassingBinaryCompatibilityCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1307. **`platforms/jvm/plugins-groovy/src/test/groovy/org/gradle/api/plugins/GroovyPluginTest.groovy`** -> AI Confidence: **99.31%**
1308. **`platforms/jvm/plugins-java-base/src/integTest/groovy/org/gradle/api/plugins/JavaBasePluginTest.groovy`** -> AI Confidence: **99.31%**
1309. **`platforms/jvm/plugins-java-base/src/integTest/groovy/org/gradle/api/plugins/jvm/internal/DefaultJvmPluginServicesTest.groovy`** -> AI Confidence: **99.31%**
1310. **`platforms/jvm/plugins-java-library/src/test/groovy/org/gradle/api/plugins/JavaLibraryPluginTest.groovy`** -> AI Confidence: **99.31%**
1311. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/api/plugins/JavaPluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1312. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/api/plugins/JavaPluginTest.groovy`** -> AI Confidence: **99.31%**
1313. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/java/JavaCrossCompilationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1314. **`platforms/jvm/plugins-java/src/integTest/groovy/org/gradle/java/compile/AbstractJavaCompilerIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1315. **`platforms/jvm/plugins-jvm-test-suite/src/integTest/groovy/org/gradle/testing/testsuites/TestSuitesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1316. **`platforms/jvm/plugins-jvm-test-suite/src/integTest/groovy/org/gradle/testing/testsuites/TestSuitesMultiTargetIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1317. **`platforms/jvm/plugins-test-report-aggregation/src/integTest/groovy/org/gradle/api/plugins/TestReportAggregationPluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1318. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/integtests/ScalaAnnotationProcessingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1319. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/ScalaConcurrencyIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1320. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/ScalaPluginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1321. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/BasicZincScalaCompilerIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1322. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/IncrementalScalaCompileIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1323. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/ScalaCompileIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1324. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/ScalaCompileJavaToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1325. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/daemon/ScalaCompilerDaemonReuseIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1326. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/scaladoc/ScalaDocIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1327. **`platforms/jvm/testing-jvm-infrastructure/src/test/groovy/org/gradle/api/internal/tasks/testing/junit/JUnitTestDefinitionProcessorTest.groovy`** -> AI Confidence: **99.31%**
1328. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/AbstractJvmFailFastIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1329. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/AbstractTestTaskIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1330. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/ParallelTestExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1331. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/TestOptionsIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1332. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/TestReportTaskIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1333. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/TestTaskCustomExecuterIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1334. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/TestTaskJavaVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1335. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/cucumberjvm/CucumberJVMReportIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1336. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/AbstractJUnitTestExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1337. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/AbstractJUnitTestFailureIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1338. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/junit4/AbstractJUnit4FilteringIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1339. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/jupiter/JUnitJupiterFilteringIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1340. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/jupiter/JUnitJupiterTestMetadataListenerIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1341. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/platform/JUnitPlatformIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1342. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/platform/JUnitPlatformLoggingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1343. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/platform/JUnitPlatformParameterizedTestIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1344. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/platform/JUnitPlatformSampleIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1345. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/nonclassbased/CucumberNonClassBasedTestingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1346. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/spek/Spek2IntegrationTest.groovy`** -> AI Confidence: **99.31%**
1347. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testng/TestNGIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1348. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testng/TestNGLoggingOutputCaptureIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1349. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testng/TestNGSuiteIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1350. **`platforms/jvm/toolchains-jvm-shared/src/test/groovy/org/gradle/jvm/toolchain/internal/JvmInstallationMetadataMatcherTest.groovy`** -> AI Confidence: **99.31%**
1351. **`platforms/jvm/war/src/test/groovy/org/gradle/api/plugins/WarPluginTest.groovy`** -> AI Confidence: **99.31%**
1352. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/AbstractNativePreCompiledHeaderIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1353. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/DuplicateBaseNamesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1354. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/assembler/AssemblyLanguageIncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1355. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppApplicationPublishingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1356. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppIncrementalBuildStaleOutputsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1357. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppLanguageIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1358. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppLanguageParallelIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1359. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppLibraryPublishingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1360. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppMissingToolchainIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1361. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppStaticLibraryPublishingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1362. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/nativeplatform/tasks/AbstractUnexportMainSymbolIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1363. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/objectivec/ObjectiveCLanguageIncrementalCompileIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1364. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/rc/WindowsResourcesIncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1365. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/rc/WindowsResourcesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1366. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftCachingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1367. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftIncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1368. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftIncrementalCompileIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1369. **`platforms/native/language-native/src/test/groovy/org/gradle/language/nativeplatform/internal/incremental/IncrementalCompileProcessorTest.groovy`** -> AI Confidence: **99.31%**
1370. **`platforms/native/language-native/src/test/groovy/org/gradle/language/nativeplatform/internal/incremental/SourceParseAndResolutionTest.groovy`** -> AI Confidence: **99.31%**
1371. **`platforms/native/language-native/src/test/groovy/org/gradle/language/nativeplatform/internal/incremental/sourceparser/RegexBackedCSourceParserTest.groovy`** -> AI Confidence: **99.31%**
1372. **`platforms/native/language-native/src/testFixtures/groovy/org/gradle/language/swift/AbstractSwiftComponentIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1373. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/BinaryConfigurationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1374. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/platform/BinaryNativePlatformIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1375. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/sourceset/GeneratedSourcesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1376. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/toolchain/GccToolChainDiscoveryIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1377. **`platforms/native/platform-native/src/test/groovy/org/gradle/nativeplatform/toolchain/internal/gcc/metadata/GccMetadataProviderTest.groovy`** -> AI Confidence: **99.31%**
1378. **`platforms/native/platform-native/src/test/groovy/org/gradle/nativeplatform/toolchain/internal/msvcpp/version/CommandLineToolVersionLocatorTest.groovy`** -> AI Confidence: **99.31%**
1379. **`platforms/native/platform-native/src/test/groovy/org/gradle/nativeplatform/toolchain/internal/msvcpp/version/WindowsRegistryVersionLocatorTest.groovy`** -> AI Confidence: **99.31%**
1380. **`platforms/native/platform-native/src/test/groovy/org/gradle/nativeplatform/toolchain/internal/tools/ToolSearchPathTest.groovy`** -> AI Confidence: **99.31%**
1381. **`platforms/native/platform-native/src/testFixtures/groovy/org/gradle/nativeplatform/fixtures/NativeBinaryFixture.groovy`** -> AI Confidence: **99.31%**
1382. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/cunit/CUnitDependentComponentsIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1383. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/cunit/CUnitSamplesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1384. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/googletest/GoogleTestDependentComponentsIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1385. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/googletest/GoogleTestSamplesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1386. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/xctest/SwiftXCTestCppInteroperabilityIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1387. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/xctest/SwiftXCTestErrorHandlingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1388. **`platforms/native/testing-native/src/integTest/groovy/org/gradle/nativeplatform/test/xctest/SwiftXCTestIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1389. **`platforms/native/tooling-native/src/crossVersionTest/groovy/org/gradle/language/cpp/tooling/r410/CppModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1390. **`platforms/native/tooling-native/src/crossVersionTest/groovy/org/gradle/language/cpp/tooling/r52/CppModelCrossVersionSpec.groovy`** -> AI Confidence: **99.31%**
1391. **`platforms/software/ant-impl/src/test/groovy/org/gradle/api/internal/project/DefaultAntBuilderTest.groovy`** -> AI Confidence: **99.31%**
1392. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/JavaApplicationInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1393. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/JavaLibraryInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1394. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/KotlinApplicationInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1395. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/KotlinGradlePluginInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1396. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/KotlinLibraryInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1397. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/MavenConversionDynamicPomIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1398. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/MavenConversionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1399. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/SwiftApplicationInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1400. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/SwiftLibraryInitIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1401. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/specs/internal/BuildInitSpecsInteractiveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1402. **`platforms/software/build-init/src/test/groovy/org/gradle/api/tasks/wrapper/WrapperTest.groovy`** -> AI Confidence: **99.31%**
1403. **`platforms/software/build-init/src/testFixtures/groovy/org/gradle/buildinit/plugins/fixtures/ScriptDslFixture.groovy`** -> AI Confidence: **99.31%**
1404. **`platforms/software/dependency-management/src/crossVersionTest/groovy/org/gradle/integtests/resolve/ResolveCrossVersionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1405. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/CacheResolveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1406. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/DependencyDownloadBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1407. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/RemoteDependencyResolveConsoleIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1408. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ResolveConfigurationDependenciesBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1409. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/artifactreuse/ArtifactResolutionQueryIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1410. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/ClasspathDependenciesAttributesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1411. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/VariantAwareResolutionWithConfigurationAttributesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1412. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/caching/ArtifactCacheUnusedEntryCleanupIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1413. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/AbstractHttpsRepoResolveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1414. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/AbstractProxyResolveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1415. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/DeprecatedTLSVersionDependencyResolutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1416. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/SocksProxyResolveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1417. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenLocalRepoResolveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1418. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rocache/AbstractReadOnlyCacheDependencyResolutionTest.groovy`** -> AI Confidence: **99.31%**
1419. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/AdditionalVariantsMetadataRulesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1420. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/ComponentMetadataRulesCachingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1421. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rules/ComponentMetadataRulesInSettingsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1422. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/strict/StrictVersionsInPlatformCentricDevelopmentIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1423. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformCachingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1424. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformExecutionBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1425. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformIncrementalIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1426. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformIsolationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1427. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformValuesInjectionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1428. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/TransformLoggingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1429. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/plugin/devel/variants/TargetJVMVersionOnPluginTooNewFailureDescriberIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1430. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/dsl/ComponentSelectorParsersTest.groovy`** -> AI Confidence: **99.31%**
1431. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/dsl/DefaultArtifactHandlerTest.groovy`** -> AI Confidence: **99.31%**
1432. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/dsl/ModuleComponentSelectorParsersTest.groovy`** -> AI Confidence: **99.31%**
1433. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/dsl/dependencies/DefaultDependencyConstraintHandlerTest.groovy`** -> AI Confidence: **99.31%**
1434. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/dsl/dependencies/DefaultDependencyHandlerTest.groovy`** -> AI Confidence: **99.31%**
1435. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencyResolveDetailsSpec.groovy`** -> AI Confidence: **99.31%**
1436. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencySubstitutionSpec.groovy`** -> AI Confidence: **99.31%**
1437. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencySubstitutionsSpec.groovy`** -> AI Confidence: **99.31%**
1438. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/ModuleSelectorStringNotationConverterTest.groovy`** -> AI Confidence: **99.31%**
1439. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/ComponentSelectionRulesProcessorTest.groovy`** -> AI Confidence: **99.31%**
1440. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/RepositoryChainArtifactResolverTest.groovy`** -> AI Confidence: **99.31%**
1441. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/RepositoryChainComponentMetaDataResolverTest.groovy`** -> AI Confidence: **99.31%**
1442. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/GradlePomModuleDescriptorParserTest.groovy`** -> AI Confidence: **99.31%**
1443. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyXmlModuleDescriptorParserTest.groovy`** -> AI Confidence: **99.31%**
1444. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/PomReaderTest.groovy`** -> AI Confidence: **99.31%**
1445. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/report/HtmlDependencyVerificationReportRendererTest.groovy`** -> AI Confidence: **99.31%**
1446. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/DefaultComponentSelectionRulesTest.groovy`** -> AI Confidence: **99.31%**
1447. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/DefaultResolutionStrategySpec.groovy`** -> AI Confidence: **99.31%**
1448. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/ModuleForcingResolveRuleSpec.groovy`** -> AI Confidence: **99.31%**
1449. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/factories/ExcludeTestSupport.groovy`** -> AI Confidence: **99.31%**
1450. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/simple/DefaultCompositeExcludeTest.groovy`** -> AI Confidence: **99.31%**
1451. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ComponentSelectorSerializerTest.groovy`** -> AI Confidence: **99.31%**
1452. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ResolutionResultGraphBuilderSpec.groovy`** -> AI Confidence: **99.31%**
1453. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/mvnsettings/DefaultLocalMavenRepositoryLocatorTest.groovy`** -> AI Confidence: **99.31%**
1454. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/repositories/DefaultIvyArtifactRepositoryTest.groovy`** -> AI Confidence: **99.31%**
1455. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/repositories/DefaultMavenArtifactRepositoryTest.groovy`** -> AI Confidence: **99.31%**
1456. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/repositories/resolver/DependenciesMetadataAdapterTest.groovy`** -> AI Confidence: **99.31%**
1457. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/repositories/resolver/IvyResourcePatternTest.groovy`** -> AI Confidence: **99.31%**
1458. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/repositories/resolver/M2ResourcePatternTest.groovy`** -> AI Confidence: **99.31%**
1459. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/type/ArtifactTypeRegistryTest.groovy`** -> AI Confidence: **99.31%**
1460. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/attributes/matching/DefaultAttributeMatcherTest.groovy`** -> AI Confidence: **99.31%**
1461. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/catalog/DefaultVersionCatalogBuilderTest.groovy`** -> AI Confidence: **99.31%**
1462. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/catalog/LibrariesSourceGeneratorTest.groovy`** -> AI Confidence: **99.31%**
1463. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/catalog/ProjectAccessorsSourceGeneratorTest.groovy`** -> AI Confidence: **99.31%**
1464. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/notations/DependencyMapNotationConverterTest.groovy`** -> AI Confidence: **99.31%**
1465. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/notations/DependencyStringNotationConverterTest.groovy`** -> AI Confidence: **99.31%**
1466. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/notations/ModuleIdentifierNotationConverterTest.groovy`** -> AI Confidence: **99.31%**
1467. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/external/model/AbstractDependencyMetadataRulesTest.groovy`** -> AI Confidence: **99.31%**
1468. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/external/model/DefaultModuleComponentSelectorTest.groovy`** -> AI Confidence: **99.31%**
1469. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/external/model/VariantFilesMetadataRulesTest.groovy`** -> AI Confidence: **99.31%**
1470. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/locking/DefaultDependencyLockingProviderTest.groovy`** -> AI Confidence: **99.31%**
1471. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/locking/DependencyLockingGraphVisitorTest.groovy`** -> AI Confidence: **99.31%**
1472. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/locking/LockFileReaderWriterTest.groovy`** -> AI Confidence: **99.31%**
1473. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/resolve/ModuleVersionResolveExceptionTest.groovy`** -> AI Confidence: **99.31%**
1474. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/resource/transfer/ProgressLoggingExternalResourceAccessorTest.groovy`** -> AI Confidence: **99.31%**
1475. **`platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/api/internal/artifacts/verification/DependencyVerificationFixture.groovy`** -> AI Confidence: **99.31%**
1476. **`platforms/software/ivy/src/test/groovy/org/gradle/api/publish/ivy/internal/publisher/IvyDescriptorFileGeneratorTest.groovy`** -> AI Confidence: **99.31%**
1477. **`platforms/software/ivy/src/testFixtures/groovy/org/gradle/api/publish/ivy/AbstractIvyPublishIntegTest.groovy`** -> AI Confidence: **99.31%**
1478. **`platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/MavenPublishHttpIntegTest.groovy`** -> AI Confidence: **99.31%**
1479. **`platforms/software/maven/src/test/groovy/org/gradle/api/publish/maven/plugins/MavenPublishPluginTest.groovy`** -> AI Confidence: **99.31%**
1480. **`platforms/software/maven/src/testFixtures/groovy/org/gradle/integtests/fixtures/publish/maven/AbstractMavenPublishIntegTest.groovy`** -> AI Confidence: **99.31%**
1481. **`platforms/software/platform-base/src/integTest/groovy/org/gradle/language/base/ComponentModelIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1482. **`platforms/software/platform-base/src/test/groovy/org/gradle/api/plugins/BasePluginTest.groovy`** -> AI Confidence: **99.31%**
1483. **`platforms/software/platform-base/src/test/groovy/org/gradle/language/base/plugins/LifecycleBasePluginTest.groovy`** -> AI Confidence: **99.31%**
1484. **`platforms/software/platform-base/src/test/groovy/org/gradle/platform/base/plugins/BinaryBasePluginTest.groovy`** -> AI Confidence: **99.31%**
1485. **`platforms/software/resources-gcs/src/integTest/groovy/org/gradle/integtests/resource/gcs/fixtures/GcsServer.groovy`** -> AI Confidence: **99.31%**
1486. **`platforms/software/resources-http/src/test/groovy/org/gradle/internal/resource/transport/http/AllowFollowForMutatingMethodRedirectStrategyTest.groovy`** -> AI Confidence: **99.31%**
1487. **`platforms/software/resources-http/src/test/groovy/org/gradle/internal/resource/transport/http/HttpClientSSLTest.groovy`** -> AI Confidence: **99.31%**
1488. **`platforms/software/resources-http/src/test/groovy/org/gradle/internal/resource/transport/http/JavaSystemPropertiesHttpTimeoutSettingsTest.groovy`** -> AI Confidence: **99.31%**
1489. **`platforms/software/resources-s3/src/test/groovy/org/gradle/internal/resource/transport/aws/s3/S3ClientTest.groovy`** -> AI Confidence: **99.31%**
1490. **`platforms/software/resources/src/test/groovy/org/gradle/internal/resource/UriTextResourceTest.groovy`** -> AI Confidence: **99.31%**
1491. **`platforms/software/signing/src/integTest/groovy/org/gradle/plugins/signing/SigningSamplesSpec.groovy`** -> AI Confidence: **99.31%**
1492. **`platforms/software/software-diagnostics/src/test/groovy/org/gradle/api/reporting/components/internal/SourceSetRendererTest.groovy`** -> AI Confidence: **99.31%**
1493. **`platforms/software/software-diagnostics/src/test/groovy/org/gradle/api/tasks/diagnostics/internal/graph/nodes/AbstractRenderableDependencyResultSpec.groovy`** -> AI Confidence: **99.31%**
1494. **`platforms/software/software-diagnostics/src/test/groovy/org/gradle/api/tasks/diagnostics/internal/insight/DependencyInsightReporterSpec.groovy`** -> AI Confidence: **99.31%**
1495. **`platforms/software/testing-base/src/integTest/groovy/org/gradle/testing/TestExecutionBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1496. **`platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/junit/result/JUnitXmlResultWriterSpec.groovy`** -> AI Confidence: **99.31%**
1497. **`platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/logging/TestCountLoggerTest.groovy`** -> AI Confidence: **99.31%**
1498. **`platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/logging/TestEventLoggerTest.groovy`** -> AI Confidence: **99.31%**
1499. **`platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/processors/MaxNParallelTestDefinitionProcessorTest.groovy`** -> AI Confidence: **99.31%**
1500. **`platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/processors/TestMainActionTest.groovy`** -> AI Confidence: **99.31%**
1501. **`platforms/software/testing-base/src/testFixtures/groovy/org/gradle/testing/AbstractTestFrameworkIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1502. **`platforms/software/version-control/src/integTest/groovy/org/gradle/vcs/internal/GitVcsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1503. **`platforms/software/version-control/src/test/groovy/org/gradle/vcs/git/internal/GitVersionControlSystemSpec.groovy`** -> AI Confidence: **99.31%**
1504. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/ConfigurationCacheCompositeBuildsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1505. **`subprojects/composite-builds/src/test/groovy/org/gradle/composite/internal/DefaultIncludedBuildTaskGraphTest.groovy`** -> AI Confidence: **99.31%**
1506. **`subprojects/core-api/src/test/groovy/org/gradle/api/tasks/util/PatternSetTest.groovy`** -> AI Confidence: **99.31%**
1507. **`subprojects/core/src/integTest/groovy/org/gradle/NativeServicesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1508. **`subprojects/core/src/integTest/groovy/org/gradle/api/BuildScriptErrorIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1509. **`subprojects/core/src/integTest/groovy/org/gradle/api/CrossBuildScriptCachingIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1510. **`subprojects/core/src/integTest/groovy/org/gradle/api/HttpProxyScriptPluginIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1511. **`subprojects/core/src/integTest/groovy/org/gradle/api/InitScriptExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1512. **`subprojects/core/src/integTest/groovy/org/gradle/api/NestedConfigureDslIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1513. **`subprojects/core/src/integTest/groovy/org/gradle/api/UndefinedBuildExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1514. **`subprojects/core/src/integTest/groovy/org/gradle/api/file/FileCollectionSymlinkIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1515. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/changedetection/state/TaskCustomTypesInputPropertyIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1516. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/project/ProjectEqualityContractIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1517. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/project/taskfactory/TaskPropertyNamingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1518. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/tasks/SnapshotTaskInputsOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1519. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/tasks/TaskCacheabilityReasonIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1520. **`subprojects/core/src/integTest/groovy/org/gradle/api/invocation/GradleLifecycleIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1521. **`subprojects/core/src/integTest/groovy/org/gradle/api/invocation/GradleLifecycleSupportedTypesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1522. **`subprojects/core/src/integTest/groovy/org/gradle/api/resource/TextResourceIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1523. **`subprojects/core/src/integTest/groovy/org/gradle/api/services/BuildServiceIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1524. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/AbstractLineEndingSensitivityIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1525. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CacheTaskArchiveErrorIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1526. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CachedCustomTaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1527. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CachedTaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1528. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyErrorIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1529. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopySpecIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1530. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/IncrementalBuildSymlinkHandlingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1531. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/IncrementalInputsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1532. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/JavaExecJavaVersionIntegrationSpec.groovy`** -> AI Confidence: **99.31%**
1533. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/LambdaInputsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1534. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/MissingTaskDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1535. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/NestedInputIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1536. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskCreationBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1537. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskInputFilePropertiesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1538. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskParametersIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1539. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskPropertiesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1540. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskServiceInjectionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1541. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskTimeoutIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1542. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/bundling/ConcurrentArchiveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1543. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/options/TaskOptionFailureIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1544. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/options/TaskOptionValuesIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1545. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/outputorigin/BuildCacheOutputOriginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1546. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/outputorigin/ContinuousIncrementalBuildOutputOriginIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1547. **`subprojects/core/src/integTest/groovy/org/gradle/cache/internal/GradleUserHomeCleanupServiceIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1548. **`subprojects/core/src/integTest/groovy/org/gradle/caching/configuration/internal/BuildCacheCompositeConfigurationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1549. **`subprojects/core/src/integTest/groovy/org/gradle/configuration/ExecuteUserLifecycleListenerBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1550. **`subprojects/core/src/integTest/groovy/org/gradle/execution/commandline/CommandLineIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1551. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/InitScriptIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1552. **`subprojects/core/src/integTest/groovy/org/gradle/internal/operations/notify/BuildOperationNotificationFixture.groovy`** -> AI Confidence: **99.31%**
1553. **`subprojects/core/src/integTest/groovy/org/gradle/plugin/ScriptPluginClassLoadingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1554. **`subprojects/core/src/test/groovy/org/gradle/api/internal/AbstractDomainObjectCollectionSpec.groovy`** -> AI Confidence: **99.31%**
1555. **`subprojects/core/src/test/groovy/org/gradle/api/internal/AbstractNamedDomainObjectContainerTest.groovy`** -> AI Confidence: **99.31%**
1556. **`subprojects/core/src/test/groovy/org/gradle/api/internal/DefaultDomainObjectCollectionTest.groovy`** -> AI Confidence: **99.31%**
1557. **`subprojects/core/src/test/groovy/org/gradle/api/internal/DefaultTaskTest.groovy`** -> AI Confidence: **99.31%**
1558. **`subprojects/core/src/test/groovy/org/gradle/api/internal/artifacts/JavaEcosystemSupportTest.groovy`** -> AI Confidence: **99.31%**
1559. **`subprojects/core/src/test/groovy/org/gradle/api/internal/artifacts/dependencies/AbstractModuleDependencySpec.groovy`** -> AI Confidence: **99.31%**
1560. **`subprojects/core/src/test/groovy/org/gradle/api/internal/attributes/BaseAttributeContainerTest.groovy`** -> AI Confidence: **99.31%**
1561. **`subprojects/core/src/test/groovy/org/gradle/api/internal/catalog/parser/TomlCatalogFileParserTest.groovy`** -> AI Confidence: **99.31%**
1562. **`subprojects/core/src/test/groovy/org/gradle/api/internal/collections/ElementSourceSpec.groovy`** -> AI Confidence: **99.31%**
1563. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/BaseDirFileResolverTest.groovy`** -> AI Confidence: **99.31%**
1564. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/DefaultSourceDirectorySetTest.groovy`** -> AI Confidence: **99.31%**
1565. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/FileNotationConverterTest.groovy`** -> AI Confidence: **99.31%**
1566. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/UriNotationConverterTest.groovy`** -> AI Confidence: **99.31%**
1567. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/copy/CopyFileVisitorImplTest.groovy`** -> AI Confidence: **99.31%**
1568. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/copy/CopySpecMatchingTest.groovy`** -> AI Confidence: **99.31%**
1569. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/copy/DefaultCopySpecResolutionTest.groovy`** -> AI Confidence: **99.31%**
1570. **`subprojects/core/src/test/groovy/org/gradle/api/internal/file/copy/DefaultCopySpecTest.groovy`** -> AI Confidence: **99.31%**
1571. **`subprojects/core/src/test/groovy/org/gradle/api/internal/initialization/DefaultClassLoaderScopeTest.groovy`** -> AI Confidence: **99.31%**
1572. **`subprojects/core/src/test/groovy/org/gradle/api/internal/plugins/DefaultPluginManagerTest.groovy`** -> AI Confidence: **99.31%**
1573. **`subprojects/core/src/test/groovy/org/gradle/api/internal/project/DefaultProjectTest.groovy`** -> AI Confidence: **99.31%**
1574. **`subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskContainerTest.groovy`** -> AI Confidence: **99.31%**
1575. **`subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskInputsTest.groovy`** -> AI Confidence: **99.31%**
1576. **`subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/TaskProvenanceUtilTest.groovy`** -> AI Confidence: **99.31%**
1577. **`subprojects/core/src/test/groovy/org/gradle/configuration/internal/DefaultListenerBuildOperationDecoratorTest.groovy`** -> AI Confidence: **99.31%**
1578. **`subprojects/core/src/test/groovy/org/gradle/execution/DefaultTasksBuildTaskSchedulerTest.groovy`** -> AI Confidence: **99.31%**
1579. **`subprojects/core/src/test/groovy/org/gradle/execution/commandline/CommandLineTaskConfigurerSpec.groovy`** -> AI Confidence: **99.31%**
1580. **`subprojects/core/src/test/groovy/org/gradle/execution/plan/ValuedVfsHierarchyTest.groovy`** -> AI Confidence: **99.31%**
1581. **`subprojects/core/src/test/groovy/org/gradle/initialization/properties/DefaultGradlePropertiesLoaderTest.groovy`** -> AI Confidence: **99.31%**
1582. **`subprojects/core/src/test/groovy/org/gradle/internal/buildevents/BuildExceptionReporterTest.groovy`** -> AI Confidence: **99.31%**
1583. **`subprojects/core/src/test/groovy/org/gradle/internal/fingerprint/impl/AbsolutePathFileCollectionFingerprinterTest.groovy`** -> AI Confidence: **99.31%**
1584. **`subprojects/core/src/test/groovy/org/gradle/internal/jvm/JavaModuleDetectorTest.groovy`** -> AI Confidence: **99.31%**
1585. **`subprojects/core/src/test/groovy/org/gradle/internal/model/StateTransitionControllerTest.groovy`** -> AI Confidence: **99.31%**
1586. **`subprojects/core/src/test/groovy/org/gradle/internal/operations/logging/DefaultBuildOperationLoggerTest.groovy`** -> AI Confidence: **99.31%**
1587. **`subprojects/core/src/test/groovy/org/gradle/internal/operations/notify/BuildOperationNotificationBridgeTest.groovy`** -> AI Confidence: **99.31%**
1588. **`subprojects/core/src/testFixtures/groovy/org/gradle/api/internal/tasks/AbstractSnapshotInputsBuildOperationResultTest.groovy`** -> AI Confidence: **99.31%**
1589. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/configuration/ExecuteDomainObjectCollectionCallbackBuildOperationTypeIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1590. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/environment/BuildEnvironmentIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1591. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/ProcessFixture.groovy`** -> AI Confidence: **99.31%**
1592. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/RepoScriptBlockUtil.groovy`** -> AI Confidence: **99.31%**
1593. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/GradleModuleMetadata.groovy`** -> AI Confidence: **99.31%**
1594. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/ivy/IvyFileModule.groovy`** -> AI Confidence: **99.31%**
1595. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/maven/AbstractMavenModule.groovy`** -> AI Confidence: **99.31%**
1596. **`testing/internal-distribution-testing/src/test/groovy/org/gradle/test/fixtures/server/http/BlockingHttpServerTest.groovy`** -> AI Confidence: **99.31%**
1597. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractContinuousIntegrationTest.groovy`** -> AI Confidence: **99.31%**
1598. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/BuildOperationTreeQueries.groovy`** -> AI Confidence: **99.31%**
1599. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/ToBeFixedSpecInterceptor.groovy`** -> AI Confidence: **99.31%**
1600. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/configurationcache/ConfigurationCacheFixture.groovy`** -> AI Confidence: **99.31%**
1601. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/configurationcache/ConfigurationCacheReportFixture.groovy`** -> AI Confidence: **99.31%**
1602. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/resolve/ResolveTestFixture.groovy`** -> AI Confidence: **99.31%**
1603. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/annotations/RunFor.groovy`** -> AI Confidence: **99.31%**
1604. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/fixture/CrossBuildPerformanceTestRunner.groovy`** -> AI Confidence: **99.31%**
1605. **`testing/internal-performance-testing/src/test/groovy/org/gradle/performance/ResultSpecification.groovy`** -> AI Confidence: **99.31%**
1606. **`testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/ConcurrentTestUtil.groovy`** -> AI Confidence: **99.31%**
1607. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/java/JavaIncrementalExecutionPerformanceTest.groovy`** -> AI Confidence: **99.31%**
1608. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/nativeplatform/NativeBuildPerformanceTest.groovy`** -> AI Confidence: **99.31%**
1609. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/nativeplatform/RealWorldNativePluginPerformanceTest.groovy`** -> AI Confidence: **99.31%**
1610. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/AbstractAndroidProjectSmokeTest.groovy`** -> AI Confidence: **99.31%**
1611. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/AndroidGradleRecipesKotlinSmokeTest.groovy`** -> AI Confidence: **99.31%**
1612. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/AndroidPluginsSmokeTest.groovy`** -> AI Confidence: **99.31%**
1613. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/BNDSmokeTest.groovy`** -> AI Confidence: **99.31%**
1614. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/DevelocityPluginSmokeTest.groovy`** -> AI Confidence: **99.31%**
1615. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/ShadowPluginSmokeTest.groovy`** -> AI Confidence: **99.31%**
1616. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/TestRetryPluginSmokeTest.groovy`** -> AI Confidence: **99.31%**
1617. **`testing/soak/src/integTest/groovy/org/gradle/jvm/toolchain/JavaToolchainDownloadSoakTest.groovy`** -> AI Confidence: **99.31%**
1618. **`platforms/core-runtime/daemon-logging/src/main/java/org/gradle/launcher/daemon/logging/DaemonMessages.java`** -> AI Confidence: **99.29%**
1619. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/internal/EclipseJavaVersionMapper.java`** -> AI Confidence: **99.29%**
1620. **`.teamcity/src/main/kotlin/common/Os.kt`** -> AI Confidence: **99.29%**
1621. **`.teamcity/src/main/kotlin/common/PerformanceTestExtensions.kt`** -> AI Confidence: **99.29%**
1622. **`.teamcity/src/main/kotlin/common/VersionedSettingsBranch.kt`** -> AI Confidence: **99.29%**
1623. **`.teamcity/src/main/kotlin/model/BucketExtensions.kt`** -> AI Confidence: **99.29%**
1624. **`.teamcity/src/main/kotlin/model/GradleSubprojectProvider.kt`** -> AI Confidence: **99.29%**
1625. **`.teamcity/src/main/kotlin/promotion/MergeReleaseIntoMaster.kt`** -> AI Confidence: **99.29%**
1626. **`.teamcity/src/main/kotlin/promotion/PublishBranchSnapshotFromQuickFeedback.kt`** -> AI Confidence: **99.29%**
1627. **`.teamcity/src/main/kotlin/promotion/PublishGradleDistributionFullBuild.kt`** -> AI Confidence: **99.29%**
1628. **`.teamcity/src/main/kotlin/promotion/PublishNightlySnapshot.kt`** -> AI Confidence: **99.29%**
1629. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/PublicApi.kt`** -> AI Confidence: **99.29%**
1630. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/classanalysis/ClassGraph.kt`** -> AI Confidence: **99.29%**
1631. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/testing/TestType.kt`** -> AI Confidence: **99.29%**
1632. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/util/ConfigurationExtensions.kt`** -> AI Confidence: **99.29%**
1633. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.build-logic.groovy-dsl-gradle-plugin.gradle.kts`** -> AI Confidence: **99.29%**
1634. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.ci-reporting.gradle.kts`** -> AI Confidence: **99.29%**
1635. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.private-javadoc.gradle.kts`** -> AI Confidence: **99.29%**
1636. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.test-retry.gradle.kts`** -> AI Confidence: **99.29%**
1637. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/nullaway/NullawayStatusService.kt`** -> AI Confidence: **99.29%**
1638. **`build-logic-commons/publishing/src/main/kotlin/gradlebuild.kotlin-dsl-plugin-bundle.gradle.kts`** -> AI Confidence: **99.29%**
1639. **`build-logic-commons/publishing/src/main/kotlin/gradlebuild.publish-defaults.gradle.kts`** -> AI Confidence: **99.29%**
1640. **`build-logic-commons/publishing/src/main/kotlin/gradlebuild.publish-public-libraries.gradle.kts`** -> AI Confidence: **99.29%**
1641. **`build-logic-settings/architecture-docs/src/main/kotlin/gradlebuild/Builders.kt`** -> AI Confidence: **99.29%**
1642. **`build-logic-settings/architecture-docs/src/main/kotlin/gradlebuild/GradleArchitecture.kt`** -> AI Confidence: **99.29%**
1643. **`build-logic-settings/configuration-cache-compatibility/src/main/kotlin/gradlebuild.configuration-cache-compatibility.settings.gradle.kts`** -> AI Confidence: **99.29%**
1644. **`build-logic-settings/version-catalogs/src/main/kotlin/gradlebuild.version-catalogs.settings.gradle.kts`** -> AI Confidence: **99.29%**
1645. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/AlphabeticalAcceptedApiChangesTask.kt`** -> AI Confidence: **99.29%**
1646. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/JApiCmpExtensions.kt`** -> AI Confidence: **99.29%**
1647. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/AbstractJavaNullabilityChangesTest.kt`** -> AI Confidence: **99.29%**
1648. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/AlphabeticalAcceptedApiChangesTaskIntegrationTest.kt`** -> AI Confidence: **99.29%**
1649. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/JSpecifyNullUnmarkedChangesTest.kt`** -> AI Confidence: **99.29%**
1650. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/KotlinInternalFilteringTest.kt`** -> AI Confidence: **99.29%**
1651. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/SortAcceptedApiChangesTaskIntegrationTest.kt`** -> AI Confidence: **99.29%**
1652. **`build-logic/binary-compatibility/src/test/kotlin/gradlebuild/binarycompatibility/UpgradedPropertiesChangesTest.kt`** -> AI Confidence: **99.29%**
1653. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild.root-target-runtimes.gradle.kts`** -> AI Confidence: **99.29%**
1654. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/FixProjectHealthTask.kt`** -> AI Confidence: **99.29%**
1655. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateContributorsInReleaseNotes.kt`** -> AI Confidence: **99.29%**
1656. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateSmokeTestedPluginsVersions.kt`** -> AI Confidence: **99.29%**
1657. **`build-logic/buildquality/src/main/kotlin/gradlebuild.arch-test.gradle.kts`** -> AI Confidence: **99.29%**
1658. **`build-logic/integration-testing/src/main/kotlin/gradlebuild.test-fixtures.gradle.kts`** -> AI Confidence: **99.29%**
1659. **`build-logic/jvm/src/main/kotlin/gradlebuild.jvm-compile.gradle.kts`** -> AI Confidence: **99.29%**
1660. **`build-logic/jvm/src/main/kotlin/gradlebuild.launchable-jar.gradle.kts`** -> AI Confidence: **99.29%**
1661. **`build-logic/jvm/src/main/kotlin/gradlebuild.strict-compile.gradle.kts`** -> AI Confidence: **99.29%**
1662. **`build-logic/jvm/src/main/kotlin/gradlebuild/jvm/JvmCompileExtension.kt`** -> AI Confidence: **99.29%**
1663. **`build-logic/jvm/src/main/kotlin/gradlebuild/propagated-env-variables.kt`** -> AI Confidence: **99.29%**
1664. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/codegen/ApiExtensionGeneratorFacade.kt`** -> AI Confidence: **99.29%**
1665. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/codegen/PluginIdExtensionsFacade.kt`** -> AI Confidence: **99.29%**
1666. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/codegen/SourceFileHeader.kt`** -> AI Confidence: **99.29%**
1667. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/support/ClassBytesRepository.kt`** -> AI Confidence: **99.29%**
1668. **`build-logic/kotlin-dsl-shared-runtime/src/main/kotlin/org/gradle/kotlin/dsl/internal/sharedruntime/support/IO.kt`** -> AI Confidence: **99.29%**
1669. **`build-logic/lifecycle/src/main/kotlin/gradlebuild.lifecycle.gradle.kts`** -> AI Confidence: **99.29%**
1670. **`build-logic/packaging/src/main/kotlin/gradlebuild.install.gradle.kts`** -> AI Confidence: **99.29%**
1671. **`build-logic/performance-testing/src/test/kotlin/gradlebuild/performance/PerformanceTestPluginTest.kt`** -> AI Confidence: **99.29%**
1672. **`build-logic/root-build/src/main/kotlin/gradlebuild.warmup-ec2.gradle.kts`** -> AI Confidence: **99.29%**
1673. **`build-logic/uber-plugins/src/main/kotlin/gradlebuild.ci-lifecycle.gradle.kts`** -> AI Confidence: **99.29%**
1674. **`build-logic/uber-plugins/src/main/kotlin/gradlebuild.distribution.api-java.gradle.kts`** -> AI Confidence: **99.29%**
1675. **`build-logic/uber-plugins/src/main/kotlin/gradlebuild.distribution.uninstrumented.api-java.gradle.kts`** -> AI Confidence: **99.29%**
1676. **`build-logic/uber-plugins/src/main/kotlin/gradlebuild.jvm-library.gradle.kts`** -> AI Confidence: **99.29%**
1677. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/buildtree/control/InvocationScenarioParameter.kt`** -> AI Confidence: **99.29%**
1678. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAction.kt`** -> AI Confidence: **99.29%**
1679. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareBuildTreeWorkGraphPreparer.kt`** -> AI Confidence: **99.29%**
1680. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareFinishExecutor.kt`** -> AI Confidence: **99.29%**
1681. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareLocalComponentCache.kt`** -> AI Confidence: **99.29%**
1682. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/InstrumentedInputAccessListener.kt`** -> AI Confidence: **99.29%**
1683. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/Workarounds.kt`** -> AI Confidence: **99.29%**
1684. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/barrier/BarrierAwareBuildTreeModelCreator.kt`** -> AI Confidence: **99.29%**
1685. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/extensions/ListExtensions.kt`** -> AI Confidence: **99.29%**
1686. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/ConfigurationCacheInjectedClasspathInstrumentationStrategy.kt`** -> AI Confidence: **99.29%**
1687. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/VintageInjectedClasspathInstrumentationStrategy.kt`** -> AI Confidence: **99.29%**
1688. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/io/safeWrap.kt`** -> AI Confidence: **99.29%**
1689. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ClassLoading.kt`** -> AI Confidence: **99.29%**
1690. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/serialization/codecs/CombinatorsTest.kt`** -> AI Confidence: **99.29%**
1691. **`platforms/core-configuration/configuration-problems-base/src/main/kotlin/org/gradle/internal/configuration/problems/ProblemDescription.kt`** -> AI Confidence: **99.29%**
1692. **`platforms/core-configuration/core-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/core/ExtraPropertiesExtensionExtensions.kt`** -> AI Confidence: **99.29%**
1693. **`platforms/core-configuration/core-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/core/LoggerExtensions.kt`** -> AI Confidence: **99.29%**
1694. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/InstanceAndPublicType.kt`** -> AI Confidence: **99.29%**
1695. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/Workarounds.kt`** -> AI Confidence: **99.29%**
1696. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/AnalysisStatementFilter.kt`** -> AI Confidence: **99.29%**
1697. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/ConfigureAccessorExtensions.kt`** -> AI Confidence: **99.29%**
1698. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/DeclarativeDslInterpretationException.kt`** -> AI Confidence: **99.29%**
1699. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/ObjectOriginUtils.kt`** -> AI Confidence: **99.29%**
1700. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/transformation/OriginReplacement.kt`** -> AI Confidence: **99.29%**
1701. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/DefaultNodeTypes.kt`** -> AI Confidence: **99.29%**
1702. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/data/DocumentDataContainerUtil.kt`** -> AI Confidence: **99.29%**
1703. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/data/DocumentDataContainers.kt`** -> AI Confidence: **99.29%**
1704. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/MutationParameter.kt`** -> AI Confidence: **99.29%**
1705. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/common/NodeRepresentationFlagsContainer.kt`** -> AI Confidence: **99.29%**
1706. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/language/LanguageTree.kt`** -> AI Confidence: **99.29%**
1707. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/language/LanguageTreeResult.kt`** -> AI Confidence: **99.29%**
1708. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/language/languageUtils.kt`** -> AI Confidence: **99.29%**
1709. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/DeclarativeRuntimeProperty.kt`** -> AI Confidence: **99.29%**
1710. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/RuntimeCustomAccessors.kt`** -> AI Confidence: **99.29%**
1711. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/DeclarativeDslSchemaBuildingException.kt`** -> AI Confidence: **99.29%**
1712. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ExtractionResult.kt`** -> AI Confidence: **99.29%**
1713. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/MemberTypeDiscovery.kt`** -> AI Confidence: **99.29%**
1714. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/SchemaFailureReporter.kt`** -> AI Confidence: **99.29%**
1715. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/SupertypeDiscovery.kt`** -> AI Confidence: **99.29%**
1716. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/com/example/demoTypes.kt`** -> AI Confidence: **99.29%**
1717. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/DomTestUtil.kt`** -> AI Confidence: **99.29%**
1718. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/resolution/testUtils.kt`** -> AI Confidence: **99.29%**
1719. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/junit5Assertions.kt`** -> AI Confidence: **99.29%**
1720. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/ErrorParsingTest.kt`** -> AI Confidence: **99.29%**
1721. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/ParseTestUtil.kt`** -> AI Confidence: **99.29%**
1722. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/StringParsingTest.kt`** -> AI Confidence: **99.29%**
1723. **`platforms/core-configuration/declarative-dsl-core/src/testFixtures/kotlin/org/gradle/internal/declarativedsl/parsing/ParseTestUtil.kt`** -> AI Confidence: **99.29%**
1724. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/evaluationSchema/FixedTypeDiscovery.kt`** -> AI Confidence: **99.29%**
1725. **`platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/EncryptionKind.kt`** -> AI Confidence: **99.29%**
1726. **`platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/NoEncryptionKeySource.kt`** -> AI Confidence: **99.29%**
1727. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/LoggingTracer.kt`** -> AI Confidence: **99.29%**
1728. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/codecs/ServicesCodec.kt`** -> AI Confidence: **99.29%**
1729. **`platforms/core-configuration/kotlin-dsl-plugins/src/main/kotlin/org/gradle/kotlin/dsl/plugins/dsl/ExperimentalCompilerWarningSilencer.kt`** -> AI Confidence: **99.29%**
1730. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/tasks/reduceGraph.kt`** -> AI Confidence: **99.29%**
1731. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/compile/PrecompiledPluginsCompileAvoidanceIntegrationTest.kt`** -> AI Confidence: **99.29%**
1732. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/KotlinDslTemplatesDeprecationsIntegrationTest.kt`** -> AI Confidence: **99.29%**
1733. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/ClassNamesFromTypeStrings.kt`** -> AI Confidence: **99.29%**
1734. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/KotlinTypeStrings.kt`** -> AI Confidence: **99.29%**
1735. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/PluginTree.kt`** -> AI Confidence: **99.29%**
1736. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/concurrent/EventLoop.kt`** -> AI Confidence: **99.29%**
1737. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/concurrent/ResurrectingThread.kt`** -> AI Confidence: **99.29%**
1738. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/CharSequenceExtensions.kt`** -> AI Confidence: **99.29%**
1739. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/PluginsBlockInterpretation.kt`** -> AI Confidence: **99.29%**
1740. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/ProgramParser.kt`** -> AI Confidence: **99.29%**
1741. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/ProgramSource.kt`** -> AI Confidence: **99.29%**
1742. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/TemporaryScriptFiles.kt`** -> AI Confidence: **99.29%**
1743. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/ClassPathModeExceptionCollector.kt`** -> AI Confidence: **99.29%**
1744. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/PrecompiledScriptsEnvironment.kt`** -> AI Confidence: **99.29%**
1745. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/CompactTree.kt`** -> AI Confidence: **99.29%**
1746. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/ConcurrentGroupingQueue.kt`** -> AI Confidence: **99.29%**
1747. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/EditorReports.kt`** -> AI Confidence: **99.29%**
1748. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/KotlinBuildScriptModelRepository.kt`** -> AI Confidence: **99.29%**
1749. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/ResolverEnvironment.kt`** -> AI Confidence: **99.29%**
1750. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/ClassLoaderScopeExtensions.kt`** -> AI Confidence: **99.29%**
1751. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/IO.kt`** -> AI Confidence: **99.29%**
1752. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/KotlinDslOptions.kt`** -> AI Confidence: **99.29%**
1753. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/Logger.kt`** -> AI Confidence: **99.29%**
1754. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/Maps.kt`** -> AI Confidence: **99.29%**
1755. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/execution/KotlinGrammarTest.kt`** -> AI Confidence: **99.29%**
1756. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/provider/ChildFirstClassLoader.kt`** -> AI Confidence: **99.29%**
1757. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/resolver/ResolverCoordinatorTest.kt`** -> AI Confidence: **99.29%**
1758. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/ProjectBuilder.kt`** -> AI Confidence: **99.29%**
1759. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/classBytes.kt`** -> AI Confidence: **99.29%**
1760. **`platforms/core-configuration/stdlib-kotlin-extensions/src/main/kotlin/org/gradle/configurationcache/extensions/CharSequenceExtensions.kt`** -> AI Confidence: **99.29%**
1761. **`platforms/core-configuration/stdlib-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/stdlib/CharSequenceExtensions.kt`** -> AI Confidence: **99.29%**
1762. **`platforms/core-configuration/stdlib-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/stdlib/ExceptionExtensions.kt`** -> AI Confidence: **99.29%**
1763. **`platforms/core-configuration/stdlib-kotlin-extensions/src/main/kotlin/org/gradle/internal/extensions/stdlib/MapExtensions.kt`** -> AI Confidence: **99.29%**
1764. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/RegexpPatternCodec.kt`** -> AI Confidence: **99.29%**
1765. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinapplication/App.kt.template`** -> AI Confidence: **99.29%**
1766. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinapplication/multi/list/LinkedList.kt.template`** -> AI Confidence: **99.29%**
1767. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinapplication/multi/utilities/JoinUtils.kt.template`** -> AI Confidence: **99.29%**
1768. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinapplication/multi/utilities/SplitUtils.kt.template`** -> AI Confidence: **99.29%**
1769. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinapplication/multi/utilities/StringUtils.kt.template`** -> AI Confidence: **99.29%**
1770. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinlibrary/Library.kt.template`** -> AI Confidence: **99.29%**
1771. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinlibrary/LibraryTest.kt.template`** -> AI Confidence: **99.29%**
1772. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/kotlinlibrary/junitjupiter/LibraryTest.kt.template`** -> AI Confidence: **99.29%**
1773. **`testing/performance/src/templates/kts-empty/build.gradle.kts`** -> AI Confidence: **99.29%**
1774. **`testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/android-kotlin-example-kotlin-dsl/app/build.gradle.kts`** -> AI Confidence: **99.29%**
1775. **`testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/kotlin-multiplatform-js-jvm-example/src/commonMain/kotlin/samples/Base64.kt`** -> AI Confidence: **99.29%**
1776. **`testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/kotlin-multiplatform-js-jvm-example/src/jsMain/kotlin/samples/Base64.kt`** -> AI Confidence: **99.29%**
1777. **`testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/kotlin-multiplatform-js-jvm-example/src/jvmMain/kotlin/samples/Base64.kt`** -> AI Confidence: **99.29%**
1778. **`testing/soak/src/integTest/kotlin/org/gradle/kotlin/dsl/caching/fixtures/ClassLoadingCache.kt`** -> AI Confidence: **99.29%**
1779. **`testing/soak/src/integTest/kotlin/org/gradle/kotlin/dsl/caching/fixtures/CompilationTrace.kt`** -> AI Confidence: **99.29%**
1780. **`platforms/core-configuration/base-diagnostics/src/integTest/resources/org/gradle/api/tasks/diagnostics/HelpTaskIntegrationTest/listsEnumAndBooleanCmdOptionValues/settings.gradle`** -> AI Confidence: **99.29%**
1781. **`platforms/core-configuration/base-diagnostics/src/test/groovy/org/gradle/api/tasks/diagnostics/internal/TaskReportRendererTest.groovy`** -> AI Confidence: **99.29%**
1782. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheBuildSrcProblemReportingIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1783. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheGracefulDegradationIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1784. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheGradlePropertiesFileIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1785. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheMultiProjectIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1786. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheScriptTaskDefinitionIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1787. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheTaskWiringIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1788. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsAccessFromKotlinDslIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1789. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1790. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsCompositeBuildIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1791. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsProblemReportingIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1792. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsTaskPathDependencyIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1793. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiBuildActionIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1794. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiCompositeBuildsIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1795. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiCoupledProjectsIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1796. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiGradleLifecycleIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1797. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiInvocationValidationIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1798. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiParameterizedModelQueryIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1799. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiPhasedBuildActionIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1800. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingModelsWithDependencyResolutionIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1801. **`platforms/core-configuration/file-collections/src/integTest/groovy/org/gradle/api/file/FileTreeIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1802. **`platforms/core-configuration/model-core/src/integTest/groovy/org/gradle/model/managed/ManagedModelGroovyScalarConfigurationIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1803. **`platforms/core-runtime/launcher/src/testFixtures/groovy/org/gradle/launcher/cli/HelpFixture.groovy`** -> AI Confidence: **99.29%**
1804. **`platforms/core-runtime/logging/src/integTest/resources/org/gradle/internal/logging/LoggingIntegrationTest/logging/build.gradle`** -> AI Confidence: **99.29%**
1805. **`platforms/core-runtime/logging/src/integTest/resources/org/gradle/internal/logging/LoggingIntegrationTest/logging/project2/build.gradle`** -> AI Confidence: **99.29%**
1806. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/console/ProgressBarTest.groovy`** -> AI Confidence: **99.29%**
1807. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/logging/console/WorkInProgressRendererTest.groovy`** -> AI Confidence: **99.29%**
1808. **`platforms/core-runtime/process-memory-services/src/test/groovy/org/gradle/process/internal/health/memory/MemInfoOsMemoryInfoTest.groovy`** -> AI Confidence: **99.29%**
1809. **`platforms/enterprise/enterprise-plugin-performance/src/templates/project-with-source/build.gradle`** -> AI Confidence: **99.29%**
1810. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioCompositeBuildIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1811. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioIncrementalIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1812. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/XcodeCompositeBuildIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1813. **`platforms/ide/ide-plugins/src/integTest/groovy/org/gradle/plugins/ide/eclipse/EclipseProjectIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1814. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/api/build.gradle`** -> AI Confidence: **99.29%**
1815. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/build.gradle`** -> AI Confidence: **99.29%**
1816. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/common/build.gradle`** -> AI Confidence: **99.29%**
1817. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/groovyproject/build.gradle`** -> AI Confidence: **99.29%**
1818. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/javabaseproject/build.gradle`** -> AI Confidence: **99.29%**
1819. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/webAppJava6/build.gradle`** -> AI Confidence: **99.29%**
1820. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/webAppWithVars/build.gradle`** -> AI Confidence: **99.29%**
1821. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/webservice/build.gradle`** -> AI Confidence: **99.29%**
1822. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaFacetAndCompilerLibraries/build.gradle`** -> AI Confidence: **99.29%**
1823. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaFacetAndCompilerLibraries/project1/build.gradle`** -> AI Confidence: **99.29%**
1824. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaFacetAndCompilerLibraries/project2/build.gradle`** -> AI Confidence: **99.29%**
1825. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaFacetAndCompilerLibraries/project3/build.gradle`** -> AI Confidence: **99.29%**
1826. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaFacetAndCompilerLibraries/project4/build.gradle`** -> AI Confidence: **99.29%**
1827. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaSdkAndCompilerLibraries/build.gradle`** -> AI Confidence: **99.29%**
1828. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaSdkAndCompilerLibraries/project1/build.gradle`** -> AI Confidence: **99.29%**
1829. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/addsScalaSdkAndCompilerLibraries/project2/build.gradle`** -> AI Confidence: **99.29%**
1830. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/canCreateAndDeleteMetaData/api/build.gradle`** -> AI Confidence: **99.29%**
1831. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/canCreateAndDeleteMetaData/build.gradle`** -> AI Confidence: **99.29%**
1832. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/canCreateAndDeleteMetaData/webservice/build.gradle`** -> AI Confidence: **99.29%**
1833. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/overwritesExistingDependencies/build.gradle`** -> AI Confidence: **99.29%**
1834. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/worksWithASubProjectThatDoesNotHaveTheIdeaPluginApplied/build.gradle`** -> AI Confidence: **99.29%**
1835. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/worksWithAnEmptyProject/build.gradle`** -> AI Confidence: **99.29%**
1836. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/worksWithNonStandardLayout/root/build.gradle`** -> AI Confidence: **99.29%**
1837. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/idea/IdeaIntegrationTest/worksWithNonStandardLayout/settings.gradle`** -> AI Confidence: **99.29%**
1838. **`platforms/ide/ide/src/integTest/groovy/org/gradle/plugins/ide/eclipse/EclipseTestConfigurationsWithExternalDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1839. **`platforms/ide/ide/src/integTest/groovy/org/gradle/plugins/ide/eclipse/EclipseTestConfigurationsWithProjectDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1840. **`platforms/ide/ide/src/test/groovy/org/gradle/plugins/ide/internal/configurer/HierarchicalElementDeduplicatorTest.groovy`** -> AI Confidence: **99.29%**
1841. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/fixture/ProblemsApiGroovyScriptUtils.groovy`** -> AI Confidence: **99.29%**
1842. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r60/ToolingApiPropertiesLoaderCrossVersionSpec.groovy`** -> AI Confidence: **99.29%**
1843. **`platforms/jvm/java-platform/src/integTest/groovy/org/gradle/integtests/resolve/platforms/JavaPlatformResolveIntegrationTest.groovy`** -> AI Confidence: **99.29%**
1844. **`platforms/jvm/javadoc/src/integTest/resources/org/gradle/api/tasks/javadoc/JavadocIntegrationTest/handlesTagsAndTaglets/build.gradle`** -> AI Confidence: **99.29%**
1845. **`platforms/jvm/language-groovy/src/integTest/resources/org/gradle/groovy/compile/IncrementalGroovyCompileIntegrationTest/failsCompilationWhenConfigScriptIsUpdated/build.gradle`** -> AI Confidence: **99.29%**
1846. **`platforms/jvm/language-groovy/src/integTest/resources/org/gradle/groovy/compile/IncrementalGroovyCompileIntegrationTest/failsCompilationWhenConfigScriptIsUpdated/newbuild.gradle`** -> AI Confidence: **99.29%**
1847. **`platforms/jvm/language-groovy/src/integTest/resources/org/gradle/groovy/compile/IncrementalGroovyCompileIntegrationTest/recompilesDependentClasses/build.gradle`** -> AI Confidence: **99.29%**
1848. **`platforms/jvm/language-groovy/src/integTest/resources/org/gradle/groovy/compile/IncrementalGroovyCompileIntegrationTest/recompilesSourceWhenPropertiesChange/build.gradle`** -> AI Confidence: **99.29%**
1849. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractApiGroovyCompilerIntegrationSpec/canUseCustomFileExtensions/build.gradle`** -> AI Confidence: **99.29%**
1850. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/canCompileAgainstGroovyClassThatDependsOnExternalClass/build.gradle`** -> AI Confidence: **99.29%**
1851. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/canListSourceFiles/build.gradle`** -> AI Confidence: **99.29%**
1852. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/compileBadCode/build.gradle`** -> AI Confidence: **99.29%**
1853. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/compileBadJavaCode/build.gradle`** -> AI Confidence: **99.29%**
1854. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/compileGoodCode/build.gradle`** -> AI Confidence: **99.29%**
1855. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/compileJavaFx8Code/build.gradle`** -> AI Confidence: **99.29%**
1856. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/configurationScriptNotSupported/build.gradle`** -> AI Confidence: **99.29%**
1857. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/failsBecauseOfInvalidConfigFile/build.gradle`** -> AI Confidence: **99.29%**
1858. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/failsBecauseOfMissingConfigFile/build.gradle`** -> AI Confidence: **99.29%**
1859. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/groovyToolClassesAreNotVisible/build.gradle`** -> AI Confidence: **99.29%**
1860. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/useConfigurationScript/build.gradle`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/junit/result/JUnitXmlResultWriterSpec.groovy` -> **99.9661%** Exposure
- `testing/internal-distribution-testing/src/test/groovy/org/gradle/integtests/fixtures/executer/OutputScrapingExecutionFailureTest.groovy` -> **0.0064%** Exposure
- `platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiLoggingIntegrationTest.groovy` -> **0.0031%** Exposure
- `platforms/software/resources/src/test/groovy/org/gradle/internal/resource/ExternalResourceNameTest.groovy` -> **0.0015%** Exposure
- `platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/junit/jupiter/JUnitJupiterLoggingOutputCaptureIntegrationTest.groovy` -> **0.0012%** Exposure
### Exploit Generation Surface
- `.teamcity/scripts/CheckBadMerge.java` -> **100.0%** Exposure
- `.teamcity/scripts/CheckRemoteProjectRef.java` -> **100.0%** Exposure
- `.teamcity/scripts/CheckWrapper.java` -> **100.0%** Exposure
- `.teamcity/scripts/FindCommits.java` -> **100.0%** Exposure
- `build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/upgrades/UpgradedProperty.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `.teamcity/scripts/CheckRemoteProjectRef.java` -> **100.0%** Exposure
- `platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/ReportGenerator.java` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForEachProjectInParallel.java` -> **100.0%** Exposure
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/DefaultConfigurableFilePermissions.java` -> **100.0%** Exposure
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/GeneratedSingletonFileTree.java` -> **100.0%** Exposure
### Raw Memory Manipulation
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-linked_ptr.h` -> **0.0067%** Exposure
### Hardcoded Payload Artifacts
- `platforms/software/security/src/test/groovy/org/gradle/security/internal/SecuritySupportSpec.groovy` -> **99.9399%** Exposure
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/S3ClientIntegrationTest.groovy` -> **99.6391%** Exposure
- `platforms/core-execution/build-cache-http/src/integTest/groovy/org/gradle/caching/http/internal/HttpBuildCacheServiceIntegrationTest.groovy` -> **97.2852%** Exposure
### Algorithmic DoS Exposure
- `.teamcity/scripts/CheckBadMerge.java` -> **100.0%** Exposure
- `.teamcity/scripts/CheckRemoteProjectRef.java` -> **100.0%** Exposure
- `.teamcity/scripts/CheckWrapper.java` -> **100.0%** Exposure
- `.teamcity/scripts/FindCommits.java` -> **100.0%** Exposure
- `build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/ExtractGradleApiInfoTask.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `126458` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `platforms/software/ant-impl/src/integTest/groovy/org/gradle/api/internal/project/DefaultIsolatedAntBuilderTest.groovy` (GROOVY) -> Cumulative Risk: **1070.82**
- **Archetype:** `file_cluster_4` (Distance: 11.384 IQR)
- **Magnitude:** 164.16 | **LOC:** 193 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `executesNestedClosures` (Impact: 26.8), `attachesLogger` (Impact: 14.3), `gradleClassesAreNotVisibleToAnt` (Impact: 11.1)

### 2. `platforms/core-execution/execution-e2e-tests/src/integTest/groovy/org/gradle/integtests/FileSystemRootUpToDateIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **1020.12**
- **Archetype:** `file_cluster_4` (Distance: 10.639 IQR)
- **Magnitude:** 164.56 | **LOC:** 114 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `def` (Impact: 52.7), `def` (Impact: 52.7), `substRoot` (Impact: 24.4)

### 3. `platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **1010.46**
- **Archetype:** `file_cluster_4` (Distance: 12.121 IQR)
- **Magnitude:** 1958.02 | **LOC:** 1078 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `def` (Impact: 172.3), `def` (Impact: 157.9), `def` (Impact: 143.9)

### 4. `platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecDebugIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **1007.2**
- **Archetype:** `file_cluster_4` (Distance: 11.72 IQR)
- **Magnitude:** 450.04 | **LOC:** 280 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `def` (Impact: 57.0), `def` (Impact: 50.8), `sampleProject` (Impact: 50.3)

### 5. `platforms/core-execution/file-watching/src/integTest/groovy/org/gradle/internal/watch/ChangesBetweenBuildsFileSystemWatchingIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **1004.43**
- **Archetype:** `file_cluster_4` (Distance: 11.727 IQR)
- **Magnitude:** 503.9 | **LOC:** 265 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `def` (Impact: 135.6), `def` (Impact: 69.1), `def` (Impact: 49.1)

### 6. `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/ExecutionResultJavaExecTaskIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **995.3**
- **Archetype:** `file_cluster_0` (Distance: 11.127 IQR)
- **Magnitude:** 81.22 | **LOC:** 89 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `writeSucceedingExec` (Impact: 30.8), `makeExecProject` (Impact: 10.7), `mainClass` (Impact: 6.8)

### 7. `platforms/jvm/plugins-java-base/src/testFixtures/groovy/org/gradle/java/compile/AbstractJavaGroovyCompileAvoidanceIntegrationSpec.groovy` (GROOVY) -> Cumulative Risk: **987.45**
- **Archetype:** `file_cluster_8` (Distance: 11.008 IQR)
- **Magnitude:** 3925.3 | **LOC:** 946 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `def` (Impact: 619.7), `def` (Impact: 514.6), `def` (Impact: 376.8)

### 8. `subprojects/core/src/integTest/groovy/org/gradle/api/internal/changedetection/state/TaskTypeUpToDateIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **986.9**
- **Archetype:** `file_cluster_4` (Distance: 11.027 IQR)
- **Magnitude:** 477.74 | **LOC:** 265 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `def` (Impact: 81.1), `def` (Impact: 65.5), `def` (Impact: 58.6)

### 9. `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/IncrementalBuildIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **986.73**
- **Archetype:** `file_cluster_4` (Distance: 12.157 IQR)
- **Magnitude:** 3248.56 | **LOC:** 1419 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `def` (Impact: 904.2), `def` (Impact: 249.3), `def` (Impact: 243.1)

### 10. `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/ExecutionResultExecTaskDeprecationIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **986.2**
- **Archetype:** `file_cluster_0` (Distance: 10.926 IQR)
- **Magnitude:** 83.1 | **LOC:** 88 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `writeSucceedingExec` (Impact: 30.8), `makeExecProject` (Impact: 15.6), `mainClass` (Impact: 6.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformInputArtifactIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.228 IQR)
- **Top Global Matches:** file_cluster_8: 13.228, file_cluster_0: 13.359, file_cluster_11: 13.516
- **Magnitude:** 9783.02 | **LOC:** 1532 | **CtrlFlow:** 88.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (92.8177%), Tech Debt (68.3783%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 1437.3 | O(2^N) | DB: 27)
  * `def` (Impact: 858.6 | O(2^N) | DB: 16)
  * `def` (Impact: 809.9 | O(2^N) | DB: 18)
  * `def` (Impact: 809.8 | O(2^N) | DB: 18)
  * `def` (Impact: 749.7 | O(2^N) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 751`, `structural_boundaries: 101`, `args: 433`, `func_start: 406`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 417`, `dead_code: 1`, `duplicate_logic: 16`
* *Architecture:* `io: 30`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 2`, `test: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.gradle.integtests.fixtures.AbstractDependencyResolutionTest, org.gradle.integtests.fixtures.DirectoryBuildCacheFixture, org.gradle.initialization.StartParameterBuildOptions, org.gradle.api.tasks.PathSensitivity, spock.lang.Issue, java.util.regex.Pattern
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformBuildOperationIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.761 IQR)
- **Top Global Matches:** file_cluster_8: 10.761, file_cluster_13: 11.231, file_cluster_0: 11.383
- **Magnitude:** 9120.22 | **LOC:** 1664 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (35.9255%), Tech Debt (79.9292%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 1036.5 | O(2^N))
  * `def` (Impact: 928.0 | O(2^N) | DB: 10)
  * `def` (Impact: 830.9 | O(2^N) | DB: 7)
  * `def` (Impact: 777.3 | O(2^N) | DB: 6)
  * `def` (Impact: 742.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 847`, `structural_boundaries: 181`, `args: 263`, `func_start: 279`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 17`, `duplicate_logic: 20`, `orphaned_logic: 1`
* *Architecture:* `io: 23`, `concurrency: 18`, `import: 31`
* *Defense:* `safety: 17`, `test: 77`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` org.gradle.internal.taskgraph.CalculateTaskGraphBuildOperationType, org.gradle.operations.execution.ExecuteWorkBuildOperationType, org.gradle.integtests.fixtures.executer.GradleContextualExecuter, org.gradle.integtests.fixtures.BuildOperationsFixture, org.gradle.api.internal.initialization.DefaultScriptClassPathResolver.InstrumentationPhase.NOT_INSTRUMENTED, org.gradle.api.services.BuildService, org.gradle.test.fixtures.file.TestFile, org.gradle.operations.dependencies.transforms.SnapshotTransformInputsBuildOperationType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.68 IQR)
- **Top Global Matches:** file_cluster_8: 10.68, file_cluster_7: 11.277, file_cluster_1: 11.49
- **Magnitude:** 8322.86 | **LOC:** 1995 | **CtrlFlow:** 90.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 164
- **Risk Profile:** Cognitive Load (51.0307%), Tech Debt (46.2902%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 6674.4 | O(2^N) | DB: 164)
  * `def` (Impact: 228.5 | O(2^N) | DB: 6)
  * `def` (Impact: 200.2 | O(2^N) | DB: 3)
  * `def` (Impact: 157.8 | O(2^N) | DB: 6)
  * `def` (Impact: 136.2 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1087`, `structural_boundaries: 114`, `args: 430`, `func_start: 469`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 8`, `duplicate_logic: 15`
* *Architecture:* `io: 90`, `api: 1`, `import: 17`
* *Defense:* `test: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` org.gradle.api.internal.artifacts.ivyservice.CacheLayout, org.gradle.api.internal.artifacts.verification.DependencyVerificationFixture.getChecksum, org.gradle.api.attributes.Category, org.gradle.security.fixtures.SigningFixtures.getValidPublicKeyLongIdHexString, org.gradle.security.internal.SecuritySupport.toHexString, java.util.concurrent.TimeUnit, org.gradle.security.fixtures.SigningFixtures.signAsciiArmored, org.gradle.security.fixtures.KeyServer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/catalog/VersionCatalogExtensionIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.293 IQR)
- **Top Global Matches:** file_cluster_8: 10.293, file_cluster_7: 11.017, file_cluster_1: 11.231
- **Magnitude:** 8252.62 | **LOC:** 2375 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (18.3267%), Tech Debt (98.1103%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 367.0 | O(2^N))
  * `def` (Impact: 339.2 | O(2^N))
  * `def` (Impact: 318.6 | O(2^N) | DB: 1)
  * `def` (Impact: 305.6 | O(2^N))
  * `def` (Impact: 260.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 689`, `structural_boundaries: 144`, `args: 316`, `func_start: 347`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 12`, `duplicate_logic: 52`, `orphaned_logic: 2`
* *Architecture:* `io: 13`, `import: 8`
* *Defense:* `safety: 36`, `test: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.gradle.api.internal.catalog.problems.VersionCatalogProblemId, org.gradle.api.internal.catalog.problems.VersionCatalogErrorMessages, org.gradle.api.artifacts.VersionCatalogsExtension, groovy.transform.CompileStatic, spock.lang.Issue, org.gradle.api.*, org.gradle.api.internal.catalog.problems.VersionCatalogProblemTestFor, org.gradle.integtests.fixtures.resolve.ResolveTestFixture
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/software-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/DependencyInsightReportTaskIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.053 IQR)
- **Top Global Matches:** file_cluster_8: 11.053, file_cluster_7: 11.634, file_cluster_4: 11.706
- **Magnitude:** 8158.56 | **LOC:** 3023 | **CtrlFlow:** 94.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (61.4691%), Tech Debt (99.5736%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 476.7 | O(2^N) | DB: 6)
  * `def` (Impact: 423.1 | O(2^N) | DB: 8)
  * `def` (Impact: 411.7 | O(N^4) | DB: 6)
  * `def` (Impact: 372.5 | O(N^5) | DB: 8)
  * `def` (Impact: 340.7 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1266`, `structural_boundaries: 81`, `args: 155`, `func_start: 121`, `class_start: 1`
* *Risk/State:* `state_mutation: 198`, `fragile_debt: 2`, `duplicate_logic: 53`, `orphaned_logic: 1`
* *Architecture:* `io: 100`, `concurrency: 145`, `import: 5`
* *Defense:* `safety: 2`, `test: 182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.gradle.integtests.resolve.locking.LockfileFixture, org.gradle.util.GradleVersion, org.gradle.api.JavaVersion, org.gradle.integtests.fixtures.SuggestionsMessages.repositoryHint, org.gradle.integtests.fixtures.AbstractIntegrationSpec
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/AbstractMavenPublishJavaIntegTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.972 IQR)
- **Top Global Matches:** file_cluster_8: 10.972, file_cluster_7: 11.572, file_cluster_13: 11.685
- **Magnitude:** 7749.32 | **LOC:** 1454 | **CtrlFlow:** 88.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (30.0502%), Tech Debt (95.1232%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 852.0 | O(2^N) | DB: 2)
  * `def` (Impact: 843.9 | O(2^N) | DB: 2)
  * `def` (Impact: 792.0 | O(N^6) | DB: 1)
  * `def` (Impact: 685.5 | O(2^N))
  * `def` (Impact: 596.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 62`, `args: 227`, `func_start: 254`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 59`, `duplicate_logic: 26`
* *Architecture:* `io: 9`, `api: 2`, `concurrency: 7`, `import: 10`
* *Defense:* `safety: 1`, `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.gradle.test.fixtures.maven.MavenJavaModule, org.gradle.api.publish.maven.internal.publication.MavenComponentParser, org.gradle.api.attributes.Category, org.gradle.integtests.fixtures.publish.maven.AbstractMavenPublishIntegTest, org.gradle.test.fixtures.maven.MavenFileModule, org.gradle.test.fixtures.maven.MavenDependencyExclusion, spock.lang.Issue, org.gradle.integtests.fixtures.GroovyBuildScriptLanguage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/versions/VersionConflictResolutionIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.732 IQR)
- **Top Global Matches:** file_cluster_8: 10.732, file_cluster_7: 11.389, file_cluster_1: 11.607
- **Magnitude:** 7302.92 | **LOC:** 2657 | **CtrlFlow:** 90.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (34.1781%), Tech Debt (99.952%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 319.1 | O(2^N))
  * `def` (Impact: 309.5 | O(2^N))
  * `def` (Impact: 281.0 | O(2^N) | DB: 1)
  * `def` (Impact: 260.5 | O(2^N))
  * `def` (Impact: 235.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1200`, `structural_boundaries: 127`, `args: 539`, `func_start: 525`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 37`, `fragile_debt: 1`, `duplicate_logic: 56`, `orphaned_logic: 1`
* *Architecture:* `io: 17`, `concurrency: 8`, `import: 9`
* *Defense:* `safety: 24`, `test: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.gradle.integtests.fixtures.SuggestionsMessages.INFO_DEBUG, org.gradle.integtests.fixtures.SuggestionsMessages.STACKTRACE_MESSAGE, org.gradle.api.attributes.Category, org.hamcrest.CoreMatchers.containsString, spock.lang.Issue, org.gradle.integtests.fixtures.SuggestionsMessages.GET_HELP, org.gradle.integtests.fixtures.SuggestionsMessages.SCAN, org.gradle.integtests.fixtures.resolve.ResolveTestFixture...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/native/language-native/src/integTest/groovy/org/gradle/language/swift/SwiftApplicationIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.99 IQR)
- **Top Global Matches:** file_cluster_8: 10.99, file_cluster_13: 11.552, file_cluster_7: 11.558
- **Magnitude:** 6994.34 | **LOC:** 1025 | **CtrlFlow:** 88.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (47.8212%), Tech Debt (99.8019%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 662.5 | O(2^N) | DB: 9)
  * `def` (Impact: 638.7 | O(2^N) | DB: 11)
  * `def` (Impact: 638.7 | O(2^N) | DB: 11)
  * `def` (Impact: 614.7 | O(2^N) | DB: 11)
  * `def` (Impact: 552.7 | O(2^N) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 80`, `args: 198`, `func_start: 141`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 66`, `duplicate_logic: 27`, `orphaned_logic: 6`
* *Architecture:* `io: 77`, `concurrency: 7`, `import: 8`
* *Defense:* `test: 189`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` org.gradle.nativeplatform.fixtures.app.SwiftCompilerDetectingApp, org.gradle.nativeplatform.fixtures.app.SwiftApp, org.gradle.nativeplatform.fixtures.app.SwiftAppWithOptionalFeature, org.gradle.nativeplatform.fixtures.RequiresInstalledToolChain, org.gradle.nativeplatform.fixtures.app.SwiftAppWithLibraries, org.gradle.nativeplatform.fixtures.ToolChainRequirement, org.gradle.nativeplatform.fixtures.app.SwiftAppWithLibrary, org.gradle.nativeplatform.fixtures.app.SwiftAppWithLibraryAndOptionalFeature
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/suppliers/DynamicRevisionRemoteResolveWithMetadataSupplierIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.395 IQR)
- **Top Global Matches:** file_cluster_8: 10.395, file_cluster_7: 11.039, file_cluster_13: 11.114
- **Magnitude:** 6511.06 | **LOC:** 1429 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (39.7033%), Tech Debt (94.5417%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 1036.3 | O(2^N) | DB: 17)
  * `def` (Impact: 504.5 | O(2^N) | DB: 3)
  * `def` (Impact: 422.9 | O(2^N) | DB: 1)
  * `def` (Impact: 384.7 | O(2^N) | DB: 3)
  * `def` (Impact: 369.2 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 639`, `structural_boundaries: 88`, `args: 165`, `func_start: 194`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 31`, `duplicate_logic: 21`, `orphaned_logic: 1`
* *Architecture:* `io: 16`, `api: 3`, `import: 11`
* *Defense:* `doc: 1`, `test: 108`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` org.gradle.integtests.resolve.AbstractModuleDependencyResolveTest, org.gradle.api.internal.artifacts.ivyservice.CacheLayout, org.gradle.integtests.fixtures.executer.GradleContextualExecuter, org.gradle.api.artifacts.CacheableRule, org.gradle.integtests.fixtures.GradleMetadataResolveRunner, org.gradle.integtests.fixtures.cache.CachingIntegrationFixture, org.gradle.integtests.fixtures.RequiredFeature, org.gradle.test.fixtures.server.http.IvyHttpModule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/ivy/src/integTest/groovy/org/gradle/api/publish/ivy/IvyPublishJavaIntegTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.997 IQR)
- **Top Global Matches:** file_cluster_8: 10.997, file_cluster_7: 11.581, file_cluster_13: 11.702
- **Magnitude:** 6347.54 | **LOC:** 1551 | **CtrlFlow:** 88.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (29.9113%), Tech Debt (67.0241%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 3840.4 | O(2^N) | DB: 32)
  * `def` (Impact: 760.1 | O(N^6) | DB: 1)
  * `def` (Impact: 385.3 | O(N^6) | DB: 1)
  * `void` (Impact: 374.9 | O(N^6) | DB: 2)
  * `void` (Impact: 178.0 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 40`, `args: 175`, `func_start: 184`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 63`, `duplicate_logic: 11`, `orphaned_logic: 1`
* *Architecture:* `io: 16`, `api: 2`, `concurrency: 14`, `import: 5`
* *Defense:* `safety: 7`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.gradle.test.fixtures.ivy.IvyJavaModule, org.gradle.api.publish.ivy.internal.publication.IvyComponentParser, org.gradle.api.internal.DocumentationRegistry, spock.lang.Issue, org.junit.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildConfigurationAttributesResolveIntegrationTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.93 IQR)
- **Top Global Matches:** file_cluster_8: 10.93, file_cluster_13: 11.455, file_cluster_11: 11.522
- **Magnitude:** 5736.38 | **LOC:** 1060 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (51.3151%), Tech Debt (76.731%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 930.5 | O(2^N) | DB: 15)
  * `def` (Impact: 859.5 | O(2^N) | DB: 21)
  * `def` (Impact: 859.5 | O(2^N) | DB: 21)
  * `def` (Impact: 803.0 | O(2^N) | DB: 12)
  * `def` (Impact: 600.9 | O(2^N) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 92`, `args: 173`, `func_start: 139`, `class_start: 19`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 72`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 39`, `concurrency: 16`, `import: 10`
* *Defense:* `safety: 5`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.acme.BuildType.debug, org.gradle.api.Plugin, org.gradle.api.Project, com.acme.Flavor.free, com.acme.Flavor.paid, com.acme.BuildType.release, org.gradle.api.attributes.Attribute, org.gradle.util.internal.ToBeImplemented...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationIntegrityCheckIntegTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.071 IQR)
- **Top Global Matches:** file_cluster_8: 10.071, file_cluster_7: 10.728, file_cluster_13: 10.847
- **Magnitude:** 5145.92 | **LOC:** 1209 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (35.6945%), Tech Debt (99.9911%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 386.4 | O(2^N))
  * `def` (Impact: 386.2 | O(2^N))
  * `def` (Impact: 363.1 | O(2^N))
  * `def` (Impact: 297.4 | O(2^N) | DB: 3)
  * `def` (Impact: 281.9 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 100`, `args: 159`, `func_start: 178`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 21`, `planned_debt: 1`, `duplicate_logic: 30`, `orphaned_logic: 1`
* *Architecture:* `io: 45`, `api: 2`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 1`, `doc: 1`, `test: 140`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.gradle.api.internal.artifacts.ivyservice.CacheLayout, org.gradle.test.precondition.Requires, org.gradle.integtests.fixtures.cache.CachingIntegrationFixture, spock.lang.Issue, org.gradle.util.Matchers.containsText, org.gradle.test.fixtures.file.TestFile, org.gradle.test.preconditions.IntegTestPreconditions, org.gradle.test.fixtures.HttpModule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/configurations/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/pubring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home/trustdb.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/pubring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home/trustdb.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/maven-publish/groovy/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/maven-publish/kotlin/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/documentation/docs/src/snippets/signing/tasks/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest/invalid-utf8-public-key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest/invalid-utf8-secret-key.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/default/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/CrossProcessSynchronizingIndexedCache.java` (JAVA) | Magnitude: 83.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 17, concurrency: 13, args: 10
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/strategy/VersionParser.java` (JAVA) | Magnitude: 268.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 32, branch: 19, api: 19
- `testing/architecture-test/src/test/java/org/gradle/architecture/test/FreezeInstructionsPrintingArchRule.java` (JAVA) | Magnitude: 109.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 15, api: 8, args: 7
- `subprojects/core/src/integTest/groovy/org/gradle/api/tasks/outputorigin/ManualUpToDateOutputOriginIntegrationTest.groovy` (GROOVY) | Magnitude: 217.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, branch: 15, structural_boundaries: 12, func_start: 11
- `testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/ivy/IvyFileModule.groovy` (GROOVY) | Magnitude: 1.31 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 572, branch: 188, args: 139, func_start: 120

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/fixtures/S3Server.groovy` (GROOVY) | Magnitude: 1.18 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 544, state_mutation: 237, branch: 134, args: 117
- `platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/extensibility/ExtensibleDynamicObjectTestHelper.groovy` (GROOVY) | Magnitude: 91.52 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, args: 25, func_start: 22, test: 15
- `platforms/software/dependency-management/src/test/groovy/org/gradle/internal/rules/DefaultRuleActionAdapterTest.groovy` (GROOVY) | Magnitude: 178.88 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, state_mutation: 28, structural_boundaries: 23, branch: 21
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/fixtures/stub/HttpStub.groovy` (GROOVY) | Magnitude: 0.05 | Delta: **0.244 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 20, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `subprojects/core/src/main/java/org/gradle/api/internal/project/CrossProjectConfigurator.java` (JAVA) | Magnitude: 179.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, branch: 6, generics: 6, args: 5
- `platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/registry/DaemonDir.java` (JAVA) | Magnitude: 21.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, io: 10, api: 8
- `platforms/native/tooling-native/src/main/java/org/gradle/language/cpp/internal/tooling/DefaultCppApplicationModel.java` (JAVA) | Magnitude: 5.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 3, func_start: 2, api: 2
- `platforms/native/tooling-native/src/main/java/org/gradle/language/cpp/internal/tooling/DefaultCppLibraryModel.java` (JAVA) | Magnitude: 5.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 3, func_start: 2, api: 2
- `platforms/native/tooling-native/src/main/java/org/gradle/language/cpp/internal/tooling/DefaultCppTestSuiteModel.java` (JAVA) | Magnitude: 5.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 3, func_start: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/NodeExecutionContext.java` (JAVA) | Magnitude: 8.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 2, func_start: 2
- `platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeatureApplicator.java` (JAVA) | Magnitude: 5.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, doc: 12, indent_spaces: 7, func_start: 5
- `platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/generator/generator/Generator.java` (JAVA) | Magnitude: 27.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, args: 4, func_start: 4, indent_spaces: 4
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/modulecache/dynamicversions/ModuleVersionsCache.java` (JAVA) | Magnitude: 7.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, args: 4, func_start: 4
- `subprojects/core-api/src/main/java/org/gradle/api/artifacts/CapabilitiesResolution.java` (JAVA) | Magnitude: 119.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 14, structural_boundaries: 10, branch: 4, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/AcceptedViolationsProvider.groovy` (GROOVY) | Magnitude: 17.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, state_mutation: 4, args: 2
- `platforms/ide/ide-native/src/testFixtures/groovy/org/gradle/ide/xcode/fixtures/WorkspaceFile.groovy` (GROOVY) | Magnitude: 0.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, io: 8, args: 5, structural_boundaries: 4
- `platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/internal/tooling/eclipse/EclipseModelBuilderDependenciesTest.groovy` (GROOVY) | Magnitude: 242.84 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 52, branch: 47, closures: 32
- `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/m5/ToolingApiBuildableEclipseModelFixesCrossVersionSpec.groovy` (GROOVY) | Magnitude: 57.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, branch: 8, closures: 7
- `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/plugins/ide/tooling/m5/ToolingApiIdeaModelCrossVersionSpec.groovy` (GROOVY) | Magnitude: 301.58 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, branch: 50, structural_boundaries: 36, state_mutation: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/ScriptHandlerScopeTest.kt` (KOTLIN) | Magnitude: 24.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, func_start: 26, import: 17, ui_framework: 15
- `testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/android-kotlin-example-kotlin-dsl/app/src/main/kotlin/org/gradle/smoketest/kotlin/android/StringPrinterFragment.kt` (KOTLIN) | Magnitude: 17.26 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ui_framework: 2, import: 2, args: 1, func_start: 1
- `testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/android-kotlin-example/app/src/main/kotlin/org/gradle/smoketest/kotlin/android/StringPrinterFragment.kt` (KOTLIN) | Magnitude: 17.26 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ui_framework: 2, import: 2, args: 1, func_start: 1
- `platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/scalaapplication/multi/list/LinkedList.scala.template` (SCALA) | Magnitude: 159.92 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 63, indent_spaces: 63, branch: 14, ui_framework: 10
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/model/ProjectIdentifier.java` (JAVA) | Magnitude: 20.92 | Delta: **0.256 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 3, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/SamplesToolingApiIntegrationTest.groovy` (GROOVY) | Magnitude: 81.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, func_start: 30, structural_boundaries: 26, args: 25
- `platforms/core-execution/file-watching/src/integTest/groovy/org/gradle/internal/watch/ChangesDuringTheBuildFileSystemWatchingIntegrationTest.groovy` (GROOVY) | Magnitude: 307.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 42, args: 35, func_start: 35
- `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r26/TestLauncherCrossVersionSpec.groovy` (GROOVY) | Magnitude: 410.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 126, branch: 125, func_start: 49, args: 46
- `subprojects/core/src/test/groovy/org/gradle/internal/service/scopes/ProjectBackedPropertyHostTest.groovy` (GROOVY) | Magnitude: 45.1 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 19, concurrency: 12, safety_bypasses: 7
- `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r68/CompositeBuildTestLauncherCrossVersionSpec.groovy` (GROOVY) | Magnitude: 254.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, branch: 44, args: 21, test: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/protocol/ConnectionVersion4.java` (JAVA) | Magnitude: 17.22 | Delta: **0.476 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: planned_debt: 8, doc: 5, structural_boundaries: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `subprojects/core-api/src/main/java/org/gradle/api/initialization/ConfigurableIncludedPluginBuild.java` (JAVA) | Magnitude: 18.22 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, args: 1, func_start: 1
- `platforms/core-runtime/build-process-services/src/main/java/org/gradle/internal/jvm/SupportedJavaVersions.java` (JAVA) | Magnitude: 18.64 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 5, doc: 5, globals: 4, immutability_locks: 4
- `platforms/jvm/platform-jvm/src/main/java/org/gradle/api/internal/tasks/JvmConstants.java` (JAVA) | Magnitude: 33.6 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 47, indent_spaces: 32, api: 31, immutability_locks: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/StoreExecutionStateStep.java` (JAVA) | Magnitude: 108.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 41, encapsulation: 22, args: 17
- `platforms/core-execution/snapshots/src/main/java/org/gradle/internal/fingerprint/hashing/RegularFileSnapshotContext.java` (JAVA) | Magnitude: 21.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, import: 2
- `platforms/core-runtime/process-memory-services/src/main/java/org/gradle/process/internal/health/memory/MemoryManager.java` (JAVA) | Magnitude: 38.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, args: 7, func_start: 7
- `platforms/enterprise/enterprise-operations/src/main/java/org/gradle/internal/resource/ExternalResourceReadMetadataBuildOperationType.java` (JAVA) | Magnitude: 9.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, api: 5, class_start: 3
- `platforms/ide/ide-plugins/src/main/java/org/gradle/plugins/ide/internal/tooling/BasicIdeaModelBuilder.java` (JAVA) | Magnitude: 13.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, api: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `platforms/jvm/javadoc/src/integTest/resources/org/gradle/api/tasks/javadoc/JavadocIntegrationTest/handlesTagsAndTaglets/src/main/java/Person.java` (JAVA) | Magnitude: 12.04 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, class_start: 1, api: 1
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest.h` (CPP) | Magnitude: 308.42 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 296, api: 254, immutability_locks: 170, structural_boundaries: 89
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest-test-part.h` (CPP) | Magnitude: 43.3 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, api: 26, immutability_locks: 21, structural_boundaries: 18
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest-typed-test.h` (CPP) | Magnitude: 26.88 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, macros: 18, api: 17, structural_boundaries: 14
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-linked_ptr.h` (CPP) | Magnitude: 77.44 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 42, args: 30, branch: 20

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperGenerationIntegrationTest.groovy` -> Churn: **70.87%** | Cog Load: 33.7479% | Debt: 100.0%
- `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/PropertyExtractor.kt` -> Churn: **58.86%** | Cog Load: 21.8804% | Debt: 99.3307%
- `platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/dependencyConfigurationSchema.kt` -> Churn: **58.86%** | Cog Load: 12.9114% | Debt: 94.9539%
- `platforms/core-runtime/launcher/src/testFixtures/groovy/org/gradle/launcher/cli/HelpFixture.groovy` -> Churn: **58.86%** | Cog Load: 90.3209% | Debt: 0.0%
- `platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/TaskbarProgressResetFunctionalTest.groovy` -> Churn: **58.86%** | Cog Load: 41.0068% | Debt: 99.9944%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformInputArtifactIntegrationTest.groovy` -> **Tom Tresansky** (100.0% isolated ownership) | Magnitude: 9783.02
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformBuildOperationIntegrationTest.groovy` -> **Vlad Chesnokov** (100.0% isolated ownership) | Magnitude: 9120.22
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy` -> **József Bartók** (100.0% isolated ownership) | Magnitude: 8322.86
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/catalog/VersionCatalogExtensionIntegrationTest.groovy` -> **Octavia Togami** (100.0% isolated ownership) | Magnitude: 8252.62
- `platforms/software/software-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/DependencyInsightReportTaskIntegrationTest.groovy` -> **Gary Hale** (100.0% isolated ownership) | Magnitude: 8158.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `subprojects/core/src/testFixtures/groovy/org/gradle/util/TestUtil.groovy` -> **Severity: 0.12** (Bridge: 0.0028 * Flux: 43.157%)
- `platforms/core-runtime/start-parameter/src/main/java/org/gradle/StartParameter.java` -> **Severity: 0.047** (Bridge: 0.0005 * Flux: 92.1082%)
- `subprojects/core/src/main/java/org/gradle/api/internal/GradleInternal.java` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 99.7201%)
- `subprojects/core-api/src/main/java/org/gradle/api/Project.java` -> **Severity: 0.034** (Bridge: 0.0026 * Flux: 12.9411%)
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/versioning/ModelMapping.java` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.8541%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/UncheckedException.java` -> **Severity: 638.33** (Blast Radius: 6.392 * Doc Risk: 99.8639%)
- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/api/UncheckedIOException.java` -> **Severity: 610.072** (Blast Radius: 6.137 * Doc Risk: 99.4089%)
- `platforms/core-execution/hashing/src/main/java/org/gradle/internal/hash/HashCode.java` -> **Severity: 416.4** (Blast Radius: 4.164 * Doc Risk: 99.9999%)
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/Collectors.java` -> **Severity: 415.5** (Blast Radius: 4.155 * Doc Risk: 100.0%)
- `platforms/core-runtime/base-services/src/main/java/org/gradle/api/Named.java` -> **Severity: 383.807** (Blast Radius: 3.839 * Doc Risk: 99.9759%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
