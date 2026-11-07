# ARCHITECTURAL_BRIEF: okhttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/square/okhttp` |
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
- **Scope:** 721 analyzed artifact(s), 102289 LOC.
- **Load-bearing artifact:** `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -- 135 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` -- pulls in 124 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` at magnitude 926.74 (structural weight, not risk).
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
| Total Artifacts | 794 |
| Analyzed Artifacts (Scanned) | 721 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 73 |
| Total LOC | 102289 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 90.8% |
| Dominant Lang | KOTLIN |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4952 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1264 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5515 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 60 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| KOTLIN | 566 | 97909 | 78.5% |
| JAVA | 70 | 2834 | 9.7% |
| MARKDOWN | 35 | 0 | 4.9% |
| PLAINTEXT | 17 | 0 | 2.4% |
| XML | 11 | 0 | 1.5% |
| JSON | 8 | 449 | 1.1% |
| SHELL | 7 | 349 | 1.0% |
| YAML | 5 | 544 | 0.7% |
| BATCH | 2 | 204 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 721 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 17%, Declarative / Non-Code 17%, Data / Markup / Trivial 16%, Encapsulated Accessors Files 10%, Parameter Forwarders Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 669 | 92.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 52 | 7.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 73*

**Composition by Extension & Reason:**
- `.md`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.api`: 15x Excluded (Unsupported Extension: '.api')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 3x Excluded (Unsupported Extension: '.pro'), 1x Unsupported Format (.pro)
- `.kt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 1x Excluded (Machine-Generated Source Code Signature: 4 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.config`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.list`: 2x Unsupported Format (.list)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.jar`: 1x Excluded (Explicitly Denied Extension: '.jar')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.4 | 11.3 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.5 | 36.0 | 49.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 32.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.4 | 7.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.1 | 9.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.5 | 88.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 985 | 230 | 4 | `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlTest.kt` |
| cleanup | 630 | 138 | 2 | `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` |
| guards | 5099 | 519 | 19 | `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` |
| danger | 3706 | 424 | 13 | `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/HpackTest.kt` |
| concurrency | 416 | 92 | 1 | `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` |
| connectivity | 2015 | 305 | 8 | `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` |
| io | 607 | 144 | 2 | `maven-tests/mvnw` |
| crypto | 0 | 0 | 0 | - |
| ipc | 17 | 4 | 0 | `maven-tests/mvnw` |
| time | 41 | 11 | 0 | `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` |
| serialization | 16 | 9 | 0 | `fuzzing/fuzzingserver-test.sh` |
| regex | 291 | 39 | 0 | `okhttp-logging-interceptor/src/test/java/okhttp3/logging/HttpLoggingInterceptorTest.kt` |
| events | 175 | 36 | 0 | `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` |
| tests | 11006 | 220 | 27 | `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` |
| docs | 1856 | 365 | 7 | `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` |
| debt | 666 | 162 | 2 | `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` |
| mutation | 20237 | 559 | 74 | `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` |
| dead_code | 3499 | 365 | 11 | `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` |
| credential | 228 | 18 | 0 | `samples/guide/src/main/java/okhttp3/recipes/CustomTrust.java` |
| threat | 2 | 2 | 0 | `okhttp/src/jvmTest/resources/web-platform-test-toascii.json` |
| ml_ai | 229 | 47 | 0 | `okhttp/src/jvmTest/kotlin/okhttp3/internal/concurrent/TaskRunnerTest.kt` |
| ui | 9 | 4 | 0 | `mockwebserver-junit5/src/main/kotlin/mockwebserver3/junit5/internal/StartStopExtension.kt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `maven-tests/mvnw` (Hits: 88)
- `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt` (Hits: 41)
- `gradlew` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **OkHttpClient.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt`) — 135 inbound connections
2. **Request.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Request.kt`) — 126 inbound connections
3. **Response.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt`) — 90 inbound connections
4. **HttpUrl.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt`) — 82 inbound connections
5. **Headers.kt** (`okhttp/src/commonJvmAndroid/kotlin/okhttp3/Headers.kt`) — 74 inbound connections

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
- `constructor` **(Stateful Encapsulated Methods)** (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **94.1** | LOC: 327
- `constructor` **(Stateful Encapsulated Methods)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Hpack.kt`) -> Impact: **84.5** | LOC: 289
- `constructor` **(Stateful Encapsulated Methods)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Hpack.kt`) -> Impact: **77.7** | LOC: 233
- `intercept` **(Compute Cores)** (@ `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt`) -> Impact: **70.6** | LOC: 167
- `parse` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt`) -> Impact: **60.6** | LOC: 172
- `parse` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cookie.kt`) -> Impact: **57.0** | LOC: 141
- `messageDone` **(Many-Argument Workhorses)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt`) -> Impact: **55.0** | LOC: 42
  * *Intent:* /** * Releases resources held with the request or response of [exchange]. This should be called when * the request completes normally or when it fails...
- `intercept` **(Compute Cores)** (@ `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http/CallServerInterceptor.kt`) -> Impact: **53.4** | LOC: 162

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `okhttp/src/jvmTest/kotlin/okhttp3` | 85 | 7535.1 | 10.79% | 81.09% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3` | 40 | 3788.0 | 21.07% | 4.57% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2` | 15 | 1929.4 | 14.89% | 16.88% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection` | 21 | 1353.42 | 12.58% | 24.59% |
| `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2` | 9 | 1138.52 | 13.31% | 76.8% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal` | 12 | 982.08 | 18.32% | 58.86% |
| `okhttp-testing-support/src/main/kotlin/okhttp3` | 30 | 977.28 | 10.53% | 43.54% |
| `mockwebserver/src/main/kotlin/mockwebserver3` | 9 | 971.74 | 13.57% | 0.0% |
| `samples/guide/src/main/java/okhttp3/recipes` | 30 | 784.74 | 8.89% | 59.35% |
| `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache` | 5 | 756.06 | 17.56% | 21.03% |

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
- `gradlew` -> **100.0%** Exposure
- `build-logic/src/main/kotlin/okhttp.jvm-conventions.gradle.kts` -> **99.9999%** Exposure
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
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/RecordingAuthenticator.kt` -> **100.0%** Exposure
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/tls/HostnameVerifierTest.kt` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6603` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.492)
- **Top Global Matches:** file_cluster_12: 8.492, file_cluster_13: 9.089, file_cluster_16: 9.534
- **Magnitude:** 926.74 | **LOC:** 4543 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **86**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (45.1%), Mutation Surface (formerly State Flux) (39.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.7%)
- **Documentation Coverage:** 90.9677% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doUpload` **(Stateful Encapsulated Methods)** (Impact: 21.3)
  * `testRedirect` **(Stateful Encapsulated Methods)** (Impact: 17.6)
  * `writeTo` **(Compute Cores)** (Impact: 10.6)
  * `intercept` **(Defensive Guards)** (Impact: 9.1)
  * `authCallsForHeader` **(Stateful Encapsulated Methods)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 435`, `args: 327`, `func_start: 309`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 160`, `planned_debt: 8`, `fragile_debt: 7`, `duplicate_logic: 11`, `unreferenced_by_name: 217`
* *Architecture:* `io: 17`, `api: 4`, `import: 86`
* *Defense:* `safety: 35`, `doc: 29`, `test: 625`, `sync_locks: 3`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` assertk.assertThat, assertk.assertions.contains, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isGreaterThanOrEqualTo, assertk.assertions.isIn, assertk.assertions.isInstanceOf, assertk.assertions.isLessThan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/CallTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.914)
- **Top Global Matches:** file_cluster_13: 7.914, file_cluster_12: 8.219, file_cluster_15: 8.668
- **Magnitude:** 847.56 | **LOC:** 4983 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **124**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Guard Balance (formerly Safety Score) (44.1%), Mutation Surface (formerly State Flux) (43.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.5%)
- **Documentation Coverage:** 89.9687% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `requestBody` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `serverHalfClosingBeforeResponse` **(I/O & Config Routines)** (Impact: 5.5)
  * `configureClientAndServerProxies` **(Stateful Encapsulated Methods)** (Impact: 5.4)
    * *Intent:* /** Use a proxy to fake IPv6 connectivity, even if localhost doesn't have IPv6. */
  * `noRecoveryFromTlsHandshakeFailureWhenTlsFallbackIsDisabled` **(I/O & Config Routines)** (Impact: 5.0)
  * `recoverWhenRetryOnConnectionFailureIsTrue` **(Annotated & Test Methods)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 506`, `args: 307`, `func_start: 272`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 212`, `fragile_debt: 5`, `duplicate_logic: 14`, `unreferenced_by_name: 191`
