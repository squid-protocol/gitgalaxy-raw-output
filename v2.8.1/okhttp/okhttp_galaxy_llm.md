# ARCHITECTURAL_BRIEF: okhttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/square/okhttp` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 794 |
| Analyzed Artifacts (Scanned) | 674 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 120 |
| Total LOC | 100557 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 84.9% |
| Dominant Lang | KOTLIN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4576 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1705 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4612 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| KOTLIN | 532 | 96795 | 78.9% |
| JAVA | 71 | 2849 | 10.5% |
| MARKDOWN | 29 | 0 | 4.3% |
| PLAINTEXT | 17 | 0 | 2.5% |
| XML | 11 | 0 | 1.6% |
| JSON | 7 | 384 | 1.0% |
| SHELL | 4 | 218 | 0.6% |
| BATCH | 2 | 204 | 0.3% |
| YAML | 1 | 107 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +1.59; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 22%, Tests & Verification Files 22%, Large Core Modules 16%, Data / Markup / Trivial 16%, Annotated Framework Methods Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 628 | 93.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 6.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 120*

**Composition by Extension & Reason:**
- `.kts`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 45 LOC)
- `.api`: 15x Excluded (Unsupported Extension: '.api')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 249 LOC)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.pro), 1x Excluded (Unsupported Extension: '.pro')
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 1x Excluded (Machine-Generated Source Code Signature: 4 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.config`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.list`: 2x Excluded (Binary Format Detected)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.4 | 12.5 | 6.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 39.8 | 49.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 36.6 | 16.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.4 | 8.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 21.7 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.9 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 84.4 | 6.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 69.4 | 90.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 979 | 228 | 4 | `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlTest.kt` |
| cleanup | 629 | 137 | 2 | `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` |
| guards | 5087 | 512 | 20 | `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` |
| danger | 3660 | 419 | 14 | `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/HpackTest.kt` |
| concurrency | 411 | 90 | 1 | `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` |
| connectivity | 2009 | 305 | 8 | `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` |
| io | 572 | 140 | 2 | `maven-tests/mvnw` |
| crypto | 0 | 0 | 0 | - |
| ipc | 14 | 3 | 0 | `maven-tests/mvnw` |
| time | 40 | 10 | 0 | `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` |
| serialization | 13 | 8 | 0 | `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt` |
| regex | 289 | 37 | 0 | `okhttp-logging-interceptor/src/test/java/okhttp3/logging/HttpLoggingInterceptorTest.kt` |
| events | 175 | 36 | 0 | `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` |
| tests | 11024 | 222 | 30 | `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` |
| docs | 1847 | 360 | 8 | `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` |
| debt | 648 | 158 | 2 | `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` |
| mutation | 20037 | 538 | 75 | `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` |
| dead_code | 3508 | 371 | 12 | `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` |
| credential | 227 | 17 | 0 | `samples/guide/src/main/java/okhttp3/recipes/CustomTrust.java` |
| threat | 2143 | 254 | 5 | `okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt` |
| ml_ai | 226 | 46 | 0 | `okhttp/src/jvmTest/kotlin/okhttp3/internal/concurrent/TaskRunnerTest.kt` |
| ui | 8 | 3 | 0 | `mockwebserver-junit5/src/main/kotlin/mockwebserver3/junit5/internal/StartStopExtension.kt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `maven-tests/mvnw` (Hits: 88)
- `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt` (Hits: 41)
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

- `constructor` **(Many-Argument Workhorses)** (@ `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt`) -> Impact: **102.4** | LOC: 455
- `writeCanonicalized` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/url/-Url.kt`) -> Impact: **101.2** | LOC: 63
- `constructor` **(Compute Cores)** (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **97.0** | LOC: 327
- `constructor` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Hpack.kt`) -> Impact: **84.5** | LOC: 289
- `constructor` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Hpack.kt`) -> Impact: **77.7** | LOC: 233
- `intercept` **(Compute Cores)** (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **73.4** | LOC: 167
- `parse` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt`) -> Impact: **62.3** | LOC: 172
- `parse` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cookie.kt`) -> Impact: **57.0** | LOC: 141
- `messageDone` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt`) -> Impact: **55.0** | LOC: 42
  * *Intent:* /** * Releases resources held with the request or response of [exchange]. This should be called when * the request completes normally or when it fails...
- `main` **(Compute Cores)** (@ `samples/slack/src/main/java/okhttp3/slack/SlackClient.java`) -> Impact: **53.6** | LOC: 25

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `okhttp/src/jvmTest/kotlin/okhttp3` | 85 | 7601.3 | 12.02% | 82.65% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3` | 40 | 3814.4 | 21.14% | 4.96% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2` | 15 | 1943.1 | 14.97% | 21.31% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection` | 21 | 1362.62 | 12.69% | 28.56% |
| `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2` | 9 | 1140.52 | 13.32% | 78.65% |
| `okhttp-testing-support/src/main/kotlin/okhttp3` | 30 | 974.58 | 10.54% | 44.32% |
| `mockwebserver/src/main/kotlin/mockwebserver3` | 9 | 972.44 | 13.58% | 0.0% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal` | 12 | 948.58 | 18.74% | 61.5% |
| `samples/guide/src/main/java/okhttp3/recipes` | 30 | 881.34 | 13.01% | 59.35% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache` | 5 | 759.16 | 17.63% | 21.3% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSSLSession.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/ResponseBodyJvmTest.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/ResponseBodyTest.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/PrintEvents.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build-logic/src/main/kotlin/okhttp.publish-conventions.gradle.kts` -> **100.0%** Exposure
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/RecordedRequest.kt` -> **100.0%** Exposure
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/publicsuffix/PublicSuffixDatabase.kt` -> **100.0%** Exposure
- `build-logic/src/main/kotlin/okhttp.jvm-conventions.gradle.kts` -> **99.9999%** Exposure
- `maven-tests/mvnw` -> **99.9998%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **217** Orphaned Functions | **11** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -> **191** Orphaned Functions | **14** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` -> **154** Orphaned Functions | **0** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlTest.kt` -> **131** Orphaned Functions | **0** Duplicates
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` -> **101** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `okhttp-tls/src/main/kotlin/okhttp3/tls/Certificates.kt` -> **100.0%** Exposure
- `okhttp-tls/src/main/kotlin/okhttp3/tls/HeldCertificate.kt` -> **100.0%** Exposure
- `okhttp-tls/src/test/java/okhttp3/tls/HeldCertificateTest.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/tls/HostnameVerifierTest.kt` -> **100.0%** Exposure
- `samples/guide/src/main/java/okhttp3/recipes/kt/CustomTrust.kt` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6595` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-CacheControlCommon.kt` (KOTLIN) -> Cumulative Risk: **669.49**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.69)
- **Magnitude:** 158.66 | **LOC:** 268 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Documentation (95.6522%), Tech Debt (94.8273%)
- **Heaviest Functions:** `commonParse` (Compute Cores, Impact: 31.1), `commonToString` (Compute Cores, Impact: 17.2), `indexOfElement` (Compute Cores, Impact: 5.7)

