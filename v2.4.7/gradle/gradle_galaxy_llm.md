# ARCHITECTURAL_BRIEF: gradle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/gradle` |
| **Timestamp** | `2026-08-07T05:01:59.352026+00:00` |
| **Scan Duration** | `53.47s` |
| **Git Branch** | `master` |
| **Git Commit** | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` |
| **Git Remote** | `https://github.com/gradle/gradle` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 18604 malicious artifacts.

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
| Total Artifacts | 26690 |
| Analyzed Artifacts (Scanned) | 19038 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7652 |
| Total LOC | 1431299 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.3% |
| Dominant Lang | JAVA |

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
> **Architectural Drift Z-Score:** `5.418`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 10120 | 53.2% |
| file_cluster_13 | 6981 | 36.7% |
| file_cluster_16 | 1045 | 5.5% |
| file_cluster_0 | 419 | 2.2% |
| file_cluster_4 | 161 | 0.8% |
| file_cluster_17 | 23 | 0.1% |
| Unknown | 19 | 0.1% |
| file_cluster_9 | 8 | 0.0% |
| file_cluster_7 | 3 | 0.0% |
| file_cluster_2 | 3 | 0.0% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |

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
| Cognitive Load Exposure | 0.0 | 100.0 | 12.1 | 6.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 32.3 | 36.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.4 | 1.2 | 0.0 |
| API Exposure | 0.0 | 16.2 | 2.9 | 2.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 30.2 | 14.6 | 0.0 |
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

