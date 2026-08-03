# ARCHITECTURAL_BRIEF: spock
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/spock` |
| **Timestamp** | `2026-08-03T21:37:07.877586+00:00` |
| **Scan Duration** | `3.75s` |
| **Git Branch** | `master` |
| **Git Commit** | `b71e3d7590dae28d608aa92f90b45bef33aaeda8` |
| **Git Remote** | `https://github.com/spockframework/spock` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1193 malicious artifacts.

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
| Total Artifacts | 1420 |
| Analyzed Artifacts (Scanned) | 1251 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 169 |
| Total LOC | 73747 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.1% |
| Dominant Lang | GROOVY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5548 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1996 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6675 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 85 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 665 | 28590 | 53.2% |
| GROOVY | 525 | 45063 | 42.0% |
| PLAINTEXT | 46 | 1 | 3.7% |
| XML | 9 | 0 | 0.7% |
| BATCH | 2 | 75 | 0.2% |
| MARKDOWN | 1 | 0 | 0.1% |
| SHELL | 1 | 4 | 0.1% |
| JSON | 1 | 4 | 0.1% |
| YAML | 1 | 10 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.216`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 710 | 56.8% |
| file_cluster_13 | 326 | 26.1% |
| file_cluster_0 | 98 | 7.8% |
| file_cluster_16 | 51 | 4.1% |
| file_cluster_4 | 13 | 1.0% |
| file_cluster_17 | 3 | 0.2% |
| Unknown | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 169*

**Composition by Extension & Reason:**
- `.groovy`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 16 exceeds 500 chars), 3x Excluded (Saturation: Line 7 exceeds 500 chars)
- `no_extension`: 13x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 249 LOC)
- `.adoc`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.java`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.imockmaker`: 2x Unsupported Format (.imockmaker)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lines`: 1x Excluded (Unsupported Extension: '.lines')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.2 | 10.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 26.8 | 3.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 16.2 | 3.8 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 43.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.0 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.0 | 4.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java` (Hits: 39)
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/TempDirExtensionSpec.groovy` (Hits: 38)
- `spock-core/src/main/java/spock/util/io/FileSystemFixture.java` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Specification.java** (`spock-core/src/main/java/spock/lang/Specification.java`) — 249 inbound connections
2. **EmbeddedSpecification.groovy** (`spock-specs/src/test/groovy/org/spockframework/EmbeddedSpecification.groovy`) — 97 inbound connections
3. **Issue.java** (`spock-core/src/main/java/spock/lang/Issue.java`) — 72 inbound connections
4. **GroovyRuntimeUtil.java** (`spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java`) — 53 inbound connections
5. **Nullable.java** (`spock-core/src/main/java/org/spockframework/util/Nullable.java`) — 49 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ByteBuddyMockFactory.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/ByteBuddyMockFactory.java`) — 32 outbound dependencies
2. **MockMakerRegistry.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/MockMakerRegistry.java`) — 28 outbound dependencies
3. **MockitoMockMakerImpl.java** (`spock-core/src/main/java/org/spockframework/mock/runtime/mockito/MockitoMockMakerImpl.java`) — 26 outbound dependencies
4. **SpockMockPostprocessor.java** (`spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java`) — 26 outbound dependencies
5. **ConditionRewriter.java** (`spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy`) -> Impact: **1491.3** | LOC: 1351
- `register` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **669.3** | LOC: 395
  * *Intent:* /** * This compound extension consists of an include processor, a tree processor, and a post processor. * It automatically links listing and literal b...
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy`) -> Impact: **516.8** | LOC: 176
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooFewInvocations.groovy`) -> Impact: **398.8** | LOC: 39
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy`) -> Impact: **376.6** | LOC: 124
- `matchesSnapshot` (@ `spock-core/src/main/java/spock/lang/Snapshotter.java`) -> Impact: **359.1** | LOC: 205
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy`) -> Impact: **310.9** | LOC: 79
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy`) -> Impact: **258.2** | LOC: 84
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy`) -> Impact: **225.9** | LOC: 74
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy`) -> Impact: **225.9** | LOC: 73

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `defineErrorCollector` (@ `spock-core/src/main/java/org/spockframework/compiler/condition/VerifyAllMethodRewriter.java`) -> **O(2^N) [Recursive]**
- `createDetached` (@ `spock-core/src/main/java/org/spockframework/mock/runtime/CompositeMockFactory.java`) -> **O(2^N) [Recursive]**
- `DataProviderMultiplier` (@ `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * During the first set of multiplier values, i.e. the first value of the {@link #multiplierIterators}, * this contains the iterators that were bui...
- `createStaticMock` (@ `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java`) -> **O(2^N) [Recursive]**
- `evaluateCondition` (@ `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ConditionalExtension.java`) -> **O(2^N) [Recursive]**
- `mockito` (@ `spock-core/src/main/java/spock/mock/MockMakers.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Provides constants and factory methods for known built-in {@link IMockMaker} implementations. * * <p>You can select the mock maker during mock c...
- `getExistingBeans` (@ `spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java`) -> **O(2^N) [Recursive]**
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ExceptionsInConditions.groovy`) -> **O(2^N) [Recursive]**
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ExceptionsInConditions.groovy`) -> **O(2^N) [Recursive]**
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ExceptionsInConditions.groovy`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `verifyLinksAndAnchors` (@ `build-logic/base/src/main/groovy/org/spockframework/gradle/AsciiDocLinkVerifier.groovy`) -> DB Complexity: **42**
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy`) -> DB Complexity: **36**
- `maven` (@ `gradle/publishMaven.gradle`) -> DB Complexity: **33**
- `matchesSnapshot` (@ `spock-core/src/main/java/spock/lang/Snapshotter.java`) -> DB Complexity: **32**
- `register` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> DB Complexity: **27**
  * *Intent:* /** * This compound extension consists of an include processor, a tree processor, and a post processor. * It automatically links listing and literal b...
- `visitCleanupBlock` (@ `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java`) -> DB Complexity: **20**
- `verifyAnchorlessCrossDocumentLinks` (@ `build-logic/base/src/main/groovy/org/spockframework/gradle/AsciiDocLinkVerifier.groovy`) -> DB Complexity: **18**
  * *Intent:* /* * Copyright 2025 the original author or authors. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file ex...
- `generateTempDir` (@ `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java`) -> DB Complexity: **15**
- `def` (@ `spock-specs/src/test/groovy/org/spockframework/util/ReflectionUtilSpec.groovy`) -> DB Complexity: **15**
- `createFeature` (@ `spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `spock-specs/src/test/groovy/org/spockframework/smoke/mock` | 62 | 11412.04 | 29.67% | 0.0% |
| `spock-core/src/main/java/org/spockframework/runtime` | 82 | 7506.74 | 19.32% | 50.57% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/extension` | 37 | 6085.26 | 28.36% | 0.0% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization` | 10 | 5053.52 | 39.2% | 0.0% |
| `config` | 1 | 5000.0 | 0.0% | 0.0% |
| `spock-core/src/main/java/org/spockframework/compiler` | 26 | 3609.86 | 16.18% | 71.38% |
| `spock-specs/src/test/groovy/org/spockframework/smoke` | 45 | 3335.94 | 20.16% | 0.0% |
| `spock-core/src/main/java/org/spockframework/util` | 50 | 3333.04 | 11.92% | 41.01% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/condition` | 28 | 3197.88 | 19.5% | 0.0% |
| `spock-core/src/main/java/org/spockframework/mock/runtime` | 44 | 2776.76 | 17.12% | 51.68% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `allVariants` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/builder/PojoBuilder.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/buildsupport/EmptyAnnotationVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/buildsupport/SpecClassFileVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/AbstractSpecVisitor.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/AbstractMultiset.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/CollectionUtil.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/Filter.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/HashMultiset.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` -> **3** Orphaned Functions | **81** Duplicates
- `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` -> **0** Orphaned Functions | **60** Duplicates
- `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` -> **46** Orphaned Functions | **10** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` -> **1** Orphaned Functions | **55** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` -> **1** Orphaned Functions | **50** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy`** -> AI Confidence: **99.48%**
2. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy`** -> AI Confidence: **99.39%**
3. **`build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`** -> AI Confidence: **99.31%**
4. **`spock-core/src/main/java/org/spockframework/runtime/ExtensionRunner.java`** -> AI Confidence: **99.31%**
5. **`spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureNode.java`** -> AI Confidence: **99.31%**
6. **`spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java`** -> AI Confidence: **99.31%**
7. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirExtension.java`** -> AI Confidence: **99.31%**
8. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TimeoutInterceptor.java`** -> AI Confidence: **99.31%**
9. **`spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java`** -> AI Confidence: **99.31%**
10. **`spock-specs/src/test/groovy/org/spockframework/mock/runtime/ByteBuddyMockMakerSpec.groovy`** -> AI Confidence: **99.31%**
11. **`spock-specs/src/test/groovy/org/spockframework/mock/runtime/CglibMockMakerSpec.groovy`** -> AI Confidence: **99.31%**
12. **`spock-specs/src/test/groovy/org/spockframework/mock/runtime/MockConfigurationSpec.groovy`** -> AI Confidence: **99.31%**
13. **`spock-specs/src/test/groovy/org/spockframework/mock/runtime/MockMakerRegistrySpec.groovy`** -> AI Confidence: **99.31%**
14. **`spock-specs/src/test/groovy/org/spockframework/mock/runtime/mockito/MockitoMockMakerSpec.groovy`** -> AI Confidence: **99.31%**
15. **`spock-specs/src/test/groovy/org/spockframework/mock/runtime/mockito/MockitoStaticMocksSpec.groovy`** -> AI Confidence: **99.31%**
16. **`spock-specs/src/test/groovy/org/spockframework/runtime/RunListenerSpec.groovy`** -> AI Confidence: **99.31%**
17. **`spock-specs/src/test/groovy/org/spockframework/smoke/StackTraceFiltering.groovy`** -> AI Confidence: **99.31%**
18. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy`** -> AI Confidence: **99.31%**
19. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/ExceptionConditions.groovy`** -> AI Confidence: **99.31%**
20. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/InvalidConditions.groovy`** -> AI Confidence: **99.31%**
21. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/IgnoreIfExtension.groovy`** -> AI Confidence: **99.31%**
22. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureExtensionSpec.groovy`** -> AI Confidence: **99.31%**
23. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/RetryFeatureExtensionSpec.groovy`** -> AI Confidence: **99.31%**
24. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/RetryTestAbortedExceptionInteropSpec.groovy`** -> AI Confidence: **99.31%**
25. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/TempDirExtensionSpec.groovy`** -> AI Confidence: **99.31%**
26. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/TimeoutExtension.groovy`** -> AI Confidence: **99.31%**
27. **`spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovyMocksForInterfaces.groovy`** -> AI Confidence: **99.31%**
28. **`spock-specs/src/test/groovy/org/spockframework/smoke/mock/InvokingMocksFromMultipleThreads.groovy`** -> AI Confidence: **99.31%**
29. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/DataTables.groovy`** -> AI Confidence: **99.31%**
30. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/MethodParameters.groovy`** -> AI Confidence: **99.31%**
31. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/ParameterizedFeatureNodeStatuses.groovy`** -> AI Confidence: **99.31%**
32. **`spock-specs/src/test/groovy/spock/util/concurrent/PollingConditionsSpec.groovy`** -> AI Confidence: **99.31%**
33. **`allVariants`** -> AI Confidence: **99.29%**
34. **`gradle/publishMaven.gradle`** -> AI Confidence: **99.29%**
35. **`settings.gradle`** -> AI Confidence: **99.29%**
36. **`spock-core/core.gradle`** -> AI Confidence: **99.29%**
37. **`spock-groovy2-compat/groovy2-compat.gradle`** -> AI Confidence: **99.29%**
38. **`spock-guice/guice.gradle`** -> AI Confidence: **99.29%**
39. **`spock-junit4/junit4.gradle`** -> AI Confidence: **99.29%**
40. **`spock-specs/specs.gradle`** -> AI Confidence: **99.29%**
41. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/AstSpec/groovy_3_language_features.groovy`** -> AI Confidence: **99.29%**
42. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod-[1].groovy`** -> AI Confidence: **99.29%**
43. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_with_exception-[1].groovy`** -> AI Confidence: **99.29%**
44. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod-[0].groovy`** -> AI Confidence: **99.29%**
45. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod-[1].groovy`** -> AI Confidence: **99.29%**
46. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod-[2].groovy`** -> AI Confidence: **99.29%**
47. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_exception-[0].groovy`** -> AI Confidence: **99.29%**
48. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_exception-[1].groovy`** -> AI Confidence: **99.29%**
49. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_exception-[2].groovy`** -> AI Confidence: **99.29%**
50. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_only_exception-[0].groovy`** -> AI Confidence: **99.29%**
51. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_only_exception-[1].groovy`** -> AI Confidence: **99.29%**
52. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_only_exception-[2].groovy`** -> AI Confidence: **99.29%**
53. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/VerifyAllMethodsAstSpec/interactions_are_illegal_in_verify_methods.groovy`** -> AI Confidence: **99.29%**
54. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/VerifyMethodsAstSpec/interactions_are_illegal_in_verify_methods.groovy`** -> AI Confidence: **99.29%**
55. **`spock-spring/spring.gradle`** -> AI Confidence: **99.29%**
56. **`spock-tapestry/tapestry.gradle`** -> AI Confidence: **99.29%**
57. **`spock-unitils/unitils.gradle`** -> AI Confidence: **99.29%**
58. **`spock-core/src/main/java/org/spockframework/compiler/DeepBlockRewriter.java`** -> AI Confidence: **99.24%**
59. **`spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java`** -> AI Confidence: **99.24%**
60. **`spock-core/src/main/java/org/spockframework/compiler/SpecParser.java`** -> AI Confidence: **99.24%**
61. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockController.java`** -> AI Confidence: **99.24%**
62. **`spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java`** -> AI Confidence: **99.24%**
63. **`spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java`** -> AI Confidence: **99.24%**
64. **`spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java`** -> AI Confidence: **99.24%**
65. **`spock-core/src/main/java/org/spockframework/runtime/SpockNode.java`** -> AI Confidence: **99.24%**
66. **`spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`** -> AI Confidence: **99.24%**
67. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RepeatUntilFailureExtension.java`** -> AI Confidence: **99.24%**
68. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryBaseInterceptor.java`** -> AI Confidence: **99.24%**
69. **`spock-junit4/src/main/java/org/spockframework/junit4/JUnit4AnnotationLifecycleMethodsExtension.java`** -> AI Confidence: **99.24%**
70. **`spock-junit4/src/test/groovy/org/spockframework/junit4/junit/JUnitRules.groovy`** -> AI Confidence: **99.24%**
71. **`spock-specs/src/test/groovy/org/spockframework/smoke/Interceptors.groovy`** -> AI Confidence: **99.24%**
72. **`spock-specs/src/test/groovy/org/spockframework/smoke/ast/AstSpec.groovy`** -> AI Confidence: **99.24%**
73. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/RequiresExtension.groovy`** -> AI Confidence: **99.24%**
74. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/SnapshotterSpec.groovy`** -> AI Confidence: **99.24%**
75. **`spock-specs/src/test/groovy/org/spockframework/verifyall/VerifyAllSpecification.groovy`** -> AI Confidence: **99.24%**
76. **`spock-specs/src/test/groovy/spock/util/mop/UseSpec.groovy`** -> AI Confidence: **99.24%**
77. **`spock-spring/src/test/groovy/org/spockframework/spring/SharedFieldsInjection.groovy`** -> AI Confidence: **99.24%**
78. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockInteraction.java`** -> AI Confidence: **99.23%**
79. **`spock-core/src/main/java/org/spockframework/runtime/FeatureNode.java`** -> AI Confidence: **99.23%**
80. **`spock-core/src/main/java/org/spockframework/runtime/StackTraceFilter.java`** -> AI Confidence: **99.23%**
81. **`spock-core/src/main/java/org/spockframework/util/RenderUtil.java`** -> AI Confidence: **99.23%**
82. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy`** -> AI Confidence: **99.23%**
83. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/RetryPendingFeatureInteropSpec.groovy`** -> AI Confidence: **99.23%**
84. **`spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy`** -> AI Confidence: **99.23%**
85. **`spock-spring/src/test/groovy/org/spockframework/spring/TransactionalGroovySqlExample.groovy`** -> AI Confidence: **99.23%**
86. **`spock-core/src/main/java/org/spockframework/runtime/condition/EditPathRenderer.java`** -> AI Confidence: **99.2%**
87. **`spock-core/src/main/java/org/spockframework/util/JsonWriter.java`** -> AI Confidence: **99.2%**
88. **`spock-specs/src/test/groovy/org/spockframework/smoke/ast/BlocksAst.groovy`** -> AI Confidence: **99.2%**
89. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/SeeExtension.groovy`** -> AI Confidence: **99.2%**
90. **`spock-core/src/main/java/org/spockframework/compiler/AstUtil.java`** -> AI Confidence: **99.18%**
91. **`spock-core/src/main/java/org/spockframework/compiler/SpockTransform.java`** -> AI Confidence: **99.18%**
92. **`spock-core/src/main/java/org/spockframework/compiler/condition/BaseVerifyMethodTransform.java`** -> AI Confidence: **99.18%**
93. **`spock-core/src/main/java/org/spockframework/mock/runtime/IMockMaker.java`** -> AI Confidence: **99.18%**
94. **`spock-core/src/main/java/org/spockframework/mock/runtime/JavaMockFactory.java`** -> AI Confidence: **99.18%**
95. **`spock-core/src/main/java/org/spockframework/mock/runtime/JavaProxyMockMaker.java`** -> AI Confidence: **99.18%**
96. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockCreationSettings.java`** -> AI Confidence: **99.18%**
97. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockObject.java`** -> AI Confidence: **99.18%**
98. **`spock-core/src/main/java/org/spockframework/runtime/ClassSelectorResolver.java`** -> AI Confidence: **99.18%**
99. **`spock-core/src/main/java/org/spockframework/runtime/RunContext.java`** -> AI Confidence: **99.18%**
100. **`spock-core/src/main/java/org/spockframework/runtime/extension/IStore.java`** -> AI Confidence: **99.18%**
101. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/GlobalTimeoutExtension.java`** -> AI Confidence: **99.18%**
102. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java`** -> AI Confidence: **99.18%**
103. **`spock-core/src/main/java/org/spockframework/runtime/model/MethodInfo.java`** -> AI Confidence: **99.18%**
104. **`spock-core/src/main/java/spock/lang/Snapshot.java`** -> AI Confidence: **99.18%**
105. **`spock-core/src/main/java/spock/lang/Specification.java`** -> AI Confidence: **99.18%**
106. **`spock-core/src/main/java/spock/util/io/FileSystemFixture.java`** -> AI Confidence: **99.18%**
107. **`spock-spring/src/main/java/org/spockframework/spring/SpringMockTestExecutionListener.java`** -> AI Confidence: **99.18%**
108. **`spock-spring/src/main/java/org/spockframework/spring/mock/DelegatingInterceptor.java`** -> AI Confidence: **99.18%**
109. **`spock-spring/src/main/java/org/spockframework/spring/mock/QualifierDefinition.java`** -> AI Confidence: **99.18%**
110. **`spock-spring/src/main/java/org/spockframework/spring/mock/SpockDefinition.java`** -> AI Confidence: **99.18%**
111. **`build-logic/preprocess-workflows/src/main/groovy/org/spockframework/gradle/PreprocessGithubWorkflowWorkAction.groovy`** -> AI Confidence: **99.18%**
112. **`spock-specs/src/main/groovy/org/spockframework/specs/jacoco/JacocoAstDumpTrigger.groovy`** -> AI Confidence: **99.18%**
113. **`spock-specs/src/test/groovy/org/spockframework/runtime/StoreSpec.groovy`** -> AI Confidence: **99.18%**
114. **`spock-specs/src/test/groovy/org/spockframework/smoke/DisambiguationInConditions.groovy`** -> AI Confidence: **99.18%**
115. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/IsRenderedExtension.groovy`** -> AI Confidence: **99.18%**
116. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/RepeatableLocalExtensionsSpec.groovy`** -> AI Confidence: **99.18%**
117. **`spock-spring/boot2-test/src/test/groovy/org/spockframework/boot2/SpringBootTestAnnotationScopedMockSpec.groovy`** -> AI Confidence: **99.18%**
118. **`spock-spring/boot2-test/src/test/groovy/org/spockframework/boot2/SpringBootTestAnnotationScopedProxyMockSpec.groovy`** -> AI Confidence: **99.18%**
119. **`spock-spring/boot2-test/src/test/groovy/org/spockframework/boot2/WebMvcTestIntegrationSpec.groovy`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/SpecAnnotator.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/SpecialMethodCall.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `spock-core/src/main/java/org/spockframework/runtime/IterationNode.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureChildExecutor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/runtime/SimpleFeatureNode.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/JavaProcessThreadDumpCollector.java` -> **100.0%** Exposure
- `spock-core/src/main/java/spock/lang/Snapshotter.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/buildsupport/SpecClassFileFinder.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/SpecParser.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4648` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/PendingFeatureIterationInterceptor.java` (JAVA) -> Cumulative Risk: **981.0**
- **Archetype:** `file_cluster_4` (Distance: 12.585 IQR)
- **Magnitude:** 227.72 | **LOC:** 97 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `intercept` (Impact: 46.3), `intercept` (Impact: 21.4), `InnerIterationInterceptor` (Impact: 20.3)

### 2. `spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureChildExecutor.java` (JAVA) -> Cumulative Risk: **980.53**
- **Archetype:** `file_cluster_4` (Distance: 11.18 IQR)
- **Magnitude:** 191.48 | **LOC:** 120 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ParameterizedFeatureChildExecutor` (Impact: 122.5), `execute` (Impact: 4.9), `awaitFinished` (Impact: 4.2)

### 3. `spock-core/src/main/java/org/spockframework/runtime/SimpleFeatureNode.java` (JAVA) -> Cumulative Risk: **811.89**
- **Archetype:** `file_cluster_4` (Distance: 9.646 IQR)
- **Magnitude:** 67.92 | **LOC:** 67 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `execute` (Impact: 22.0), `SimpleFeatureNode` (Impact: 8.1), `prepare` (Impact: 4.7)

### 4. `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java` (JAVA) -> Cumulative Risk: **792.27**
- **Archetype:** `file_cluster_4` (Distance: 11.546 IQR)
- **Magnitude:** 114.2 | **LOC:** 124 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9693%), State Flux (99.9648%)
- **Heaviest Functions:** `intercept` (Impact: 20.8), `intercept` (Impact: 17.4), `addInterceptorToFeatureMethod` (Impact: 8.5)

### 5. `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` (JAVA) -> Cumulative Risk: **782.48**
- **Archetype:** `file_cluster_0` (Distance: 10.719 IQR)
- **Magnitude:** 397.68 | **LOC:** 868 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9997%)
- **Heaviest Functions:** `visitMapExpression` (Impact: 28.6), `rewriteToSpockRuntimeCall` (Impact: 25.7), `surroundWithTryCatch` (Impact: 23.8)

### 6. `spock-core/src/main/java/org/spockframework/compiler/SpecAnnotator.java` (JAVA) -> Cumulative Risk: **778.39**
- **Archetype:** `file_cluster_0` (Distance: 11.144 IQR)
- **Magnitude:** 219.96 | **LOC:** 251 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (98.6989%), Tech Debt (97.0997%)
- **Heaviest Functions:** `handleMultipleContainedAnnotations` (Impact: 50.1), `addRepeatedExtensionAnnotations` (Impact: 32.5), `flattenRepeatableExtensionAnnotationCont` (Impact: 25.3)

### 7. `spock-core/src/main/java/org/spockframework/runtime/model/MethodInfo.java` (JAVA) -> Cumulative Risk: **771.04**
- **Archetype:** `file_cluster_13` (Distance: 10.708 IQR)
- **Magnitude:** 165.36 | **LOC:** 171 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9961%), Documentation (99.9582%), Tech Debt (97.9284%)
- **Heaviest Functions:** `invoke` (Impact: 56.3), `getParameters` (Impact: 18.6), `getNameProvider` (Impact: 7.5)

### 8. `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoConverter.java` (JAVA) -> Cumulative Risk: **759.42**
- **Archetype:** `file_cluster_0` (Distance: 10.34 IQR)
- **Magnitude:** 287.0 | **LOC:** 422 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9361%)
- **Heaviest Functions:** `visitTernaryExpression` (Impact: 23.0), `visitBinaryExpression` (Impact: 14.0), `visitShortTernaryExpression` (Impact: 13.9)

### 9. `spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java` (JAVA) -> Cumulative Risk: **730.55**
- **Archetype:** `file_cluster_13` (Distance: 10.557 IQR)
- **Magnitude:** 524.68 | **LOC:** 411 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getExistingBeans` (Impact: 49.1), `determinePrimaryCandidate` (Impact: 42.9), `getBeanName` (Impact: 40.2)

### 10. `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA) -> Cumulative Risk: **724.68**
- **Archetype:** `file_cluster_8` (Distance: 11.766 IQR)
- **Magnitude:** 395.18 | **LOC:** 454 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9767%), State Flux (99.8747%)
- **Heaviest Functions:** `invoke` (Impact: 24.2), `runIterationCleanups` (Impact: 17.3), `createMethodInfoForDoRunInitializer` (Impact: 16.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `config/code-signing-secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooFewInvocations.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.461 IQR)
- **Top Global Matches:** file_cluster_8: 9.461, file_cluster_7: 10.267, file_cluster_1: 10.463
- **Magnitude:** 2962.86 | **LOC:** 1225 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (25.0661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 398.8 | O(2^N))
  * `def` (Impact: 217.7 | O(2^N))
  * `def` (Impact: 203.6 | O(2^N))
  * `def` (Impact: 189.8 | O(2^N))
  * `def` (Impact: 180.0 | O(2^N))
    * *Intent:* /* * Copyright 2012 the original author or authors. * * Licensed under the Apache License, Version 2...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 145`, `args: 71`, `func_start: 98`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `import: 4`
* *Defense:* `safety: 5`, `test: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.spockframework.EmbeddedSpecification, java.util.regex.Pattern, org.hamcrest.CoreMatchers, org.spockframework.mock.TooFewInvocationsError
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.625 IQR)
- **Top Global Matches:** file_cluster_8: 11.625, file_cluster_7: 12.115, file_cluster_13: 12.234
- **Magnitude:** 2359.86 | **LOC:** 2144 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (63.0473%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 1491.3 | O(2^N) | DB: 36)
  * `def` (Impact: 18.0 | O(2^N))
  * `def` (Impact: 18.0 | O(2^N) | DB: 1)
  * `def` (Impact: 17.9 | O(2^N))
  * `def` (Impact: 17.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 171`, `args: 204`, `func_start: 228`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 174`, `duplicate_logic: 81`, `orphaned_logic: 3`
* *Architecture:* `api: 70`, `import: 5`
* *Defense:* `safety: 4`, `doc: 1`, `test: 453`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` spock.util.environment.Jvm, org.spockframework.runtime.GroovyRuntimeUtil, java.lang.reflect.Modifier, java.util.regex.Pattern, spock.lang.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.947 IQR)
- **Top Global Matches:** file_cluster_8: 8.947, file_cluster_7: 9.797, file_cluster_1: 9.975
- **Magnitude:** 2063.32 | **LOC:** 746 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.8352%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 516.8 | O(2^N))
  * `def` (Impact: 376.6 | O(2^N))
  * `def` (Impact: 310.9 | O(2^N))
  * `def` (Impact: 258.2 | O(2^N))
  * `def` (Impact: 225.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 87`, `args: 50`, `func_start: 70`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `duplicate_logic: 9`
* *Architecture:* `import: 3`
* *Defense:* `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.spockframework.EmbeddedSpecification, org.spockframework.mock.TooManyInvocationsError, java.util.regex.Pattern
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/UnrolledFeatureMethods.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.375 IQR)
- **Top Global Matches:** file_cluster_8: 10.375, file_cluster_0: 10.68, file_cluster_13: 10.98
- **Magnitude:** 1916.66 | **LOC:** 608 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (33.7979%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 158.8 | O(2^N) | DB: 1)
  * `def` (Impact: 146.8 | O(2^N))
  * `def` (Impact: 146.5 | O(2^N))
  * `def` (Impact: 134.3 | O(2^N))
  * `def` (Impact: 134.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 107`, `args: 24`, `func_start: 51`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`, `duplicate_logic: 24`, `orphaned_logic: 2`
* *Architecture:* `import: 5`
* *Defense:* `doc: 1`, `test: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.spockframework.runtime.extension.*, org.spockframework.EmbeddedSpecification, org.spockframework.runtime.model.*, java.lang.annotation.*, spock.lang.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.947 IQR)
- **Top Global Matches:** file_cluster_8: 11.947, file_cluster_0: 12.103, file_cluster_13: 12.292
- **Magnitude:** 1346.14 | **LOC:** 1381 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (23.0096%), Tech Debt (97.8681%)
**Top Internal Functions/Classes:**
  * `visitClass` (Impact: 54.1 | O(N^2) | DB: 2)
  * `visitMethod` (Impact: 50.5 | O(N^3) | DB: 1)
  * `compileScript` (Impact: 45.9 | O(N^2) | DB: 3)
    * *Intent:* /* * This has been adapted from https://github.com/apache/groovy/blob/5d2944523f198d96b6515e85a24d2b...
  * `visitGStringExpression` (Impact: 45.4 | O(N^3))
  * `visitAllImports` (Impact: 39.5 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 72`, `args: 244`, `func_start: 237`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 79`, `duplicate_logic: 10`, `orphaned_logic: 46`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 23`, `doc: 24`, `sync_locks: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.codehaus.groovy.syntax.Types, groovy.transform.*, org.objectweb.asm.ClassReader, org.codehaus.groovy.classgen.*, java.lang.reflect.Modifier, org.codehaus.groovy.ast.expr.*, org.objectweb.asm.FieldVisitor, org.codehaus.groovy.control.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.56 IQR)
- **Top Global Matches:** file_cluster_0: 10.56, file_cluster_8: 10.692, file_cluster_16: 10.756
- **Magnitude:** 1113.92 | **LOC:** 998 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.2978%), Tech Debt (99.9946%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 114.9 | O(2^N) | DB: 1)
  * `next` (Impact: 98.0 | O(2^N) | DB: 1)
  * `DataProviderMultiplier` (Impact: 80.6 | O(2^N))
    * *Intent:* /** * During the first set of multiplier values, i.e. the first value of the {@link #multiplierItera...
  * `next` (Impact: 73.7 | O(2^N))
  * `estimateNumIterations` (Impact: 61.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 182`, `args: 64`, `func_start: 76`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 15`, `dead_code: 2`, `duplicate_logic: 34`, `orphaned_logic: 2`
* *Architecture:* `api: 52`, `import: 10`
* *Defense:* `safety: 39`, `doc: 36`, `immutability_locks: 32`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` spock.config.RunnerConfiguration, java.util.stream.Collectors.toList, java.io.StringWriter, org.spockframework.runtime.GroovyRuntimeUtil.closeQuietly, java.util.*, org.spockframework.util.Nullable, org.spockframework.runtime.model.*, java.io.PrintWriter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureExtensionSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.805 IQR)
- **Top Global Matches:** file_cluster_8: 9.805, file_cluster_0: 10.584, file_cluster_7: 10.597
- **Magnitude:** 836.96 | **LOC:** 729 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.1849%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 43.1 | O(2^N))
  * `def` (Impact: 43.1 | O(2^N))
  * `def` (Impact: 42.9 | O(2^N))
  * `def` (Impact: 42.9 | O(2^N))
  * `def` (Impact: 42.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 91`, `args: 132`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 26`, `orphaned_logic: 1`
* *Architecture:* `import: 9`
* *Defense:* `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.junit.platform.testkit.engine.TestExecutionResultConditions.message, org.assertj.core.api.Condition, org.spockframework.EmbeddedSpecification, org.junit.platform.testkit.engine.EventConditions.finishedWithFailure, org.opentest4j.MultipleFailuresError, org.junit.platform.testkit.engine.EventConditions.abortedWithReason, org.junit.platform.testkit.engine.TestExecutionResultConditions.cause, org.opentest4j.TestAbortedException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.165 IQR)
- **Top Global Matches:** file_cluster_13: 15.165, file_cluster_11: 15.195, file_cluster_17: 15.199
- **Magnitude:** 710.52 | **LOC:** 713 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (12.4874%), Tech Debt (41.8342%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 669.3 | O(N^6) | DB: 27)
    * *Intent:* /** * This compound extension consists of an include processor, a tree processor, and a post process...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 58`, `args: 35`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 28`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 7`, `import: 16`
* *Defense:* `safety: 3`, `doc: 39`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.*, org.asciidoctor.extension.*, java.nio.file.Files.readString, org.asciidoctor.extension.Contexts.LITERAL, java.lang.String.join, java.lang.Boolean.parseBoolean, org.asciidoctor.extension.Contexts.LISTING, java.util.regex.Pattern...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.562 IQR)
- **Top Global Matches:** file_cluster_8: 9.562, file_cluster_7: 10.342, file_cluster_13: 10.406
- **Magnitude:** 626.62 | **LOC:** 898 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (26.8135%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 25.6 | O(2^N))
  * `def` (Impact: 25.4 | O(2^N))
  * `def` (Impact: 21.9 | O(2^N) | DB: 1)
  * `def` (Impact: 21.8 | O(2^N) | DB: 1)
  * `def` (Impact: 21.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 99`, `args: 14`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `duplicate_logic: 48`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `doc: 1`, `test: 207`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.spockframework.compiler.InvalidSpecCompileException, org.spockframework.runtime.SpockExecutionException, org.spockframework.EmbeddedSpecification, spock.lang.Snapshotter, org.opentest4j.MultipleFailuresError, org.codehaus.groovy.syntax.SyntaxException, spock.lang.Issue, spock.lang.Snapshot
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/ParameterizedFeatureNodeStatuses.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.071 IQR)
- **Top Global Matches:** file_cluster_8: 9.071, file_cluster_7: 9.955, file_cluster_13: 10.029
- **Magnitude:** 612.1 | **LOC:** 892 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.7049%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 45.9 | O(2^N))
  * `def` (Impact: 44.0 | O(2^N))
  * `def` (Impact: 31.6 | O(2^N))
  * `def` (Impact: 29.9 | O(2^N))
  * `def` (Impact: 29.7 | O(2^N))
    * *Intent:* * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file exce...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 89`, `args: 40`, `func_start: 76`, `class_start: 4`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 23`, `orphaned_logic: 1`
* *Architecture:* `import: 19`
* *Defense:* `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` org.spockframework.runtime.extension.IAnnotationDrivenExtension, java.lang.annotation.Target, org.opentest4j.TestAbortedException, org.spockframework.runtime.model.parallel.ExecutionMode, java.lang.annotation.Retention, org.spockframework.runtime.extension.IMethodInvocation, org.spockframework.runtime.model.ErrorInfo, org.spockframework.runtime.AbstractRunListener...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/extension/ParallelSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.405 IQR)
- **Top Global Matches:** file_cluster_4: 10.405, file_cluster_8: 10.461, file_cluster_0: 10.668
- **Magnitude:** 599.82 | **LOC:** 534 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (88.3057%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 49.8 | O(2^N) | DB: 1)
  * `def` (Impact: 49.7 | O(2^N) | DB: 1)
  * `def` (Impact: 43.0 | O(2^N))
  * `def` (Impact: 38.0 | O(2^N))
  * `def` (Impact: 32.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 112`, `args: 72`, `func_start: 85`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 21`, `duplicate_logic: 13`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 116`, `import: 6`
* *Defense:* `safety: 2`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.concurrent.CountDownLatch, java.util.concurrent.atomic.AtomicInteger, org.spockframework.EmbeddedSpecification, java.util.concurrent.TimeUnit.MILLISECONDS, org.spockframework.runtime.model.parallel.*, spock.lang.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/extension/RetryFeatureExtensionSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.034 IQR)
- **Top Global Matches:** file_cluster_8: 10.034, file_cluster_0: 10.379, file_cluster_13: 10.554
- **Magnitude:** 596.52 | **LOC:** 760 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.6244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 28.8 | O(2^N) | DB: 1)
  * `def` (Impact: 28.8 | O(2^N))
  * `def` (Impact: 27.7 | O(2^N))
  * `def` (Impact: 25.4 | O(2^N))
  * `def` (Impact: 25.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 137`, `args: 57`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 20`, `duplicate_logic: 30`
* *Architecture:* `concurrency: 15`, `import: 17`
* *Defense:* `safety: 8`, `test: 115`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.spockframework.runtime.ConditionNotSatisfiedError, java.util.concurrent.atomic.AtomicInteger, org.spockframework.runtime.SpockMultipleFailuresError, org.junit.platform.testkit.engine.EventConditions.finishedSuccessfully, org.junit.platform.testkit.engine.EventConditions.event, org.spockframework.runtime.extension.IAnnotationDrivenExtension, org.junit.platform.testkit.engine.EventConditions.test, org.spockframework.EmbeddedSpecification...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.557 IQR)
- **Top Global Matches:** file_cluster_13: 10.557, file_cluster_8: 10.826, file_cluster_16: 10.923
- **Magnitude:** 524.68 | **LOC:** 411 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.0983%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getExistingBeans` (Impact: 49.1 | O(2^N) | DB: 1)
  * `determinePrimaryCandidate` (Impact: 42.9 | O(N^6))
  * `getBeanName` (Impact: 40.2 | O(N^6))
  * `getExistingBeans` (Impact: 37.2 | O(N^6) | DB: 1)
  * `register` (Impact: 36.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 101`, `args: 34`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 28`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 11`, `import: 24`
* *Defense:* `safety: 8`, `doc: 16`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.502
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0008
  * `Imports (Out-Degree: 5):` java.util.concurrent.ConcurrentHashMap, org.spockframework.spring.SpringExtensionException, org.springframework.util.StringUtils, java.util.*, org.springframework.beans.factory.BeanFactory, org.springframework.beans.factory.support.BeanNameGenerator, org.springframework.core.PriorityOrdered, org.springframework.beans.factory.FactoryBean...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.837 IQR)
- **Top Global Matches:** file_cluster_16: 9.837, file_cluster_8: 10.412, file_cluster_13: 10.587
- **Magnitude:** 496.68 | **LOC:** 354 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.8488%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createMockImpl` (Impact: 40.2 | O(N^2))
  * `createMockImpl` (Impact: 19.2 | O(2^N))
  * `createStaticMock` (Impact: 17.4 | O(2^N))
  * `checkExceptionThrown` (Impact: 16.4 | O(N^2))
  * `createMock` (Impact: 14.7 | O(N^2))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 104`, `args: 123`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 71`, `planned_debt: 16`, `duplicate_logic: 60`
* *Architecture:* `api: 60`, `import: 10`
* *Defense:* `doc: 2`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0018
  * `Imports (Out-Degree: 2):` groovy.transform.stc.SecondParam, spock.mock.IMockMakerSettings, org.spockframework.util.*, spock.lang.Specification, java.util.*, java.util.Collections.emptyMap, org.spockframework.util.ObjectUtil.uncheckedCast, groovy.transform.stc.ClosureParams...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.854 IQR)
- **Top Global Matches:** file_cluster_8: 9.854, file_cluster_13: 10.643, file_cluster_7: 10.653
- **Magnitude:** 488.36 | **LOC:** 906 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.878%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 68.9 | O(2^N))
  * `def` (Impact: 45.8 | O(2^N))
  * `def` (Impact: 27.0 | O(2^N))
  * `def` (Impact: 21.4 | O(2^N))
  * `def` (Impact: 21.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 155`, `args: 36`, `func_start: 82`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 72`, `dead_code: 1`, `duplicate_logic: 50`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 59`, `doc: 1`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.spockframework.runtime.GroovyRuntimeUtil, java.lang.Math.min, spock.lang.Requires, java.sql.Date, spock.lang.Issue, org.spockframework.runtime.SpockComparisonFailure, spock.lang.ResourceLock, java.lang.Integer.MAX_VALUE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureIfExtensionSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.381 IQR)
- **Top Global Matches:** file_cluster_8: 9.381, file_cluster_0: 9.825, file_cluster_7: 10.193
- **Magnitude:** 462.76 | **LOC:** 391 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (20.1154%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 32.0 | O(2^N))
  * `def` (Impact: 25.2 | O(2^N))
  * `def` (Impact: 25.0 | O(2^N))
  * `def` (Impact: 25.0 | O(2^N))
  * `def` (Impact: 25.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 74`, `args: 26`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 21`
* *Architecture:* `import: 5`
* *Defense:* `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.spockframework.EmbeddedSpecification, org.spockframework.runtime.ConditionNotSatisfiedError, org.spockframework.runtime.SpockComparisonFailure, spock.lang.PendingFeatureIf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/spock/util/concurrent/PollingConditionsSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.418 IQR)
- **Top Global Matches:** file_cluster_8: 11.418, file_cluster_4: 11.434, file_cluster_0: 11.541
- **Magnitude:** 455.12 | **LOC:** 465 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (66.0971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 39.3 | O(2^N) | DB: 1)
  * `def` (Impact: 39.3 | O(2^N) | DB: 1)
  * `def` (Impact: 35.1 | O(2^N) | DB: 1)
  * `def` (Impact: 35.0 | O(2^N) | DB: 1)
  * `def` (Impact: 35.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 61`, `args: 19`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 52`, `duplicate_logic: 17`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 36`, `import: 9`
* *Defense:* `safety: 12`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` org.spockframework.runtime.ConditionNotSatisfiedError, org.spockframework.runtime.GroovyRuntimeUtil, org.spockframework.EmbeddedSpecification, spock.lang.PendingFeatureIf, org.spockframework.runtime.SpockTimeoutError, spock.lang.PendingFeature, spock.lang.Requires, spock.lang.Issue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.858 IQR)
- **Top Global Matches:** file_cluster_16: 10.858, file_cluster_13: 11.044, file_cluster_8: 11.164
- **Magnitude:** 454.86 | **LOC:** 422 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (29.3591%), Tech Debt (28.8526%)
**Top Internal Functions/Classes:**
  * `collectAll` (Impact: 16.3 | O(2^N))
  * `filterFeatures` (Impact: 15.0 | O(N^2) | DB: 1)
  * `toFeatureName` (Impact: 13.7 | O(N^2))
  * `isInitializerOrFixtureMethod` (Impact: 13.5 | O(N^2))
  * `getSpecsTopToBottom` (Impact: 12.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 111`, `args: 90`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`, `duplicate_logic: 2`
* *Architecture:* `api: 123`, `import: 13`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.121
  * `Choke Point (Betweenness):` 0.004675 | `Ripple Effect (Closeness):` 0.114779
  * `Imports (Out-Degree: 9):` org.spockframework.runtime.IFeatureSortOrder, java.util.*, org.spockframework.runtime.model.parallel.ExclusiveResource, org.spockframework.runtime.IMethodNameMapper, java.util.Comparator.comparingInt, java.util.function.Supplier, org.spockframework.util.CollectionUtil, java.util.function.BiConsumer...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/spock/lang/Snapshotter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.656 IQR)
- **Top Global Matches:** file_cluster_13: 10.656, file_cluster_0: 10.957, file_cluster_8: 10.961
- **Magnitude:** 452.58 | **LOC:** 366 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (8.5156%), Tech Debt (37.0168%)
**Top Internal Functions/Classes:**
  * `matchesSnapshot` (Impact: 359.1 | O(2^N) | DB: 32)
  * `loadSnapshot` (Impact: 13.6 | O(2^N))
    * *Intent:* /** * Allows to perform snapshot testing. * <p>
  * `deleteActual` (Impact: 4.7 | O(2^N))
  * `matchesSnapshot` (Impact: 4.2 | O(2^N))
    * *Intent:* /** * Declares a {@link Function} for normalizing the reference value. * <p>
  * `saveSnapshot` (Impact: 3.7 | O(2^N))
    * *Intent:* /** * Allows to perform snapshot testing. * <p> * Snapshots are stored in a file in the configured {...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 69`, `args: 60`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 36`, `import: 21`
* *Defense:* `safety: 14`, `doc: 12`, `test: 1`, `sync_locks: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.059
  * `Choke Point (Betweenness):` 0.000248 | `Ripple Effect (Closeness):` 0.009697
  * `Imports (Out-Degree: 9):` java.util.Locale, java.nio.file.Files, java.nio.charset.Charset, java.util.function.BiConsumer, java.util.Objects, org.spockframework.util.Checks, org.spockframework.runtime.ConditionNotSatisfiedError, org.spockframework.util.IoUtil...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.054 IQR)
- **Top Global Matches:** file_cluster_17: 11.054, file_cluster_13: 11.26, file_cluster_0: 11.385
- **Magnitude:** 441.28 | **LOC:** 984 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (22.7078%), Tech Debt (98.0673%)
**Top Internal Functions/Classes:**
  * `rewrite` (Impact: 47.5 | O(N^3) | DB: 10)
  * `rewriteWhereStat` (Impact: 41.5 | O(N^2) | DB: 13)
  * `handleFeatureParameters` (Impact: 22.3 | O(N^2) | DB: 3)
  * `generatePreviousColumnExtractorStatement` (Impact: 21.7 | O(N^6) | DB: 4)
  * `createDataProcessorAnnotation` (Impact: 21.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 132`, `args: 61`, `func_start: 47`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 47`, `dead_code: 2`, `duplicate_logic: 8`, `orphaned_logic: 5`
* *Architecture:* `io: 12`, `api: 8`, `import: 13`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.util.*, java.lang.Boolean.FALSE, org.codehaus.groovy.syntax.*, org.spockframework.util.*, org.spockframework.runtime.model.DataProcessorMetadata, java.util.function.Function.identity, org.codehaus.groovy.control.SourceUnit, org.codehaus.groovy.ast.expr.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/DataTables.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.238 IQR)
- **Top Global Matches:** file_cluster_8: 9.238, file_cluster_13: 10.024, file_cluster_7: 10.059
- **Magnitude:** 440.6 | **LOC:** 846 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.1549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 38.5 | O(2^N) | DB: 1)
  * `def` (Impact: 29.1 | O(2^N))
  * `def` (Impact: 19.3 | O(2^N))
  * `def` (Impact: 19.3 | O(2^N))
  * `def` (Impact: 19.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 92`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `state_mutation: 21`, `duplicate_logic: 46`
* *Architecture:* `import: 15`
* *Defense:* `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` org.spockframework.runtime.SpockExecutionException, org.spockframework.runtime.model.parallel.Resources.SYSTEM_OUT, org.spockframework.runtime.StandardStreamsCapturer, spock.lang.Shared, org.spockframework.EmbeddedSpecification, spock.lang.AutoCleanup, spock.lang.Snapshotter, spock.lang.PendingFeature...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.169 IQR)
- **Top Global Matches:** file_cluster_8: 10.169, file_cluster_13: 10.532, file_cluster_0: 10.704
- **Magnitude:** 430.3 | **LOC:** 562 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (23.4834%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 44.2 | O(2^N))
  * `def` (Impact: 26.2 | O(2^N) | DB: 1)
  * `def` (Impact: 26.2 | O(2^N))
  * `def` (Impact: 21.0 | O(N^1))
  * `def` (Impact: 19.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 117`, `args: 29`, `func_start: 80`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 55`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 2`, `import: 14`
* *Defense:* `safety: 9`, `doc: 1`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.spockframework.runtime.ConditionNotSatisfiedError, java.util.regex.Matcher, org.spockframework.runtime.ConditionFailedWithExceptionError, org.spockframework.EmbeddedSpecification, java.lang.Math.min, spock.lang.Snapshotter, org.opentest4j.AssertionFailedError, java.util.regex.Pattern...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/mock/runtime/mockito/MockitoMockMakerSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.147 IQR)
- **Top Global Matches:** file_cluster_8: 9.147, file_cluster_13: 9.751, file_cluster_0: 9.899
- **Magnitude:** 429.34 | **LOC:** 546 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (35.3485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 63.0 | O(2^N))
  * `def` (Impact: 28.4 | O(2^N))
  * `def` (Impact: 26.2 | O(2^N))
  * `def` (Impact: 23.5 | O(2^N))
  * `def` (Impact: 16.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 124`, `args: 23`, `func_start: 61`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 2`, `planned_debt: 2`, `duplicate_logic: 41`
* *Architecture:* `concurrency: 13`, `import: 15`
* *Defense:* `safety: 6`, `test: 97`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` spock.util.environment.Jvm, java.lang.reflect.Proxy, spock.lang.Specification, org.spockframework.mock.MockUtil, org.spockframework.runtime.GroovyRuntimeUtil, spock.mock.DetachedMockFactory, org.spockframework.mock.runtime.ByteBuddyTestClassLoader, org.spockframework.mock.CannotCreateMockException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/MethodParameters.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.782 IQR)
- **Top Global Matches:** file_cluster_8: 10.782, file_cluster_0: 10.79, file_cluster_13: 10.95
- **Magnitude:** 412.36 | **LOC:** 425 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.8522%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 61.2 | O(2^N))
  * `def` (Impact: 45.0 | O(2^N))
  * `def` (Impact: 42.9 | O(2^N))
  * `def` (Impact: 35.3 | O(2^N))
  * `def` (Impact: 32.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 57`, `args: 21`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `duplicate_logic: 25`
* *Architecture:* `import: 14`
* *Defense:* `safety: 10`, `doc: 1`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` org.spockframework.runtime.SpockExecutionException, org.spockframework.runtime.model.MethodInfo, org.junit.platform.testkit.engine.EventConditions.displayName, org.spockframework.runtime.extension.IAnnotationDrivenExtension, org.spockframework.EmbeddedSpecification, java.lang.annotation.RetentionPolicy, spock.lang.Unroll, org.codehaus.groovy.runtime.typehandling.GroovyCastException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `spock-core/src/main/java/spock/util/time/MutableClock.java` (JAVA) | Magnitude: 68.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, doc: 29, func_start: 23, structural_boundaries: 20
- `spock-core/src/main/java/spock/util/io/FileSystemFixture.java` (JAVA) | Magnitude: 107.92 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 38, io: 26, args: 20
- `spock-core/src/main/java/org/spockframework/mock/constraint/WildcardArgumentConstraint.java` (JAVA) | Magnitude: 10.88 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, api: 4, args: 3
- `spock-guice/src/test/groovy/org/spockframework/guice/GuiceSpecInheritance.groovy` (GROOVY) | Magnitude: 9.28 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 14, safety: 13, decorators: 5
- `spock-spring/src/test/groovy/org/spockframework/spring/mock/ComplexUsageSpec.groovy` (GROOVY) | Magnitude: 23.44 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, decorators: 17, structural_boundaries: 15, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/DefaultValueProvider.groovy` (GROOVY) | Magnitude: 38.52 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 16, branch: 13, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `spock-core/src/main/java/spock/config/IncludeExcludeCriteria.java` (JAVA) | Magnitude: 39.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, branch: 9, structural_boundaries: 9, state_mutation: 6
- `spock-specs/src/test/groovy/org/spockframework/runtime/RunListenerSpec.groovy` (GROOVY) | Magnitude: 302.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 184, branch: 59, structural_boundaries: 54, test: 50
- `spock-core/src/main/groovy/spock/util/EmbeddedSpecCompiler.groovy` (GROOVY) | Magnitude: 156.4 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 33, func_start: 32, args: 30
- `spock-core/src/main/java/org/spockframework/mock/response/DefaultResponseGenerator.java` (JAVA) | Magnitude: 6.82 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 2, decorators: 2
- `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoValueRenderer.java` (JAVA) | Magnitude: 83.06 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 32, branch: 16, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `spock-spring/src/main/java/org/spockframework/spring/mock/SpockContextCustomizerFactory.java` (JAVA) | Magnitude: 13.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, generics: 2, branch: 1
- `spock-core/src/main/java/org/spockframework/util/IThrowableBiConsumer.java` (JAVA) | Magnitude: 17.74 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 2, args: 1, func_start: 1
- `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` (JAVA) | Magnitude: 310.3 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 232, api: 107, structural_boundaries: 91, args: 57
- `spock-core/src/main/java/org/spockframework/runtime/extension/IStatelessAnnotationDrivenExtension.java` (JAVA) | Magnitude: 14.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 5, generics: 2, import: 2
- `spock-core/src/main/java/org/spockframework/mock/TooManyInvocationsError.java` (JAVA) | Magnitude: 106.54 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 76, branch: 20, structural_boundaries: 19, api: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `spock-core/src/main/java/org/spockframework/runtime/ExtensionRunner.java` (JAVA) | Magnitude: 234.7 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, branch: 48, structural_boundaries: 33, func_start: 25
- `spock-specs/specs.gradle` (GROOVY) | Magnitude: 35.36 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 23, branch: 10, args: 6
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (JAVA) | Magnitude: 441.28 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 364, structural_boundaries: 132, branch: 70, args: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `spock-core/src/main/java/org/spockframework/runtime/AsyncRunListener.java` (JAVA) | Magnitude: 116.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 26, args: 24, func_start: 24
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java` (JAVA) | Magnitude: 114.2 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 35, state_mutation: 24, concurrency: 19
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/ParallelSpec.groovy` (GROOVY) | Magnitude: 599.82 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 415, concurrency: 116, structural_boundaries: 112, func_start: 85
- `spock-specs/src/test/groovy/org/spockframework/runtime/extension/builtin/ThreadDumpUtilityTypeTest.groovy` (GROOVY) | Magnitude: 20.66 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, concurrency: 12, import: 7
- `spock-core/src/main/java/org/spockframework/runtime/SimpleFeatureNode.java` (JAVA) | Magnitude: 67.92 | Delta: **0.22 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, concurrency: 18, func_start: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `spock-core/src/main/java/org/spockframework/runtime/model/parallel/Resources.java` (JAVA) | Magnitude: 9.12 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, sec_high_risk_execution: 10, indent_spaces: 8, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `spock-specs/src/test/groovy/org/spockframework/groovy/PackageNames.groovy` (GROOVY) | Magnitude: 7.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 7, import: 4, branch: 2
- `spock-core/src/main/java/org/spockframework/mock/DefaultCompareToInteraction.java` (JAVA) | Magnitude: 14.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 5, api: 5
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ThreadDumpUtilityType.java` (JAVA) | Magnitude: 34.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 16, args: 10, branch: 7
- `spock-unitils/src/test/groovy/org/spockframework/unitils/dbunit/UserDaoSpec.groovy` (GROOVY) | Magnitude: 17.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 15, import: 7, func_start: 6
- `spock-core/src/main/java/org/spockframework/compiler/NoSpecialMethodCall.java` (JAVA) | Magnitude: 71.94 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 30, api: 23, args: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `spock-specs/src/test/java/org/spockframework/smoke/CallChainException.java` (JAVA) | Magnitude: 12.04 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, class_start: 1, api: 1, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 2359.86
- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooManyInvocations.groovy` -> **Leonard Brünings** (100.0% isolated ownership) | Magnitude: 2063.32
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/RetryFeatureExtensionSpec.groovy` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 596.52
- `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 496.68
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 488.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 0.884** (Bridge: 0.0109 * Flux: 81.51%)
- `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` -> **Severity: 0.311** (Bridge: 0.004 * Flux: 78.1336%)
- `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` -> **Severity: 0.309** (Bridge: 0.0047 * Flux: 66.0852%)
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/StepwiseExtension.java` -> **Severity: 0.097** (Bridge: 0.001 * Flux: 95.8452%)
- `spock-core/src/main/java/org/spockframework/runtime/model/MethodInfo.java` -> **Severity: 0.065** (Bridge: 0.0007 * Flux: 97.5913%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 17.365** (Embedded: 0.2058 * Error Risk: 84.3935%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 11.607** (Embedded: 0.1398 * Error Risk: 83.0115%)
- `spock-core/src/main/java/org/spockframework/util/ObjectUtil.java` -> **Severity: 10.246** (Embedded: 0.1035 * Error Risk: 98.9604%)
- `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` -> **Severity: 8.563** (Embedded: 0.1148 * Error Risk: 74.6016%)
- `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` -> **Severity: 8.23** (Embedded: 0.0911 * Error Risk: 90.3095%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `spock-core/src/main/java/org/spockframework/lang/Wildcard.java` -> **Severity: 1612.236** (Blast Radius: 16.123 * Doc Risk: 99.996%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 1160.958** (Blast Radius: 13.64 * Doc Risk: 85.1142%)
- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 1005.166** (Blast Radius: 67.459 * Doc Risk: 14.9004%)
- `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` -> **Severity: 889.85** (Blast Radius: 8.972 * Doc Risk: 99.1808%)
- `spock-core/src/main/java/org/spockframework/runtime/InvalidSpecException.java` -> **Severity: 687.729** (Blast Radius: 6.879 * Doc Risk: 99.9752%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
