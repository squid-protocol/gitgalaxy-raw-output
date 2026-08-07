# ARCHITECTURAL_BRIEF: retrofit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/retrofit` |
| **Timestamp** | `2026-08-07T05:28:18.289335+00:00` |
| **Scan Duration** | `1.68s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `77e6ba21d9ba372d1b23ef29881912910da23347` |
| **Git Remote** | `https://github.com/square/retrofit` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 355 malicious artifacts.

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
| Modularity | 0.3795 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `4.476`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 203 | 44.8% |
| file_cluster_8 | 119 | 26.3% |
| file_cluster_0 | 28 | 6.2% |
| file_cluster_4 | 25 | 5.5% |
| file_cluster_16 | 18 | 4.0% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 20.6 | 8.3 | 0.0 |
| Error & Exception Exposure | 0.0 | 97.7 | 40.5 | 44.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.0 | 4.7 | 4.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 45.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.9 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 20.0 | 0.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 14.4 | 7.9 | 0.0 |
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

- `parseParameterAnnotation` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **353.8** | LOC: 457
- `parseMethodAnnotation` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **57.8** | LOC: 37
- `unresolvableResponseTypeThrows` (@ `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) -> Impact: **54.5** | LOC: 62
- `unresolvableParameterTypeThrows` (@ `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) -> Impact: **54.5** | LOC: 62
- `enqueue` (@ `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java`) -> Impact: **48.3** | LOC: 60
- `request` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`) -> Impact: **48.0** | LOC: 30
- `getGenericSupertype` (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **38.0** | LOC: 39
- `emitResponse` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`) -> Impact: **37.4** | LOC: 27
- `subscribeActual` (@ `retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/CallExecuteObservable.java`) -> Impact: **35.6** | LOC: 34
- `subscribeActual` (@ `retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/CallExecuteObservable.java`) -> Impact: **35.6** | LOC: 34

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `retrofit/java-test/src/test/java/retrofit2` | 17 | 5423.66 | 30.82% | 0.0% |
| `retrofit/android-test` | 1 | 5000.0 | 0.0% | 0.0% |
| `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2` | 27 | 2407.12 | 26.91% | 0.0% |
| `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3` | 27 | 2404.74 | 26.91% | 0.0% |
| `retrofit/src/main/java/retrofit2` | 28 | 2285.44 | 16.78% | 55.0% |
| `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava` | 19 | 1432.48 | 34.49% | 0.0% |
| `retrofit-mock/src/test/java/retrofit2/mock` | 5 | 892.22 | 61.58% | 0.0% |
| `retrofit-mock/src/main/java/retrofit2/mock` | 8 | 659.2 | 31.54% | 35.69% |
| `retrofit/src/main/java/retrofit2/http` | 26 | 604.76 | 5.78% | 0.0% |
| `samples/src/main/java/com/example/retrofit` | 14 | 538.74 | 14.28% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `retrofit-adapters/guava/src/main/java/retrofit2/adapter/guava/GuavaCallAdapterFactory.java` -> **100.0%** Exposure
- `retrofit-adapters/java8/src/main/java/retrofit2/adapter/java8/Java8CallAdapterFactory.java` -> **100.0%** Exposure
- `retrofit-converters/scalars/src/main/java/retrofit2/converter/scalars/ScalarResponseBodyConverters.java` -> **100.0%** Exposure
- `retrofit-converters/simplexml/src/main/java/retrofit2/converter/simplexml/SimpleXmlConverterFactory.java` -> **100.0%** Exposure
- `retrofit-mock/src/main/java/retrofit2/mock/Calls.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `website/public/1.x/converter-jackson/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-protobuf/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-simplexml/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-wire/script.js` -> **100.0%** Exposure
- `website/public/1.x/retrofit/script.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` -> **164** Orphaned Functions | **185** Duplicates
- `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` -> **72** Orphaned Functions | **64** Duplicates
- `retrofit/java-test/src/test/java/retrofit2/CallTest.java` -> **44** Orphaned Functions | **76** Duplicates
- `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` -> **16** Orphaned Functions | **26** Duplicates
- `retrofit-mock/src/test/java/retrofit2/mock/NetworkBehaviorTest.java` -> **15** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`** -> AI Confidence: **99.31%**
2. **`retrofit-mock/src/test/java/retrofit2/mock/NetworkBehaviorTest.java`** -> AI Confidence: **99.31%**
3. **`retrofit/src/main/java/retrofit2/RequestBuilder.java`** -> AI Confidence: **99.31%**
4. **`retrofit/src/main/java/retrofit2/RequestFactory.java`** -> AI Confidence: **99.31%**
5. **`retrofit/src/main/java/retrofit2/Utils.java`** -> AI Confidence: **99.31%**
6. **`retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/CallExecuteObservable.java`** -> AI Confidence: **99.24%**
7. **`retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/CallExecuteObservable.java`** -> AI Confidence: **99.24%**
8. **`retrofit/src/main/java/retrofit2/Retrofit.java`** -> AI Confidence: **99.24%**
9. **`retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/CallEnqueueObservable.java`** -> AI Confidence: **99.23%**
10. **`retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/CallEnqueueObservable.java`** -> AI Confidence: **99.23%**
11. **`retrofit/java-test/src/test/java/retrofit2/ResponseTest.java`** -> AI Confidence: **99.23%**
12. **`retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/ResultOnSubscribe.java`** -> AI Confidence: **99.18%**
13. **`retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/ResultObservable.java`** -> AI Confidence: **99.18%**
14. **`retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RecordingCompletableObserver.java`** -> AI Confidence: **99.18%**
15. **`retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/ResultObservable.java`** -> AI Confidence: **99.18%**
16. **`retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/RecordingCompletableObserver.java`** -> AI Confidence: **99.18%**
17. **`retrofit-adapters/scala/src/main/java/retrofit2/adapter/scala/ScalaCallAdapterFactory.java`** -> AI Confidence: **99.18%**
18. **`retrofit-converters/jaxb/src/test/java/retrofit2/converter/jaxb/JaxbConverterFactoryTest.java`** -> AI Confidence: **99.18%**
19. **`retrofit-converters/jaxb3/src/test/java/retrofit2/converter/jaxb3/JaxbConverterFactoryTest.java`** -> AI Confidence: **99.18%**
20. **`retrofit-converters/moshi/src/main/java/retrofit2/converter/moshi/MoshiResponseBodyConverter.java`** -> AI Confidence: **99.18%**
21. **`retrofit-converters/protobuf/src/main/java/retrofit2/converter/protobuf/ProtoResponseBodyConverter.java`** -> AI Confidence: **99.18%**
22. **`retrofit-converters/scalars/src/test/java/retrofit2/converter/scalars/ScalarsConverterFactoryTest.java`** -> AI Confidence: **99.18%**
23. **`retrofit-converters/wire/src/test/java/retrofit2/converter/wire/CrashingPhone.java`** -> AI Confidence: **99.18%**
24. **`retrofit-converters/wire/src/test/java/retrofit2/converter/wire/WireConverterFactoryTest.java`** -> AI Confidence: **99.18%**
25. **`retrofit-mock/src/main/java/retrofit2/mock/BehaviorDelegate.java`** -> AI Confidence: **99.18%**
26. **`retrofit-mock/src/main/java/retrofit2/mock/NetworkBehavior.java`** -> AI Confidence: **99.18%**
27. **`retrofit/java-test/src/test/java/retrofit2/AnnotationArraySubject.java`** -> AI Confidence: **99.18%**
28. **`retrofit/java-test/src/test/java/retrofit2/CallAdapterTest.java`** -> AI Confidence: **99.18%**
29. **`retrofit/java-test/src/test/java/retrofit2/InvocationTest.java`** -> AI Confidence: **99.18%**
30. **`retrofit/kotlin-test/src/test/java/retrofit2/KotlinSuspendRawTest.java`** -> AI Confidence: **99.18%**
31. **`retrofit/src/main/java/retrofit2/CompletableFutureCallAdapterFactory.java`** -> AI Confidence: **99.18%**
32. **`retrofit/src/main/java/retrofit2/DefaultCallAdapterFactory.java`** -> AI Confidence: **99.18%**
33. **`retrofit/src/main/java/retrofit2/OkHttpCall.java`** -> AI Confidence: **99.18%**
34. **`samples/src/main/java/com/example/retrofit/AnnotatedConverters.java`** -> AI Confidence: **99.18%**
35. **`samples/src/main/java/com/example/retrofit/ErrorHandlingAdapter.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `31` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3184` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java` (JAVA) -> Cumulative Risk: **672.75**
- **Archetype:** `file_cluster_4` (Distance: 10.838 IQR)
- **Magnitude:** 221.86 | **LOC:** 178 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9958%)
- **Heaviest Functions:** `enqueue` (Impact: 48.3), `run` (Impact: 26.2), `execute` (Impact: 15.0)

### 2. `website/public/2.x/converter-kotlinx-serialization/scripts/navigation-loader.js` (JAVASCRIPT) -> Cumulative Risk: **594.37**
- **Archetype:** `file_cluster_17` (Distance: 14.474 IQR)
- **Magnitude:** 64.1 | **LOC:** 96 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.8015%), Concurrency (93.8856%)
- **Heaviest Functions:** `revealNavigationForCurrentPage` (Impact: 13.0), `scrollNavigationToSelectedElement` (Impact: 9.9), `revealParents` (Impact: 5.5)

### 3. `retrofit-mock/src/main/java/retrofit2/mock/Calls.java` (JAVA) -> Cumulative Risk: **581.01**
- **Archetype:** `file_cluster_0` (Distance: 10.419 IQR)
- **Magnitude:** 165.2 | **LOC:** 215 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9985%), Documentation (90.3286%)
- **Heaviest Functions:** `enqueue` (Impact: 19.4), `execute` (Impact: 9.6), `getDelegate` (Impact: 9.5)

### 4. `retrofit/android-test/src/androidTest/java/retrofit2/CompletableFutureAndroidTest.java` (JAVA) -> Cumulative Risk: **528.41**
- **Archetype:** `file_cluster_13` (Distance: 9.898 IQR)
- **Magnitude:** 25.0 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (96.1368%), Cognitive Load (95.865%)
- **Heaviest Functions:** `setUp` (Impact: 2.7), `completableFutureApi24` (Impact: 2.6)

### 5. `retrofit-mock/src/main/java/retrofit2/mock/NetworkBehavior.java` (JAVA) -> Cumulative Risk: **510.72**
- **Archetype:** `file_cluster_13` (Distance: 11.692 IQR)
- **Magnitude:** 126.64 | **LOC:** 212 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4068%), Documentation (97.0438%), Safety Score (92.2017%)
- **Heaviest Functions:** `createErrorResponse` (Impact: 14.8), `setErrorFactory` (Impact: 7.7), `create` (Impact: 5.5)

### 6. `retrofit/src/main/java/retrofit2/CompletableFutureCallAdapterFactory.java` (JAVA) -> Cumulative Risk: **502.3**
- **Archetype:** `file_cluster_16` (Distance: 9.594 IQR)
- **Magnitude:** 70.04 | **LOC:** 158 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9102%), Documentation (74.9164%)
- **Heaviest Functions:** `onResponse` (Impact: 5.6), `cancel` (Impact: 5.2), `CallCancelCompletableFuture` (Impact: 4.2)

### 7. `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java` (JAVA) -> Cumulative Risk: **477.93**
- **Archetype:** `file_cluster_13` (Distance: 10.612 IQR)
- **Magnitude:** 165.24 | **LOC:** 177 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (97.6989%), Verification (80.0%), Tech Debt (57.8569%)
- **Heaviest Functions:** `request` (Impact: 48.0), `emitResponse` (Impact: 37.4), `deliverResponse` (Impact: 28.7)

### 8. `retrofit-adapters/java8/src/main/java/retrofit2/adapter/java8/Java8CallAdapterFactory.java` (JAVA) -> Cumulative Risk: **472.09**
- **Archetype:** `file_cluster_16` (Distance: 9.476 IQR)
- **Magnitude:** 82.12 | **LOC:** 176 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.5394%), Documentation (67.4838%)
- **Heaviest Functions:** `adapt` (Impact: 12.2), `adapt` (Impact: 6.7), `onResponse` (Impact: 5.6)

### 9. `retrofit/src/main/java/retrofit2/RequestBuilder.java` (JAVA) -> Cumulative Risk: **453.69**
- **Archetype:** `file_cluster_8` (Distance: 9.631 IQR)
- **Magnitude:** 189.0 | **LOC:** 299 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.0987%), Safety Score (86.2949%), Verification (80.0%)
- **Heaviest Functions:** `get` (Impact: 29.7), `canonicalizeForPath` (Impact: 21.1), `RequestBuilder` (Impact: 19.6)

### 10. `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT) -> Cumulative Risk: **444.32**
- **Archetype:** `file_cluster_17` (Distance: 11.95 IQR)
- **Magnitude:** 306.48 | **LOC:** 372 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9264%), State Flux (99.5031%), Safety Score (51.5175%)
- **Heaviest Functions:** `handleAnchor` (Impact: 24.9), `togglePlatformDependent` (Impact: 20.1), `darkModeSwitch` (Impact: 11.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `retrofit/android-test/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_0` (Drift: 11.819 IQR)
- **Top Global Matches:** file_cluster_0: 11.819, file_cluster_8: 12.144, file_cluster_16: 12.384
- **Magnitude:** 2207.02 | **LOC:** 3422 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `malformedAnnotationRelativeUrlThrows` (Impact: 18.7)
  * `malformedParameterRelativeUrlThrows` (Impact: 18.7)
  * `headWithoutVoidThrows` (Impact: 17.9)
  * `twoMethodsFail` (Impact: 16.7)
  * `multipartPartMapWithEncoding` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 861`, `args: 336`, `func_start: 422`, `class_start: 172`
* *Risk/State:* `safety_bypasses: 227`, `state_mutation: 76`, `duplicate_logic: 185`, `orphaned_logic: 164`
* *Architecture:* `io: 34`, `api: 168`, `import: 49`
* *Defense:* `safety: 145`, `test: 652`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` retrofit2.http.Path, retrofit2.http.HeaderMap, retrofit2.http.POST, retrofit2.http.Url, java.util.HashMap, java.util.List, retrofit2.http.DELETE, retrofit2.http.Field...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.064 IQR)
- **Top Global Matches:** file_cluster_0: 12.064, file_cluster_4: 12.128, file_cluster_8: 12.398
- **Magnitude:** 1563.24 | **LOC:** 1806 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.1602%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unresolvableResponseTypeThrows` (Impact: 54.5)
  * `unresolvableParameterTypeThrows` (Impact: 54.5)
  * `callAdapterFactoryQueriedCanDelegateTwic` (Impact: 29.8)
  * `annotationParsingFailureObservedByWaitin` (Impact: 26.6)
  * `baseUrlNoTrailingSlashThrows` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 505`, `args: 133`, `func_start: 158`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 89`, `duplicate_logic: 64`, `orphaned_logic: 72`
* *Architecture:* `api: 117`, `concurrency: 299`, `import: 45`
* *Defense:* `safety: 80`, `doc: 1`, `test: 197`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` retrofit2.http.POST, org.junit.Assert.assertNotNull, java.util.Set, org.junit.Assert.assertEquals, java.lang.annotation.Retention, java.util.List, java.util.concurrent.atomic.AtomicReference, retrofit2.helpers.DelegatingCallAdapterFactory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/CallTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.509 IQR)
- **Top Global Matches:** file_cluster_4: 11.509, file_cluster_0: 11.574, file_cluster_8: 11.844
- **Magnitude:** 949.56 | **LOC:** 1522 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.8652%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `conversionProblemIncomingMaskedByConvert` (Impact: 13.9)
  * `fatalErrorsAreNotCaughtEnqueue` (Impact: 13.6)
  * `requestThrowingBeforeExecuteFailsExecute` (Impact: 13.1)
  * `requestThrowingNonFatalErrorBeforeExecut` (Impact: 13.1)
  * `requestAfterExecuteThrowingAlsoThrows` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 434`, `args: 100`, `func_start: 125`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 92`, `duplicate_logic: 76`, `orphaned_logic: 44`