* *Architecture:* `io: 5`, `import: 124`
* *Defense:* `safety: 18`, `doc: 30`, `test: 807`, `sync_locks: 8`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` assertk.all, assertk.assertThat, assertk.assertions.contains, assertk.assertions.containsExactly, assertk.assertions.doesNotContain, assertk.assertions.hasMessage, assertk.assertions.hasSize, assertk.assertions.index...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.101)
- **Top Global Matches:** file_cluster_12: 7.101, file_cluster_5: 8.837, file_cluster_16: 9.462
- **Magnitude:** 683.4 | **LOC:** 1817 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **82** in-repo importer(s); it depends on **25**; blast radius 25.149; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.1%), Complexity Load (formerly Cognitive Load) (48.0%), Connectivity (formerly Api Exposure) (25.6%)
- **Documentation Coverage:** 59.4203% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 60.6)
  * `schemeDelimiterOffset` **(Stateful Encapsulated Methods)** (Impact: 19.2)
    * *Intent:* /** * Returns the index of the ':' in `input` that is after scheme characters. Returns -1 if * `inpu...
  * `toString` **(I/O & Config Routines)** (Impact: 17.4)
  * `push` **(Stateful Encapsulated Methods)** (Impact: 16.2)
    * *Intent:* /** Adds a path segment. If the input is ".." or equivalent, this pops a path segment. */
  * `resolvePath` **(Stateful Encapsulated Methods)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 172`, `args: 87`, `func_start: 86`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 124`
* *Architecture:* `api: 26`, `import: 25`
* *Defense:* `safety: 10`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.149
  * `Choke Point (Betweenness):` 0.00916 | `Ripple Effect (Closeness):` 0.237186
  * `Imports (Out-Degree: 7):` java.net.MalformedURLException, java.net.URI, java.net.URISyntaxException, java.net.URL, okhttp3.HttpUrl.Companion.toHttpUrl, okhttp3.HttpUrl.Companion.toHttpUrlOrNull, okhttp3.internal.canParseAsIpAddress, okhttp3.internal.delimiterOffset...
  * `Imported By (In-Degree: 82):` (Excluded from Brief to save tokens)

### `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.272)
- **Top Global Matches:** file_cluster_4: 6.272, file_cluster_12: 10.012, file_cluster_16: 10.969
- **Magnitude:** 561.34 | **LOC:** 1295 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **63** in-repo importer(s); it depends on **66**; blast radius 7.092; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (56.4%), Connectivity (formerly Api Exposure) (24.7%)
- **Documentation Coverage:** 56.9767% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readRequest` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `readRequest` **(Compute Cores)** (Impact: 32.3)
  * `handle` **(I/O & Config Routines)** (Impact: 27.1)
  * `writeResponse` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `processOneRequest` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* /** * Reads a request and writes its response. Returns true if further calls should be attempted * o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 191`, `args: 44`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 85`
* *Architecture:* `api: 29`, `import: 66`
* *Defense:* `safety: 21`, `doc: 26`, `sync_locks: 11`, `immutability_locks: 3`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.092
  * `Choke Point (Betweenness):` 0.012504 | `Ripple Effect (Closeness):` 0.096406
  * `Imports (Out-Degree: 25):` java.io.Closeable, java.io.IOException, java.net.InetAddress, java.net.InetSocketAddress, java.net.ProtocolException, java.net.Proxy, java.net.ServerSocket, java.net.Socket...
  * `Imported By (In-Degree: 63):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.435)