### 2. `samples/crawler/src/main/java/okhttp3/sample/Crawler.java` (JAVA) -> Cumulative Risk: **642.23**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.04)
- **Magnitude:** 93.62 | **LOC:** 152 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), State Flux (98.4507%)
- **Heaviest Functions:** `fetch` (Compute Cores, Impact: 20.4), `main` (Compute Cores, Impact: 5.3), `drainQueue` (Defensive Guards, Impact: 4.9)

### 3. `okhttp/src/jvmTest/kotlin/okhttp3/FakeRoutePlanner.kt` (KOTLIN) -> Cumulative Risk: **635.55**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.37)
- **Magnitude:** 111.74 | **LOC:** 217 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9952%), Cognitive Load (97.3816%)
- **Heaviest Functions:** `plan` (I/O & Config Routines, Impact: 7.0), `connectTcp` (I/O & Config Routines, Impact: 5.7), `connectTlsEtc` (I/O & Config Routines, Impact: 4.5)

### 4. `samples/slack/src/main/java/okhttp3/slack/OAuthSessionFactory.java` (JAVA) -> Cumulative Risk: **632.53**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.14)
- **Magnitude:** 79.84 | **LOC:** 127 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9852%), Concurrency (99.9695%), Tech Debt (91.5138%)
- **Heaviest Functions:** `dispatch` (Defensive Guards, Impact: 10.2), `newAuthorizeUrl` (Parameter Forwarders, Impact: 4.5), `start` (Interface Declarations, Impact: 2.4)

### 5. `samples/slack/src/main/java/okhttp3/slack/SlackClient.java` (JAVA) -> Cumulative Risk: **625.85**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.41)
- **Magnitude:** 97.26 | **LOC:** 100 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (100.0%), Concurrency (99.6755%), Verification (80.0%)
- **Heaviest Functions:** `main` (Compute Cores, Impact: 53.6), `requestOauthSession` (Callbacks & Closures, Impact: 7.6), `awaitAccessToken` (Interface Declarations, Impact: 3.1)

### 6. `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-HeadersCommon.kt` (KOTLIN) -> Cumulative Risk: **587.98**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.48)
- **Magnitude:** 117.96 | **LOC:** 212 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9584%), State Flux (97.206%), Verification (80.0%)
- **Heaviest Functions:** `headersCheckValue` (Defensive Guards, Impact: 9.3), `commonValues` (Generic / Templated Code, Impact: 6.2), `commonHeadersGet` (Generic / Templated Code, Impact: 5.7)

### 7. `samples/guide/src/main/java/okhttp3/recipes/kt/WiresharkExample.kt` (KOTLIN) -> Cumulative Risk: **580.77**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.65)
- **Magnitude:** 92.56 | **LOC:** 377 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (96.955%), Verification (80.0%)
- **Heaviest Functions:** `publish` (Compute Cores, Impact: 12.1), `connectionAcquired` (Compute Cores, Impact: 8.2), `launchWireShark` (I/O & Config Routines, Impact: 7.8)