* *Architecture:* `io: 2`, `api: 96`, `concurrency: 282`, `import: 33`
* *Defense:* `safety: 56`, `test: 155`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` retrofit2.http.Path, retrofit2.http.POST, okio.ForwardingSource, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.http.Body, okio.Okio, java.io.IOException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.599 IQR)
- **Top Global Matches:** file_cluster_8: 10.599, file_cluster_13: 10.728, file_cluster_16: 10.887
- **Magnitude:** 637.16 | **LOC:** 873 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.2234%), Tech Debt (98.4336%)
**Top Internal Functions/Classes:**
  * `parseParameterAnnotation` (Impact: 353.8)
  * `parseMethodAnnotation` (Impact: 57.8)
  * `boxIfPrimitive` (Impact: 27.5)
  * `parseHeaders` (Impact: 25.4)
    * *Intent:* // Get the relative URL path and existing query string, if present.
  * `build` (Impact: 24.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 178`, `args: 13`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 9`, `duplicate_logic: 20`, `orphaned_logic: 1`
* *Architecture:* `io: 12`, `import: 45`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` retrofit2.http.Path, retrofit2.http.HeaderMap, retrofit2.http.POST, retrofit2.http.Url, java.util.Set, java.util.regex.Matcher, java.util.List, retrofit2.http.DELETE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.95 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.094 IQR)
- **Top Global Matches:** file_cluster_17: 11.95, file_cluster_8: 12.571, file_cluster_11: 12.657
- **Magnitude:** 306.48 | **LOC:** 372 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.2278%), Tech Debt (99.9264%)
**Top Internal Functions/Classes:**
  * `handleAnchor` (Impact: 24.9)
  * `togglePlatformDependent` (Impact: 20.1)
  * `darkModeSwitch` (Impact: 11.5)
  * `refreshPlatformTabs` (Impact: 11.5)
  * `searchForContentTarget` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 71`, `args: 49`, `func_start: 53`
* *Risk/State:* `state_mutation: 71`, `dead_code: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 4`, `api: 6`, `concurrency: 1`
* *Defense:* `safety: 31`, `doc: 1`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/FlowableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.795 IQR)
- **Top Global Matches:** file_cluster_4: 11.795, file_cluster_0: 12.062, file_cluster_13: 12.112
- **Magnitude:** 294.34 | **LOC:** 348 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 6.2)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 6.0)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 93`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 13`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.exceptions.CompositeException, org.reactivestreams.Subscription, retrofit2.Retrofit, java.util.concurrent.atomic.AtomicReference, io.reactivex.Flowable, okhttp3.mockwebserver.MockResponse, retrofit2.Response, io.reactivex.exceptions.Exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/ObservableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.795 IQR)
- **Top Global Matches:** file_cluster_4: 11.795, file_cluster_0: 12.062, file_cluster_13: 12.112
- **Magnitude:** 294.34 | **LOC:** 348 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 6.2)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 6.0)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 93`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 13`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.exceptions.CompositeException, retrofit2.Retrofit, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response, io.reactivex.exceptions.Exceptions, org.junit.Before, io.reactivex.Observer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/FlowableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.825 IQR)
- **Top Global Matches:** file_cluster_4: 11.825, file_cluster_0: 12.093, file_cluster_13: 12.157
- **Magnitude:** 293.6 | **LOC:** 338 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 6.2)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 5.8)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 89`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 13`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 18`
* *Defense:* `test: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.rxjava3.plugins.RxJavaPlugins, io.reactivex.rxjava3.exceptions.Exceptions, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, org.junit.Before, retrofit2.Response, io.reactivex.rxjava3.exceptions.CompositeException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/ObservableThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.825 IQR)
- **Top Global Matches:** file_cluster_4: 11.825, file_cluster_0: 12.093, file_cluster_13: 12.157
- **Magnitude:** 293.6 | **LOC:** 338 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 6.2)
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 5.8)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 89`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 13`, `orphaned_logic: 10`
* *Architecture:* `api: 28`, `concurrency: 102`, `import: 18`
* *Defense:* `test: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.rxjava3.plugins.RxJavaPlugins, io.reactivex.rxjava3.exceptions.Exceptions, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, org.junit.Before, retrofit2.Response, io.reactivex.rxjava3.exceptions.CompositeException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.167 IQR)
- **Top Global Matches:** file_cluster_4: 11.167, file_cluster_0: 11.216, file_cluster_16: 11.398
- **Magnitude:** 282.5 | **LOC:** 342 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `responseEnqueue` (Impact: 8.7)
  * `deferredThrowExecute` (Impact: 7.5)
  * `responseExecute` (Impact: 7.4)
  * `responseCancelExecute` (Impact: 7.4)
  * `failureExecute` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 83`, `args: 36`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 15`, `duplicate_logic: 26`, `orphaned_logic: 16`
