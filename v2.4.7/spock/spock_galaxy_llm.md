# ARCHITECTURAL_BRIEF: spock
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/spock` |
| **Timestamp** | `2026-08-07T05:37:36.039006+00:00` |
| **Scan Duration** | `3.44s` |
| **Git Branch** | `master` |
| **Git Commit** | `b71e3d7590dae28d608aa92f90b45bef33aaeda8` |
| **Git Remote** | `https://github.com/spockframework/spock` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1193 malicious artifacts.

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
| Total Artifacts | 1420 |
| Analyzed Artifacts (Scanned) | 1251 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 169 |
| Total LOC | 73747 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.1% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5534 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `5.299`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 726 | 58.0% |
| file_cluster_13 | 320 | 25.6% |
| file_cluster_0 | 92 | 7.4% |
| file_cluster_16 | 50 | 4.0% |
| file_cluster_4 | 11 | 0.9% |
| file_cluster_17 | 3 | 0.2% |
| Unknown | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

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
| Cognitive Load Exposure | 0.0 | 100.0 | 12.7 | 7.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 33.7 | 37.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 16.2 | 3.8 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 43.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.0 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 24.7 | 4.0 | 0.0 |
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

- `register` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **205.3** | LOC: 395
  * *Intent:* /** * This compound extension consists of an include processor, a tree processor, and a post processor. * It automatically links listing and literal b...
- `intercept` (@ `spock-core/src/main/java/org/spockframework/runtime/extension/AbstractMethodInterceptor.java`) -> Impact: **108.0** | LOC: 43
  * *Intent:* /* * Copyright 2009 the original author or authors. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file ex...
- `writeString` (@ `spock-core/src/main/java/org/spockframework/util/JsonWriter.java`) -> Impact: **104.3** | LOC: 74
- `filterForTags` (@ `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`) -> Impact: **102.0** | LOC: 136
- `respond` (@ `spock-core/src/main/java/org/spockframework/mock/EmptyOrDummyResponse.java`) -> Impact: **98.7** | LOC: 70
- `matchesSnapshot` (@ `spock-core/src/main/java/spock/lang/Snapshotter.java`) -> Impact: **97.5** | LOC: 205
- `setCall` (@ `spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java`) -> Impact: **73.2** | LOC: 144
- `visitCleanupBlock` (@ `spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java`) -> Impact: **71.8** | LOC: 114
- `evaluateExpression` (@ `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/UnrollIterationNameProvider.java`) -> Impact: **62.5** | LOC: 50
- `verify` (@ `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`) -> Impact: **61.3** | LOC: 62

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `spock-core/src/main/java/org/spockframework/runtime` | 82 | 5667.64 | 19.13% | 55.79% |
| `config` | 1 | 5000.0 | 0.0% | 0.0% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/mock` | 62 | 3622.84 | 14.6% | 0.0% |
| `spock-core/src/main/java/org/spockframework/compiler` | 26 | 3051.46 | 16.16% | 75.89% |
| `spock-core/src/main/java/org/spockframework/util` | 50 | 2590.34 | 11.9% | 44.17% |
| `spock-specs/src/test/groovy/org/spockframework/smoke/extension` | 37 | 2434.36 | 14.23% | 0.0% |
| `spock-core/src/main/java/org/spockframework/mock/runtime` | 44 | 2339.74 | 15.93% | 55.39% |
| `spock-core/src/main/java/org/spockframework/runtime/extension/builtin` | 53 | 2190.28 | 17.05% | 33.92% |
| `spock-core/src/main/java/org/spockframework/runtime/model` | 40 | 2009.51 | 9.48% | 20.99% |
| `spock-core/src/main/groovy/spock/util` | 3 | 1758.3 | 13.66% | 100.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `allVariants` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/builder/PojoBuilder.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/buildsupport/EmptyAnnotationVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/buildsupport/SpecClassFileVisitor.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/compiler/AbstractDeepBlockRewriter.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/AbstractMultiset.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/CollectionUtil.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/Filter.java` -> **100.0%** Exposure
- `spock-core/src/main/java/org/spockframework/util/HashMultiset.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` -> **46** Orphaned Functions | **91** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` -> **3** Orphaned Functions | **87** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/verifyall/VerifyAllSpecification.groovy` -> **1** Orphaned Functions | **60** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionEvaluation.groovy` -> **1** Orphaned Functions | **57** Duplicates
- `spock-specs/src/test/groovy/org/spockframework/smoke/condition/ConditionRendering.groovy` -> **1** Orphaned Functions | **57** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy`** -> AI Confidence: **99.48%**
2. **`build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java`** -> AI Confidence: **99.31%**
3. **`spock-core/src/main/java/org/spockframework/runtime/ExtensionRunner.java`** -> AI Confidence: **99.31%**
4. **`spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureNode.java`** -> AI Confidence: **99.31%**
5. **`spock-core/src/main/java/org/spockframework/runtime/SpecInfoBuilder.java`** -> AI Confidence: **99.31%**
6. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirExtension.java`** -> AI Confidence: **99.31%**
7. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TimeoutInterceptor.java`** -> AI Confidence: **99.31%**
8. **`spock-core/src/main/java/org/spockframework/util/ReflectionUtil.java`** -> AI Confidence: **99.31%**
9. **`allVariants`** -> AI Confidence: **99.29%**
10. **`spock-groovy2-compat/groovy2-compat.gradle`** -> AI Confidence: **99.29%**
11. **`spock-guice/guice.gradle`** -> AI Confidence: **99.29%**
12. **`spock-junit4/junit4.gradle`** -> AI Confidence: **99.29%**
13. **`spock-specs/specs.gradle`** -> AI Confidence: **99.29%**
14. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/AstSpec/groovy_3_language_features.groovy`** -> AI Confidence: **99.29%**
15. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod-[1].groovy`** -> AI Confidence: **99.29%**
16. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_with_exception-[1].groovy`** -> AI Confidence: **99.29%**
17. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod-[0].groovy`** -> AI Confidence: **99.29%**
18. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod-[1].groovy`** -> AI Confidence: **99.29%**
19. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod-[2].groovy`** -> AI Confidence: **99.29%**
20. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_exception-[0].groovy`** -> AI Confidence: **99.29%**
21. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_exception-[1].groovy`** -> AI Confidence: **99.29%**
22. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_exception-[2].groovy`** -> AI Confidence: **99.29%**
23. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_only_exception-[0].groovy`** -> AI Confidence: **99.29%**
24. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_only_exception-[1].groovy`** -> AI Confidence: **99.29%**
25. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_within_condition_method__conditionMethod_with_only_exception-[2].groovy`** -> AI Confidence: **99.29%**
26. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/VerifyAllMethodsAstSpec/interactions_are_illegal_in_verify_methods.groovy`** -> AI Confidence: **99.29%**
27. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/VerifyMethodsAstSpec/interactions_are_illegal_in_verify_methods.groovy`** -> AI Confidence: **99.29%**
28. **`spock-core/src/main/java/org/spockframework/compiler/DeepBlockRewriter.java`** -> AI Confidence: **99.24%**
29. **`spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java`** -> AI Confidence: **99.24%**
30. **`spock-core/src/main/java/org/spockframework/compiler/SpecParser.java`** -> AI Confidence: **99.24%**
31. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockController.java`** -> AI Confidence: **99.24%**
32. **`spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java`** -> AI Confidence: **99.24%**
33. **`spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java`** -> AI Confidence: **99.24%**
34. **`spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java`** -> AI Confidence: **99.24%**
35. **`spock-core/src/main/java/org/spockframework/runtime/SpockNode.java`** -> AI Confidence: **99.24%**
36. **`spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java`** -> AI Confidence: **99.24%**
37. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RepeatUntilFailureExtension.java`** -> AI Confidence: **99.24%**
38. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryBaseInterceptor.java`** -> AI Confidence: **99.24%**
39. **`spock-junit4/src/main/java/org/spockframework/junit4/JUnit4AnnotationLifecycleMethodsExtension.java`** -> AI Confidence: **99.24%**
40. **`spock-specs/src/test/groovy/org/spockframework/smoke/mock/InvokingMocksFromMultipleThreads.groovy`** -> AI Confidence: **99.24%**
41. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockInteraction.java`** -> AI Confidence: **99.23%**
42. **`spock-core/src/main/java/org/spockframework/runtime/FeatureNode.java`** -> AI Confidence: **99.23%**
43. **`spock-core/src/main/java/org/spockframework/runtime/StackTraceFilter.java`** -> AI Confidence: **99.23%**
44. **`spock-core/src/main/java/org/spockframework/util/RenderUtil.java`** -> AI Confidence: **99.23%**
45. **`spock-core/src/main/java/org/spockframework/runtime/condition/EditPathRenderer.java`** -> AI Confidence: **99.2%**
46. **`spock-core/src/main/java/org/spockframework/util/JsonWriter.java`** -> AI Confidence: **99.2%**
47. **`spock-core/src/main/java/org/spockframework/compiler/AstUtil.java`** -> AI Confidence: **99.18%**
48. **`spock-core/src/main/java/org/spockframework/compiler/SpockTransform.java`** -> AI Confidence: **99.18%**
49. **`spock-core/src/main/java/org/spockframework/compiler/condition/BaseVerifyMethodTransform.java`** -> AI Confidence: **99.18%**
50. **`spock-core/src/main/java/org/spockframework/mock/runtime/IMockMaker.java`** -> AI Confidence: **99.18%**
51. **`spock-core/src/main/java/org/spockframework/mock/runtime/JavaMockFactory.java`** -> AI Confidence: **99.18%**
52. **`spock-core/src/main/java/org/spockframework/mock/runtime/JavaProxyMockMaker.java`** -> AI Confidence: **99.18%**
53. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockCreationSettings.java`** -> AI Confidence: **99.18%**
54. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockObject.java`** -> AI Confidence: **99.18%**
55. **`spock-core/src/main/java/org/spockframework/runtime/ClassSelectorResolver.java`** -> AI Confidence: **99.18%**
56. **`spock-core/src/main/java/org/spockframework/runtime/RunContext.java`** -> AI Confidence: **99.18%**
57. **`spock-core/src/main/java/org/spockframework/runtime/extension/IStore.java`** -> AI Confidence: **99.18%**
58. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/GlobalTimeoutExtension.java`** -> AI Confidence: **99.18%**
59. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java`** -> AI Confidence: **99.18%**
60. **`spock-core/src/main/java/org/spockframework/runtime/model/MethodInfo.java`** -> AI Confidence: **99.18%**
61. **`spock-core/src/main/java/spock/lang/Snapshot.java`** -> AI Confidence: **99.18%**
62. **`spock-core/src/main/java/spock/lang/Specification.java`** -> AI Confidence: **99.18%**
63. **`spock-core/src/main/java/spock/util/io/FileSystemFixture.java`** -> AI Confidence: **99.18%**
64. **`spock-spring/src/main/java/org/spockframework/spring/SpringMockTestExecutionListener.java`** -> AI Confidence: **99.18%**
65. **`spock-spring/src/main/java/org/spockframework/spring/mock/DelegatingInterceptor.java`** -> AI Confidence: **99.18%**
66. **`spock-spring/src/main/java/org/spockframework/spring/mock/QualifierDefinition.java`** -> AI Confidence: **99.18%**
67. **`spock-spring/src/main/java/org/spockframework/spring/mock/SpockDefinition.java`** -> AI Confidence: **99.18%**
68. **`build-logic/preprocess-workflows/src/main/groovy/org/spockframework/gradle/PreprocessGithubWorkflowWorkAction.groovy`** -> AI Confidence: **99.18%**
69. **`spock-specs/src/test/groovy/org/spockframework/smoke/Interceptors.groovy`** -> AI Confidence: **99.18%**
70. **`spock-specs/src/test/groovy/org/spockframework/smoke/ast/AstSpec.groovy`** -> AI Confidence: **99.18%**
71. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/ExceptionConditions.groovy`** -> AI Confidence: **99.18%**
72. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/InvalidConditions.groovy`** -> AI Confidence: **99.18%**
73. **`spock-specs/src/test/groovy/org/spockframework/smoke/condition/IsRenderedExtension.groovy`** -> AI Confidence: **99.18%**
74. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureExtensionSpec.groovy`** -> AI Confidence: **99.18%**
75. **`spock-specs/src/test/groovy/org/spockframework/smoke/extension/TimeoutExtension.groovy`** -> AI Confidence: **99.18%**
76. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy`** -> AI Confidence: **99.18%**
77. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/MethodParameters.groovy`** -> AI Confidence: **99.18%**
78. **`spock-specs/src/test/groovy/spock/util/concurrent/PollingConditionsSpec.groovy`** -> AI Confidence: **99.18%**
79. **`spock-spring/src/test/groovy/org/spockframework/spring/SharedFieldsInjection.groovy`** -> AI Confidence: **99.18%**
80. **`spock-spring/src/test/groovy/org/spockframework/spring/TransactionalGroovySqlExample.groovy`** -> AI Confidence: **99.18%**
81. **`settings.gradle`** -> AI Confidence: **99.17%**
82. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod-[0].groovy`** -> AI Confidence: **99.17%**
83. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod-[2].groovy`** -> AI Confidence: **99.17%**
84. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_with_exception-[0].groovy`** -> AI Confidence: **99.17%**
85. **`spock-specs/src/test/resources/snapshots/org/spockframework/smoke/ast/condition/ConditionMethodsAstSpec/condition_method__conditionMethod_with_exception-[2].groovy`** -> AI Confidence: **99.17%**
86. **`spock-core/src/main/java/org/spockframework/compiler/SpecAnnotator.java`** -> AI Confidence: **99.16%**
87. **`spock-core/src/main/java/org/spockframework/compiler/SpecRewriter.java`** -> AI Confidence: **99.16%**
88. **`spock-core/src/main/java/org/spockframework/compiler/SpecialMethodCall.java`** -> AI Confidence: **99.16%**
89. **`spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java`** -> AI Confidence: **99.16%**
90. **`spock-core/src/main/java/org/spockframework/mock/ClosureParameterTypeFromVariableType.java`** -> AI Confidence: **99.16%**
91. **`spock-core/src/main/java/org/spockframework/mock/EmptyOrDummyResponse.java`** -> AI Confidence: **99.16%**
92. **`spock-core/src/main/java/org/spockframework/mock/runtime/ByteBuddyMockInteractionValidator.java`** -> AI Confidence: **99.16%**
93. **`spock-core/src/main/java/org/spockframework/mock/runtime/CglibMockFactory.java`** -> AI Confidence: **99.16%**
94. **`spock-core/src/main/java/org/spockframework/mock/runtime/GroovyMockFactory.java`** -> AI Confidence: **99.16%**
95. **`spock-core/src/main/java/org/spockframework/mock/runtime/MockMakerRegistry.java`** -> AI Confidence: **99.16%**
96. **`spock-core/src/main/java/org/spockframework/mock/runtime/mockito/MockitoMockMakerImpl.java`** -> AI Confidence: **99.16%**
97. **`spock-core/src/main/java/org/spockframework/runtime/GroovyRuntimeUtil.java`** -> AI Confidence: **99.16%**
98. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ConditionalExtension.java`** -> AI Confidence: **99.16%**
99. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/IgnoreIfExtension.java`** -> AI Confidence: **99.16%**
100. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RequiresExtension.java`** -> AI Confidence: **99.16%**
101. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TempDirInterceptor.java`** -> AI Confidence: **99.16%**
102. **`spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java`** -> AI Confidence: **99.16%**
103. **`spock-core/src/main/java/spock/lang/Snapshotter.java`** -> AI Confidence: **99.16%**
104. **`spock-spring/src/main/java/org/spockframework/spring/SpringExtension.java`** -> AI Confidence: **99.16%**
105. **`spock-spring/src/main/java/org/spockframework/spring/mock/SpockMockPostprocessor.java`** -> AI Confidence: **99.16%**
106. **`build-logic/preprocess-workflows/src/main/groovy/org/spockframework/gradle/DetermineImportedFilesWorkAction.groovy`** -> AI Confidence: **99.16%**
107. **`spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/ParameterizedFeatureNodeStatuses.groovy`** -> AI Confidence: **99.16%**
108. **`spock-core/src/main/java/org/spockframework/mock/runtime/GroovyRealGetPropertyInvoker.java`** -> AI Confidence: **99.15%**
109. **`spock-core/src/main/java/org/spockframework/mock/runtime/GroovyRealSetPropertyInvoker.java`** -> AI Confidence: **99.15%**
110. **`spock-core/src/main/java/org/spockframework/mock/runtime/InteractionBuilder.java`** -> AI Confidence: **99.15%**
111. **`spock-core/src/main/java/org/spockframework/runtime/ConfigurationScriptLoader.java`** -> AI Confidence: **99.15%**
112. **`spock-core/src/main/java/org/spockframework/runtime/MethodSelectorResolver.java`** -> AI Confidence: **99.15%**
113. **`spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureChildExecutor.java`** -> AI Confidence: **99.15%**
114. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/StepwiseExtension.java`** -> AI Confidence: **99.15%**
115. **`spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TagExtension.java`** -> AI Confidence: **99.15%**
116. **`spock-core/src/main/java/org/spockframework/util/GenericTypeReflectorUtil.java`** -> AI Confidence: **99.15%**
117. **`spock-core/src/main/java/spock/lang/Retry.java`** -> AI Confidence: **99.15%**
118. **`spock-guice/src/main/java/org/spockframework/guice/GuiceInterceptor.java`** -> AI Confidence: **99.15%**
119. **`spock-tapestry/src/main/java/org/spockframework/tapestry/TapestryInterceptor.java`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4648` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `spock-core/src/main/java/org/spockframework/runtime/ParameterizedFeatureChildExecutor.java` (JAVA) -> Cumulative Risk: **735.04**
- **Archetype:** `file_cluster_4` (Distance: 11.18 IQR)
- **Magnitude:** 143.38 | **LOC:** 120 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9934%)
- **Heaviest Functions:** `ParameterizedFeatureChildExecutor` (Impact: 37.5), `executionFinished` (Impact: 19.9), `executionFinished` (Impact: 9.1)

### 2. `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/PendingFeatureIterationInterceptor.java` (JAVA) -> Cumulative Risk: **710.82**
- **Archetype:** `file_cluster_4` (Distance: 12.493 IQR)
- **Magnitude:** 188.02 | **LOC:** 97 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9704%), Tech Debt (98.3356%)
- **Heaviest Functions:** `intercept` (Impact: 26.1), `intercept` (Impact: 16.0), `InnerIterationInterceptor` (Impact: 6.2)

### 3. `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` (JAVA) -> Cumulative Risk: **619.4**
- **Archetype:** `file_cluster_0` (Distance: 10.84 IQR)
- **Magnitude:** 295.58 | **LOC:** 419 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9984%), State Flux (99.7752%), Documentation (98.1606%)
- **Heaviest Functions:** `replaceExpr` (Impact: 7.1), `replaceAllExprs` (Impact: 6.3), `visitArrayExpression` (Impact: 5.2)

### 4. `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java` (JAVA) -> Cumulative Risk: **612.6**
- **Archetype:** `file_cluster_4` (Distance: 11.553 IQR)
- **Magnitude:** 99.7 | **LOC:** 124 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9806%), Tech Debt (99.9693%), State Flux (99.9648%)
- **Heaviest Functions:** `intercept` (Impact: 15.4), `intercept` (Impact: 12.9), `addInterceptorToFeatureMethod` (Impact: 5.9)

### 5. `spock-core/src/main/java/org/spockframework/runtime/SimpleFeatureNode.java` (JAVA) -> Cumulative Risk: **592.71**
- **Archetype:** `file_cluster_4` (Distance: 9.76 IQR)
- **Magnitude:** 54.42 | **LOC:** 67 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (98.2394%), Documentation (85.0803%)
- **Heaviest Functions:** `execute` (Impact: 8.2), `executionFinished` (Impact: 5.4), `prepare` (Impact: 2.7)

### 6. `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` (JAVA) -> Cumulative Risk: **589.68**
- **Archetype:** `file_cluster_13` (Distance: 11.882 IQR)
- **Magnitude:** 246.86 | **LOC:** 402 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.5755%), Tech Debt (98.5606%), State Flux (90.5824%)
- **Heaviest Functions:** `getAssertionMessage` (Impact: 13.6), `getAnnotation` (Impact: 10.9), `isDynamicTypedExpression` (Impact: 10.4)

### 7. `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA) -> Cumulative Risk: **588.95**
- **Archetype:** `file_cluster_8` (Distance: 11.641 IQR)
- **Magnitude:** 365.18 | **LOC:** 454 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.8747%), Safety Score (91.4628%)
- **Heaviest Functions:** `invoke` (Impact: 24.2), `runIterationCleanups` (Impact: 11.7), `createMethodInfoForDoRunInitializer` (Impact: 11.2)

### 8. `spock-core/src/main/java/org/spockframework/runtime/model/MethodInfo.java` (JAVA) -> Cumulative Risk: **587.82**
- **Archetype:** `file_cluster_13` (Distance: 10.706 IQR)
- **Magnitude:** 111.46 | **LOC:** 171 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.149%), Tech Debt (97.9284%), State Flux (97.5913%)
- **Heaviest Functions:** `invoke` (Impact: 14.7), `getNameProvider` (Impact: 7.6), `getParameters` (Impact: 6.6)

### 9. `spock-core/src/main/java/org/spockframework/runtime/SpockExecutionContext.java` (JAVA) -> Cumulative Risk: **580.39**
- **Archetype:** `file_cluster_8` (Distance: 10.259 IQR)
- **Magnitude:** 128.48 | **LOC:** 196 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), Documentation (98.5131%), State Flux (97.9541%)
- **Heaviest Functions:** `clone` (Impact: 7.1), `setRunContext` (Impact: 2.4), `setRunner` (Impact: 2.4)

### 10. `spock-core/src/main/java/org/spockframework/mock/runtime/InteractionBuilder.java` (JAVA) -> Cumulative Risk: **573.4**
- **Archetype:** `file_cluster_8` (Distance: 11.504 IQR)
- **Magnitude:** 182.04 | **LOC:** 201 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.8666%), State Flux (99.213%), Verification (80.0%)
- **Heaviest Functions:** `setRangeCount` (Impact: 12.3), `addEqualArg` (Impact: 11.5), `convertCount` (Impact: 7.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `config/code-signing-secring.gpg` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `spock-core/src/main/groovy/spock/util/SourceToAstNodeAndSourceTranspiler.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.939 IQR)
- **Top Global Matches:** file_cluster_8: 11.939, file_cluster_0: 12.074, file_cluster_13: 12.267
- **Magnitude:** 1510.04 | **LOC:** 1381 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.7649%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visitClass` (Impact: 41.2)
  * `visitAllImports` (Impact: 39.5)
  * `visitPropertyExpression` (Impact: 34.3)
  * `visitMethod` (Impact: 29.3)
  * `visitIfElse` (Impact: 25.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 72`, `args: 245`, `func_start: 237`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 79`, `duplicate_logic: 91`, `orphaned_logic: 46`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 23`, `doc: 24`, `sync_locks: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.codehaus.groovy.ast.stmt.*, org.intellij.lang.annotations.Language, org.objectweb.asm.AnnotationVisitor, org.objectweb.asm.FieldVisitor, java.security.CodeSource, java.util.Collections.disjoint, org.spockframework.compat.groovy2.GroovyCodeVisitorCompat, org.objectweb.asm.Opcodes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.47 IQR)
- **Top Global Matches:** file_cluster_8: 9.47, file_cluster_7: 10.215, file_cluster_1: 10.446
- **Magnitude:** 535.66 | **LOC:** 2144 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.7105%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 23.9)
  * `def` (Impact: 7.5)
  * `def` (Impact: 7.2)
  * `def` (Impact: 6.5)
  * `GroovySpy` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 171`, `args: 228`, `func_start: 228`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 100`, `duplicate_logic: 87`, `orphaned_logic: 3`
* *Architecture:* `api: 70`, `import: 5`
* *Defense:* `safety: 4`, `doc: 1`, `test: 453`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` java.util.regex.Pattern, spock.lang.*, java.lang.reflect.Modifier, spock.util.environment.Jvm, org.spockframework.runtime.GroovyRuntimeUtil
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/DataIteratorFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.539 IQR)
- **Top Global Matches:** file_cluster_0: 10.539, file_cluster_8: 10.674, file_cluster_16: 10.737
- **Magnitude:** 531.42 | **LOC:** 998 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2913%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 34.3)
  * `next` (Impact: 28.8)
  * `createDataProviderIterators` (Impact: 26.6)
  * `next` (Impact: 21.9)
    * *Intent:* // no iterators => no data providers => only derived parameterizations => limit to one iteration
  * `createDataProviders` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 182`, `args: 60`, `func_start: 70`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 15`, `dead_code: 2`, `duplicate_logic: 38`, `orphaned_logic: 2`
* *Architecture:* `api: 52`, `import: 10`
* *Defense:* `safety: 39`, `doc: 36`, `immutability_locks: 32`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.Collections.singletonList, java.util.Collections.emptyIterator, java.util.*, org.jetbrains.annotations.NotNull, org.spockframework.runtime.GroovyRuntimeUtil.closeQuietly, java.util.stream.Collectors.toList, org.spockframework.runtime.model.*, spock.config.RunnerConfiguration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build-logic/asciidoc-extensions/src/main/java/org/spockframework/plugins/asciidoctor/IncludedSourceLinker.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.105 IQR)
- **Top Global Matches:** file_cluster_13: 15.105, file_cluster_17: 15.132, file_cluster_11: 15.141
- **Magnitude:** 473.32 | **LOC:** 713 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.4012%), Tech Debt (99.9956%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 205.3)
    * *Intent:* /** * This compound extension consists of an include processor, a tree processor, and a post process...
  * `filterForTags` (Impact: 102.0)
  * `determineTagsToFilterFor` (Impact: 22.6)
  * `processBlocks` (Impact: 22.1)
  * `process` (Impact: 14.5)
    * *Intent:* * <p>Currently, only the {@code tag}, {@code tags}, {@code lines}, and {@code indent} attributes on ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 58`, `args: 31`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 28`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 7`, `import: 16`
* *Defense:* `safety: 3`, `doc: 39`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.lang.String.format, java.nio.charset.StandardCharsets.UTF_8, java.util.regex.Matcher, java.util.stream.Stream, org.asciidoctor.log.Severity.WARN, org.asciidoctor.extension.Contexts.LITERAL, java.nio.file.Files.readString, java.nio.file.Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/model/SpecInfo.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.854 IQR)
- **Top Global Matches:** file_cluster_16: 10.854, file_cluster_13: 11.04, file_cluster_8: 11.16
- **Magnitude:** 425.66 | **LOC:** 422 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.3591%), Tech Debt (28.8526%)
**Top Internal Functions/Classes:**
  * `getSpecsTopToBottom` (Impact: 12.3)
  * `getSpecsBottomToTop` (Impact: 12.3)
  * `filterFeatures` (Impact: 10.1)
  * `toFeatureName` (Impact: 10.1)
  * `isInitializerOrFixtureMethod` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 111`, `args: 90`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`, `duplicate_logic: 2`
* *Architecture:* `api: 123`, `import: 13`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.121
  * `Choke Point (Betweenness):` 0.004675 | `Ripple Effect (Closeness):` 0.114779
  * `Imports (Out-Degree: 9):` org.spockframework.runtime.model.parallel.ExclusiveResource, java.util.function.Supplier, java.util.function.BiConsumer, java.util.*, org.spockframework.runtime.IFeatureFilter, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.runtime.model.parallel.ExecutionMode, org.spockframework.runtime.IMethodNameMapper...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.559 IQR)
- **Top Global Matches:** file_cluster_16: 9.559, file_cluster_8: 10.149, file_cluster_13: 10.332
- **Magnitude:** 389.28 | **LOC:** 354 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.8488%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createMockImpl` (Impact: 25.7)
  * `thrownImpl` (Impact: 11.3)
  * `checkExceptionThrown` (Impact: 11.2)
  * `GroovySpyImpl` (Impact: 10.2)
  * `createMock` (Impact: 9.4)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 104`, `args: 65`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 71`, `planned_debt: 16`, `duplicate_logic: 53`
* *Architecture:* `api: 60`, `import: 10`
* *Defense:* `doc: 2`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0018
  * `Imports (Out-Degree: 2):` org.spockframework.mock.*, groovy.transform.stc.ThirdParam, spock.lang.Specification, spock.mock.IMockMakerSettings, java.util.*, org.spockframework.util.ObjectUtil.uncheckedCast, groovy.transform.stc.SecondParam, org.spockframework.util.*...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/runtime/PlatformSpecRunner.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.641 IQR)
- **Top Global Matches:** file_cluster_8: 11.641, file_cluster_13: 11.704, file_cluster_17: 11.754
- **Magnitude:** 365.18 | **LOC:** 454 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.3096%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `invoke` (Impact: 24.2)
  * `runIterationCleanups` (Impact: 11.7)
  * `createMethodInfoForDoRunInitializer` (Impact: 11.2)
  * `createMethodInfoForDoRunSetup` (Impact: 11.2)
  * `createMethodInfoForDoRunCleanup` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 105`, `args: 64`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 85`, `duplicate_logic: 22`, `orphaned_logic: 9`
* *Architecture:* `api: 12`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` spock.lang.Specification, java.util.Collections, java.lang.System.arraycopy, org.spockframework.runtime.extension.IMethodInterceptor, java.util.Arrays.copyOfRange, org.spockframework.runtime.model.*, org.spockframework.runtime.model.MethodInfo.MISSING_ARGUMENT, java.util.List...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/InvalidWhereBlocks.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.945 IQR)
- **Top Global Matches:** file_cluster_8: 8.945, file_cluster_7: 9.825, file_cluster_1: 9.994
- **Magnitude:** 359.92 | **LOC:** 898 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 17.7)
  * `def` (Impact: 16.8)
  * `def` (Impact: 13.3)
  * `def` (Impact: 12.4)
  * `def` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 99`, `args: 62`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `duplicate_logic: 48`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `doc: 1`, `test: 207`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.opentest4j.MultipleFailuresError, spock.lang.Snapshot, spock.lang.Snapshotter, org.spockframework.runtime.SpockExecutionException, org.codehaus.groovy.syntax.SyntaxException, org.spockframework.EmbeddedSpecification, org.spockframework.compiler.InvalidSpecCompileException, spock.lang.Issue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/parameterization/ParameterizedFeatureNodeStatuses.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.967 IQR)
- **Top Global Matches:** file_cluster_8: 8.967, file_cluster_7: 9.889, file_cluster_13: 9.981
- **Magnitude:** 349.2 | **LOC:** 892 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 14.7)
  * `def` (Impact: 13.3)
  * `def` (Impact: 13.2)
  * `def` (Impact: 13.1)
  * `def` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 89`, `args: 76`, `func_start: 76`, `class_start: 4`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 49`, `orphaned_logic: 1`
* *Architecture:* `import: 19`
* *Defense:* `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` org.spockframework.runtime.SpockComparisonFailure, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.runtime.model.ErrorInfo, org.opentest4j.TestAbortedException, org.opentest4j.*, java.lang.annotation.ElementType, org.spockframework.EmbeddedSpecification, java.lang.annotation.Target...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/mock/TooFewInvocations.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.939 IQR)
- **Top Global Matches:** file_cluster_8: 8.939, file_cluster_7: 9.838, file_cluster_1: 10.0
- **Magnitude:** 336.76 | **LOC:** 1225 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.9414%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 19.9)
  * `def` (Impact: 17.8)
    * *Intent:* /* * Copyright 2012 the original author or authors. * * Licensed under the Apache License, Version 2...
  * `def` (Impact: 16.5)
  * `def` (Impact: 15.6)
  * `def` (Impact: 15.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 145`, `args: 102`, `func_start: 98`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`, `planned_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `import: 4`
* *Defense:* `safety: 5`, `test: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.spockframework.EmbeddedSpecification, org.spockframework.mock.TooFewInvocationsError, java.util.regex.Pattern, org.hamcrest.CoreMatchers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/spock/lang/Snapshotter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.632 IQR)
- **Top Global Matches:** file_cluster_13: 10.632, file_cluster_0: 10.928, file_cluster_8: 10.961
- **Magnitude:** 311.38 | **LOC:** 366 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.1755%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `matchesSnapshot` (Impact: 97.5)
  * `unwrap` (Impact: 15.9)
  * `calculateSafeUniqueName` (Impact: 14.8)
  * `loadSnapshot` (Impact: 14.0)
  * `matchesSnapshot` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 69`, `args: 59`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 6`, `duplicate_logic: 21`
* *Architecture:* `io: 11`, `api: 37`, `import: 21`
* *Defense:* `safety: 14`, `doc: 12`, `test: 1`, `sync_locks: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.059
  * `Choke Point (Betweenness):` 0.000248 | `Ripple Effect (Closeness):` 0.009697
  * `Imports (Out-Degree: 9):` org.codehaus.groovy.runtime.StringGroovyMethods, org.spockframework.util.Checks, java.nio.file.Path, org.spockframework.util.IoUtil, org.spockframework.runtime.model.FeatureInfo, java.util.Objects, java.io.UncheckedIOException, java.io.IOException...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureExtensionSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.512 IQR)
- **Top Global Matches:** file_cluster_8: 9.512, file_cluster_7: 10.349, file_cluster_0: 10.363
- **Magnitude:** 307.96 | **LOC:** 729 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 19.4)
  * `def` (Impact: 19.2)
  * `def` (Impact: 19.2)
  * `def` (Impact: 18.5)
  * `def` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 91`, `args: 158`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 55`, `orphaned_logic: 1`
* *Architecture:* `import: 9`
* *Defense:* `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.junit.platform.testkit.engine.EventConditions.finishedWithFailure, org.assertj.core.api.Condition, org.junit.platform.testkit.engine.TestExecutionResultConditions.cause, org.opentest4j.TestAbortedException, org.opentest4j.MultipleFailuresError, org.junit.platform.testkit.engine.TestExecutionResultConditions.message, org.junit.platform.testkit.engine.EventConditions.abortedWithReason, org.junit.platform.testkit.engine.TestExecutionResultConditions.instanceOf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.981 IQR)
- **Top Global Matches:** file_cluster_17: 10.981, file_cluster_13: 11.188, file_cluster_0: 11.313
- **Magnitude:** 306.78 | **LOC:** 984 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.7078%), Tech Debt (99.4579%)
**Top Internal Functions/Classes:**
  * `rewriteWhereStat` (Impact: 29.2)
  * `rewrite` (Impact: 25.5)
  * `handleFeatureParameters` (Impact: 15.3)
  * `createDataProcessorAnnotation` (Impact: 14.7)
  * `createFilterMethod` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 132`, `args: 51`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 47`, `dead_code: 2`, `duplicate_logic: 10`, `orphaned_logic: 5`
* *Architecture:* `io: 12`, `api: 8`, `import: 13`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.util.stream.Collectors.*, org.spockframework.compiler.model.WhereBlock, org.codehaus.groovy.ast.stmt.*, org.spockframework.runtime.model.DataProcessorMetadata, org.codehaus.groovy.syntax.*, org.objectweb.asm.Opcodes, org.spockframework.util.*, org.codehaus.groovy.ast.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.158 IQR)
- **Top Global Matches:** file_cluster_16: 11.158, file_cluster_0: 11.172, file_cluster_13: 11.279
- **Magnitude:** 297.0 | **LOC:** 445 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.3522%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasBytecodeName` (Impact: 18.3)
    * *Intent:* /** * Returns the features this feature implies. * All features are within the same specification hi...
  * `addImpliedFeature` (Impact: 13.0)
  * `addScopedMethodInterceptor` (Impact: 3.9)
    * *Intent:* /** * @since 2.4
  * `addSetupInterceptor` (Impact: 2.6)
  * `addCleanupInterceptor` (Impact: 2.6)
    * *Intent:* /** * @since 2.4 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 91`, `args: 56`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 30`
* *Architecture:* `api: 107`, `import: 9`
* *Defense:* `safety: 2`, `doc: 32`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.706
  * `Choke Point (Betweenness):` 0.003977 | `Ripple Effect (Closeness):` 0.11592
  * `Imports (Out-Degree: 8):` org.spockframework.runtime.model.parallel.ExclusiveResource, java.util.*, org.spockframework.runtime.extension.IMethodInterceptor, org.spockframework.util.Checks, org.spockframework.runtime.model.parallel.ExecutionMode, org.spockframework.runtime.extension.IBlockListener, org.spockframework.runtime.extension.IDataDriver, java.lang.reflect.AnnotatedElement...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/compiler/ExpressionReplacingVisitorSupport.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.84 IQR)
- **Top Global Matches:** file_cluster_0: 10.84, file_cluster_8: 11.105, file_cluster_13: 11.487
- **Magnitude:** 295.58 | **LOC:** 419 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3246%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `replaceExpr` (Impact: 7.1)
    * *Intent:* * Copyright 2009 the original author or authors. * * Licensed under the Apache License, Version 2.0 ...
  * `replaceAllExprs` (Impact: 6.3)
  * `visitArrayExpression` (Impact: 5.2)
  * `visitPropertyExpression` (Impact: 3.1)
  * `visitTryCatchFinally` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 81`, `args: 55`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 72`, `orphaned_logic: 46`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.codehaus.groovy.ast.expr.*, java.util.List, java.util.ListIterator, org.codehaus.groovy.ast.stmt.*, org.codehaus.groovy.classgen.BytecodeExpression
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/ConditionRewriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.46 IQR)
- **Top Global Matches:** file_cluster_0: 10.46, file_cluster_13: 10.588, file_cluster_8: 10.822
- **Magnitude:** 292.98 | **LOC:** 868 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.4046%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `extractVariableNumber` (Impact: 18.7)
  * `visitMapExpression` (Impact: 14.0)
  * `rewriteToSpockRuntimeCall` (Impact: 13.4)
    * *Intent:* // used in the following places: // - LHS of multi-assignment // - wraps NamedArgumentListExpression...
  * `surroundWithTryCatch` (Impact: 12.6)
  * `unrecord` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 176`, `args: 43`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 49`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 28`
* *Architecture:* `io: 8`, `api: 29`, `import: 23`
* *Defense:* `safety: 10`, `doc: 1`, `sync_locks: 9`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` java.util.Collections.singletonList, org.spockframework.util.Identifiers, org.spockframework.util.AbstractExpressionConverter, java.util.Arrays.asList, org.codehaus.groovy.ast.Parameter, org.codehaus.groovy.ast.stmt.*, org.spockframework.compat.groovy2.GroovyCodeVisitorCompat, org.spockframework.compiler.AstUtil.createDirectMethodCall...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.042 IQR)
- **Top Global Matches:** file_cluster_8: 11.042, file_cluster_13: 11.065, file_cluster_0: 11.109
- **Magnitude:** 262.02 | **LOC:** 396 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.0607%), Tech Debt (99.9773%)
**Top Internal Functions/Classes:**
  * `setCall` (Impact: 73.2)
  * `addArgs` (Impact: 20.8)
  * `parseCall` (Impact: 19.9)
  * `addArg` (Impact: 14.9)
  * `addResponses` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 68`, `args: 22`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 19`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 2`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 21`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.codehaus.groovy.ast.expr.*, java.util.*, org.spockframework.util.*, org.codehaus.groovy.ast.*, org.codehaus.groovy.syntax.Types, org.spockframework.compiler.AstUtil.createDirectMethodCall, org.spockframework.lang.Wildcard, java.util.Arrays.asList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/SpockRuntime.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.286 IQR)
- **Top Global Matches:** file_cluster_13: 10.286, file_cluster_0: 10.704, file_cluster_8: 10.745
- **Magnitude:** 247.98 | **LOC:** 448 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (20.344%), Tech Debt (72.3163%)
**Top Internal Functions/Classes:**
  * `verify` (Impact: 61.3)
  * `conditionFailedWithException` (Impact: 24.0)
  * `replaceMatcherValues` (Impact: 16.9)
  * `parse` (Impact: 16.5)
  * `verify` (Impact: 13.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 91`, `args: 26`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 23`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `import: 24`
* *Defense:* `safety: 9`, `doc: 2`, `test: 2`, `sync_locks: 12`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` org.spockframework.runtime.extension.IBlockListener, groovy.lang.DelegatesTo, org.codehaus.groovy.runtime.InvokerHelper, groovy.lang.Closure, org.spockframework.util.ReflectionUtil.isArray, java.util.stream.Collectors.toList, org.spockframework.util.Nullable, org.spockframework.util.CollectionUtil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.882 IQR)
- **Top Global Matches:** file_cluster_13: 11.882, file_cluster_0: 12.068, file_cluster_8: 12.26
- **Magnitude:** 246.86 | **LOC:** 402 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0057%), Tech Debt (98.5606%)
**Top Internal Functions/Classes:**
  * `getAssertionMessage` (Impact: 13.6)
  * `getAnnotation` (Impact: 10.9)
  * `isDynamicTypedExpression` (Impact: 10.4)
  * `isJavaIdentifier` (Impact: 10.3)
    * *Intent:* /** * Tells whether the given node has an annotation of the given type. * * @param node an AST node ...
  * `asArgumentList` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 98`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 27`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 51`, `import: 9`
* *Defense:* `safety: 18`, `doc: 13`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.972
  * `Choke Point (Betweenness):` 0.000316 | `Ripple Effect (Closeness):` 0.091129
  * `Imports (Out-Degree: 2):` java.util.regex.Pattern, org.codehaus.groovy.syntax.Token, org.codehaus.groovy.runtime.dgmimpl.arrays.IntegerArrayGetAtMetaMethod, spock.lang.Specification, java.util.Collections.singletonList, java.util.*, org.codehaus.groovy.ast.expr.*, org.objectweb.asm.Opcodes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spock-core/src/main/java/org/spockframework/util/TeePrintStream.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.782 IQR)
- **Top Global Matches:** file_cluster_8: 8.782, file_cluster_0: 8.882, file_cluster_13: 9.535
- **Magnitude:** 242.76 | **LOC:** 353 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2773%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `clearError` (Impact: 14.1)
  * `append` (Impact: 5.3)
  * `append` (Impact: 5.3)
  * `write` (Impact: 5.2)
  * `print` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 52`, `args: 44`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 32`, `orphaned_logic: 6`
* *Architecture:* `api: 44`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.*, java.util.concurrent.CopyOnWriteArrayList, java.util.Arrays.asList, groovy.lang.MissingMethodException, org.spockframework.runtime.GroovyRuntimeUtil, java.io.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/smoke/extension/PendingFeatureIfExtensionSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.188 IQR)
- **Top Global Matches:** file_cluster_8: 9.188, file_cluster_0: 9.796, file_cluster_7: 10.059
- **Magnitude:** 239.26 | **LOC:** 391 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 15.4)
  * `def` (Impact: 15.3)
  * `def` (Impact: 15.1)
  * `def` (Impact: 14.8)
  * `def` (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 74`, `args: 51`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 21`
* *Architecture:* `import: 5`
* *Defense:* `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.spockframework.EmbeddedSpecification, spock.lang.PendingFeatureIf, org.spockframework.runtime.ConditionNotSatisfiedError, org.spockframework.runtime.SpockComparisonFailure
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-specs/src/test/groovy/org/spockframework/mock/runtime/mockito/MockitoMockMakerSpec.groovy` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.883 IQR)
- **Top Global Matches:** file_cluster_8: 8.883, file_cluster_13: 9.582, file_cluster_0: 9.739
- **Magnitude:** 232.84 | **LOC:** 546 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.8629%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `def` (Impact: 16.5)
  * `def` (Impact: 9.7)
  * `def` (Impact: 9.4)
  * `def` (Impact: 9.2)
  * `def` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 124`, `args: 62`, `func_start: 61`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 2`, `planned_debt: 2`, `duplicate_logic: 41`
* *Architecture:* `concurrency: 13`, `import: 15`
* *Defense:* `safety: 6`, `test: 97`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` spock.lang.Specification, spock.mock.MockMakers.mockito, org.mockito.MockMakers, org.mockito.exceptions.base.MockitoException, spock.lang.Requires, java.lang.reflect.Proxy, org.spockframework.mock.CannotCreateMockException, spock.mock.DetachedMockFactory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoConverter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.253 IQR)
- **Top Global Matches:** file_cluster_0: 10.253, file_cluster_8: 10.343, file_cluster_13: 10.515
- **Magnitude:** 232.5 | **LOC:** 422 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.8086%), Tech Debt (99.9361%)
**Top Internal Functions/Classes:**
  * `visitTernaryExpression` (Impact: 10.4)
  * `visitShortTernaryExpression` (Impact: 10.3)
  * `startOf` (Impact: 9.4)
  * `visitBinaryExpression` (Impact: 7.9)
  * `visitPropertyExpression` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 89`, `args: 44`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 32`, `orphaned_logic: 34`
* *Architecture:* `api: 39`, `import: 14`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.util.Collections.singletonList, org.codehaus.groovy.ast.expr.*, org.spockframework.compat.groovy2.GroovyCodeVisitorCompat, org.spockframework.runtime.model.TextRegion, java.util.ArrayList, org.codehaus.groovy.syntax.Types, org.codehaus.groovy.ast.ASTNode, org.spockframework.runtime.model.TextPosition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spock-core/src/main/java/org/spockframework/util/JsonWriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.405 IQR)
- **Top Global Matches:** file_cluster_8: 8.405, file_cluster_7: 9.128, file_cluster_16: 9.21
- **Magnitude:** 232.4 | **LOC:** 230 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7201%), Tech Debt (99.8372%)
**Top Internal Functions/Classes:**
  * `writeString` (Impact: 104.3)
  * `write` (Impact: 34.4)
  * `writeIterable` (Impact: 19.0)
  * `writeMap` (Impact: 15.6)
  * `writeNewline` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 27`, `args: 13`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 3`, `duplicate_logic: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 7`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.*, java.io.*, java.text.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `spock-core/src/main/java/org/spockframework/mock/DefaultCompareToInteraction.java` (JAVA) | Magnitude: 15.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 5, api: 5
- `spock-specs/src/test/groovy/org/spockframework/smoke/extension/TempDirExtensionSpec.groovy` (GROOVY) | Magnitude: 163.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 296, structural_boundaries: 69, test: 48, args: 43
- `spock-core/src/main/java/spock/util/io/FileSystemFixture.java` (JAVA) | Magnitude: 75.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 38, io: 26, func_start: 17
- `spock-core/src/main/java/spock/util/time/MutableClock.java` (JAVA) | Magnitude: 62.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, doc: 29, structural_boundaries: 20, api: 19
- `spock-core/src/main/java/org/spockframework/mock/runtime/ByteBuddyInterceptorAdapter.java` (JAVA) | Magnitude: 179.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, decorators: 11, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `spock-core/src/main/java/spock/config/IncludeExcludeCriteria.java` (JAVA) | Magnitude: 31.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, branch: 9, structural_boundaries: 9, state_mutation: 6
- `spock-core/src/main/groovy/spock/util/EmbeddedSpecCompiler.groovy` (GROOVY) | Magnitude: 83.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 33, func_start: 32, args: 30
- `spock-spring/src/test/groovy/org/spockframework/spring/mock/imported/SpringBeanOnTestFieldForExistingBeanWithQualifierIntegrationSpec.groovy` (GROOVY) | Magnitude: 16.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 18, decorators: 9, args: 8
- `spock-core/src/main/java/org/spockframework/runtime/ExpressionInfoValueRenderer.java` (JAVA) | Magnitude: 72.76 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 32, branch: 16, args: 9
- `spock-core/src/main/java/org/spockframework/mock/MockImplementation.java` (JAVA) | Magnitude: 14.12 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, indent_spaces: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `spock-spring/src/main/java/org/spockframework/spring/mock/SpockContextCustomizerFactory.java` (JAVA) | Magnitude: 5.14 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, generics: 2, branch: 1
- `spock-core/src/main/java/org/spockframework/util/IThrowableBiConsumer.java` (JAVA) | Magnitude: 17.74 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 2, args: 1, func_start: 1
- `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` (JAVA) | Magnitude: 297.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 232, api: 107, structural_boundaries: 91, args: 56
- `spock-core/src/main/java/org/spockframework/runtime/GlobalExtensionRegistry.java` (JAVA) | Magnitude: 209.62 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 162, structural_boundaries: 60, branch: 59, generics: 32
- `spock-core/src/main/java/org/spockframework/runtime/extension/IStatelessAnnotationDrivenExtension.java` (JAVA) | Magnitude: 14.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 5, generics: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `spock-core/src/main/java/org/spockframework/runtime/ExtensionRunner.java` (JAVA) | Magnitude: 138.4 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, branch: 48, structural_boundaries: 33, args: 22
- `spock-specs/specs.gradle` (GROOVY) | Magnitude: 36.66 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 23, branch: 8, args: 6
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` (JAVA) | Magnitude: 306.78 | Delta: **0.207 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 364, structural_boundaries: 132, branch: 70, args: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `spock-core/src/main/java/org/spockframework/runtime/AsyncRunListener.java` (JAVA) | Magnitude: 97.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 26, args: 24, concurrency: 21
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/RetryIterationInterceptor.java` (JAVA) | Magnitude: 99.7 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 35, state_mutation: 24, concurrency: 19
- `spock-specs/src/test/groovy/org/spockframework/runtime/extension/builtin/ThreadDumpUtilityTypeTest.groovy` (GROOVY) | Magnitude: 19.46 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, concurrency: 12, import: 7
- `spock-core/src/main/java/org/spockframework/runtime/SimpleFeatureNode.java` (JAVA) | Magnitude: 54.42 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, concurrency: 18, args: 7
- `spock-spring/spring5-test/src/test/groovy/org/spockframework/spring5/NoMockConfig.groovy` (GROOVY) | Magnitude: 29.9 | Delta: **0.288 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 15, indent_spaces: 15, structural_boundaries: 9, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `spock-core/src/main/java/org/spockframework/runtime/model/parallel/Resources.java` (JAVA) | Magnitude: 9.12 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, sec_high_risk_execution: 10, indent_spaces: 8, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/ThreadDumpUtilityType.java` (JAVA) | Magnitude: 36.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 16, branch: 7, args: 7
- `spock-core/src/main/java/org/spockframework/compiler/NoSpecialMethodCall.java` (JAVA) | Magnitude: 77.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 30, api: 23, args: 21
- `spock-spring/src/test/groovy/org/spockframework/spring/LazyBeans.groovy` (GROOVY) | Magnitude: 10.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, decorators: 6, import: 4
- `spock-spring/src/test/groovy/org/spockframework/spring/mock/imported/SpringBeanWithInjectedFieldIntegrationSpec.groovy` (GROOVY) | Magnitude: 6.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, import: 4, args: 3
- `spock-core/src/main/java/org/spockframework/runtime/extension/builtin/TimeoutInterceptor.java` (JAVA) | Magnitude: 150.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 151, branch: 39, structural_boundaries: 34, func_start: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `spock-specs/src/test/java/org/spockframework/smoke/CallChainException.java` (JAVA) | Magnitude: 12.04 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, class_start: 1, api: 1, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `spock-specs/src/test/groovy/org/spockframework/smoke/mock/GroovySpiesThatAreGlobal.groovy` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 535.66
- `spock-core/src/main/java/org/spockframework/runtime/SpecInternals.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 389.28
- `spock-core/src/main/java/org/spockframework/compiler/WhereBlockRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 306.78
- `spock-core/src/main/java/org/spockframework/runtime/model/FeatureInfo.java` -> **Leonard Brünings** (100.0% isolated ownership) | Magnitude: 297.0
- `spock-core/src/main/java/org/spockframework/compiler/InteractionRewriter.java` -> **Björn Kautler** (100.0% isolated ownership) | Magnitude: 262.02

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

- `spock-core/src/main/java/org/spockframework/lang/Wildcard.java` -> **Severity: 1580.631** (Blast Radius: 16.123 * Doc Risk: 98.0358%)
- `spock-core/src/main/java/spock/lang/Specification.java` -> **Severity: 1005.166** (Blast Radius: 67.459 * Doc Risk: 14.9004%)
- `spock-core/src/main/java/org/spockframework/compiler/AstUtil.java` -> **Severity: 884.419** (Blast Radius: 8.972 * Doc Risk: 98.5755%)
- `spock-core/src/main/java/org/spockframework/util/ExceptionUtil.java` -> **Severity: 840.86** (Blast Radius: 13.64 * Doc Risk: 61.6466%)
- `spock-core/src/main/java/org/spockframework/runtime/InvalidSpecException.java` -> **Severity: 655.829** (Blast Radius: 6.879 * Doc Risk: 95.3378%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
