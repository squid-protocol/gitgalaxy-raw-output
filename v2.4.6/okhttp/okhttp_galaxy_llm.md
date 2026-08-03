# ARCHITECTURAL_BRIEF: okhttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/okhttp` |
| **Timestamp** | `2026-08-03T21:17:19.522427+00:00` |
| **Scan Duration** | `2.43s` |
| **Git Branch** | `master` |
| **Git Commit** | `c396b08f7a06e412c4cc8f5c83b0d7ed19f7fa6c` |
| **Git Remote** | `https://github.com/square/okhttp` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 609 malicious artifacts.

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
| Modularity | 0.456 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `5.585`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 401 | 59.6% |
| file_cluster_13 | 202 | 30.0% |
| file_cluster_0 | 12 | 1.8% |
| file_cluster_16 | 9 | 1.3% |
| file_cluster_12 | 2 | 0.3% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 19.4 | 10.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.6 | 17.5 | 6.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 38.6 | 13.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.0 | 2.3 | 0.0 |
| API Exposure | 0.0 | 12.6 | 2.2 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.7 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.7 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 90.3 | 6.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 30.6 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 24.6 | 1.5 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `constructor` (@ `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt`) -> Impact: **312.5** | LOC: 450
- `constructor` (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **281.8** | LOC: 276
- `intercept` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheInterceptor.kt`) -> Impact: **255.8** | LOC: 237
- `intercept` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/CallServerInterceptor.kt`) -> Impact: **235.8** | LOC: 157
- `any` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> Impact: **210.4** | LOC: 44
  * *Intent:* /**
- `native_path_[Truncated]` (@ `maven-tests/mvnw`) -> Impact: **178.8** | LOC: 224
  * *Intent:* # OS specific support.
- `isValid` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt`) -> Impact: **174.8** | LOC: 239
- `write` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/DerWriter.kt`) -> Impact: **168.2** | LOC: 130
- `intercept` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RetryAndFollowUpInterceptor.kt`) -> Impact: **167.2** | LOC: 165
- `writeCanonicalized` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/url/-Url.kt`) -> Impact: **162.2** | LOC: 60

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `any` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `isDefaultValue` (@ `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt`) -> **O(2^N) [Recursive]**
- `testPublicSuffixDb` (@ `android-test/src/test/kotlin/okhttp/android/test/NonRobolectricOkHttpClientTest.kt`) -> **O(2^N) [Recursive]**
- `toString` (@ `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt`) -> **O(2^N) [Recursive]**
- `decode` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/HeldCertificate.kt`) -> **O(2^N) [Recursive]**
- `choice` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> **O(2^N) [Recursive]**
- `encode` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> **O(2^N) [Recursive]**
- `encode` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> **O(2^N) [Recursive]**
- `encode` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> **O(2^N) [Recursive]**
- `encode` (@ `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `native_path_[Truncated]` (@ `maven-tests/mvnw`) -> DB Complexity: **275**
  * *Intent:* # OS specific support.
- `toString` (@ `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt`) -> DB Complexity: **95**
- `isValid` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt`) -> DB Complexity: **48**
- `toString` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt`) -> DB Complexity: **47**
  * *Intent:* /** Returns the HTTP headers. */ /** * Returns a non-null stream with the server's response. The returned value must be * [closed][ResponseBody] and m...
- `okHttpClientBuilder` (@ `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt`) -> DB Complexity: **47**
- `toString` (@ `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/MockHttp2Peer.kt`) -> DB Complexity: **46**
- `mockResponse` (@ `mockwebserver-deprecated/src/test/java/okhttp3/mockwebserver/KotlinSourceModernTest.kt`) -> DB Complexity: **38**
- `mockResponse` (@ `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt`) -> DB Complexity: **38**
- `connectionPreface` (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Writer.kt`) -> DB Complexity: **37**
- `connectionCloseInRequest` (@ `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt`) -> DB Complexity: **35**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `okhttp/src/jvmTest/kotlin/okhttp3` | 85 | 7845.91 | 15.27% | 78.47% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3` | 40 | 3845.32 | 26.81% | 13.6% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection` | 21 | 2443.76 | 23.69% | 25.39% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2` | 15 | 1634.24 | 22.02% | 21.52% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http` | 13 | 1598.01 | 39.73% | 10.51% |
| `samples/guide/src/main/java/okhttp3/recipes` | 30 | 1429.76 | 10.31% | 65.69% |
| `okhttp-testing-support/src/main/kotlin/okhttp3` | 30 | 1402.74 | 25.43% | 42.88% |
| `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der` | 11 | 1329.5 | 26.43% | 39.36% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache` | 5 | 1199.28 | 31.93% | 7.99% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal` | 12 | 976.4 | 22.55% | 53.4% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/QueueDispatcher.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSSLSocketFactory.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingServerSocketFactory.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSocketFactory.kt` -> **100.0%** Exposure
- `okhttp/src/androidHostTest/kotlin/okhttp3/internal/publicsuffix/PublicSuffixTesting.android.kt` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `build-logic/src/main/kotlin/okhttp.jvm-conventions.gradle.kts` -> **100.0%** Exposure
- `build-logic/src/main/kotlin/okhttp.publish-conventions.gradle.kts` -> **100.0%** Exposure
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/RecordedRequest.kt` -> **100.0%** Exposure
- `okhttp-testing-support/src/main/kotlin/okhttp3/TestValueFactory.kt` -> **100.0%** Exposure
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/AnyValue.kt` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/EventListener.kt` -> **0** Orphaned Functions | **60** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -> **38** Orphaned Functions | **10** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` -> **41** Orphaned Functions | **4** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/ws/WebSocketReaderTest.kt` -> **43** Orphaned Functions | **0** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **38** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt`** -> AI Confidence: **99.48%**
2. **`android-test/src/androidDeviceTest/java/okhttp/android/test/SingleAndroidTest.kt`** -> AI Confidence: **99.48%**
3. **`android-test/src/androidDeviceTest/java/okhttp/android/test/alpn/AlpnOverrideTest.kt`** -> AI Confidence: **99.48%**
4. **`android-test/src/androidDeviceTest/java/okhttp/android/test/letsencrypt/LetsEncryptClientTest.kt`** -> AI Confidence: **99.48%**
5. **`android-test/src/androidDeviceTest/java/okhttp/android/test/sni/SniOverrideTest.kt`** -> AI Confidence: **99.48%**
6. **`android-test/src/test/kotlin/okhttp/android/test/AndroidLoggingTest.kt`** -> AI Confidence: **99.48%**
7. **`android-test/src/test/kotlin/okhttp/android/test/BaseOkHttpClientUnitTest.kt`** -> AI Confidence: **99.48%**
8. **`build-logic/src/main/kotlin/BndBuildAction.kt`** -> AI Confidence: **99.48%**
9. **`build-logic/src/main/kotlin/JavaModules.kt`** -> AI Confidence: **99.48%**
10. **`build-logic/src/main/kotlin/okhttp.publish-conventions.gradle.kts`** -> AI Confidence: **99.48%**
11. **`container-tests/src/test/java/okhttp3/containers/BasicLoomTest.kt`** -> AI Confidence: **99.48%**
12. **`container-tests/src/test/java/okhttp3/containers/BasicMockServerTest.kt`** -> AI Confidence: **99.48%**
13. **`container-tests/src/test/java/okhttp3/containers/BasicProxyTest.kt`** -> AI Confidence: **99.48%**
14. **`container-tests/src/test/java/okhttp3/containers/SocksProxyTest.kt`** -> AI Confidence: **99.48%**
15. **`mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/DeprecationBridge.kt`** -> AI Confidence: **99.48%**
16. **`mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/MockWebServer.kt`** -> AI Confidence: **99.48%**
17. **`mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/RecordedRequest.kt`** -> AI Confidence: **99.48%**
18. **`mockwebserver-deprecated/src/test/java/okhttp3/mockwebserver/MockWebServerTest.kt`** -> AI Confidence: **99.48%**
19. **`mockwebserver-junit4/src/test/java/mockwebserver3/junit4/MockWebServerRuleTest.kt`** -> AI Confidence: **99.48%**
20. **`mockwebserver-junit5/src/main/kotlin/mockwebserver3/junit5/internal/StartStopExtension.kt`** -> AI Confidence: **99.48%**
21. **`mockwebserver-junit5/src/test/java/mockwebserver3/junit5/StartStopTest.kt`** -> AI Confidence: **99.48%**
22. **`mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt`** -> AI Confidence: **99.48%**
23. **`mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt`** -> AI Confidence: **99.48%**
24. **`mockwebserver/src/main/kotlin/mockwebserver3/internal/MockWebServerSocket.kt`** -> AI Confidence: **99.48%**
25. **`mockwebserver/src/main/kotlin/mockwebserver3/internal/RecordedRequestFactory.kt`** -> AI Confidence: **99.48%**
26. **`mockwebserver/src/test/java/mockwebserver3/CustomDispatcherTest.kt`** -> AI Confidence: **99.48%**
27. **`mockwebserver/src/test/java/mockwebserver3/MockResponseSniTest.kt`** -> AI Confidence: **99.48%**
28. **`mockwebserver/src/test/java/mockwebserver3/MockWebServerTest.kt`** -> AI Confidence: **99.48%**
29. **`mockwebserver/src/test/java/mockwebserver3/internal/http2/Http2Server.kt`** -> AI Confidence: **99.48%**
30. **`okcurl/src/main/kotlin/okhttp3/curl/Main.kt`** -> AI Confidence: **99.48%**
31. **`okcurl/src/main/kotlin/okhttp3/curl/internal/-MainCommon.kt`** -> AI Confidence: **99.48%**
32. **`okcurl/src/main/kotlin/okhttp3/curl/logging/OneLineLogFormat.kt`** -> AI Confidence: **99.48%**
33. **`okcurl/src/test/kotlin/okhttp3/curl/MainTest.kt`** -> AI Confidence: **99.48%**
34. **`okhttp-dnsoverhttps/src/main/kotlin/okhttp3/dnsoverhttps/DnsOverHttps.kt`** -> AI Confidence: **99.48%**
35. **`okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/DnsOverHttpsTest.kt`** -> AI Confidence: **99.48%**
36. **`okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/TestDohMain.kt`** -> AI Confidence: **99.48%**
37. **`okhttp-hpacktests/src/test/java/okhttp3/internal/http2/HpackRoundTripTest.kt`** -> AI Confidence: **99.48%**
38. **`okhttp-hpacktests/src/test/java/okhttp3/internal/http2/hpackjson/HpackJsonUtil.kt`** -> AI Confidence: **99.48%**
39. **`okhttp-idna-mapping-table/src/main/kotlin/okhttp3/internal/idn/GenerateIdnaMappingTableCode.kt`** -> AI Confidence: **99.48%**
40. **`okhttp-idna-mapping-table/src/main/kotlin/okhttp3/internal/idn/SimpleIdnaMappingTable.kt`** -> AI Confidence: **99.48%**
41. **`okhttp-idna-mapping-table/src/test/kotlin/okhttp3/internal/idn/MappingTablesTest.kt`** -> AI Confidence: **99.48%**
42. **`okhttp-java-net-cookiejar/src/main/kotlin/okhttp3/java/net/cookiejar/JavaNetCookieJar.kt`** -> AI Confidence: **99.48%**
43. **`okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`** -> AI Confidence: **99.48%**
44. **`okhttp-logging-interceptor/src/test/java/okhttp3/logging/HttpLoggingInterceptorTest.kt`** -> AI Confidence: **99.48%**
45. **`okhttp-logging-interceptor/src/test/java/okhttp3/logging/LoggingEventListenerTest.kt`** -> AI Confidence: **99.48%**
46. **`okhttp-osgi-tests/src/test/kotlin/okhttp3/osgi/OsgiTest.kt`** -> AI Confidence: **99.48%**
47. **`okhttp-sse/src/main/kotlin/okhttp3/sse/internal/RealEventSource.kt`** -> AI Confidence: **99.48%**
48. **`okhttp-sse/src/test/java/okhttp3/sse/internal/EventSourceHttpTest.kt`** -> AI Confidence: **99.48%**
49. **`okhttp-sse/src/test/java/okhttp3/sse/internal/EventSourceRecorder.kt`** -> AI Confidence: **99.48%**
50. **`okhttp-sse/src/test/java/okhttp3/sse/internal/ServerSentEventIteratorTest.kt`** -> AI Confidence: **99.48%**
51. **`okhttp-testing-support/src/main/kotlin/okhttp3/EventListenerAdapter.kt`** -> AI Confidence: **99.48%**
52. **`okhttp-testing-support/src/main/kotlin/okhttp3/EventRecorder.kt`** -> AI Confidence: **99.48%**
53. **`okhttp-testing-support/src/main/kotlin/okhttp3/OkHttpClientTestRule.kt`** -> AI Confidence: **99.48%**
54. **`okhttp-testing-support/src/main/kotlin/okhttp3/OkHttpDebugLogging.kt`** -> AI Confidence: **99.48%**
55. **`okhttp-testing-support/src/main/kotlin/okhttp3/RecordingConnectionListener.kt`** -> AI Confidence: **99.48%**
56. **`okhttp-testing-support/src/main/kotlin/okhttp3/TestUtilJvm.kt`** -> AI Confidence: **99.48%**
57. **`okhttp-testing-support/src/main/kotlin/okhttp3/TestValueFactory.kt`** -> AI Confidence: **99.48%**
58. **`okhttp-testing-support/src/main/kotlin/okhttp3/UppercaseRequestInterceptor.kt`** -> AI Confidence: **99.48%**
59. **`okhttp-testing-support/src/main/kotlin/okhttp3/internal/concurrent/TaskFaker.kt`** -> AI Confidence: **99.48%**
60. **`okhttp-testing-support/src/main/kotlin/okhttp3/internal/duplex/AsyncRequestBody.kt`** -> AI Confidence: **99.48%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlTest.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlJvmTest.kt` -> **0.0004%** Exposure
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **0.0001%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/CookieTest.kt` -> **0.0001%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/tls/HostnameVerifierTest.kt` -> **0.0001%** Exposure
### Exploit Generation Surface
- `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt` -> **100.0%** Exposure
- `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` -> **100.0%** Exposure
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **100.0%** Exposure
- `mockwebserver/src/test/java/mockwebserver3/RecordedRequestTest.kt` -> **100.0%** Exposure
- `okhttp-dnsoverhttps/src/main/kotlin/okhttp3/dnsoverhttps/DnsOverHttps.kt` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt` -> **100.0%** Exposure
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Call.kt` -> **100.0%** Exposure
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **100.0%** Exposure
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/ResponseBody.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/CacheResponse.java` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `okhttp-tls/src/main/kotlin/okhttp3/tls/Certificates.kt` -> **100.0%** Exposure
- `okhttp-tls/src/test/java/okhttp3/tls/HeldCertificateTest.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/tls/HostnameVerifierTest.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/kt/CustomTrust.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/CustomTrust.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt` -> **100.0%** Exposure
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/RecordedRequest.kt` -> **100.0%** Exposure
- `mockwebserver-deprecated/src/test/java/okhttp3/mockwebserver/KotlinSourceModernTest.kt` -> **100.0%** Exposure
- `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` -> **100.0%** Exposure
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6595` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt` (KOTLIN) -> Cumulative Risk: **736.93**
- **Archetype:** `file_cluster_8` (Distance: 11.931 IQR)
- **Magnitude:** 556.32 | **LOC:** 530 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.95%)
- **Heaviest Functions:** `any` (Impact: 210.4), `choice` (Impact: 46.2), `sequence` (Impact: 36.6)

### 2. `samples/slack/src/main/java/okhttp3/slack/OAuthSessionFactory.java` (JAVA) -> Cumulative Risk: **732.49**
- **Archetype:** `file_cluster_13` (Distance: 11.844 IQR)
- **Magnitude:** 114.14 | **LOC:** 127 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9978%), State Flux (99.9759%), Algorithmic Dos (97.7596%)
- **Heaviest Functions:** `dispatch` (Impact: 31.1), `close` (Impact: 18.2), `start` (Impact: 8.3)

### 3. `okhttp/src/jvmTest/kotlin/okhttp3/SocketChannelTest.kt` (KOTLIN) -> Cumulative Risk: **731.13**
- **Archetype:** `file_cluster_13` (Distance: 10.939 IQR)
- **Magnitude:** 189.36 | **LOC:** 273 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (97.57%)
- **Heaviest Functions:** `testConnection` (Impact: 139.5), `toString` (Impact: 3.8), `testHttps` (Impact: 3.7)

### 4. `okhttp-tls/src/main/kotlin/okhttp3/tls/HeldCertificate.kt` (KOTLIN) -> Cumulative Risk: **721.14**
- **Archetype:** `file_cluster_13` (Distance: 12.405 IQR)
- **Magnitude:** 217.02 | **LOC:** 609 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9999%), Secrets Risk (99.9998%), Algorithmic Dos (99.9935%)
- **Heaviest Functions:** `decode` (Impact: 41.3), `decode` (Impact: 31.1), `decodePkcs8` (Impact: 12.6)

### 5. `maven-tests/mvnw` (SHELL) -> Cumulative Risk: **719.84**
- **Archetype:** `file_cluster_11` (Distance: 13.764 IQR)
- **Magnitude:** 257.94 | **LOC:** 260 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Injection Surface (99.5158%)
- **Heaviest Functions:** `native_path_[Truncated]` (Impact: 178.8), `__global_context__` (Impact: 3.5)

### 6. `samples/crawler/src/main/java/okhttp3/sample/Crawler.java` (JAVA) -> Cumulative Risk: **716.5**
- **Archetype:** `file_cluster_13` (Distance: 10.893 IQR)
- **Magnitude:** 107.36 | **LOC:** 152 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.5189%), Cognitive Load (88.3928%)
- **Heaviest Functions:** `drainQueue` (Impact: 24.9), `parallelDrainQueue` (Impact: 14.1), `main` (Impact: 12.1)

### 7. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealConnectionPool.kt` (KOTLIN) -> Cumulative Risk: **716.27**
- **Archetype:** `file_cluster_13` (Distance: 11.654 IQR)
- **Magnitude:** 300.9 | **LOC:** 332 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `callAcquirePooledConnection` (Impact: 71.2), `closeConnections` (Impact: 61.8), `evictAll` (Impact: 28.8)

### 8. `okhttp/src/jvmTest/kotlin/okhttp3/FakeRoutePlanner.kt` (KOTLIN) -> Cumulative Risk: **698.88**
- **Archetype:** `file_cluster_8` (Distance: 12.677 IQR)
- **Magnitude:** 185.34 | **LOC:** 217 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Algorithmic Dos (99.9665%)
- **Heaviest Functions:** `plan` (Impact: 28.8), `connectTcp` (Impact: 14.6), `connectTlsEtc` (Impact: 11.8)

### 9. `okhttp/src/jvmTest/kotlin/okhttp3/internal/publicsuffix/PublicSuffixListGenerator.kt` (KOTLIN) -> Cumulative Risk: **691.21**
- **Archetype:** `file_cluster_13` (Distance: 11.581 IQR)
- **Magnitude:** 106.78 | **LOC:** 178 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (91.663%)
- **Heaviest Functions:** `readImportResults` (Impact: 22.0), `toRule` (Impact: 10.7), `writeOut` (Impact: 9.6)

### 10. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/CallServerInterceptor.kt` (KOTLIN) -> Cumulative Risk: **689.29**
- **Archetype:** `file_cluster_13` (Distance: 10.995 IQR)
- **Magnitude:** 291.64 | **LOC:** 208 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `intercept` (Impact: 235.8), `shouldIgnoreAndWaitForRealResponse` (Impact: 6.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.254 IQR)
- **Top Global Matches:** file_cluster_8: 11.254, file_cluster_13: 11.39, file_cluster_0: 11.393
- **Magnitude:** 644.84 | **LOC:** 1466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9711%)
**Top Internal Functions/Classes:**
  * `call` (Impact: 6.7 | O(2^N))
  * `eventListener` (Impact: 6.7 | O(2^N))
  * `mockResponse` (Impact: 6.7 | O(2^N) | DB: 38)
  * `webSocketListener` (Impact: 6.7 | O(2^N))
  * `recordedRequest` (Impact: 6.5 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 171`, `func_start: 167`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 332`, `planned_debt: 123`, `orphaned_logic: 29`
* *Architecture:* `io: 14`, `api: 6`, `import: 69`
* *Defense:* `safety: 4`, `doc: 1`, `test: 69`, `immutability_locks: 320`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` java.net.URI, okhttp3.internal.authenticator.JavaNetAuthenticator, java.security.cert.X509Certificate, java.net.InetAddress, javax.net.ssl.SSLSocketFactory, okhttp3.HttpUrl.Companion.toHttpUrlOrNull, java.math.BigInteger, okhttp3.java.net.cookiejar.JavaNetCookieJar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.241 IQR)
- **Top Global Matches:** file_cluster_13: 12.241, file_cluster_0: 12.313, file_cluster_8: 12.486
- **Magnitude:** 579.7 | **LOC:** 1122 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (40.3086%), Tech Debt (39.9637%)
**Top Internal Functions/Classes:**
  * `detach` (Impact: 137.0 | O(N^4) | DB: 11)
  * `hasNext` (Impact: 70.0 | O(2^N) | DB: 1)
  * `completeEdit` (Impact: 69.5 | O(N^2) | DB: 5)
    * *Intent:* * count, and a blank line. * * Each of the subsequent lines in the file is a record of the state of ...
  * `remove` (Impact: 21.3 | O(2^N) | DB: 2)
  * `rebuildJournal` (Impact: 17.5 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `args: 25`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 105`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 35`, `import: 26`
* *Defense:* `safety: 7`, `doc: 32`, `test: 1`, `sync_locks: 16`, `immutability_locks: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.118
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.067557
  * `Imports (Out-Degree: 4):` okhttp3.internal.concurrent.TaskRunner, java.io.Closeable, okhttp3.internal.platform.Platform, okio.Sink, okhttp3.internal.closeQuietly, okhttp3.internal.concurrent.assertLockHeld, okhttp3.internal.concurrent.Task, okhttp3.internal.concurrent.Lockable...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/Adapters.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.931 IQR)
- **Top Global Matches:** file_cluster_8: 11.931, file_cluster_16: 12.009, file_cluster_13: 12.133
- **Magnitude:** 556.32 | **LOC:** 530 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (42.7472%), Tech Debt (99.95%)
**Top Internal Functions/Classes:**
  * `any` (Impact: 210.4 | O(2^N))
    * *Intent:* /**
  * `choice` (Impact: 46.2 | O(2^N))
  * `sequence` (Impact: 36.6 | O(N^3) | DB: 5)
  * `usingTypeHint` (Impact: 27.0 | O(N^2))
  * `parseUtcTime` (Impact: 12.8 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `args: 48`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 93`, `planned_debt: 4`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 3`, `doc: 10`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.TimeZone, java.util.Date, java.math.BigInteger, java.net.ProtocolException, java.text.SimpleDateFormat, okio.ByteString, kotlin.reflect.KClass, java.text.ParseException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/EventListener.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.616 IQR)
- **Top Global Matches:** file_cluster_8: 9.616, file_cluster_7: 10.053, file_cluster_1: 10.301
- **Magnitude:** 533.3 | **LOC:** 860 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.4172%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `plus` (Impact: 24.8 | O(N^2) | DB: 2)
  * `connectFailed` (Impact: 16.4 | O(2^N))
    * *Intent:* /** * Invoked immediately after receiving response headers. * * This method is always invoked after ...
  * `connectEnd` (Impact: 15.2 | O(2^N))
    * *Intent:* /** * Invoked when response headers are first returned from the server. * * The connection is implic...
  * `proxySelectEnd` (Impact: 13.9 | O(2^N))
    * *Intent:* /** * Invoked immediately after sending request headers. * * This method is always invoked after [re...
  * `dnsEnd` (Impact: 13.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 60`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 38`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116539
  * `Imports (Out-Degree: 0):` java.net.InetAddress, java.net.InetSocketAddress, java.net.ProtocolException, java.net.Proxy, java.io.IOException
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.428 IQR)
- **Top Global Matches:** file_cluster_13: 12.428, file_cluster_8: 12.506, file_cluster_0: 12.595
- **Magnitude:** 519.84 | **LOC:** 403 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (66.9815%), Tech Debt (65.9856%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 61.7 | O(2^N) | DB: 2)
  * `bodyComplete` (Impact: 53.2 | O(N^2) | DB: 6)
    * *Intent:* /** * Revoke this exchange's access to streams. This is necessary when a follow-up request is
  * `write` (Impact: 37.1 | O(2^N) | DB: 2)
  * `close` (Impact: 37.1 | O(2^N) | DB: 1)
  * `close` (Impact: 26.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `args: 24`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 126`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `import: 16`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.312
  * `Choke Point (Betweenness):` 0.001904 | `Ripple Effect (Closeness):` 0.111586
  * `Imports (Out-Degree: 7):` okhttp3.Headers, okio.Source, okhttp3.Response, okio.ForwardingSource, okio.buffer, okhttp3.Request, okio.Sink, okio.Socket...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.767 IQR)
- **Top Global Matches:** file_cluster_13: 12.767, file_cluster_0: 13.109, file_cluster_8: 13.194
- **Magnitude:** 482.78 | **LOC:** 627 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (44.6196%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `callDone` (Impact: 153.6 | O(N^3) | DB: 16)
  * `messageDone` (Impact: 99.7 | O(N^2) | DB: 5)
  * `noMoreExchanges` (Impact: 24.8 | O(N^2) | DB: 3)
  * `enterNetworkInterceptorExchange` (Impact: 22.1 | O(N^2) | DB: 14)
  * `initExchange` (Impact: 13.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `args: 28`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 119`
* *Architecture:* `io: 1`, `api: 32`, `import: 36`
* *Defense:* `safety: 19`, `doc: 16`, `test: 5`, `sync_locks: 9`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.562
  * `Choke Point (Betweenness):` 0.015594 | `Ripple Effect (Closeness):` 0.138551
  * `Imports (Out-Degree: 14):` java.util.concurrent.TimeUnit.MILLISECONDS, okhttp3.Interceptor, okhttp3.internal.computeIfAbsent, okhttp3.internal.http.BridgeInterceptor, okhttp3.internal.platform.Platform, okhttp3.internal.closeQuietly, okhttp3.internal.concurrent.assertLockHeld, kotlin.reflect.KClass...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.982 IQR)
- **Top Global Matches:** file_cluster_8: 11.982, file_cluster_13: 12.078, file_cluster_0: 12.267
- **Magnitude:** 454.92 | **LOC:** 4983 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (14.0034%), Tech Debt (96.8429%)
**Top Internal Functions/Classes:**
  * `gzip` (Impact: 53.0 | O(2^N) | DB: 17)
  * `connectionReuseWhenResponseBodyConsumed_` (Impact: 30.0 | O(N^4) | DB: 15)
  * `cancelLater` (Impact: 16.9 | O(N^3))
  * `canceledAfterResponseIsDeliveredBreaksSt` (Impact: 15.8 | O(N^3) | DB: 5)
  * `executeSynchronously` (Impact: 12.7 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `args: 134`, `func_start: 116`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 108`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 38`
* *Architecture:* `io: 5`, `api: 8`, `import: 124`
* *Defense:* `safety: 9`, `doc: 13`, `test: 252`, `sync_locks: 8`, `immutability_locks: 133`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` javax.net.ssl.SSLSocketFactory, org.junit.jupiter.api.Assumptions.assumeFalse, okhttp3.tls.HandshakeCertificates, mockwebserver3.SocketEffect.CloseSocket, assertk.assertions.isNotNull, assertk.assertions.isLessThan, assertk.assertions.isNotEmpty, okhttp3.HttpUrl.Companion.toHttpUrl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.947 IQR)
- **Top Global Matches:** file_cluster_13: 11.947, file_cluster_8: 12.127, file_cluster_0: 12.226
- **Magnitude:** 422.24 | **LOC:** 606 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.2278%), Tech Debt (91.3813%)
**Top Internal Functions/Classes:**
  * `readSettings` (Impact: 71.7 | O(N^3))
  * `read` (Impact: 42.9 | O(2^N) | DB: 2)
  * `nextFrame` (Impact: 26.6 | O(N^1))
  * `readWindowUpdate` (Impact: 23.4 | O(N^2) | DB: 5)
  * `readGoAway` (Impact: 19.5 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `args: 31`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`, `planned_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 26`, `import: 34`
* *Defense:* `safety: 5`, `doc: 31`, `immutability_locks: 43`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` okhttp3.internal.http2.Http2.FLAG_PADDED, java.io.Closeable, okhttp3.internal.http2.Http2.TYPE_RST_STREAM, okhttp3.internal.and, okhttp3.internal.http2.Http2.FLAG_ACK, okhttp3.internal.readMedium, okhttp3.internal.http2.Http2.TYPE_HEADERS, java.util.logging.Level.FINE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.598 IQR)
- **Top Global Matches:** file_cluster_8: 11.598, file_cluster_12: 11.849, file_cluster_13: 11.931
- **Magnitude:** 390.5 | **LOC:** 2538 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^4) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (98.1493%), Tech Debt (37.9998%)
**Top Internal Functions/Classes:**
  * `responseBodyFail` (Impact: 84.0 | O(N^4) | DB: 28)
  * `assertBytesReadWritten` (Impact: 38.3 | O(N^2))
  * `assertSuccessfulEventOrder` (Impact: 14.9 | O(N^3) | DB: 3)
  * `tearDown` (Impact: 5.6 | O(N^1))
  * `successfulCallEventSequenceForIpAddress` (Impact: 5.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `args: 89`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 62`, `orphaned_logic: 38`
* *Architecture:* `io: 3`, `api: 4`, `import: 89`
* *Defense:* `safety: 3`, `doc: 5`, `test: 200`, `immutability_locks: 147`, `cleanup: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` assertk.assertions.isSameInstanceAs, org.hamcrest.MatcherAssert, mockwebserver3.SocketEffect.CloseSocket, assertk.assertions.isNotNull, assertk.assertions.isNotEmpty, okhttp3.HttpUrl.Companion.toHttpUrl, okhttp3.CallEvent.ResponseBodyStart, okhttp3.CallEvent.ResponseHeadersEnd...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http1/Http1ExchangeCodec.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.982 IQR)
- **Top Global Matches:** file_cluster_13: 11.982, file_cluster_8: 12.125, file_cluster_7: 12.447
- **Magnitude:** 382.9 | **LOC:** 584 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (27.9341%), Tech Debt (80.8361%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 55.1 | O(2^N) | DB: 1)
    * *Intent:* /** * Sets the delegate of `timeout` to [Timeout.NONE] and resets its underlying timeout * to the de...
  * `read` (Impact: 36.8 | O(2^N) | DB: 1)
  * `readResponseHeaders` (Impact: 32.5 | O(N^2) | DB: 8)
  * `readChunkSize` (Impact: 28.9 | O(N^3) | DB: 2)
  * `openResponseBodySource` (Impact: 15.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `args: 26`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 68`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 22`, `import: 27`
* *Defense:* `safety: 14`, `doc: 11`, `immutability_locks: 38`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.973
  * `Choke Point (Betweenness):` 0.000197 | `Ripple Effect (Closeness):` 0.009409
  * `Imports (Out-Degree: 9):` java.util.concurrent.TimeUnit.MILLISECONDS, okhttp3.Headers, okio.Sink, okhttp3.internal.connection.BufferedSocket, okhttp3.internal.http.ExchangeCodec, java.io.EOFException, okio.Timeout, okhttp3.internal.discard...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.583 IQR)
- **Top Global Matches:** file_cluster_8: 11.583, file_cluster_13: 11.706, file_cluster_0: 11.893
- **Magnitude:** 375.64 | **LOC:** 4543 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (10.6425%), Tech Debt (98.6782%)
**Top Internal Functions/Classes:**
  * `connectionCloseInRequest` (Impact: 48.6 | O(N^3) | DB: 35)
  * `doUpload` (Impact: 46.2 | O(N^3) | DB: 5)
  * `writeTimeouts` (Impact: 12.9 | O(N^3) | DB: 7)
  * `connectViaHttpsReusingConnectionsDiffere` (Impact: 9.9 | O(N^2) | DB: 2)
  * `connectViaHttpsReusingConnections` (Impact: 7.8 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `args: 109`, `func_start: 101`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 81`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 4`, `orphaned_logic: 38`
* *Architecture:* `io: 13`, `api: 11`, `import: 86`
* *Defense:* `safety: 6`, `doc: 16`, `test: 157`, `sync_locks: 1`, `immutability_locks: 98`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.net.URI, java.util.EnumSet, mockwebserver3.SocketEffect.CloseSocket, assertk.assertions.isLessThan, assertk.assertions.isNotEmpty, org.opentest4j.TestAbortedException, okhttp3.HttpUrl.Companion.toHttpUrl, okio.buffer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cache.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.845 IQR)
- **Top Global Matches:** file_cluster_13: 11.845, file_cluster_0: 12.088, file_cluster_8: 12.127
- **Magnitude:** 370.26 | **LOC:** 838 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (56.8806%), Tech Debt (25.6552%)
**Top Internal Functions/Classes:**
  * `source` (Impact: 103.0 | O(2^N) | DB: 5)
  * `requestCount` (Impact: 50.5 | O(2^N) | DB: 4)
    * *Intent:* * the cache, and fetch data directly from the server. To force a full refresh, add the `no-cache` * ...
  * `constructor` (Impact: 26.8 | O(N^3) | DB: 11)
  * `readCertificateList` (Impact: 25.0 | O(N^2) | DB: 1)
  * `writeTo` (Impact: 22.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `args: 31`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 73`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 16`, `import: 35`
* *Defense:* `safety: 6`, `doc: 11`, `sync_locks: 7`, `immutability_locks: 63`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.702
  * `Choke Point (Betweenness):` 0.002155 | `Ripple Effect (Closeness):` 0.082762
  * `Imports (Out-Degree: 8):` java.security.cert.CertificateEncodingException, okhttp3.internal.concurrent.TaskRunner, java.io.Closeable, okhttp3.internal.platform.Platform, okhttp3.HttpUrl.Companion.toHttpUrlOrNull, okio.Sink, java.security.cert.CertificateFactory, okhttp3.internal.closeQuietly...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpMethod.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.335 IQR)
- **Top Global Matches:** file_cluster_0: 13.335, file_cluster_8: 13.398, file_cluster_13: 13.464
- **Magnitude:** 366.05 | **LOC:** 52 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.975
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130702
  * `Imports (Out-Degree: 0):` kotlin.jvm.JvmStatic
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.344 IQR)
- **Top Global Matches:** file_cluster_13: 12.344, file_cluster_8: 12.734, file_cluster_0: 12.816
- **Magnitude:** 360.1 | **LOC:** 703 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (68.7092%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isValid` (Impact: 174.8 | O(N^3) | DB: 48)
  * `connect` (Impact: 26.6 | O(N^3) | DB: 7)
  * `cancel` (Impact: 3.6 | O(2^N))
    * *Intent:* /** This task processes the outgoing queues. Call [runWriter] to after enqueueing. */
  * `onFailure` (Impact: 3.3 | O(N^2))
  * `init` (Impact: 1.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `args: 15`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 123`
* *Architecture:* `io: 2`, `api: 21`, `import: 36`
* *Defense:* `safety: 9`, `doc: 12`, `sync_locks: 8`, `immutability_locks: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.878
  * `Choke Point (Betweenness):` 0.005104 | `Ripple Effect (Closeness):` 0.13617
  * `Imports (Out-Degree: 14):` java.util.concurrent.TimeUnit.MILLISECONDS, okhttp3.internal.concurrent.TaskRunner, okhttp3.WebSocket, okhttp3.WebSocketListener, okhttp3.internal.ws.WebSocketProtocol.CLOSE_MESSAGE_MAX, okhttp3.internal.closeQuietly, okhttp3.internal.connection.BufferedSocket, okhttp3.internal.concurrent.assertLockHeld...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.585 IQR)