* *Architecture:* `api: 35`, `concurrency: 90`, `import: 14`
* *Defense:* `safety: 14`, `test: 54`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, retrofit2.Call, retrofit2.Response, java.util.concurrent.Callable, java.io.IOException, org.junit.Assert.assertEquals, org.junit.Assert.assertFalse, org.junit.Assert.fail...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Utils.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.691 IQR)
- **Top Global Matches:** file_cluster_8: 10.691, file_cluster_13: 10.773, file_cluster_0: 10.78
- **Magnitude:** 279.84 | **LOC:** 558 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.383%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `getGenericSupertype` (Impact: 38.0)
  * `hasUnresolvableType` (Impact: 30.9)
  * `getRawType` (Impact: 23.6)
  * `WildcardTypeImpl` (Impact: 14.7)
  * `throwIfFatal` (Impact: 13.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 100`, `args: 32`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 30`, `duplicate_logic: 17`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 26`, `doc: 5`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.lang.annotation.Annotation, java.lang.reflect.Method, java.lang.reflect.ParameterizedType, java.lang.reflect.WildcardType, java.io.IOException, java.util.Arrays, java.lang.reflect.GenericArrayType, java.lang.reflect.GenericDeclaration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/MaybeThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.031 IQR)
- **Top Global Matches:** file_cluster_4: 12.031, file_cluster_13: 12.35, file_cluster_0: 12.362
- **Magnitude:** 278.86 | **LOC:** 287 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 14.5)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 5.9)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 79`, `args: 28`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 9`, `orphaned_logic: 7`
* *Architecture:* `api: 22`, `concurrency: 102`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.exceptions.CompositeException, retrofit2.Retrofit, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response, io.reactivex.exceptions.Exceptions, org.junit.Ignore, io.reactivex.Maybe...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/MaybeThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.083 IQR)
- **Top Global Matches:** file_cluster_4: 12.083, file_cluster_0: 12.414, file_cluster_13: 12.416
- **Magnitude:** 278.42 | **LOC:** 280 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 14.5)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 5.8)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 75`, `args: 28`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 9`, `orphaned_logic: 7`
* *Architecture:* `api: 22`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.rxjava3.disposables.Disposable, retrofit2.Retrofit, io.reactivex.rxjava3.plugins.RxJavaPlugins, io.reactivex.rxjava3.exceptions.Exceptions, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response, org.junit.Ignore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/SingleThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.044 IQR)
- **Top Global Matches:** file_cluster_4: 12.044, file_cluster_13: 12.362, file_cluster_0: 12.386
- **Magnitude:** 275.4 | **LOC:** 284 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 14.5)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 5.9)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 78`, `args: 27`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 9`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `concurrency: 102`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.exceptions.CompositeException, retrofit2.Retrofit, io.reactivex.SingleObserver, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response, io.reactivex.exceptions.Exceptions, io.reactivex.Single...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/SingleThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.098 IQR)
- **Top Global Matches:** file_cluster_4: 12.098, file_cluster_13: 12.429, file_cluster_0: 12.439
- **Magnitude:** 274.96 | **LOC:** 277 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 14.5)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 8.3)
  * `responseThrowingInOnErrorDeliveredToPlug` (Impact: 8.3)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 5.8)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 74`, `args: 27`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `duplicate_logic: 9`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `concurrency: 102`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.rxjava3.disposables.Disposable, retrofit2.Retrofit, io.reactivex.rxjava3.plugins.RxJavaPlugins, io.reactivex.rxjava3.exceptions.Exceptions, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response, org.junit.Ignore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.746 IQR)