### 8. `samples/slack/src/main/java/okhttp3/slack/RtmSession.java` (JAVA) -> Cumulative Risk: **569.71**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.21)
- **Magnitude:** 43.82 | **LOC:** 76 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (90.6079%), Documentation (86.6667%)
- **Heaviest Functions:** `onClosing` (Annotated Framework Methods, Impact: 4.2), `onOpen` (Annotated Framework Methods, Impact: 3.6), `onMessage` (Annotated Framework Methods, Impact: 3.6)

### 9. `maven-tests/mvnw` (SHELL) -> Cumulative Risk: **568.21**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.90)
- **Magnitude:** 171.2 | **LOC:** 260 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Safety Score (99.2941%)
- **Heaviest Functions:** `__global_context__` (I/O & Config Routines, Impact: 17.1), `set_java_home` (I/O & Config Routines, Impact: 12.8), `Anonymous_Block` (Defensive Guards, Impact: 11.2)

### 10. `samples/guide/src/main/java/okhttp3/recipes/PrintEvents.java` (JAVA) -> Cumulative Risk: **565.71**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.36)
- **Magnitude:** 117.9 | **LOC:** 205 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.0976%)
- **Heaviest Functions:** `run` (Annotated Framework Methods, Impact: 4.5), `connectFailed` (Annotated Framework Methods, Impact: 2.6), `connectEnd` (Annotated Framework Methods, Impact: 2.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 928.14 | **LOC:** 4543 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.0438%), Tech Debt (99.9258%)
**Top Internal Functions/Classes:**
  * `doUpload` **(Compute Cores)** (Impact: 21.3)
  * `testRedirect` **(Compute Cores)** (Impact: 17.6)
  * `writeTo` **(Compute Cores)** (Impact: 10.6)
  * `intercept` **(Defensive Guards)** (Impact: 9.1)
  * `authCallsForHeader` **(Compute Cores)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 435`, `args: 327`, `func_start: 309`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 160`, `planned_debt: 8`, `fragile_debt: 7`, `duplicate_logic: 11`, `unreferenced_by_name: 217`
* *Architecture:* `io: 17`, `api: 4`, `import: 86`
* *Defense:* `safety: 35`, `doc: 29`, `test: 625`, `sync_locks: 3`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` assertk.assertThat, assertk.assertions.contains, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isGreaterThanOrEqualTo, assertk.assertions.isIn, assertk.assertions.isInstanceOf, assertk.assertions.isLessThan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 864.46 | **LOC:** 4983 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (12.1429%), Tech Debt (99.5262%)
**Top Internal Functions/Classes:**
  * `requestBody` **(Type Conversions)** (Impact: 9.1)
  * `serverHalfClosingBeforeResponse` **(Tests & Verification)** (Impact: 5.5)
  * `configureClientAndServerProxies` **(Callbacks & Closures)** (Impact: 5.4)
    * *Intent:* /** Use a proxy to fake IPv6 connectivity, even if localhost doesn't have IPv6. */
  * `noRecoveryFromTlsHandshakeFailureWhenTlsFallbackIsDisabled` **(Tests & Verification)** (Impact: 5.0)
  * `canRetryNormalRequestBody` **(Tests & Verification)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 506`, `args: 307`, `func_start: 272`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 212`, `dead_code: 1`, `fragile_debt: 5`, `duplicate_logic: 14`, `unreferenced_by_name: 191`
* *Architecture:* `io: 5`, `import: 124`
* *Defense:* `safety: 18`, `doc: 30`, `test: 807`, `sync_locks: 8`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` assertk.all, assertk.assertThat, assertk.assertions.contains, assertk.assertions.containsExactly, assertk.assertions.doesNotContain, assertk.assertions.hasMessage, assertk.assertions.hasSize, assertk.assertions.index...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 682.1 | **LOC:** 1817 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.1449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 62.3)
  * `schemeDelimiterOffset` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /** * Returns the index of the ':' in `input` that is after scheme characters. Returns -1 if * `inpu...
  * `toString` **(I/O & Config Routines)** (Impact: 18.9)
  * `push` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* /** Adds a path segment. If the input is ".." or equivalent, this pops a path segment. */
  * `resolvePath` **(Many-Argument Workhorses)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 172`, `args: 85`, `func_start: 84`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 124`