- **Top Global Matches:** file_cluster_0: 7.435, file_cluster_13: 7.488, file_cluster_11: 7.858
- **Magnitude:** 557.94 | **LOC:** 1466 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **69**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (57.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eventListener` **(Interface Declarations)** (Impact: 6.2)
  * `withWriteTimeout` **(Compute Cores)** (Impact: 3.5)
  * `call` **(Generic / Templated Code)** (Impact: 2.9)
  * `webSocketListener` **(Annotated & Test Methods)** (Impact: 2.9)
  * `connectFailed` **(Parameter Forwarders)** (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 257`, `args: 171`, `func_start: 167`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 257`, `planned_debt: 123`, `duplicate_logic: 7`, `unreferenced_by_name: 91`
* *Architecture:* `io: 14`, `import: 69`
* *Defense:* `safety: 4`, `doc: 1`, `test: 69`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` java.io.File, java.io.IOException, java.math.BigInteger, java.net.CookieHandler, java.net.InetAddress, java.net.InetSocketAddress, java.net.Proxy, java.net.ProxySelector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.886)
- **Top Global Matches:** file_cluster_13: 7.886, file_cluster_12: 8.317, file_cluster_16: 8.573
- **Magnitude:** 493.14 | **LOC:** 4261 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.3%), Guard Balance (formerly Safety Score) (43.2%), Mutation Surface (formerly State Flux) (12.2%)
- **Documentation Coverage:** 89.8396% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertCached` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `testRequestMethod` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `requestBodyOrNull` **(Stateful Encapsulated Methods)** (Impact: 7.5)
  * `temporaryRedirectCachedWithCachingHeader` **(Stateful Encapsulated Methods)** (Impact: 3.8)
  * `assertClientSuppliedCondition` **(Stateful Encapsulated Methods)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 255`, `args: 197`, `func_start: 187`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 39`, `fragile_debt: 1`, `unreferenced_by_name: 154`
* *Architecture:* `io: 1`, `api: 1`, `import: 53`
* *Defense:* `safety: 2`, `doc: 19`, `test: 630`, `sync_locks: 4`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` assertk.assertThat, assertk.assertions.containsExactly, assertk.assertions.isCloseTo, assertk.assertions.isEmpty, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isNotNull, assertk.assertions.isNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.826)
- **Top Global Matches:** file_cluster_12: 7.826, file_cluster_16: 8.286, file_cluster_15: 9.203
- **Magnitude:** 481.6 | **LOC:** 1122 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.917; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.9%), Guard Balance (formerly Safety Score) (59.5%), Complexity Load (formerly Cognitive Load) (33.6%), Connectivity (formerly Api Exposure) (18.3%)
- **Documentation Coverage:** 36.0465% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `completeEdit` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `readJournalLine` **(Stateful Encapsulated Methods)** (Impact: 23.6)
  * `edit` **(Compute Cores)** (Impact: 21.9)
    * *Intent:* /** Returns an editor for the entry named [key], or null if another edit is in progress. */
  * `removeEntry` **(Stateful Encapsulated Methods)** (Impact: 12.1)
  * `readJournal` **(I/O & Config Routines)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 175`, `args: 47`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 68`, `planned_debt: 1`
* *Architecture:* `api: 34`, `import: 26`
* *Defense:* `safety: 17`, `doc: 41`, `test: 3`, `sync_locks: 28`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.917
  * `Choke Point (Betweenness):` 0.000918 | `Ripple Effect (Closeness):` 0.105609
  * `Imports (Out-Degree: 8):` java.io.Closeable, java.io.EOFException, java.io.Flushable, java.io.IOException, okhttp3.internal.cache.DiskLruCache.Editor, okhttp3.internal.closeQuietly, okhttp3.internal.concurrent.Lockable, okhttp3.internal.concurrent.Task...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.034)
- **Top Global Matches:** file_cluster_12: 7.034, file_cluster_5: 7.939, file_cluster_13: 9.175
- **Magnitude:** 438.56 | **LOC:** 1395 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **135** in-repo importer(s); it depends on **31**; blast radius 19.476; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (46.9%), Connectivity (formerly Api Exposure) (46.5%)
- **Documentation Coverage:** 58.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `protocols` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* * * [Protocol.HTTP_1_0] is not supported in this set. Requests are initiated with `HTTP/1.1`. If * t...
  * `init` **(I/O & Config Routines)** (Impact: 6.2)
  * `sslSocketFactory` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* * Trust managers targeting Android must also define a method that has this signature: * * ```java * ...
  * `sslSocketFactory` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* /** * Sets the socket factory used to secure HTTPS connections. If unset, the system default will * ...
  * `address` **(Compute Cores)** (Impact: 4.1)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.476
  * `Choke Point (Betweenness):` 0.045163 | `Ripple Effect (Closeness):` 0.242071
  * `Imports (Out-Degree: 12):` java.net.Proxy, java.net.ProxySelector, java.net.Socket, java.time.Duration, java.util.Random, java.util.concurrent.ExecutorService, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.MILLISECONDS...
  * `Imported By (In-Degree: 135):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Hpack.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.156)
- **Top Global Matches:** file_cluster_4: 7.156, file_cluster_6: 10.633, file_cluster_12: 11.679
- **Magnitude:** 435.62 | **LOC:** 676 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **15**; blast radius 1.521; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Complexity Load (formerly Cognitive Load) (68.6%), Guard Balance (formerly Safety Score) (62.1%), Debt Markers (formerly Tech Debt) (55.3%)
- **Documentation Coverage:** 83.8235% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 84.5)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 77.7)
  * `writeHeaders` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* /** * This does not use "never indexed" semantics for sensitive headers. * * http://tools.ietf.org/h...
  * `insertIntoDynamicTable` **(Stateful Encapsulated Methods)** (Impact: 12.3)
    * *Intent:* /** index == -1 when new. */
  * `readInt` **(Compute Cores)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 76`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 55`, `duplicate_logic: 4`, `unreferenced_by_name: 4`
* *Architecture:* `import: 15`
* *Defense:* `doc: 10`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.521
  * `Choke Point (Betweenness):` 0.001564 | `Ripple Effect (Closeness):` 0.087402
  * `Imports (Out-Degree: 6):` java.io.IOException, java.util.Arrays, okhttp3.internal.HEADER_LIMIT, okhttp3.internal.and, okhttp3.internal.http2.Header.Companion.RESPONSE_STATUS, okhttp3.internal.http2.Header.Companion.TARGET_AUTHORITY, okhttp3.internal.http2.Header.Companion.TARGET_METHOD, okhttp3.internal.http2.Header.Companion.TARGET_PATH...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Connection.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.035)