- **Top Global Matches:** file_cluster_4: 11.746, file_cluster_0: 12.091, file_cluster_13: 12.125
- **Magnitude:** 257.2 | **LOC:** 338 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `syncCanBeCanceled` (Impact: 12.9)
  * `syncFailureThrowsAfterDelay` (Impact: 7.6)
  * `syncFailureThrownAfterDelay` (Impact: 7.6)
  * `setUp` (Impact: 5.6)
  * `asyncFailureTriggersFailureAfterDelay` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 72`, `args: 22`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 49`, `duplicate_logic: 11`, `orphaned_logic: 9`
* *Architecture:* `api: 20`, `concurrency: 104`, `import: 17`
* *Defense:* `safety: 8`, `test: 30`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.util.concurrent.atomic.AtomicReference, retrofit2.Call, java.util.concurrent.TimeUnit, org.junit.Before, retrofit2.Response, java.io.IOException, java.util.concurrent.CountDownLatch, java.util.concurrent.TimeUnit.SECONDS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Retrofit.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.116 IQR)
- **Top Global Matches:** file_cluster_13: 11.116, file_cluster_16: 11.245, file_cluster_8: 11.47
- **Magnitude:** 254.7 | **LOC:** 717 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.5526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateServiceInterface` (Impact: 28.4)
  * `loadServiceMethod` (Impact: 26.6)
    * *Intent:* * Create an implementation of the API endpoints defined by the {@code service} interface. * * <p>The...
  * `create` (Impact: 21.0)
    * *Intent:* * * <pre><code> * Retrofit retrofit = new Retrofit.Builder() * .baseUrl("https://api.example.com/") ...
  * `build` (Impact: 14.3)
  * `nextRequestBodyConverter` (Impact: 11.8)
    * *Intent:* // On successful lock insertion, perform the work and update the map before releasing. // Other thre...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 91`, `args: 25`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 24`, `duplicate_logic: 16`
* *Architecture:* `api: 35`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 20`, `doc: 36`, `sync_locks: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 100.004
  * `Choke Point (Betweenness):` 0.002682 | `Ripple Effect (Closeness):` 0.280261
  * `Imports (Out-Degree: 4):` java.util.concurrent.ConcurrentHashMap, java.lang.reflect.Modifier, retrofit2.http.Url, java.util.List, retrofit2.http.HTTP, java.util.ArrayList, java.util.Deque, java.lang.reflect.Proxy...
  * `Imported By (In-Degree: 133):` (Excluded from Brief to save tokens)

### `retrofit-mock/src/test/java/retrofit2/mock/NetworkBehaviorTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.994 IQR)
- **Top Global Matches:** file_cluster_0: 12.994, file_cluster_13: 13.151, file_cluster_8: 13.39
- **Magnitude:** 232.1 | **LOC:** 235 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.4817%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `delayVarianceIsAccurate` (Impact: 12.4)
  * `varianceRestrictsRange` (Impact: 11.9)
    * *Intent:* // Exact instance check as opposed to isInstanceOf's subtype checking.
  * `failureRestrictsRange` (Impact: 11.9)
  * `errorRestrictsRange` (Impact: 11.9)
  * `failurePercentageIsAccurate` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 35`, `args: 18`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 60`, `duplicate_logic: 12`, `orphaned_logic: 15`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 24`, `test: 40`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` retrofit2.Response, java.util.concurrent.Callable, java.io.IOException, org.junit.Assert.assertEquals, java.util.concurrent.TimeUnit.SECONDS, java.util.Random, okhttp3.ResponseBody, org.junit.Assert.fail...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-converters/moshi/src/test/java/retrofit2/converter/moshi/MoshiConverterFactoryTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.087 IQR)
