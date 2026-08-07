# ARCHITECTURAL_BRIEF: okhttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/okhttp` |
| **Timestamp** | `2026-08-07T05:19:26.232218+00:00` |
| **Scan Duration** | `2.36s` |
| **Git Branch** | `master` |
| **Git Commit** | `c396b08f7a06e412c4cc8f5c83b0d7ed19f7fa6c` |
| **Git Remote** | `https://github.com/square/okhttp` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 609 malicious artifacts.

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
| Total Artifacts | 794 |
| Analyzed Artifacts (Scanned) | 673 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 121 |
| Total LOC | 77776 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 84.8% |
| Dominant Lang | KOTLIN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4562 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1705 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1234 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| KOTLIN | 532 | 74188 | 79.0% |
| JAVA | 71 | 2792 | 10.5% |
| MARKDOWN | 29 | 0 | 4.3% |
| PLAINTEXT | 17 | 0 | 2.5% |
| XML | 11 | 0 | 1.6% |
| JSON | 7 | 384 | 1.0% |
| SHELL | 4 | 215 | 0.6% |
| BATCH | 2 | 197 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.288`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 320 | 47.5% |
| file_cluster_13 | 278 | 41.3% |
| file_cluster_0 | 18 | 2.7% |
| file_cluster_16 | 8 | 1.2% |
| file_cluster_12 | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_11 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 6.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 121*

**Composition by Extension & Reason:**
- `.kts`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 45 LOC)
- `.api`: 15x Excluded (Unsupported Extension: '.api')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 249 LOC)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.pro), 1x Excluded (Unsupported Extension: '.pro')
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 1x Excluded (Machine-Generated Source Code Signature: 4 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.config`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.list`: 2x Excluded (Binary Format Detected)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 19.6 | 10.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.1 | 41.6 | 51.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 44.1 | 28.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.5 | 2.3 | 0.0 |
| API Exposure | 0.0 | 12.6 | 2.2 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.7 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 90.3 | 6.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.7 | 15.1 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `maven-tests/mvnw` (Hits: 85)
- `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt` (Hits: 40)
- `okhttp/src/jvmTest/kotlin/okhttp3/OkHttpClientTest.kt` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Request.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Request.kt`) — 125 inbound connections
2. **OkHttpClient.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt`) — 115 inbound connections
3. **Response.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt`) — 86 inbound connections
4. **PlatformRule.kt** (`okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt`) — 56 inbound connections
5. **MockWebServer.kt** (`mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt`) — 55 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CallTest.kt** (`okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt`) — 124 outbound dependencies
2. **OkHttpTest.kt** (`android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt`) — 96 outbound dependencies
3. **EventListenerTest.kt** (`okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt`) — 89 outbound dependencies
4. **URLConnectionTest.kt** (`okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt`) — 86 outbound dependencies
5. **HttpOverHttp2Test.kt** (`okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/HttpOverHttp2Test.kt`) — 83 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `native_path_[Truncated]` (@ `maven-tests/mvnw`) -> Impact: **182.3** | LOC: 224
  * *Intent:* # OS specific support.