* *Architecture:* `api: 26`, `import: 25`
* *Defense:* `safety: 10`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.798
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.114698
  * `Imports (Out-Degree: 1):` java.net.MalformedURLException, java.net.URI, java.net.URISyntaxException, java.net.URL, okhttp3.HttpUrl.Companion.toHttpUrl, okhttp3.HttpUrl.Companion.toHttpUrlOrNull, okhttp3.internal.canParseAsIpAddress, okhttp3.internal.delimiterOffset...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 562.34 | **LOC:** 1295 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.4394%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readRequest` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* /** @param exchangeIndex the index of this request on this connection.*/
  * `readRequest` **(Compute Cores)** (Impact: 32.3)
  * `handle` **(I/O & Config Routines)** (Impact: 27.1)
  * `writeResponse` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `processOneRequest` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* /** * Reads a request and writes its response. Returns true if further calls should be attempted * o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 191`, `args: 44`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 85`
* *Architecture:* `api: 29`, `import: 66`
* *Defense:* `safety: 21`, `doc: 26`, `sync_locks: 11`, `immutability_locks: 3`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.949
  * `Choke Point (Betweenness):` 0.006948 | `Ripple Effect (Closeness):` 0.079341
  * `Imports (Out-Degree: 19):` java.io.Closeable, java.io.IOException, java.net.InetAddress, java.net.InetSocketAddress, java.net.ProtocolException, java.net.Proxy, java.net.ServerSocket, java.net.Socket...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 557.94 | **LOC:** 1466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `eventListener` **(Interface Declarations)** (Impact: 6.2)
  * `withWriteTimeout` **(State Mutators)** (Impact: 3.5)
  * `call` **(Interface Declarations)** (Impact: 2.9)
  * `webSocketListener` **(Interface Declarations)** (Impact: 2.9)
  * `connectFailed` **(Parameter Forwarders)** (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 257`, `args: 171`, `func_start: 167`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 257`, `planned_debt: 123`, `duplicate_logic: 7`, `unreferenced_by_name: 91`
* *Architecture:* `io: 14`, `import: 69`
* *Defense:* `safety: 4`, `doc: 1`, `test: 69`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` java.io.File, java.io.IOException, java.math.BigInteger, java.net.CookieHandler, java.net.InetAddress, java.net.InetSocketAddress, java.net.Proxy, java.net.ProxySelector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 498.64 | **LOC:** 4261 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (5.7468%), Tech Debt (97.4337%)
**Top Internal Functions/Classes:**
  * `assertCached` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `testRequestMethod` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `requestBodyOrNull` **(Compute Cores)** (Impact: 7.5)
  * `temporaryRedirectCachedWithCachingHeader` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `assertClientSuppliedCondition` **(Many-Argument Workhorses)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 255`, `args: 197`, `func_start: 187`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 39`, `fragile_debt: 1`, `unreferenced_by_name: 154`
* *Architecture:* `io: 1`, `api: 1`, `import: 53`
* *Defense:* `safety: 2`, `doc: 19`, `test: 630`, `sync_locks: 4`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` assertk.assertThat, assertk.assertions.containsExactly, assertk.assertions.isCloseTo, assertk.assertions.isEmpty, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isNotNull, assertk.assertions.isNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 483.3 | **LOC:** 1122 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.7106%), Tech Debt (8.3122%)
**Top Internal Functions/Classes:**
  * `completeEdit` **(Compute Cores)** (Impact: 38.1)
  * `readJournalLine` **(Compute Cores)** (Impact: 23.6)
  * `edit` **(Compute Cores)** (Impact: 21.9)
    * *Intent:* /** Returns an editor for the entry named [key], or null if another edit is in progress. */
  * `removeEntry` **(Compute Cores)** (Impact: 12.1)
  * `readJournal` **(I/O & Config Routines)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 175`, `args: 47`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 68`, `planned_debt: 1`
* *Architecture:* `api: 34`, `import: 26`
* *Defense:* `safety: 17`, `doc: 41`, `test: 3`, `sync_locks: 28`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.117
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.067457
  * `Imports (Out-Degree: 4):` java.io.Closeable, java.io.EOFException, java.io.Flushable, java.io.IOException, okhttp3.internal.cache.DiskLruCache.Editor, okhttp3.internal.closeQuietly, okhttp3.internal.concurrent.Lockable, okhttp3.internal.concurrent.Task...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 438.56 | **LOC:** 1395 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.944%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `protocols` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* * * [Protocol.HTTP_1_0] is not supported in this set. Requests are initiated with `HTTP/1.1`. If * t...
  * `init` **(I/O & Config Routines)** (Impact: 6.2)
  * `sslSocketFactory` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* * Trust managers targeting Android must also define a method that has this signature: * * ```java * ...
  * `sslSocketFactory` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* /** * Sets the socket factory used to secure HTTPS connections. If unset, the system default will * ...
  * `address` **(I/O & Config Routines)** (Impact: 4.1)
    * *Intent:* /** * Creates an [Address] of out of the provided [HttpUrl] * that uses this client’s DNS, TLS, and ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 117`, `args: 85`, `func_start: 83`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 132`
* *Architecture:* `io: 4`, `api: 48`, `import: 31`
* *Defense:* `safety: 24`, `doc: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.068
  * `Choke Point (Betweenness):` 0.018191 | `Ripple Effect (Closeness):` 0.178684
  * `Imports (Out-Degree: 8):` java.net.Proxy, java.net.ProxySelector, java.net.Socket, java.time.Duration, java.util.Random, java.util.concurrent.ExecutorService, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.MILLISECONDS...
  * `Imported By (In-Degree: 115):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Hpack.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 435.62 | **LOC:** 676 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (69.3974%), Tech Debt (56.5036%)
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 84.5)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 77.7)
  * `writeHeaders` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* /** * This does not use "never indexed" semantics for sensitive headers. * * http://tools.ietf.org/h...
  * `insertIntoDynamicTable` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* /** index == -1 when new. */
  * `readInt` **(Compute Cores)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 76`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 55`, `dead_code: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 4`