- **Top Global Matches:** file_cluster_8: 10.585, file_cluster_13: 10.631, file_cluster_0: 11.065
- **Magnitude:** 344.32 | **LOC:** 516 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (20.7455%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 312.5 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `args: 69`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 8`, `import: 34`
* *Defense:* `safety: 4`, `doc: 2`, `test: 1`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.115
  * `Choke Point (Betweenness):` 0.002537 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 7):` org.openjsse.net.ssl.OpenJSSE, okhttp3.TestUtil, okhttp3.internal.platform.Platform, org.junit.jupiter.api.Assumptions.assumeFalse, com.amazon.corretto.crypto.provider.SelfTestStatus, okhttp3.tls.HandshakeCertificates, org.hamcrest.Description, org.bouncycastle.jsse.provider.BouncyCastleJsseProvider...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.339 IQR)
- **Top Global Matches:** file_cluster_13: 11.339, file_cluster_8: 11.416, file_cluster_0: 11.635
- **Magnitude:** 336.64 | **LOC:** 371 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (38.9097%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 281.8 | O(N^3) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `args: 13`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 43`
* *Architecture:* `io: 2`, `api: 7`, `import: 16`
* *Defense:* `safety: 2`, `doc: 7`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.489
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.010582
  * `Imports (Out-Degree: 7):` okhttp3.internal.isProbablyUtf8, okhttp3.Headers, okhttp3.Interceptor, okhttp3.internal.http.promisesBody, okhttp3.Response, okhttp3.OkHttpClient, okhttp3.internal.UnreadableResponseBody, okhttp3.internal.platform.Platform...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.347 IQR)
- **Top Global Matches:** file_cluster_13: 11.347, file_cluster_8: 11.401, file_cluster_0: 11.649
- **Magnitude:** 330.68 | **LOC:** 1094 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (21.7124%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testConscryptRequest` (Impact: 24.4 | O(N^4) | DB: 6)
  * `testRequestUsesPlayProvider` (Impact: 23.9 | O(N^4) | DB: 6)
  * `testUnderscoreRequest` (Impact: 19.0 | O(N^3))
  * `testBouncyCastleRequest` (Impact: 15.5 | O(N^4) | DB: 3)
  * `testRequestUsesAndroidConscrypt` (Impact: 14.8 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `args: 57`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 51`, `planned_debt: 3`, `orphaned_logic: 27`
* *Architecture:* `io: 10`, `api: 13`, `import: 96`
* *Defense:* `safety: 7`, `test: 96`, `sync_locks: 3`, `immutability_locks: 79`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory, com.squareup.moshi.Moshi, androidx.test.platform.app.InstrumentationRegistry, okhttp3.tls.HandshakeCertificates, okhttp3.Cache, org.opentest4j.TestAbortedException, java.security.cert.Certificate, okhttp3.HttpUrl.Companion.toHttpUrl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.113 IQR)
- **Top Global Matches:** file_cluster_13: 12.113, file_cluster_8: 12.384, file_cluster_0: 12.413
- **Magnitude:** 325.94 | **LOC:** 1817 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (48.8111%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `schemeDelimiterOffset` (Impact: 142.5 | O(N^3) | DB: 2)
    * *Intent:* * retrieve the resource. Although URLs have many schemes (`mailto`, `file`, `ftp`), this class only ...
  * `push` (Impact: 33.2 | O(N^2) | DB: 6)
    * *Intent:* /**
  * `toQueryNamesAndValues` (Impact: 19.1 | O(N^2) | DB: 8)
    * *Intent:* * clicking a relative link on a specified page. For example: * * ```java * HttpUrl base = HttpUrl.pa...
  * `pop` (Impact: 10.9 | O(N^2) | DB: 1)
    * *Intent:* * ``` * * As another example, this code prints the human-readable query parameters of a Twitter sear...
  * `defaultPort` (Impact: 9.3 | O(N^2))
    * *Intent:* * ``` * http://who-let-the-dogs.out/_Who%3F_?_Who?_#_Who?_ * ``` * * When parsing URLs that lack per...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 23`, `import: 25`
* *Defense:* `doc: 13`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.805
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.114869
  * `Imports (Out-Degree: 1):` java.net.URI, okhttp3.internal.canParseAsIpAddress, java.net.MalformedURLException, okhttp3.internal.delimiterOffset, okhttp3.HttpUrl.Companion.toHttpUrlOrNull, okhttp3.internal.url.FRAGMENT_ENCODE_SET, okhttp3.internal.url.QUERY_COMPONENT_ENCODE_SET, okhttp3.HttpUrl.Companion.toHttpUrl...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.065 IQR)
- **Top Global Matches:** file_cluster_8: 11.065, file_cluster_13: 11.131, file_cluster_16: 11.425
- **Magnitude:** 310.66 | **LOC:** 874 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (11.9517%), Tech Debt (99.3464%)
**Top Internal Functions/Classes:**
  * `testOverrideBadImplementation` (Impact: 90.8 | O(N^5) | DB: 20)
  * `overrideBadImplementation` (Impact: 35.0 | O(N^4) | DB: 1)
  * `createSocket` (Impact: 15.7 | O(N^3) | DB: 6)
  * `testOverrideInNetworkInterceptor` (Impact: 13.5 | O(N^4) | DB: 1)
  * `isDefaultValue` (Impact: 11.3 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `args: 59`, `func_start: 49`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 40`, `planned_debt: 11`, `duplicate_logic: 9`, `orphaned_logic: 3`
* *Architecture:* `io: 40`, `api: 3`, `import: 46`
* *Defense:* `safety: 4`, `doc: 1`, `test: 4`, `immutability_locks: 53`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.net.URI, java.util.Locale.getDefault, kotlin.time.Duration.Companion.nanoseconds, java.security.cert.X509Certificate, assertk.assertThat, assertk.assertions.isNotSameInstanceAs, javax.net.ssl.SSLSocketFactory, mockwebserver3.MockWebServer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/CacheInterceptor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.485 IQR)
- **Top Global Matches:** file_cluster_13: 10.485, file_cluster_8: 10.571, file_cluster_7: 10.936
- **Magnitude:** 309.46 | **LOC:** 310 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (33.9729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `intercept` (Impact: 255.8 | O(N^3) | DB: 10)
  * `requestForCache` (Impact: 11.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 28`
* *Architecture:* `api: 10`, `import: 22`
* *Defense:* `doc: 5`, `immutability_locks: 23`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.229
  * `Choke Point (Betweenness):` 0.001971 | `Ripple Effect (Closeness):` 0.100171
  * `Imports (Out-Degree: 10):` java.util.concurrent.TimeUnit.MILLISECONDS, okhttp3.Headers, okhttp3.Interceptor, java.net.HttpURLConnection.HTTP_NOT_MODIFIED, java.net.HttpURLConnection.HTTP_GATEWAY_TIMEOUT, okhttp3.internal.closeQuietly, okhttp3.internal.http.RealResponseBody, okhttp3.Cache...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealConnectionPool.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.654 IQR)
- **Top Global Matches:** file_cluster_13: 11.654, file_cluster_8: 11.789, file_cluster_7: 12.074
- **Magnitude:** 300.9 | **LOC:** 332 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^3) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (55.0618%), Tech Debt (17.225%)
**Top Internal Functions/Classes:**
  * `callAcquirePooledConnection` (Impact: 71.2 | O(N^3) | DB: 2)
    * *Intent:* /**
  * `closeConnections` (Impact: 61.8 | O(N^2) | DB: 18)
  * `evictAll` (Impact: 28.8 | O(N^3) | DB: 2)
  * `pruneAndGetAllocationCount` (Impact: 22.7 | O(N^2) | DB: 2)
  * `connectionBecameIdle` (Impact: 12.7 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `args: 11`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 73`, `fragile_debt: 1`
* *Architecture:* `api: 19`, `import: 15`
* *Defense:* `safety: 1`, `doc: 6`, `test: 3`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.747
  * `Choke Point (Betweenness):` 0.00053 | `Ripple Effect (Closeness):` 0.069552
  * `Imports (Out-Degree: 7):` okhttp3.internal.concurrent.Task, okhttp3.ConnectionPool, okhttp3.internal.concurrent.TaskRunner, okhttp3.internal.platform.Platform, java.util.concurrent.TimeUnit, okhttp3.internal.okHttpName, java.util.concurrent.ConcurrentLinkedQueue, okhttp3.internal.closeQuietly...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/CallServerInterceptor.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.995 IQR)
- **Top Global Matches:** file_cluster_13: 10.995, file_cluster_8: 11.021, file_cluster_7: 11.479
- **Magnitude:** 291.64 | **LOC:** 208 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^5) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (58.7767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `intercept` (Impact: 235.8 | O(N^5) | DB: 14)
  * `shouldIgnoreAndWaitForRealResponse` (Impact: 6.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 41`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.229
  * `Choke Point (Betweenness):` 0.001512 | `Ripple Effect (Closeness):` 0.100518
  * `Imports (Out-Degree: 6):` okhttp3.internal.http2.ConnectionShutdownException, okhttp3.Headers, okhttp3.Interceptor, okhttp3.Response, okhttp3.internal.skipAll, okhttp3.internal.UnreadableResponseBody, okio.buffer, java.net.ProtocolException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.347 IQR)
- **Top Global Matches:** file_cluster_8: 11.347, file_cluster_0: 11.599, file_cluster_13: 11.648
- **Magnitude:** 282.82 | **LOC:** 2160 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (14.5227%), Tech Debt (99.7622%)
**Top Internal Functions/Classes:**
  * `readJournalLines` (Impact: 13.5 | O(N^2) | DB: 1)
  * `createJournalWithHeader` (Impact: 9.7 | O(N^2))
  * `readFileOrNull` (Impact: 6.3 | O(N^2))
  * `create` (Impact: 5.8 | O(2^N))
  * `assertValue` (Impact: 5.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `args: 90`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 76`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 41`
* *Architecture:* `io: 2`, `api: 5`, `import: 31`
* *Defense:* `safety: 6`, `doc: 7`, `test: 200`, `sync_locks: 1`, `immutability_locks: 66`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assertk.assertions.isSameInstanceAs, okhttp3.TestUtil, org.junit.jupiter.api.Tag, assertk.assertThat, assertk.assertions.isNull, assertk.fail, java.util.ArrayDeque, okhttp3.internal.concurrent.TaskFaker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp-idna-mapping-table/src/main/kotlin/okhttp3/internal/idn/MappingTables.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.338 IQR)
- **Top Global Matches:** file_cluster_8: 12.338, file_cluster_16: 12.48, file_cluster_13: 12.536
- **Magnitude:** 280.52 | **LOC:** 299 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (54.6707%), Tech Debt (14.3183%)
**Top Internal Functions/Classes:**
  * `sections` (Impact: 42.2 | O(N^3) | DB: 2)
  * `buildIdnaMappingTableData` (Impact: 40.2 | O(N^3) | DB: 7)
    * *Intent:* /* * Copyright (C) 2023 Square, Inc. * * Licensed under the Apache License, Version 2.0 (the "Licens...
  * `mergeAdjacentRanges` (Impact: 28.6 | O(N^2) | DB: 8)
  * `mergeAdjacentDeltaMappedRanges` (Impact: 28.1 | O(N^2) | DB: 4)
  * `withoutSectionSpans` (Impact: 25.5 | O(N^2) | DB: 5)
    * *Intent:* /** * Modifies [ranges] to combine any adjacent [MappedRange.InlineDelta] of same size to single ent...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `args: 13`, `func_start: 10`
* *Risk/State:* `state_mutation: 76`, `orphaned_logic: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 10`, `doc: 7`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` okio.Buffer, kotlin.streams.toList, kotlin.math.abs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RealInterceptorChain.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.963 IQR)
- **Top Global Matches:** file_cluster_13: 12.963, file_cluster_8: 13.197, file_cluster_0: 13.433
- **Magnitude:** 277.74 | **LOC:** 375 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (61.9534%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `proceed` (Impact: 37.6 | O(2^N))
  * `withSslSocketFactory` (Impact: 19.1 | O(N^2) | DB: 7)
  * `withCertificatePinner` (Impact: 12.6 | O(N^2))
  * `address` (Impact: 7.2 | O(N^1) | DB: 18)
  * `withConnectTimeout` (Impact: 4.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `args: 25`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 106`
* *Architecture:* `io: 2`, `api: 30`, `import: 27`
* *Defense:* `safety: 21`, `doc: 2`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.722
  * `Choke Point (Betweenness):` 0.007517 | `Ripple Effect (Closeness):` 0.102528
  * `Imports (Out-Degree: 18):` okhttp3.Authenticator, okhttp3.Interceptor, javax.net.ssl.SSLSocketFactory, javax.net.ssl.HostnameVerifier, okhttp3.Cache, okhttp3.Connection, okhttp3.internal.connection.RealCall, javax.net.ssl.X509TrustManager...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/RequestBody.kt` (KOTLIN) | Magnitude: 92.58 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, args: 33, func_start: 31, decorators: 31
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/CacheControl.kt` (KOTLIN) | Magnitude: 70.64 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, state_mutation: 42, decorators: 27, immutability_locks: 25
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Challenge.kt` (KOTLIN) | Magnitude: 54.42 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 36, decorators: 12, immutability_locks: 12
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpMethod.kt` (KOTLIN) | Magnitude: 366.05 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 24, branch: 11, args: 6
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Handshake.kt` (KOTLIN) | Magnitude: 85.6 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 33, branch: 15, decorators: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `maven-tests/mvnw` (SHELL) | Magnitude: 257.94 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, io: 85, branch: 79, state_mutation: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/CipherSuite.kt` (KOTLIN) | Magnitude: 89.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 177, immutability_locks: 129, decorators: 124, reflection_metaprogramming: 121
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/AddressPolicy.kt` (KOTLIN) | Magnitude: 14.12 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, decorators: 3, reflection_metaprogramming: 3, immutability_locks: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/SuppressSignatureCheck.kt` (KOTLIN) | Magnitude: 16.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 4, decorators: 3, api: 2, encapsulation: 2
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/concurrent/Lockable.kt` (KOTLIN) | Magnitude: 35.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, api: 12, reflection_metaprogramming: 8, encapsulation: 8
- `okhttp/src/androidMain/kotlin/okhttp3/internal/platform/ContextAwarePlatform.kt` (KOTLIN) | Magnitude: 14.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 1, api: 1, state_mutation: 1, import: 1
- `okhttp/src/jvmTest/kotlin/okhttp3/JSSETest.kt` (KOTLIN) | Magnitude: 43.82 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, import: 21, test: 20, decorators: 10
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/io/FaultyFileSystem.kt` (KOTLIN) | Magnitude: 96.54 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 23, branch: 12, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/CertificateAdapters.kt` (KOTLIN) | Magnitude: 163.16 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 271, state_mutation: 68, safety_bypasses: 33, explicit_casts: 28
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/InsecureAndroidTrustManager.kt` (KOTLIN) | Magnitude: 50.76 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, branch: 8, generics: 8, import: 6
- `okhttp-hpacktests/src/test/java/okhttp3/internal/http2/hpackjson/Case.kt` (KOTLIN) | Magnitude: 58.31 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, immutability_locks: 6, api: 3, state_mutation: 3
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RouteDatabase.kt` (KOTLIN) | Magnitude: 9.48 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, doc: 4, decorators: 4, sync_locks: 4
- `okhttp-tls/src/main/kotlin/okhttp3/tls/internal/der/DerAdapter.kt` (KOTLIN) | Magnitude: 83.58 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, state_mutation: 25, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/PushPromise.kt` (KOTLIN) | Magnitude: 53.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 12, decorators: 12, immutability_locks: 8
- `okcurl/src/main/kotlin/okhttp3/curl/Main.kt` (KOTLIN) | Magnitude: 42.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, import: 26, immutability_locks: 26, args: 13
- `okcurl/src/main/kotlin/okhttp3/curl/internal/-MainCommon.kt` (KOTLIN) | Magnitude: 61.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, branch: 19, immutability_locks: 11, import: 8
- `okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/TestDohMain.kt` (KOTLIN) | Magnitude: 82.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 51, debug_prints: 10, import: 8
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilCommon.kt` (KOTLIN) | Magnitude: 274.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 196, branch: 93, api: 29, panics_and_aborts: 29

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cache.kt` -> Churn: **77.7%** | Cog Load: 56.8806% | Debt: 25.6552%
- `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -> Churn: **60.91%** | Cog Load: 14.0034% | Debt: 96.8429%
- `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` -> Churn: **55.93%** | Cog Load: 0.0% | Debt: 99.9711%
- `okhttp/src/jvmTest/kotlin/okhttp3/RequestTest.kt` -> Churn: **55.83%** | Cog Load: 34.2713% | Debt: 94.6625%
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/http/HttpUpgradesTest.kt` -> Churn: **52.6%** | Cog Load: 0.0% | Debt: 60.3713%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 579.7
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/EventListener.kt` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 533.3
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 422.24
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http1/Http1ExchangeCodec.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 382.9
- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 375.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 1.966** (Bridge: 0.0197 * Flux: 99.9455%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` -> **Severity: 1.559** (Bridge: 0.0156 * Flux: 99.9919%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/RealInterceptorChain.kt` -> **Severity: 0.752** (Bridge: 0.0075 * Flux: 99.996%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` -> **Severity: 0.51** (Bridge: 0.0051 * Flux: 99.9992%)
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **Severity: 0.37** (Bridge: 0.0046 * Flux: 79.7731%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/HttpMethod.kt` -> **Severity: 10.92** (Embedded: 0.1307 * Error Risk: 83.5484%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 9.519** (Embedded: 0.1789 * Error Risk: 53.1959%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Request.kt` -> **Severity: 9.08** (Embedded: 0.1812 * Error Risk: 50.1149%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/concurrent/Lockable.kt` -> **Severity: 8.927** (Embedded: 0.1116 * Error Risk: 80.0%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/platform/Platform.kt` -> **Severity: 8.689** (Embedded: 0.1719 * Error Risk: 50.5479%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/platform/Platform.kt` -> **Severity: 1677.476** (Blast Radius: 21.138 * Doc Risk: 79.3583%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Headers.kt` -> **Severity: 1423.673** (Blast Radius: 15.489 * Doc Risk: 91.9151%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt` -> **Severity: 1061.412** (Blast Radius: 16.312 * Doc Risk: 65.0694%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/tls/CertificateChainCleaner.kt` -> **Severity: 1018.016** (Blast Radius: 10.92 * Doc Risk: 93.2249%)
- `mockwebserver-junit5/src/main/kotlin/mockwebserver3/junit5/internal/StartStopExtension.kt` -> **Severity: 931.6** (Blast Radius: 9.316 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