- `constructor` (@ `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt`) -> Impact: **138.5** | LOC: 450
- `intercept` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheInterceptor.kt`) -> Impact: **133.8** | LOC: 237
- `constructor` (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **129.8** | LOC: 276
- `intercept` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RetryAndFollowUpInterceptor.kt`) -> Impact: **114.2** | LOC: 165
- `intercept` (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **110.3** | LOC: 167
  * *Intent:* /** * Logs request and response lines and their respective headers and bodies (if present). *
- `writeCanonicalized` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/url/-Url.kt`) -> Impact: **109.1** | LOC: 60
- `isValid` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt`) -> Impact: **93.4** | LOC: 239
- `main` (@ `samples/slack/src/main/java/okhttp3/slack/SlackClient.java`) -> Impact: **91.9** | LOC: 25
- `intercept` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/CallServerInterceptor.kt`) -> Impact: **83.8** | LOC: 157

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `okhttp/src/jvmTest/kotlin/okhttp3` | 85 | 7443.01 | 15.46% | 85.66% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3` | 40 | 3032.52 | 27.7% | 24.66% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection` | 21 | 2125.76 | 23.67% | 37.59% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2` | 15 | 1456.94 | 22.02% | 37.67% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http` | 13 | 1385.11 | 39.73% | 18.2% |
| `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2` | 9 | 1160.84 | 14.9% | 83.24% |
| `okhttp-testing-support/src/main/kotlin/okhttp3` | 30 | 1124.34 | 25.63% | 43.72% |
| `samples/guide/src/main/java/okhttp3/recipes` | 30 | 1084.16 | 10.08% | 71.88% |
| `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der` | 11 | 984.3 | 27.4% | 54.19% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache` | 5 | 956.18 | 31.93% | 15.84% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/QueueDispatcher.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/CallEvent.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSSLSocketFactory.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingServerSocketFactory.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSocketFactory.kt` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `build-logic/src/main/kotlin/okhttp.jvm-conventions.gradle.kts` -> **100.0%** Exposure
- `build-logic/src/main/kotlin/okhttp.publish-conventions.gradle.kts` -> **100.0%** Exposure
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/RecordedRequest.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/TestValueFactory.kt` -> **100.0%** Exposure
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/AnyValue.kt` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -> **70** Orphaned Functions | **22** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` -> **73** Orphaned Functions | **4** Duplicates
- `okhttp-tls/src/test/java/okhttp3/tls/internal/der/DerTest.kt` -> **0** Orphaned Functions | **75** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **53** Orphaned Functions | **20** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt` -> **55** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/url/-Url.kt`** -> AI Confidence: **99.32%**
2. **`mockwebserver/src/main/kotlin/mockwebserver3/internal/RecordedRequestFactory.kt`** -> AI Confidence: **99.31%**
3. **`okcurl/src/main/kotlin/okhttp3/curl/internal/-MainCommon.kt`** -> AI Confidence: **99.31%**
4. **`okhttp-idna-mapping-table/src/main/kotlin/okhttp3/internal/idn/SimpleIdnaMappingTable.kt`** -> AI Confidence: **99.31%**
5. **`okhttp-java-net-cookiejar/src/main/kotlin/okhttp3/java/net/cookiejar/JavaNetCookieJar.kt`** -> AI Confidence: **99.31%**
6. **`okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`** -> AI Confidence: **99.31%**
7. **`okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/DerReader.kt`** -> AI Confidence: **99.31%**
8. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cookie.kt`** -> AI Confidence: **99.31%**
9. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Dispatcher.kt`** -> AI Confidence: **99.31%**
10. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt`** -> AI Confidence: **99.31%**
11. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilCommon.kt`** -> AI Confidence: **99.31%**
12. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheInterceptor.kt`** -> AI Confidence: **99.31%**
13. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheStrategy.kt`** -> AI Confidence: **99.31%**
14. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt`** -> AI Confidence: **99.31%**
15. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt`** -> AI Confidence: **99.31%**
16. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/FastFallbackExchangeFinder.kt`** -> AI Confidence: **99.31%**
17. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt`** -> AI Confidence: **99.31%**
18. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealConnectionPool.kt`** -> AI Confidence: **99.31%**
19. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/CallServerInterceptor.kt`** -> AI Confidence: **99.31%**
20. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpHeaders.kt`** -> AI Confidence: **99.31%**
21. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RetryAndFollowUpInterceptor.kt`** -> AI Confidence: **99.31%**
22. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Stream.kt`** -> AI Confidence: **99.31%**
23. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/platform/Jdk9Platform.kt`** -> AI Confidence: **99.31%**
24. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/tls/OkHostnameVerifier.kt`** -> AI Confidence: **99.31%**
25. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/WebSocketReader.kt`** -> AI Confidence: **99.31%**
26. **`okhttp/src/jvmTest/kotlin/okhttp3/WebPlatformUrlTest.kt`** -> AI Confidence: **99.31%**
27. **`samples/tlssurvey/src/main/kotlin/okhttp3/survey/RunSurvey.kt`** -> AI Confidence: **99.31%**
28. **`build-logic/src/main/kotlin/okhttp.dokka-multimodule-conventions.gradle.kts`** -> AI Confidence: **99.29%**
29. **`settings.gradle.kts`** -> AI Confidence: **99.29%**
30. **`maven-tests/mvnw`** -> AI Confidence: **99.29%**
31. **`mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/RecordedRequest.kt`** -> AI Confidence: **99.24%**
32. **`mockwebserver/src/test/java/mockwebserver3/internal/http2/Http2Server.kt`** -> AI Confidence: **99.24%**
33. **`okhttp-testing-support/src/main/kotlin/okhttp3/EventRecorder.kt`** -> AI Confidence: **99.24%**
34. **`okhttp-testing-support/src/main/kotlin/okhttp3/RecordingConnectionListener.kt`** -> AI Confidence: **99.24%**
35. **`okhttp-tls/src/main/kotlin/okhttp3/tls/internal/TlsUtil.kt`** -> AI Confidence: **99.24%**
36. **`okhttp/src/androidMain/kotlin/okhttp3/internal/platform/android/AndroidLog.kt`** -> AI Confidence: **99.24%**
37. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Address.kt`** -> AI Confidence: **99.24%**
38. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilJvm.kt`** -> AI Confidence: **99.24%**
39. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/authenticator/JavaNetAuthenticator.kt`** -> AI Confidence: **99.24%**
40. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/ConnectPlan.kt`** -> AI Confidence: **99.24%**
41. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealRoutePlanner.kt`** -> AI Confidence: **99.24%**
42. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RouteSelector.kt`** -> AI Confidence: **99.24%**
43. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http1/Http1ExchangeCodec.kt`** -> AI Confidence: **99.24%**
44. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt`** -> AI Confidence: **99.24%**
45. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt`** -> AI Confidence: **99.24%**
46. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/WebSocketWriter.kt`** -> AI Confidence: **99.24%**
47. **`okhttp/src/jvmMain/kotlin/okhttp3/internal/platform/OpenJSSEPlatform.kt`** -> AI Confidence: **99.24%**
48. **`okhttp/src/jvmTest/kotlin/okhttp3/SocksProxy.kt`** -> AI Confidence: **99.24%**
49. **`okhttp-sse/src/main/kotlin/okhttp3/sse/internal/RealEventSource.kt`** -> AI Confidence: **99.23%**
50. **`okhttp/src/androidMain/kotlin/okhttp3/internal/platform/android/AndroidSocketAdapter.kt`** -> AI Confidence: **99.23%**
51. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/publicsuffix/BasePublicSuffixList.kt`** -> AI Confidence: **99.23%**
52. **`mockwebserver-junit5/src/main/kotlin/mockwebserver3/junit5/internal/StartStopExtension.kt`** -> AI Confidence: **99.18%**
53. **`okhttp-osgi-tests/src/test/kotlin/okhttp3/osgi/OsgiTest.kt`** -> AI Confidence: **99.18%**
54. **`okhttp-sse/src/test/java/okhttp3/sse/internal/EventSourceRecorder.kt`** -> AI Confidence: **99.18%**
55. **`okhttp-testing-support/src/main/kotlin/okhttp3/OkHttpClientTestRule.kt`** -> AI Confidence: **99.18%**
56. **`okhttp-testing-support/src/main/kotlin/okhttp3/TestUtilJvm.kt`** -> AI Confidence: **99.18%**
57. **`okhttp-testing-support/src/main/kotlin/okhttp3/internal/concurrent/TaskFaker.kt`** -> AI Confidence: **99.18%**
58. **`okhttp-tls/src/main/kotlin/okhttp3/tls/internal/InsecureExtendedTrustManager.kt`** -> AI Confidence: **99.18%**
59. **`okhttp/src/androidMain/kotlin/okhttp3/internal/platform/Android10Platform.kt`** -> AI Confidence: **99.18%**
60. **`okhttp/src/commonJvmAndroid/kotlin/okhttp3/MultipartReader.kt`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `okhttp-tls/src/main/kotlin/okhttp3/tls/Certificates.kt` -> **100.0%** Exposure
- `okhttp-tls/src/test/java/okhttp3/tls/HeldCertificateTest.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/tls/HostnameVerifierTest.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/kt/CustomTrust.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/CustomTrust.java` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6595` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-CacheControlCommon.kt` (KOTLIN) -> Cumulative Risk: **651.78**
- **Archetype:** `file_cluster_8` (Distance: 12.01 IQR)
- **Magnitude:** 168.24 | **LOC:** 268 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.8276%), Cognitive Load (93.8273%)
- **Heaviest Functions:** `commonToString` (Impact: 32.4), `commonParse` (Impact: 14.6), `indexOfElement` (Impact: 10.6)

### 2. `okhttp/src/jvmTest/kotlin/okhttp3/FakeRoutePlanner.kt` (KOTLIN) -> Cumulative Risk: **638.85**
- **Archetype:** `file_cluster_13` (Distance: 12.325 IQR)
- **Magnitude:** 151.64 | **LOC:** 217 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (96.4212%), Cognitive Load (89.2145%)
- **Heaviest Functions:** `plan` (Impact: 14.9), `connectTcp` (Impact: 10.3), `connectTlsEtc` (Impact: 8.4)

### 3. `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` (KOTLIN) -> Cumulative Risk: **605.65**
- **Archetype:** `file_cluster_13` (Distance: 11.559 IQR)
- **Magnitude:** 279.98 | **LOC:** 576 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.997%), Documentation (99.6667%), Safety Score (81.9947%)
- **Heaviest Functions:** `toString` (Impact: 23.1), `chunkedBody` (Impact: 5.0), `constructor` (Impact: 3.1)

### 4. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-HeadersCommon.kt` (KOTLIN) -> Cumulative Risk: **605.48**
- **Archetype:** `file_cluster_8` (Distance: 11.647 IQR)
- **Magnitude:** 145.68 | **LOC:** 212 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9145%), State Flux (93.8197%)
- **Heaviest Functions:** `commonHeadersGet` (Impact: 10.6), `headersCheckValue` (Impact: 10.6), `commonValues` (Impact: 10.5)

### 5. `samples/slack/src/main/java/okhttp3/slack/OAuthSessionFactory.java` (JAVA) -> Cumulative Risk: **601.48**
- **Archetype:** `file_cluster_13` (Distance: 11.561 IQR)
- **Magnitude:** 90.74 | **LOC:** 127 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9887%), State Flux (99.8309%), Concurrency (98.7322%)
- **Heaviest Functions:** `dispatch` (Impact: 21.3), `close` (Impact: 9.3), `newAuthorizeUrl` (Impact: 4.5)

### 6. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/url/-Url.kt` (KOTLIN) -> Cumulative Risk: **597.13**
- **Archetype:** `file_cluster_13` (Distance: 11.253 IQR)
- **Magnitude:** 158.52 | **LOC:** 245 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9929%), Cognitive Load (95.1718%), Documentation (90.3198%)
- **Heaviest Functions:** `writeCanonicalized` (Impact: 109.1)

### 7. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt` (KOTLIN) -> Cumulative Risk: **595.33**
- **Archetype:** `file_cluster_13` (Distance: 12.075 IQR)
- **Magnitude:** 330.74 | **LOC:** 403 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Tech Debt (89.7401%), Safety Score (85.2775%)
- **Heaviest Functions:** `bodyComplete` (Impact: 36.0), `read` (Impact: 21.7), `write` (Impact: 13.1)

### 8. `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/MockResponse.kt` (KOTLIN) -> Cumulative Risk: **576.74**
- **Archetype:** `file_cluster_8` (Distance: 11.165 IQR)
- **Magnitude:** 156.32 | **LOC:** 287 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9977%), Cognitive Load (94.1759%), Safety Score (82.217%)
- **Heaviest Functions:** `setResponseCode` (Impact: 8.6), `setChunkedBody` (Impact: 4.9), `clone` (Impact: 3.8)

### 9. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RealInterceptorChain.kt` (KOTLIN) -> Cumulative Risk: **568.9**
- **Archetype:** `file_cluster_13` (Distance: 12.464 IQR)
- **Magnitude:** 243.84 | **LOC:** 375 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.996%), Verification (80.0%)
- **Heaviest Functions:** `proceed` (Impact: 13.7), `withSslSocketFactory` (Impact: 13.1), `withCertificatePinner` (Impact: 8.6)

### 10. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealConnection.kt` (KOTLIN) -> Cumulative Risk: **556.04**
- **Archetype:** `file_cluster_13` (Distance: 11.065 IQR)
- **Magnitude:** 180.56 | **LOC:** 463 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.3777%), Verification (80.0%)
- **Heaviest Functions:** `isEligible` (Impact: 46.7), `newCodec` (Impact: 8.8), `toString` (Impact: 7.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.419 IQR)
- **Top Global Matches:** file_cluster_13: 11.419, file_cluster_0: 11.423, file_cluster_8: 11.423
- **Magnitude:** 580.94 | **LOC:** 1466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9937%)
**Top Internal Functions/Classes:**
  * `newInterceptorChain` (Impact: 7.9)
  * `eventListener` (Impact: 6.9)
  * `mockResponse` (Impact: 4.1)
  * `okHttpClientBuilder` (Impact: 3.7)
  * `call` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 257`, `args: 171`, `func_start: 167`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 332`, `planned_debt: 123`, `orphaned_logic: 42`
* *Architecture:* `io: 14`, `api: 6`, `import: 69`
* *Defense:* `safety: 4`, `doc: 1`, `test: 69`, `immutability_locks: 320`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` okhttp3.tls.HeldCertificate, java.net.InetSocketAddress, okhttp3.mockwebserver.RecordedRequest, java.util.concurrent.Executors, okhttp3.internal.proxy.NullProxySelector, okhttp3.logging.LoggingEventListener, javax.net.ssl.X509TrustManager, java.net.InetAddress...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.752 IQR)
- **Top Global Matches:** file_cluster_8: 10.752, file_cluster_13: 10.797, file_cluster_0: 10.99
- **Magnitude:** 563.02 | **LOC:** 4983 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (13.922%), Tech Debt (99.9885%)
**Top Internal Functions/Classes:**
  * `gzip` (Impact: 29.6)
  * `onResponse` (Impact: 28.7)
  * `connectionReuseWhenResponseBodyConsumed_` (Impact: 27.7)
  * `requestBody` (Impact: 12.2)
  * `canceledAfterResponseIsDeliveredBreaksSt` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 284`, `args: 134`, `func_start: 116`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 108`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 22`, `orphaned_logic: 70`
* *Architecture:* `io: 5`, `api: 8`, `import: 124`
* *Defense:* `safety: 9`, `doc: 13`, `test: 252`, `sync_locks: 8`, `immutability_locks: 133`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` okhttp3.CertificatePinner.Companion.pin, assertk.assertions.index, java.net.HttpCookie, okhttp3.internal.closeQuietly, okio.fakefilesystem.FakeFileSystem, java.net.HttpURLConnection, java.util.concurrent.BlockingQueue, assertk.assertions.isNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.41 IQR)
- **Top Global Matches:** file_cluster_13: 12.41, file_cluster_0: 12.752, file_cluster_8: 12.945
- **Magnitude:** 466.68 | **LOC:** 627 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (43.9249%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `callDone` (Impact: 81.6)
  * `messageDone` (Impact: 67.2)
  * `redactedUrl` (Impact: 29.9)
  * `run` (Impact: 20.7)
    * *Intent:* /** * Complete this call. This should be called once these properties are all false: * [requestBodyO...
  * `noMoreExchanges` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 81`, `args: 28`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 117`
* *Architecture:* `io: 1`, `api: 37`, `import: 36`
* *Defense:* `safety: 19`, `doc: 16`, `test: 5`, `sync_locks: 9`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.562
  * `Choke Point (Betweenness):` 0.015594 | `Ripple Effect (Closeness):` 0.138551
  * `Imports (Out-Degree: 14):` okhttp3.internal.closeQuietly, java.util.concurrent.atomic.AtomicReferenceFieldUpdater, java.util.concurrent.RejectedExecutionException, java.io.InterruptedIOException, okhttp3.Call, java.util.concurrent.atomic.AtomicInteger, okhttp3.internal.assertLockNotHeld, java.net.Socket...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.977 IQR)
- **Top Global Matches:** file_cluster_13: 11.977, file_cluster_0: 12.452, file_cluster_8: 12.473
- **Magnitude:** 449.1 | **LOC:** 703 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.4688%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isValid` (Impact: 93.4)
  * `finishReader` (Impact: 72.4)
  * `writeOneFrame` (Impact: 39.7)
  * `writePingFrame` (Impact: 20.5)
    * *Intent:* /** * For testing: receive a single frame and return true if there are more frames to read. Invoked ...
  * `connect` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 67`, `args: 15`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 123`
* *Architecture:* `io: 2`, `api: 24`, `import: 36`
* *Defense:* `safety: 9`, `doc: 12`, `sync_locks: 8`, `immutability_locks: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.878
  * `Choke Point (Betweenness):` 0.005104 | `Ripple Effect (Closeness):` 0.13617
  * `Imports (Out-Degree: 14):` java.net.ProtocolException, okhttp3.internal.closeQuietly, okio.ByteString.Companion.encodeUtf8, java.net.SocketTimeoutException, okhttp3.Protocol, okhttp3.Call, okhttp3.WebSocketListener, okhttp3.internal.concurrent.Task...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.066 IQR)
- **Top Global Matches:** file_cluster_8: 10.066, file_cluster_13: 10.374, file_cluster_12: 10.463
- **Magnitude:** 446.6 | **LOC:** 2538 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (97.7699%), Tech Debt (76.5211%)
**Top Internal Functions/Classes:**
  * `responseBodyFail` (Impact: 65.5)
  * `assertBytesReadWritten` (Impact: 26.4)
  * `timeToFirstByte` (Impact: 20.3)
  * `assertSuccessfulEventOrder` (Impact: 8.9)
  * `writeTo` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 495`, `args: 89`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 62`, `duplicate_logic: 6`, `orphaned_logic: 55`
* *Architecture:* `io: 3`, `api: 4`, `import: 89`
* *Defense:* `safety: 3`, `doc: 5`, `test: 200`, `immutability_locks: 147`, `cleanup: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` java.net.HttpURLConnection, assertk.assertions.isNull, okhttp3.logging.HttpLoggingInterceptor, mockwebserver3.junit5.StartStop, org.junit.jupiter.api.BeforeEach, assertk.assertions.prop, okhttp3.CallEvent.CallFailed, assertk.all...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.513 IQR)
- **Top Global Matches:** file_cluster_8: 10.513, file_cluster_13: 10.582, file_cluster_0: 10.77
- **Magnitude:** 444.34 | **LOC:** 4543 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.371%), Tech Debt (99.9979%)
**Top Internal Functions/Classes:**
  * `connectionCloseInRequest` (Impact: 43.1)
  * `doUpload` (Impact: 24.2)
  * `writeTo` (Impact: 14.8)
  * `connect` (Impact: 8.6)
  * `newSet` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 206`, `args: 109`, `func_start: 101`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 79`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 20`, `orphaned_logic: 53`
* *Architecture:* `io: 13`, `api: 11`, `import: 86`
* *Defense:* `safety: 6`, `doc: 16`, `test: 157`, `sync_locks: 1`, `immutability_locks: 98`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.net.HttpURLConnection, java.util.zip.GZIPInputStream, assertk.assertions.isNull, javax.net.ssl.X509TrustManager, org.bouncycastle.tls.TlsFatalAlert, java.net.Socket, mockwebserver3.junit5.StartStop, java.net.ProxySelector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.922 IQR)
- **Top Global Matches:** file_cluster_13: 11.922, file_cluster_0: 11.988, file_cluster_8: 12.278
- **Magnitude:** 443.6 | **LOC:** 1122 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.3086%), Tech Debt (79.2031%)
**Top Internal Functions/Classes:**
  * `detach` (Impact: 59.1)
  * `completeEdit` (Impact: 47.5)
    * *Intent:* * count, and a blank line. * * Each of the subsequent lines in the file is a record of the state of ...
  * `snapshot` (Impact: 27.3)
  * `hasNext` (Impact: 18.1)
  * `newSource` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 94`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 105`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 37`, `import: 26`
* *Defense:* `safety: 7`, `doc: 32`, `test: 1`, `sync_locks: 16`, `immutability_locks: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.118
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.067557
  * `Imports (Out-Degree: 4):` okhttp3.internal.platform.Platform.Companion.WARN, java.io.Flushable, okhttp3.internal.closeQuietly, okio.FileNotFoundException, okio.ForwardingSource, okio.Path, okhttp3.internal.concurrent.Task, okhttp3.internal.isCivilized...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.083 IQR)
- **Top Global Matches:** file_cluster_13: 10.083, file_cluster_8: 10.247, file_cluster_0: 10.491
- **Magnitude:** 388.02 | **LOC:** 516 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.725%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 138.5)
  * `init` (Impact: 25.6)
  * `getPlatformSystemProperty` (Impact: 17.4)
  * `interceptTestMethod` (Impact: 14.4)
    * *Intent:* /** * Marks a test as Platform aware, before the test runs a consistent Platform will be * establish...
  * `setupPlatform` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 112`, `args: 70`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`, `duplicate_logic: 3`
* *Architecture:* `api: 44`, `import: 34`
* *Defense:* `safety: 4`, `doc: 2`, `test: 1`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.115
  * `Choke Point (Betweenness):` 0.002537 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 7):` okhttp3.TestUtil, org.bouncycastle.jce.provider.BouncyCastleProvider, org.junit.jupiter.api.extension.ExtensionContext, org.junit.jupiter.api.Assumptions.assumeTrue, okhttp3.internal.platform.OpenJSSEPlatform, org.junit.jupiter.api.extension.ReflectiveInvocationContext, org.opentest4j.TestAbortedException, com.amazon.corretto.crypto.provider.SelfTestStatus...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.612 IQR)
- **Top Global Matches:** file_cluster_8: 10.612, file_cluster_0: 10.798, file_cluster_13: 10.866
- **Magnitude:** 382.02 | **LOC:** 2160 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.9161%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `fun` (Impact: 19.2)
  * `fun` (Impact: 18.9)
  * `fun` (Impact: 14.2)
    * *Intent:* // Cause the rebuild action to fail.
  * `fun` (Impact: 13.3)
  * `fun` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 111`, `args: 90`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 74`, `fragile_debt: 1`, `duplicate_logic: 19`, `orphaned_logic: 41`
* *Architecture:* `io: 2`, `api: 5`, `import: 31`
* *Defense:* `safety: 6`, `doc: 7`, `test: 200`, `sync_locks: 1`, `immutability_locks: 66`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` okhttp3.TestUtil, okio.fakefilesystem.FakeFileSystem, okhttp3.internal.concurrent.TaskFaker, okhttp3.internal.cache.DiskLruCache.Snapshot, assertk.assertThat, org.junit.jupiter.api.Timeout, assertk.assertions.isNull, okio.Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.912 IQR)
- **Top Global Matches:** file_cluster_8: 8.912, file_cluster_7: 9.712, file_cluster_13: 9.838
- **Magnitude:** 378.92 | **LOC:** 4261 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (5.7273%), Tech Debt (82.512%)
**Top Internal Functions/Classes:**
  * `secureResponseCaching` (Impact: 44.2)
  * `testPublicPathConstructor` (Impact: 7.4)
  * `assertConditionallyCached` (Impact: 6.6)
  * `onPathParameter` (Impact: 4.9)
  * `truncateViolently` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 154`, `args: 92`, `func_start: 89`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 22`, `duplicate_logic: 4`, `orphaned_logic: 73`
* *Architecture:* `io: 1`, `api: 4`, `import: 53`
* *Defense:* `safety: 1`, `doc: 12`, `test: 336`, `sync_locks: 3`, `immutability_locks: 181`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` mockwebserver3.RecordedRequest, okio.fakefilesystem.FakeFileSystem, java.net.HttpURLConnection, assertk.assertThat, java.text.DateFormat, mockwebserver3.SocketEffect.ShutdownConnection, okhttp3.internal.addHeaderLenient, assertk.assertions.isNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cache.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.386 IQR)
- **Top Global Matches:** file_cluster_13: 11.386, file_cluster_0: 11.632, file_cluster_8: 11.792
- **Magnitude:** 372.26 | **LOC:** 838 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (37.1933%), Tech Debt (97.0836%)
**Top Internal Functions/Classes:**
  * `body` (Impact: 60.3)
    * *Intent:* * // The resource was cached! Show it. * } else { * // The resource was not cached. * } * ``` * * Th...
  * `source` (Impact: 37.2)
  * `constructor` (Impact: 23.6)
  * `readCertificateList` (Impact: 17.0)
  * `readInt` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 93`, `args: 33`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 73`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 16`, `import: 35`
* *Defense:* `safety: 6`, `doc: 11`, `sync_locks: 7`, `immutability_locks: 63`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.702
  * `Choke Point (Betweenness):` 0.002155 | `Ripple Effect (Closeness):` 0.082762
  * `Imports (Out-Degree: 8):` okhttp3.internal.platform.Platform.Companion.WARN, java.io.Flushable, okhttp3.internal.closeQuietly, okio.ByteString.Companion.encodeUtf8, okio.ForwardingSource, okio.Path, java.security.cert.CertificateEncodingException, okio.FileSystem...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpMethod.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.194 IQR)
- **Top Global Matches:** file_cluster_0: 13.194, file_cluster_13: 13.328, file_cluster_8: 13.368
- **Magnitude:** 366.05 | **LOC:** 52 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 9`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.975
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130702
  * `Imports (Out-Degree: 0):` kotlin.jvm.JvmStatic
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.463 IQR)
- **Top Global Matches:** file_cluster_8: 11.463, file_cluster_16: 11.549, file_cluster_13: 11.571
- **Magnitude:** 359.12 | **LOC:** 530 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.7472%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `any` (Impact: 40.2)
    * *Intent:* /**
  * `sequence` (Impact: 19.4)
  * `toDer` (Impact: 18.9)
    * *Intent:* /** * This decodes a value into its contents using a preceding member of the same SEQUENCE. For * ex...
  * `usingTypeHint` (Impact: 18.4)
  * `fromDer` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 107`, `args: 48`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 93`, `planned_debt: 4`, `duplicate_logic: 24`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 3`, `doc: 10`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.net.ProtocolException, java.text.ParseException, java.util.Date, java.math.BigInteger, java.util.TimeZone, java.text.SimpleDateFormat, kotlin.reflect.KClass, okio.ByteString
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.08 IQR)
- **Top Global Matches:** file_cluster_13: 11.08, file_cluster_8: 11.292, file_cluster_0: 11.368
- **Magnitude:** 352.14 | **LOC:** 371 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (60.4682%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 129.8)
  * `intercept` (Impact: 110.3)
    * *Intent:* /** * Logs request and response lines and their respective headers and bodies (if present). *
  * `redactUrl` (Impact: 16.8)
  * `bodyHasUnknownEncoding` (Impact: 10.2)
  * `bodyIsStreaming` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 44`, `args: 14`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 43`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 11`, `import: 16`
* *Defense:* `safety: 2`, `doc: 7`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.489
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.010582
  * `Imports (Out-Degree: 7):` okhttp3.internal.http.promisesBody, okio.Buffer, okio.GzipSource, okhttp3.Interceptor, okhttp3.OkHttpClient, java.util.TreeSet, okhttp3.internal.UnreadableResponseBody, okhttp3.internal.platform.Platform...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `okhttp-tls/src/test/java/okhttp3/tls/internal/der/DerCertificatesTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.212 IQR)
- **Top Global Matches:** file_cluster_8: 10.212, file_cluster_13: 10.685, file_cluster_7: 10.851
- **Magnitude:** 335.82 | **LOC:** 1098 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.349%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fun` (Impact: 8.0)
  * `fun` (Impact: 8.0)
  * `fun` (Impact: 5.2)
  * `fun` (Impact: 4.7)
  * `encodeKey` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 49`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 225`, `duplicate_logic: 16`
* *Architecture:* `api: 15`, `import: 27`
* *Defense:* `safety: 1`, `doc: 4`, `test: 51`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` okio.ByteString.Companion.encodeUtf8, okhttp3.tls.decodeCertificatePem, assertk.assertThat, java.security.KeyFactory, java.security.spec.PKCS8EncodedKeySpec, assertk.assertions.isNull, okhttp3.tls.internal.der.ObjectIdentifiers.BASIC_CONSTRAINTS, java.math.BigInteger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.075 IQR)
- **Top Global Matches:** file_cluster_13: 12.075, file_cluster_0: 12.24, file_cluster_8: 12.252
- **Magnitude:** 330.74 | **LOC:** 403 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (66.9815%), Tech Debt (89.7401%)
**Top Internal Functions/Classes:**
  * `bodyComplete` (Impact: 36.0)
    * *Intent:* /** * Revoke this exchange's access to streams. This is necessary when a follow-up request is
  * `read` (Impact: 21.7)
  * `write` (Impact: 13.1)
  * `close` (Impact: 12.8)
  * `complete` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 70`, `args: 24`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 126`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `import: 16`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.312
  * `Choke Point (Betweenness):` 0.001904 | `Ripple Effect (Closeness):` 0.111586
  * `Imports (Out-Degree: 7):` okhttp3.ResponseBody, okio.Sink, okhttp3.EventListener, java.net.ProtocolException, okio.Buffer, okio.buffer, okhttp3.internal.http.ExchangeCodec, okio.Socket...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.508 IQR)
- **Top Global Matches:** file_cluster_13: 11.508, file_cluster_0: 11.79, file_cluster_8: 11.79
- **Magnitude:** 330.34 | **LOC:** 606 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.2278%), Tech Debt (91.3813%)
**Top Internal Functions/Classes:**
  * `readSettings` (Impact: 37.4)
  * `nextFrame` (Impact: 26.6)
  * `readWindowUpdate` (Impact: 16.1)
  * `read` (Impact: 14.9)
  * `readHeaders` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 98`, `args: 31`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`, `planned_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 26`, `import: 34`
* *Defense:* `safety: 5`, `doc: 31`, `immutability_locks: 43`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` okhttp3.internal.http2.Http2.TYPE_WINDOW_UPDATE, okhttp3.internal.http2.Http2.FLAG_COMPRESSED, okhttp3.internal.http2.Http2.CONNECTION_PREFACE, okhttp3.internal.http2.Http2.FLAG_END_STREAM, java.util.logging.Logger, okhttp3.internal.http2.Http2.FLAG_PADDED, java.io.Closeable, okhttp3.internal.http2.Http2.frameLog...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp-tls/src/test/java/okhttp3/tls/internal/der/DerTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.52 IQR)
- **Top Global Matches:** file_cluster_8: 9.52, file_cluster_0: 9.804, file_cluster_13: 10.019
- **Magnitude:** 300.7 | **LOC:** 983 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fun` (Impact: 7.2)
  * `fun` (Impact: 7.1)
  * `fun` (Impact: 7.0)
  * `fun` (Impact: 6.8)
  * `fun` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 114`, `args: 107`, `func_start: 77`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `duplicate_logic: 75`
* *Architecture:* `api: 8`, `import: 25`
* *Defense:* `safety: 3`, `doc: 4`, `test: 246`, `immutability_locks: 113`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.net.ProtocolException, okio.ByteString.Companion.encodeUtf8, assertk.assertThat, assertk.assertions.isNull, java.net.InetAddress, okhttp3.tls.internal.der.ObjectIdentifiers.BASIC_CONSTRAINTS, okhttp3.tls.internal.der.CertificateAdapters.generalNameIpAddress, java.math.BigInteger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.376 IQR)
- **Top Global Matches:** file_cluster_13: 10.376, file_cluster_8: 10.532, file_cluster_0: 10.688
- **Magnitude:** 297.38 | **LOC:** 1094 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.1923%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testConscryptRequest` (Impact: 11.4)
  * `testRequestUsesPlayProvider` (Impact: 10.9)
  * `testUnderscoreRequest` (Impact: 10.4)
  * `testRequestUsesPlayProviderLocalhostInse` (Impact: 10.1)
  * `testCustomTrustManagerWithAndroidCheck` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 196`, `args: 57`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 51`, `planned_debt: 3`, `duplicate_logic: 18`, `orphaned_logic: 31`
* *Architecture:* `io: 10`, `api: 13`, `import: 96`
* *Defense:* `safety: 7`, `test: 96`, `sync_locks: 3`, `immutability_locks: 79`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory, org.junit.jupiter.api.Assumptions.assumeTrue, okhttp3.Connection, okhttp3.TlsVersion, javax.net.ssl.X509TrustManager, android.os.Build, mockwebserver3.junit5.StartStop, org.junit.jupiter.api.BeforeEach...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.559 IQR)
- **Top Global Matches:** file_cluster_8: 11.559, file_cluster_13: 11.559, file_cluster_7: 11.824
- **Magnitude:** 279.98 | **LOC:** 576 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.06%), Tech Debt (81.0209%)
**Top Internal Functions/Classes:**
  * `toString` (Impact: 23.1)
  * `chunkedBody` (Impact: 5.0)
  * `constructor` (Impact: 3.1)
  * `constructor` (Impact: 3.0)
  * `constructor` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 38`, `args: 27`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `state_mutation: 124`, `duplicate_logic: 5`
* *Architecture:* `api: 82`, `import: 10`
* *Defense:* `safety: 3`, `doc: 16`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.006
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.075893
  * `Imports (Out-Degree: 4):` okio.Buffer, okhttp3.internal.http2.Settings, java.util.concurrent.TimeUnit, okhttp3.internal.http2.ErrorCode, okhttp3.WebSocketListener, mockwebserver3.SocketEffect.CloseStream, okhttp3.Headers.Companion.headersOf, mockwebserver3.internal.toMockResponseBody...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Writer.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.172 IQR)
- **Top Global Matches:** file_cluster_13: 12.172, file_cluster_0: 12.456, file_cluster_8: 12.659
- **Magnitude:** 278.06 | **LOC:** 384 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.2945%), Tech Debt (55.7517%)
**Top Internal Functions/Classes:**
  * `connectionPreface` (Impact: 64.5)
  * `headers` (Impact: 14.7)
  * `windowUpdate` (Impact: 11.5)
  * `settings` (Impact: 10.9)
  * `ping` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 54`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 99`, `orphaned_logic: 6`
* *Architecture:* `api: 22`, `import: 27`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` okhttp3.internal.http2.Http2.TYPE_WINDOW_UPDATE, okhttp3.internal.writeMedium, okhttp3.internal.http2.Http2.CONNECTION_PREFACE, okhttp3.internal.http2.Http2.FLAG_END_STREAM, java.util.logging.Logger, java.io.Closeable, okhttp3.internal.http2.Http2.frameLog, java.util.logging.Level.FINE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.808 IQR)
- **Top Global Matches:** file_cluster_13: 11.808, file_cluster_0: 12.107, file_cluster_8: 12.19
- **Magnitude:** 276.24 | **LOC:** 1817 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.8111%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `schemeDelimiterOffset` (Impact: 73.2)
    * *Intent:* * retrieve the resource. Although URLs have many schemes (`mailto`, `file`, `ftp`), this class only ...
  * `push` (Impact: 22.7)
    * *Intent:* /**
  * `portColonOffset` (Impact: 19.0)
    * *Intent:* * ### Query * * The query is optional: it can be null, empty, or non-empty. For many HTTP URLs the q...
  * `slashCount` (Impact: 14.8)
    * *Intent:* * This class never returns -1 for the port: if no port is explicitly specified in the URL then the *...
  * `toQueryNamesAndValues` (Impact: 13.1)
    * *Intent:* * clicking a relative link on a specified page. For example: * * ```java * HttpUrl base = HttpUrl.pa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 58`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 25`, `import: 25`
* *Defense:* `doc: 13`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.805
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.114869
  * `Imports (Out-Degree: 1):` okhttp3.internal.url.QUERY_COMPONENT_ENCODE_SET_URI, okhttp3.internal.url.PATH_SEGMENT_ENCODE_SET_URI, okhttp3.internal.indexOfFirstNonAsciiWhitespace, okhttp3.internal.url.canonicalize, okhttp3.internal.url.percentDecode, okhttp3.internal.url.QUERY_ENCODE_SET, okhttp3.internal.unmodifiable, okhttp3.internal.toCanonicalHost...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http1/Http1ExchangeCodec.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.594 IQR)
- **Top Global Matches:** file_cluster_13: 11.594, file_cluster_8: 11.84, file_cluster_7: 12.189
- **Magnitude:** 271.6 | **LOC:** 584 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.9341%), Tech Debt (80.8361%)
**Top Internal Functions/Classes:**
  * `readResponseHeaders` (Impact: 22.6)
  * `read` (Impact: 19.1)
    * *Intent:* /** * Sets the delegate of `timeout` to [Timeout.NONE] and resets its underlying timeout * to the de...
  * `readChunkSize` (Impact: 15.1)
  * `read` (Impact: 12.8)
  * `openResponseBodySource` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 77`, `args: 26`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 68`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 22`, `import: 27`
* *Defense:* `safety: 14`, `doc: 11`, `immutability_locks: 38`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.973
  * `Choke Point (Betweenness):` 0.000197 | `Ripple Effect (Closeness):` 0.009409
  * `Imports (Out-Degree: 9):` okhttp3.internal.http.promisesBody, java.net.ProtocolException, okhttp3.internal.headersContentLength, okhttp3.HttpUrl, okhttp3.internal.http.ExchangeCodec, okhttp3.internal.http.receiveHeaders, okhttp3.Headers, okhttp3.internal.skipAll...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RetryAndFollowUpInterceptor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.521 IQR)
- **Top Global Matches:** file_cluster_13: 11.521, file_cluster_8: 12.125, file_cluster_0: 12.203
- **Magnitude:** 269.92 | **LOC:** 365 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (60.1823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `intercept` (Impact: 114.2)
  * `followUpRequest` (Impact: 62.2)
  * `isRecoverable` (Impact: 21.4)
  * `retryAfter` (Impact: 12.7)
  * `requestIsOneShot` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 55`, `args: 6`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`
* *Architecture:* `io: 1`, `api: 11`, `import: 28`
* *Defense:* `safety: 8`, `doc: 3`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.229
  * `Choke Point (Betweenness):` 0.000341 | `Ripple Effect (Closeness):` 0.100171
  * `Imports (Out-Degree: 7):` java.net.ProtocolException, okhttp3.internal.closeQuietly, java.io.InterruptedIOException, java.net.SocketTimeoutException, java.net.HttpURLConnection.HTTP_MOVED_TEMP, okhttp3.internal.canReuseConnectionFor, java.net.HttpURLConnection.HTTP_CLIENT_TIMEOUT, okhttp3.internal.http2.ConnectionShutdownException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheInterceptor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.187 IQR)
- **Top Global Matches:** file_cluster_13: 10.187, file_cluster_8: 10.396, file_cluster_7: 10.78
- **Magnitude:** 265.36 | **LOC:** 310 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (33.9729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `intercept` (Impact: 133.8)
  * `cacheWritingResponse` (Impact: 29.3)
  * `combine` (Impact: 25.5)
  * `read` (Impact: 17.4)
  * `requestForCache` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 50`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 28`
* *Architecture:* `api: 10`, `import: 22`
* *Defense:* `doc: 5`, `immutability_locks: 23`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.229
  * `Choke Point (Betweenness):` 0.001971 | `Ripple Effect (Closeness):` 0.100171
  * `Imports (Out-Degree: 10):` okhttp3.internal.http.promisesBody, okhttp3.internal.closeQuietly, okhttp3.Protocol, okhttp3.Cache, okhttp3.internal.http.ExchangeCodec, okhttp3.Headers, okhttp3.Interceptor, java.net.HttpURLConnection.HTTP_GATEWAY_TIMEOUT...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RouteDatabase.kt` (KOTLIN) | Magnitude: 9.48 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, doc: 4, decorators: 4
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/RequestBody.kt` (KOTLIN) | Magnitude: 64.28 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 59, args: 33, func_start: 31
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/CacheControl.kt` (KOTLIN) | Magnitude: 77.44 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 42, structural_boundaries: 32, decorators: 27
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Challenge.kt` (KOTLIN) | Magnitude: 51.02 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 36, structural_boundaries: 19, decorators: 12
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/flowcontrol/WindowCounter.kt` (KOTLIN) | Magnitude: 9.08 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 4, state_mutation: 4, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `maven-tests/mvnw` (SHELL) | Magnitude: 263.74 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 123, indent_spaces: 102, io: 85, state_mutation: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/AddressPolicy.kt` (KOTLIN) | Magnitude: 14.12 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, decorators: 3, reflection_metaprogramming: 3, immutability_locks: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/InsecureAndroidTrustManager.kt` (KOTLIN) | Magnitude: 19.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 18, branch: 8, generics: 8
- `samples/guide/src/main/java/okhttp3/recipes/PostStreamingWithPipe.java` (JAVA) | Magnitude: 63.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 32, import: 9, branch: 8
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/MessageDeflater.kt` (KOTLIN) | Magnitude: 11.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 14, immutability_locks: 8, encapsulation: 8
- `samples/compare/src/test/kotlin/okhttp3/compare/JavaHttpClientTest.kt` (KOTLIN) | Magnitude: 4.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, import: 15, test: 9
- `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` (KOTLIN) | Magnitude: 580.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1207, state_mutation: 332, immutability_locks: 320, structural_boundaries: 257

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/CookieJar.kt` (KOTLIN) | Magnitude: 5.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, args: 4, func_start: 4
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/BasicDerAdapter.kt` (KOTLIN) | Magnitude: 34.68 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 20, structural_boundaries: 10, args: 6
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/CertificateAdapters.kt` (KOTLIN) | Magnitude: 109.16 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 271, state_mutation: 68, safety_bypasses: 33, explicit_casts: 28
- `okhttp-testing-support/src/main/kotlin/okhttp3/FailingCall.kt` (KOTLIN) | Magnitude: 49.9 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 17, args: 13, func_start: 13
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/DerAdapter.kt` (KOTLIN) | Magnitude: 72.88 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, state_mutation: 25, structural_boundaries: 23, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpStatusCodes.kt` (KOTLIN) | Magnitude: 15.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 14, doc: 7, globals: 7, sec_dead_code: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` (KOTLIN) | Magnitude: 279.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 314, state_mutation: 124, api: 82, immutability_locks: 39
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/http/ExternalHttp2Example.kt` (KOTLIN) | Magnitude: 14.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 6, branch: 3, state_mutation: 3
- `okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/DnsOverHttpsTest.kt` (KOTLIN) | Magnitude: 68.0 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 250, structural_boundaries: 61, test: 55, import: 36
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheRequest.kt` (KOTLIN) | Magnitude: 22.48 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 3, args: 2, func_start: 2
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/idn/IdnaMappingTable.kt` (KOTLIN) | Magnitude: 21.8 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 6, branch: 5, structural_boundaries: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` -> Churn: **90.27%** | Cog Load: 5.7273% | Debt: 82.512%
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cache.kt` -> Churn: **77.7%** | Cog Load: 37.1933% | Debt: 97.0836%
- `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -> Churn: **60.91%** | Cog Load: 13.922% | Debt: 99.9885%
- `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` -> Churn: **55.93%** | Cog Load: 0.0% | Debt: 99.9937%
- `okhttp/src/jvmTest/kotlin/okhttp3/RequestTest.kt` -> Churn: **55.83%** | Cog Load: 34.2713% | Debt: 94.6625%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 444.34
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 443.6
- `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 388.02
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 330.34
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 276.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 1.966** (Bridge: 0.0197 * Flux: 99.9455%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` -> **Severity: 1.559** (Bridge: 0.0156 * Flux: 99.9899%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RealInterceptorChain.kt` -> **Severity: 0.752** (Bridge: 0.0075 * Flux: 99.996%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` -> **Severity: 0.51** (Bridge: 0.0051 * Flux: 99.9992%)
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **Severity: 0.37** (Bridge: 0.0046 * Flux: 79.7731%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 14.037** (Embedded: 0.1789 * Error Risk: 78.4384%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpMethod.kt` -> **Severity: 12.675** (Embedded: 0.1307 * Error Risk: 96.9785%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt` -> **Severity: 11.809** (Embedded: 0.1585 * Error Risk: 74.5302%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` -> **Severity: 11.57** (Embedded: 0.1362 * Error Risk: 84.9698%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/publicsuffix/PublicSuffixDatabase.kt` -> **Severity: 11.384** (Embedded: 0.1335 * Error Risk: 85.2748%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/platform/Platform.kt` -> **Severity: 1636.301** (Blast Radius: 21.138 * Doc Risk: 77.4104%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Headers.kt` -> **Severity: 1203.457** (Blast Radius: 15.489 * Doc Risk: 77.6975%)
- `mockwebserver-junit5/src/main/kotlin/mockwebserver3/junit5/internal/StartStopExtension.kt` -> **Severity: 931.6** (Blast Radius: 9.316 * Doc Risk: 100.0%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt` -> **Severity: 732.265** (Blast Radius: 16.312 * Doc Risk: 44.8912%)
- `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` -> **Severity: 698.265** (Blast Radius: 7.006 * Doc Risk: 99.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