* *Architecture:* `import: 15`
* *Defense:* `doc: 10`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.IOException, java.util.Arrays, okhttp3.internal.HEADER_LIMIT, okhttp3.internal.and, okhttp3.internal.http2.Header.Companion.RESPONSE_STATUS, okhttp3.internal.http2.Header.Companion.TARGET_AUTHORITY, okhttp3.internal.http2.Header.Companion.TARGET_METHOD, okhttp3.internal.http2.Header.Companion.TARGET_PATH...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Connection.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 424.06 | **LOC:** 1047 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.4906%), Tech Debt (11.2495%)
**Top Internal Functions/Classes:**
  * `newStream` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `headers` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `applyAndAckSettings` **(Many-Argument Workhorses)** (Impact: 16.4)
    * *Intent:* /** * Apply inbound settings and send an acknowledgement to the peer that provided them. * * We need...
  * `writeData` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* /** * Callers of this method are not thread safe, and sometimes on application threads. Most often, ...
  * `ping` **(Many-Argument Workhorses)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *Api Near Db Sink:* 4 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 140`, `args: 57`, `func_start: 53`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`, `planned_debt: 6`
* *Architecture:* `api: 45`, `import: 25`
* *Defense:* `safety: 3`, `doc: 35`, `test: 1`, `immutability_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.514
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.050271
  * `Imports (Out-Degree: 6):` java.io.Closeable, java.io.IOException, java.io.InterruptedIOException, java.util.concurrent.TimeUnit, okhttp3.Headers, okhttp3.internal.EMPTY_BYTE_ARRAY, okhttp3.internal.closeQuietly, okhttp3.internal.concurrent.Lockable...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 417.84 | **LOC:** 2160 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.7027%), Tech Debt (99.8383%)
**Top Internal Functions/Classes:**
  * `createJournalWithHeader` **(Many-Argument Workhorses)** (Impact: 6.5)
  * `fun` **(Tests & Verification)** (Impact: 6.2)
  * `trimToSizeWithActiveEdit` **(Tests & Verification)** (Impact: 6.0)
    * *Intent:* /** * We had a long-lived bug where [DiskLruCache.trimToSize] could infinite loop if entries * being...
  * `fun` **(Tests & Verification)** (Impact: 6.0)
  * `fun` **(Tests & Verification)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 179`, `args: 159`, `func_start: 141`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 63`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 101`
* *Architecture:* `io: 2`, `import: 31`
* *Defense:* `safety: 6`, `doc: 10`, `test: 450`, `sync_locks: 2`, `cleanup: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` app.cash.burst.Burst, assertk.assertThat, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isNull, assertk.assertions.isSameInstanceAs, assertk.assertions.isTrue, assertk.fail...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 365.64 | **LOC:** 2538 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (97.1461%), Tech Debt (66.5045%)
**Top Internal Functions/Classes:**
  * `assertBytesReadWritten` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `assertSuccessfulEventOrder` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `aggregateEventListenerIsComplete` **(Tests & Verification)** (Impact: 6.5)
    * *Intent:* /** Reflectively call every event function to confirm it is correctly forwarded. */
  * `requestBodyMultipleFailuresReportedOnlyOnce` **(Interface Declarations)** (Impact: 5.8)
  * `timeToFirstByte` **(Interface Declarations)** (Impact: 5.8)
    * *Intent:* /** * Test to confirm that events are reported at the time they occur and no earlier and no later. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 630`, `args: 117`, `func_start: 103`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 48`, `duplicate_logic: 2`, `unreferenced_by_name: 70`
* *Architecture:* `io: 3`, `import: 89`
* *Defense:* `safety: 4`, `doc: 9`, `test: 247`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` app.cash.burst.Burst, assertk.all, assertk.assertThat, assertk.assertions.contains, assertk.assertions.containsExactly, assertk.assertions.doesNotContain, assertk.assertions.isEmpty, assertk.assertions.isEqualTo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/HttpOverHttp2Test.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 360.52 | **LOC:** 2169 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (9.0684%), Tech Debt (99.492%)
**Top Internal Functions/Classes:**
  * `responseHeadersAfterGoaway` **(Tests & Verification)** (Impact: 6.8)
  * `waitForConnectionShutdown` **(Annotated Framework Methods)** (Impact: 6.3)
  * `countFrames` **(Generic / Templated Code)** (Impact: 5.8)
  * `concurrentHttp2ConnectionsDeduplicated` **(Tests & Verification)** (Impact: 5.8)
    * *Intent:* /** * We don't know if the connection will support HTTP/2 until after we've connected. When multiple...
  * `firstFrame` **(Generic / Templated Code)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 215`, `args: 115`, `func_start: 97`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 65`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 11`, `unreferenced_by_name: 64`
* *Architecture:* `io: 2`, `api: 1`, `import: 83`
* *Defense:* `safety: 9`, `doc: 13`, `test: 294`, `sync_locks: 3`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` app.cash.burst.Burst, app.cash.burst.burstValues, assertk.assertThat, assertk.assertions.contains, assertk.assertions.hasMessage, assertk.assertions.isCloseTo, assertk.assertions.isEqualTo, assertk.assertions.isFalse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cookie.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 358.76 | **LOC:** 735 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.7229%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `parseExpires` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /** Parse a date as specified in RFC 6265, section 5.1.1. */
  * `dateCharacterOffset` **(Many-Argument Workhorses)** (Impact: 21.1)
    * *Intent:* /** * Returns the index of the next date character in `input`, or if `invert` the index * of the nex...
  * `equals` **(Defensive Guards)** (Impact: 16.2)
  * `toString` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* /** * @param forObsoleteRfc2965 true to include a leading `.` on the domain pattern. This is * neces...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 89`, `args: 37`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`
* *Architecture:* `api: 8`, `import: 16`
* *Defense:* `safety: 21`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.566
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.081391
  * `Imports (Out-Degree: 1):` java.util.Calendar, java.util.Date, java.util.GregorianCalendar, java.util.Locale, java.util.regex.Pattern, okhttp3.internal.UTC, okhttp3.internal.canParseAsIpAddress, okhttp3.internal.delimiterOffset...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Stream.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 310.2 | **LOC:** 743 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.921%), Tech Debt (9.5136%)
**Top Internal Functions/Classes:**
  * `read` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `receive` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* /** * Accept bytes on the connection's reader thread. This function avoids holding locks while it * ...
  * `receiveHeaders` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* /** Accept headers from the network and store them until the client calls [takeHeaders]. */
  * `takeHeaders` **(Defensive Guards)** (Impact: 12.4)
    * *Intent:* /** * Removes and returns the stream's received response headers, blocking if necessary until header...
  * `emitFrame` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Emit a single data frame to the connection. The frame's size be limited by this stream's * wri...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 101`, `args: 35`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 34`, `planned_debt: 2`
* *Architecture:* `api: 24`, `import: 20`
* *Defense:* `safety: 10`, `doc: 34`, `test: 10`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.514
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.050271
  * `Imports (Out-Degree: 3):` java.io.EOFException, java.io.IOException, java.io.InterruptedIOException, java.net.SocketTimeoutException, java.util.ArrayDeque, okhttp3.Headers, okhttp3.internal.concurrent.Lockable, okhttp3.internal.concurrent.assertLockNotHeld...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 303.12 | **LOC:** 516 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.3985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 102.4)
  * `init` **(I/O & Config Routines)** (Impact: 25.6)
  * `getPlatformSystemProperty` **(Defensive Guards)** (Impact: 8.8)
  * `setupPlatform` **(I/O & Config Routines)** (Impact: 5.8)
  * `interceptTestMethod` **(Generic / Templated Code)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 120`, `args: 70`, `func_start: 70`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 43`, `import: 34`
* *Defense:* `safety: 4`, `doc: 2`, `test: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.106
  * `Choke Point (Betweenness):` 0.002729 | `Ripple Effect (Closeness):` 0.08321
  * `Imports (Out-Degree: 7):` android.os.Build, com.amazon.corretto.crypto.provider.AmazonCorrettoCryptoProvider, com.amazon.corretto.crypto.provider.SelfTestStatus, java.lang.reflect.Method, java.security.Security, okhttp3.TestUtil, okhttp3.internal.platform.ConscryptPlatform, okhttp3.internal.platform.Jdk8WithJettyBootPlatform...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 294.64 | **LOC:** 627 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (37.5188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `messageDone` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /** * Releases resources held with the request or response of [exchange]. This should be called when...
  * `enterNetworkInterceptorExchange` **(Many-Argument Workhorses)** (Impact: 13.9)
    * *Intent:* /** * Prepare for a potential trip through all of this call's network interceptors. This prepares to...
  * `callDone` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* /** * Complete this call. This should be called once these properties are all false: * [requestBodyO...
  * `noMoreExchanges` **(Compute Cores)** (Impact: 9.2)
  * `run` **(Defensive Guards)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 106`, `args: 35`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 37`
* *Architecture:* `io: 2`, `api: 24`, `import: 36`
* *Defense:* `safety: 21`, `doc: 17`, `test: 5`, `sync_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.556
  * `Choke Point (Betweenness):` 0.016467 | `Ripple Effect (Closeness):` 0.138345
  * `Imports (Out-Degree: 14):` java.io.IOException, java.io.InterruptedIOException, java.lang.ref.WeakReference, java.net.Socket, java.util.concurrent.CopyOnWriteArrayList, java.util.concurrent.ExecutorService, java.util.concurrent.RejectedExecutionException, java.util.concurrent.TimeUnit.MILLISECONDS...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 292.66 | **LOC:** 576 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1333%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toString` **(I/O & Config Routines)** (Impact: 6.0)
  * `chunkedBody` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* /** * Sets the response body to [body], chunked every [maxChunkSize] bytes. */
  * `throttleBody` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* /** * Throttles the request reader and response writer to sleep for the given period after each * se...
  * `constructor` **(State Mutators)** (Impact: 2.4)
  * `constructor` **(State Mutators)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 54`, `args: 43`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `api: 92`, `import: 10`
* *Defense:* `safety: 3`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.001
  * `Choke Point (Betweenness):` 0.00032 | `Ripple Effect (Closeness):` 0.07578
  * `Imports (Out-Degree: 4):` java.util.concurrent.TimeUnit, mockwebserver3.SocketEffect.CloseStream, mockwebserver3.internal.toMockResponseBody, okhttp3.Headers, okhttp3.Headers.Companion.headersOf, okhttp3.WebSocketListener, okhttp3.internal.addHeaderLenient, okhttp3.internal.http2.ErrorCode...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 286.3 | **LOC:** 703 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.7041%), Tech Debt (8.7186%)
**Top Internal Functions/Classes:**
  * `writeOneFrame` **(I/O & Config Routines)** (Impact: 19.3)
    * *Intent:* /** * Attempts to remove a single frame from a queue and send it. This prefers to write urgent pongs...
  * `failWebSocket` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `checkUpgradeSuccess` **(Defensive Guards)** (Impact: 10.1)
  * `close` **(Many-Argument Workhorses)** (Impact: 9.2)
  * `finishReader` **(I/O & Config Routines)** (Impact: 8.7)
    * *Intent:* /** * Clean up and publish necessary close events when the reader is done. Invoked only by the reade...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 122`, `args: 32`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 47`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 15`, `import: 36`
* *Defense:* `safety: 11`, `doc: 30`, `test: 1`, `sync_locks: 17`, `immutability_locks: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.875
  * `Choke Point (Betweenness):` 0.005923 | `Ripple Effect (Closeness):` 0.135968
  * `Imports (Out-Degree: 14):` java.io.IOException, java.net.ProtocolException, java.net.SocketTimeoutException, java.util.ArrayDeque, java.util.Random, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.MILLISECONDS, okhttp3.Call...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 276.54 | **LOC:** 2169 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3522%), Tech Debt (99.9721%)
**Top Internal Functions/Classes:**
  * `assertInvalid` **(Compute Cores)** (Impact: 7.8)
  * `usernameCharacters` **(Tests & Verification)** (Impact: 3.3)
  * `passwordCharacters` **(Tests & Verification)** (Impact: 3.3)
  * `pathCharacters` **(Tests & Verification)** (Impact: 2.9)
  * `hostnameInPunycodeNfcAndNfd` **(Tests & Verification)** (Impact: 2.6)
    * *Intent:* /** * UTS 46 Validity Criteria: Decoded punycode must be NFC. * * https://www.unicode.org/reports/tr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 161`, `args: 138`, `func_start: 138`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 8`, `planned_debt: 7`, `unreferenced_by_name: 131`
* *Architecture:* `import: 13`
* *Defense:* `doc: 9`, `test: 691`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assertk.assertThat, assertk.assertions.containsExactly, assertk.assertions.containsExactlyInAnyOrder, assertk.assertions.hasMessage, assertk.assertions.isEqualTo, assertk.assertions.isNull, kotlin.test.Ignore, kotlin.test.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cache.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 276.12 | **LOC:** 838 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (43.2496%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* * * The file is newline separated. The first two lines are the URL and the request method. Next * is...
  * `writeTo` **(Compute Cores)** (Impact: 9.2)
  * `put` **(Compute Cores)** (Impact: 8.7)
  * `varyHeaders` **(Compute Cores)** (Impact: 7.7)
    * *Intent:* /** * Returns the subset of the headers in [requestHeaders] that impact the content of the * respons...
  * `varyFields` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* /** * Returns the names of the request headers that need to be checked for equality when caching. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 153`, `args: 50`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`
* *Architecture:* `io: 4`, `api: 16`, `import: 35`
* *Defense:* `safety: 10`, `doc: 16`, `sync_locks: 9`, `immutability_locks: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.699
  * `Choke Point (Betweenness):` 0.002289 | `Ripple Effect (Closeness):` 0.082639
  * `Imports (Out-Degree: 8):` java.io.Closeable, java.io.File, java.io.Flushable, java.io.IOException, java.security.cert.Certificate, java.security.cert.CertificateEncodingException, java.security.cert.CertificateException, java.security.cert.CertificateFactory...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 255.14 | **LOC:** 371 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.8042%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 97.0)
  * `intercept` **(Compute Cores)** (Impact: 73.4)
  * `redactUrl` **(Type Conversions)** (Impact: 9.3)
  * `logHeader` **(Compute Cores)** (Impact: 5.5)
  * `bodyHasUnknownEncoding` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 46`, `args: 14`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `io: 2`, `api: 7`, `import: 16`
* *Defense:* `safety: 2`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.488
  * `Choke Point (Betweenness):` 0.000287 | `Ripple Effect (Closeness):` 0.010566
  * `Imports (Out-Degree: 7):` java.io.IOException, java.nio.charset.Charset, java.util.TreeSet, java.util.concurrent.TimeUnit, okhttp3.Headers, okhttp3.HttpUrl, okhttp3.Interceptor, okhttp3.OkHttpClient...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 247.34 | **LOC:** 606 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.3275%), Tech Debt (37.6725%)
**Top Internal Functions/Classes:**
  * `readSettings` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `nextFrame` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `readHeaders` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `readData` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `readGoAway` **(Many-Argument Workhorses)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 102`, `args: 31`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `planned_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 34`
* *Defense:* `safety: 3`, `doc: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.Closeable, java.io.EOFException, java.io.IOException, java.util.logging.Level.FINE, java.util.logging.Logger, okhttp3.internal.and, okhttp3.internal.format, okhttp3.internal.http2.Http2.CONNECTION_PREFACE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/Http2ConnectionTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 240.88 | **LOC:** 2079 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.348%), Tech Debt (80.7223%)
**Top Internal Functions/Classes:**
  * `readSendsWindowUpdate` **(Tests & Verification)** (Impact: 6.5)
  * `readSendsWindowUpdateHttp2` **(Tests & Verification)** (Impact: 6.4)
  * `sendGoAway` **(Tests & Verification)** (Impact: 3.5)
  * `blockedStreamDoesntStarveNewStream` **(Tests & Verification)** (Impact: 3.5)
  * `discardedDataFramesAreCounted` **(Tests & Verification)** (Impact: 3.3)
    * *Intent:* /** * Confirm that we account for discarded data frames. It's possible that data frames are in-fligh...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 134`, `args: 92`, `func_start: 81`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 32`, `unreferenced_by_name: 64`
* *Architecture:* `import: 39`
* *Defense:* `safety: 2`, `doc: 11`, `test: 385`, `sync_locks: 7`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` assertk.assertThat, assertk.assertions.contains, assertk.assertions.hasSize, assertk.assertions.isCloseTo, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isGreaterThan, assertk.assertions.isLessThan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 238.88 | **LOC:** 874 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (7.9394%), Tech Debt (99.4063%)
**Top Internal Functions/Classes:**
  * `testOverrideBadImplementation` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* /** * Test that if we set a bad implementation on the OkHttpClient directly, that we can avoid the f...
  * `overrideBadImplementation` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `testOverrideInApplicationInterceptor` **(Tests & Verification)** (Impact: 8.1)
    * *Intent:* /** * Test that we can override in a Application Interceptor, purely by seeing that the chain report...
  * `secureConnectEnd` **(Compute Cores)** (Impact: 3.9)
  * `writeTo` **(Interface Declarations)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 194`, `args: 116`, `func_start: 104`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`, `planned_debt: 11`, `duplicate_logic: 6`, `unreferenced_by_name: 14`
* *Architecture:* `io: 41`, `import: 46`
* *Defense:* `safety: 3`, `doc: 3`, `test: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` app.cash.burst.Burst, app.cash.burst.burstValues, assertk.assertFailure, assertk.assertThat, assertk.assertions.hasMessage, assertk.assertions.isFailure, assertk.assertions.isFalse, assertk.assertions.isNotSameInstanceAs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` -> Churn: **84.43%** | Cog Load: 5.7468% | Debt: 97.4337%
- `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -> Churn: **60.91%** | Cog Load: 12.1429% | Debt: 99.5262%
- `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` -> Churn: **55.93%** | Cog Load: 0.0% | Debt: 100.0%
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/http/HttpUpgradesTest.kt` -> Churn: **52.6%** | Cog Load: 0.0% | Debt: 58.2988%
- `build-logic/src/main/kotlin/okhttp.publish-conventions.gradle.kts` -> Churn: **51.8%** | Cog Load: 64.296% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 928.14
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 682.1
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 562.34
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 483.3
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Connection.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 424.06

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 1.819** (Bridge: 0.0182 * Flux: 99.986%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` -> **Severity: 1.641** (Bridge: 0.0165 * Flux: 99.6816%)
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **Severity: 0.693** (Bridge: 0.0069 * Flux: 99.6863%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` -> **Severity: 0.592** (Bridge: 0.0059 * Flux: 99.8856%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt` -> **Severity: 0.349** (Bridge: 0.0035 * Flux: 99.1589%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 14.682** (Embedded: 0.1787 * Error Risk: 82.167%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/publicsuffix/PublicSuffixDatabase.kt` -> **Severity: 12.048** (Embedded: 0.1333 * Error Risk: 90.3861%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Request.kt` -> **Severity: 11.613** (Embedded: 0.1809 * Error Risk: 64.1912%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/concurrent/TaskRunner.kt` -> **Severity: 11.455** (Embedded: 0.1494 * Error Risk: 76.6904%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` -> **Severity: 11.146** (Embedded: 0.136 * Error Risk: 81.9736%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/Exchange.kt` -> **Severity: 1478.983** (Blast Radius: 16.299 * Doc Risk: 90.7407%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 1405.571** (Blast Radius: 24.068 * Doc Risk: 58.4%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/platform/Platform.kt` -> **Severity: 1285.566** (Blast Radius: 21.12 * Doc Risk: 60.8696%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt` -> **Severity: 1255.623** (Blast Radius: 17.788 * Doc Risk: 70.5882%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Request.kt` -> **Severity: 1164.681** (Blast Radius: 25.623 * Doc Risk: 45.4545%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