- **Top Global Matches:** file_cluster_13: 11.087, file_cluster_0: 11.123, file_cluster_4: 11.457
- **Magnitude:** 223.54 | **LOC:** 371 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.2127%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 15.5)
  * `MoshiConverterFactoryTest` (Impact: 15.5)
  * `asLenient` (Impact: 10.0)
  * `nonUtf8BomIsNotSkipped` (Impact: 9.7)
  * `failOnUnknown` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 124`, `args: 29`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 35`, `duplicate_logic: 9`, `orphaned_logic: 10`
* *Architecture:* `api: 22`, `concurrency: 18`, `import: 36`
* *Defense:* `safety: 8`, `test: 28`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` retrofit2.http.POST, org.junit.Assert.assertEquals, java.io.EOFException, java.lang.annotation.Retention, retrofit2.Retrofit, org.junit.Assume.assumeTrue, java.util.concurrent.atomic.AtomicReference, retrofit2.Call...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.838 IQR)
- **Top Global Matches:** file_cluster_4: 10.838, file_cluster_0: 11.083, file_cluster_13: 11.143
- **Magnitude:** 221.86 | **LOC:** 178 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9958%)
**Top Internal Functions/Classes:**
  * `enqueue` (Impact: 48.3)
  * `run` (Impact: 26.2)
  * `execute` (Impact: 15.0)
  * `delaySleep` (Impact: 7.5)
  * `cancel` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 45`, `args: 15`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 11`, `duplicate_logic: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 13`, `concurrency: 60`, `import: 13`
* *Defense:* `safety: 6`, `sync_locks: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.util.concurrent.atomic.AtomicReference, javax.annotation.concurrent.GuardedBy, retrofit2.Call, retrofit2.Response, java.io.IOException, java.util.concurrent.CountDownLatch, okio.Timeout, java.util.concurrent.Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/RxJava2CallAdapterFactoryTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.795 IQR)
- **Top Global Matches:** file_cluster_16: 10.795, file_cluster_8: 10.915, file_cluster_13: 10.955
- **Magnitude:** 207.14 | **LOC:** 295 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `responseTypes` (Impact: 33.7)
  * `rawBodyTypeThrows` (Impact: 31.4)
  * `rawResponseTypeThrows` (Impact: 31.2)
  * `rawResultTypeThrows` (Impact: 31.2)
  * `setUp` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 124`, `args: 7`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `duplicate_logic: 13`, `orphaned_logic: 7`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 26`, `test: 49`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io.reactivex.Observable, io.reactivex.Flowable, retrofit2.Response, io.reactivex.Maybe, java.lang.annotation.Annotation, org.junit.Before, retrofit2.CallAdapter, java.lang.reflect.Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/RxJava3CallAdapterFactoryTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.795 IQR)