- **Top Global Matches:** file_cluster_16: 7.035, file_cluster_12: 7.492, file_cluster_15: 7.588
- **Magnitude:** 421.76 | **LOC:** 1047 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **25**; blast radius 1.214; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.9%), Guard Balance (formerly Safety Score) (57.6%), Complexity Load (formerly Cognitive Load) (29.3%), Connectivity (formerly Api Exposure) (28.0%)
- **Documentation Coverage:** 51.5152% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newStream` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `applyAndAckSettings` **(Many-Argument Workhorses)** (Impact: 16.4)
    * *Intent:* /** * Apply inbound settings and send an acknowledgement to the peer that provided them. * * We need...
  * `headers` **(Many-Argument Workhorses)** (Impact: 15.8)
  * `writeData` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* /** * Callers of this method are not thread safe, and sometimes on application threads. Most often, ...
  * `ping` **(Many-Argument Workhorses)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *Api Near Db Sink:* 4 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 140`, `args: 57`, `func_start: 53`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`, `planned_debt: 6`
* *Architecture:* `api: 45`, `import: 25`
* *Defense:* `safety: 3`, `doc: 35`, `test: 1`, `immutability_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.214
  * `Choke Point (Betweenness):` 0.012992 | `Ripple Effect (Closeness):` 0.129985
  * `Imports (Out-Degree: 15):` java.io.Closeable, java.io.IOException, java.io.InterruptedIOException, java.util.concurrent.TimeUnit, okhttp3.Headers, okhttp3.internal.EMPTY_BYTE_ARRAY, okhttp3.internal.closeQuietly, okhttp3.internal.concurrent.Lockable...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.693)