- `def` (@ `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy`) -> Impact: **592.5** | LOC: 1288
- `uncheckedModule` (@ `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy`) -> Impact: **396.5** | LOC: 1290
- `def` (@ `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientKotlinDslScriptsModelBuilderCrossVersionSpec.groovy`) -> Impact: **226.3** | LOC: 603
- `doResolveAugmentation` (@ `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/FunctionCallResolver.kt`) -> Impact: **196.8** | LOC: 337
- `def` (@ `subprojects/core/src/integTest/groovy/org/gradle/initialization/DistributionPropertiesLoaderIntegrationTest.groovy`) -> Impact: **163.9** | LOC: 61
  * *Intent:* /* * Copyright 2019 the original author or authors. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file ex...
- `startElement` (@ `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlReader.java`) -> Impact: **157.0** | LOC: 98
- `writeCustomTestSourceEmittingTestEngineS` (@ `platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/AbstractResourceBasedTestingCrossVersionSpec.groovy`) -> Impact: **145.8** | LOC: 457
- `read` (@ `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/SnapshotSerializer.java`) -> Impact: **141.0** | LOC: 77
- `assertSupportedChecksums` (@ `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/writer/WriteDependencyVerificationFile.java`) -> Impact: **139.6** | LOC: 271
- `loadOrScheduleRequestedTasks` (@ `platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCache.kt`) -> Impact: **135.3** | LOC: 626

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/groovy/gnupg-home` | 3 | 15000.0 | 0.0% | 0.0% |
| `platforms/documentation/docs/src/snippets/signing/gnupg-signatory/kotlin/gnupg-home` | 3 | 15000.0 | 0.0% | 0.0% |
| `platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureWriteIntegTest` | 2 | 10000.0 | 0.0% | 0.0% |
| `subprojects/core/src/integTest/groovy/org/gradle/api/tasks` | 80 | 9382.46 | 35.38% | 91.75% |
| `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve` | 65 | 6941.54 | 12.81% | 89.92% |
| `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl` | 80 | 6622.52 | 19.24% | 72.05% |
| `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider` | 63 | 5585.78 | 14.28% | 47.72% |
| `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/default` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/subkey` | 3 | 5002.0 | 0.0% | 0.0% |
| `platforms/software/signing/src/testFixtures/resources/keys/gradle` | 3 | 5002.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `build-logic-commons/code-quality-rules/src/main/java/gradlebuild/codenarc/rules/IntegrationTestFixturesRule.java` -> **100.0%** Exposure
- `platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/text/DefaultTextReportBuilder.java` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForEachProjectInParallel.java` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForEachProjectInTree.java` -> **100.0%** Exposure
- `platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForSameProjectInParallel.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/DirectoryWalker.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/MapEntryCollector.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/ValueCollector.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/DelegatingBaseExecSpec.java` -> **100.0%** Exposure
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/DelegatingExecSpec.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/versions/VersionConflictResolutionIntegrationTest.groovy` -> **2** Orphaned Functions | **242** Duplicates
- `platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/BuildScriptBuilder.java` -> **0** Orphaned Functions | **187** Duplicates
- `platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/PropertySpec.groovy` -> **0** Orphaned Functions | **137** Duplicates
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/MultipleVariantSelectionIntegrationTest.groovy` -> **2** Orphaned Functions | **134** Duplicates
- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/attributes/DependenciesAttributesIntegrationTest.groovy` -> **2** Orphaned Functions | **128** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DaemonStateCoordinator.java`** -> AI Confidence: **99.39%**
2. **`platforms/jvm/jvm-services/src/main/java/org/gradle/api/internal/artifacts/JavaEcosystemAttributesDescriber.java`** -> AI Confidence: **99.39%**
3. **`platforms/core-runtime/wrapper-main/src/crossVersionTest/groovy/org/gradle/integtests/wrapper/WrapperPropertiesLoaderCrossVersionTest.groovy`** -> AI Confidence: **99.39%**
4. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest-printers.h`** -> AI Confidence: **99.39%**
5. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-param-util.h`** -> AI Confidence: **99.39%**
6. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/JvmProjectInitDescriptor.java`** -> AI Confidence: **99.35%**
7. **`platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/integtests/fixtures/publish/ModuleVersionSpec.groovy`** -> AI Confidence: **99.35%**
8. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/ProjectLoadingIntegrationTest.java`** -> AI Confidence: **99.34%**
9. **`testing/performance/src/templates/cpp-source/exe.cpp`** -> AI Confidence: **99.32%**
10. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-linked_ptr.h`** -> AI Confidence: **99.32%**
11. **`build-logic/cleanup/src/main/java/gradlebuild/cleanup/services/KillLeakingJavaProcesses.java`** -> AI Confidence: **99.31%**
12. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/configuration/TaskDetailPrinter.java`** -> AI Confidence: **99.31%**
13. **`platforms/core-configuration/java-api-extractor/src/main/java/org/gradle/internal/tools/api/impl/JavaApiMemberWriter.java`** -> AI Confidence: **99.31%**
14. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/OrElseValueProducer.java`** -> AI Confidence: **99.31%**
15. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/DefaultTaskDependency.java`** -> AI Confidence: **99.31%**
16. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/DependencyInjectingInstantiator.java`** -> AI Confidence: **99.31%**
17. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/properties/annotations/AbstractTypeMetadataWalker.java`** -> AI Confidence: **99.31%**
18. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/AbstractValueProcessor.java`** -> AI Confidence: **99.31%**
19. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/SnapshotSerializer.java`** -> AI Confidence: **99.31%**
20. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/ModelTypeInitializationException.java`** -> AI Confidence: **99.31%**
21. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/FormattingValidationProblemCollector.java`** -> AI Confidence: **99.31%**
22. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/ModelRuleExtractor.java`** -> AI Confidence: **99.31%**
23. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/binding/DefaultStructBindingsStore.java`** -> AI Confidence: **99.31%**
24. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/cache/ModelSchemaCache.java`** -> AI Confidence: **99.31%**
25. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/StructSchemaExtractionStrategySupport.java`** -> AI Confidence: **99.31%**
26. **`platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/model/internal/fixture/ModelActionBuilder.java`** -> AI Confidence: **99.31%**
27. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/ClassInspector.java`** -> AI Confidence: **99.31%**
28. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/Types.java`** -> AI Confidence: **99.31%**
29. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/annotations/impl/DefaultTypeAnnotationMetadataStore.java`** -> AI Confidence: **99.31%**
30. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/validation/DefaultTypeAwareProblemBuilder.java`** -> AI Confidence: **99.31%**
31. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/FingerprintMapSerializer.java`** -> AI Confidence: **99.31%**
32. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/ExecuteWorkBuildOperationFiringStep.java`** -> AI Confidence: **99.31%**
33. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/RemovePreviousOutputsStep.java`** -> AI Confidence: **99.31%**
34. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/DefaultFileWatcherProbeRegistry.java`** -> AI Confidence: **99.31%**
35. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/LockOnDemandCrossProcessCacheAccess.java`** -> AI Confidence: **99.31%**
36. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/LockOnDemandEagerReleaseCrossProcessCacheAccess.java`** -> AI Confidence: **99.31%**
37. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/reflect/DirectInstantiator.java`** -> AI Confidence: **99.31%**
38. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/util/NumberUtil.java`** -> AI Confidence: **99.31%**
39. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/work/DefaultConditionalExecutionQueue.java`** -> AI Confidence: **99.31%**
40. **`platforms/core-runtime/base-services/src/main/java/org/gradle/util/internal/TextUtil.java`** -> AI Confidence: **99.31%**
41. **`platforms/core-runtime/build-operations-trace/src/main/java/org/gradle/internal/operations/trace/BuildOperationRecord.java`** -> AI Confidence: **99.31%**
42. **`platforms/core-runtime/concurrent/src/main/java/org/gradle/internal/concurrent/MultiProducerSingleConsumerProcessor.java`** -> AI Confidence: **99.31%**
43. **`platforms/core-runtime/files/src/main/java/org/gradle/internal/file/nio/PosixFilePermissionConverter.java`** -> AI Confidence: **99.31%**
44. **`platforms/core-runtime/groovy-loader/src/main/java/org/gradle/internal/groovyloader/ClassInfoCleaningGroovySystemLoader.java`** -> AI Confidence: **99.31%**
45. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/extensions/property/PropertyUpgradeClassSourceGenerator.java`** -> AI Confidence: **99.31%**
46. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/JavadocUtils.java`** -> AI Confidence: **99.31%**
47. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/groovy/CodeGeneratingSignatureTreeVisitor.java`** -> AI Confidence: **99.31%**
48. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/FileSystemWatchingBuildActionRunner.java`** -> AI Confidence: **99.31%**
49. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/continuous/FileEventCollector.java`** -> AI Confidence: **99.31%**
50. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/BuildStatusRenderer.java`** -> AI Confidence: **99.31%**
51. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/ConsoleConfigureAction.java`** -> AI Confidence: **99.31%**
52. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/OutputEventTransformer.java`** -> AI Confidence: **99.31%**
53. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/ProgressLogEventGenerator.java`** -> AI Confidence: **99.31%**
54. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/text/TreeFormatter.java`** -> AI Confidence: **99.31%**
55. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/dispatch/AsyncDispatch.java`** -> AI Confidence: **99.31%**
56. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/event/AbstractBroadcastDispatch.java`** -> AI Confidence: **99.31%**
57. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/hub/MessageHub.java`** -> AI Confidence: **99.31%**
58. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/filesystem/services/NativePlatformBackedFileMetadataAccessor.java`** -> AI Confidence: **99.31%**
59. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/jansi/JansiBootPathConfigurer.java`** -> AI Confidence: **99.31%**
60. **`platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/util/MergeOptionsUtil.java`** -> AI Confidence: **99.31%**
61. **`platforms/core-runtime/serialization/src/main/java/org/gradle/internal/serialize/DefaultSerializerRegistry.java`** -> AI Confidence: **99.31%**
62. **`platforms/core-runtime/serialization/src/main/java/org/gradle/internal/serialize/ExceptionPlaceholder.java`** -> AI Confidence: **99.31%**
63. **`platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/ServiceScopeValidator.java`** -> AI Confidence: **99.31%**
64. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/tasks/internal/ValidationProblemSerialization.java`** -> AI Confidence: **99.31%**
65. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/Project.java`** -> AI Confidence: **99.31%**
66. **`platforms/ide/problems-rendering/src/main/java/org/gradle/problems/internal/rendering/ProblemBodyWriter.java`** -> AI Confidence: **99.31%**
67. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/adapter/TypeInspector.java`** -> AI Confidence: **99.31%**
68. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/async/ServiceLifecycle.java`** -> AI Confidence: **99.31%**
69. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/ToolingParameterProxy.java`** -> AI Confidence: **99.31%**
70. **`platforms/jvm/antlr/src/main/java/org/gradle/api/plugins/antlr/internal/antlr2/GenerationPlanBuilder.java`** -> AI Confidence: **99.31%**
71. **`platforms/jvm/code-quality-workers/src/main/java/org/gradle/api/plugins/quality/internal/PmdInvoker.java`** -> AI Confidence: **99.31%**
72. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/JavaCompilerArgumentsBuilder.java`** -> AI Confidence: **99.31%**
73. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/deps/ClassSetAnalysisData.java`** -> AI Confidence: **99.31%**
74. **`platforms/jvm/scala/src/main/java/org/gradle/api/tasks/scala/internal/ScalaCompileOptionsConfigurer.java`** -> AI Confidence: **99.31%**
75. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/junit/CategoryFilter.java`** -> AI Confidence: **99.31%**
76. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/sourceparser/AbstractExpression.java`** -> AI Confidence: **99.31%**
77. **`platforms/native/language-native/src/main/java/org/gradle/swiftpm/tasks/GenerateSwiftPackageManagerManifest.java`** -> AI Confidence: **99.31%**
78. **`platforms/software/build-init-specs/src/main/java/org/gradle/buildinit/specs/internal/BuildInitSpecRegistry.java`** -> AI Confidence: **99.31%**
79. **`platforms/software/build-init/src/main/java/org/gradle/api/tasks/wrapper/internal/GradleVersionResolver.java`** -> AI Confidence: **99.31%**
80. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/JvmApplicationProjectInitDescriptor.java`** -> AI Confidence: **99.31%**
81. **`platforms/software/build-init/src/main/java/org/gradle/unexported/buildinit/plugins/internal/maven/Maven2Gradle.java`** -> AI Confidence: **99.31%**
82. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/AbstractJVMVersionTooNewFailureDescriber.java`** -> AI Confidence: **99.31%**
83. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/ComponentSelectionRulesProcessor.java`** -> AI Confidence: **99.31%**
84. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/GradleModuleMetadataParser.java`** -> AI Confidence: **99.31%**
85. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/PomDomParser.java`** -> AI Confidence: **99.31%**
86. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/report/DependencyVerificationReportWriter.java`** -> AI Confidence: **99.31%**
87. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/writer/PgpKeyGrouper.java`** -> AI Confidence: **99.31%**
88. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/factories/Unions.java`** -> AI Confidence: **99.31%**
89. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/DependencyGraphPathResolver.java`** -> AI Confidence: **99.31%**
90. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/ComponentRejectedMessageBuilder.java`** -> AI Confidence: **99.31%**
91. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/DependencyGraphBuilder.java`** -> AI Confidence: **99.31%**
92. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/CapabilityConflictResolver.java`** -> AI Confidence: **99.31%**
93. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ComponentIdentifierSerializer.java`** -> AI Confidence: **99.31%**
94. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlReader.java`** -> AI Confidence: **99.31%**
95. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/verifier/DependencyVerifier.java`** -> AI Confidence: **99.31%**
96. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/immutable/ImmutableAttributesSchema.java`** -> AI Confidence: **99.31%**
97. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/immutable/artifact/ImmutableArtifactTypeRegistry.java`** -> AI Confidence: **99.31%**
98. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/matching/DefaultAttributeSelectionSchema.java`** -> AI Confidence: **99.31%**
99. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/DependencyMapNotationConverter.java`** -> AI Confidence: **99.31%**
100. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/DefaultConfigurationMetadata.java`** -> AI Confidence: **99.31%**
101. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ivy/IvyConfigurationHelper.java`** -> AI Confidence: **99.31%**
102. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ivy/IvyDependencyDescriptor.java`** -> AI Confidence: **99.31%**
103. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/AbstractResolutionFailureDescriber.java`** -> AI Confidence: **99.31%**
104. **`platforms/software/platform-base/src/main/java/org/gradle/language/base/internal/model/BinarySourceTransformations.java`** -> AI Confidence: **99.31%**
105. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/registry/ModelMapBasedRule.java`** -> AI Confidence: **99.31%**
106. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/ApacheDirectoryListingParser.java`** -> AI Confidence: **99.31%**
107. **`platforms/software/resources/src/main/java/org/gradle/internal/resource/ExternalResourceName.java`** -> AI Confidence: **99.31%**
108. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/configurations/model/ConfigurationReportModelFactory.java`** -> AI Confidence: **99.31%**
109. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/junit/result/TestEventReporterAsListener.java`** -> AI Confidence: **99.31%**
110. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/TestTreeModel.java`** -> AI Confidence: **99.31%**
111. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/TestState.java`** -> AI Confidence: **99.31%**
112. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/serializable/TestOutputReader.java`** -> AI Confidence: **99.31%**
113. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/serializable/TestOutputWriter.java`** -> AI Confidence: **99.31%**
114. **`subprojects/core-api/src/main/java/org/gradle/api/internal/cache/CacheDirUtil.java`** -> AI Confidence: **99.31%**
115. **`subprojects/core/src/main/java/org/gradle/api/internal/attributes/DefaultImmutableAttributesContainer.java`** -> AI Confidence: **99.31%**
116. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/DefaultSharedModelDefaults.java`** -> AI Confidence: **99.31%**
117. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/DefaultTaskRequiredServices.java`** -> AI Confidence: **99.31%**
118. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/ExecuteTaskBuildOperationResult.java`** -> AI Confidence: **99.31%**
119. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/ValidationActions.java`** -> AI Confidence: **99.31%**
120. **`subprojects/core/src/main/java/org/gradle/api/services/internal/BuildServiceRegistryInternal.java`** -> AI Confidence: **99.31%**
121. **`subprojects/core/src/main/java/org/gradle/execution/plan/DefaultFinalizedExecutionPlan.java`** -> AI Confidence: **99.31%**
122. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/GradleResolveVisitor.java`** -> AI Confidence: **99.31%**
123. **`subprojects/core/src/main/java/org/gradle/initialization/exception/DefaultExceptionAnalyser.java`** -> AI Confidence: **99.31%**
124. **`subprojects/core/src/main/java/org/gradle/internal/operations/DefaultBuildOperationQueue.java`** -> AI Confidence: **99.31%**
125. **`subprojects/core/src/main/java/org/gradle/internal/work/DefaultAsyncWorkTracker.java`** -> AI Confidence: **99.31%**
126. **`subprojects/core/src/main/java/org/gradle/plugin/use/internal/PluginUseScriptBlockMetadataCompiler.java`** -> AI Confidence: **99.31%**
127. **`subprojects/core/src/main/java/org/gradle/util/internal/NameMatcher.java`** -> AI Confidence: **99.31%**
128. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/compatibility/AbstractContextualMultiVersionTestInterceptor.java`** -> AI Confidence: **99.31%**
129. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/daemon/DaemonContextParser.java`** -> AI Confidence: **99.31%**
130. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/OutputScrapingExecutionFailure.java`** -> AI Confidence: **99.31%**
131. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/ResultAssertion.java`** -> AI Confidence: **99.31%**
132. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/logging/GroupedOutputFixture.java`** -> AI Confidence: **99.31%**
133. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/logging/comparison/DiffUtils.java`** -> AI Confidence: **99.31%**
134. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/ChainingHttpHandler.java`** -> AI Confidence: **99.31%**
135. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/ExpectMaxNConcurrentRequests.java`** -> AI Confidence: **99.31%**
136. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/SendPartialResponseThenBlock.java`** -> AI Confidence: **99.31%**
137. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/measure/DataSeries.java`** -> AI Confidence: **99.31%**
138. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/BaseCrossBuildResultsStore.java`** -> AI Confidence: **99.31%**
139. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/AbstractTablePageGenerator.java`** -> AI Confidence: **99.31%**
140. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/DefaultPerformanceExecutionDataProvider.java`** -> AI Confidence: **99.31%**
141. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/IndexPageGenerator.java`** -> AI Confidence: **99.31%**
142. **`.teamcity/src/main/kotlin/model/FunctionalTestBucketGenerator.kt`** -> AI Confidence: **99.31%**
143. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.cache-miss-monitor.gradle.kts`** -> AI Confidence: **99.31%**
144. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/sources/KotlinSourceQueries.kt`** -> AI Confidence: **99.31%**
145. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/runtimes/CheckTargetRuntimes.kt`** -> AI Confidence: **99.31%**
146. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/GenerateLicenseFile.kt`** -> AI Confidence: **99.31%**
147. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/buildtree/control/BuildModelParametersProvider.kt`** -> AI Confidence: **99.31%**
148. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/DefaultClassDecoder.kt`** -> AI Confidence: **99.31%**
149. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/FunctionCallResolver.kt`** -> AI Confidence: **99.31%**
150. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/StatementResolver.kt`** -> AI Confidence: **99.31%**
151. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/utils.kt`** -> AI Confidence: **99.31%**
152. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/DataStructuralEquality.kt`** -> AI Confidence: **99.31%**
153. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/FunctionBinding.kt`** -> AI Confidence: **99.31%**
154. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ClassMembersForSchema.kt`** -> AI Confidence: **99.31%**
155. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaUtils/AnalysisSchemaUtils.kt`** -> AI Confidence: **99.31%**
156. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/MutatedDocumentTextGeneratorTest.kt`** -> AI Confidence: **99.31%**
157. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/Lexer.kt`** -> AI Confidence: **99.31%**
158. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/internal/GradleDistRepoDescriptorLocator.kt`** -> AI Confidence: **99.31%**
159. **`platforms/core-configuration/base-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/HelpTaskIntegrationTest.groovy`** -> AI Confidence: **99.31%**
160. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/fixtures/BuildLogicChangeFixture.groovy`** -> AI Confidence: **99.31%**
161. **`platforms/core-configuration/declarative-dsl-provider/src/integTest/groovy/org/gradle/internal/declarativedsl/settings/ProjectTypeModelDefaultsIntegrationTest.groovy`** -> AI Confidence: **99.31%**
162. **`platforms/core-runtime/logging/src/test/groovy/org/gradle/internal/deprecation/DeprecationMessagesTest.groovy`** -> AI Confidence: **99.31%**
163. **`platforms/core-runtime/process-services/src/integTest/groovy/org/gradle/process/internal/CancellationBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.31%**
164. **`platforms/native/platform-native/src/testFixtures/groovy/org/gradle/nativeplatform/fixtures/NativeBinaryFixture.groovy`** -> AI Confidence: **99.31%**
165. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/internal/component/resolution/failure/ResolutionFailureHandlerIntegrationTest.groovy`** -> AI Confidence: **99.31%**
166. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/caching/RecoverFromBrokenResolutionIntegrationTest.groovy`** -> AI Confidence: **99.31%**
167. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyBrokenRemoteResolveIntegrationTest.groovy`** -> AI Confidence: **99.31%**
168. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationIntegrityCheckIntegTest.groovy`** -> AI Confidence: **99.31%**
169. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy`** -> AI Confidence: **99.31%**
170. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/tasks/userinput/UserInputHandlingIntegrationTest.groovy`** -> AI Confidence: **99.31%**
171. **`subprojects/core/src/integTest/groovy/org/gradle/internal/operations/notify/BuildOperationNotificationFixture.groovy`** -> AI Confidence: **99.31%**
172. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/GradleModuleMetadata.groovy`** -> AI Confidence: **99.31%**
173. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractContinuousIntegrationTest.groovy`** -> AI Confidence: **99.31%**
174. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/BuildOperationTreeQueries.groovy`** -> AI Confidence: **99.31%**
175. **`testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/ConcurrentTestUtil.groovy`** -> AI Confidence: **99.31%**
176. **`platforms/core-runtime/daemon-logging/src/main/java/org/gradle/launcher/daemon/logging/DaemonMessages.java`** -> AI Confidence: **99.29%**
177. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/internal/EclipseJavaVersionMapper.java`** -> AI Confidence: **99.29%**
178. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.build-logic.groovy-dsl-gradle-plugin.gradle.kts`** -> AI Confidence: **99.29%**
179. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.test-retry.gradle.kts`** -> AI Confidence: **99.29%**
180. **`build-logic/root-build/src/main/kotlin/gradlebuild.warmup-ec2.gradle.kts`** -> AI Confidence: **99.29%**
181. **`build-logic/uber-plugins/src/main/kotlin/gradlebuild.distribution.api-java.gradle.kts`** -> AI Confidence: **99.29%**
182. **`build-logic/uber-plugins/src/main/kotlin/gradlebuild.distribution.uninstrumented.api-java.gradle.kts`** -> AI Confidence: **99.29%**
183. **`testing/performance/src/templates/kts-empty/build.gradle.kts`** -> AI Confidence: **99.29%**
184. **`platforms/core-runtime/launcher/src/testFixtures/groovy/org/gradle/launcher/cli/HelpFixture.groovy`** -> AI Confidence: **99.29%**
185. **`platforms/enterprise/enterprise-plugin-performance/src/templates/project-with-source/build.gradle`** -> AI Confidence: **99.29%**
186. **`platforms/ide/ide-plugins/src/integTest/resources/org/gradle/plugins/ide/eclipse/EclipseIntegrationTest/canCreateAndDeleteMetaData/build.gradle`** -> AI Confidence: **99.29%**
187. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/fixture/ProblemsApiGroovyScriptUtils.groovy`** -> AI Confidence: **99.29%**
188. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/compileJavaFx8Code/build.gradle`** -> AI Confidence: **99.29%**
189. **`platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractBasicGroovyCompilerIntegrationSpec/useConfigurationScript/build.gradle`** -> AI Confidence: **99.29%**
190. **`platforms/software/dependency-management/src/integTest/resources/org/gradle/integtests/resolve/ArtifactDependenciesIntegrationTest/dependencyReportWithConflicts/subproject/build.gradle`** -> AI Confidence: **99.29%**
191. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/DistributionPropertiesLoaderIntegrationTest.groovy`** -> AI Confidence: **99.29%**
192. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/gradle/GradleFileModuleAdapter.groovy`** -> AI Confidence: **99.29%**
193. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/InspectsConfigurationReport.groovy`** -> AI Confidence: **99.29%**
194. **`testing/internal-performance-testing/src/templates/root-project/build.gradle`** -> AI Confidence: **99.29%**
195. **`testing/internal-testing/src/main/resources/GradleBuildSpockConfig.groovy`** -> AI Confidence: **99.29%**
196. **`testing/performance/src/templates/config-inject/build.gradle`** -> AI Confidence: **99.29%**
197. **`testing/performance/src/templates/cpp-project/build.gradle`** -> AI Confidence: **99.29%**
198. **`testing/performance/src/templates/generateLotsOfDeprecationWarnings/build.gradle`** -> AI Confidence: **99.29%**
199. **`testing/performance/src/templates/native-dependents/build.gradle`** -> AI Confidence: **99.29%**
200. **`testing/performance/src/templates/native-monolithic/common.gradle`** -> AI Confidence: **99.29%**
201. **`testing/performance/src/templates/native-monolithic/prebuilt.gradle`** -> AI Confidence: **99.29%**
202. **`testing/performance/src/templates/native-pch-component/build.gradle`** -> AI Confidence: **99.29%**
203. **`testing/performance/src/templates/project-with-source/build.gradle`** -> AI Confidence: **99.29%**
204. **`testing/performance/src/templates/task-creation/build.gradle`** -> AI Confidence: **99.29%**
205. **`testing/smoke-test/src/smokeTest/resources/org/gradle/play/integtest/fixtures/external/shared/public/javascripts/hello.js`** -> AI Confidence: **99.29%**
206. **`testing/smoke-test/src/smokeTest/resources/org/gradle/smoketests/play-example/public/javascripts/hello.js`** -> AI Confidence: **99.29%**
207. **`testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-death-test-internal.h`** -> AI Confidence: **99.29%**
208. **`.teamcity/scripts/CheckWrapper.java`** -> AI Confidence: **99.24%**
209. **`.teamcity/scripts/FindCommits.java`** -> AI Confidence: **99.24%**
210. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/ProjectReportTask.java`** -> AI Confidence: **99.24%**
211. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/AggregateMultiProjectTaskReportModel.java`** -> AI Confidence: **99.24%**
212. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/text/DefaultTextReportBuilder.java`** -> AI Confidence: **99.24%**
213. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/CalculatedTaskInputFileCollection.java`** -> AI Confidence: **99.24%**
214. **`platforms/core-configuration/input-tracking/src/main/java/org/gradle/internal/configuration/inputs/AccessTrackingProperties.java`** -> AI Confidence: **99.24%**
215. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/ProviderInternal.java`** -> AI Confidence: **99.24%**
216. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/DelegatingJavaExecSpec.java`** -> AI Confidence: **99.24%**
217. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/extensibility/ExtensionsStorage.java`** -> AI Confidence: **99.24%**
218. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AbstractClassGenerator.java`** -> AI Confidence: **99.24%**
219. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/managed/DefaultManagedObjectRegistry.java`** -> AI Confidence: **99.24%**
220. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/metaobject/BeanDynamicObject.java`** -> AI Confidence: **99.24%**
221. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/properties/annotations/DefaultTypeMetadataStore.java`** -> AI Confidence: **99.24%**
222. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/DefaultIsolatableFactory.java`** -> AI Confidence: **99.24%**
223. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/ModelRuleSourceDetector.java`** -> AI Confidence: **99.24%**
224. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/RuleDefinitionRuleExtractor.java`** -> AI Confidence: **99.24%**
225. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/binding/DefaultStructBindings.java`** -> AI Confidence: **99.24%**
226. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/AbstractStructSchema.java`** -> AI Confidence: **99.24%**
227. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/ModelProperty.java`** -> AI Confidence: **99.24%**
228. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/BindingPredicate.java`** -> AI Confidence: **99.24%**
229. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/ModelGraph.java`** -> AI Confidence: **99.24%**
230. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/UnboundRulesProcessor.java`** -> AI Confidence: **99.24%**
231. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/type/ModelTypes.java`** -> AI Confidence: **99.24%**
232. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/typeregistration/BaseInstanceFactory.java`** -> AI Confidence: **99.24%**
233. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/JavaPropertyReflectionUtil.java`** -> AI Confidence: **99.24%**
234. **`platforms/core-execution/build-cache-http/src/main/java/org/gradle/caching/http/internal/HttpBuildCacheService.java`** -> AI Confidence: **99.24%**
235. **`platforms/core-execution/daemon-server-worker/src/main/java/org/gradle/workers/internal/DefaultWorkerServer.java`** -> AI Confidence: **99.24%**
236. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/OutputsCleaner.java`** -> AI Confidence: **99.24%**
237. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/changes/IgnoredPathCompareStrategy.java`** -> AI Confidence: **99.24%**
238. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/model/annotations/AbstractInputPropertyAnnotationHandler.java`** -> AI Confidence: **99.24%**
239. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/DefaultCacheCoordinator.java`** -> AI Confidence: **99.24%**
240. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/ExclusiveCacheAccessingWorker.java`** -> AI Confidence: **99.24%**
241. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/FixedSharedModeCrossProcessCacheAccess.java`** -> AI Confidence: **99.24%**
242. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/InMemoryDecoratedCache.java`** -> AI Confidence: **99.24%**
243. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/locklistener/DefaultFileLockContentionHandler.java`** -> AI Confidence: **99.24%**
244. **`platforms/core-execution/snapshots/src/main/java/org/gradle/internal/snapshot/DirectorySnapshot.java`** -> AI Confidence: **99.24%**
245. **`platforms/core-execution/worker-process-services/src/main/java/org/gradle/process/internal/worker/DefaultWorkerProcess.java`** -> AI Confidence: **99.24%**
246. **`platforms/core-execution/worker-process-services/src/main/java/org/gradle/process/internal/worker/child/ApplicationClassesInSystemClassLoaderWorkerImplementationFactory.java`** -> AI Confidence: **99.24%**
247. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/IoActions.java`** -> AI Confidence: **99.24%**
248. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/graph/CachingDirectedGraphWalker.java`** -> AI Confidence: **99.24%**
249. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/resources/DefaultResourceLockCoordinationService.java`** -> AI Confidence: **99.24%**
250. **`platforms/core-runtime/base-services/src/main/java/org/gradle/util/internal/DefaultGradleVersion.java`** -> AI Confidence: **99.24%**
251. **`platforms/core-runtime/build-discovery/src/main/java/org/gradle/internal/scripts/DefaultScriptFileResolver.java`** -> AI Confidence: **99.24%**
252. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/ClasspathUtil.java`** -> AI Confidence: **99.24%**
253. **`platforms/core-runtime/cli/src/main/java/org/gradle/cli/CommandLineParser.java`** -> AI Confidence: **99.24%**
254. **`platforms/core-runtime/client-services/src/main/java/org/gradle/internal/daemon/client/serialization/ClasspathInferer.java`** -> AI Confidence: **99.24%**
255. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/client/ReportDaemonStatusClient.java`** -> AI Confidence: **99.24%**
256. **`platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentMapTrie.java`** -> AI Confidence: **99.24%**
257. **`platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentSetTrie.java`** -> AI Confidence: **99.24%**
258. **`platforms/core-runtime/concurrent/src/main/java/org/gradle/internal/concurrent/CompositeStoppable.java`** -> AI Confidence: **99.24%**
259. **`platforms/core-runtime/files/src/main/java/org/gradle/internal/file/impl/DefaultDeleter.java`** -> AI Confidence: **99.24%**
260. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/InstrumentationCodeGeneratorHost.java`** -> AI Confidence: **99.24%**
261. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/groovy/MatchesSignatureGeneratingSignatureTreeVisitor.java`** -> AI Confidence: **99.24%**
262. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/modelreader/impl/TypeUtils.java`** -> AI Confidence: **99.24%**
263. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DefaultDaemonConnection.java`** -> AI Confidence: **99.24%**
264. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DefaultIncomingConnectionHandler.java`** -> AI Confidence: **99.24%**
265. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/EstablishBuildEnvironment.java`** -> AI Confidence: **99.24%**
266. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/health/HealthExpirationStrategy.java`** -> AI Confidence: **99.24%**
267. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/event/DefaultListenerManager.java`** -> AI Confidence: **99.24%**
268. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/hub/queue/MultiEndPointQueue.java`** -> AI Confidence: **99.24%**
269. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/inet/InetAddresses.java`** -> AI Confidence: **99.24%**
270. **`platforms/core-runtime/native/src/main/java/org/gradle/platform/internal/CurrentBuildPlatform.java`** -> AI Confidence: **99.24%**
271. **`platforms/core-runtime/process-memory-services/src/main/java/org/gradle/process/internal/health/memory/MemInfoOsMemoryInfo.java`** -> AI Confidence: **99.24%**
272. **`platforms/core-runtime/process-services-base/src/main/java/org/gradle/process/internal/ExecHandleRunner.java`** -> AI Confidence: **99.24%**
273. **`platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/JvmOptions.java`** -> AI Confidence: **99.24%**
274. **`platforms/core-runtime/serialization/src/main/java/org/gradle/internal/serialize/ExceptionSerializationUtil.java`** -> AI Confidence: **99.24%**
275. **`platforms/core-runtime/serialization/src/main/java/org/gradle/internal/serialize/kryo/StringDeduplicatingKryoBackedDecoder.java`** -> AI Confidence: **99.24%**
276. **`platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/RelevantMethods.java`** -> AI Confidence: **99.24%**
277. **`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/util/internal/CollectionUtils.java`** -> AI Confidence: **99.24%**
278. **`platforms/core-runtime/wrapper-shared/src/main/java/org/gradle/util/internal/WrapperCredentials.java`** -> AI Confidence: **99.24%**
279. **`platforms/core-runtime/wrapper-shared/src/main/java/org/gradle/wrapper/PropertiesFileHandler.java`** -> AI Confidence: **99.24%**
280. **`platforms/enterprise/enterprise/src/main/java/org/gradle/internal/enterprise/exceptions/ExceptionMetadataHelper.java`** -> AI Confidence: **99.24%**
281. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/features/internal/binding/DefaultProjectFeatureImplementation.java`** -> AI Confidence: **99.24%**
282. **`platforms/ide/ide-plugins/src/main/java/org/gradle/plugins/ide/internal/tooling/EclipseModelBuilder.java`** -> AI Confidence: **99.24%**
283. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/Classpath.java`** -> AI Confidence: **99.24%**
284. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/internal/SourceFoldersCreator.java`** -> AI Confidence: **99.24%**
285. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/idea/model/Module.java`** -> AI Confidence: **99.24%**
286. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/configurer/HierarchicalElementDeduplicator.java`** -> AI Confidence: **99.24%**
287. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/resolver/IdeDependencySet.java`** -> AI Confidence: **99.24%**
288. **`platforms/ide/problems-api/src/main/java/org/gradle/api/problems/internal/ExceptionProblemRegistry.java`** -> AI Confidence: **99.24%**
289. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/ClientBuildEventGenerator.java`** -> AI Confidence: **99.24%**
290. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/TestExecutionBuildConfigurationAction.java`** -> AI Confidence: **99.24%**
291. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/TestExecutionResultEvaluator.java`** -> AI Confidence: **99.24%**
292. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/adapter/ProtocolToModelAdapter.java`** -> AI Confidence: **99.24%**
293. **`platforms/jvm/code-quality-workers/src/main/java/org/gradle/api/plugins/quality/internal/CheckstyleInvoker.java`** -> AI Confidence: **99.24%**
294. **`platforms/jvm/code-quality-workers/src/main/java/org/gradle/api/plugins/quality/internal/CodeNarcInvoker.java`** -> AI Confidence: **99.24%**
295. **`platforms/jvm/code-quality/src/main/java/org/gradle/api/plugins/quality/PmdPlugin.java`** -> AI Confidence: **99.24%**
296. **`platforms/jvm/ear/src/main/java/org/gradle/plugins/ear/descriptor/internal/DefaultDeploymentDescriptor.java`** -> AI Confidence: **99.24%**
297. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/processing/AggregatingProcessingStrategy.java`** -> AI Confidence: **99.24%**
298. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/deps/ClassDependentsAccumulator.java`** -> AI Confidence: **99.24%**
299. **`platforms/jvm/platform-jvm/src/main/java/org/gradle/api/java/archives/internal/DefaultManifestMergeSpec.java`** -> AI Confidence: **99.24%**
300. **`platforms/jvm/plugins-groovy/src/main/java/org/gradle/api/internal/plugins/GroovyJarFile.java`** -> AI Confidence: **99.24%**
301. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/junit/DescriptionMap.java`** -> AI Confidence: **99.24%**
302. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/junitplatform/filters/ClassMethodNameFilter.java`** -> AI Confidence: **99.24%**
303. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/testng/TestNGListenerAdapterFactory.java`** -> AI Confidence: **99.24%**
304. **`platforms/jvm/toolchains-jvm-shared/src/main/java/org/gradle/jvm/toolchain/internal/install/DefaultJdkCacheDirectory.java`** -> AI Confidence: **99.24%**
305. **`platforms/native/language-native/src/main/java/org/gradle/language/internal/DefaultBinaryCollection.java`** -> AI Confidence: **99.24%**
306. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/DefaultSourceIncludesResolver.java`** -> AI Confidence: **99.24%**
307. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/sourceparser/IncludeDirectivesSerializer.java`** -> AI Confidence: **99.24%**
308. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/gcc/metadata/GccMetadataProvider.java`** -> AI Confidence: **99.24%**
309. **`platforms/native/testing-native/src/main/java/org/gradle/nativeplatform/test/xctest/internal/execution/XCTestScraper.java`** -> AI Confidence: **99.24%**
310. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/LanguageSpecificAdaptor.java`** -> AI Confidence: **99.24%**
311. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dependencies/DefaultResolvedVersionConstraint.java`** -> AI Confidence: **99.24%**
312. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/DynamicAddDependencyMethods.java`** -> AI Confidence: **99.24%**
313. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/DefaultIvyContextManager.java`** -> AI Confidence: **99.24%**
314. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/RepositoryChainComponentMetaDataResolver.java`** -> AI Confidence: **99.24%**
315. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyXmlModuleDescriptorParser.java`** -> AI Confidence: **99.24%**
316. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/PomReader.java`** -> AI Confidence: **99.24%**
317. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/report/HtmlDependencyVerificationReportRenderer.java`** -> AI Confidence: **99.24%**
318. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/LatestModuleConflictResolver.java`** -> AI Confidence: **99.24%**
319. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/ModuleResolveState.java`** -> AI Confidence: **99.24%**
320. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/NodeState.java`** -> AI Confidence: **99.24%**
321. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/oldresult/TransientConfigurationResultsBuilder.java`** -> AI Confidence: **99.24%**
322. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/DefaultMavenRepositoryContentDescriptor.java`** -> AI Confidence: **99.24%**
323. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/ResourceVersionLister.java`** -> AI Confidence: **99.24%**
324. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/immutable/ImmutableAttributesSchemaFactory.java`** -> AI Confidence: **99.24%**
325. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/matching/AttributeSelectionSchema.java`** -> AI Confidence: **99.24%**
326. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/matching/CachingAttributeSelectionSchema.java`** -> AI Confidence: **99.24%**
327. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/matching/DefaultAttributeMatcher.java`** -> AI Confidence: **99.24%**
328. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/catalog/LibrariesSourceGenerator.java`** -> AI Confidence: **99.24%**
329. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/GraphVariantSelector.java`** -> AI Confidence: **99.24%**
330. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/ResolutionCandidateAssessor.java`** -> AI Confidence: **99.24%**
331. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/IncompatibleMultipleNodesValidationFailureDescriber.java`** -> AI Confidence: **99.24%**
332. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/NoCompatibleVariantsFailureDescriber.java`** -> AI Confidence: **99.24%**
333. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/locking/DependencyLockingGraphVisitor.java`** -> AI Confidence: **99.24%**
334. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/locking/LockFileReaderWriter.java`** -> AI Confidence: **99.24%**
335. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resolve/ModuleVersionNotFoundException.java`** -> AI Confidence: **99.24%**
336. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/validation/MavenPublicationErrorChecker.java`** -> AI Confidence: **99.24%**
337. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/VariantAspectExtractionStrategy.java`** -> AI Confidence: **99.24%**
338. **`platforms/software/plugins-version-catalog/src/main/java/org/gradle/api/plugins/catalog/internal/DependenciesAwareVersionCatalogBuilder.java`** -> AI Confidence: **99.24%**
339. **`platforms/software/plugins-version-catalog/src/main/java/org/gradle/api/plugins/catalog/internal/TomlWriter.java`** -> AI Confidence: **99.24%**
340. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/metadata/ModuleMetadataJsonWriter.java`** -> AI Confidence: **99.24%**
341. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/metadata/ModuleMetadataSpecBuilder.java`** -> AI Confidence: **99.24%**
342. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/SystemDefaultSSLContextFactory.java`** -> AI Confidence: **99.24%**
343. **`platforms/software/resources/src/main/java/org/gradle/internal/resource/UriTextResource.java`** -> AI Confidence: **99.24%**
344. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/components/internal/TypeAwareBinaryRenderer.java`** -> AI Confidence: **99.24%**
345. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/insight/DependencyInsightReporter.java`** -> AI Confidence: **99.24%**
346. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/junit/result/JUnitXmlResultWriter.java`** -> AI Confidence: **99.24%**
347. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/logging/AbstractTestLogger.java`** -> AI Confidence: **99.24%**
348. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/logging/FullExceptionFormatter.java`** -> AI Confidence: **99.24%**
349. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/logging/SimpleTestEventLogger.java`** -> AI Confidence: **99.24%**
350. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/TestTreeModelResultsProvider.java`** -> AI Confidence: **99.24%**
351. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/serializable/SerializableTestResultStore.java`** -> AI Confidence: **99.24%**
352. **`subprojects/core-api/src/main/java/org/gradle/api/artifacts/dsl/Dependencies.java`** -> AI Confidence: **99.24%**
353. **`subprojects/core-api/src/main/java/org/gradle/api/reflect/TypeOf.java`** -> AI Confidence: **99.24%**
354. **`subprojects/core-api/src/main/java/org/gradle/model/internal/type/ModelType.java`** -> AI Confidence: **99.24%**
355. **`subprojects/core/src/main/java/org/gradle/api/internal/attributes/DefaultMutableAttributeContainer.java`** -> AI Confidence: **99.24%**
356. **`subprojects/core/src/main/java/org/gradle/api/internal/catalog/parser/TomlCatalogFileParser.java`** -> AI Confidence: **99.24%**
357. **`subprojects/core/src/main/java/org/gradle/api/internal/collections/DefaultCollectionEventRegister.java`** -> AI Confidence: **99.24%**
358. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/DefaultClassLoaderScope.java`** -> AI Confidence: **99.24%**
359. **`subprojects/core/src/main/java/org/gradle/api/internal/plugins/DefaultPluginManager.java`** -> AI Confidence: **99.24%**
360. **`subprojects/core/src/main/java/org/gradle/api/internal/plugins/DefaultPluginRegistry.java`** -> AI Confidence: **99.24%**
361. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/BaseSnapshotInputsBuildOperationResult.java`** -> AI Confidence: **99.24%**
362. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/SkipOnlyIfTaskExecuter.java`** -> AI Confidence: **99.24%**
363. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/options/OptionReader.java`** -> AI Confidence: **99.24%**
364. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/CompositePropertyVisitor.java`** -> AI Confidence: **99.24%**
365. **`subprojects/core/src/main/java/org/gradle/api/services/internal/DefaultBuildServicesRegistry.java`** -> AI Confidence: **99.24%**
366. **`subprojects/core/src/main/java/org/gradle/cache/internal/DaemonLogCleanupAction.java`** -> AI Confidence: **99.24%**
367. **`subprojects/core/src/main/java/org/gradle/cache/internal/WrapperDistributionCleanupAction.java`** -> AI Confidence: **99.24%**
368. **`subprojects/core/src/main/java/org/gradle/execution/commandline/CommandLineTaskConfigurer.java`** -> AI Confidence: **99.24%**
369. **`subprojects/core/src/main/java/org/gradle/execution/plan/DefaultPlanExecutor.java`** -> AI Confidence: **99.24%**
370. **`subprojects/core/src/main/java/org/gradle/execution/plan/FinalizerGroup.java`** -> AI Confidence: **99.24%**
371. **`subprojects/core/src/main/java/org/gradle/internal/buildevents/ContextAwareExceptionHandler.java`** -> AI Confidence: **99.24%**
372. **`subprojects/core/src/main/java/org/gradle/internal/classpath/CallInterceptingMetaClass.java`** -> AI Confidence: **99.24%**
373. **`subprojects/core/src/main/java/org/gradle/internal/classpath/transforms/AdhocInterceptors.java`** -> AI Confidence: **99.24%**
374. **`subprojects/core/src/testFixtures/groovy/org/gradle/util/internal/MultithreadedTestRule.java`** -> AI Confidence: **99.24%**
375. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/ExecutionFailureWithThrowable.java`** -> AI Confidence: **99.24%**
376. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/OutputScrapingExecutionResult.java`** -> AI Confidence: **99.24%**
377. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/extensions/AbstractMultiTestInterceptor.java`** -> AI Confidence: **99.24%**
378. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/GradleBackedArtifactBuilder.java`** -> AI Confidence: **99.24%**
379. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/CrossVersionResultsStore.java`** -> AI Confidence: **99.24%**
380. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/DefaultReportGenerator.java`** -> AI Confidence: **99.24%**
381. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/FlakinessDetectionPerformanceExecutionDataProvider.java`** -> AI Confidence: **99.24%**
382. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/HtmlPageGenerator.java`** -> AI Confidence: **99.24%**
383. **`.teamcity/src/main/kotlin/configurations/PerformanceTestsPass.kt`** -> AI Confidence: **99.24%**
384. **`build-logic-commons/module-identity/src/main/kotlin/gradlebuild/identity/provider/BuildTimestampValueSource.kt`** -> AI Confidence: **99.24%**
385. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateFixedIssuesInReleaseNotes.kt`** -> AI Confidence: **99.24%**
386. **`build-logic/cleanup/src/main/kotlin/gradlebuild/cleanup/Cleanup.kt`** -> AI Confidence: **99.24%**
387. **`build-logic/performance-testing/src/main/kotlin/gradlebuild/performance/tasks/BuildCommitDistribution.kt`** -> AI Confidence: **99.24%**
388. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/fingerprint/ConfigurationCacheFingerprintChecker.kt`** -> AI Confidence: **99.24%**
389. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/problems/ConfigurationCacheProblemsSummary.kt`** -> AI Confidence: **99.24%**
390. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ParallelStringDecoder.kt`** -> AI Confidence: **99.24%**
391. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/NamedReferenceResolver.kt`** -> AI Confidence: **99.24%**
392. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/DefaultModelToDocumentMutationPlanner.kt`** -> AI Confidence: **99.24%**
393. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/DeclarativeRuntimeFunction.kt`** -> AI Confidence: **99.24%**
394. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/RuntimeFunctionResolver.kt`** -> AI Confidence: **99.24%**
395. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/objectGraph/PropertyLinksResolver.kt`** -> AI Confidence: **99.24%**
396. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/GrammarToTree.kt`** -> AI Confidence: **99.24%**
397. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/LightTreeUtil.kt`** -> AI Confidence: **99.24%**
398. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/FunctionExtractor.kt`** -> AI Confidence: **99.24%**
399. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/ndoc/DclContainerMemberExtractionUtils.kt`** -> AI Confidence: **99.24%**
400. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/PrecompiledScriptPlugin.kt`** -> AI Confidence: **99.24%**
401. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/OptInAnnotationsCollector.kt`** -> AI Confidence: **99.24%**
402. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/PartialEvaluator.kt`** -> AI Confidence: **99.24%**
403. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/FindGradleSources.kt`** -> AI Confidence: **99.24%**
404. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/KotlinBuildScriptDependenciesResolver.kt`** -> AI Confidence: **99.24%**
405. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/rules/NullabilityBreakingChangesRule.groovy`** -> AI Confidence: **99.24%**
406. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/BuildEnvironmentIntegrationTest.groovy`** -> AI Confidence: **99.24%**
407. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/DeprecationHandlingIntegrationTest.groovy`** -> AI Confidence: **99.24%**
408. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/CancellationSpec.groovy`** -> AI Confidence: **99.24%**
409. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/PhasedBuildActionCrossVersionSpec.groovy`** -> AI Confidence: **99.24%**
410. **`platforms/jvm/ear/src/test/groovy/org/gradle/plugins/ear/descriptor/internal/DefaultDeploymentDescriptorTest.groovy`** -> AI Confidence: **99.24%**
411. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/platform/BinaryNativePlatformIntegrationTest.groovy`** -> AI Confidence: **99.24%**
412. **`platforms/software/build-init/src/testFixtures/groovy/org/gradle/buildinit/plugins/fixtures/ScriptDslFixture.groovy`** -> AI Confidence: **99.24%**
413. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/DependencyUnresolvedModuleIntegrationTest.groovy`** -> AI Confidence: **99.24%**
414. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ConfigurationRolesIntegrationTest.groovy`** -> AI Confidence: **99.24%**
415. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/suppliers/DynamicRevisionRemoteResolveWithMetadataSupplierIntegrationTest.groovy`** -> AI Confidence: **99.24%**
416. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/simple/DefaultCompositeExcludeTest.groovy`** -> AI Confidence: **99.24%**
417. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlWriterTest.groovy`** -> AI Confidence: **99.24%**
418. **`platforms/software/maven/src/testFixtures/groovy/org/gradle/integtests/fixtures/publish/maven/AbstractMavenPublishIntegTest.groovy`** -> AI Confidence: **99.24%**
419. **`platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/maven/MavenS3RepoErrorsIntegrationTest.groovy`** -> AI Confidence: **99.24%**
420. **`subprojects/core/src/integTest/groovy/org/gradle/initialization/buildsrc/BuildSrcIdentityIntegrationTest.groovy`** -> AI Confidence: **99.24%**
421. **`subprojects/core/src/integTest/groovy/org/gradle/plugin/ScriptPluginClassLoadingIntegrationTest.groovy`** -> AI Confidence: **99.24%**
422. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/TaskErrorExecutionIntegrationTest.groovy`** -> AI Confidence: **99.24%**
423. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/ProcessFixture.groovy`** -> AI Confidence: **99.24%**
424. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/ivy/IvyFileModule.groovy`** -> AI Confidence: **99.24%**
425. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/maven/AbstractMavenModule.groovy`** -> AI Confidence: **99.24%**
426. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/BuildOperationNotificationsFixture.groovy`** -> AI Confidence: **99.24%**
427. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/ToBeFixedSpecInterceptor.groovy`** -> AI Confidence: **99.24%**
428. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/nativeplatform/RealWorldNativePluginPerformanceTest.groovy`** -> AI Confidence: **99.24%**
429. **`platforms/core-configuration/base-services-groovy/src/main/java/org/gradle/api/specs/Specs.java`** -> AI Confidence: **99.23%**
430. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/AbstractCollectingSupplier.java`** -> AI Confidence: **99.23%**
431. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/MergeProvider.java`** -> AI Confidence: **99.23%**
432. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/DelegatingBaseExecSpec.java`** -> AI Confidence: **99.23%**
433. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/metaobject/AbstractDynamicObject.java`** -> AI Confidence: **99.23%**
434. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/properties/annotations/NestedValidationUtil.java`** -> AI Confidence: **99.23%**
435. **`platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeaturesDynamicObject.java`** -> AI Confidence: **99.23%**
436. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/PreCreateOutputParentsStep.java`** -> AI Confidence: **99.23%**
437. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/Actions.java`** -> AI Confidence: **99.23%**
438. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/process/ArgWriter.java`** -> AI Confidence: **99.23%**
439. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/reflect/JavaReflectionUtil.java`** -> AI Confidence: **99.23%**
440. **`platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentMap1.java`** -> AI Confidence: **99.23%**
441. **`platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentSet.java`** -> AI Confidence: **99.23%**
442. **`platforms/core-runtime/collections/src/main/java/org/gradle/internal/collect/PersistentSet1.java`** -> AI Confidence: **99.23%**
443. **`platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/context/DaemonCompatibilitySpec.java`** -> AI Confidence: **99.23%**
444. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/DefaultAnsiExecutor.java`** -> AI Confidence: **99.23%**
445. **`platforms/core-runtime/process-services-base/src/main/java/org/gradle/util/internal/DisconnectableInputStream.java`** -> AI Confidence: **99.23%**
446. **`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/reflect/JavaMethod.java`** -> AI Confidence: **99.23%**
447. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/idea/model/PathFactory.java`** -> AI Confidence: **99.23%**
448. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/idea/model/internal/IdeaDependenciesOptimizer.java`** -> AI Confidence: **99.23%**
449. **`platforms/jvm/jacoco/src/main/java/org/gradle/internal/jacoco/rules/JacocoViolationRuleImpl.java`** -> AI Confidence: **99.23%**
450. **`platforms/jvm/testing-jvm/src/main/java/org/gradle/api/internal/tasks/testing/detection/JarFilePackageLister.java`** -> AI Confidence: **99.23%**
451. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/AttributeDescriberSelector.java`** -> AI Confidence: **99.23%**
452. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resolve/RejectedByAttributesVersion.java`** -> AI Confidence: **99.23%**
453. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/DefaultBinaryNamingScheme.java`** -> AI Confidence: **99.23%**
454. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/registry/AbstractAnnotationDrivenComponentModelRuleExtractor.java`** -> AI Confidence: **99.23%**
455. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/registry/DefaultTypeBuilder.java`** -> AI Confidence: **99.23%**
456. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/graph/DependencyGraphsRenderer.java`** -> AI Confidence: **99.23%**
457. **`subprojects/core-api/src/main/java/org/gradle/api/file/RelativePath.java`** -> AI Confidence: **99.23%**
458. **`subprojects/core/src/main/java/org/gradle/execution/DefaultCancellableOperationManager.java`** -> AI Confidence: **99.23%**
459. **`subprojects/core/src/main/java/org/gradle/execution/plan/ActionNode.java`** -> AI Confidence: **99.23%**
460. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/TaskDefinitionScriptTransformer.java`** -> AI Confidence: **99.23%**
461. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/logging/comparison/ExhaustiveLinesSearcher.java`** -> AI Confidence: **99.23%**
462. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild.code-quality.gradle.kts`** -> AI Confidence: **99.23%**
463. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/ScopeLocationMatcher.kt`** -> AI Confidence: **99.23%**
464. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/demo/demoUtils.kt`** -> AI Confidence: **99.23%**
465. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/checks/AccessOnCurrentReceiverCheck.kt`** -> AI Confidence: **99.23%**
466. **`platforms/software/ivy/src/testFixtures/groovy/org/gradle/api/publish/ivy/AbstractIvyPublishIntegTest.groovy`** -> AI Confidence: **99.23%**
467. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyErrorIntegrationTest.groovy`** -> AI Confidence: **99.23%**
468. **`subprojects/core/src/test/groovy/org/gradle/internal/operations/logging/DefaultBuildOperationLoggerTest.groovy`** -> AI Confidence: **99.23%**
469. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/configurationcache/ConfigurationCacheFixture.groovy`** -> AI Confidence: **99.23%**
470. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/resolve/ResolveTestFixture.groovy`** -> AI Confidence: **99.23%**
471. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/WithExternalRepository.groovy`** -> AI Confidence: **99.23%**
472. **`build-logic-commons/code-quality-rules/src/main/java/gradlebuild/codenarc/rules/IntegrationTestFixtureVisitor.java`** -> AI Confidence: **99.18%**
473. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/AbstractProjectBasedReportTask.java`** -> AI Confidence: **99.18%**
474. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/ReportGenerator.java`** -> AI Confidence: **99.18%**
475. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/configuration/Help.java`** -> AI Confidence: **99.18%**
476. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchCustomModelForEachProjectInTree.java`** -> AI Confidence: **99.18%**
477. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/FetchParameterizedCustomModelForEachProject.java`** -> AI Confidence: **99.18%**
478. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AntFileCollectionBuilder.java`** -> AI Confidence: **99.18%**
479. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AntFileTreeBuilder.java`** -> AI Confidence: **99.18%**
480. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AttributeBasedFileVisitDetailsFactory.java`** -> AI Confidence: **99.18%**
481. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/FilteredFileCollection.java`** -> AI Confidence: **99.18%**
482. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/DefaultConfigurableFileCollection.java`** -> AI Confidence: **99.18%**
483. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/DirectoryFileTree.java`** -> AI Confidence: **99.18%**
484. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/ProviderBackedFileCollection.java`** -> AI Confidence: **99.18%**
485. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/DefaultFileSystemOperations.java`** -> AI Confidence: **99.18%**
486. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/DefaultSourceDirectorySet.java`** -> AI Confidence: **99.18%**
487. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/archive/TarCopyAction.java`** -> AI Confidence: **99.18%**
488. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/archive/TarFileTree.java`** -> AI Confidence: **99.18%**
489. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/archive/compression/GzipArchiver.java`** -> AI Confidence: **99.18%**
490. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/DefaultFileCopyDetails.java`** -> AI Confidence: **99.18%**
491. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/FilterChain.java`** -> AI Confidence: **99.18%**
492. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/resources/CharSourceBackedTextResource.java`** -> AI Confidence: **99.18%**
493. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/resources/FileCollectionBackedTextResource.java`** -> AI Confidence: **99.18%**
494. **`platforms/core-configuration/input-tracking/src/main/java/org/gradle/internal/configuration/inputs/AccessTrackingSet.java`** -> AI Confidence: **99.18%**
495. **`platforms/core-configuration/java-api-extractor/src/main/java/org/gradle/internal/tools/api/ApiClassExtractor.java`** -> AI Confidence: **99.18%**
496. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/model/NamedObjectInstantiator.java`** -> AI Confidence: **99.18%**
497. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/plugins/DslObject.java`** -> AI Confidence: **99.18%**
498. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/AppendOnceList.java`** -> AI Confidence: **99.18%**
499. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/CredentialsProviderFactory.java`** -> AI Confidence: **99.18%**
500. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/DefaultPropertyFactory.java`** -> AI Confidence: **99.18%**
501. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/DefaultSetProperty.java`** -> AI Confidence: **99.18%**
502. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/DefaultValueSourceProviderFactory.java`** -> AI Confidence: **99.18%**
503. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/ManagedFactories.java`** -> AI Confidence: **99.18%**
504. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/Providers.java`** -> AI Confidence: **99.18%**
505. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/MapWithPrefixedKeysValueSource.java`** -> AI Confidence: **99.18%**
506. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/AbstractTaskDependency.java`** -> AI Confidence: **99.18%**
507. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/extensibility/ExtensibleDynamicObject.java`** -> AI Confidence: **99.18%**
508. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/extensibility/MixInClosurePropertiesAsMethodsDynamicObject.java`** -> AI Confidence: **99.18%**
509. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/ClassGenerator.java`** -> AI Confidence: **99.18%**
510. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/ManagedObjectFactory.java`** -> AI Confidence: **99.18%**
511. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/isolated/IsolationScheme.java`** -> AI Confidence: **99.18%**
512. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/properties/StaticValue.java`** -> AI Confidence: **99.18%**
513. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/properties/bean/DefaultPropertyWalker.java`** -> AI Confidence: **99.18%**
514. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/GradleSerializedValueSnapshot.java`** -> AI Confidence: **99.18%**
515. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/snapshot/impl/JavaSerializedValueSnapshot.java`** -> AI Confidence: **99.18%**
516. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/NodeBackedModelMap.java`** -> AI Confidence: **99.18%**
517. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/NodeBackedModelSet.java`** -> AI Confidence: **99.18%**
518. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/AbstractModelCreationRuleExtractor.java`** -> AI Confidence: **99.18%**
519. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/AbstractMutationModelRuleExtractor.java`** -> AI Confidence: **99.18%**
520. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/MethodRuleDefinition.java`** -> AI Confidence: **99.18%**
521. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/CandidateMethods.java`** -> AI Confidence: **99.18%**
522. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/DefaultModelSchemaExtractionContext.java`** -> AI Confidence: **99.18%**
523. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ManagedImplStructStrategy.java`** -> AI Confidence: **99.18%**
524. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ModelPropertyExtractionContext.java`** -> AI Confidence: **99.18%**
525. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ModelSchemaAspectExtractor.java`** -> AI Confidence: **99.18%**
526. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ModelSchemaUtils.java`** -> AI Confidence: **99.18%**
527. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ModelSetStrategy.java`** -> AI Confidence: **99.18%**
528. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/RuleSourceSchemaExtractionStrategy.java`** -> AI Confidence: **99.18%**
529. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/SpecializedMapNodeInitializerExtractionStrategy.java`** -> AI Confidence: **99.18%**
530. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/UnmanagedImplStructStrategy.java`** -> AI Confidence: **99.18%**
531. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/DefaultModelRegistry.java`** -> AI Confidence: **99.18%**
532. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/RuleBinder.java`** -> AI Confidence: **99.18%**
533. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/report/AmbiguousBindingReporter.java`** -> AI Confidence: **99.18%**
534. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/instantiation/generator/IdentityClassGenerator.java`** -> AI Confidence: **99.18%**
535. **`platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/model/internal/fixture/ModelRegistryHelperExtension.java`** -> AI Confidence: **99.18%**
536. **`platforms/core-configuration/model-groovy/src/main/java/org/gradle/model/dsl/internal/transform/ClosureBackedRuleFactory.java`** -> AI Confidence: **99.18%**
537. **`platforms/core-configuration/model-groovy/src/main/java/org/gradle/model/dsl/internal/transform/RuleVisitor.java`** -> AI Confidence: **99.18%**
538. **`platforms/core-configuration/model-groovy/src/main/java/org/gradle/model/dsl/internal/transform/RulesVisitor.java`** -> AI Confidence: **99.18%**
539. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/MethodDescription.java`** -> AI Confidence: **99.18%**
540. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/MutableClassDetails.java`** -> AI Confidence: **99.18%**
541. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/ProblemRecordingTypeValidationContext.java`** -> AI Confidence: **99.18%**
542. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/annotations/impl/AbstractHasAnnotationMetadata.java`** -> AI Confidence: **99.18%**
543. **`platforms/core-configuration/project-features-api/src/main/java/org/gradle/features/registration/ConfigurationRegistrar.java`** -> AI Confidence: **99.18%**
544. **`platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeatureApplicationContextInternal.java`** -> AI Confidence: **99.18%**
545. **`platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeatureDeclarations.java`** -> AI Confidence: **99.18%**
546. **`platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeatureSupportInternal.java`** -> AI Confidence: **99.18%**
547. **`platforms/core-execution/build-cache-local/src/main/java/org/gradle/caching/local/internal/DirectoryBuildCache.java`** -> AI Confidence: **99.18%**
548. **`platforms/core-execution/build-cache/src/jmh/java/org/gradle/caching/internal/tasks/FileWalkingBenchmark.java`** -> AI Confidence: **99.18%**
549. **`platforms/core-execution/build-cache/src/main/java/org/gradle/caching/internal/controller/service/OpFiringRemoteBuildCacheServiceHandle.java`** -> AI Confidence: **99.18%**
550. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/UnitOfWork.java`** -> AI Confidence: **99.18%**
551. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/WorkValidationContext.java`** -> AI Confidence: **99.18%**
552. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/changes/OutputFileChanges.java`** -> AI Confidence: **99.18%**
553. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/DefaultImmutableWorkspaceMetadataStore.java`** -> AI Confidence: **99.18%**
554. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/DefaultOverlappingOutputDetector.java`** -> AI Confidence: **99.18%**
555. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/DefaultPreviousExecutionStateSerializer.java`** -> AI Confidence: **99.18%**
556. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/OutputSnapshotUtil.java`** -> AI Confidence: **99.18%**
557. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/impl/DefaultInputFingerprinter.java`** -> AI Confidence: **99.18%**
558. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/model/annotations/AbstractInputFilePropertyAnnotationHandler.java`** -> AI Confidence: **99.18%**
559. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/model/annotations/InputPropertyAnnotationHandler.java`** -> AI Confidence: **99.18%**
560. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/CaptureMutableStateBeforeExecutionStep.java`** -> AI Confidence: **99.18%**
561. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/HandleStaleOutputsStep.java`** -> AI Confidence: **99.18%**
562. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/IdentifyStep.java`** -> AI Confidence: **99.18%**
563. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/ResolveInputChangesStep.java`** -> AI Confidence: **99.18%**
564. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/ResolveMutableCachingStateStep.java`** -> AI Confidence: **99.18%**
565. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/SkipUpToDateStep.java`** -> AI Confidence: **99.18%**
566. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/UpToDateResult.java`** -> AI Confidence: **99.18%**
567. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/ValidateStep.java`** -> AI Confidence: **99.18%**
568. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/DarwinFileWatcherRegistryFactory.java`** -> AI Confidence: **99.18%**
569. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/DefaultFileWatcherRegistry.java`** -> AI Confidence: **99.18%**
570. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/HierarchicalFileWatcherUpdater.java`** -> AI Confidence: **99.18%**
571. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/LinuxFileWatcherRegistryFactory.java`** -> AI Confidence: **99.18%**
572. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/WatchableHierarchies.java`** -> AI Confidence: **99.18%**
573. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/vfs/impl/DefaultWatchableFileSystemDetector.java`** -> AI Confidence: **99.18%**
574. **`platforms/core-execution/hashing-services/src/main/java/org/gradle/api/internal/changedetection/state/FileTimeStampInspector.java`** -> AI Confidence: **99.18%**
575. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/AbstractCacheCleanup.java`** -> AI Confidence: **99.18%**
576. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/DefaultCacheCleanupExecutor.java`** -> AI Confidence: **99.18%**
577. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/DefaultCacheFactory.java`** -> AI Confidence: **99.18%**
578. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/DefaultInMemoryCacheDecoratorFactory.java`** -> AI Confidence: **99.18%**
579. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/FileBackedObjectHolder.java`** -> AI Confidence: **99.18%**
580. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/FineGrainedMarkAndSweepLeastRecentlyUsedCacheCleanup.java`** -> AI Confidence: **99.18%**
581. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/FixedExclusiveModeCrossProcessCacheAccess.java`** -> AI Confidence: **99.18%**
582. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/ProducerGuard.java`** -> AI Confidence: **99.18%**
583. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/SingleDepthFilesFinder.java`** -> AI Confidence: **99.18%**
584. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/locklistener/FileLockPacketPayload.java`** -> AI Confidence: **99.18%**
585. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/streams/DefaultValueStore.java`** -> AI Confidence: **99.18%**
586. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/btree/BTreeIndexedCacheTest.java`** -> AI Confidence: **99.18%**
587. **`platforms/core-execution/request-handler-worker/src/main/java/org/gradle/process/internal/worker/request/WorkerAction.java`** -> AI Confidence: **99.18%**
588. **`platforms/core-execution/snapshots/src/main/java/org/gradle/internal/fingerprint/impl/RelativePathFingerprintingStrategy.java`** -> AI Confidence: **99.18%**
589. **`platforms/core-execution/snapshots/src/main/java/org/gradle/internal/snapshot/impl/FileSystemSnapshotFilter.java`** -> AI Confidence: **99.18%**
590. **`platforms/core-execution/snapshots/src/main/java/org/gradle/internal/vfs/impl/AbstractVirtualFileSystem.java`** -> AI Confidence: **99.18%**
591. **`platforms/core-execution/worker-main/src/main/java/org/gradle/process/internal/worker/GradleWorkerMain.java`** -> AI Confidence: **99.18%**
592. **`platforms/core-execution/worker-process-services/src/main/java/org/gradle/process/internal/worker/DefaultMultiRequestWorkerProcessBuilder.java`** -> AI Confidence: **99.18%**
593. **`platforms/core-execution/worker-process-services/src/main/java/org/gradle/process/internal/worker/request/Receiver.java`** -> AI Confidence: **99.18%**
594. **`platforms/core-execution/workers/src/main/java/org/gradle/workers/internal/ClassLoaderStructureProvider.java`** -> AI Confidence: **99.18%**
595. **`platforms/core-execution/workers/src/main/java/org/gradle/workers/internal/DefaultProcessWorkerSpec.java`** -> AI Confidence: **99.18%**
596. **`platforms/core-runtime/base-asm/src/main/java/org/gradle/model/internal/asm/MethodVisitorScope.java`** -> AI Confidence: **99.18%**
597. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/exceptions/FormattingDiagnosticsVisitor.java`** -> AI Confidence: **99.18%**
598. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/resources/AbstractResourceLockRegistry.java`** -> AI Confidence: **99.18%**
599. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/util/PropertiesUtils.java`** -> AI Confidence: **99.18%**
600. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/work/WaitBuildOperationFiringSynchronizer.java`** -> AI Confidence: **99.18%**
601. **`platforms/core-runtime/base-services/src/main/java/org/gradle/util/internal/GFileUtils.java`** -> AI Confidence: **99.18%**
602. **`platforms/core-runtime/build-discovery-impl/src/main/java/org/gradle/initialization/layout/BuildLayoutFactory.java`** -> AI Confidence: **99.18%**
603. **`platforms/core-runtime/build-operations-trace/src/main/java/org/gradle/internal/operations/trace/BuildOperationTrace.java`** -> AI Confidence: **99.18%**
604. **`platforms/core-runtime/build-process-services/src/main/java/org/gradle/launcher/bootstrap/ProcessBootstrap.java`** -> AI Confidence: **99.18%**
605. **`platforms/core-runtime/build-state/src/main/java/org/gradle/internal/buildprocess/execution/BuildSessionLifecycleBuildActionExecutor.java`** -> AI Confidence: **99.18%**
606. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/ConfigurableClassLoaderHierarchyHasher.java`** -> AI Confidence: **99.18%**
607. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/VisitableURLClassLoader.java`** -> AI Confidence: **99.18%**
608. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classpath/DefaultClassPath.java`** -> AI Confidence: **99.18%**
609. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/bootstrap/DaemonOutputConsumer.java`** -> AI Confidence: **99.18%**
610. **`platforms/core-runtime/daemon-messaging/src/main/java/org/gradle/launcher/daemon/diagnostics/DaemonLogFileUtils.java`** -> AI Confidence: **99.18%**
611. **`platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/bootstrap/DaemonStartupCommunication.java`** -> AI Confidence: **99.18%**
612. **`platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/context/DefaultDaemonContext.java`** -> AI Confidence: **99.18%**
613. **`platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/registry/DaemonStopEvent.java`** -> AI Confidence: **99.18%**
614. **`platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/registry/PersistentDaemonRegistry.java`** -> AI Confidence: **99.18%**
615. **`platforms/core-runtime/daemon-services/src/main/java/org/gradle/api/internal/tasks/userinput/DefaultUserInputHandler.java`** -> AI Confidence: **99.18%**
616. **`platforms/core-runtime/daemon-services/src/main/java/org/gradle/internal/daemon/serialization/DaemonSidePayloadClassLoaderFactory.java`** -> AI Confidence: **99.18%**
617. **`platforms/core-runtime/files/src/main/java/org/gradle/api/internal/file/archive/impl/FileZipInput.java`** -> AI Confidence: **99.18%**
618. **`platforms/core-runtime/files/src/main/java/org/gradle/api/internal/file/archive/impl/StreamZipInput.java`** -> AI Confidence: **99.18%**
619. **`platforms/core-runtime/files/src/main/java/org/gradle/internal/file/nio/NioFileMetadataAccessor.java`** -> AI Confidence: **99.18%**
620. **`platforms/core-runtime/gradle-cli/src/main/java/org/gradle/launcher/cli/WelcomeMessageAction.java`** -> AI Confidence: **99.18%**
621. **`platforms/core-runtime/internal-instrumentation-api/src/main/java/org/gradle/internal/instrumentation/api/jvmbytecode/DefaultBridgeMethodBuilder.java`** -> AI Confidence: **99.18%**
622. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/AddGeneratedClassNameFlagFromClassLevelAnnotation.java`** -> AI Confidence: **99.18%**
623. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/ConfigurationCacheInstrumentationProcessor.java`** -> AI Confidence: **99.18%**
624. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/TypeUtils.java`** -> AI Confidence: **99.18%**
625. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/groovy/InterceptGroovyCallsGenerator.java`** -> AI Confidence: **99.18%**
626. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/groovy/SignatureTree.java`** -> AI Confidence: **99.18%**
627. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/modelreader/impl/AnnotationCallInterceptionRequestReaderImpl.java`** -> AI Confidence: **99.18%**
628. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/modelreader/impl/TypeMirrorToType.java`** -> AI Confidence: **99.18%**
629. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DaemonIdleTimeoutExpirationStrategy.java`** -> AI Confidence: **99.18%**
630. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DaemonTcpServerConnector.java`** -> AI Confidence: **99.18%**
631. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/NotMostRecentlyUsedDaemonExpirationStrategy.java`** -> AI Confidence: **99.18%**
632. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/LogAndCheckHealth.java`** -> AI Confidence: **99.18%**
633. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/health/DaemonHealthStats.java`** -> AI Confidence: **99.18%**
634. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/exec/BuildTreeLifecycleBuildActionExecutor.java`** -> AI Confidence: **99.18%**
635. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/LoggingBridgingBuildActionExecuter.java`** -> AI Confidence: **99.18%**
636. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/ShutdownCoordinator.java`** -> AI Confidence: **99.18%**
637. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/connection/BuildLogLevelMixIn.java`** -> AI Confidence: **99.18%**
638. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/deprecation/DeprecationLogger.java`** -> AI Confidence: **99.18%**
639. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/DefaultColorMap.java`** -> AI Confidence: **99.18%**
640. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/StyledTextOutputBackedRenderer.java`** -> AI Confidence: **99.18%**
641. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/ThrottlingOutputEventListener.java`** -> AI Confidence: **99.18%**
642. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/sink/GroupingProgressLogEventGenerator.java`** -> AI Confidence: **99.18%**
643. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/source/JavaUtilLoggingSystem.java`** -> AI Confidence: **99.18%**
644. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/text/StreamBackedStandardOutputListener.java`** -> AI Confidence: **99.18%**
645. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/hub/queue/EndPointQueue.java`** -> AI Confidence: **99.18%**
646. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/filesystem/services/FallbackFileMetadataAccessor.java`** -> AI Confidence: **99.18%**
647. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/filesystem/services/GenericFileSystem.java`** -> AI Confidence: **99.18%**
648. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/jna/UnsupportedEnvironment.java`** -> AI Confidence: **99.18%**
649. **`platforms/core-runtime/process-services-base/src/main/java/org/gradle/process/internal/ClientExecHandleBuilder.java`** -> AI Confidence: **99.18%**
650. **`platforms/core-runtime/process-services-base/src/main/java/org/gradle/process/internal/ProcessArgumentsSpec.java`** -> AI Confidence: **99.18%**
651. **`platforms/core-runtime/process-services-base/src/main/java/org/gradle/process/internal/streams/ExecOutputHandleRunner.java`** -> AI Confidence: **99.18%**
652. **`platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/DefaultJavaForkOptions.java`** -> AI Confidence: **99.18%**
653. **`platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/JavaExecHandleBuilder.java`** -> AI Confidence: **99.18%**
654. **`platforms/core-runtime/serialization/src/main/java/org/gradle/api/internal/initialization/loadercache/ModelClassLoaderFactory.java`** -> AI Confidence: **99.18%**
655. **`platforms/core-runtime/serialization/src/main/java/org/gradle/tooling/internal/provider/serialization/DefaultPayloadClassLoaderRegistry.java`** -> AI Confidence: **99.18%**
656. **`platforms/core-runtime/serialization/src/main/java/org/gradle/tooling/internal/provider/serialization/PayloadSerializer.java`** -> AI Confidence: **99.18%**
657. **`platforms/core-runtime/start-parameter/src/main/java/org/gradle/api/internal/file/BasicFileResolver.java`** -> AI Confidence: **99.18%**
658. **`platforms/core-runtime/start-parameter/src/main/java/org/gradle/internal/DefaultTaskExecutionRequest.java`** -> AI Confidence: **99.18%**
659. **`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/os/OperatingSystem.java`** -> AI Confidence: **99.18%**
660. **`platforms/core-runtime/versioned-cache/src/main/java/org/gradle/internal/versionedcache/VersionSpecificCacheDirectoryScanner.java`** -> AI Confidence: **99.18%**
661. **`platforms/core-runtime/wrapper-shared/src/main/java/org/gradle/wrapper/Install.java`** -> AI Confidence: **99.18%**
662. **`platforms/core-runtime/wrapper-shared/src/main/java/org/gradle/wrapper/WrapperExecutor.java`** -> AI Confidence: **99.18%**
663. **`platforms/core-runtime/wrapper-shared/src/test/groovy/org/gradle/wrapper/PathAssemblerTest.java`** -> AI Confidence: **99.18%**
664. **`platforms/enterprise/enterprise/src/main/java/org/gradle/internal/enterprise/impl/DefaultGradleEnterprisePluginAdapter.java`** -> AI Confidence: **99.18%**
665. **`platforms/extensibility/plugin-development/src/integTest/resources/org/gradle/compile/daemon/ParallelCompilerDaemonIntegrationTest/shared/JavaClass.java`** -> AI Confidence: **99.18%**
666. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/internal/precompiled/GeneratePluginAdaptersTask.java`** -> AI Confidence: **99.18%**
667. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/tasks/ValidatePlugins.java`** -> AI Confidence: **99.18%**
668. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/tasks/internal/ProblemReportAdapterFactory.java`** -> AI Confidence: **99.18%**
669. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/tasks/internal/ValidateAction.java`** -> AI Confidence: **99.18%**
670. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/plugin/management/internal/DefaultPluginHandler.java`** -> AI Confidence: **99.18%**
671. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/plugin/management/internal/DefaultPluginResolutionStrategy.java`** -> AI Confidence: **99.18%**
672. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/plugin/use/internal/DefaultPluginRequestApplicator.java`** -> AI Confidence: **99.18%**
673. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/plugin/use/resolve/internal/CorePluginResolver.java`** -> AI Confidence: **99.18%**
674. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/plugin/use/tracker/internal/PluginVersionTracker.java`** -> AI Confidence: **99.18%**
675. **`platforms/extensibility/test-kit/src/main/java/org/gradle/testkit/runner/internal/DefaultBuildResult.java`** -> AI Confidence: **99.18%**
676. **`platforms/extensibility/test-kit/src/main/java/org/gradle/testkit/runner/internal/DefaultGradleRunner.java`** -> AI Confidence: **99.18%**
677. **`platforms/extensibility/test-kit/src/main/java/org/gradle/testkit/runner/internal/PluginUnderTestMetadataReading.java`** -> AI Confidence: **99.18%**
678. **`platforms/extensibility/unit-test-fixtures/src/main/java/org/gradle/testfixtures/internal/TestInMemoryCacheFactory.java`** -> AI Confidence: **99.18%**
679. **`platforms/extensibility/unit-test-fixtures/src/main/java/org/gradle/testfixtures/internal/TestInMemoryIndexedCache.java`** -> AI Confidence: **99.18%**
680. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/fixtures/MSBuildExecutor.java`** -> AI Confidence: **99.18%**
681. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/internal/AbstractCppBinaryVisualStudioTargetBinary.java`** -> AI Confidence: **99.18%**
682. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/tasks/GenerateFiltersFileTask.java`** -> AI Confidence: **99.18%**
683. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/tasks/GenerateSolutionFileTask.java`** -> AI Confidence: **99.18%**
684. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/tasks/internal/RelativeFileNameTransformer.java`** -> AI Confidence: **99.18%**
685. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/tasks/internal/VisualStudioProjectFile.java`** -> AI Confidence: **99.18%**
686. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/xcode/internal/xcodeproj/XcodeprojSerializer.java`** -> AI Confidence: **99.18%**
687. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/xcode/tasks/GenerateSchemeFileTask.java`** -> AI Confidence: **99.18%**
688. **`platforms/ide/ide-plugins/src/main/java/org/gradle/plugins/ide/idea/internal/IdeaScalaConfigurer.java`** -> AI Confidence: **99.18%**
689. **`platforms/ide/ide-plugins/src/main/java/org/gradle/plugins/ide/internal/tooling/IdeaModuleBuilderSupport.java`** -> AI Confidence: **99.18%**
690. **`platforms/ide/ide-plugins/src/main/java/org/gradle/plugins/ide/internal/tooling/IsolatedProjectsSafeIdeaModelBuilder.java`** -> AI Confidence: **99.18%**
691. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/api/GeneratorTask.java`** -> AI Confidence: **99.18%**
692. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/AbstractLibrary.java`** -> AI Confidence: **99.18%**
693. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/internal/DefaultResourceFilter.java`** -> AI Confidence: **99.18%**
694. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/internal/DefaultResourceFilterMatcher.java`** -> AI Confidence: **99.18%**
695. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/internal/EclipseDependenciesCreator.java`** -> AI Confidence: **99.18%**
696. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/idea/model/SingleEntryModuleLibrary.java`** -> AI Confidence: **99.18%**
697. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/DefaultIdeArtifactRegistry.java`** -> AI Confidence: **99.18%**
698. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/configurer/DefaultUniqueProjectNameProvider.java`** -> AI Confidence: **99.18%**
699. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/configurer/EclipseModelAwareUniqueProjectNameProvider.java`** -> AI Confidence: **99.18%**
700. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/generator/XmlPersistableConfigurationObject.java`** -> AI Confidence: **99.18%**
701. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/tooling/BuildInvocationsBuilder.java`** -> AI Confidence: **99.18%**
702. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/tooling/GradleBuildBuilder.java`** -> AI Confidence: **99.18%**
703. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/tooling/GradleProjectBuilder.java`** -> AI Confidence: **99.18%**
704. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/AbstractClientProvidedBuildActionRunner.java`** -> AI Confidence: **99.18%**
705. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/BuildModelActionRunner.java`** -> AI Confidence: **99.18%**
706. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/ClientForwardingBuildOperationListener.java`** -> AI Confidence: **99.18%**
707. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/ClientForwardingTestOutputOperationListener.java`** -> AI Confidence: **99.18%**
708. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/PluginApplicationTracker.java`** -> AI Confidence: **99.18%**
709. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/ProblemsProgressEventUtils.java`** -> AI Confidence: **99.18%**
710. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/ProjectConfigurationTracker.java`** -> AI Confidence: **99.18%**
711. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/TaskForTestEventTracker.java`** -> AI Confidence: **99.18%**
712. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/TaskOriginTracker.java`** -> AI Confidence: **99.18%**
713. **`platforms/ide/tooling-api/src/crossVersionTestModels/java/org/gradle/integtests/tooling/r112/FetchTasksBuildAction.java`** -> AI Confidence: **99.18%**
714. **`platforms/ide/tooling-api/src/crossVersionTestModels/java/org/gradle/integtests/tooling/r930/FetchCustomModelPerProjectAction.java`** -> AI Confidence: **99.18%**
715. **`platforms/ide/tooling-api/src/crossVersionTestModels/java/org/gradle/plugins/ide/tooling/r33/FetchEclipseProjects.java`** -> AI Confidence: **99.18%**
716. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/adapter/CollectionMapper.java`** -> AI Confidence: **99.18%**
717. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/BlockingResultHandler.java`** -> AI Confidence: **99.18%**
718. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/ConnectionConfigurationUtil.java`** -> AI Confidence: **99.18%**
719. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/ConnectionExceptionTransformer.java`** -> AI Confidence: **99.18%**
720. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/DistributionInstaller.java`** -> AI Confidence: **99.18%**
721. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/CancellableModelBuilderBackedModelProducer.java`** -> AI Confidence: **99.18%**
722. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/HelpAndVersionHandlingConsumerConnection.java`** -> AI Confidence: **99.18%**
723. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/NestedActionAwareBuildControllerAdapter.java`** -> AI Confidence: **99.18%**
724. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/converters/ConsumerTargetTypeProvider.java`** -> AI Confidence: **99.18%**
725. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/ConsumerOperationParameters.java`** -> AI Confidence: **99.18%**
726. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/CrossVersionTestEngine.java`** -> AI Confidence: **99.18%**
727. **`platforms/jvm/antlr/src/main/java/org/gradle/api/plugins/antlr/AntlrTask.java`** -> AI Confidence: **99.18%**
728. **`platforms/jvm/antlr/src/main/java/org/gradle/api/plugins/antlr/internal/AntlrExecuter.java`** -> AI Confidence: **99.18%**
729. **`platforms/jvm/groovy-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/GroovyCompileTransformingClassLoader.java`** -> AI Confidence: **99.18%**
730. **`platforms/jvm/groovydoc-worker/src/main/java/org/gradle/api/internal/tasks/GroovydocAntAction.java`** -> AI Confidence: **99.18%**
731. **`platforms/jvm/jacoco-workers/src/main/java/org/gradle/internal/jacoco/AntJacocoCheck.java`** -> AI Confidence: **99.18%**
732. **`platforms/jvm/jacoco-workers/src/main/java/org/gradle/internal/jacoco/AntJacocoReport.java`** -> AI Confidence: **99.18%**
733. **`platforms/jvm/java-compiler-plugin/src/testFixtures/java/org/gradle/internal/compiler/java/TestCompiler.java`** -> AI Confidence: **99.18%**
734. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/CompilationClassBackupService.java`** -> AI Confidence: **99.18%**
735. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/JdkJavaCompiler.java`** -> AI Confidence: **99.18%**
736. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/JdkTools.java`** -> AI Confidence: **99.18%**
737. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/ResourceCleaningCompilationTask.java`** -> AI Confidence: **99.18%**
738. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/processing/IsolatingProcessingStrategy.java`** -> AI Confidence: **99.18%**
739. **`platforms/jvm/javadoc/src/main/java/org/gradle/external/javadoc/internal/JavadocExecHandleBuilder.java`** -> AI Confidence: **99.18%**
740. **`platforms/jvm/javadoc/src/main/java/org/gradle/external/javadoc/internal/JavadocOptionFile.java`** -> AI Confidence: **99.18%**
741. **`platforms/jvm/javadoc/src/main/java/org/gradle/external/javadoc/internal/JavadocOptionFileWriter.java`** -> AI Confidence: **99.18%**
742. **`platforms/jvm/jvm-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/daemon/CompilerWorkAction.java`** -> AI Confidence: **99.18%**
743. **`platforms/jvm/jvm-services/src/main/java/org/gradle/jvm/toolchain/internal/DefaultJvmVendorSpec.java`** -> AI Confidence: **99.18%**
744. **`platforms/jvm/jvm-services/src/main/java/org/gradle/jvm/toolchain/internal/LinuxInstallationSupplier.java`** -> AI Confidence: **99.18%**
745. **`platforms/jvm/jvm-services/src/main/java/org/gradle/jvm/toolchain/internal/WindowsInstallationSupplier.java`** -> AI Confidence: **99.18%**
746. **`platforms/jvm/language-groovy/src/main/java/org/gradle/api/internal/tasks/compile/NormalizingGroovyCompiler.java`** -> AI Confidence: **99.18%**
747. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/asm/ClassDependenciesVisitor.java`** -> AI Confidence: **99.18%**
748. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/recomp/CurrentCompilationAccess.java`** -> AI Confidence: **99.18%**
749. **`platforms/jvm/normalization-java/src/main/java/org/gradle/api/internal/changedetection/state/FallbackHandlingResourceHasher.java`** -> AI Confidence: **99.18%**
750. **`platforms/jvm/normalization-java/src/main/java/org/gradle/api/internal/changedetection/state/IgnoringResourceHasher.java`** -> AI Confidence: **99.18%**
751. **`platforms/jvm/normalization-java/src/main/java/org/gradle/api/internal/changedetection/state/LineEndingNormalizingFileSystemLocationSnapshotHasher.java`** -> AI Confidence: **99.18%**
752. **`platforms/jvm/normalization-java/src/main/java/org/gradle/api/internal/changedetection/state/MetaInfAwareClasspathResourceHasher.java`** -> AI Confidence: **99.18%**
753. **`platforms/jvm/normalization-java/src/main/java/org/gradle/api/internal/changedetection/state/PropertiesFileAwareClasspathResourceHasher.java`** -> AI Confidence: **99.18%**
754. **`platforms/jvm/platform-jvm/src/main/java/org/gradle/api/plugins/internal/JavaConfigurationVariantMapping.java`** -> AI Confidence: **99.18%**
755. **`platforms/jvm/platform-jvm/src/main/java/org/gradle/api/plugins/jvm/internal/JvmPluginServices.java`** -> AI Confidence: **99.18%**
756. **`platforms/jvm/plugins-application/src/main/java/org/gradle/api/plugins/ApplicationPlugin.java`** -> AI Confidence: **99.18%**
757. **`platforms/jvm/plugins-groovy/src/main/java/org/gradle/api/tasks/GroovyRuntime.java`** -> AI Confidence: **99.18%**
758. **`platforms/jvm/plugins-java-base/src/main/java/org/gradle/api/plugins/internal/DefaultJavaPluginExtension.java`** -> AI Confidence: **99.18%**
759. **`platforms/jvm/plugins-java-base/src/main/java/org/gradle/api/plugins/jvm/internal/DefaultJvmFeature.java`** -> AI Confidence: **99.18%**
760. **`platforms/jvm/plugins-java-base/src/main/java/org/gradle/api/plugins/jvm/internal/DefaultJvmLanguageSourceDirectoryBuilder.java`** -> AI Confidence: **99.18%**
761. **`platforms/jvm/scala-compiler-worker/src/main/java/org/gradle/api/internal/tasks/scala/TimeCheckingClassLoaderCache.java`** -> AI Confidence: **99.18%**
762. **`platforms/jvm/scala-compiler-worker/src/main/java/org/gradle/api/internal/tasks/scala/ZincScalaCompiler.java`** -> AI Confidence: **99.18%**
763. **`platforms/jvm/scala/src/main/java/org/gradle/api/internal/tasks/scala/NormalizingScalaCompiler.java`** -> AI Confidence: **99.18%**
764. **`platforms/jvm/scala/src/main/java/org/gradle/api/plugins/scala/ScalaBasePlugin.java`** -> AI Confidence: **99.18%**
765. **`platforms/jvm/scala/src/main/java/org/gradle/language/scala/tasks/AbstractScalaCompile.java`** -> AI Confidence: **99.18%**
766. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/testng/TestNGTestRunner.java`** -> AI Confidence: **99.18%**
767. **`platforms/jvm/testing-jvm/src/main/java/org/gradle/api/internal/tasks/testing/detection/ClassFileExtractionManager.java`** -> AI Confidence: **99.18%**
768. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/dynamic-rbt-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/DynamicResourceBasedTestEngine.java`** -> AI Confidence: **99.18%**
769. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/matches-nothing-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/MatchesNothingTestEngine.java`** -> AI Confidence: **99.18%**
770. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/multi-file-rbt-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/MultiFileResourceBasedTestEngine.java`** -> AI Confidence: **99.18%**
771. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/rbt-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/ResourceBasedTestEngine.java`** -> AI Confidence: **99.18%**
772. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/resource-and-class-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/ClassAndResourceBasedTestEngine.java`** -> AI Confidence: **99.18%**
773. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/resource-and-class-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/ClassBasedSelectorResolver.java`** -> AI Confidence: **99.18%**
774. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/uses-only-test-dynamic-rbt-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/UsesOnlyTestDynamicResourceBasedTestEngine.java`** -> AI Confidence: **99.18%**
775. **`platforms/jvm/toolchains-jvm-shared/src/main/java/org/gradle/jvm/toolchain/internal/RealizedJavaToolchainRepository.java`** -> AI Confidence: **99.18%**
776. **`platforms/jvm/toolchains-jvm/src/main/java/org/gradle/jvm/toolchain/internal/DefaultJavaToolchainResolverRegistry.java`** -> AI Confidence: **99.18%**
777. **`platforms/jvm/toolchains-jvm/src/main/java/org/gradle/jvm/toolchain/internal/DefaultJavaToolchainResolverService.java`** -> AI Confidence: **99.18%**
778. **`platforms/jvm/toolchains-jvm/src/main/java/org/gradle/jvm/toolchain/internal/task/ShowToolchainsTask.java`** -> AI Confidence: **99.18%**
779. **`platforms/jvm/war/src/main/java/org/gradle/api/tasks/bundling/War.java`** -> AI Confidence: **99.18%**
780. **`platforms/native/language-native/src/main/java/org/gradle/language/cpp/plugins/CppApplicationPlugin.java`** -> AI Confidence: **99.18%**
781. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/AbstractHeaderExportingDependentSourceSet.java`** -> AI Confidence: **99.18%**
782. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/DefaultHeaderDependenciesCollector.java`** -> AI Confidence: **99.18%**
783. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/IncrementalNativeCompiler.java`** -> AI Confidence: **99.18%**
784. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/tasks/UnexportMainSymbol.java`** -> AI Confidence: **99.18%**
785. **`platforms/native/language-native/src/main/java/org/gradle/language/swift/plugins/SwiftApplicationPlugin.java`** -> AI Confidence: **99.18%**
786. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/internal/AbstractNativeLibraryBinarySpec.java`** -> AI Confidence: **99.18%**
787. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/internal/configure/NativeComponentRules.java`** -> AI Confidence: **99.18%**
788. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/internal/prebuilt/PrebuiltLibraryBinaryLocator.java`** -> AI Confidence: **99.18%**
789. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/internal/prebuilt/PrebuiltLibraryInitializer.java`** -> AI Confidence: **99.18%**
790. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/gcc/AbstractGccCompatibleToolChain.java`** -> AI Confidence: **99.18%**
791. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/gcc/GccLinker.java`** -> AI Confidence: **99.18%**
792. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/LegacyWindowsSdkInstall.java`** -> AI Confidence: **99.18%**
793. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/LinkExeLinker.java`** -> AI Confidence: **99.18%**
794. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/VisualCppToolChain.java`** -> AI Confidence: **99.18%**
795. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/version/DefaultVisualCppMetadataProvider.java`** -> AI Confidence: **99.18%**
796. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/version/WindowsRegistryVersionLocator.java`** -> AI Confidence: **99.18%**
797. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/swift/IncrementalSwiftCompiler.java`** -> AI Confidence: **99.18%**
798. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/swift/SwiftLinker.java`** -> AI Confidence: **99.18%**
799. **`platforms/native/platform-native/src/testFixtures/groovy/org/gradle/nativeplatform/fixtures/NativeToolChainTestInterceptor.java`** -> AI Confidence: **99.18%**
800. **`platforms/native/platform-native/src/testFixtures/groovy/org/gradle/nativeplatform/fixtures/app/SourceElement.java`** -> AI Confidence: **99.18%**
801. **`platforms/native/tooling-native/src/crossVersionTestModels/java/org/gradle/language/cpp/tooling/r410/FetchAllCppProjects.java`** -> AI Confidence: **99.18%**
802. **`platforms/software/ant-impl/src/main/java/org/gradle/api/internal/project/DefaultAntBuilder.java`** -> AI Confidence: **99.18%**
803. **`platforms/software/ant-impl/src/main/java/org/gradle/api/internal/project/antbuilder/DefaultIsolatedAntBuilder.java`** -> AI Confidence: **99.18%**
804. **`platforms/software/ant-impl/src/main/java/org/gradle/api/tasks/ant/AntTarget.java`** -> AI Confidence: **99.18%**
805. **`platforms/software/ant/src/main/java/org/gradle/api/internal/project/ant/AntLoggingAdapter.java`** -> AI Confidence: **99.18%**
806. **`platforms/software/ant/src/main/java/org/gradle/api/internal/project/ant/BasicAntBuilder.java`** -> AI Confidence: **99.18%**
807. **`platforms/software/build-init/src/main/java/org/gradle/api/tasks/wrapper/Wrapper.java`** -> AI Confidence: **99.18%**
808. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/BuildScriptBuilder.java`** -> AI Confidence: **99.18%**
809. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/SwiftProjectInitDescriptor.java`** -> AI Confidence: **99.18%**
810. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/TemplateFactory.java`** -> AI Confidence: **99.18%**
811. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/VersionCatalogDependencyRegistry.java`** -> AI Confidence: **99.18%**
812. **`platforms/software/build-init/src/main/java/org/gradle/unexported/buildinit/plugins/internal/maven/PomProjectInitDescriptor.java`** -> AI Confidence: **99.18%**
813. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/DefaultArtifactRepositoryContainer.java`** -> AI Confidence: **99.18%**
814. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/DefaultResolvedDependency.java`** -> AI Confidence: **99.18%**
815. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/GlobalDependencyResolutionRules.java`** -> AI Confidence: **99.18%**
816. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ResolveExceptionMapper.java`** -> AI Confidence: **99.18%**
817. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/DefaultConfiguration.java`** -> AI Confidence: **99.18%**
818. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/TasksFromDependentProjects.java`** -> AI Confidence: **99.18%**
819. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/VariantIdentityUniquenessVerifier.java`** -> AI Confidence: **99.18%**
820. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dependencies/AbstractExternalModuleDependency.java`** -> AI Confidence: **99.18%**
821. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dependencies/DefaultImmutableVersionConstraint.java`** -> AI Confidence: **99.18%**
822. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dependencies/DefaultMinimalDependencyVariant.java`** -> AI Confidence: **99.18%**
823. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/ClassBasedMetadataRuleWrapper.java`** -> AI Confidence: **99.18%**
824. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/DefaultArtifactHandler.java`** -> AI Confidence: **99.18%**
825. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/DefaultRepositoryHandler.java`** -> AI Confidence: **99.18%**
826. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/LazyPublishArtifact.java`** -> AI Confidence: **99.18%**
827. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/MetadataDescriptorFactory.java`** -> AI Confidence: **99.18%**
828. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/DefaultDependencyHandler.java`** -> AI Confidence: **99.18%**
829. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/GradlePluginVariantsSupport.java`** -> AI Confidence: **99.18%**
830. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/DefaultArtifactCaches.java`** -> AI Confidence: **99.18%**
831. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/DefaultIvyExtraInfo.java`** -> AI Confidence: **99.18%**
832. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ReadOnlyArtifactCacheLockingAccessCoordinator.java`** -> AI Confidence: **99.18%**
833. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencySubstitution.java`** -> AI Confidence: **99.18%**
834. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencySubstitutionApplicator.java`** -> AI Confidence: **99.18%**
835. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencySubstitutions.java`** -> AI Confidence: **99.18%**
836. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/CachingModuleComponentRepository.java`** -> AI Confidence: **99.18%**
837. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/ComponentMetaDataResolveState.java`** -> AI Confidence: **99.18%**
838. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/DefaultMetadataProvider.java`** -> AI Confidence: **99.18%**
839. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/ErrorHandlingArtifactResolver.java`** -> AI Confidence: **99.18%**
840. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/ErrorHandlingModuleComponentRepository.java`** -> AI Confidence: **99.18%**
841. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/RepositoryChainArtifactResolver.java`** -> AI Confidence: **99.18%**
842. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/GradlePomModuleDescriptorParser.java`** -> AI Confidence: **99.18%**
843. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/IvyModuleDescriptorConverter.java`** -> AI Confidence: **99.18%**
844. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/report/SimpleTextDependencyVerificationReportRenderer.java`** -> AI Confidence: **99.18%**
845. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/modulecache/ModuleComponentResolveMetadataSerializer.java`** -> AI Confidence: **99.18%**
846. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/modulecache/ModuleMetadataSerializer.java`** -> AI Confidence: **99.18%**
847. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/modulecache/ModuleSourcesSerializer.java`** -> AI Confidence: **99.18%**
848. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/modulecache/artifacts/InMemoryModuleArtifactCache.java`** -> AI Confidence: **99.18%**
849. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/moduleconverter/dependencies/DefaultLocalVariantGraphResolveStateBuilder.java`** -> AI Confidence: **99.18%**
850. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/projectmodule/DefaultProjectPublicationRegistry.java`** -> AI Confidence: **99.18%**
851. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/DefaultComponentSelectionRules.java`** -> AI Confidence: **99.18%**
852. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/ModuleForcingResolveRule.java`** -> AI Confidence: **99.18%**
853. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/ComponentResolversChain.java`** -> AI Confidence: **99.18%**
854. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/artifact/ArtifactBackedResolvedVariant.java`** -> AI Confidence: **99.18%**
855. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/artifact/ResolvedArtifactsGraphVisitor.java`** -> AI Confidence: **99.18%**
856. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/ModuleExclusions.java`** -> AI Confidence: **99.18%**
857. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/simple/DefaultIvyPatternMatcherExcludeRuleSpec.java`** -> AI Confidence: **99.18%**
858. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/DependencyState.java`** -> AI Confidence: **99.18%**
859. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/MessageBuilderHelper.java`** -> AI Confidence: **99.18%**
860. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/VariantNameBuilder.java`** -> AI Confidence: **99.18%**
861. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/DeduplicatingAttributeContainerSerializer.java`** -> AI Confidence: **99.18%**
862. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ResolutionResultGraphBuilder.java`** -> AI Confidence: **99.18%**
863. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ThisBuildTreeOnlyComponentResultSerializer.java`** -> AI Confidence: **99.18%**
864. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/mvnsettings/DefaultMavenSettingsProvider.java`** -> AI Confidence: **99.18%**
865. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/query/DefaultArtifactResolutionQuery.java`** -> AI Confidence: **99.18%**
866. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/AbstractArtifactRepository.java`** -> AI Confidence: **99.18%**
867. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/AbstractAuthenticationSupportedRepository.java`** -> AI Confidence: **99.18%**
868. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/DefaultIvyArtifactRepository.java`** -> AI Confidence: **99.18%**
869. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/DefaultRepositoryContentDescriptor.java`** -> AI Confidence: **99.18%**
870. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/descriptor/UrlRepositoryDescriptor.java`** -> AI Confidence: **99.18%**
871. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/maven/MavenVersionLister.java`** -> AI Confidence: **99.18%**
872. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/metadata/DefaultGradleModuleMetadataSource.java`** -> AI Confidence: **99.18%**
873. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/AbstractDependenciesMetadataAdapter.java`** -> AI Confidence: **99.18%**
874. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/ComponentMetadataDetailsAdapter.java`** -> AI Confidence: **99.18%**
875. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/DirectDependencyMetadataAdapter.java`** -> AI Confidence: **99.18%**
876. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/ExternalResourceResolver.java`** -> AI Confidence: **99.18%**
877. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/result/DefaultResolvedVariantResult.java`** -> AI Confidence: **99.18%**
878. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/AttributeMatchingArtifactVariantSelector.java`** -> AI Confidence: **99.18%**
879. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/DefaultTransform.java`** -> AI Confidence: **99.18%**
880. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/DefaultTransformedVariantFactory.java`** -> AI Confidence: **99.18%**
881. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/TransformStep.java`** -> AI Confidence: **99.18%**
882. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/TransformedProjectArtifactSet.java`** -> AI Confidence: **99.18%**
883. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/TransformingAsyncArtifactListener.java`** -> AI Confidence: **99.18%**
884. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/signatures/CrossBuildCachingKeyService.java`** -> AI Confidence: **99.18%**
885. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/signatures/DefaultSignatureVerificationServiceFactory.java`** -> AI Confidence: **99.18%**
886. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/verifier/DependencyVerifierBuilder.java`** -> AI Confidence: **99.18%**
887. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/AttributeDesugaring.java`** -> AI Confidence: **99.18%**
888. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/DefaultCompatibilityRuleChain.java`** -> AI Confidence: **99.18%**
889. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/DefaultDisambiguationRuleChain.java`** -> AI Confidence: **99.18%**
890. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/FreezableAttributeContainer.java`** -> AI Confidence: **99.18%**
891. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/DependencyClassPathNotationConverter.java`** -> AI Confidence: **99.18%**
892. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/DependencyNotationParser.java`** -> AI Confidence: **99.18%**
893. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/DependencyProjectNotationConverter.java`** -> AI Confidence: **99.18%**
894. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/DependencyStringNotationConverter.java`** -> AI Confidence: **99.18%**
895. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/ModuleIdentifierNotationConverter.java`** -> AI Confidence: **99.18%**
896. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/notations/ProjectDependencyFactory.java`** -> AI Confidence: **99.18%**
897. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/runtimeshaded/ImplementationDependencyRelocator.java`** -> AI Confidence: **99.18%**
898. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/AbstractRealisedModuleComponentResolveMetadata.java`** -> AI Confidence: **99.18%**
899. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ExternalModuleDependencyMetadata.java`** -> AI Confidence: **99.18%**
900. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ImmutableCapabilities.java`** -> AI Confidence: **99.18%**
901. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/JavaEcosystemVariantDerivationStrategy.java`** -> AI Confidence: **99.18%**
902. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/LazyVariantBackedConfigurationMetadata.java`** -> AI Confidence: **99.18%**
903. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ProjectDerivedCapability.java`** -> AI Confidence: **99.18%**
904. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/local/model/DefaultLibraryComponentSelector.java`** -> AI Confidence: **99.18%**
905. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/DependencyMetadata.java`** -> AI Confidence: **99.18%**
906. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/DependencyMetadataRules.java`** -> AI Confidence: **99.18%**
907. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/LoggingAttributeMatchingExplanationBuilder.java`** -> AI Confidence: **99.18%**
908. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/VariantAttributesRules.java`** -> AI Confidence: **99.18%**
909. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/AmbiguousArtifactsFailureDescriber.java`** -> AI Confidence: **99.18%**
910. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/MissingAttributeAmbiguousVariantsFailureDescriber.java`** -> AI Confidence: **99.18%**
911. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/locking/DefaultDependencyLockingProvider.java`** -> AI Confidence: **99.18%**
912. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resolve/ModuleVersionResolveException.java`** -> AI Confidence: **99.18%**
913. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resolve/resolver/DefaultVariantArtifactResolver.java`** -> AI Confidence: **99.18%**
914. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resource/cached/DefaultCachedExternalResourceIndex.java`** -> AI Confidence: **99.18%**
915. **`platforms/software/ivy/src/main/java/org/gradle/api/publish/ivy/internal/publication/DefaultIvyPublication.java`** -> AI Confidence: **99.18%**
916. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/artifact/AbstractMavenArtifact.java`** -> AI Confidence: **99.18%**
917. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/publication/DefaultMavenPom.java`** -> AI Confidence: **99.18%**
918. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/publication/DefaultMavenPublication.java`** -> AI Confidence: **99.18%**
919. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/publication/MavenComponentParser.java`** -> AI Confidence: **99.18%**
920. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/publisher/AbstractMavenPublisher.java`** -> AI Confidence: **99.18%**
921. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/tasks/MavenPomFileGenerator.java`** -> AI Confidence: **99.18%**
922. **`platforms/software/platform-base/src/main/java/org/gradle/language/base/sources/BaseLanguageSourceSet.java`** -> AI Confidence: **99.18%**
923. **`platforms/software/platform-base/src/main/java/org/gradle/model/internal/core/DomainObjectCollectionBackedModelMap.java`** -> AI Confidence: **99.18%**
924. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/binary/BaseBinarySpec.java`** -> AI Confidence: **99.18%**
925. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/DefaultProjectDependencySpec.java`** -> AI Confidence: **99.18%**
926. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/component/ConfigurationSoftwareComponentVariant.java`** -> AI Confidence: **99.18%**
927. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/mapping/DefaultDependencyCoordinateResolverFactory.java`** -> AI Confidence: **99.18%**
928. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/mapping/ResolutionBackedPublicationDependencyResolver.java`** -> AI Confidence: **99.18%**
929. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/mapping/VersionMappingComponentDependencyResolver.java`** -> AI Confidence: **99.18%**
930. **`platforms/software/publish/src/main/java/org/gradle/api/publish/plugins/PublishingPlugin.java`** -> AI Confidence: **99.18%**
931. **`platforms/software/reporting/src/main/java/org/gradle/api/reporting/GenerateBuildDashboard.java`** -> AI Confidence: **99.18%**
932. **`platforms/software/reporting/src/main/java/org/gradle/api/reporting/internal/BuildDashboardGenerator.java`** -> AI Confidence: **99.18%**
933. **`platforms/software/resources-gcs/src/main/java/org/gradle/internal/resource/transport/gcp/gcs/GcsConnectionProperties.java`** -> AI Confidence: **99.18%**
934. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/ApacheCommonsHttpClient.java`** -> AI Confidence: **99.18%**
935. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/HttpResourceAccessor.java`** -> AI Confidence: **99.18%**
936. **`platforms/software/resources-s3/src/main/java/org/gradle/internal/resource/transport/aws/s3/S3ConnectionProperties.java`** -> AI Confidence: **99.18%**
937. **`platforms/software/resources-s3/src/main/java/org/gradle/internal/resource/transport/aws/s3/S3ConnectorFactory.java`** -> AI Confidence: **99.18%**
938. **`platforms/software/resources-sftp/src/main/java/org/gradle/internal/resource/transport/sftp/SftpClientFactory.java`** -> AI Confidence: **99.18%**
939. **`platforms/software/security/src/main/java/org/gradle/security/internal/KeyringStripper.java`** -> AI Confidence: **99.18%**
940. **`platforms/software/security/src/main/java/org/gradle/security/internal/PublicKeyDownloadService.java`** -> AI Confidence: **99.18%**
941. **`platforms/software/security/src/main/java/org/gradle/security/internal/SecuritySupport.java`** -> AI Confidence: **99.18%**
942. **`platforms/software/signing/src/main/java/org/gradle/plugins/signing/Sign.java`** -> AI Confidence: **99.18%**
943. **`platforms/software/signing/src/main/java/org/gradle/plugins/signing/signatory/internal/pgp/PgpSignatoryUtil.java`** -> AI Confidence: **99.18%**
944. **`platforms/software/signing/src/main/java/org/gradle/plugins/signing/signatory/pgp/PgpSignatoryFactory.java`** -> AI Confidence: **99.18%**
945. **`platforms/software/signing/src/main/java/org/gradle/security/internal/gnupg/GnupgSignatory.java`** -> AI Confidence: **99.18%**
946. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/components/internal/AbstractBinaryRenderer.java`** -> AI Confidence: **99.18%**
947. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/components/internal/ComponentReportRenderer.java`** -> AI Confidence: **99.18%**
948. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/dependencies/HtmlDependencyReportTask.java`** -> AI Confidence: **99.18%**
949. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/dependents/internal/DependentComponentsGraphRenderer.java`** -> AI Confidence: **99.18%**
950. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/AbstractDependencyReportTask.java`** -> AI Confidence: **99.18%**
951. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/dsl/DependencyResultSpec.java`** -> AI Confidence: **99.18%**
952. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/graph/nodes/InvertedRenderableModuleResult.java`** -> AI Confidence: **99.18%**
953. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/graph/nodes/RenderableDependencyResult.java`** -> AI Confidence: **99.18%**
954. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/graph/nodes/UnresolvableConfigurationResult.java`** -> AI Confidence: **99.18%**
955. **`platforms/software/test-suites-base/src/main/java/org/gradle/testing/base/plugins/TestingModelBasePlugin.java`** -> AI Confidence: **99.18%**
956. **`platforms/software/testing-base-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/processors/CaptureTestOutputTestResultProcessor.java`** -> AI Confidence: **99.18%**
957. **`platforms/software/testing-base-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/results/AttachParentTestResultProcessor.java`** -> AI Confidence: **99.18%**
958. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/processors/MaxNParallelTestDefinitionProcessor.java`** -> AI Confidence: **99.18%**
959. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/processors/TestMainAction.java`** -> AI Confidence: **99.18%**
960. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/JunitXmlTestReportGenerator.java`** -> AI Confidence: **99.18%**
961. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/PerRootInfo.java`** -> AI Confidence: **99.18%**
962. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/PerRootTabRenderer.java`** -> AI Confidence: **99.18%**
963. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/serializable/SerializableTestResult.java`** -> AI Confidence: **99.18%**
964. **`platforms/software/version-control/src/main/java/org/gradle/vcs/internal/DefaultVcsMappings.java`** -> AI Confidence: **99.18%**
965. **`platforms/software/version-control/src/main/java/org/gradle/vcs/internal/services/DefaultVersionControlRepositoryFactory.java`** -> AI Confidence: **99.18%**
966. **`subprojects/composite-builds/src/main/java/org/gradle/composite/internal/CompositeBuildDependencySubstitutions.java`** -> AI Confidence: **99.18%**
967. **`subprojects/composite-builds/src/main/java/org/gradle/composite/internal/DefaultBuildController.java`** -> AI Confidence: **99.18%**
968. **`subprojects/composite-builds/src/main/java/org/gradle/composite/internal/DefaultIncludedBuildRegistry.java`** -> AI Confidence: **99.18%**
969. **`subprojects/composite-builds/src/main/java/org/gradle/composite/internal/IncludedBuildDependencySubstitutionsBuilder.java`** -> AI Confidence: **99.18%**
970. **`subprojects/composite-builds/src/main/java/org/gradle/composite/internal/plugins/CompositeBuildPluginResolverContributor.java`** -> AI Confidence: **99.18%**
971. **`subprojects/core-api/src/main/java/org/gradle/api/artifacts/Configuration.java`** -> AI Confidence: **99.18%**
972. **`subprojects/core-api/src/main/java/org/gradle/api/artifacts/dsl/DependencyModifier.java`** -> AI Confidence: **99.18%**
973. **`subprojects/core-api/src/main/java/org/gradle/api/artifacts/dsl/RepositoryHandler.java`** -> AI Confidence: **99.18%**
974. **`subprojects/core-api/src/main/java/org/gradle/api/component/SoftwareComponentVariant.java`** -> AI Confidence: **99.18%**
975. **`subprojects/core-api/src/main/java/org/gradle/api/file/CopyProcessingSpec.java`** -> AI Confidence: **99.18%**
976. **`subprojects/core-api/src/main/java/org/gradle/api/internal/provider/views/MapPropertyMapView.java`** -> AI Confidence: **99.18%**
977. **`subprojects/core-api/src/main/java/org/gradle/api/internal/provider/views/SetPropertySetView.java`** -> AI Confidence: **99.18%**
978. **`subprojects/core-api/src/main/java/org/gradle/api/provider/ProviderFactory.java`** -> AI Confidence: **99.18%**
979. **`subprojects/core-api/src/main/java/org/gradle/api/tasks/util/internal/PatternSpecFactory.java`** -> AI Confidence: **99.18%**
980. **`subprojects/core-api/src/main/java/org/gradle/internal/typeconversion/FlatteningNotationParser.java`** -> AI Confidence: **99.18%**
981. **`subprojects/core/src/main/java/org/gradle/api/internal/DefaultDomainObjectCollection.java`** -> AI Confidence: **99.18%**
982. **`subprojects/core/src/main/java/org/gradle/api/internal/DefaultNamedDomainObjectCollection.java`** -> AI Confidence: **99.18%**
983. **`subprojects/core/src/main/java/org/gradle/api/internal/DefaultNamedDomainObjectSet.java`** -> AI Confidence: **99.18%**
984. **`subprojects/core/src/main/java/org/gradle/api/internal/DefaultPolymorphicDomainObjectContainer.java`** -> AI Confidence: **99.18%**
985. **`subprojects/core/src/main/java/org/gradle/api/internal/DelegatingDomainObjectSet.java`** -> AI Confidence: **99.18%**
986. **`subprojects/core/src/main/java/org/gradle/api/internal/DependencyClassPathProvider.java`** -> AI Confidence: **99.18%**
987. **`subprojects/core/src/main/java/org/gradle/api/internal/DynamicModulesClassPathProvider.java`** -> AI Confidence: **99.18%**
988. **`subprojects/core/src/main/java/org/gradle/api/internal/FactoryNamedDomainObjectContainer.java`** -> AI Confidence: **99.18%**
989. **`subprojects/core/src/main/java/org/gradle/api/internal/artifacts/configurations/RoleBasedConfigurationContainerInternal.java`** -> AI Confidence: **99.18%**
990. **`subprojects/core/src/main/java/org/gradle/api/internal/artifacts/dependencies/AbstractModuleDependency.java`** -> AI Confidence: **99.18%**
991. **`subprojects/core/src/main/java/org/gradle/api/internal/artifacts/dependencies/DefaultMutableModuleDependencyCapabilitiesHandler.java`** -> AI Confidence: **99.18%**
992. **`subprojects/core/src/main/java/org/gradle/api/internal/artifacts/publish/DecoratingPublishArtifact.java`** -> AI Confidence: **99.18%**
993. **`subprojects/core/src/main/java/org/gradle/api/internal/attributes/EmptyImmutableAttributes.java`** -> AI Confidence: **99.18%**
994. **`subprojects/core/src/main/java/org/gradle/api/internal/catalog/problems/DefaultCatalogProblemBuilder.java`** -> AI Confidence: **99.18%**
995. **`subprojects/core/src/main/java/org/gradle/api/internal/collections/ListElementSource.java`** -> AI Confidence: **99.18%**
996. **`subprojects/core/src/main/java/org/gradle/api/internal/component/DefaultSoftwareComponentVariant.java`** -> AI Confidence: **99.18%**
997. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/DefaultScriptHandler.java`** -> AI Confidence: **99.18%**
998. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/transform/utils/CachedInstrumentationAnalysisSerializer.java`** -> AI Confidence: **99.18%**
999. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/transform/utils/DefaultInstrumentationAnalysisSerializer.java`** -> AI Confidence: **99.18%**
1000. **`subprojects/core/src/main/java/org/gradle/api/internal/options/InternalOptionsFactory.java`** -> AI Confidence: **99.18%**
1001. **`subprojects/core/src/main/java/org/gradle/api/internal/plugins/DefaultObjectConfigurationAction.java`** -> AI Confidence: **99.18%**
1002. **`subprojects/core/src/main/java/org/gradle/api/internal/plugins/ImperativeOnlyPluginTarget.java`** -> AI Confidence: **99.18%**
1003. **`subprojects/core/src/main/java/org/gradle/api/internal/project/taskfactory/AnnotationProcessingTaskFactory.java`** -> AI Confidence: **99.18%**
1004. **`subprojects/core/src/main/java/org/gradle/api/internal/project/taskfactory/DefaultTaskClassInfoStore.java`** -> AI Confidence: **99.18%**
1005. **`subprojects/core/src/main/java/org/gradle/api/internal/project/taskfactory/TaskFactory.java`** -> AI Confidence: **99.18%**
1006. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/BaseFilePropertyVisitState.java`** -> AI Confidence: **99.18%**
1007. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/DefaultRealizableTaskCollection.java`** -> AI Confidence: **99.18%**
1008. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/TaskOptionsGenerator.java`** -> AI Confidence: **99.18%**
1009. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/EventFiringTaskExecuter.java`** -> AI Confidence: **99.18%**
1010. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/ExecuteActionsTaskExecuter.java`** -> AI Confidence: **99.18%**
1011. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/options/FieldOptionElement.java`** -> AI Confidence: **99.18%**
1012. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/options/InstanceOptionDescriptor.java`** -> AI Confidence: **99.18%**
1013. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/options/MethodOptionElement.java`** -> AI Confidence: **99.18%**
1014. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/options/MultipleValueOptionElement.java`** -> AI Confidence: **99.18%**
1015. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/AbstractValidatingProperty.java`** -> AI Confidence: **99.18%**
1016. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/DefaultPropertyTypeResolver.java`** -> AI Confidence: **99.18%**
1017. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/FileParameterUtils.java`** -> AI Confidence: **99.18%**
1018. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/ScriptSourceAwareImplementationResolver.java`** -> AI Confidence: **99.18%**
1019. **`subprojects/core/src/main/java/org/gradle/api/tasks/AbstractCopyTask.java`** -> AI Confidence: **99.18%**
1020. **`subprojects/core/src/main/java/org/gradle/api/tasks/WriteProperties.java`** -> AI Confidence: **99.18%**
1021. **`subprojects/core/src/main/java/org/gradle/api/tasks/bundling/Tar.java`** -> AI Confidence: **99.18%**
1022. **`subprojects/core/src/main/java/org/gradle/api/tasks/bundling/Zip.java`** -> AI Confidence: **99.18%**
1023. **`subprojects/core/src/main/java/org/gradle/cache/internal/BuildScopeCacheDir.java`** -> AI Confidence: **99.18%**
1024. **`subprojects/core/src/main/java/org/gradle/cache/internal/DefaultCrossBuildInMemoryCacheFactory.java`** -> AI Confidence: **99.18%**
1025. **`subprojects/core/src/main/java/org/gradle/caching/configuration/internal/DefaultBuildCacheConfiguration.java`** -> AI Confidence: **99.18%**
1026. **`subprojects/core/src/main/java/org/gradle/caching/internal/services/AbstractBuildCacheControllerFactory.java`** -> AI Confidence: **99.18%**
1027. **`subprojects/core/src/main/java/org/gradle/caching/local/internal/DirectoryBuildCacheEntryRetention.java`** -> AI Confidence: **99.18%**
1028. **`subprojects/core/src/main/java/org/gradle/caching/local/internal/DirectoryBuildCacheServiceFactory.java`** -> AI Confidence: **99.18%**
1029. **`subprojects/core/src/main/java/org/gradle/configuration/DefaultScriptPluginFactory.java`** -> AI Confidence: **99.18%**
1030. **`subprojects/core/src/main/java/org/gradle/configuration/ScriptPluginFactorySelector.java`** -> AI Confidence: **99.18%**
1031. **`subprojects/core/src/main/java/org/gradle/configuration/internal/DefaultListenerBuildOperationDecorator.java`** -> AI Confidence: **99.18%**
1032. **`subprojects/core/src/main/java/org/gradle/configuration/project/LifecycleProjectEvaluator.java`** -> AI Confidence: **99.18%**
1033. **`subprojects/core/src/main/java/org/gradle/execution/DefaultTaskSelector.java`** -> AI Confidence: **99.18%**
1034. **`subprojects/core/src/main/java/org/gradle/execution/DefaultTasksBuildTaskScheduler.java`** -> AI Confidence: **99.18%**
1035. **`subprojects/core/src/main/java/org/gradle/execution/DefaultWorkValidationWarningRecorder.java`** -> AI Confidence: **99.18%**
1036. **`subprojects/core/src/main/java/org/gradle/execution/TaskNameResolvingBuildTaskScheduler.java`** -> AI Confidence: **99.18%**
1037. **`subprojects/core/src/main/java/org/gradle/execution/plan/DefaultNodeValidator.java`** -> AI Confidence: **99.18%**
1038. **`subprojects/core/src/main/java/org/gradle/execution/plan/Node.java`** -> AI Confidence: **99.18%**
1039. **`subprojects/core/src/main/java/org/gradle/execution/plan/ToPlannedTaskConverter.java`** -> AI Confidence: **99.18%**
1040. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/TextResourceScriptSource.java`** -> AI Confidence: **99.18%**
1041. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/BuildScopeInMemoryCachingScriptClassCompiler.java`** -> AI Confidence: **99.18%**
1042. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/CrossBuildInMemoryCachingScriptClassCache.java`** -> AI Confidence: **99.18%**
1043. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/CustomCompilationUnit.java`** -> AI Confidence: **99.18%**
1044. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/RegistryAwareClassLoaderHierarchyHasher.java`** -> AI Confidence: **99.18%**
1045. **`subprojects/core/src/main/java/org/gradle/initialization/DefaultSettings.java`** -> AI Confidence: **99.18%**
1046. **`subprojects/core/src/main/java/org/gradle/initialization/DefaultSettingsPreparer.java`** -> AI Confidence: **99.18%**
1047. **`subprojects/core/src/main/java/org/gradle/initialization/ProjectPropertySettingBuildLoader.java`** -> AI Confidence: **99.18%**
1048. **`subprojects/core/src/main/java/org/gradle/initialization/properties/FilteringGradleProperties.java`** -> AI Confidence: **99.18%**
1049. **`subprojects/core/src/main/java/org/gradle/internal/action/DefaultConfigurableRule.java`** -> AI Confidence: **99.18%**
1050. **`subprojects/core/src/main/java/org/gradle/internal/buildevents/BuildLogger.java`** -> AI Confidence: **99.18%**
1051. **`subprojects/core/src/main/java/org/gradle/internal/buildevents/BuildResultLogger.java`** -> AI Confidence: **99.18%**
1052. **`subprojects/core/src/main/java/org/gradle/internal/buildtree/DefaultBuildTreeLifecycleController.java`** -> AI Confidence: **99.18%**
1053. **`subprojects/core/src/main/java/org/gradle/internal/buildtree/DefaultBuildTreeModelCreator.java`** -> AI Confidence: **99.18%**
1054. **`subprojects/core/src/main/java/org/gradle/internal/buildtree/ProblemReportingBuildActionRunner.java`** -> AI Confidence: **99.18%**
1055. **`subprojects/core/src/main/java/org/gradle/internal/classpath/GroovyCallInterceptorsProvider.java`** -> AI Confidence: **99.18%**
1056. **`subprojects/core/src/main/java/org/gradle/internal/classpath/InPlaceClasspathBuilder.java`** -> AI Confidence: **99.18%**
1057. **`subprojects/core/src/main/java/org/gradle/internal/classpath/Instrumented.java`** -> AI Confidence: **99.18%**
1058. **`subprojects/core/src/main/java/org/gradle/internal/classpath/declarations/GroovyDynamicDispatchInterceptors.java`** -> AI Confidence: **99.18%**
1059. **`subprojects/core/src/main/java/org/gradle/internal/classpath/declarations/KotlinStdlibFileInterceptors.java`** -> AI Confidence: **99.18%**
1060. **`subprojects/core/src/main/java/org/gradle/internal/classpath/intercept/JvmBytecodeInterceptorFactoryProvider.java`** -> AI Confidence: **99.18%**
1061. **`subprojects/core/src/main/java/org/gradle/internal/classpath/transforms/BaseClasspathElementTransform.java`** -> AI Confidence: **99.18%**
1062. **`subprojects/core/src/main/java/org/gradle/internal/classpath/transforms/InstrumentingBackwardsCompatibilityVisitor.java`** -> AI Confidence: **99.18%**
1063. **`subprojects/core/src/main/java/org/gradle/internal/classpath/types/GradleCoreInstrumentationTypeRegistry.java`** -> AI Confidence: **99.18%**
1064. **`subprojects/core/src/main/java/org/gradle/internal/enterprise/core/GradleEnterprisePluginManager.java`** -> AI Confidence: **99.18%**
1065. **`subprojects/core/src/main/java/org/gradle/internal/execution/DefaultWorkExecutionTracker.java`** -> AI Confidence: **99.18%**
1066. **`subprojects/core/src/main/java/org/gradle/internal/execution/TaskGraphBuildExecutionAction.java`** -> AI Confidence: **99.18%**
1067. **`subprojects/core/src/main/java/org/gradle/internal/fingerprint/impl/FileCollectionFingerprinterRegistrations.java`** -> AI Confidence: **99.18%**
1068. **`subprojects/core/src/main/java/org/gradle/internal/model/StateTransitionController.java`** -> AI Confidence: **99.18%**
1069. **`subprojects/core/src/main/java/org/gradle/internal/operations/logging/DefaultBuildOperationLogger.java`** -> AI Confidence: **99.18%**
1070. **`subprojects/core/src/main/java/org/gradle/invocation/DefaultGradle.java`** -> AI Confidence: **99.18%**
1071. **`subprojects/core/src/main/java/org/gradle/plugin/management/internal/DefaultPluginRequest.java`** -> AI Confidence: **99.18%**
1072. **`subprojects/core/src/main/java/org/gradle/plugin/management/internal/argumentloaded/ArgumentSourcedPluginRequest.java`** -> AI Confidence: **99.18%**
1073. **`subprojects/core/src/main/java/org/gradle/tooling/provider/model/internal/DefaultIntermediateToolingModelProvider.java`** -> AI Confidence: **99.18%**
1074. **`subprojects/core/src/testFixtures/groovy/org/gradle/internal/operations/BuildOperationExecutorSupport.java`** -> AI Confidence: **99.18%**
1075. **`testing/architecture-test/src/test/java/org/gradle/architecture/test/ForbiddenNullabilityAnnotationsTest.java`** -> AI Confidence: **99.18%**
1076. **`testing/architecture-test/src/test/java/org/gradle/architecture/test/PackageInfoTest.java`** -> AI Confidence: **99.18%**
1077. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/AvailableJavaHomes.java`** -> AI Confidence: **99.18%**
1078. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/compatibility/AbstractCompatibilityTestInterceptor.java`** -> AI Confidence: **99.18%**
1079. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/versions/ReleasedVersionDistributions.java`** -> AI Confidence: **99.18%**
1080. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/BlockingHttpServer.java`** -> AI Confidence: **99.18%**
1081. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/TestResources.java`** -> AI Confidence: **99.18%**
1082. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/ParallelForkingGradleExecuter.java`** -> AI Confidence: **99.18%**
1083. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/mirror/SetMirrorsSampleModifier.java`** -> AI Confidence: **99.18%**
1084. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/polyglot/PolyglotDslTestInterceptor.java`** -> AI Confidence: **99.18%**
1085. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/fixture/AbstractBuildExperimentRunner.java`** -> AI Confidence: **99.18%**
1086. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/fixture/CompositeDataReporter.java`** -> AI Confidence: **99.18%**
1087. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/fixture/GradleBuildExperimentRunner.java`** -> AI Confidence: **99.18%**
1088. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/measure/Amount.java`** -> AI Confidence: **99.18%**
1089. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/AbstractReportGenerator.java`** -> AI Confidence: **99.18%**
1090. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/FlakinessIndexPageGenerator.java`** -> AI Confidence: **99.18%**
1091. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/PerformanceExecutionDataProvider.java`** -> AI Confidence: **99.18%**
1092. **`testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/file/AbstractTestDirectoryProvider.java`** -> AI Confidence: **99.18%**
1093. **`testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/file/TestFile.java`** -> AI Confidence: **99.18%**
1094. **`testing/internal-testing/src/main/groovy/org/gradle/util/internal/FailsWithMessageExtension.java`** -> AI Confidence: **99.18%**
1095. **`.teamcity/src/main/kotlin/configurations/FunctionalTest.kt`** -> AI Confidence: **99.18%**
1096. **`.teamcity/src/main/kotlin/promotion/PromotionProject.kt`** -> AI Confidence: **99.18%**
1097. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/BuildParams.kt`** -> AI Confidence: **99.18%**
1098. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/classanalysis/AnalyzeAndShade.kt`** -> AI Confidence: **99.18%**
1099. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/tasks/PackageListGenerator.kt`** -> AI Confidence: **99.18%**
1100. **`build-logic-settings/build-environment/src/main/kotlin/gradlebuild/basics/BuildEnvironmentService.kt`** -> AI Confidence: **99.18%**
1101. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/metadata/HasKotlinFlagsMetadataQuery.kt`** -> AI Confidence: **99.18%**
1102. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/sources/JavaSourceQueries.kt`** -> AI Confidence: **99.18%**
1103. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/sources/SourcesRepository.kt`** -> AI Confidence: **99.18%**
1104. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/AbstractVersionsUpdateTask.kt`** -> AI Confidence: **99.18%**
1105. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/SubprojectsInfo.kt`** -> AI Confidence: **99.18%**
1106. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/UpdateInitPluginTemplateVersionFile.kt`** -> AI Confidence: **99.18%**
1107. **`build-logic/buildquality/src/main/kotlin/gradlebuild/codenarc/rules/IntegrationTestFixturesRule.kt`** -> AI Confidence: **99.18%**
1108. **`build-logic/cleanup/src/main/kotlin/gradlebuild/testing/services/BuildBucketProvider.kt`** -> AI Confidence: **99.18%**
1109. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/action/AnnotationGeneratorWorkAction.kt`** -> AI Confidence: **99.18%**
1110. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/ide/AndroidStudioProvisioningPlugin.kt`** -> AI Confidence: **99.18%**
1111. **`build-logic/jvm/src/main/kotlin/gradlebuild/jvm/argumentproviders/CiEnvironmentProvider.kt`** -> AI Confidence: **99.18%**
1112. **`build-logic/packaging/src/main/kotlin/gradlebuild.distributions.gradle.kts`** -> AI Confidence: **99.18%**
1113. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/ExtractJavaAbi.kt`** -> AI Confidence: **99.18%**
1114. **`build-logic/profiling/src/main/kotlin/gradlebuild.buildscan.gradle.kts`** -> AI Confidence: **99.18%**
1115. **`platforms/core-configuration/bean-serialization-services/src/main/kotlin/org/gradle/internal/serialize/beans/services/BeanConstructors.kt`** -> AI Confidence: **99.18%**
1116. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheAwareBuildTreeWorkController.kt`** -> AI Confidence: **99.18%**
1117. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheKey.kt`** -> AI Confidence: **99.18%**
1118. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheState.kt`** -> AI Confidence: **99.18%**
1119. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CrossProjectConfigurationReportingTaskExecutionGraph.kt`** -> AI Confidence: **99.18%**
1120. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultBuildToolingModelControllerFactory.kt`** -> AI Confidence: **99.18%**
1121. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCache.kt`** -> AI Confidence: **99.18%**
1122. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DeprecatedFeaturesListener.kt`** -> AI Confidence: **99.18%**
1123. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ProblemReportingCrossProjectModelAccess.kt`** -> AI Confidence: **99.18%**
1124. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/AbstractInjectedClasspathInstrumentationStrategy.kt`** -> AI Confidence: **99.18%**
1125. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/problems/ConfigurationCacheProblems.kt`** -> AI Confidence: **99.18%**
1126. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ClassPathEncodingExtensions.kt`** -> AI Confidence: **99.18%**
1127. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/DefaultSharedObjectCodec.kt`** -> AI Confidence: **99.18%**
1128. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/serialize/ParallelStringEncoder.kt`** -> AI Confidence: **99.18%**
1129. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/services/RemoteScriptUpToDateChecker.kt`** -> AI Confidence: **99.18%**
1130. **`platforms/core-configuration/configuration-cache/src/test/kotlin/org/gradle/internal/cc/impl/problems/ConfigurationCacheProblemsSummaryTest.kt`** -> AI Confidence: **99.18%**
1131. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/CalculatedValueContainerCodec.kt`** -> AI Confidence: **99.18%**
1132. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/FileCollectionCodec.kt`** -> AI Confidence: **99.18%**
1133. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/GradlePropertiesCodec.kt`** -> AI Confidence: **99.18%**
1134. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/PathToFileResolverCodec.kt`** -> AI Confidence: **99.18%**
1135. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/ProviderCodecs.kt`** -> AI Confidence: **99.18%**
1136. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/TaskNodeCodec.kt`** -> AI Confidence: **99.18%**
1137. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/TaskReferenceCodec.kt`** -> AI Confidence: **99.18%**
1138. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/jos/JavaSerializationEncodingLookup.kt`** -> AI Confidence: **99.18%**
1139. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/analysis/ResolutionTracer.kt`** -> AI Confidence: **99.18%**
1140. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/MutationApplicabilityChecker.kt`** -> AI Confidence: **99.18%**
1141. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/resolution/DefaultDocumentResolutionContainer.kt`** -> AI Confidence: **99.18%**
1142. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/objectGraph/PropertyLinkTrace.kt`** -> AI Confidence: **99.18%**
1143. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/objectGraph/reflectObject.kt`** -> AI Confidence: **99.18%**
1144. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/DataSchemaBuilder.kt`** -> AI Confidence: **99.18%**
1145. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/analysis/AugmentationResolutionTest.kt`** -> AI Confidence: **99.18%**
1146. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/dom/mutation/ModelToDocumentMutationPlannerTest.kt`** -> AI Confidence: **99.18%**
1147. **`platforms/core-configuration/declarative-dsl-core/src/test/kotlin/org/gradle/internal/declarativedsl/parsing/RandomInputParsingTest.kt`** -> AI Confidence: **99.18%**
1148. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/runner/AnalysisStepRunner.kt`** -> AI Confidence: **99.18%**
1149. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/common/GradlePropertyApiAnalysisSchemaComponent.kt`** -> AI Confidence: **99.18%**
1150. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/features/schemaFromProjectFeatures.kt`** -> AI Confidence: **99.18%**
1151. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/interpreter/defaults/ActionBasedModelDefaultsHandler.kt`** -> AI Confidence: **99.18%**
1152. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/ndoc/ContainersSchemaComponent.kt`** -> AI Confidence: **99.18%**
1153. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/project/ExtensionProperties.kt`** -> AI Confidence: **99.18%**
1154. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/provider/SchemaBuildingFailureProblems.kt`** -> AI Confidence: **99.18%**
1155. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/ImmutableAttributesSchemaCodec.kt`** -> AI Confidence: **99.18%**
1156. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/LocalFileDependencyBackedArtifactSetCodec.kt`** -> AI Confidence: **99.18%**
1157. **`platforms/core-configuration/dependency-management-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/dm/transform/Transforms.kt`** -> AI Confidence: **99.18%**
1158. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Codec.kt`** -> AI Confidence: **99.18%**
1159. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Combinators.kt`** -> AI Confidence: **99.18%**
1160. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/Logging.kt`** -> AI Confidence: **99.18%**
1161. **`platforms/core-configuration/graph-serialization/src/main/kotlin/org/gradle/internal/serialize/graph/codecs/BindingsBackedCodec.kt`** -> AI Confidence: **99.18%**
1162. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/integration/PrecompiledScriptPluginSyntheticIntegrationTest.kt`** -> AI Confidence: **99.18%**
1163. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/integTest/kotlin/org/gradle/kotlin/dsl/plugins/precompiled/PrecompiledScriptPluginAccessorsTest.kt`** -> AI Confidence: **99.18%**
1164. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/DefaultProjectSchemaProvider.kt`** -> AI Confidence: **99.18%**
1165. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/precompiled/tasks/GeneratePrecompiledScriptPluginAccessors.kt`** -> AI Confidence: **99.18%**
1166. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/KotlinBuildScriptModelBuilder.kt`** -> AI Confidence: **99.18%**
1167. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/KotlinDslScriptsModelBuilder.kt`** -> AI Confidence: **99.18%**
1168. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/main/kotlin/org/gradle/kotlin/dsl/tooling/builders/internal/KotlinScriptingModelBuildersRegistrant.kt`** -> AI Confidence: **99.18%**
1169. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/Emitter.kt`** -> AI Confidence: **99.18%**
1170. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/DefaultKotlinMetadataCompatibilityChecker.kt`** -> AI Confidence: **99.18%**
1171. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/Interpreter.kt`** -> AI Confidence: **99.18%**
1172. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/normalization/KotlinApiMemberWriter.kt`** -> AI Confidence: **99.18%**
1173. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/provider/KotlinScriptPluginFactory.kt`** -> AI Confidence: **99.18%**
1174. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/provider/ScriptApiTest.kt`** -> AI Confidence: **99.18%**
1175. **`platforms/core-configuration/kotlin-dsl/src/test/kotlin/org/gradle/kotlin/dsl/resolver/SourcePathProviderTest.kt`** -> AI Confidence: **99.18%**
1176. **`platforms/core-configuration/kotlin-dsl/src/testFixtures/kotlin/org/gradle/kotlin/dsl/fixtures/AbstractKotlinIntegrationTest.kt`** -> AI Confidence: **99.18%**
1177. **`platforms/core-configuration/stdlib-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/stdlib/StreamCodecs.kt`** -> AI Confidence: **99.18%**
1178. **`platforms/ide/problems/src/main/kotlin/org/gradle/problems/internal/impl/DefaultProblemsReportCreator.kt`** -> AI Confidence: **99.18%**
1179. **`testing/soak/src/integTest/kotlin/org/gradle/kotlin/dsl/caching/fixtures/CompilationCache.kt`** -> AI Confidence: **99.18%**
1180. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/rules/AbstractGradleViolationRule.groovy`** -> AI Confidence: **99.18%**
1181. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/rules/MethodsRemovedInInternalSuperClassRule.groovy`** -> AI Confidence: **99.18%**
1182. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/transforms/ExplodeZipAndFindJars.groovy`** -> AI Confidence: **99.18%**
1183. **`build-logic/performance-testing/src/main/groovy/gradlebuild/performance/generator/tasks/NativeProjectWithDepsGeneratorTask.groovy`** -> AI Confidence: **99.18%**
1184. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheEncryptionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1185. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/ConfigurationCacheProblemReportingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1186. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsFixture.groovy`** -> AI Confidence: **99.18%**
1187. **`platforms/core-configuration/configuration-cache/src/integTest/groovy/org/gradle/internal/cc/impl/isolated/IsolatedProjectsToolingApiIdeaProjectIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1188. **`platforms/core-configuration/declarative-dsl-provider/src/integTest/groovy/org/gradle/internal/declarativedsl/settings/DeclarativeDslProjectSettingsIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1189. **`platforms/core-configuration/input-tracking/src/test/groovy/org/gradle/internal/configuration/inputs/AccessTrackingPropertiesNonStringTest.groovy`** -> AI Confidence: **99.18%**
1190. **`platforms/core-configuration/java-api-extractor/src/test/groovy/org/gradle/internal/tools/api/ApiClassExtractorTestSupport.groovy`** -> AI Confidence: **99.18%**
1191. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/plugins/PrecompiledKotlinPluginCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1192. **`platforms/core-configuration/kotlin-dsl-integ-tests/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/plugins/ProjectTheExtensionCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1193. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/tooling/builders/AbstractKotlinScriptModelCrossVersionTest.groovy`** -> AI Confidence: **99.18%**
1194. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/tooling/builders/r60/KotlinDslScriptsModelCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1195. **`platforms/core-configuration/kotlin-dsl-tooling-builders/src/crossVersionTest/groovy/org/gradle/kotlin/dsl/tooling/builders/r93/GradleDslBaseScriptModelCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1196. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/api/internal/provider/sources/process/ProcessOutputValueSourceTest.groovy`** -> AI Confidence: **99.18%**
1197. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/registry/DefaultModelRegistryTest.groovy`** -> AI Confidence: **99.18%**
1198. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/registry/RegistrySpec.groovy`** -> AI Confidence: **99.18%**
1199. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/model/internal/typeregistration/BaseInstanceFactoryTest.groovy`** -> AI Confidence: **99.18%**
1200. **`platforms/core-configuration/model-reflect/src/test/groovy/org/gradle/internal/reflect/JavaPropertyReflectionUtilTest.groovy`** -> AI Confidence: **99.18%**
1201. **`platforms/core-configuration/model-reflect/src/test/groovy/org/gradle/internal/reflect/validation/ValidationMessageCheckerTest.groovy`** -> AI Confidence: **99.18%**
1202. **`platforms/core-configuration/project-features/src/integTest/groovy/org/gradle/features/ProjectFeatureSafetyIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1203. **`platforms/core-execution/build-cache-http/src/integTest/groovy/org/gradle/caching/http/internal/HttpBuildCacheServiceIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1204. **`platforms/core-execution/build-cache-local/src/integTest/groovy/org/gradle/caching/local/internal/AbstractBuildCacheCleanupIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1205. **`platforms/core-execution/execution-e2e-tests/src/integTest/groovy/org/gradle/integtests/NestedInputKotlinImplementationTrackingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1206. **`platforms/core-execution/execution/src/integTest/groovy/org/gradle/internal/execution/MutableUnitOfWorkBuilder.groovy`** -> AI Confidence: **99.18%**
1207. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/AbstractFileLockManagerTest.groovy`** -> AI Confidence: **99.18%**
1208. **`platforms/core-execution/persistent-cache/src/test/groovy/org/gradle/cache/internal/DefaultPersistentDirectoryCacheTest.groovy`** -> AI Confidence: **99.18%**
1209. **`platforms/core-execution/snapshots/src/testFixtures/groovy/org/gradle/internal/snapshot/TestSnapshotFixture.groovy`** -> AI Confidence: **99.18%**
1210. **`platforms/core-execution/worker-process-services/src/integTest/groovy/org/gradle/process/internal/PathLimitationIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1211. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerDaemonProcessFailureIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1212. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorErrorHandlingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1213. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1214. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParametersKotlinIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1215. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/ActionsTest.groovy`** -> AI Confidence: **99.18%**
1216. **`platforms/core-runtime/base-services/src/test/groovy/org/gradle/internal/jvm/JvmTest.groovy`** -> AI Confidence: **99.18%**
1217. **`platforms/core-runtime/build-process-services/src/test/groovy/org/gradle/api/internal/classpath/ManifestUtilTest.groovy`** -> AI Confidence: **99.18%**
1218. **`platforms/core-runtime/build-process-services/src/test/groovy/org/gradle/internal/installation/CurrentGradleInstallationLocatorTest.groovy`** -> AI Confidence: **99.18%**
1219. **`platforms/core-runtime/daemon-services/src/test/groovy/org/gradle/api/internal/tasks/userinput/DefaultUserInputHandlerTest.groovy`** -> AI Confidence: **99.18%**
1220. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/CommandLineIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1221. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/SupportedBuildJvmVersionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1222. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/continuous/ContinuousBuildGateIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1223. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonInitialCommunicationFailureIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1224. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonLifecycleSpec.groovy`** -> AI Confidence: **99.18%**
1225. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/ProcessCrashHandlingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1226. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/server/scaninfo/DaemonScanInfoIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1227. **`platforms/core-runtime/logging/src/integTest/groovy/org/gradle/internal/logging/console/taskgrouping/AbstractBasicGroupedTaskLoggingFunctionalTest.groovy`** -> AI Confidence: **99.18%**
1228. **`platforms/core-runtime/stdlib-java-extensions/src/test/groovy/org/gradle/internal/os/OperatingSystemTest.groovy`** -> AI Confidence: **99.18%**
1229. **`platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperChecksumVerificationTest.groovy`** -> AI Confidence: **99.18%**
1230. **`platforms/documentation/samples/src/integTest/groovy/org/gradle/integtests/samples/java/SamplesJavaTestingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1231. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/BaseBuildScanPluginCheckInFixture.groovy`** -> AI Confidence: **99.18%**
1232. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/DevelocityPluginConfigIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1233. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/DevelocityPluginConfigurationCachingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1234. **`platforms/enterprise/enterprise/src/test/groovy/org/gradle/internal/enterprise/DevelocityBuildLifecycleServiceTest.groovy`** -> AI Confidence: **99.18%**
1235. **`platforms/extensibility/plugin-development/src/integTest/groovy/org/gradle/plugin/devel/plugins/PrecompiledGroovyPluginsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1236. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerConventionalPluginClasspathInjectionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1237. **`platforms/extensibility/test-kit/src/integTest/groovy/org/gradle/testkit/runner/GradleRunnerUnsupportedFeatureFailureIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1238. **`platforms/extensibility/test-kit/src/test/groovy/org/gradle/testkit/runner/internal/DefaultGradleRunnerTest.groovy`** -> AI Confidence: **99.18%**
1239. **`platforms/extensibility/test-kit/src/testFixtures/groovy/org/gradle/testkit/runner/BaseGradleRunnerIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1240. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/AbstractVisualStudioProjectIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1241. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioSoftwareModelMultiProjectIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1242. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/visualstudio/VisualStudioSoftwareModelSingleProjectIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1243. **`platforms/ide/ide-native/src/integTest/groovy/org/gradle/ide/xcode/fixtures/AbstractXcodeIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1244. **`platforms/ide/ide-native/src/testFixtures/groovy/org/gradle/ide/xcode/fixtures/ProjectFile.groovy`** -> AI Confidence: **99.18%**
1245. **`platforms/ide/ide-plugins/src/test/groovy/org/gradle/plugins/ide/eclipse/EclipseWtpPluginTest.groovy`** -> AI Confidence: **99.18%**
1246. **`platforms/ide/ide/src/test/groovy/org/gradle/plugins/ide/internal/generator/XmlPersistableConfigurationObjectTest.groovy`** -> AI Confidence: **99.18%**
1247. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r112/BuildInvocationsCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1248. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r213/ModelsWithGradleProjectCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1249. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r26/TestLauncherCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1250. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r27/TestLauncherCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1251. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r32/NonSerializableExceptionCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1252. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r43/CapturingUserInputCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1253. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/ProjectConfigurationProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1254. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r62/CapturingMultipleUserInputCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1255. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r76/BuildPhaseOperationEventCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1256. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r812/BuildFailureProblemsCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1257. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r812/CustomTestEventsCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1258. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r813/CustomTestMetadataEventsCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1259. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r813/JvmArgumentPassingCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1260. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r89/ProblemProgressEventCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1261. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r930/FetchBuildActionCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1262. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/AbstractResourceBasedTestingCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1263. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientGradleBuildBuilderCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1264. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r940/ResilientKotlinDslScriptsModelBuilderCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1265. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ConcurrentToolingApiIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1266. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/GlobalLoggingManipulationIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1267. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1268. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/ProgressEvents.groovy`** -> AI Confidence: **99.18%**
1269. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/ToolingApi.groovy`** -> AI Confidence: **99.18%**
1270. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/ToolingApiExecution.groovy`** -> AI Confidence: **99.18%**
1271. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/checkstyle/CheckstylePluginMultiProjectTest.groovy`** -> AI Confidence: **99.18%**
1272. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/pmd/PmdPluginVersionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1273. **`platforms/jvm/ear/src/integTest/groovy/org/gradle/plugins/ear/EarPluginIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1274. **`platforms/jvm/jvm-services/src/test/groovy/org/gradle/jvm/toolchain/internal/MavenToolchainsInstallationSupplierTest.groovy`** -> AI Confidence: **99.18%**
1275. **`platforms/jvm/language-groovy/src/integTest/groovy/org/gradle/groovy/compile/GroovyCompileToolchainIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1276. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1277. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaExecToolchainIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1278. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/JavaToolchainBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1279. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaAnnotationProcessingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1280. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileToolchainIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1281. **`platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/javadoc/JavadocToolchainIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1282. **`platforms/jvm/plugins-application/src/integTest/groovy/org/gradle/integtests/ApplicationIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1283. **`platforms/jvm/plugins-groovy/src/crossVersionTest/groovy/org/gradle/integtests/StaticGroovyTaskSubclassingBinaryCompatibilityCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1284. **`platforms/jvm/plugins-jvm-test-fixtures/src/testFixtures/groovy/org/gradle/java/fixtures/AbstractTestFixturesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1285. **`platforms/jvm/plugins-jvm-test-suite/src/integTest/groovy/org/gradle/testing/testsuites/TestSuitesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1286. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/integtests/ScalaAnnotationProcessingIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1287. **`platforms/jvm/scala/src/integTest/groovy/org/gradle/scala/compile/ScalaCompileJavaToolchainIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1288. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testsuites/dependencies/TestSuitesGroovyDSLDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1289. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/testsuites/dependencies/TestSuitesKotlinDSLDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1290. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/AbstractNativeLanguageIncrementalBuildIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1291. **`platforms/native/language-native/src/integTest/groovy/org/gradle/language/cpp/CppLanguageParallelIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1292. **`platforms/native/platform-native/src/integTest/groovy/org/gradle/nativeplatform/toolchain/GccToolChainDiscoveryIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1293. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/specs/internal/BuildInitSpecsInteractiveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1294. **`platforms/software/dependency-management/src/crossVersionTest/groovy/org/gradle/integtests/api/problems/internal/ResolutionFailureDataCrossVersionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1295. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ConfigurationCacheDependencyResolutionFeaturesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1296. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/MetadataArtifactResolveTestFixture.groovy`** -> AI Confidence: **99.18%**
1297. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/RemoteDependencyResolveConsoleIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1298. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/RepositoriesDeclaredInSettingsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1299. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/api/ResolvedArtifactsApiIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1300. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/http/AbstractProxyResolveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1301. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/ivy/IvyDynamicRevisionRemoteResolveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1302. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenLocalRepoResolveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1303. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/maven/MavenSnapshotResolveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1304. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/rocache/AbstractReadOnlyCacheDependencyResolutionTest.groovy`** -> AI Confidence: **99.18%**
1305. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/transform/ArtifactTransformWithDependenciesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1306. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/versions/VersionConflictResolutionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1307. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/repositories/resolver/IvyResourcePatternTest.groovy`** -> AI Confidence: **99.18%**
1308. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/artifacts/type/ArtifactTypeRegistryTest.groovy`** -> AI Confidence: **99.18%**
1309. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/catalog/ProjectAccessorsSourceGeneratorTest.groovy`** -> AI Confidence: **99.18%**
1310. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/model/AttributePrecedenceSchemaAttributeMatcherTest.groovy`** -> AI Confidence: **99.18%**
1311. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/resolve/ModuleVersionNotFoundExceptionTest.groovy`** -> AI Confidence: **99.18%**
1312. **`platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/MavenPublishHttpIntegTest.groovy`** -> AI Confidence: **99.18%**
1313. **`platforms/software/platform-base/src/test/groovy/org/gradle/platform/base/internal/registry/AbstractAnnotationModelRuleExtractorTest.groovy`** -> AI Confidence: **99.18%**
1314. **`platforms/software/platform-base/src/test/groovy/org/gradle/platform/base/internal/registry/BinaryTypeModelRuleExtractorTest.groovy`** -> AI Confidence: **99.18%**
1315. **`platforms/software/plugins-distribution/src/integTest/groovy/org/gradle/api/distribution/plugins/DistributionBasePluginTest.groovy`** -> AI Confidence: **99.18%**
1316. **`platforms/software/resources-gcs/src/integTest/groovy/org/gradle/integtests/resource/gcs/maven/MavenGcsRepoErrorsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1317. **`platforms/software/signing/src/integTest/groovy/org/gradle/plugins/signing/SigningIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1318. **`platforms/software/signing/src/testFixtures/groovy/org/gradle/security/fixtures/KeyServer.groovy`** -> AI Confidence: **99.18%**
1319. **`platforms/software/software-diagnostics/src/integTest/groovy/org/gradle/api/tasks/diagnostics/DependencyInsightReportVariantDetailsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1320. **`platforms/software/testing-base/src/integTest/groovy/org/gradle/testing/TestExecutionBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1321. **`platforms/software/testing-base/src/test/groovy/org/gradle/api/internal/tasks/testing/junit/result/JUnitXmlResultWriterSpec.groovy`** -> AI Confidence: **99.18%**
1322. **`platforms/software/testing-base/src/testFixtures/groovy/org/gradle/api/internal/tasks/testing/report/VerifiesGenericTestReportResults.groovy`** -> AI Confidence: **99.18%**
1323. **`platforms/software/testing-base/src/testFixtures/groovy/org/gradle/integtests/fixtures/HtmlTestExecutionResult.groovy`** -> AI Confidence: **99.18%**
1324. **`platforms/software/testing-base/src/testFixtures/groovy/org/gradle/integtests/fixtures/JUnitTestClassExecutionResult.groovy`** -> AI Confidence: **99.18%**
1325. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildConfigurationAttributesResolveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1326. **`subprojects/composite-builds/src/integTest/groovy/org/gradle/integtests/composite/CompositeBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1327. **`subprojects/core/src/integTest/groovy/org/gradle/api/ConfigurationOnDemandIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1328. **`subprojects/core/src/integTest/groovy/org/gradle/api/FinalizerTaskIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1329. **`subprojects/core/src/integTest/groovy/org/gradle/api/InitScriptExecutionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1330. **`subprojects/core/src/integTest/groovy/org/gradle/api/invocation/GradleLifecycleUnsupportedTypesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1331. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CachedImplementationIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1332. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/CopyTaskIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1333. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/GradleBuildTaskIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1334. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/IncrementalInputsIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1335. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/ReproducibleArchivesIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1336. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskCreationBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1337. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskServiceInjectionIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1338. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/bundling/ConcurrentArchiveIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1339. **`subprojects/core/src/integTest/groovy/org/gradle/normalization/ConfigureRuntimeClasspathNormalizationIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1340. **`subprojects/core/src/test/groovy/org/gradle/api/internal/CustomNamedDomainObjectCollectionTest.groovy`** -> AI Confidence: **99.18%**
1341. **`subprojects/core/src/test/groovy/org/gradle/api/internal/catalog/parser/TomlCatalogFileParserTest.groovy`** -> AI Confidence: **99.18%**
1342. **`subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/TaskProvenanceUtilTest.groovy`** -> AI Confidence: **99.18%**
1343. **`subprojects/core/src/test/groovy/org/gradle/caching/internal/packaging/impl/DefaultTarPackerFileSystemSupportTest.groovy`** -> AI Confidence: **99.18%**
1344. **`subprojects/core/src/test/groovy/org/gradle/groovy/scripts/internal/DefaultScriptRunnerFactoryTest.groovy`** -> AI Confidence: **99.18%**
1345. **`subprojects/core/src/test/groovy/org/gradle/internal/classpath/CompositeCallInterceptionTest.groovy`** -> AI Confidence: **99.18%**
1346. **`subprojects/core/src/test/groovy/org/gradle/internal/installation/GradleRuntimeShadedJarDetectorTest.groovy`** -> AI Confidence: **99.18%**
1347. **`subprojects/core/src/test/groovy/org/gradle/internal/model/StateTransitionControllerTest.groovy`** -> AI Confidence: **99.18%**
1348. **`testing/integ-test/src/crossVersionTest/groovy/org/gradle/integtests/AbstractTaskSubclassingBinaryCompatibilityCrossVersionSpec.groovy`** -> AI Confidence: **99.18%**
1349. **`testing/integ-test/src/integTest/groovy/org/gradle/integtests/SyncTaskIntegrationTest.groovy`** -> AI Confidence: **99.18%**
1350. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/daemon/AbstractDaemonFixture.groovy`** -> AI Confidence: **99.18%**
1351. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/test/fixtures/server/http/NtlmAuthenticator.groovy`** -> AI Confidence: **99.18%**
1352. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/AbstractIntegrationSpec.groovy`** -> AI Confidence: **99.18%**
1353. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/CompilationOutputsFixture.groovy`** -> AI Confidence: **99.18%**
1354. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/compatibility/CrossVersionTestInterceptor.groovy`** -> AI Confidence: **99.18%**
1355. **`testing/internal-integ-testing/src/main/groovy/org/gradle/test/fixtures/server/sftp/SFTPServer.groovy`** -> AI Confidence: **99.18%**
1356. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/fixture/BaselineVersionResolver.groovy`** -> AI Confidence: **99.18%**
1357. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/fixture/JavaTestProject.groovy`** -> AI Confidence: **99.18%**
1358. **`testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/archive/JarTestFixture.groovy`** -> AI Confidence: **99.18%**
1359. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/buildcache/AbstractTaskOutputCachingPerformanceTest.groovy`** -> AI Confidence: **99.18%**
1360. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/java/JavaConfigurationCachePerformanceTest.groovy`** -> AI Confidence: **99.18%**
1361. **`testing/performance/src/performanceTest/groovy/org/gradle/performance/regression/java/JavaIncrementalExecutionPerformanceTest.groovy`** -> AI Confidence: **99.18%**
1362. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/AndroidPluginsSmokeTest.groovy`** -> AI Confidence: **99.18%**
1363. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/DevelocityPluginSmokeTest.groovy`** -> AI Confidence: **99.18%**
1364. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/GradleBuildExternalPluginsValidationSmokeTest.groovy`** -> AI Confidence: **99.18%**
1365. **`testing/smoke-test/src/smokeTest/groovy/org/gradle/smoketests/ShadowPluginSmokeTest.groovy`** -> AI Confidence: **99.18%**
1366. **`testing/soak/src/integTest/groovy/org/gradle/jvm/toolchain/JavaToolchainDownloadSoakTest.groovy`** -> AI Confidence: **99.18%**
1367. **`platforms/core-configuration/project-features-demos/src/main/java/org/gradle/api/plugins/java/LibraryDependencies.java`** -> AI Confidence: **99.17%**
1368. **`platforms/core-runtime/instrumentation-reporting/src/main/java/org/gradle/internal/instrumentation/reporting/listener/OnInterceptedMethodInsFormatter.java`** -> AI Confidence: **99.17%**
1369. **`.teamcity/src/main/kotlin/model/BucketExtensions.kt`** -> AI Confidence: **99.17%**
1370. **`build-logic-commons/publishing/src/main/kotlin/gradlebuild.publish-defaults.gradle.kts`** -> AI Confidence: **99.17%**
1371. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild.root-target-runtimes.gradle.kts`** -> AI Confidence: **99.17%**
1372. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r60/ToolingApiPropertiesLoaderCrossVersionSpec.groovy`** -> AI Confidence: **99.17%**
1373. **`testing/internal-testing/src/main/groovy/org/gradle/test/fixtures/concurrent/TestExecutor.groovy`** -> AI Confidence: **99.17%**
1374. **`platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/scalaapplication/multi/list/LinkedList.scala.template`** -> AI Confidence: **99.17%**
1375. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/rules/BinaryBreakingChangesRule.java`** -> AI Confidence: **99.16%**
1376. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/rules/UpgradePropertiesRuleSetup.java`** -> AI Confidence: **99.16%**
1377. **`build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/upgrades/UpgradedProperties.java`** -> AI Confidence: **99.16%**
1378. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/reporting/model/internal/ModelNodeRenderer.java`** -> AI Confidence: **99.16%**
1379. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/PropertyReportTask.java`** -> AI Confidence: **99.16%**
1380. **`platforms/core-configuration/base-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/TaskReportTask.java`** -> AI Confidence: **99.16%**
1381. **`platforms/core-configuration/base-services-groovy/src/main/java/org/gradle/groovy/scripts/internal/AstUtils.java`** -> AI Confidence: **99.16%**
1382. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AbstractFileResolver.java`** -> AI Confidence: **99.16%**
1383. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AbstractFileTreeElement.java`** -> AI Confidence: **99.16%**
1384. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/CompositeFileCollection.java`** -> AI Confidence: **99.16%**
1385. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/FileNotationConverter.java`** -> AI Confidence: **99.16%**
1386. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/UriNotationConverter.java`** -> AI Confidence: **99.16%**
1387. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/PathVisitor.java`** -> AI Confidence: **99.16%**
1388. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/ReproducibleDirectoryWalker.java`** -> AI Confidence: **99.16%**
1389. **`platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/collections/UnpackingVisitor.java`** -> AI Confidence: **99.16%**
1390. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/archive/ZipCopyAction.java`** -> AI Confidence: **99.16%**
1391. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/DefaultCopySpec.java`** -> AI Confidence: **99.16%**
1392. **`platforms/core-configuration/file-operations/src/main/java/org/gradle/api/internal/file/copy/DuplicateHandlingCopyActionDecorator.java`** -> AI Confidence: **99.16%**
1393. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/AbstractCollectionProperty.java`** -> AI Confidence: **99.16%**
1394. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/AbstractMinimalProvider.java`** -> AI Confidence: **99.16%**
1395. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/ValueSupplier.java`** -> AI Confidence: **99.16%**
1396. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/sources/process/ProviderCompatibleBaseExecSpec.java`** -> AI Confidence: **99.16%**
1397. **`platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/CachingTaskDependencyResolveContext.java`** -> AI Confidence: **99.16%**
1398. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/extensibility/ConventionAwareHelper.java`** -> AI Confidence: **99.16%**
1399. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/extensibility/DefaultExtraPropertiesExtension.java`** -> AI Confidence: **99.16%**
1400. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/inspection/DefaultTypeParameterInspection.java`** -> AI Confidence: **99.16%**
1401. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java`** -> AI Confidence: **99.16%**
1402. **`platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/DefaultInstantiationScheme.java`** -> AI Confidence: **99.16%**
1403. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/DefaultNodeInitializerRegistry.java`** -> AI Confidence: **99.16%**
1404. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/ModelMapModelProjection.java`** -> AI Confidence: **99.16%**
1405. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/ModelPath.java`** -> AI Confidence: **99.16%**
1406. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/ModelRegistrations.java`** -> AI Confidence: **99.16%**
1407. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/core/rule/describe/MethodModelRuleDescriptor.java`** -> AI Confidence: **99.16%**
1408. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/DefaultMethodRuleDefinition.java`** -> AI Confidence: **99.16%**
1409. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/ManagedModelCreationRuleExtractor.java`** -> AI Confidence: **99.16%**
1410. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/inspect/StructNodeInitializer.java`** -> AI Confidence: **99.16%**
1411. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/instance/ManagedProxyFactory.java`** -> AI Confidence: **99.16%**
1412. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/projection/ManagedModelProjection.java`** -> AI Confidence: **99.16%**
1413. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/DefaultModelSchemaExtractor.java`** -> AI Confidence: **99.16%**
1414. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/FactoryBasedStructNodeInitializerExtractionStrategy.java`** -> AI Confidence: **99.16%**
1415. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/JavaUtilCollectionStrategy.java`** -> AI Confidence: **99.16%**
1416. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/PropertyAccessorExtractionContext.java`** -> AI Confidence: **99.16%**
1417. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/ScalarCollectionModelView.java`** -> AI Confidence: **99.16%**
1418. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/manage/schema/extract/SpecializedMapStrategy.java`** -> AI Confidence: **99.16%**
1419. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/method/WeaklyTypeReferencingMethod.java`** -> AI Confidence: **99.16%**
1420. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/ModelElementNode.java`** -> AI Confidence: **99.16%**
1421. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/ModelNodeInternal.java`** -> AI Confidence: **99.16%**
1422. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/ModelReferenceNode.java`** -> AI Confidence: **99.16%**
1423. **`platforms/core-configuration/model-core/src/main/java/org/gradle/model/internal/registry/RuleBindings.java`** -> AI Confidence: **99.16%**
1424. **`platforms/core-configuration/model-core/src/main/java/org/gradle/util/internal/ConfigureUtil.java`** -> AI Confidence: **99.16%**
1425. **`platforms/core-configuration/model-groovy/src/main/java/org/gradle/model/dsl/internal/NonTransformedModelDslBacking.java`** -> AI Confidence: **99.16%**
1426. **`platforms/core-configuration/model-groovy/src/main/java/org/gradle/model/dsl/internal/transform/ModelBlockTransformer.java`** -> AI Confidence: **99.16%**
1427. **`platforms/core-configuration/model-reflect/src/main/java/org/gradle/internal/reflect/DefaultTypeValidationContext.java`** -> AI Confidence: **99.16%**
1428. **`platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/DefaultDeclaredProjectFeatureBindingBuilder.java`** -> AI Confidence: **99.16%**
1429. **`platforms/core-execution/build-cache-packaging/src/main/java/org/gradle/caching/internal/packaging/impl/TarBuildCacheEntryPacker.java`** -> AI Confidence: **99.16%**
1430. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/changes/NormalizedPathChangeDetector.java`** -> AI Confidence: **99.16%**
1431. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/impl/FileSystemSnapshotSerializer.java`** -> AI Confidence: **99.16%**
1432. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/model/annotations/ModifierAnnotationCategory.java`** -> AI Confidence: **99.16%**
1433. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/AbstractResolveCachingStateStep.java`** -> AI Confidence: **99.16%**
1434. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/AssignImmutableWorkspaceStep.java`** -> AI Confidence: **99.16%**
1435. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/BuildCacheStep.java`** -> AI Confidence: **99.16%**
1436. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/ResolveChangesStep.java`** -> AI Confidence: **99.16%**
1437. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/SkipEmptyMutableWorkStep.java`** -> AI Confidence: **99.16%**
1438. **`platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/timeout/impl/DefaultTimeoutHandler.java`** -> AI Confidence: **99.16%**
1439. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/AbstractFileWatcherUpdater.java`** -> AI Confidence: **99.16%**
1440. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/registry/impl/NonHierarchicalFileWatcherUpdater.java`** -> AI Confidence: **99.16%**
1441. **`platforms/core-execution/file-watching/src/main/java/org/gradle/internal/watch/vfs/impl/WatchingVirtualFileSystem.java`** -> AI Confidence: **99.16%**
1442. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/DefaultPersistentDirectoryCache.java`** -> AI Confidence: **99.16%**
1443. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/OnDemandFileAccess.java`** -> AI Confidence: **99.16%**
1444. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/filelock/LockStateAccess.java`** -> AI Confidence: **99.16%**
1445. **`platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/locklistener/DefaultFileLockCommunicator.java`** -> AI Confidence: **99.16%**
1446. **`platforms/core-execution/snapshots/src/main/java/org/gradle/internal/vfs/impl/DefaultFileSystemAccess.java`** -> AI Confidence: **99.16%**
1447. **`platforms/core-execution/snapshots/src/main/java/org/gradle/internal/vfs/impl/DefaultSnapshotHierarchy.java`** -> AI Confidence: **99.16%**
1448. **`platforms/core-execution/worker-main/src/main/java/org/gradle/process/internal/worker/messaging/WorkerConfigSerializer.java`** -> AI Confidence: **99.16%**
1449. **`platforms/core-execution/workers/src/main/java/org/gradle/workers/internal/DefaultWorkerExecutor.java`** -> AI Confidence: **99.16%**
1450. **`platforms/core-execution/workers/src/main/java/org/gradle/workers/internal/WorkerDaemonClientsManager.java`** -> AI Confidence: **99.16%**
1451. **`platforms/core-runtime/base-asm/src/main/java/org/gradle/model/internal/asm/AsmClassGeneratorUtils.java`** -> AI Confidence: **99.16%**
1452. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/FileUtils.java`** -> AI Confidence: **99.16%**
1453. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/SystemProperties.java`** -> AI Confidence: **99.16%**
1454. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/jvm/Jvm.java`** -> AI Confidence: **99.16%**
1455. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/service/DefaultServiceLocator.java`** -> AI Confidence: **99.16%**
1456. **`platforms/core-runtime/base-services/src/main/java/org/gradle/internal/xml/XmlFactories.java`** -> AI Confidence: **99.16%**
1457. **`platforms/core-runtime/base-services/src/main/java/org/gradle/util/Path.java`** -> AI Confidence: **99.16%**
1458. **`platforms/core-runtime/build-configuration/src/main/java/org/gradle/internal/buildconfiguration/DaemonJvmPropertiesConfigurator.java`** -> AI Confidence: **99.16%**
1459. **`platforms/core-runtime/build-process-services/src/main/java/org/gradle/api/internal/classpath/ManifestUtil.java`** -> AI Confidence: **99.16%**
1460. **`platforms/core-runtime/build-process-services/src/main/java/org/gradle/api/internal/classpath/ModuleRegistry.java`** -> AI Confidence: **99.16%**
1461. **`platforms/core-runtime/build-profile/src/main/java/org/gradle/profile/BuildProfile.java`** -> AI Confidence: **99.16%**
1462. **`platforms/core-runtime/build-state/src/main/java/org/gradle/internal/buildprocess/execution/StartParamsValidatingActionExecutor.java`** -> AI Confidence: **99.16%**
1463. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/FilteringClassLoader.java`** -> AI Confidence: **99.16%**
1464. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/MultiParentClassLoader.java`** -> AI Confidence: **99.16%**
1465. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/TransformReplacer.java`** -> AI Confidence: **99.16%**
1466. **`platforms/core-runtime/classloaders/src/main/java/org/gradle/internal/classloader/TransformingClassLoader.java`** -> AI Confidence: **99.16%**
1467. **`platforms/core-runtime/client-services/src/main/java/org/gradle/internal/daemon/client/clientinput/DaemonClientInputForwarder.java`** -> AI Confidence: **99.16%**
1468. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/client/DaemonClient.java`** -> AI Confidence: **99.16%**
1469. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/client/DaemonStopClient.java`** -> AI Confidence: **99.16%**
1470. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/client/DefaultDaemonConnector.java`** -> AI Confidence: **99.16%**
1471. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/client/DefaultDaemonStarter.java`** -> AI Confidence: **99.16%**
1472. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/client/NotifyDaemonAboutChangedPathsClient.java`** -> AI Confidence: **99.16%**
1473. **`platforms/core-runtime/client-services/src/main/java/org/gradle/launcher/daemon/toolchain/DaemonJavaToolchainProvisioningService.java`** -> AI Confidence: **99.16%**
1474. **`platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/registry/DaemonRegistryContent.java`** -> AI Confidence: **99.16%**
1475. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/extensions/property/PropertyUpgradeAnnotatedMethodReader.java`** -> AI Confidence: **99.16%**
1476. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/AbstractInstrumentationProcessor.java`** -> AI Confidence: **99.16%**
1477. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/RequestGroupingInstrumentationClassSourceGenerator.java`** -> AI Confidence: **99.16%**
1478. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/groovy/GroovyClassGeneratorUtils.java`** -> AI Confidence: **99.16%**
1479. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/codegen/jvmbytecode/InterceptJvmCallsGenerator.java`** -> AI Confidence: **99.16%**
1480. **`platforms/core-runtime/internal-instrumentation-processor/src/main/java/org/gradle/internal/instrumentation/processor/modelreader/impl/AnnotationUtils.java`** -> AI Confidence: **99.16%**
1481. **`platforms/core-runtime/io/src/main/java/org/gradle/internal/io/StreamByteBuffer.java`** -> AI Confidence: **99.16%**
1482. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/DaemonRegistryUpdater.java`** -> AI Confidence: **99.16%**
1483. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/api/HandleStop.java`** -> AI Confidence: **99.16%**
1484. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/LogToClient.java`** -> AI Confidence: **99.16%**
1485. **`platforms/core-runtime/launcher/src/main/java/org/gradle/launcher/daemon/server/health/LowMemoryDaemonExpirationStrategy.java`** -> AI Confidence: **99.16%**
1486. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/ForwardStdInToThisProcess.java`** -> AI Confidence: **99.16%**
1487. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/ProviderStartParameterConverter.java`** -> AI Confidence: **99.16%**
1488. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/SubscribableBuildActionExecutor.java`** -> AI Confidence: **99.16%**
1489. **`platforms/core-runtime/launcher/src/main/java/org/gradle/tooling/internal/provider/continuous/ContinuousBuildActionExecutor.java`** -> AI Confidence: **99.16%**
1490. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/AbstractUserInputRenderer.java`** -> AI Confidence: **99.16%**
1491. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/console/ProgressBar.java`** -> AI Confidence: **99.16%**
1492. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/progress/DefaultProgressLoggerFactory.java`** -> AI Confidence: **99.16%**
1493. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/services/DefaultLoggingManager.java`** -> AI Confidence: **99.16%**
1494. **`platforms/core-runtime/logging/src/main/java/org/gradle/internal/problems/failure/DefaultFailureFactory.java`** -> AI Confidence: **99.16%**
1495. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/event/BroadcastDispatch.java`** -> AI Confidence: **99.16%**
1496. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/hub/InterHubMessageSerializer.java`** -> AI Confidence: **99.16%**
1497. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/inet/InetAddressFactory.java`** -> AI Confidence: **99.16%**
1498. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/inet/SocketConnection.java`** -> AI Confidence: **99.16%**
1499. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/inet/TcpIncomingConnector.java`** -> AI Confidence: **99.16%**
1500. **`platforms/core-runtime/messaging/src/main/java/org/gradle/internal/remote/internal/inet/TcpOutgoingConnector.java`** -> AI Confidence: **99.16%**
1501. **`platforms/core-runtime/native/src/main/java/org/gradle/internal/nativeintegration/services/NativeServices.java`** -> AI Confidence: **99.16%**
1502. **`platforms/core-runtime/process-memory-services/src/main/java/org/gradle/process/internal/health/memory/DefaultMBeanAttributeProvider.java`** -> AI Confidence: **99.16%**
1503. **`platforms/core-runtime/process-memory-services/src/main/java/org/gradle/process/internal/health/memory/DefaultMemoryManager.java`** -> AI Confidence: **99.16%**
1504. **`platforms/core-runtime/process-services-base/src/main/java/org/gradle/process/internal/DefaultExecHandle.java`** -> AI Confidence: **99.16%**
1505. **`platforms/core-runtime/serialization/src/main/java/org/gradle/tooling/internal/provider/serialization/ClassLoaderCache.java`** -> AI Confidence: **99.16%**
1506. **`platforms/core-runtime/serialization/src/main/java/org/gradle/tooling/internal/provider/serialization/WellKnownClassLoaderRegistry.java`** -> AI Confidence: **99.16%**
1507. **`platforms/core-runtime/service-registry-impl/src/main/java/org/gradle/internal/service/DefaultServiceRegistry.java`** -> AI Confidence: **99.16%**
1508. **`platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/exceptions/DefaultMultiCauseException.java`** -> AI Confidence: **99.16%**
1509. **`platforms/core-runtime/wrapper-shared/src/main/java/org/gradle/wrapper/Download.java`** -> AI Confidence: **99.16%**
1510. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/internal/precompiled/PrecompiledGroovyPluginsPlugin.java`** -> AI Confidence: **99.16%**
1511. **`platforms/extensibility/plugin-development/src/main/java/org/gradle/plugin/devel/tasks/GeneratePluginDescriptors.java`** -> AI Confidence: **99.16%**
1512. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/features/internal/binding/DefaultProjectFeatureDeclarations.java`** -> AI Confidence: **99.16%**
1513. **`platforms/extensibility/plugin-use/src/main/java/org/gradle/plugin/use/resolve/service/internal/DefaultInjectedClasspathPluginResolver.java`** -> AI Confidence: **99.16%**
1514. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/internal/NativeSpecVisualStudioTargetBinary.java`** -> AI Confidence: **99.16%**
1515. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/tasks/GenerateProjectFileTask.java`** -> AI Confidence: **99.16%**
1516. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/visualstudio/tasks/internal/VisualStudioSolutionFile.java`** -> AI Confidence: **99.16%**
1517. **`platforms/ide/ide-native/src/main/java/org/gradle/ide/xcode/tasks/GenerateXcodeProjectFileTask.java`** -> AI Confidence: **99.16%**
1518. **`platforms/ide/ide-plugins/src/main/java/org/gradle/plugins/ide/idea/model/Project.java`** -> AI Confidence: **99.16%**
1519. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/AbstractClasspathEntry.java`** -> AI Confidence: **99.16%**
1520. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/eclipse/model/WtpComponent.java`** -> AI Confidence: **99.16%**
1521. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/idea/model/ProjectLibrary.java`** -> AI Confidence: **99.16%**
1522. **`platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/resolver/DefaultGradleApiSourcesResolver.java`** -> AI Confidence: **99.16%**
1523. **`platforms/ide/problems-api/src/main/java/org/gradle/api/problems/internal/BuildOperationProblem.java`** -> AI Confidence: **99.16%**
1524. **`platforms/ide/problems-api/src/main/java/org/gradle/api/problems/internal/DefaultProblemBuilder.java`** -> AI Confidence: **99.16%**
1525. **`platforms/ide/tooling-api-builders/src/main/java/org/gradle/tooling/internal/provider/runner/TestOperationMapper.java`** -> AI Confidence: **99.16%**
1526. **`platforms/ide/tooling-api/src/crossVersionTestModels/java/org/gradle/integtests/tooling/r940/KotlinModelAction.java`** -> AI Confidence: **99.16%**
1527. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/HelpModelCompatibilityHelper.java`** -> AI Confidence: **99.16%**
1528. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/LazyConsumerActionExecutor.java`** -> AI Confidence: **99.16%**
1529. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/connection/UnparameterizedBuildController.java`** -> AI Confidence: **99.16%**
1530. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/loader/SynchronizedToolingImplementationLoader.java`** -> AI Confidence: **99.16%**
1531. **`platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/consumer/parameters/BuildProgressListenerAdapter.java`** -> AI Confidence: **99.16%**
1532. **`platforms/jvm/antlr/src/main/java/org/gradle/api/plugins/antlr/internal/antlr2/MetadataExtractor.java`** -> AI Confidence: **99.16%**
1533. **`platforms/jvm/java-compiler-plugin/src/main/java/org/gradle/internal/compiler/java/listeners/constants/ConstantsTreeVisitor.java`** -> AI Confidence: **99.16%**
1534. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/AnnotationProcessingCompileTask.java`** -> AI Confidence: **99.16%**
1535. **`platforms/jvm/java-compiler-worker/src/main/java/org/gradle/api/internal/tasks/compile/DiagnosticToProblemListener.java`** -> AI Confidence: **99.16%**
1536. **`platforms/jvm/jvm-services/src/main/java/org/gradle/api/internal/artifacts/JavaEcosystemSupport.java`** -> AI Confidence: **99.16%**
1537. **`platforms/jvm/jvm-services/src/main/java/org/gradle/internal/jvm/DefaultJavaModuleDetector.java`** -> AI Confidence: **99.16%**
1538. **`platforms/jvm/jvm-services/src/main/java/org/gradle/internal/jvm/inspection/DefaultJavaInstallationRegistry.java`** -> AI Confidence: **99.16%**
1539. **`platforms/jvm/jvm-services/src/main/java/org/gradle/internal/jvm/inspection/DefaultJvmMetadataDetector.java`** -> AI Confidence: **99.16%**
1540. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/AnnotationProcessorDiscoveringCompiler.java`** -> AI Confidence: **99.16%**
1541. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/NormalizingJavaCompiler.java`** -> AI Confidence: **99.16%**
1542. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/IncrementalResultStoringCompiler.java`** -> AI Confidence: **99.16%**
1543. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/classpath/DefaultClassSetAnalyzer.java`** -> AI Confidence: **99.16%**
1544. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/deps/ClassSetAnalysis.java`** -> AI Confidence: **99.16%**
1545. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/recomp/AbstractRecompilationSpecProvider.java`** -> AI Confidence: **99.16%**
1546. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/incremental/transaction/CompileTransaction.java`** -> AI Confidence: **99.16%**
1547. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/processing/AnnotationProcessorDetector.java`** -> AI Confidence: **99.16%**
1548. **`platforms/jvm/language-java/src/main/java/org/gradle/api/internal/tasks/compile/tooling/JavaCompileTaskSuccessResultPostProcessor.java`** -> AI Confidence: **99.16%**
1549. **`platforms/jvm/platform-jvm/src/main/java/org/gradle/api/java/archives/internal/DefaultManifest.java`** -> AI Confidence: **99.16%**
1550. **`platforms/jvm/plugins-application/src/main/java/org/gradle/api/internal/plugins/StartScriptTemplateBindingFactory.java`** -> AI Confidence: **99.16%**
1551. **`platforms/jvm/plugins-java-base/src/main/java/org/gradle/api/plugins/internal/JvmPluginsHelper.java`** -> AI Confidence: **99.16%**
1552. **`platforms/jvm/scala-compiler-worker/src/main/java/org/gradle/api/internal/tasks/scala/ZincScalaCompilerFactory.java`** -> AI Confidence: **99.16%**
1553. **`platforms/jvm/scala/src/main/java/org/gradle/api/tasks/ScalaRuntime.java`** -> AI Confidence: **99.16%**
1554. **`platforms/jvm/scaladoc-worker/src/main/java/org/gradle/api/tasks/scala/internal/GenerateScaladoc.java`** -> AI Confidence: **99.16%**
1555. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/junit/JUnitTestExecutor.java`** -> AI Confidence: **99.16%**
1556. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/junitplatform/JUnitPlatformTestDefinitionProcessor.java`** -> AI Confidence: **99.16%**
1557. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/testng/TestNGTestDefinitionProcessor.java`** -> AI Confidence: **99.16%**
1558. **`platforms/jvm/testing-jvm-infrastructure/src/main/java/org/gradle/api/internal/tasks/testing/testng/TestNGTestResultProcessorAdapter.java`** -> AI Confidence: **99.16%**
1559. **`platforms/jvm/testing-jvm/src/main/java/org/gradle/api/internal/tasks/testing/detection/AbstractTestFrameworkDetector.java`** -> AI Confidence: **99.16%**
1560. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/multi-file-rbt-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/MultiFileResourceBasedSelectorResolver.java`** -> AI Confidence: **99.16%**
1561. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/parallel-rbt-engine/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/ParallelResourceBasedTestEngine.java`** -> AI Confidence: **99.16%**
1562. **`platforms/jvm/testing-jvm/src/testFixtures/resources/testengines/shared/test-engine-build/src/main/java/org/gradle/testing/testengine/engine/ResourceBasedSelectorResolver.java`** -> AI Confidence: **99.16%**
1563. **`platforms/jvm/toolchains-jvm-shared/src/main/java/org/gradle/jvm/toolchain/internal/install/JavaToolchainProvisioningService.java`** -> AI Confidence: **99.16%**
1564. **`platforms/jvm/toolchains-jvm/src/main/java/org/gradle/jvm/internal/services/DefaultJvmToolchainsConfigurationValidator.java`** -> AI Confidence: **99.16%**
1565. **`platforms/jvm/toolchains-jvm/src/main/java/org/gradle/jvm/toolchain/internal/install/DefaultJavaToolchainProvisioningService.java`** -> AI Confidence: **99.16%**
1566. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/Dimensions.java`** -> AI Confidence: **99.16%**
1567. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/CollectingMacroLookup.java`** -> AI Confidence: **99.16%**
1568. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/CompilationStateSerializer.java`** -> AI Confidence: **99.16%**
1569. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/IncrementalCompileFilesFactory.java`** -> AI Confidence: **99.16%**
1570. **`platforms/native/language-native/src/main/java/org/gradle/language/nativeplatform/internal/incremental/sourceparser/RegexBackedCSourceParser.java`** -> AI Confidence: **99.16%**
1571. **`platforms/native/language-native/src/main/java/org/gradle/swiftpm/plugins/SwiftPackageManagerExportPlugin.java`** -> AI Confidence: **99.16%**
1572. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/internal/NativeDependentBinariesResolutionStrategy.java`** -> AI Confidence: **99.16%**
1573. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/internal/resolve/DefaultLibraryResolver.java`** -> AI Confidence: **99.16%**
1574. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/AbstractPlatformToolProvider.java`** -> AI Confidence: **99.16%**
1575. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/PCHUtils.java`** -> AI Confidence: **99.16%**
1576. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/AbstractWindowsKitComponentLocator.java`** -> AI Confidence: **99.16%**
1577. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/DefaultVisualStudioLocator.java`** -> AI Confidence: **99.16%**
1578. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/LegacyWindowsSdkLocator.java`** -> AI Confidence: **99.16%**
1579. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/msvcpp/version/CommandLineToolVersionLocator.java`** -> AI Confidence: **99.16%**
1580. **`platforms/native/platform-native/src/main/java/org/gradle/nativeplatform/toolchain/internal/tools/ToolSearchPath.java`** -> AI Confidence: **99.16%**
1581. **`platforms/native/platform-native/src/testFixtures/groovy/org/gradle/nativeplatform/fixtures/AvailableToolChains.java`** -> AI Confidence: **99.16%**
1582. **`platforms/software/ant-impl/src/main/java/org/gradle/api/internal/project/antbuilder/ClassPathToClassLoaderCache.java`** -> AI Confidence: **99.16%**
1583. **`platforms/software/ant/src/main/java/org/gradle/api/internal/project/antbuilder/AntBuilderDelegate.java`** -> AI Confidence: **99.16%**
1584. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/GitIgnoreGenerator.java`** -> AI Confidence: **99.16%**
1585. **`platforms/software/build-init/src/main/java/org/gradle/buildinit/tasks/InitBuild.java`** -> AI Confidence: **99.16%**
1586. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/DefaultConfigurationContainer.java`** -> AI Confidence: **99.16%**
1587. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/DefaultConfigurationPublications.java`** -> AI Confidence: **99.16%**
1588. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/ResolutionHost.java`** -> AI Confidence: **99.16%**
1589. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/configurations/ResolveConfigurationResolutionBuildOperationDetails.java`** -> AI Confidence: **99.16%**
1590. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/ComponentSelectorParsers.java`** -> AI Confidence: **99.16%**
1591. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/ModuleComponentSelectorParsers.java`** -> AI Confidence: **99.16%**
1592. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/DefaultDependencyConstraintHandler.java`** -> AI Confidence: **99.16%**
1593. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/NewerGradleNeededByPluginFailureDescriber.java`** -> AI Confidence: **99.16%**
1594. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/DefaultCacheExpirationControl.java`** -> AI Confidence: **99.16%**
1595. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/dependencysubstitution/DefaultDependencyResolveDetails.java`** -> AI Confidence: **99.16%**
1596. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/DefaultVersionedComponentChooser.java`** -> AI Confidence: **99.16%**
1597. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/DynamicVersionResolver.java`** -> AI Confidence: **99.16%**
1598. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/parser/GradlePomModuleDescriptorBuilder.java`** -> AI Confidence: **99.16%**
1599. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/verification/writer/WriteDependencyVerificationFile.java`** -> AI Confidence: **99.16%**
1600. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/projectmodule/DefaultProjectDependencyPublicationResolver.java`** -> AI Confidence: **99.16%**
1601. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolutionstrategy/DefaultCapabilitiesResolution.java`** -> AI Confidence: **99.16%**
1602. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/artifact/VariantResolvingArtifactSet.java`** -> AI Confidence: **99.16%**
1603. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/factories/ExcludeFactory.java`** -> AI Confidence: **99.16%**
1604. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/factories/LoggingExcludeFactory.java`** -> AI Confidence: **99.16%**
1605. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/excludes/factories/NormalizingExcludeFactory.java`** -> AI Confidence: **99.16%**
1606. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/ComponentState.java`** -> AI Confidence: **99.16%**
1607. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/ModuleSelectors.java`** -> AI Confidence: **99.16%**
1608. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/SelectorState.java`** -> AI Confidence: **99.16%**
1609. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/builder/VirtualPlatformState.java`** -> AI Confidence: **99.16%**
1610. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/ConflictContainer.java`** -> AI Confidence: **99.16%**
1611. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/DefaultCapabilitiesConflictHandler.java`** -> AI Confidence: **99.16%**
1612. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/DefaultModuleConflictHandler.java`** -> AI Confidence: **99.16%**
1613. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/conflicts/VersionConflictResolutionDetails.java`** -> AI Confidence: **99.16%**
1614. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/selectors/SelectorStateResolver.java`** -> AI Confidence: **99.16%**
1615. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/graph/selectors/SelectorStateResolverResults.java`** -> AI Confidence: **99.16%**
1616. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/ComponentSelectorSerializer.java`** -> AI Confidence: **99.16%**
1617. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/DesugaredAttributeContainerSerializer.java`** -> AI Confidence: **99.16%**
1618. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/result/StreamingResolutionResultBuilder.java`** -> AI Confidence: **99.16%**
1619. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/resolveengine/store/DefaultBinaryStore.java`** -> AI Confidence: **99.16%**
1620. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/AuthenticationSupporter.java`** -> AI Confidence: **99.16%**
1621. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/resolver/DefaultExternalResourceArtifactResolver.java`** -> AI Confidence: **99.16%**
1622. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/repositories/transport/RepositoryTransportFactory.java`** -> AI Confidence: **99.16%**
1623. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/ConsumerProvidedVariantFinder.java`** -> AI Confidence: **99.16%**
1624. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/transform/DefaultVariantTransformRegistry.java`** -> AI Confidence: **99.16%**
1625. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/serializer/DependencyVerificationsXmlWriter.java`** -> AI Confidence: **99.16%**
1626. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/signatures/CrossBuildSignatureVerificationService.java`** -> AI Confidence: **99.16%**
1627. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/verifier/DependencyVerificationConfiguration.java`** -> AI Confidence: **99.16%**
1628. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/verification/verifier/SignatureVerificationFailure.java`** -> AI Confidence: **99.16%**
1629. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/DefaultAttributesSchema.java`** -> AI Confidence: **99.16%**
1630. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/attributes/matching/MultipleCandidateMatcher.java`** -> AI Confidence: **99.16%**
1631. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/catalog/DefaultVersionCatalogBuilder.java`** -> AI Confidence: **99.16%**
1632. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/catalog/SimpleGeneratedJavaClassCompiler.java`** -> AI Confidence: **99.16%**
1633. **`platforms/software/dependency-management/src/main/java/org/gradle/api/internal/runtimeshaded/RuntimeShadedJarCreator.java`** -> AI Confidence: **99.16%**
1634. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/AbstractLazyModuleComponentResolveMetadata.java`** -> AI Confidence: **99.16%**
1635. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/AbstractRealisedModuleResolveMetadataSerializationHelper.java`** -> AI Confidence: **99.16%**
1636. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/LazyRuleAwareWithBaseConfigurationMetadata.java`** -> AI Confidence: **99.16%**
1637. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/LazyToRealisedModuleComponentResolveMetadataHelper.java`** -> AI Confidence: **99.16%**
1638. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ivy/RealisedIvyModuleResolveMetadata.java`** -> AI Confidence: **99.16%**
1639. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/ivy/RealisedIvyModuleResolveMetadataSerializationHelper.java`** -> AI Confidence: **99.16%**
1640. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/maven/RealisedMavenModuleResolveMetadata.java`** -> AI Confidence: **99.16%**
1641. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/external/model/maven/RealisedMavenModuleResolveMetadataSerializationHelper.java`** -> AI Confidence: **99.16%**
1642. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/model/VariantFilesRules.java`** -> AI Confidence: **99.16%**
1643. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/AmbiguousArtifactTransformsFailureDescriber.java`** -> AI Confidence: **99.16%**
1644. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/component/resolution/failure/describer/ModuleRejectedIncompatibleConstraintsFailureDescriber.java`** -> AI Confidence: **99.16%**
1645. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/management/DefaultDependencyResolutionManagement.java`** -> AI Confidence: **99.16%**
1646. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resolve/caching/CrossBuildCachingRuleExecutor.java`** -> AI Confidence: **99.16%**
1647. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resolve/caching/DesugaringAttributeContainerSerializer.java`** -> AI Confidence: **99.16%**
1648. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/resource/transfer/DefaultCacheAwareExternalResourceAccessor.java`** -> AI Confidence: **99.16%**
1649. **`platforms/software/dependency-management/src/main/java/org/gradle/internal/rules/RuleSourceBackedRuleAction.java`** -> AI Confidence: **99.16%**
1650. **`platforms/software/ivy/src/main/java/org/gradle/api/publish/ivy/internal/publication/IvyComponentParser.java`** -> AI Confidence: **99.16%**
1651. **`platforms/software/ivy/src/main/java/org/gradle/api/publish/ivy/internal/tasks/IvyDescriptorFileGenerator.java`** -> AI Confidence: **99.16%**
1652. **`platforms/software/ivy/src/main/java/org/gradle/api/publish/ivy/internal/versionmapping/DefaultVersionMappingStrategy.java`** -> AI Confidence: **99.16%**
1653. **`platforms/software/maven/src/main/java/org/gradle/api/publish/maven/internal/publisher/ValidatingMavenPublisher.java`** -> AI Confidence: **99.16%**
1654. **`platforms/software/platform-base/src/main/java/org/gradle/api/internal/resolve/LibraryResolutionResult.java`** -> AI Confidence: **99.16%**
1655. **`platforms/software/platform-base/src/main/java/org/gradle/language/base/internal/tasks/StaleOutputCleaner.java`** -> AI Confidence: **99.16%**
1656. **`platforms/software/platform-base/src/main/java/org/gradle/platform/base/internal/registry/ComponentTypeModelRuleExtractor.java`** -> AI Confidence: **99.16%**
1657. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/component/DefaultAdhocSoftwareComponent.java`** -> AI Confidence: **99.16%**
1658. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/metadata/InvalidPublicationChecker.java`** -> AI Confidence: **99.16%**
1659. **`platforms/software/publish/src/main/java/org/gradle/api/publish/internal/versionmapping/DefaultVersionMappingStrategy.java`** -> AI Confidence: **99.16%**
1660. **`platforms/software/resources-gcs/src/main/java/org/gradle/internal/resource/transport/gcp/gcs/GcsClient.java`** -> AI Confidence: **99.16%**
1661. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/HttpClientConfigurer.java`** -> AI Confidence: **99.16%**
1662. **`platforms/software/resources-http/src/main/java/org/gradle/internal/resource/transport/http/HttpResponseResource.java`** -> AI Confidence: **99.16%**
1663. **`platforms/software/resources-s3/src/main/java/org/gradle/internal/resource/transport/aws/s3/S3Client.java`** -> AI Confidence: **99.16%**
1664. **`platforms/software/resources-s3/src/main/java/org/gradle/internal/resource/transport/aws/s3/S3ResourceConnector.java`** -> AI Confidence: **99.16%**
1665. **`platforms/software/resources-s3/src/main/java/org/gradle/internal/resource/transport/aws/s3/S3ResourceResolver.java`** -> AI Confidence: **99.16%**
1666. **`platforms/software/resources-sftp/src/main/java/org/gradle/internal/resource/transport/sftp/SftpResourceAccessor.java`** -> AI Confidence: **99.16%**
1667. **`platforms/software/resources-sftp/src/main/java/org/gradle/internal/resource/transport/sftp/SftpResourceUploader.java`** -> AI Confidence: **99.16%**
1668. **`platforms/software/resources/src/main/java/org/gradle/internal/resource/local/LocalFileStandInExternalResource.java`** -> AI Confidence: **99.16%**
1669. **`platforms/software/security/src/main/java/org/gradle/security/internal/KeyringFilePublicKeyService.java`** -> AI Confidence: **99.16%**
1670. **`platforms/software/signing/src/main/java/org/gradle/plugins/signing/SignOperation.java`** -> AI Confidence: **99.16%**
1671. **`platforms/software/signing/src/main/java/org/gradle/plugins/signing/Signature.java`** -> AI Confidence: **99.16%**
1672. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/components/internal/SourceSetRenderer.java`** -> AI Confidence: **99.16%**
1673. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/dependencies/internal/JsonProjectDependencyRenderer.java`** -> AI Confidence: **99.16%**
1674. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/reporting/dependents/internal/DependentComponentsRenderer.java`** -> AI Confidence: **99.16%**
1675. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/DependencyInsightReportTask.java`** -> AI Confidence: **99.16%**
1676. **`platforms/software/software-diagnostics/src/main/java/org/gradle/api/tasks/diagnostics/internal/insight/DependencyResultSorter.java`** -> AI Confidence: **99.16%**
1677. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/DefaultRootTestEventReporter.java`** -> AI Confidence: **99.16%**
1678. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/LifecycleTrackingTestEventReporter.java`** -> AI Confidence: **99.16%**
1679. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/junit/result/Binary2JUnitXmlReportGenerator.java`** -> AI Confidence: **99.16%**
1680. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/logging/TestCountLogger.java`** -> AI Confidence: **99.16%**
1681. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/logging/TestEventLogger.java`** -> AI Confidence: **99.16%**
1682. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/GenericHtmlTestReportGenerator.java`** -> AI Confidence: **99.16%**
1683. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/report/generic/GenericPageRenderer.java`** -> AI Confidence: **99.16%**
1684. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/results/StateTrackingTestResultProcessor.java`** -> AI Confidence: **99.16%**
1685. **`platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/worker/ForkingTestDefinitionProcessor.java`** -> AI Confidence: **99.16%**
1686. **`platforms/software/version-control/src/main/java/org/gradle/vcs/git/internal/GitVersionControlSystem.java`** -> AI Confidence: **99.16%**
1687. **`platforms/software/version-control/src/main/java/org/gradle/vcs/internal/DefaultVcsMappingsStore.java`** -> AI Confidence: **99.16%**
1688. **`platforms/software/version-control/src/main/java/org/gradle/vcs/internal/resolver/DefaultVcsVersionWorkingDirResolver.java`** -> AI Confidence: **99.16%**
1689. **`subprojects/composite-builds/src/main/java/org/gradle/composite/internal/DefaultBuildControllers.java`** -> AI Confidence: **99.16%**
1690. **`subprojects/core-api/src/main/java/org/gradle/api/artifacts/dsl/DependencyCollector.java`** -> AI Confidence: **99.16%**
1691. **`subprojects/core-api/src/main/java/org/gradle/api/artifacts/dsl/DependencyHandler.java`** -> AI Confidence: **99.16%**
1692. **`subprojects/core-api/src/main/java/org/gradle/api/file/CopySpec.java`** -> AI Confidence: **99.16%**
1693. **`subprojects/core-api/src/main/java/org/gradle/api/provider/Provider.java`** -> AI Confidence: **99.16%**
1694. **`subprojects/core-api/src/main/java/org/gradle/api/tasks/util/PatternSet.java`** -> AI Confidence: **99.16%**
1695. **`subprojects/core/src/main/java/org/gradle/api/internal/CompositeDomainObjectSet.java`** -> AI Confidence: **99.16%**
1696. **`subprojects/core/src/main/java/org/gradle/api/internal/DefaultPolymorphicNamedEntityInstantiator.java`** -> AI Confidence: **99.16%**
1697. **`subprojects/core/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/DefaultDependencyCollector.java`** -> AI Confidence: **99.16%**
1698. **`subprojects/core/src/main/java/org/gradle/api/internal/artifacts/dsl/dependencies/DependenciesExtensionModule.java`** -> AI Confidence: **99.16%**
1699. **`subprojects/core/src/main/java/org/gradle/api/internal/attributes/HierarchicalMutableAttributeContainer.java`** -> AI Confidence: **99.16%**
1700. **`subprojects/core/src/main/java/org/gradle/api/internal/attributes/IncubatingAttributesChecker.java`** -> AI Confidence: **99.16%**
1701. **`subprojects/core/src/main/java/org/gradle/api/internal/collections/AbstractIterationOrderRetainingElementSource.java`** -> AI Confidence: **99.16%**
1702. **`subprojects/core/src/main/java/org/gradle/api/internal/collections/SortedSetElementSource.java`** -> AI Confidence: **99.16%**
1703. **`subprojects/core/src/main/java/org/gradle/api/internal/initialization/loadercache/DefaultClassLoaderCache.java`** -> AI Confidence: **99.16%**
1704. **`subprojects/core/src/main/java/org/gradle/api/internal/plugins/DefaultPluginContainer.java`** -> AI Confidence: **99.16%**
1705. **`subprojects/core/src/main/java/org/gradle/api/internal/plugins/ProjectFeatureDeclarationPluginTarget.java`** -> AI Confidence: **99.16%**
1706. **`subprojects/core/src/main/java/org/gradle/api/internal/project/BuildOperationCrossProjectConfigurator.java`** -> AI Confidence: **99.16%**
1707. **`subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultCrossProjectModelAccess.java`** -> AI Confidence: **99.16%**
1708. **`subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultProjectStateRegistry.java`** -> AI Confidence: **99.16%**
1709. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/DefaultTaskContainer.java`** -> AI Confidence: **99.16%**
1710. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/TaskStatistics.java`** -> AI Confidence: **99.16%**
1711. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/DefaultTaskCacheabilityResolver.java`** -> AI Confidence: **99.16%**
1712. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/execution/TaskExecution.java`** -> AI Confidence: **99.16%**
1713. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/InspectionSchemeFactory.java`** -> AI Confidence: **99.16%**
1714. **`subprojects/core/src/main/java/org/gradle/api/internal/tasks/properties/OutputUnpacker.java`** -> AI Confidence: **99.16%**
1715. **`subprojects/core/src/main/java/org/gradle/api/services/internal/BuildServiceProvider.java`** -> AI Confidence: **99.16%**
1716. **`subprojects/core/src/main/java/org/gradle/api/services/internal/ConsumedBuildServiceProvider.java`** -> AI Confidence: **99.16%**
1717. **`subprojects/core/src/main/java/org/gradle/api/services/internal/RegisteredBuildServiceProvider.java`** -> AI Confidence: **99.16%**
1718. **`subprojects/core/src/main/java/org/gradle/cache/internal/VersionSpecificCacheCleanupAction.java`** -> AI Confidence: **99.16%**
1719. **`subprojects/core/src/main/java/org/gradle/configuration/BuildOperationScriptPlugin.java`** -> AI Confidence: **99.16%**
1720. **`subprojects/core/src/main/java/org/gradle/deployment/internal/DefaultDeploymentRegistry.java`** -> AI Confidence: **99.16%**
1721. **`subprojects/core/src/main/java/org/gradle/execution/TaskNameResolver.java`** -> AI Confidence: **99.16%**
1722. **`subprojects/core/src/main/java/org/gradle/execution/TaskPathProjectEvaluator.java`** -> AI Confidence: **99.16%**
1723. **`subprojects/core/src/main/java/org/gradle/execution/plan/DefaultExecutionPlan.java`** -> AI Confidence: **99.16%**
1724. **`subprojects/core/src/main/java/org/gradle/execution/plan/DetermineExecutionPlanAction.java`** -> AI Confidence: **99.16%**
1725. **`subprojects/core/src/main/java/org/gradle/execution/plan/LocalTaskNode.java`** -> AI Confidence: **99.16%**
1726. **`subprojects/core/src/main/java/org/gradle/execution/plan/NodeSets.java`** -> AI Confidence: **99.16%**
1727. **`subprojects/core/src/main/java/org/gradle/execution/plan/ResolveMutationsNode.java`** -> AI Confidence: **99.16%**
1728. **`subprojects/core/src/main/java/org/gradle/execution/plan/TaskInAnotherBuild.java`** -> AI Confidence: **99.16%**
1729. **`subprojects/core/src/main/java/org/gradle/execution/plan/ToPlannedNodeConverterRegistry.java`** -> AI Confidence: **99.16%**
1730. **`subprojects/core/src/main/java/org/gradle/execution/selection/DefaultBuildTaskSelector.java`** -> AI Confidence: **99.16%**
1731. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/DefaultScriptCompilationHandler.java`** -> AI Confidence: **99.16%**
1732. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/InitialPassStatementTransformer.java`** -> AI Confidence: **99.16%**
1733. **`subprojects/core/src/main/java/org/gradle/groovy/scripts/internal/SubsetScriptTransformer.java`** -> AI Confidence: **99.16%**
1734. **`subprojects/core/src/main/java/org/gradle/internal/buildevents/BuildExceptionReporter.java`** -> AI Confidence: **99.16%**
1735. **`subprojects/core/src/main/java/org/gradle/internal/buildtree/BuildInclusionCoordinator.java`** -> AI Confidence: **99.16%**
1736. **`subprojects/core/src/main/java/org/gradle/internal/buildtree/IntermediateBuildActionRunner.java`** -> AI Confidence: **99.16%**
1737. **`subprojects/core/src/main/java/org/gradle/internal/classpath/ClasspathWalker.java`** -> AI Confidence: **99.16%**
1738. **`subprojects/core/src/main/java/org/gradle/internal/classpath/DefaultClasspathBuilder.java`** -> AI Confidence: **99.16%**
1739. **`subprojects/core/src/main/java/org/gradle/internal/classpath/intercept/DefaultCallSiteDecorator.java`** -> AI Confidence: **99.16%**
1740. **`subprojects/core/src/main/java/org/gradle/internal/classpath/transforms/LambdaSerializationTransformer.java`** -> AI Confidence: **99.16%**
1741. **`subprojects/core/src/main/java/org/gradle/internal/cleanup/DefaultBuildOutputCleanupRegistry.java`** -> AI Confidence: **99.16%**
1742. **`subprojects/core/src/main/java/org/gradle/internal/model/CalculatedValueContainer.java`** -> AI Confidence: **99.16%**
1743. **`subprojects/core/src/main/java/org/gradle/internal/operations/logging/LoggingBuildOperationProgressBroadcaster.java`** -> AI Confidence: **99.16%**
1744. **`subprojects/core/src/main/java/org/gradle/internal/operations/notify/BuildOperationNotificationBridge.java`** -> AI Confidence: **99.16%**
1745. **`subprojects/core/src/main/java/org/gradle/internal/problems/DefaultProblemLocationAnalyzer.java`** -> AI Confidence: **99.16%**
1746. **`subprojects/core/src/main/java/org/gradle/internal/resource/local/DefaultPathKeyFileStore.java`** -> AI Confidence: **99.16%**
1747. **`subprojects/core/src/main/java/org/gradle/internal/service/scopes/DefaultGradleUserHomeScopeServiceRegistry.java`** -> AI Confidence: **99.16%**
1748. **`subprojects/core/src/main/java/org/gradle/internal/typeconversion/MapNotationConverter.java`** -> AI Confidence: **99.16%**
1749. **`subprojects/core/src/main/java/org/gradle/internal/xml/XmlTransformer.java`** -> AI Confidence: **99.16%**
1750. **`subprojects/core/src/main/java/org/gradle/normalization/internal/DefaultRuntimeClasspathNormalization.java`** -> AI Confidence: **99.16%**
1751. **`subprojects/core/src/main/java/org/gradle/util/internal/JarUtil.java`** -> AI Confidence: **99.16%**
1752. **`subprojects/core/src/testFixtures/groovy/org/gradle/api/tasks/TaskDependencyMatchers.java`** -> AI Confidence: **99.16%**
1753. **`testing/architecture-test/src/test/java/org/gradle/architecture/test/KotlinCompatibilityTest.java`** -> AI Confidence: **99.16%**
1754. **`testing/architecture-test/src/test/java/org/gradle/architecture/test/PlatformBoundariesTest.java`** -> AI Confidence: **99.16%**
1755. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/LogContent.java`** -> AI Confidence: **99.16%**
1756. **`testing/internal-distribution-testing/src/main/groovy/org/gradle/integtests/fixtures/timeout/JavaProcessStackTracesMonitor.java`** -> AI Confidence: **99.16%**
1757. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/Sample.java`** -> AI Confidence: **99.16%**
1758. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/AbstractGradleExecuter.java`** -> AI Confidence: **99.16%**
1759. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/DependencyReplacingSampleModifier.java`** -> AI Confidence: **99.16%**
1760. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/ForkingGradleHandle.java`** -> AI Confidence: **99.16%**
1761. **`testing/internal-integ-testing/src/main/groovy/org/gradle/integtests/fixtures/executer/NoDaemonGradleExecuter.java`** -> AI Confidence: **99.16%**
1762. **`testing/internal-integ-testing/src/main/groovy/org/gradle/test/fixtures/server/http/RestFilter.java`** -> AI Confidence: **99.16%**
1763. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/ResultsStoreHelper.java`** -> AI Confidence: **99.16%**
1764. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/TestDataGenerator.java`** -> AI Confidence: **99.16%**
1765. **`testing/internal-performance-testing/src/main/groovy/org/gradle/performance/results/report/TestPageGenerator.java`** -> AI Confidence: **99.16%**
1766. **`testing/internal-testing/src/main/groovy/org/gradle/util/internal/Resources.java`** -> AI Confidence: **99.16%**
1767. **`.teamcity/src/main/kotlin/common/CommonExtensions.kt`** -> AI Confidence: **99.16%**
1768. **`.teamcity/src/main/kotlin/configurations/DocsTest.kt`** -> AI Confidence: **99.16%**
1769. **`.teamcity/src/main/kotlin/configurations/Gradleception.kt`** -> AI Confidence: **99.16%**
1770. **`.teamcity/src/main/kotlin/configurations/PerformanceTest.kt`** -> AI Confidence: **99.16%**
1771. **`.teamcity/src/main/kotlin/configurations/StageTriggers.kt`** -> AI Confidence: **99.16%**
1772. **`.teamcity/src/main/kotlin/model/PerformanceTestBucketProvider.kt`** -> AI Confidence: **99.16%**
1773. **`.teamcity/src/main/kotlin/projects/StageProject.kt`** -> AI Confidence: **99.16%**
1774. **`.teamcity/src/test/kotlin/CIConfigIntegrationTests.kt`** -> AI Confidence: **99.16%**
1775. **`build-logic-commons/basics/src/main/kotlin/gradlebuild/basics/transforms/Minify.kt`** -> AI Confidence: **99.16%**
1776. **`build-logic-commons/gradle-plugin/src/main/kotlin/gradlebuild/testcleanup/TestFilesCleanupService.kt`** -> AI Confidence: **99.16%**
1777. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/BinaryCompatibilityRepository.kt`** -> AI Confidence: **99.16%**
1778. **`build-logic/binary-compatibility/src/main/kotlin/gradlebuild/binarycompatibility/metadata/KotlinMetadataQueries.kt`** -> AI Confidence: **99.16%**
1779. **`build-logic/build-update-utils/src/main/kotlin/gradlebuild/buildutils/tasks/AbstractCheckOrUpdateContributorsInReleaseNotes.kt`** -> AI Confidence: **99.16%**
1780. **`build-logic/buildquality/src/main/kotlin/gradlebuild/incubation/action/IncubatingApiReportWorkAction.kt`** -> AI Confidence: **99.16%**
1781. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/ide/ExtractAndroidStudioTask.kt`** -> AI Confidence: **99.16%**
1782. **`build-logic/integration-testing/src/main/kotlin/gradlebuild/integrationtests/shared-configuration.kt`** -> AI Confidence: **99.16%**
1783. **`build-logic/jvm/src/main/kotlin/gradlebuild.unittest-and-compile.gradle.kts`** -> AI Confidence: **99.16%**
1784. **`build-logic/jvm/src/main/kotlin/gradlebuild/jvm/JvmCompilation.kt`** -> AI Confidence: **99.16%**
1785. **`build-logic/packaging/src/main/kotlin/gradlebuild/packaging/tasks/GenerateClasspathModuleProperties.kt`** -> AI Confidence: **99.16%**
1786. **`platforms/core-configuration/bean-serialization-services/src/main/kotlin/org/gradle/internal/serialize/beans/services/BeanSchema.kt`** -> AI Confidence: **99.16%**
1787. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/ConfigurationCacheClassLoaderScopeRegistryListener.kt`** -> AI Confidence: **99.16%**
1788. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/CrossProjectModelAccessTrackingParentDynamicObject.kt`** -> AI Confidence: **99.16%**
1789. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/DefaultConfigurationCacheDegradationController.kt`** -> AI Confidence: **99.16%**
1790. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/RelevantProjectsRegistry.kt`** -> AI Confidence: **99.16%**
1791. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/initialization/ConfigurationCacheProblemsListener.kt`** -> AI Confidence: **99.16%**
1792. **`platforms/core-configuration/configuration-cache/src/main/kotlin/org/gradle/internal/cc/impl/models/ProjectStateStore.kt`** -> AI Confidence: **99.16%**
1793. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/JavaRecordCodec.kt`** -> AI Confidence: **99.16%**
1794. **`platforms/core-configuration/core-serialization-codecs/src/main/kotlin/org/gradle/internal/serialize/codecs/core/WorkNodeCodec.kt`** -> AI Confidence: **99.16%**
1795. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/fromLanguageTree/LanguageTreeToDom.kt`** -> AI Confidence: **99.16%**
1796. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/mutation/DocumentTextMutationPlanner.kt`** -> AI Confidence: **99.16%**
1797. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/dom/operations/overlay/DocumentOverlay.kt`** -> AI Confidence: **99.16%**
1798. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/DeclarativeReflectionToObjectConverter.kt`** -> AI Confidence: **99.16%**
1799. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/mappingToJvm/RuntimePropertyResolver.kt`** -> AI Confidence: **99.16%**
1800. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/parsing/FailureCollectorContext.kt`** -> AI Confidence: **99.16%**
1801. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ConfigureLambdaHandler.kt`** -> AI Confidence: **99.16%**
1802. **`platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/SchemaResult.kt`** -> AI Confidence: **99.16%**
1803. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/EvaluationFailureMessageGenerator.kt`** -> AI Confidence: **99.16%**
1804. **`platforms/core-configuration/declarative-dsl-evaluator/src/main/kotlin/org/gradle/internal/declarativedsl/evaluator/main/AnalysisDocumentUtils.kt`** -> AI Confidence: **99.16%**
1805. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/project/TypesafeProjectAccessorsComponent.kt`** -> AI Confidence: **99.16%**
1806. **`platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/settings/SettingsBlocksCheck.kt`** -> AI Confidence: **99.16%**
1807. **`platforms/core-configuration/encryption-services/src/main/kotlin/org/gradle/internal/encryption/impl/DefaultEncryptionService.kt`** -> AI Confidence: **99.16%**
1808. **`platforms/core-configuration/kotlin-dsl-provider-plugins/src/main/kotlin/org/gradle/kotlin/dsl/provider/plugins/KotlinDslDclSchemaCollector.kt`** -> AI Confidence: **99.16%**
1809. **`platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/resolver/SourceDistributionResolverIntegrationTest.kt`** -> AI Confidence: **99.16%**
1810. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/accessors/AccessorFragments.kt`** -> AI Confidence: **99.16%**
1811. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/execution/Combinators.kt`** -> AI Confidence: **99.16%**
1812. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/KotlinBuildScriptModelRequest.kt`** -> AI Confidence: **99.16%**
1813. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/ResolverEventLogger.kt`** -> AI Confidence: **99.16%**
1814. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/resolver/SourceDistributionProvider.kt`** -> AI Confidence: **99.16%**
1815. **`platforms/core-configuration/kotlin-dsl/src/main/kotlin/org/gradle/kotlin/dsl/support/KotlinCompiler.kt`** -> AI Confidence: **99.16%**
1816. **`build-logic/performance-testing/src/main/groovy/gradlebuild/performance/generator/tasks/AbstractProjectGeneratorTask.groovy`** -> AI Confidence: **99.16%**
1817. **`build-logic/performance-testing/src/main/groovy/gradlebuild/performance/generator/tasks/JvmProjectGeneratorTask.groovy`** -> AI Confidence: **99.16%**
1818. **`build-logic/performance-testing/src/main/groovy/gradlebuild/performance/tasks/PerformanceTest.groovy`** -> AI Confidence: **99.16%**
1819. **`platforms/core-configuration/model-core/src/test/groovy/org/gradle/internal/snapshot/impl/IsolatableSerializerRegistryTest.groovy`** -> AI Confidence: **99.16%**
1820. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParallelBuildOperationsIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1821. **`platforms/core-execution/workers/src/integTest/groovy/org/gradle/workers/internal/WorkerExecutorParallelIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1822. **`platforms/core-runtime/build-configuration/src/integTest/groovy/org/gradle/interal/buildconfiguration/tasks/UpdateDaemonJvmIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1823. **`platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/AbstractDaemonLifecycleSpec.groovy`** -> AI Confidence: **99.16%**
1824. **`platforms/core-runtime/messaging/src/integTest/groovy/org/gradle/internal/remote/UnicastMessagingIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1825. **`platforms/enterprise/enterprise/src/integTest/groovy/org/gradle/internal/enterprise/core/BuildScanAutoApplyIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1826. **`platforms/extensibility/plugin-use/src/integTest/groovy/org/gradle/plugin/repository/ResolvingFromMultipleCustomPluginRepositorySpec.groovy`** -> AI Confidence: **99.16%**
1827. **`platforms/ide/problems-rendering/src/test/groovy/org/gradle/problems/internal/rendering/SimpleProblemWriterTest.groovy`** -> AI Confidence: **99.16%**
1828. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/DefaultTestEventSpec.groovy`** -> AI Confidence: **99.16%**
1829. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/TestLauncherSpec.groovy`** -> AI Confidence: **99.16%**
1830. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r40/ResolveArtifactsProgressCrossVersionSpec.groovy`** -> AI Confidence: **99.16%**
1831. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r51/TaskOriginCrossVersionSpec.groovy`** -> AI Confidence: **99.16%**
1832. **`platforms/ide/tooling-api/src/crossVersionTest/groovy/org/gradle/integtests/tooling/r85/TestLauncherDebugCrossVersionSpec.groovy`** -> AI Confidence: **99.16%**
1833. **`platforms/ide/tooling-api/src/integTest/groovy/org/gradle/integtests/tooling/ToolingApiClientJdkCompatibilityTest.groovy`** -> AI Confidence: **99.16%**
1834. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/ContinuousBuildToolingApiSpecification.groovy`** -> AI Confidence: **99.16%**
1835. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/ToolingApiDistributionResolver.groovy`** -> AI Confidence: **99.16%**
1836. **`platforms/ide/tooling-api/src/testFixtures/groovy/org/gradle/integtests/tooling/fixture/ToolingApiSpecification.groovy`** -> AI Confidence: **99.16%**
1837. **`platforms/jvm/code-quality/src/integTest/groovy/org/gradle/api/plugins/quality/AntWorkerMemoryLeakIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1838. **`platforms/jvm/language-java/src/testFixtures/groovy/org/gradle/language/fixtures/AnnotationProcessorFixture.groovy`** -> AI Confidence: **99.16%**
1839. **`platforms/jvm/language-jvm/src/integTest/groovy/org/gradle/api/tasks/bundling/JarEncodingIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1840. **`platforms/jvm/testing-jvm/src/integTest/groovy/org/gradle/testing/TestTaskCustomExecuterIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1841. **`platforms/jvm/toolchains-jvm-shared/src/testFixtures/groovy/org/gradle/jvm/toolchain/JdkRepository.groovy`** -> AI Confidence: **99.16%**
1842. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/AbstractInitIntegrationSpec.groovy`** -> AI Confidence: **99.16%**
1843. **`platforms/software/build-init/src/integTest/groovy/org/gradle/buildinit/plugins/BuildInitPluginIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1844. **`platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/AbstractDependencyVerificationIntegTest.groovy`** -> AI Confidence: **99.16%**
1845. **`platforms/software/dependency-management/src/test/groovy/org/gradle/api/internal/catalog/LibrariesSourceGeneratorTest.groovy`** -> AI Confidence: **99.16%**
1846. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/external/model/AbstractDependencyMetadataRulesTest.groovy`** -> AI Confidence: **99.16%**
1847. **`platforms/software/dependency-management/src/test/groovy/org/gradle/internal/component/model/GraphVariantSelectorTest.groovy`** -> AI Confidence: **99.16%**
1848. **`platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/api/internal/artifacts/verification/DependencyVerificationFixture.groovy`** -> AI Confidence: **99.16%**
1849. **`platforms/software/dependency-management/src/testFixtures/groovy/org/gradle/containers/GradleInContainer.groovy`** -> AI Confidence: **99.16%**
1850. **`platforms/software/ivy/src/integTest/groovy/org/gradle/api/publish/ivy/IvyPublishHttpIntegTest.groovy`** -> AI Confidence: **99.16%**
1851. **`platforms/software/maven/src/integTest/groovy/org/gradle/api/publish/maven/AbstractMavenPublishJavaIntegTest.groovy`** -> AI Confidence: **99.16%**
1852. **`platforms/software/resources-http/src/test/groovy/org/gradle/internal/resource/transport/http/JavaSystemPropertiesHttpTimeoutSettingsTest.groovy`** -> AI Confidence: **99.16%**
1853. **`platforms/software/testing-base/src/integTest/groovy/org/gradle/testing/TestEventReporterIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1854. **`platforms/software/testing-base/src/testFixtures/groovy/org/gradle/api/internal/tasks/testing/report/generic/GenericHtmlTestExecutionResult.groovy`** -> AI Confidence: **99.16%**
1855. **`subprojects/core/src/integTest/groovy/org/gradle/api/internal/tasks/TaskCacheabilityReasonIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1856. **`subprojects/core/src/integTest/groovy/org/gradle/api/tasks/TaskTimeoutIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1857. **`subprojects/core/src/integTest/groovy/org/gradle/configuration/ExecuteUserLifecycleListenerBuildOperationIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1858. **`subprojects/core/src/integTest/groovy/org/gradle/execution/taskgraph/ParallelTaskExecutionIntegrationTest.groovy`** -> AI Confidence: **99.16%**
1859. **`subprojects/core/src/test/groovy/org/gradle/api/internal/artifacts/JavaEcosystemSupportTest.groovy`** -> AI Confidence: **99.16%**
1860. **`subprojects/core/src/test/groovy/org/gradle/api/internal/attributes/BaseAttributeContainerTest.groovy`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `platforms/software/security/src/test/groovy/org/gradle/security/internal/SecuritySupportSpec.groovy` -> **99.9399%** Exposure
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/S3ClientIntegrationTest.groovy` -> **99.6391%** Exposure
- `platforms/core-execution/build-cache-http/src/integTest/groovy/org/gradle/caching/http/internal/HttpBuildCacheServiceIntegrationTest.groovy` -> **97.2852%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `126458` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `subprojects/core/src/testFixtures/groovy/org/gradle/util/internal/MockExecutor.java` (JAVA) -> Cumulative Risk: **768.13**
- **Archetype:** `file_cluster_4` (Distance: 11.592 IQR)
- **Magnitude:** 176.66 | **LOC:** 142 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `invokeAll` (Impact: 6.2), `invokeAny` (Impact: 6.2), `submit` (Impact: 5.1)

### 2. `platforms/software/ant/src/main/java/org/gradle/api/internal/project/ant/BasicAntBuilder.java` (JAVA) -> Cumulative Risk: **765.34**
- **Archetype:** `file_cluster_0` (Distance: 11.887 IQR)
- **Magnitude:** 109.36 | **LOC:** 140 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9904%), Tech Debt (99.926%)
- **Heaviest Functions:** `doInvokeMethod` (Impact: 6.7), `importBuild` (Impact: 6.2), `BasicAntBuilder` (Impact: 6.1)

### 3. `platforms/software/resources/src/main/java/org/gradle/internal/resource/transfer/DefaultExternalResourceConnector.java` (JAVA) -> Cumulative Risk: **696.66**
- **Archetype:** `file_cluster_4` (Distance: 10.415 IQR)
- **Magnitude:** 224.78 | **LOC:** 267 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `create` (Impact: 16.6), `statsFor` (Impact: 14.4), `toString` (Impact: 13.9)

### 4. `platforms/core-runtime/base-services/src/main/java/org/gradle/initialization/DefaultBuildCancellationToken.java` (JAVA) -> Cumulative Risk: **695.24**
- **Archetype:** `file_cluster_4` (Distance: 10.822 IQR)
- **Magnitude:** 96.18 | **LOC:** 85 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `cancel` (Impact: 16.9), `addCallback` (Impact: 8.0), `removeCallback` (Impact: 2.7)

### 5. `platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/DefaultExecSpec.java` (JAVA) -> Cumulative Risk: **688.78**
- **Archetype:** `file_cluster_0` (Distance: 11.731 IQR)
- **Magnitude:** 157.42 | **LOC:** 174 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `copyBaseExecSpecTo` (Impact: 7.5), `commandLine` (Impact: 5.1), `setCommandLine` (Impact: 5.1)

### 6. `subprojects/core/src/main/java/org/gradle/api/internal/tasks/TaskStatistics.java` (JAVA) -> Cumulative Risk: **684.06**
- **Archetype:** `file_cluster_4` (Distance: 10.245 IQR)
- **Magnitude:** 143.16 | **LOC:** 146 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Tech Debt (87.267%), Documentation (85.9788%)
- **Heaviest Functions:** `lazyTaskRealized` (Impact: 14.3), `eagerTask` (Impact: 11.9), `TaskStatistics` (Impact: 11.1)

### 7. `platforms/core-configuration/file-collections/src/integTest/groovy/org/gradle/api/file/FilePropertyLifecycleIntegrationTest.groovy` (GROOVY) -> Cumulative Risk: **674.03**
- **Archetype:** `file_cluster_4` (Distance: 12.101 IQR)
- **Magnitude:** 703.98 | **LOC:** 747 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.7637%)
- **Heaviest Functions:** `outputContains` (Impact: 36.2), `def` (Impact: 34.6), `def` (Impact: 34.5)

### 8. `platforms/core-runtime/build-operations/src/main/java/org/gradle/internal/operations/DefaultBuildOperationListenerManager.java` (JAVA) -> Cumulative Risk: **673.81**
- **Archetype:** `file_cluster_4` (Distance: 10.545 IQR)
- **Magnitude:** 84.38 | **LOC:** 128 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `started` (Impact: 5.6), `progress` (Impact: 5.6), `finished` (Impact: 5.5)

### 9. `platforms/core-runtime/concurrent/src/main/java/org/gradle/internal/concurrent/AbstractManagedExecutor.java` (JAVA) -> Cumulative Risk: **672.62**
- **Archetype:** `file_cluster_0` (Distance: 11.501 IQR)
- **Magnitude:** 90.06 | **LOC:** 106 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (93.4637%), State Flux (92.2141%)
- **Heaviest Functions:** `stop` (Impact: 11.2), `trackedCommand` (Impact: 8.6), `trackedCommand` (Impact: 8.0)

### 10. `platforms/core-runtime/process-services/src/main/java/org/gradle/process/internal/DefaultExecHandleBuilder.java` (JAVA) -> Cumulative Risk: **662.19**
- **Archetype:** `file_cluster_0` (Distance: 11.059 IQR)
- **Magnitude:** 183.28 | **LOC:** 234 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9554%)
- **Heaviest Functions:** `commandLine` (Impact: 5.1), `setCommandLine` (Impact: 5.1), `args` (Impact: 5.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `platforms/documentation/docs/src/snippets/signing/configurations/common/secKeyRingFile.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `platforms/software/signing/src/integTest/resources/org/gradle/plugins/signing/keys/subkey/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `platforms/software/signing/src/testFixtures/resources/keys/gradle/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `platforms/software/signing/src/testFixtures/resources/keys/invalid-key-ring/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `platforms/software/signing/src/testFixtures/resources/keys/rfc9580v6sample/secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `testing/internal-integ-testing/src/main/resources/sshd-config/test-dsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.455 IQR)
- **Top Global Matches:** file_cluster_8: 10.455, file_cluster_7: 11.093, file_cluster_1: 11.293
- **Magnitude:** 2350.06 | **LOC:** 1995 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.016%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 592.5)
  * `uncheckedModule` (Impact: 396.5)
  * `def` (Impact: 69.2)
  * `def` (Impact: 66.0)
  * `def` (Impact: 43.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 114`, `args: 473`, `func_start: 469`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 6`, `duplicate_logic: 115`, `orphaned_logic: 1`
* *Architecture:* `io: 90`, `api: 1`, `import: 17`
* *Defense:* `test: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` org.gradle.security.fixtures.SimpleKeyRing, org.gradle.api.attributes.Usage, org.gradle.security.fixtures.SigningFixtures, org.gradle.security.fixtures.KeyServer, org.gradle.test.fixtures.server.http.MavenHttpModule, org.gradle.api.internal.artifacts.verification.DependencyVerificationFixture.getChecksum, spock.lang.Issue, org.gradle.security.fixtures.SigningFixtures.getValidPublicKeyLongIdHexString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/software/build-init/src/main/java/org/gradle/buildinit/plugins/internal/BuildScriptBuilder.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.216 IQR)
- **Top Global Matches:** file_cluster_0: 11.216, file_cluster_8: 11.45, file_cluster_13: 11.495
- **Magnitude:** 1681.44 | **LOC:** 2469 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.5983%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `configureConventionPlugin` (Impact: 67.2)
  * `printStatement` (Impact: 40.0)
  * `forInsecureProtocolOption` (Impact: 26.7)
  * `writeCodeTo` (Impact: 25.7)
  * `writeBodyTo` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 576`, `args: 309`, `func_start: 340`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 122`, `planned_debt: 4`, `duplicate_logic: 187`
* *Architecture:* `io: 61`, `api: 233`, `import: 43`
* *Defense:* `safety: 19`, `doc: 62`, `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` org.gradle.jvm.toolchain.JavaLanguageVersion, java.util.Map, java.util.LinkedHashMap, java.util.List, org.gradle.api.Action, com.google.common.base.Splitter, org.gradle.internal.deprecation.Documentation, org.gradle.buildinit.plugins.internal.modifiers.BuildInitDsl...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `subprojects/core/src/test/groovy/org/gradle/execution/plan/DefaultExecutionPlanParallelTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.475 IQR)
- **Top Global Matches:** file_cluster_8: 11.475, file_cluster_4: 11.649, file_cluster_0: 12.023
- **Magnitude:** 1406.78 | **LOC:** 2486 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (87.7206%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestPriorityNode` (Impact: 23.0)
  * `def` (Impact: 18.0)
  * `def` (Impact: 16.8)
  * `def` (Impact: 16.7)
  * `def` (Impact: 15.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 368`, `args: 618`, `func_start: 606`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 24`, `planned_debt: 11`, `duplicate_logic: 111`, `orphaned_logic: 12`
* *Architecture:* `io: 119`, `concurrency: 499`, `import: 29`
* *Defense:* `safety: 66`, `doc: 1`, `test: 582`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` org.gradle.api.DefaultTask, org.gradle.composite.internal.BuildTreeWorkGraphController, org.gradle.test.precondition.Requires, org.gradle.test.preconditions.UnitTestPreconditions, org.gradle.util.Path, org.gradle.api.internal.project.taskfactory.TestTaskIdentities, org.gradle.api.tasks.LocalState, org.gradle.api.tasks.InputFile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AbstractClassGenerator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.557 IQR)
- **Top Global Matches:** file_cluster_13: 11.557, file_cluster_16: 11.645, file_cluster_8: 11.69
- **Magnitude:** 1385.72 | **LOC:** 1598 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9418%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `unclaimed` (Impact: 88.7)
    * *Intent:* /** * Validate the property is declared properly.
  * `inspectType` (Impact: 76.9)
  * `generateUnderLock` (Impact: 76.0)
  * `AbstractClassGenerator` (Impact: 44.0)
    * *Intent:* /**
  * `validateMethod` (Impact: 41.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 424`, `args: 176`, `func_start: 185`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 101`, `planned_debt: 2`, `duplicate_logic: 63`, `orphaned_logic: 7`
* *Architecture:* `api: 74`, `import: 69`
* *Defense:* `safety: 4`, `doc: 17`, `test: 5`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` com.google.common.reflect.TypeToken, org.gradle.cache.Cache, org.gradle.internal.reflect.ClassDetails, com.google.common.collect.ImmutableCollection, org.gradle.api.provider.SupportsConvention, org.gradle.api.Describable, com.google.common.collect.ImmutableMultimap, org.gradle.internal.extensibility.NoConventionMapping...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `subprojects/core-api/src/main/java/org/gradle/api/artifacts/dsl/DependencyCollector.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.309 IQR)
- **Top Global Matches:** file_cluster_13: 15.309, file_cluster_16: 15.391, file_cluster_0: 15.643
- **Magnitude:** 1352.39 | **LOC:** 284 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.4438%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 60`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `doc: 83`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` org.gradle.api.provider.ProviderConvertible, java.util.Set, org.gradle.api.NonExtensible, org.gradle.api.artifacts.ExternalModuleDependency, org.gradle.api.Incubating, org.gradle.api.artifacts.DependencyConstraint, org.gradle.api.file.FileCollection, org.gradle.api.artifacts.FileCollectionDependency...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `platforms/core-configuration/model-core/src/testFixtures/groovy/org/gradle/api/internal/provider/PropertySpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.53 IQR)
- **Top Global Matches:** file_cluster_8: 9.53, file_cluster_7: 10.312, file_cluster_1: 10.491
- **Magnitude:** 1105.64 | **LOC:** 3128 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3863%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 19.8)
  * `def` (Impact: 19.1)
  * `def` (Impact: 19.1)
  * `def` (Impact: 17.4)
  * `def` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 613`, `args: 200`, `func_start: 200`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 150`, `high_risk_execution: 3`, `state_mutation: 2`, `planned_debt: 7`, `duplicate_logic: 137`
* *Architecture:* `io: 6`, `api: 7`, `concurrency: 54`, `import: 16`
* *Defense:* `safety: 5`, `doc: 5`, `test: 576`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` org.gradle.api.internal.provider.CircularEvaluationSpec.ProviderConsumer.GET_PRODUCER, org.gradle.internal.DisplayName, org.gradle.internal.evaluation.EvaluationContext, java.util.function.Consumer, org.gradle.api.specs.Spec, org.gradle.internal.Describables, org.gradle.api.Action, org.gradle.internal.state.ModelObject...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `subprojects/core/src/test/groovy/org/gradle/api/internal/tasks/DefaultTaskContainerTest.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.23 IQR)
- **Top Global Matches:** file_cluster_8: 10.23, file_cluster_4: 10.469, file_cluster_7: 10.978
- **Magnitude:** 1073.14 | **LOC:** 1683 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `void` (Impact: 15.0)
  * `void` (Impact: 15.0)
  * `void` (Impact: 13.6)
  * `void` (Impact: 12.4)
  * `void` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 257`, `args: 133`, `func_start: 128`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 33`, `state_mutation: 8`, `planned_debt: 2`, `duplicate_logic: 87`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `concurrency: 580`, `import: 33`
* *Defense:* `test: 282`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` org.gradle.internal.reflect.DirectInstantiator, org.gradle.api.DefaultTask, org.gradle.api.internal.project.taskfactory.TaskFactory, org.gradle.api.Action, org.gradle.internal.code.UserCodeSource, org.gradle.api.internal.project.taskfactory.ITaskFactory, org.gradle.util.Path, org.gradle.api.internal.project.CrossProjectModelAccess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/ivyresolve/strategy/VersionParser.java` (JAVA) | Magnitude: 111.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 32, branch: 19, api: 19
- `subprojects/core/src/main/java/org/gradle/internal/classpath/PerThreadInstrumentedGroovyCallsTracker.java` (JAVA) | Magnitude: 17.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, api: 6, decorators: 6
- `platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractGroovyCompilerIntegrationSpec/canUseAstTransformWithAsm/src/test/groovy/GroovyMagicFieldTransformTest.groovy` (GROOVY) | Magnitude: 4.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 2, args: 2, func_start: 2
- `platforms/jvm/language-groovy/src/testFixtures/resources/org/gradle/groovy/compile/AbstractGroovyCompilerIntegrationSpec/canUseAstTransformWrittenInGroovy/src/test/groovy/GroovyMagicFieldTransformTest.groovy` (GROOVY) | Magnitude: 4.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 2, args: 2, func_start: 2
- `platforms/software/testing-base/src/main/java/org/gradle/api/internal/tasks/testing/filter/DefaultTestFilter.java` (JAVA) | Magnitude: 120.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 34, state_mutation: 31, api: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `platforms/software/resources-s3/src/integTest/groovy/org/gradle/integtests/resource/s3/fixtures/stub/HttpStub.groovy` (GROOVY) | Magnitude: 0.03 | Delta: **0.244 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 20, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `subprojects/core/src/main/java/org/gradle/api/internal/project/CrossProjectConfigurator.java` (JAVA) | Magnitude: 179.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, branch: 6, generics: 6, args: 5
- `platforms/core-execution/persistent-cache/src/main/java/org/gradle/cache/internal/CrossProcessSynchronizingIndexedCache.java` (JAVA) | Magnitude: 51.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 17, concurrency: 13, args: 10
- `platforms/core-execution/scoped-persistent-cache/src/main/java/org/gradle/cache/internal/scopes/AbstractScopedCacheBuilderFactory.java` (JAVA) | Magnitude: 29.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 19, api: 9, args: 8
- `platforms/core-runtime/daemon-protocol/src/main/java/org/gradle/launcher/daemon/registry/DaemonDir.java` (JAVA) | Magnitude: 17.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, io: 10, api: 8
- `platforms/core-runtime/logging/src/main/java/org/gradle/internal/logging/DefaultLoggingConfiguration.java` (JAVA) | Magnitude: 71.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, api: 28, structural_boundaries: 26, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/tasks/NodeExecutionContext.java` (JAVA) | Magnitude: 6.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 2, func_start: 2
- `platforms/core-configuration/project-features/src/main/java/org/gradle/features/internal/binding/ProjectFeatureApplicator.java` (JAVA) | Magnitude: 4.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, doc: 12, indent_spaces: 7, func_start: 5
- `platforms/ide/ide/src/main/java/org/gradle/plugins/ide/internal/generator/generator/Generator.java` (JAVA) | Magnitude: 27.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, args: 4, func_start: 4, indent_spaces: 4
- `platforms/software/dependency-management/src/main/java/org/gradle/api/internal/artifacts/ivyservice/modulecache/dynamicversions/ModuleVersionsCache.java` (JAVA) | Magnitude: 6.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, args: 4, func_start: 4
- `subprojects/core-api/src/main/java/org/gradle/api/artifacts/CapabilitiesResolution.java` (JAVA) | Magnitude: 119.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 14, structural_boundaries: 10, branch: 4, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `platforms/native/language-native/src/test/groovy/org/gradle/language/cpp/plugins/CppLibraryPluginTest.groovy` (GROOVY) | Magnitude: 112.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 249, structural_boundaries: 69, safety_bypasses: 32, safety: 30
- `build-logic/binary-compatibility/src/main/groovy/gradlebuild/binarycompatibility/AcceptedViolationsProvider.groovy` (GROOVY) | Magnitude: 9.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, state_mutation: 4, args: 2
- `platforms/ide/ide/src/testFixtures/groovy/org/gradle/plugins/ide/eclipse/EclipseWtpComponentFixture.groovy` (GROOVY) | Magnitude: 31.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 20, args: 16, func_start: 14
- `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/ClassMembersForSchema.kt` (KOTLIN) | Magnitude: 286.64 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 238, branch: 81, structural_boundaries: 79, immutability_locks: 58
- `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/SupertypeDiscovery.kt` (KOTLIN) | Magnitude: 14.74 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, safety: 6, structural_boundaries: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `platforms/software/build-init/src/main/resources/org/gradle/buildinit/tasks/templates/scalaapplication/multi/list/LinkedList.scala.template` (SCALA) | Magnitude: 110.32 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 63, indent_spaces: 63, branch: 14, ui_framework: 10
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/model/ProjectIdentifier.java` (JAVA) | Magnitude: 20.92 | Delta: **0.256 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 3, args: 2, func_start: 2
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/model/Model.java` (JAVA) | Magnitude: 12.04 | Delta: **0.55 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/continuous/ChangesDuringBuildContinuousIntegrationTest.groovy` (GROOVY) | Magnitude: 137.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 186, concurrency: 42, io: 27, test: 24
- `platforms/core-execution/snapshots/src/main/java/org/gradle/internal/snapshot/impl/FileSystemSnapshotFilter.java` (JAVA) | Magnitude: 84.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 34, concurrency: 30, encapsulation: 20
- `platforms/core-runtime/launcher/src/integTest/groovy/org/gradle/launcher/daemon/DaemonToolchainInvalidCriteriaIntegrationTest.groovy` (GROOVY) | Magnitude: 41.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 18, test: 17, func_start: 12
- `platforms/software/plugins-distribution/src/integTest/groovy/org/gradle/api/distribution/plugins/DistributionPluginTest.groovy` (GROOVY) | Magnitude: 60.98 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 30, test: 18, concurrency: 15
- `platforms/jvm/language-java/src/integTest/groovy/org/gradle/api/tasks/compile/JavaCompileRelocationIntegrationTest.groovy` (GROOVY) | Magnitude: 24.28 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, io: 9, args: 6

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
- `platforms/core-configuration/file-collections/src/main/java/org/gradle/api/internal/file/AbstractFileResolver.java` (JAVA) | Magnitude: 81.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 40, io: 20, branch: 19
- `platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/model/annotations/InputFilePropertyAnnotationHandler.java` (JAVA) | Magnitude: 4.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, import: 7, encapsulation: 7, indent_spaces: 7
- `platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/steps/StoreExecutionStateStep.java` (JAVA) | Magnitude: 50.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 41, encapsulation: 22, args: 17
- `platforms/core-execution/snapshots/src/main/java/org/gradle/internal/fingerprint/hashing/RegularFileSnapshotContext.java` (JAVA) | Magnitude: 21.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, import: 2
- `platforms/core-runtime/process-memory-services/src/main/java/org/gradle/process/internal/health/memory/MemoryManager.java` (JAVA) | Magnitude: 38.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, args: 7, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `platforms/jvm/javadoc/src/integTest/resources/org/gradle/api/tasks/javadoc/JavadocIntegrationTest/handlesTagsAndTaglets/src/main/java/Person.java` (JAVA) | Magnitude: 12.04 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, class_start: 1, api: 1
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest.h` (CPP) | Magnitude: 297.22 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 296, api: 254, immutability_locks: 170, structural_boundaries: 89
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest-test-part.h` (CPP) | Magnitude: 43.3 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, api: 26, immutability_locks: 21, structural_boundaries: 18
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/gtest-typed-test.h` (CPP) | Magnitude: 26.38 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, macros: 18, api: 17, structural_boundaries: 14
- `testing/performance/src/templates/native-dependents-resources/googleTest/libs/googleTest/1.7.0/include/gtest/internal/gtest-linked_ptr.h` (CPP) | Magnitude: 104.84 | Delta: **0.17 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 42, args: 30, branch: 20

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `platforms/core-runtime/wrapper-main/src/integTest/groovy/org/gradle/integtests/WrapperGenerationIntegrationTest.groovy` -> Churn: **70.87%** | Cog Load: 11.5501% | Debt: 100.0%
- `platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/DependencyCollectorFunctionExtractorAndRuntimeResolver.kt` -> Churn: **61.3%** | Cog Load: 45.8725% | Debt: 95.1298%
- `platforms/core-configuration/kotlin-dsl/src/integTest/kotlin/org/gradle/kotlin/dsl/resolver/SourceDistributionResolverIntegrationTest.kt` -> Churn: **60.08%** | Cog Load: 29.7152% | Debt: 90.7814%
- `platforms/core-configuration/declarative-dsl-core/src/main/kotlin/org/gradle/internal/declarativedsl/schemaBuilder/PropertyExtractor.kt` -> Churn: **58.86%** | Cog Load: 21.8804% | Debt: 99.9538%
- `platforms/core-configuration/declarative-dsl-provider/src/main/kotlin/org/gradle/internal/declarativedsl/dependencycollectors/dependencyConfigurationSchema.kt` -> Churn: **58.86%** | Cog Load: 12.9114% | Debt: 94.9539%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `platforms/software/dependency-management/src/integTest/groovy/org/gradle/integtests/resolve/verification/DependencyVerificationSignatureCheckIntegTest.groovy` -> **József Bartók** (100.0% isolated ownership) | Magnitude: 2350.06
- `subprojects/core/src/main/java/org/gradle/api/internal/project/DefaultProject.java` -> **Gary Hale** (100.0% isolated ownership) | Magnitude: 987.9
- `platforms/core-configuration/model-core/src/main/java/org/gradle/internal/instantiation/generator/AsmBackedClassGenerator.java` -> **Sterling Greene** (100.0% isolated ownership) | Magnitude: 946.28
- `platforms/ide/tooling-api/src/main/java/org/gradle/tooling/internal/adapter/ProtocolToModelAdapter.java` -> **Justin Van Dort** (100.0% isolated ownership) | Magnitude: 785.72
- `subprojects/core/src/integTest/groovy/org/gradle/api/services/BuildServiceIntegrationTest.groovy` -> **Tom Tresansky** (100.0% isolated ownership) | Magnitude: 729.68

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

- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/api/UncheckedIOException.java` -> **Severity: 467.972** (Blast Radius: 6.137 * Doc Risk: 76.2542%)
- `platforms/core-configuration/model-core/src/main/java/org/gradle/api/internal/provider/Collectors.java` -> **Severity: 413.992** (Blast Radius: 4.155 * Doc Risk: 99.6371%)
- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/internal/os/OperatingSystem.java` -> **Severity: 344.626** (Blast Radius: 3.458 * Doc Risk: 99.6605%)
- `platforms/core-execution/hashing/src/main/java/org/gradle/internal/hash/HashCode.java` -> **Severity: 296.629** (Blast Radius: 4.164 * Doc Risk: 71.2365%)
- `platforms/core-runtime/stdlib-java-extensions/src/main/java/org/gradle/api/Incubating.java` -> **Severity: 275.347** (Blast Radius: 23.099 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