- **Top Global Matches:** file_cluster_16: 10.795, file_cluster_8: 10.915, file_cluster_13: 10.955
- **Magnitude:** 207.14 | **LOC:** 295 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `responseTypes` (Impact: 33.7)
  * `rawBodyTypeThrows` (Impact: 31.4)
  * `rawResponseTypeThrows` (Impact: 31.2)
  * `rawResultTypeThrows` (Impact: 31.2)
  * `setUp` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 124`, `args: 7`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `duplicate_logic: 13`, `orphaned_logic: 7`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 26`, `test: 49`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` retrofit2.Response, java.lang.annotation.Annotation, org.junit.Before, io.reactivex.rxjava3.core.Single, io.reactivex.rxjava3.core.Maybe, retrofit2.CallAdapter, io.reactivex.rxjava3.core.Observable, com.google.common.reflect.TypeToken...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/SingleThrowingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.681 IQR)
- **Top Global Matches:** file_cluster_4: 10.681, file_cluster_13: 10.936, file_cluster_0: 11.01
- **Magnitude:** 200.76 | **LOC:** 293 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleError` (Impact: 10.4)
  * `resultThrowingInOnSuccessDeliveredToPlug` (Impact: 10.2)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 8.5)
  * `responseThrowingInOnSuccessDeliveredToPl` (Impact: 8.5)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 67`, `args: 19`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 15`, `duplicate_logic: 10`, `orphaned_logic: 5`