- **Top Global Matches:** file_cluster_5: 7.693, file_cluster_7: 7.814, file_cluster_12: 7.859
- **Magnitude:** 407.54 | **LOC:** 2160 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (47.1%), Mutation Surface (formerly State Flux) (31.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.5%)
- **Documentation Coverage:** 92.9078% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createJournalWithHeader` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `trimToSizeWithActiveEdit` **(Annotated & Test Methods)** (Impact: 6.0)
    * *Intent:* /** * We had a long-lived bug where [DiskLruCache.trimToSize] could infinite loop if entries * being...
  * `fun` **(Annotated & Test Methods)** (Impact: 6.0)
  * `fun` **(Annotated & Test Methods)** (Impact: 6.0)
  * `evictAllDoesntInterruptPartialRead` **(Annotated & Test Methods)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 179`, `args: 159`, `func_start: 141`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 93`, `state_mutation: 63`, `fragile_debt: 2`, `unreferenced_by_name: 101`
* *Architecture:* `io: 2`, `import: 31`
* *Defense:* `safety: 6`, `doc: 10`, `test: 450`, `sync_locks: 2`, `cleanup: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` app.cash.burst.Burst, assertk.assertThat, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isNull, assertk.assertions.isSameInstanceAs, assertk.assertions.isTrue, assertk.fail...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/EventListenerTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.632)
- **Top Global Matches:** file_cluster_12: 8.632, file_cluster_13: 8.992, file_cluster_0: 9.278
- **Magnitude:** 364.64 | **LOC:** 2538 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **89**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (97.1%), Debt Markers (formerly Tech Debt) (66.3%), Guard Balance (formerly Safety Score) (46.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.5%)
- **Documentation Coverage:** 87.6712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertBytesReadWritten` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `assertSuccessfulEventOrder` **(Stateful Encapsulated Methods)** (Impact: 8.1)
  * `requestBodyMultipleFailuresReportedOnlyOnce` **(Annotated & Test Methods)** (Impact: 5.8)
  * `timeToFirstByte` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* /** * Test to confirm that events are reported at the time they occur and no earlier and no later. *...
  * `aggregateEventListenerIsComplete` **(Annotated & Test Methods)** (Impact: 5.5)
    * *Intent:* /** Reflectively call every event function to confirm it is correctly forwarded. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 630`, `args: 117`, `func_start: 103`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 48`, `duplicate_logic: 2`, `unreferenced_by_name: 70`
* *Architecture:* `io: 3`, `import: 89`
* *Defense:* `safety: 4`, `doc: 9`, `test: 247`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` app.cash.burst.Burst, assertk.all, assertk.assertThat, assertk.assertions.contains, assertk.assertions.containsExactly, assertk.assertions.doesNotContain, assertk.assertions.isEmpty, assertk.assertions.isEqualTo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/HttpOverHttp2Test.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.581)
- **Top Global Matches:** file_cluster_12: 6.581, file_cluster_13: 8.118, file_cluster_15: 8.586
- **Magnitude:** 360.52 | **LOC:** 2169 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **83**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Guard Balance (formerly Safety Score) (45.9%), Mutation Surface (formerly State Flux) (37.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.2%)
- **Documentation Coverage:** 87.8788% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `responseHeadersAfterGoaway` **(I/O & Config Routines)** (Impact: 6.8)
  * `waitForConnectionShutdown` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `countFrames` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `concurrentHttp2ConnectionsDeduplicated` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* /** * We don't know if the connection will support HTTP/2 until after we've connected. When multiple...
  * `firstFrame` **(Stateful Encapsulated Methods)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 215`, `args: 115`, `func_start: 97`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 65`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 11`, `unreferenced_by_name: 64`
* *Architecture:* `io: 2`, `api: 1`, `import: 83`
* *Defense:* `safety: 9`, `doc: 13`, `test: 294`, `sync_locks: 3`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` app.cash.burst.Burst, app.cash.burst.burstValues, assertk.assertThat, assertk.assertions.contains, assertk.assertions.hasMessage, assertk.assertions.isCloseTo, assertk.assertions.isEqualTo, assertk.assertions.isFalse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cookie.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.695)
- **Top Global Matches:** file_cluster_16: 7.695, file_cluster_4: 8.351, file_cluster_15: 8.404
- **Magnitude:** 358.76 | **LOC:** 735 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 2.102; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.7%)
- **Documentation Coverage:** 70.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `parseExpires` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /** Parse a date as specified in RFC 6265, section 5.1.1. */
  * `dateCharacterOffset` **(Stateful Encapsulated Methods)** (Impact: 21.1)
    * *Intent:* /** * Returns the index of the next date character in `input`, or if `invert` the index * of the nex...
  * `equals` **(Defensive Guards)** (Impact: 16.2)
  * `toString` **(Stateful Encapsulated Methods)** (Impact: 14.7)
    * *Intent:* /** * necessary for `example.com` to match `www.example.com` under RFC 2965. This extra dot is * ign...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 89`, `args: 37`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`
* *Architecture:* `api: 8`, `import: 16`
* *Defense:* `safety: 21`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.102
  * `Choke Point (Betweenness):` 0.000244 | `Ripple Effect (Closeness):` 0.140785
  * `Imports (Out-Degree: 5):` java.util.Calendar, java.util.Date, java.util.GregorianCalendar, java.util.Locale, java.util.regex.Pattern, okhttp3.internal.UTC, okhttp3.internal.canParseAsIpAddress, okhttp3.internal.delimiterOffset...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Stream.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.029)
- **Top Global Matches:** file_cluster_12: 7.029, file_cluster_4: 8.129, file_cluster_16: 8.598
- **Magnitude:** 310.2 | **LOC:** 743 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **20**; blast radius 1.413; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.4%), Connectivity (formerly Api Exposure) (26.6%)
- **Documentation Coverage:** 45.1613% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `receive` **(Many-Argument Workhorses)** (Impact: 16.9)
    * *Intent:* /** * Accept bytes on the connection's reader thread. This function avoids holding locks while it * ...
  * `receiveHeaders` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* /** Accept headers from the network and store them until the client calls [takeHeaders]. */
  * `takeHeaders` **(Defensive Guards)** (Impact: 12.4)
    * *Intent:* /** * Removes and returns the stream's received response headers, blocking if necessary until header...
  * `emitFrame` **(Stateful Encapsulated Methods)** (Impact: 10.0)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.413
  * `Choke Point (Betweenness):` 0.001075 | `Ripple Effect (Closeness):` 0.130527
  * `Imports (Out-Degree: 6):` java.io.EOFException, java.io.IOException, java.io.InterruptedIOException, java.net.SocketTimeoutException, java.util.ArrayDeque, okhttp3.Headers, okhttp3.internal.concurrent.Lockable, okhttp3.internal.concurrent.assertLockNotHeld...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `okhttp-testing-support/src/main/kotlin/okhttp3/testing/PlatformRule.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.088)
- **Top Global Matches:** file_cluster_11: 8.088, file_cluster_15: 8.23, file_cluster_0: 8.318
- **Magnitude:** 303.12 | **LOC:** 516 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **58** in-repo importer(s); it depends on **34**; blast radius 5.237; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.9%), Guard Balance (formerly Safety Score) (50.1%), Complexity Load (formerly Cognitive Load) (25.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.7%)
- **Documentation Coverage:** 89.1304% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.237
  * `Choke Point (Betweenness):` 0.01295 | `Ripple Effect (Closeness):` 0.088721
  * `Imports (Out-Degree: 9):` android.os.Build, com.amazon.corretto.crypto.provider.AmazonCorrettoCryptoProvider, com.amazon.corretto.crypto.provider.SelfTestStatus, java.lang.reflect.Method, java.security.Security, okhttp3.TestUtil, okhttp3.internal.platform.ConscryptPlatform, okhttp3.internal.platform.Jdk8WithJettyBootPlatform...
  * `Imported By (In-Degree: 58):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.717)
- **Top Global Matches:** file_cluster_12: 7.717, file_cluster_16: 8.829, file_cluster_5: 8.947
- **Magnitude:** 293.64 | **LOC:** 627 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **36**; blast radius 4.615; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%), Complexity Load (formerly Cognitive Load) (37.3%)
- **Documentation Coverage:** 70.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `messageDone` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /** * Releases resources held with the request or response of [exchange]. This should be called when...
  * `enterNetworkInterceptorExchange` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* /** * Prepare for a potential trip through all of this call's network interceptors. This prepares to...
  * `callDone` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* /** * Complete this call. This should be called once these properties are all false: * [requestBodyO...
  * `noMoreExchanges` **(Stateful Encapsulated Methods)** (Impact: 9.2)
  * `initExchange` **(Stateful Encapsulated Methods)** (Impact: 8.1)
    * *Intent:* /** Finds a new or pooled connection to carry a forthcoming request and response. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 106`, `args: 35`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 37`
* *Architecture:* `io: 2`, `api: 24`, `import: 36`
* *Defense:* `safety: 21`, `doc: 17`, `test: 5`, `sync_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.615
  * `Choke Point (Betweenness):` 0.042801 | `Ripple Effect (Closeness):` 0.179817
  * `Imports (Out-Degree: 23):` java.io.IOException, java.io.InterruptedIOException, java.lang.ref.WeakReference, java.net.Socket, java.util.concurrent.CopyOnWriteArrayList, java.util.concurrent.ExecutorService, java.util.concurrent.RejectedExecutionException, java.util.concurrent.TimeUnit.MILLISECONDS...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.476)
- **Top Global Matches:** file_cluster_15: 6.476, file_cluster_11: 6.605, file_cluster_16: 7.307
- **Magnitude:** 292.96 | **LOC:** 576 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **57** in-repo importer(s); it depends on **10**; blast radius 4.013; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.5%), Guard Balance (formerly Safety Score) (61.7%), Complexity Load (formerly Cognitive Load) (32.1%)
- **Documentation Coverage:** 32.5301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toString` **(Encapsulated Accessors)** (Impact: 6.0)
  * `chunkedBody` **(Type Conversions)** (Impact: 4.4)
    * *Intent:* /** * Sets the response body to [body], chunked every [maxChunkSize] bytes. */
  * `constructor` **(State Mutators)** (Impact: 2.5)
  * `throttleBody` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* /** * Throttles the request reader and response writer to sleep for the given period after each * se...
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 54`, `args: 43`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `api: 92`, `import: 10`
* *Defense:* `safety: 3`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.013
  * `Choke Point (Betweenness):` 0.006904 | `Ripple Effect (Closeness):` 0.112696
  * `Imports (Out-Degree: 8):` java.util.concurrent.TimeUnit, mockwebserver3.SocketEffect.CloseStream, mockwebserver3.internal.toMockResponseBody, okhttp3.Headers, okhttp3.Headers.Companion.headersOf, okhttp3.WebSocketListener, okhttp3.internal.addHeaderLenient, okhttp3.internal.http2.ErrorCode...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/ws/RealWebSocket.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.992)
- **Top Global Matches:** file_cluster_12: 6.992, file_cluster_5: 9.198, file_cluster_4: 9.771
- **Magnitude:** 286.3 | **LOC:** 703 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **36**; blast radius 1.814; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (34.7%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 72.549% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeOneFrame` **(I/O & Config Routines)** (Impact: 19.3)
    * *Intent:* /** * Attempts to remove a single frame from a queue and send it. This prefers to write urgent pongs...
  * `failWebSocket` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `checkUpgradeSuccess` **(Stateful Encapsulated Methods)** (Impact: 10.1)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.814
  * `Choke Point (Betweenness):` 0.008604 | `Ripple Effect (Closeness):` 0.173834
  * `Imports (Out-Degree: 19):` java.io.IOException, java.net.ProtocolException, java.net.SocketTimeoutException, java.util.ArrayDeque, java.util.Random, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.MILLISECONDS, okhttp3.Call...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/HttpUrlTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.848)
- **Top Global Matches:** file_cluster_13: 7.848, file_cluster_12: 9.194, file_cluster_2: 9.519
- **Magnitude:** 276.54 | **LOC:** 2169 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 1.81; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (33.7%), Mutation Surface (formerly State Flux) (9.7%), Complexity Load (formerly Cognitive Load) (5.4%)
- **Documentation Coverage:** 93.4783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertInvalid` **(Stateful Encapsulated Methods)** (Impact: 7.8)
  * `usernameCharacters` **(Annotated & Test Methods)** (Impact: 3.3)
  * `passwordCharacters` **(Annotated & Test Methods)** (Impact: 3.3)
  * `pathCharacters` **(Annotated & Test Methods)** (Impact: 2.9)
  * `hostnameInPunycodeNfcAndNfd` **(Annotated & Test Methods)** (Impact: 2.6)
    * *Intent:* /** * UTS 46 Validity Criteria: Decoded punycode must be NFC. * * https://www.unicode.org/reports/tr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 161`, `args: 138`, `func_start: 138`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 8`, `planned_debt: 7`, `unreferenced_by_name: 131`
* *Architecture:* `import: 13`
* *Defense:* `doc: 9`, `test: 691`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.81
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.162848
  * `Imports (Out-Degree: 2):` assertk.assertThat, assertk.assertions.containsExactly, assertk.assertions.containsExactlyInAnyOrder, assertk.assertions.hasMessage, assertk.assertions.isEqualTo, assertk.assertions.isNull, kotlin.test.Ignore, kotlin.test.Test...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Cache.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.185)
- **Top Global Matches:** file_cluster_12: 7.185, file_cluster_16: 7.94, file_cluster_13: 8.388
- **Magnitude:** 274.02 | **LOC:** 838 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **35**; blast radius 2.41; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.8%), Guard Balance (formerly Safety Score) (57.4%), Complexity Load (formerly Cognitive Load) (43.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.5%)
- **Documentation Coverage:** 68.3544% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 18.4)
    * *Intent:* * * The file is newline separated. The first two lines are the URL and the request method. Next * is...
  * `writeTo` **(Type Conversions)** (Impact: 9.2)
  * `put` **(Stateful Encapsulated Methods)** (Impact: 8.7)
  * `varyHeaders` **(Stateful Encapsulated Methods)** (Impact: 7.7)
    * *Intent:* /** * Returns the subset of the headers in [requestHeaders] that impact the content of the * respons...
  * `varyFields` **(Stateful Encapsulated Methods)** (Impact: 6.8)
    * *Intent:* /** * Returns the names of the request headers that need to be checked for equality when caching. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 153`, `args: 50`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`
* *Architecture:* `io: 4`, `api: 16`, `import: 35`
* *Defense:* `safety: 10`, `doc: 16`, `sync_locks: 9`, `immutability_locks: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.41
  * `Choke Point (Betweenness):` 0.004313 | `Ripple Effect (Closeness):` 0.132737
  * `Imports (Out-Degree: 13):` java.io.Closeable, java.io.File, java.io.Flushable, java.io.IOException, java.security.cert.Certificate, java.security.cert.CertificateEncodingException, java.security.cert.CertificateException, java.security.cert.CertificateFactory...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `okhttp-logging-interceptor/src/main/kotlin/okhttp3/logging/HttpLoggingInterceptor.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.214)
- **Top Global Matches:** file_cluster_6: 7.214, file_cluster_4: 10.803, file_cluster_8: 15.864
- **Magnitude:** 248.84 | **LOC:** 371 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **16**; blast radius 1.013; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Guard Balance (formerly Safety Score) (56.9%), Complexity Load (formerly Cognitive Load) (48.9%), Connectivity (formerly Api Exposure) (16.7%)
- **Documentation Coverage:** 56.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 94.1)
  * `intercept` **(Compute Cores)** (Impact: 70.6)
  * `redactUrl` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `logHeader` **(Encapsulated Accessors)** (Impact: 5.5)
  * `bodyHasUnknownEncoding` **(Encapsulated Accessors)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 46`, `args: 14`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `io: 2`, `api: 7`, `import: 16`
* *Defense:* `safety: 2`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.013
  * `Choke Point (Betweenness):` 0.000966 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 11):` java.io.IOException, java.nio.charset.Charset, java.util.TreeSet, java.util.concurrent.TimeUnit, okhttp3.Headers, okhttp3.HttpUrl, okhttp3.Interceptor, okhttp3.OkHttpClient...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/InterceptorOverridesTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.489)
- **Top Global Matches:** file_cluster_0: 7.489, file_cluster_12: 8.391, file_cluster_15: 8.478
- **Magnitude:** 242.88 | **LOC:** 874 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 97.1698% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testOverrideBadImplementation` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* /** * Test that if we set a bad implementation on the OkHttpClient directly, that we can avoid the f...
  * `overrideBadImplementation` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `testOverrideInApplicationInterceptor` **(Many-Argument Workhorses)** (Impact: 8.1)
    * *Intent:* /** * Test that we can override in a Application Interceptor, purely by seeing that the chain report...
  * `testApplicationInterceptor` **(Generic / Templated Code)** (Impact: 5.0)
  * `secureConnectEnd` **(Compute Cores)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 194`, `args: 117`, `func_start: 105`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`, `planned_debt: 11`, `duplicate_logic: 6`, `unreferenced_by_name: 14`
* *Architecture:* `io: 41`, `import: 46`
* *Defense:* `safety: 3`, `doc: 3`, `test: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` app.cash.burst.Burst, app.cash.burst.burstValues, assertk.assertFailure, assertk.assertThat, assertk.assertions.hasMessage, assertk.assertions.isFailure, assertk.assertions.isFalse, assertk.assertions.isNotSameInstanceAs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.428)
- **Top Global Matches:** file_cluster_12: 7.428, file_cluster_16: 7.451, file_cluster_15: 7.74
- **Magnitude:** 241.04 | **LOC:** 606 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **34**; blast radius 0.762; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.6%), Guard Balance (formerly Safety Score) (54.5%), Debt Markers (formerly Tech Debt) (35.7%)
- **Documentation Coverage:** 78.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSettings` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `nextFrame` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `readHeaders` **(Stateful Encapsulated Methods)** (Impact: 12.3)
  * `readData` **(Stateful Encapsulated Methods)** (Impact: 12.3)
  * `readGoAway` **(Stateful Encapsulated Methods)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 102`, `args: 31`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `planned_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 34`
* *Defense:* `safety: 3`, `doc: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.00108 | `Ripple Effect (Closeness):` 0.104089
  * `Imports (Out-Degree: 6):` java.io.Closeable, java.io.EOFException, java.io.IOException, java.util.logging.Level.FINE, java.util.logging.Logger, okhttp3.internal.and, okhttp3.internal.format, okhttp3.internal.http2.Http2.CONNECTION_PREFACE...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/Http2ConnectionTest.kt` (KOTLIN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.386)
- **Top Global Matches:** file_cluster_13: 7.386, file_cluster_12: 8.021, file_cluster_15: 8.534
- **Magnitude:** 240.88 | **LOC:** 2079 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (80.5%), Guard Balance (formerly Safety Score) (40.2%), Mutation Surface (formerly State Flux) (17.3%), Complexity Load (formerly Cognitive Load) (6.3%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readSendsWindowUpdate` **(I/O & Config Routines)** (Impact: 6.5)
  * `readSendsWindowUpdateHttp2` **(I/O & Config Routines)** (Impact: 6.4)
  * `sendGoAway` **(Annotated & Test Methods)** (Impact: 3.5)
  * `blockedStreamDoesntStarveNewStream` **(I/O & Config Routines)** (Impact: 3.5)
  * `discardedDataFramesAreCounted` **(Annotated & Test Methods)** (Impact: 3.3)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` assertk.assertThat, assertk.assertions.contains, assertk.assertions.hasSize, assertk.assertions.isCloseTo, assertk.assertions.isEqualTo, assertk.assertions.isFalse, assertk.assertions.isGreaterThan, assertk.assertions.isLessThan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `okhttp-hpacktests/src/test/java/okhttp3/internal/http2/hpackjson/Story.kt` (KOTLIN) | Magnitude: 3.64 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, class_start: 2, branch: 1
- `okhttp/src/jvmTest/kotlin/okhttp3/KotlinSourceModernTest.kt` (KOTLIN) | Magnitude: 557.94 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1207, core_var_decl: 517, structural_boundaries: 257, state_mutation: 257
- `okhttp-testing-support/src/main/kotlin/okhttp3/internal/RecordingOkAuthenticator.kt` (KOTLIN) | Magnitude: 26.26 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 16, branch: 6, import: 5
- `mockwebserver/src/main/kotlin/mockwebserver3/RecordedRequest.kt` (KOTLIN) | Magnitude: 17.6 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: api: 16, indent_spaces: 16, doc: 14, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `build-logic/src/main/kotlin/AlpnVersions.kt` (KOTLIN) | Magnitude: 9.22 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 5, branch: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `samples/guide/src/main/java/okhttp3/recipes/kt/UploadProgress.kt` (KOTLIN) | Magnitude: 52.8 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 31, core_var_decl: 15, import: 11
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/DeprecationBridge.kt` (KOTLIN) | Magnitude: 32.4 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 106, core_var_decl: 24, structural_boundaries: 19, design_snake_case: 13
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/ConnectionPool.kt` (KOTLIN) | Magnitude: 22.1 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 47, core_var_decl: 26, design_camel_case: 15, design_pascal_case: 11
- `okhttp-testing-support/src/main/kotlin/okhttp3/UppercaseResponseInterceptor.kt` (KOTLIN) | Magnitude: 13.24 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 20, import: 6, args: 5
- `okhttp-testing-support/src/main/kotlin/okhttp3/ForwardingRequestBody.kt` (KOTLIN) | Magnitude: 9.74 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, func_start: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `build-logic/src/main/kotlin/Osgi.kt` (KOTLIN) | Magnitude: 9.54 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 18, import: 12, core_var_decl: 9
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Reader.kt` (KOTLIN) | Magnitude: 241.04 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 394, structural_boundaries: 102, core_var_decl: 59, branch: 57
- `mockwebserver/src/test/java/mockwebserver3/MockWebServerTest.kt` (KOTLIN) | Magnitude: 134.24 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 773, test: 155, core_var_decl: 135, structural_boundaries: 119
- `samples/guide/src/main/java/okhttp3/recipes/Authenticate.java` (JAVA) | Magnitude: 14.62 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, import: 5, args: 4
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/concurrent/TaskQueue.kt` (KOTLIN) | Magnitude: 86.1 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 30, core_var_decl: 23, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `okhttp-tls/src/test/java/okhttp3/tls/internal/der/DerCertificatesTest.kt` (KOTLIN) | Magnitude: 134.52 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 966, core_var_decl: 298, design_snake_case: 181, design_camel_case: 115
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/publicsuffix/ResourcePublicSuffixList.kt` (KOTLIN) | Magnitude: 2.72 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, import: 4, core_var_decl: 4
- `okhttp-coroutines/src/test/kotlin/okhttp3/coroutines/ExecuteAsyncTest.kt` (KOTLIN) | Magnitude: 33.2 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 50, import: 34, core_var_decl: 14
- `mockwebserver-deprecated/src/main/kotlin/okhttp3/mockwebserver/Dispatcher.kt` (KOTLIN) | Magnitude: 4.84 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 3, func_start: 3
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Route.kt` (KOTLIN) | Magnitude: 37.38 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 67, core_var_decl: 20, structural_boundaries: 15, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `fuzzing/fuzzingserver-test.sh` (SHELL) | Magnitude: 12.8 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 17, io: 7, indent_spaces: 4, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/BaseTestHandler.kt` (KOTLIN) | Magnitude: 27.84 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 16, args: 11, func_start: 11
- `samples/guide/src/main/java/okhttp3/recipes/UploadProgress.java` (JAVA) | Magnitude: 65.0 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 41, core_var_decl: 13, import: 12
- `samples/guide/src/main/java/okhttp3/recipes/CheckHandshake.java` (JAVA) | Magnitude: 13.6 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 23, import: 9, core_var_decl: 6
- `mockwebserver/src/main/kotlin/mockwebserver3/MockResponse.kt` (KOTLIN) | Magnitude: 292.96 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 398, state_mutation: 111, api: 92, core_var_decl: 71
- `okhttp-sse/src/main/kotlin/okhttp3/sse/internal/RealEventSource.kt` (KOTLIN) | Magnitude: 40.6 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 27, branch: 11, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http1/Http1ExchangeCodec.kt` (KOTLIN) | Magnitude: 199.28 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 398, structural_boundaries: 102, core_var_decl: 62, encapsulation: 51
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/internal.kt` (KOTLIN) | Magnitude: 53.28 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 30, import: 17, encapsulation: 16
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilCommon.kt` (KOTLIN) | Magnitude: 187.58 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 92, branch: 51, core_var_decl: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `android-test/src/androidDeviceTest/java/okhttp/android/test/letsencrypt/LetsEncryptClientTest.kt` (KOTLIN) | Magnitude: 13.0 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 14, import: 11, core_var_decl: 6
- `okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/TestDohMain.kt` (KOTLIN) | Magnitude: 24.12 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 82, core_var_decl: 28, design_camel_case: 17, structural_boundaries: 15
- `.github/workflows/build.yml` (YAML) | Magnitude: 55.02 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 345, args: 51, import: 51, structural_boundaries: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `okhttp/src/jvmTest/kotlin/okhttp3/RecordingExecutor.kt` (KOTLIN) | Magnitude: 24.68 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, core_var_decl: 9, args: 8
- `okhttp/src/jvmTest/kotlin/okhttp3/internal/cache/DiskLruCacheTest.kt` (KOTLIN) | Magnitude: 407.54 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1714, test: 450, structural_boundaries: 179, args: 159

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `okhttp-testing-support/src/test/kotlin/okhttp3/OkHttpClientTestRuleTest.kt` (KOTLIN) | Magnitude: 4.14 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, import: 7, args: 4
- `mockwebserver-junit5/src/main/java9/module-info.java` (JAVA) | Magnitude: 12.6 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 2, safety_bypasses: 1, decorators: 1
- `okhttp-brotli/src/main/java9/module-info.java` (JAVA) | Magnitude: 12.6 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 2, safety_bypasses: 1, decorators: 1
- `okhttp-coroutines/src/main/java9/module-info.java` (JAVA) | Magnitude: 12.6 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 2, safety_bypasses: 1, decorators: 1
- `okhttp-dnsoverhttps/src/main/java9/module-info.java` (JAVA) | Magnitude: 12.6 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 2, safety_bypasses: 1, decorators: 1

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt` -> Churn: **63.3%** | Cog Load: 5.7085% | Debt: 97.409%
- `build-logic/src/main/kotlin/okhttp.publish-conventions.gradle.kts` -> Churn: **54.64%** | Cog Load: 62.9346% | Debt: 0.0%
- `gradlew` -> Churn: **50.07%** | Cog Load: 55.8629% | Debt: 26.3198%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 926.74
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 683.4
- `mockwebserver/src/main/kotlin/mockwebserver3/MockWebServer.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 561.34
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/cache/DiskLruCache.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 481.6
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/http2/Http2Connection.kt` -> **renovate[bot]** (100.0% isolated ownership) | Magnitude: 421.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 4.516** (Bridge: 0.0452 * Flux: 99.986%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealCall.kt` -> **Severity: 4.266** (Bridge: 0.0428 * Flux: 99.6816%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealConnection.kt` -> **Severity: 2.042** (Bridge: 0.0209 * Flux: 97.788%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RouteSelector.kt` -> **Severity: 1.608** (Bridge: 0.0161 * Flux: 99.9813%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/connection/RealRoutePlanner.kt` -> **Severity: 1.512** (Bridge: 0.0182 * Flux: 82.9686%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **Severity: 15.202** (Embedded: 0.2372 * Error Risk: 64.0938%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 15.09** (Embedded: 0.2421 * Error Risk: 62.3389%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilJvm.kt` -> **Severity: 13.231** (Embedded: 0.2498 * Error Risk: 52.9675%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Headers.kt` -> **Severity: 13.117** (Embedded: 0.2348 * Error Risk: 55.8584%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/Response.kt` -> **Severity: 12.422** (Embedded: 0.2247 * Error Risk: 55.2761%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilCommon.kt` -> **Severity: 2144.157** (Blast Radius: 40.873 * Doc Risk: 52.459%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-HeadersCommon.kt` -> **Severity: 1732.741** (Blast Radius: 21.528 * Doc Risk: 80.4878%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/HttpUrl.kt` -> **Severity: 1494.361** (Blast Radius: 25.149 * Doc Risk: 59.4203%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/internal/-UtilJvm.kt` -> **Severity: 1463.605** (Blast Radius: 35.777 * Doc Risk: 40.9091%)
- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/OkHttpClient.kt` -> **Severity: 1137.398** (Blast Radius: 19.476 * Doc Risk: 58.4%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 266 literal sites + 31 sites through wrappers = 297
- **`panics_and_aborts`:** 1936 literal sites + 286 sites through wrappers = 2222

- `get` (function, panics_and_aborts, primitive): 144 call sites in 1 files -- `okhttp/src/jvmTest/kotlin/okhttp3/CacheTest.kt`
- `printEvent` (function, debug_prints, primitive): 25 call sites in 1 files -- `samples/guide/src/main/java/okhttp3/recipes/PrintEvents.java`
- `pin` (function, panics_and_aborts, primitive): 13 call sites in 6 files -- `okhttp/src/commonJvmAndroid/kotlin/okhttp3/CertificatePinner.kt`
- `bodyToHex` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `okhttp/src/jvmTest/kotlin/okhttp3/RequestTest.kt`
- `assumeNetwork` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `android-test/src/androidDeviceTest/java/okhttp/android/test/OkHttpTest.kt`
- `getByIp` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/DohProviders.kt`
- `literalHeaders` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `okhttp/src/jvmTest/kotlin/okhttp3/internal/http2/Http2Test.kt`
- `headersToList` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `mockwebserver/src/test/java/mockwebserver3/MockWebServerTest.kt`
- `configureSocket` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSSLSocketFactory.kt`
- `gzip` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `okhttp/src/jvmTest/kotlin/okhttp3/URLConnectionTest.kt`
- `log` (function, debug_prints, primitive): 6 call sites in 1 files -- `okhttp-testing-support/src/main/kotlin/okhttp3/okio/LoggingFilesystem.kt`
- `configureSocket` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `okhttp-testing-support/src/main/kotlin/okhttp3/DelegatingSocketFactory.kt`
*(+33 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 35641 call pairs -- scoped 37.6%, unique 1.4%, ambiguous 26.1%, external 34.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| kotlin | 34559 | 37.3% | 1.4% | 26.0% | 35.3% |
| java | 1018 | 47.3% | 0.9% | 29.7% | 22.1% |
| shell | 64 | 25.0% | 0.0% | 0.0% | 75.0% |

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
