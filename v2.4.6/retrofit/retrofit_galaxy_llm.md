# ARCHITECTURAL_BRIEF: retrofit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/retrofit` |
| **Timestamp** | `2026-08-03T21:27:11.539834+00:00` |
| **Scan Duration** | `1.8s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `77e6ba21d9ba372d1b23ef29881912910da23347` |
| **Git Remote** | `https://github.com/square/retrofit` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 355 malicious artifacts.

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
| Total Artifacts | 1109 |
| Analyzed Artifacts (Scanned) | 453 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 656 |
| Total LOC | 43448 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 40.8% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3937 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.459 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6885 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 306 | 27261 | 67.5% |
| PLAINTEXT | 31 | 1 | 6.8% |
| JAVASCRIPT | 29 | 1235 | 6.4% |
| CSS | 28 | 13222 | 6.2% |
| MARKDOWN | 26 | 0 | 5.7% |
| KOTLIN | 16 | 1152 | 3.5% |
| XML | 7 | 0 | 1.5% |
| HTML | 4 | 435 | 0.9% |
| JSON | 2 | 6 | 0.4% |
| BATCH | 1 | 72 | 0.2% |
| PROTO | 1 | 10 | 0.2% |
| GROOVY | 1 | 39 | 0.2% |
| TYPESCRIPT | 1 | 15 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.432`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 199 | 43.9% |
| file_cluster_8 | 122 | 26.9% |
| file_cluster_0 | 28 | 6.2% |
| file_cluster_4 | 25 | 5.5% |
| file_cluster_16 | 19 | 4.2% |
| file_cluster_17 | 2 | 0.4% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 56 | 12.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 656*

**Composition by Extension & Reason:**
- `.html`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 37x Excluded (Machine-Generated Source Code Signature: 127 LOC), 27x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `no_extension`: 24x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 253 LOC)
- `.gradle`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 7x Unsupported Format (.pro)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.jar`: 1x Excluded (Explicitly Denied Extension: '.jar')
- `.properties`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.processors`: 1x Unsupported Format (.processors)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.5 | 8.3 | 0.0 |
| Error & Exception Exposure | 0.0 | 95.6 | 38.1 | 41.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.0 | 4.6 | 4.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 45.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.9 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 20.0 | 0.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.1 | 9.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.1 | 2.1 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` (Hits: 34)
- `retrofit/kotlin-test/src/test/java/retrofit2/KotlinSuspendTest.kt` (Hits: 21)
- `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/index.html` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Retrofit.java** (`retrofit/src/main/java/retrofit2/Retrofit.java`) — 133 inbound connections
2. **Response.java** (`retrofit/src/main/java/retrofit2/Response.java`) — 100 inbound connections
3. **GET.java** (`retrofit/src/main/java/retrofit2/http/GET.java`) — 97 inbound connections
4. **Converter.java** (`retrofit/src/main/java/retrofit2/Converter.java`) — 58 inbound connections
5. **Call.java** (`retrofit/src/main/java/retrofit2/Call.java`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RequestFactoryTest.java** (`retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java`) — 49 outbound dependencies
2. **RetrofitTest.java** (`retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) — 45 outbound dependencies
3. **RequestFactory.java** (`retrofit/src/main/java/retrofit2/RequestFactory.java`) — 45 outbound dependencies
4. **MoshiConverterFactoryTest.java** (`retrofit-converters/moshi/src/test/java/retrofit2/converter/moshi/MoshiConverterFactoryTest.java`) — 36 outbound dependencies
5. **CallTest.java** (`retrofit/java-test/src/test/java/retrofit2/CallTest.java`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseParameterAnnotation` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **1015.6** | LOC: 456
- `enqueue` (@ `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java`) -> Impact: **277.2** | LOC: 58
- `enqueue` (@ `samples/src/main/java/com/example/retrofit/ErrorHandlingAdapter.java`) -> Impact: **136.6** | LOC: 37
- `hasUnresolvableType` (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **119.1** | LOC: 30
- `unresolvableResponseTypeThrows` (@ `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) -> Impact: **118.0** | LOC: 61
- `unresolvableParameterTypeThrows` (@ `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) -> Impact: **118.0** | LOC: 61
- `getGenericSupertype` (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **110.0** | LOC: 39
- `create` (@ `retrofit/src/main/java/retrofit2/KotlinExtensions.kt`) -> Impact: **97.0** | LOC: 35
  * *Intent:* /* * Copyright (C) 2018 Square, Inc. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in complia...
- `parseAnnotations` (@ `retrofit/src/main/java/retrofit2/HttpServiceMethod.java`) -> Impact: **90.0** | LOC: 85
- `request` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`) -> Impact: **86.4** | LOC: 29

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `enqueue` (@ `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java`) -> **O(2^N) [Recursive]**
- `enqueue` (@ `retrofit/src/main/java/retrofit2/DefaultCallAdapterFactory.java`) -> **O(2^N) [Recursive]**
- `crawlPage` (@ `samples/src/main/java/com/example/retrofit/Crawler.java`) -> **O(2^N) [Recursive]**
- `create` (@ `retrofit/src/main/java/retrofit2/KotlinExtensions.kt`) -> **O(2^N) [Recursive]**
  * *Intent:* /* * Copyright (C) 2018 Square, Inc. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in complia...
- `onError` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/BodyOnSubscribe.java`) -> **O(2^N) [Recursive]**
- `onError` (@ `retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/BodyObservable.java`) -> **O(2^N) [Recursive]**
- `onError` (@ `retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/BodyObservable.java`) -> **O(2^N) [Recursive]**
- `enqueue` (@ `samples/src/main/java/com/example/retrofit/ErrorHandlingAdapter.java`) -> **O(2^N) [Recursive]**
- `onNext` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/BodyOnSubscribe.java`) -> **O(2^N) [Recursive]**
- `call` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallEnqueueOnSubscribe.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `parseParameterAnnotation` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> DB Complexity: **30**
- `starlight` (@ `website/astro.config.mjs`) -> DB Complexity: **17**
- `safeLocalStorage` (@ `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js`) -> DB Complexity: **13**
  * *Intent:* /* * Copyright 2014-2024 JetBrains s.r.o. Use of this source code is governed by the Apache 2.0 license.
- `supportedResponseTypes` (@ `retrofit-converters/scalars/src/test/java/retrofit2/converter/scalars/ScalarsConverterFactoryTest.java`) -> DB Complexity: **11**
- `supportedResponseTypes` (@ `retrofit-converters/scalars/src/test/java/retrofit2/converter/scalars/ScalarsConverterPrimitivesFactoryTest.java`) -> DB Complexity: **10**
- `apply` (@ `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/RecordingSubscriber.java`) -> DB Complexity: **9**
- `apply` (@ `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/RxJavaPluginsResetRule.java`) -> DB Complexity: **9**
  * *Intent:* /* * Copyright (C) 2016 Square, Inc. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in complia...
- `apply` (@ `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RecordingCompletableObserver.java`) -> DB Complexity: **9**
- `apply` (@ `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RecordingMaybeObserver.java`) -> DB Complexity: **9**
- `apply` (@ `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RecordingObserver.java`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `retrofit/java-test/src/test/java/retrofit2` | 17 | 6089.16 | 29.38% | 0.0% |
| `retrofit/android-test` | 1 | 5000.0 | 0.0% | 0.0% |
| `retrofit/src/main/java/retrofit2` | 28 | 4000.14 | 17.67% | 48.41% |
| `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2` | 27 | 2544.12 | 26.92% | 0.0% |
| `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3` | 27 | 2542.34 | 26.92% | 0.0% |
| `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava` | 19 | 1406.98 | 34.5% | 0.0% |
| `__monolith__` | 8 | 1103.04 | 4.66% | 0.0% |
| `retrofit-mock/src/main/java/retrofit2/mock` | 8 | 972.6 | 31.54% | 28.2% |
| `retrofit/src/main/java/retrofit2/http` | 26 | 887.58 | 5.78% | 0.0% |
| `retrofit-mock/src/test/java/retrofit2/mock` | 5 | 841.12 | 61.43% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `retrofit-converters/scalars/src/main/java/retrofit2/converter/scalars/ScalarResponseBodyConverters.java` -> **100.0%** Exposure
- `retrofit-converters/simplexml/src/main/java/retrofit2/converter/simplexml/SimpleXmlConverterFactory.java` -> **100.0%** Exposure
- `retrofit-mock/src/main/java/retrofit2/mock/Calls.java` -> **100.0%** Exposure
- `retrofit/src/main/java/retrofit2/BuiltInConverters.java` -> **100.0%** Exposure
- `retrofit/src/main/java/retrofit2/CompletableFutureCallAdapterFactory.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `website/public/1.x/converter-jackson/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-protobuf/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-simplexml/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-wire/script.js` -> **100.0%** Exposure
- `website/public/1.x/retrofit/script.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` -> **164** Orphaned Functions | **0** Duplicates
- `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` -> **72** Orphaned Functions | **0** Duplicates
- `retrofit/java-test/src/test/java/retrofit2/CallTest.java` -> **44** Orphaned Functions | **0** Duplicates
- `retrofit-mock/src/main/java/retrofit2/mock/Calls.java` -> **1** Orphaned Functions | **20** Duplicates
- `retrofit/src/main/java/retrofit2/Utils.java` -> **5** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`retrofit-converters/kotlinx-serialization/src/main/java/retrofit2/converter/kotlinx/serialization/Factory.kt`** -> AI Confidence: **99.48%**
2. **`retrofit-converters/kotlinx-serialization/src/main/java/retrofit2/converter/kotlinx/serialization/Serializer.kt`** -> AI Confidence: **99.48%**
3. **`retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateKotlinTest.kt`** -> AI Confidence: **99.48%**
4. **`retrofit-response-type-keeper/src/main/kotlin/retrofit2/keeper/RetrofitResponseTypeKeepProcessor.kt`** -> AI Confidence: **99.48%**
5. **`retrofit/kotlin-test/src/test/java/retrofit2/KotlinSuspendTest.kt`** -> AI Confidence: **99.48%**
6. **`retrofit/src/main/java/retrofit2/KotlinExtensions.kt`** -> AI Confidence: **99.48%**
7. **`samples/src/main/java/com/example/retrofit/ConditionalLoggingInterceptor.kt`** -> AI Confidence: **99.48%**
8. **`retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`** -> AI Confidence: **99.31%**
9. **`retrofit-mock/src/test/java/retrofit2/mock/NetworkBehaviorTest.java`** -> AI Confidence: **99.31%**
10. **`retrofit/src/main/java/retrofit2/RequestBuilder.java`** -> AI Confidence: **99.31%**
11. **`retrofit/src/main/java/retrofit2/RequestFactory.java`** -> AI Confidence: **99.31%**
12. **`retrofit/src/main/java/retrofit2/Utils.java`** -> AI Confidence: **99.31%**
13. **`settings.gradle`** -> AI Confidence: **99.29%**
14. **`retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/CallExecuteObservable.java`** -> AI Confidence: **99.24%**
15. **`retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/CallExecuteObservable.java`** -> AI Confidence: **99.24%**
16. **`retrofit/src/main/java/retrofit2/Retrofit.java`** -> AI Confidence: **99.24%**
17. **`retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/CallEnqueueObservable.java`** -> AI Confidence: **99.23%**
18. **`retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/CallEnqueueObservable.java`** -> AI Confidence: **99.23%**
19. **`retrofit/java-test/src/test/java/retrofit2/ResponseTest.java`** -> AI Confidence: **99.23%**
20. **`retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/ResultOnSubscribe.java`** -> AI Confidence: **99.18%**
21. **`retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/ResultObservable.java`** -> AI Confidence: **99.18%**
22. **`retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RecordingCompletableObserver.java`** -> AI Confidence: **99.18%**
23. **`retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/ResultObservable.java`** -> AI Confidence: **99.18%**
24. **`retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/RecordingCompletableObserver.java`** -> AI Confidence: **99.18%**
25. **`retrofit-adapters/scala/src/main/java/retrofit2/adapter/scala/ScalaCallAdapterFactory.java`** -> AI Confidence: **99.18%**
26. **`retrofit-converters/jaxb/src/test/java/retrofit2/converter/jaxb/JaxbConverterFactoryTest.java`** -> AI Confidence: **99.18%**
27. **`retrofit-converters/jaxb3/src/test/java/retrofit2/converter/jaxb3/JaxbConverterFactoryTest.java`** -> AI Confidence: **99.18%**
28. **`retrofit-converters/moshi/src/main/java/retrofit2/converter/moshi/MoshiResponseBodyConverter.java`** -> AI Confidence: **99.18%**
29. **`retrofit-converters/protobuf/src/main/java/retrofit2/converter/protobuf/ProtoResponseBodyConverter.java`** -> AI Confidence: **99.18%**
30. **`retrofit-converters/scalars/src/test/java/retrofit2/converter/scalars/ScalarsConverterFactoryTest.java`** -> AI Confidence: **99.18%**
31. **`retrofit-converters/wire/src/test/java/retrofit2/converter/wire/CrashingPhone.java`** -> AI Confidence: **99.18%**
32. **`retrofit-converters/wire/src/test/java/retrofit2/converter/wire/WireConverterFactoryTest.java`** -> AI Confidence: **99.18%**
33. **`retrofit-mock/src/main/java/retrofit2/mock/BehaviorDelegate.java`** -> AI Confidence: **99.18%**
34. **`retrofit-mock/src/main/java/retrofit2/mock/NetworkBehavior.java`** -> AI Confidence: **99.18%**
35. **`retrofit/java-test/src/test/java/retrofit2/AnnotationArraySubject.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/AsyncTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingSafeSubscriberTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingTest.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `retrofit-converters/gson/src/test/java/retrofit2/converter/gson/GsonConverterFactoryTest.java` -> **100.0%** Exposure
- `retrofit-converters/guava/src/test/java/retrofit/converter/guava/GuavaOptionalConverterFactoryTest.java` -> **100.0%** Exposure
- `retrofit-converters/jackson/src/test/java/retrofit2/converter/jackson/JacksonConverterFactoryTest.java` -> **100.0%** Exposure
- `retrofit-converters/java8/src/test/java/retrofit/converter/java8/Java8OptionalConverterFactoryTest.java` -> **100.0%** Exposure
- `retrofit-converters/jaxb/src/test/java/retrofit2/converter/jaxb/JaxbConverterFactoryTest.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `retrofit-adapters/guava/src/main/java/retrofit2/adapter/guava/GuavaCallAdapterFactory.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/AsyncTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableThrowingSafeSubscriberTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableThrowingTest.java` -> **100.0%** Exposure
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingSafeSubscriberTest.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `31` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3184` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java` (JAVA) -> Cumulative Risk: **942.11**
- **Archetype:** `file_cluster_4` (Distance: 10.894 IQR)
- **Magnitude:** 421.16 | **LOC:** 178 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `enqueue` (Impact: 277.2), `execute` (Impact: 25.5), `cancel` (Impact: 12.3)

### 2. `website/public/2.x/converter-kotlinx-serialization/scripts/navigation-loader.js` (JAVASCRIPT) -> Cumulative Risk: **821.41**
- **Archetype:** `file_cluster_17` (Distance: 14.48 IQR)
- **Magnitude:** 115.7 | **LOC:** 96 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Documentation (99.8532%)
- **Heaviest Functions:** `revealNavigationForCurrentPage` (Impact: 37.3), `revealParents` (Impact: 21.1), `scrollNavigationToSelectedElement` (Impact: 18.5)

### 3. `retrofit-mock/src/main/java/retrofit2/mock/Calls.java` (JAVA) -> Cumulative Risk: **692.2**
- **Archetype:** `file_cluster_0` (Distance: 10.476 IQR)
- **Magnitude:** 211.3 | **LOC:** 215 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `enqueue` (Impact: 24.2), `request` (Impact: 18.3), `getDelegate` (Impact: 14.0)

### 4. `retrofit/android-test/src/androidTest/java/retrofit2/CompletableFutureAndroidTest.java` (JAVA) -> Cumulative Risk: **690.11**
- **Archetype:** `file_cluster_13` (Distance: 9.927 IQR)
- **Magnitude:** 26.4 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (99.5763%), Tech Debt (96.1368%)
- **Heaviest Functions:** `setUp` (Impact: 4.4), `completableFutureApi24` (Impact: 2.3)

### 5. `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateTest.java` (JAVA) -> Cumulative Risk: **675.04**
- **Archetype:** `file_cluster_4` (Distance: 11.933 IQR)
- **Magnitude:** 251.5 | **LOC:** 338 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `syncCanBeCanceled` (Impact: 26.6), `setUp` (Impact: 9.1), `syncFailureThrowsAfterDelay` (Impact: 6.8)

### 6. `retrofit-adapters/java8/src/main/java/retrofit2/adapter/java8/Java8CallAdapterFactory.java` (JAVA) -> Cumulative Risk: **667.07**
- **Archetype:** `file_cluster_16` (Distance: 9.466 IQR)
- **Magnitude:** 84.72 | **LOC:** 176 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9999%), Tech Debt (99.9073%)
- **Heaviest Functions:** `adapt` (Impact: 26.0), `adapt` (Impact: 13.6), `responseType` (Impact: 4.2)

### 7. `retrofit/java-test/src/test/java/retrofit2/DefaultCallAdapterFactoryTest.java` (JAVA) -> Cumulative Risk: **656.61**
- **Archetype:** `file_cluster_0` (Distance: 10.757 IQR)
- **Magnitude:** 113.14 | **LOC:** 160 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `responseType` (Impact: 12.6), `rawTypeThrows` (Impact: 12.5), `adaptedCallExecute` (Impact: 5.8)

### 8. `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` (JAVA) -> Cumulative Risk: **632.74**
- **Archetype:** `file_cluster_4` (Distance: 11.363 IQR)
- **Magnitude:** 248.6 | **LOC:** 342 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `responseEnqueue` (Impact: 13.9), `deferredThrowExecute` (Impact: 12.7), `responseExecute` (Impact: 6.7)

### 9. `retrofit/java-test/src/test/java/retrofit2/CallTest.java` (JAVA) -> Cumulative Risk: **625.36**
- **Archetype:** `file_cluster_4` (Distance: 11.74 IQR)
- **Magnitude:** 997.56 | **LOC:** 1522 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `conversionProblemIncomingMaskedByConvert` (Impact: 37.7), `fatalErrorsAreNotCaughtEnqueue` (Impact: 22.4), `requestThrowingBeforeExecuteFailsExecute` (Impact: 21.9)

### 10. `retrofit/src/main/java/retrofit2/KotlinExtensions.kt` (KOTLIN) -> Cumulative Risk: **623.08**
- **Archetype:** `file_cluster_16` (Distance: 9.862 IQR)
- **Magnitude:** 129.48 | **LOC:** 126 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9917%), Tech Debt (99.9908%)
- **Heaviest Functions:** `create` (Impact: 97.0), `onResponse` (Impact: 10.7), `suspendAndThrow` (Impact: 3.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `retrofit/android-test/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.052 IQR)
- **Top Global Matches:** file_cluster_0: 12.052, file_cluster_8: 12.346, file_cluster_16: 12.583
- **Magnitude:** 2494.02 | **LOC:** 3422 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.1448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `twoMethodsFail` (Impact: 29.0 | O(N^3))
  * `multipartPartMapRejectsNullValues` (Impact: 26.2 | O(N^4) | DB: 2)
  * `fieldMapRejectsNullValues` (Impact: 26.2 | O(N^4) | DB: 2)
  * `queryMapRejectsNullValues` (Impact: 26.1 | O(N^4) | DB: 2)
  * `headerMapRejectsNullValues` (Impact: 26.1 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 861`, `args: 336`, `func_start: 961`, `class_start: 172`
* *Risk/State:* `safety_bypasses: 227`, `state_mutation: 76`, `orphaned_logic: 164`
* *Architecture:* `io: 34`, `api: 168`, `import: 49`
* *Defense:* `safety: 145`, `test: 652`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` java.net.URI, java.util.Map, retrofit2.http.QueryName, retrofit2.TestingUtils.buildRequest, retrofit2.http.Headers, okhttp3.MediaType, org.junit.Assert.fail, java.util.Arrays.asList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.211 IQR)
- **Top Global Matches:** file_cluster_0: 12.211, file_cluster_4: 12.284, file_cluster_8: 12.521
- **Magnitude:** 1875.14 | **LOC:** 1806 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (66.1602%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unresolvableResponseTypeThrows` (Impact: 118.0 | O(N^4))
  * `unresolvableParameterTypeThrows` (Impact: 118.0 | O(N^4))
  * `annotationParsingFailureObservedByWaitin` (Impact: 64.2 | O(N^5) | DB: 6)
  * `callAdapterFactoryQueriedCanDelegateTwic` (Impact: 50.9 | O(N^3) | DB: 4)
  * `callAdapterFactoryQueriedCanDelegate` (Impact: 42.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 505`, `args: 132`, `func_start: 283`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 89`, `orphaned_logic: 72`
* *Architecture:* `api: 117`, `concurrency: 299`, `import: 45`
* *Defense:* `safety: 80`, `doc: 1`, `test: 197`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` java.util.Set, java.util.Map, java.util.concurrent.Future, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AT_START, org.junit.Assert.assertNotNull, org.junit.Assert.assertSame, okhttp3.MediaType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.902 IQR)
- **Top Global Matches:** file_cluster_8: 10.902, file_cluster_13: 11.036, file_cluster_16: 11.18
- **Magnitude:** 1347.86 | **LOC:** 873 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (28.1862%), Tech Debt (15.2032%)
**Top Internal Functions/Classes:**
  * `parseParameterAnnotation` (Impact: 1015.6 | O(N^5) | DB: 30)
  * `parseMethodAnnotation` (Impact: 85.7 | O(N^2))
  * `build` (Impact: 58.5 | O(N^4))
  * `parseHeaders` (Impact: 49.7 | O(N^3) | DB: 1)
    * *Intent:* // Get the relative URL path and existing query string, if present.
  * `parseHttpMethodAndPath` (Impact: 36.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 178`, `args: 77`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 9`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 12`, `import: 45`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` java.util.regex.Matcher, java.net.URI, java.util.Set, retrofit2.Utils.methodError, java.util.Map, retrofit2.http.QueryName, okhttp3.MediaType, retrofit2.http.Header...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `settings.gradle` (GROOVY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.864 IQR)
- **Top Global Matches:** file_cluster_8: 7.864, file_cluster_7: 8.88, file_cluster_1: 9.087
- **Magnitude:** 1063.28 | **LOC:** 50 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (37.2405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/CallTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.74 IQR)
- **Top Global Matches:** file_cluster_4: 11.74, file_cluster_0: 11.793, file_cluster_8: 12.032
- **Magnitude:** 997.56 | **LOC:** 1522 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (71.3383%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `conversionProblemIncomingMaskedByConvert` (Impact: 37.7 | O(N^6) | DB: 1)
  * `fatalErrorsAreNotCaughtEnqueue` (Impact: 22.4 | O(N^3) | DB: 4)
  * `requestThrowingBeforeExecuteFailsExecute` (Impact: 21.9 | O(N^3) | DB: 2)
  * `requestThrowingNonFatalErrorBeforeExecut` (Impact: 21.9 | O(N^3) | DB: 2)
  * `requestAfterExecuteThrowingAlsoThrows` (Impact: 21.9 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 434`, `args: 123`, `func_start: 237`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 92`, `orphaned_logic: 44`
* *Architecture:* `io: 2`, `api: 96`, `concurrency: 282`, `import: 33`
* *Defense:* `safety: 56`, `test: 155`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.util.concurrent.atomic.AtomicReference, org.junit.Assert.fail, retrofit2.http.Body, java.util.concurrent.TimeUnit.SECONDS, retrofit2.http.Path, okio.BufferedSource, org.junit.Test, java.io.IOException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Utils.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.726 IQR)
- **Top Global Matches:** file_cluster_8: 10.726, file_cluster_13: 10.809, file_cluster_0: 10.817
- **Magnitude:** 525.44 | **LOC:** 558 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.383%), Tech Debt (99.9991%)
**Top Internal Functions/Classes:**
  * `hasUnresolvableType` (Impact: 119.1 | O(2^N))
  * `getGenericSupertype` (Impact: 110.0 | O(2^N))
  * `getRawType` (Impact: 46.0 | O(2^N))
  * `WildcardTypeImpl` (Impact: 21.6 | O(N^2))
  * `ParameterizedTypeImpl` (Impact: 18.8 | O(N^2))
    * *Intent:* /** * Returns the generic form of {@code supertype}. For example, if this is {@code * ArrayList<Stri...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 100`, `args: 39`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 30`, `duplicate_logic: 15`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 26`, `doc: 5`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.NoSuchElementException, java.lang.reflect.GenericArrayType, java.lang.reflect.Array, java.util.Arrays, java.util.Objects, okio.Buffer, java.io.IOException, java.lang.reflect.Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Retrofit.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.205 IQR)
- **Top Global Matches:** file_cluster_13: 11.205, file_cluster_16: 11.325, file_cluster_8: 11.552
- **Magnitude:** 464.0 | **LOC:** 717 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (21.0666%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `nextResponseBodyConverter` (Impact: 61.6 | O(N^3))
  * `create` (Impact: 56.8 | O(N^5))
  * `validateServiceInterface` (Impact: 55.2 | O(N^3) | DB: 2)
  * `loadServiceMethod` (Impact: 50.8 | O(N^3) | DB: 2)
    * *Intent:* * Create an implementation of the API endpoints defined by the {@code service} interface. * * <p>The...
  * `nextRequestBodyConverter` (Impact: 46.8 | O(N^2))
    * *Intent:* // On successful lock insertion, perform the work and update the map before releasing. // Other thre...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 91`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 24`, `duplicate_logic: 6`
* *Architecture:* `api: 35`, `concurrency: 7`, `import: 25`
* *Defense:* `safety: 20`, `doc: 36`, `sync_locks: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 100.004
  * `Choke Point (Betweenness):` 0.002682 | `Ripple Effect (Closeness):` 0.280261
  * `Imports (Out-Degree: 4):` java.net.URL, retrofit2.http.Header, java.lang.reflect.Modifier, java.lang.reflect.InvocationHandler, okhttp3.HttpUrl, java.util.Collections.unmodifiableList, javax.annotation.Nullable, java.util.concurrent.Executor...
  * `Imported By (In-Degree: 133):` (Excluded from Brief to save tokens)

### `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.966 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.724 IQR)
- **Top Global Matches:** file_cluster_17: 11.966, file_cluster_8: 12.558, file_cluster_11: 12.684
- **Magnitude:** 425.48 | **LOC:** 372 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (45.2278%), Tech Debt (32.1168%)
**Top Internal Functions/Classes:**
  * `handleAnchor` (Impact: 58.7 | O(N^4) | DB: 6)
  * `togglePlatformDependent` (Impact: 58.2 | O(N^5) | DB: 4)
  * `refreshPlatformTabs` (Impact: 37.5 | O(N^6) | DB: 2)
  * `safeLocalStorage` (Impact: 23.0 | O(N^4) | DB: 13)
    * *Intent:* /* * Copyright 2014-2024 JetBrains s.r.o. Use of this source code is governed by the Apache 2.0 lice...
  * `scrollToElementInContent` (Impact: 22.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 71`, `args: 49`, `func_start: 53`
* *Risk/State:* `state_mutation: 71`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 1`
* *Defense:* `safety: 31`, `doc: 1`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.894 IQR)
- **Top Global Matches:** file_cluster_4: 10.894, file_cluster_0: 11.126, file_cluster_13: 11.181
- **Magnitude:** 421.16 | **LOC:** 178 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (40.0808%)
**Top Internal Functions/Classes:**
  * `enqueue` (Impact: 277.2 | O(2^N))
  * `execute` (Impact: 25.5 | O(N^3) | DB: 4)
  * `cancel` (Impact: 12.3 | O(2^N))
  * `clone` (Impact: 4.2 | O(2^N))
  * `request` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 45`, `args: 16`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 11`, `orphaned_logic: 3`
* *Architecture:* `api: 13`, `concurrency: 60`, `import: 13`
* *Defense:* `safety: 6`, `sync_locks: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.Future, java.util.concurrent.atomic.AtomicReference, okhttp3.Request, retrofit2.Call, java.io.IOException, retrofit2.Callback, java.util.concurrent.TimeUnit.MILLISECONDS, javax.annotation.Nullable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/FlowableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.856 IQR)
- **Top Global Matches:** file_cluster_4: 11.856, file_cluster_0: 12.112, file_cluster_13: 12.157
- **Magnitude:** 319.64 | **LOC:** 348 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 11.4 | O(N^4) | DB: 3)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 11.4 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 93`, `args: 34`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, org.reactivestreams.Subscriber, io.reactivex.Flowable, io.reactivex.exceptions.CompositeException, retrofit2.Response, retrofit2.http.GET, org.junit.Rule, okhttp3.mockwebserver.MockResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/ObservableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.856 IQR)
- **Top Global Matches:** file_cluster_4: 11.856, file_cluster_0: 12.112, file_cluster_13: 12.157
- **Magnitude:** 319.64 | **LOC:** 348 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 11.4 | O(N^4) | DB: 3)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 11.4 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 93`, `args: 34`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, retrofit2.Response, retrofit2.http.GET, org.junit.Rule, okhttp3.mockwebserver.MockResponse, io.reactivex.Observer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/FlowableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.87 IQR)
- **Top Global Matches:** file_cluster_4: 11.87, file_cluster_0: 12.127, file_cluster_13: 12.186
- **Magnitude:** 319.2 | **LOC:** 338 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 11.3 | O(N^4) | DB: 3)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 11.3 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 89`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 18`
* *Defense:* `test: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.junit.Rule, okhttp3.mockwebserver.MockResponse, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockWebServer, io.reactivex.rxjava3.core.Flowable, org.junit.rules.TestRule, io.reactivex.rxjava3.exceptions.Exceptions, retrofit2.Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/ObservableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.869 IQR)
- **Top Global Matches:** file_cluster_4: 11.869, file_cluster_0: 12.127, file_cluster_13: 12.186
- **Magnitude:** 319.2 | **LOC:** 338 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 11.3 | O(N^4) | DB: 3)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 11.3 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 89`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 18`
* *Defense:* `test: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.rxjava3.core.Observable, org.junit.Rule, okhttp3.mockwebserver.MockResponse, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockWebServer, io.reactivex.rxjava3.disposables.Disposable, org.junit.rules.TestRule, io.reactivex.rxjava3.exceptions.Exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/ParameterHandler.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.326 IQR)
- **Top Global Matches:** file_cluster_8: 9.326, file_cluster_16: 9.455, file_cluster_0: 9.697
- **Magnitude:** 301.38 | **LOC:** 459 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.6803%), Tech Debt (99.9685%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 46.6 | O(N^4))
  * `apply` (Impact: 46.6 | O(N^4))
  * `apply` (Impact: 36.3 | O(N^4))
  * `apply` (Impact: 28.9 | O(N^3))
  * `iterable` (Impact: 12.6 | O(N^2))
    * *Intent:* * Copyright (C) 2015 Square, Inc. * * Licensed under the Apache License, Version 2.0 (the "License")...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 85`, `args: 35`, `func_start: 35`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 6`, `duplicate_logic: 15`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `import: 8`
* *Defense:* `safety: 8`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Map, java.lang.reflect.Array, java.util.Objects, java.io.IOException, javax.annotation.Nullable, okhttp3.RequestBody, okhttp3.MultipartBody, java.lang.reflect.Method
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/MaybeThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.082 IQR)
- **Top Global Matches:** file_cluster_4: 12.082, file_cluster_13: 12.388, file_cluster_0: 12.404
- **Magnitude:** 294.96 | **LOC:** 287 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 11.3 | O(N^4) | DB: 3)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 11.3 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 79`, `args: 28`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 7`
* *Architecture:* `api: 22`, `concurrency: 102`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, io.reactivex.disposables.Disposable, io.reactivex.MaybeObserver, io.reactivex.exceptions.CompositeException, retrofit2.Response, retrofit2.http.GET, io.reactivex.Maybe, org.junit.Rule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/MaybeThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.115 IQR)
- **Top Global Matches:** file_cluster_4: 12.115, file_cluster_13: 12.435, file_cluster_0: 12.437
- **Magnitude:** 294.52 | **LOC:** 280 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 11.2 | O(N^4) | DB: 3)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 11.2 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 75`, `args: 28`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 7`
* *Architecture:* `api: 22`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, io.reactivex.rxjava3.core.MaybeObserver, io.reactivex.rxjava3.exceptions.CompositeException, retrofit2.Response, io.reactivex.rxjava3.core.Maybe, retrofit2.http.GET, org.junit.Rule, okhttp3.mockwebserver.MockResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/SingleThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.096 IQR)
- **Top Global Matches:** file_cluster_4: 12.096, file_cluster_13: 12.401, file_cluster_0: 12.429
- **Magnitude:** 289.7 | **LOC:** 284 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 11.3 | O(N^4) | DB: 3)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 11.3 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 78`, `args: 27`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `concurrency: 102`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, io.reactivex.SingleObserver, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, retrofit2.Response, retrofit2.http.GET, org.junit.Rule, okhttp3.mockwebserver.MockResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/SingleThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.13 IQR)
- **Top Global Matches:** file_cluster_4: 12.13, file_cluster_13: 12.449, file_cluster_0: 12.462
- **Magnitude:** 289.26 | **LOC:** 277 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 16.6 | O(N^4) | DB: 6)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 16.6 | O(N^4) | DB: 6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 11.7 | O(N^4) | DB: 3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 11.2 | O(N^4) | DB: 3)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 11.2 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 74`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, io.reactivex.rxjava3.exceptions.CompositeException, retrofit2.Response, retrofit2.http.GET, org.junit.Rule, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, io.reactivex.rxjava3.exceptions.Exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-converters/moshi/src/test/java/retrofit2/converter/moshi/MoshiConverterFactoryTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.18 IQR)
- **Top Global Matches:** file_cluster_13: 11.18, file_cluster_0: 11.22, file_cluster_4: 11.552
- **Magnitude:** 268.74 | **LOC:** 371 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (31.2127%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MoshiConverterFactoryTest` (Impact: 42.3 | O(N^5) | DB: 2)
  * `read` (Impact: 27.6 | O(N^3))
  * `nonUtf8BomIsNotSkipped` (Impact: 16.8 | O(N^3) | DB: 1)
  * `asLenient` (Impact: 13.0 | O(N^2) | DB: 2)
  * `anInterface` (Impact: 12.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 124`, `args: 31`, `func_start: 50`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 35`, `duplicate_logic: 3`, `orphaned_logic: 8`
* *Architecture:* `api: 22`, `concurrency: 18`, `import: 36`
* *Defense:* `safety: 8`, `test: 28`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.google.testing.junit.testparameterinjector.TestParameter, okio.ByteString, java.util.concurrent.atomic.AtomicReference, com.squareup.moshi.FromJson, com.google.testing.junit.testparameterinjector.TestParameterInjector, com.squareup.moshi.JsonQualifier, retrofit2.Callback, org.junit.Assert.fail...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.612 IQR)
- **Top Global Matches:** file_cluster_13: 10.612, file_cluster_8: 10.752, file_cluster_4: 10.89
- **Magnitude:** 251.54 | **LOC:** 177 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.0642%), Tech Debt (57.8569%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 86.4 | O(N^3))
  * `emitResponse` (Impact: 73.3 | O(N^3))
  * `deliverResponse` (Impact: 42.1 | O(N^2))
  * `emitError` (Impact: 15.8 | O(N^2))
  * `CallArbiter` (Impact: 3.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 35`, `args: 7`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 8`, `orphaned_logic: 4`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 12`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` rx.exceptions.CompositeException, rx.Producer, rx.exceptions.OnErrorNotImplementedException, java.util.concurrent.atomic.AtomicInteger, rx.exceptions.Exceptions, rx.Subscriber, retrofit2.Call, rx.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.933 IQR)
- **Top Global Matches:** file_cluster_4: 11.933, file_cluster_0: 12.263, file_cluster_13: 12.292
- **Magnitude:** 251.5 | **LOC:** 338 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `syncCanBeCanceled` (Impact: 26.6 | O(N^4) | DB: 3)
  * `setUp` (Impact: 9.1 | O(N^3) | DB: 1)
  * `syncFailureThrowsAfterDelay` (Impact: 6.8 | O(N^1) | DB: 3)
  * `syncFailureThrownAfterDelay` (Impact: 6.8 | O(N^1) | DB: 3)
  * `asyncFailureTriggersFailureAfterDelay` (Impact: 5.5 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 72`, `args: 23`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 49`, `orphaned_logic: 9`
* *Architecture:* `api: 20`, `concurrency: 104`, `import: 17`
* *Defense:* `safety: 8`, `test: 30`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.util.concurrent.TimeUnit.SECONDS, java.util.concurrent.TimeUnit, java.util.concurrent.atomic.AtomicReference, retrofit2.Response, retrofit2.Call, java.io.IOException, retrofit2.Callback, retrofit2.Retrofit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.363 IQR)
- **Top Global Matches:** file_cluster_4: 11.363, file_cluster_0: 11.396, file_cluster_16: 11.544
- **Magnitude:** 248.6 | **LOC:** 342 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (87.0113%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `responseEnqueue` (Impact: 13.9 | O(N^3) | DB: 2)
  * `deferredThrowExecute` (Impact: 12.7 | O(N^3))
  * `responseExecute` (Impact: 6.7 | O(N^1))
  * `responseCancelExecute` (Impact: 6.7 | O(N^1))
  * `deferredReturnEnqueue` (Impact: 6.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 83`, `args: 36`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 15`, `orphaned_logic: 16`
* *Architecture:* `api: 35`, `concurrency: 90`, `import: 14`
* *Defense:* `safety: 14`, `test: 54`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.junit.Assert.assertFalse, java.security.cert.CertificateException, java.util.concurrent.atomic.AtomicReference, org.junit.Assert.assertSame, retrofit2.Call, java.io.IOException, org.junit.Assert.assertEquals, retrofit2.Callback...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestBuilder.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.583 IQR)
- **Top Global Matches:** file_cluster_8: 9.583, file_cluster_13: 9.757, file_cluster_0: 9.931
- **Magnitude:** 220.9 | **LOC:** 299 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (21.1588%), Tech Debt (99.0987%)
**Top Internal Functions/Classes:**
  * `addQueryParam` (Impact: 37.0 | O(N^3))
  * `canonicalizeForPath` (Impact: 30.9 | O(N^2) | DB: 1)
  * `canonicalizeForPath` (Impact: 26.9 | O(2^N))
  * `addHeader` (Impact: 24.6 | O(N^2) | DB: 1)
  * `RequestBuilder` (Impact: 19.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 49`, `args: 17`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 21`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` okhttp3.Headers, okhttp3.Request, okio.BufferedSink, okio.Buffer, okhttp3.MultipartBody, java.io.IOException, okhttp3.MediaType, javax.annotation.Nullable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RxJava2CallAdapterFactoryTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.107 IQR)
- **Top Global Matches:** file_cluster_16: 11.107, file_cluster_8: 11.226, file_cluster_13: 11.279
- **Magnitude:** 220.84 | **LOC:** 295 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.4508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rawBodyTypeThrows` (Impact: 54.2 | O(N^3))
  * `responseTypes` (Impact: 43.6 | O(N^2))
  * `rawResponseTypeThrows` (Impact: 41.0 | O(N^2))
  * `rawResultTypeThrows` (Impact: 41.0 | O(N^2))
  * `setUp` (Impact: 12.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 124`, `args: 7`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 26`, `test: 49`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.Observable, retrofit2.CallAdapter, java.util.List, io.reactivex.Single, org.junit.Test, retrofit2.Response, com.google.common.reflect.TypeToken, java.lang.reflect.Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `retrofit-converters/wire/src/test/java/retrofit2/converter/wire/Phone.java` (JAVA) | Magnitude: 168.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 36, api: 19, func_start: 17
- `retrofit-converters/jaxb/src/test/java/retrofit2/converter/jaxb/PhoneNumber.java` (JAVA) | Magnitude: 19.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, func_start: 5, decorators: 5
- `retrofit-converters/jaxb3/src/test/java/retrofit2/converter/jaxb3/PhoneNumber.java` (JAVA) | Magnitude: 19.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, func_start: 5, decorators: 5
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ResultTest.java` (JAVA) | Magnitude: 27.24 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, func_start: 14, structural_boundaries: 12, test: 12
- `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/ResultTest.java` (JAVA) | Magnitude: 27.24 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, func_start: 14, structural_boundaries: 12, test: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `website/src/content.config.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, branch: 5, structural_boundaries: 5, safety: 3
- `retrofit-converters/scalars/src/test/java/retrofit2/converter/scalars/ScalarsConverterPrimitivesFactoryTest.java` (JAVA) | Magnitude: 73.44 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 43, func_start: 26, state_mutation: 17
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/RxJavaCallAdapterFactoryTest.java` (JAVA) | Magnitude: 135.84 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 74, func_start: 36, generics: 35
- `retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/BodyObservable.java` (JAVA) | Magnitude: 103.94 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 21, listeners: 12, branch: 10
- `retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/BodyObservable.java` (JAVA) | Magnitude: 103.94 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 21, listeners: 12, generics: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `retrofit-adapters/scala/src/main/java/retrofit2/adapter/scala/ResponseCallAdapter.java` (JAVA) | Magnitude: 19.38 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, generics: 9, import: 7
- `retrofit/src/main/java/retrofit2/Response.java` (JAVA) | Magnitude: 144.52 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 37, args: 16, api: 15
- `retrofit/src/main/java/retrofit2/CallAdapter.java` (JAVA) | Magnitude: 18.28 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, doc: 7, api: 5
- `retrofit-converters/kotlinx-serialization/src/main/java/retrofit2/converter/kotlinx/serialization/DeserializationStrategyConverter.kt` (KOTLIN) | Magnitude: 20.34 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 3, import: 3, encapsulation: 3, indent_spaces: 3
- `retrofit-converters/kotlinx-serialization/src/main/java/retrofit2/converter/kotlinx/serialization/Serializer.kt` (KOTLIN) | Magnitude: 26.38 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, generics: 13, import: 12, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `website/public/2.x/converter-kotlinx-serialization/scripts/navigation-loader.js` (JAVASCRIPT) | Magnitude: 115.7 | Delta: **0.475 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 22, branch: 17, state_mutation: 17
- `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT) | Magnitude: 425.48 | Delta: **0.592 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 71, state_mutation: 71, branch: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableThrowingSafeSubscriberTest.java` (JAVA) | Magnitude: 87.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 42, concurrency: 30, import: 19
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableThrowingTest.java` (JAVA) | Magnitude: 78.86 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 40, concurrency: 30, import: 17
- `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/AsyncTest.java` (JAVA) | Magnitude: 116.5 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 71, concurrency: 54, import: 31
- `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/AsyncTest.java` (JAVA) | Magnitude: 116.48 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 70, concurrency: 54, import: 30
- `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` (JAVA) | Magnitude: 248.6 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 273, concurrency: 90, func_start: 88, structural_boundaries: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `retrofit/src/main/java/retrofit2/AndroidMainExecutor.java` (JAVA) | Magnitude: 4.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 5, import: 3, immutability_locks: 2
- `retrofit/src/main/java/retrofit2/BuiltInConverters.java` (JAVA) | Magnitude: 32.26 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 46, immutability_locks: 13, branch: 10
- `retrofit-converters/scalars/src/main/java/retrofit2/converter/scalars/ScalarsConverterFactory.java` (JAVA) | Magnitude: 9.84 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 67, indent_spaces: 63, import: 16, branch: 12
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ForwardingSubscriber.java` (JAVA) | Magnitude: 18.9 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, listeners: 6, args: 4
- `retrofit-converters/kotlinx-serialization/src/main/java/retrofit2/converter/kotlinx/serialization/SerializationStrategyConverter.kt` (KOTLIN) | Magnitude: 21.38 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: import: 4, encapsulation: 4, indent_spaces: 4, generics: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `retrofit/src/main/java/retrofit2/RequestFactory.java` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 1347.86
- `retrofit/src/main/java/retrofit2/KotlinExtensions.kt` -> **Jake Wharton** (100.0% isolated ownership) | Magnitude: 129.48
- `retrofit/java-test/src/test/java/retrofit2/InvocationTest.java` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 105.96
- `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateKotlinTest.kt` -> **Jake Wharton** (100.0% isolated ownership) | Magnitude: 85.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 21.968** (Embedded: 0.2803 * Error Risk: 78.3826%)
- `retrofit/src/main/java/retrofit2/http/GET.java` -> **Severity: 15.629** (Embedded: 0.2283 * Error Risk: 68.4615%)
- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 13.948** (Embedded: 0.2213 * Error Risk: 63.0189%)
- `retrofit/src/main/java/retrofit2/http/Header.java` -> **Severity: 12.885** (Embedded: 0.1882 * Error Risk: 68.4615%)
- `retrofit/src/main/java/retrofit2/http/Url.java` -> **Severity: 11.941** (Embedded: 0.1666 * Error Risk: 71.6667%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 5666.377** (Blast Radius: 100.004 * Doc Risk: 56.6615%)
- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 4339.323** (Blast Radius: 45.634 * Doc Risk: 95.0897%)
- `retrofit/src/main/java/retrofit2/Converter.java` -> **Severity: 1642.982** (Blast Radius: 52.271 * Doc Risk: 31.432%)
- `retrofit/src/main/java/retrofit2/http/GET.java` -> **Severity: 574.811** (Blast Radius: 55.64 * Doc Risk: 10.3309%)
- `retrofit/src/main/java/retrofit2/http/Headers.java` -> **Severity: 435.189** (Blast Radius: 42.125 * Doc Risk: 10.3309%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