* *Architecture:* `api: 19`, `concurrency: 78`, `import: 20`
* *Defense:* `test: 8`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rx.exceptions.Exceptions, com.google.common.truth.Truth.assertThat, rx.plugins.RxJavaErrorHandler, retrofit2.Retrofit, rx.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingSafeSubscriberTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.633 IQR)
- **Top Global Matches:** file_cluster_4: 10.633, file_cluster_0: 10.819, file_cluster_13: 10.854
- **Magnitude:** 192.8 | **LOC:** 344 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.8389%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnCompleteDeliveredToPlugi` (Impact: 10.8)
  * `responseThrowingInOnCompleteDeliveredToP` (Impact: 10.8)
  * `resultThrowingInOnCompletedDeliveredToPl` (Impact: 8.7)
  * `handleError` (Impact: 7.7)
  * `handleError` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 72`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 13`, `duplicate_logic: 10`, `orphaned_logic: 7`
* *Architecture:* `api: 21`, `concurrency: 66`, `import: 19`
* *Defense:* `safety: 3`, `test: 13`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rx.exceptions.Exceptions, rx.plugins.RxJavaErrorHandler, retrofit2.Retrofit, rx.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, retrofit2.Response, rx.exceptions.CompositeException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `retrofit-converters/wire/src/test/java/retrofit2/converter/wire/Phone.java` (JAVA) | Magnitude: 95.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 36, api: 19, func_start: 17
- `retrofit-converters/jaxb/src/test/java/retrofit2/converter/jaxb/PhoneNumber.java` (JAVA) | Magnitude: 13.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, func_start: 5, decorators: 5
- `retrofit-converters/jaxb3/src/test/java/retrofit2/converter/jaxb3/PhoneNumber.java` (JAVA) | Magnitude: 13.76 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, func_start: 5, decorators: 5
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ResultTest.java` (JAVA) | Magnitude: 29.84 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 12, test: 12, func_start: 6
- `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/ResultTest.java` (JAVA) | Magnitude: 29.84 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 12, test: 12, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `website/src/content.config.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, branch: 5, structural_boundaries: 5, safety: 3
- `retrofit-converters/scalars/src/test/java/retrofit2/converter/scalars/ScalarsConverterPrimitivesFactoryTest.java` (JAVA) | Magnitude: 80.94 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 43, state_mutation: 17, func_start: 16
- `retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/BodyObservable.java` (JAVA) | Magnitude: 47.64 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 21, listeners: 12, branch: 10
- `retrofit/kotlin-test/src/test/java/retrofit2/KotlinExtensionsTest.kt` (KOTLIN) | Magnitude: 2.4 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, import: 4, class_start: 2
- `retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/BodyObservable.java` (JAVA) | Magnitude: 47.64 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 21, listeners: 12, generics: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `retrofit-adapters/scala/src/main/java/retrofit2/adapter/scala/ResponseCallAdapter.java` (JAVA) | Magnitude: 19.38 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, generics: 9, import: 7
- `retrofit/src/main/java/retrofit2/Response.java` (JAVA) | Magnitude: 65.52 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 37, api: 15, doc: 14
- `retrofit/src/main/java/retrofit2/CallAdapter.java` (JAVA) | Magnitude: 21.18 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, doc: 7, api: 5
- `retrofit/src/main/java/retrofit2/HttpServiceMethod.java` (JAVA) | Magnitude: 74.84 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 45, generics: 44, branch: 28
- `retrofit/src/main/java/retrofit2/CompletableFutureCallAdapterFactory.java` (JAVA) | Magnitude: 70.04 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 46, generics: 31, decorators: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `website/public/2.x/converter-kotlinx-serialization/scripts/navigation-loader.js` (JAVASCRIPT) | Magnitude: 64.1 | Delta: **0.474 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 22, branch: 17, state_mutation: 17
- `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT) | Magnitude: 306.48 | Delta: **0.621 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 71, state_mutation: 71, branch: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableThrowingSafeSubscriberTest.java` (JAVA) | Magnitude: 80.94 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 42, concurrency: 30, import: 19
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/CompletableThrowingTest.java` (JAVA) | Magnitude: 75.96 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 40, concurrency: 30, import: 17
- `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/AsyncTest.java` (JAVA) | Magnitude: 112.7 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 71, concurrency: 54, import: 31
- `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/AsyncTest.java` (JAVA) | Magnitude: 112.68 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 70, concurrency: 54, import: 30
- `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` (JAVA) | Magnitude: 282.5 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 273, concurrency: 90, structural_boundaries: 83, generics: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `retrofit/src/main/java/retrofit2/AndroidMainExecutor.java` (JAVA) | Magnitude: 4.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 5, import: 3, immutability_locks: 2
- `retrofit/src/main/java/retrofit2/BuiltInConverters.java` (JAVA) | Magnitude: 30.76 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 46, immutability_locks: 13, branch: 10
- `retrofit/java-test/src/test/java/retrofit2/ResponseTest.java` (JAVA) | Magnitude: 129.0 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 175, test: 68, structural_boundaries: 32, func_start: 24
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ForwardingSubscriber.java` (JAVA) | Magnitude: 13.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, listeners: 6, args: 4
- `retrofit-converters/scalars/src/main/java/retrofit2/converter/scalars/ScalarsConverterFactory.java` (JAVA) | Magnitude: 9.84 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 67, indent_spaces: 63, import: 16, branch: 12

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `retrofit/src/main/java/retrofit2/RequestFactory.java` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 637.16
- `retrofit/java-test/src/test/java/retrofit2/InvocationTest.java` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 111.36
- `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateKotlinTest.kt` -> **Jake Wharton** (100.0% isolated ownership) | Magnitude: 67.36
- `retrofit/src/main/java/retrofit2/KotlinExtensions.kt` -> **Jake Wharton** (100.0% isolated ownership) | Magnitude: 52.28

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

- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 2922.278** (Blast Radius: 45.634 * Doc Risk: 64.0373%)
- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 1493.19** (Blast Radius: 100.004 * Doc Risk: 14.9313%)
- `retrofit/src/main/java/retrofit2/Converter.java` -> **Severity: 1251.927** (Blast Radius: 52.271 * Doc Risk: 23.9507%)
- `retrofit/src/main/java/retrofit2/http/GET.java` -> **Severity: 574.811** (Blast Radius: 55.64 * Doc Risk: 10.3309%)
- `retrofit/src/main/java/retrofit2/http/Headers.java` -> **Severity: 435.189** (Blast Radius: 42.125 * Doc Risk: 10.3309%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
